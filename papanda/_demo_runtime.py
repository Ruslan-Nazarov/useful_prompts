"""Internal child process: all imports use only the isolated source snapshot."""

import argparse
import asyncio
import json
import os
from contextlib import closing
from datetime import date, datetime, time, timedelta
from pathlib import Path


def resolve_dates(value, anchor):
    if isinstance(value, list):
        return [resolve_dates(item, anchor) for item in value]
    if isinstance(value, dict):
        if set(value) == {"$date"}:
            return anchor + timedelta(days=value["$date"])
        if set(value) == {"$datetime"}:
            offset, clock = value["$datetime"]
            return datetime.combine(anchor + timedelta(days=offset), time.fromisoformat(clock))
        return {key: resolve_dates(item, anchor) for key, item in value.items()}
    return value


def checked_root():
    root = Path(os.environ["PAPANDA_DEMO_ROOT"]).resolve()
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    if manifest["kind"] != "papanda-fictional-video-demo":
        raise ValueError("Not a generated demo")
    import fastapi_app
    if Path(fastapi_app.__file__).resolve().parent != root / "app/fastapi_app":
        raise ValueError("Refusing to import a non-demo application")
    from fastapi_app.config import settings
    from fastapi_app.services.maintenance_service import _active_db_path

    if settings.data_dir.resolve() != root / "data":
        raise ValueError("Data directory is not isolated")
    if _active_db_path() != root / "data/db/papanda.db":
        raise ValueError("Database path is not isolated")
    if (root / "app/.env").exists():
        raise ValueError("Demo snapshot must not contain .env")
    return root, manifest


def validate_fixture(tables):
    from fastapi_app.services.event.recurrence_rules import generate_dates_rrule

    for event in tables.get("Event", []):
        if event.get("recurrence_rule") and not generate_dates_rrule(
            event["date"], event["recurrence_rule"], event["recurrence_end"]
        ):
            raise ValueError("Demo recurrence does not produce any occurrences")
    ends = {}
    activities = sorted(
        tables.get("Observation", []), key=lambda row: (row["set_id"], row["created_at"].time())
    )
    for activity in activities:
        start = activity["created_at"].time()
        end = time.fromisoformat(activity["end_time"])
        if start >= end or start < ends.get(activity["set_id"], time.min):
            raise ValueError("Demo activities overlap or have an invalid time interval")
        ends[activity["set_id"]] = end


async def seed(root, manifest):
    from fastapi_app import models
    from fastapi_app.database import close_db, get_session_maker, init_db
    from fastapi_app.services.maintenance_service import _active_db_path

    if _active_db_path().exists():
        raise ValueError("Refusing to overwrite an existing database; prepare a new run")
    fixture = json.loads((root / "demo-data.json").read_text(encoding="utf-8"))
    anchor = date.fromisoformat(manifest["anchor"])
    tables = resolve_dates(fixture["tables"], anchor)
    validate_fixture(tables)
    try:
        await init_db()
        async with get_session_maker()() as db:
            async with db.begin():
                for name, rows in tables.items():
                    model = getattr(models, name)
                    db.add_all([model(**row) for row in rows])
                    # Parent rows precede child rows in the fixture.
                    await db.flush()
    finally:
        await close_db()
    print("Created fictional demo database.", flush=True)


def check(root):
    from fastapi_app.services.maintenance_service import _active_db_path, _readonly_connection

    with closing(_readonly_connection(_active_db_path())) as conn:
        if conn.execute("PRAGMA quick_check").fetchall() != [("ok",)]:
            raise ValueError("Database integrity check failed")
        if conn.execute("PRAGMA foreign_key_check").fetchall():
            raise ValueError("Broken database links")
        fixture = json.loads((root / "demo-data.json").read_text(encoding="utf-8"))
        from fastapi_app import models

        counts = {}
        for name, rows in fixture["tables"].items():
            table = getattr(models, name).__tablename__
            count = conn.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
            if count < len(rows):
                raise ValueError(f"Missing demo rows in {table}: {count} < {len(rows)}")
            counts[table] = count
        for table in ("google_calendar_connection", "google_calendar_event", "users"):
            if conn.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]:
                raise ValueError(f"Unexpected external account data in {table}")
    check_pages()
    print(json.dumps({"checked": "database + HTTP smoke", "rows": counts}, ensure_ascii=False))


def check_pages():
    from fastapi.testclient import TestClient

    app = demo_app()

    with TestClient(app, headers={"Accept-Language": "ru"}) as client:
        for route in ("/", "/settings", "/openapi.json", "/static/css/styles.css"):
            response = client.get(route)
            if response.status_code != 200:
                raise ValueError(f"{route}: HTTP {response.status_code}")
            if route == "/" and "Довести Атлас" not in response.text:
                raise ValueError("Demo focus is missing from dashboard")
            if route in ("/", "/settings"):
                if 'data-demo="fictional"' not in response.text:
                    raise ValueError("Missing demo-only template marker")
                if "fonts.googleapis.com/css" in response.text or "mc.yandex.ru/metrika" in response.text:
                    raise ValueError("External fonts or analytics in demo HTML")
        if client.post("/api/voice/transcribe").status_code != 403:
            raise ValueError("Voice integration must be disabled in filming demo")
        if client.get("/api/google-calendar/status").status_code != 403:
            raise ValueError("Calendar integration must be disabled in filming demo")


def demo_app():
    from fastapi.responses import JSONResponse

    from fastapi_app.main import app

    @app.middleware("http")
    async def block_demo_integrations(request, call_next):
        if request.url.path.startswith(("/api/google-calendar", "/api/voice")):
            return JSONResponse(
                {"detail": "В демоверсии внешние интеграции отключены."}, status_code=403
            )
        return await call_next(request)

    return app


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("seed", "run", "check"))
    parser.add_argument("--port", type=int, default=8011)
    args = parser.parse_args()
    root, manifest = checked_root()
    if args.command == "seed":
        asyncio.run(seed(root, manifest))
        return
    if not (root / "data/db/papanda.db").is_file():
        raise ValueError("Missing demo database")
    if args.command == "check":
        check(root)
    else:
        import uvicorn

        uvicorn.run(demo_app(), host="127.0.0.1", port=args.port, log_level="warning")


if __name__ == "__main__":
    main()
