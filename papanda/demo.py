"""Build an isolated filming copy of Papanda; never import the working application."""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import uuid
import zipfile
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

KIT = Path(__file__).resolve().parent
DEMO = KIT / ".demo"
EXTENSIONS = {".py", ".html", ".css", ".js", ".json", ".svg", ".png", ".ico",
              ".jpg", ".jpeg", ".webp", ".woff", ".woff2", ".ttf", ".txt", ".md", ".map"}
EXCLUDED = {"__pycache__", "analytics.html", "head_analytics.html"}
PUBLIC_FILES = (
    ".gitignore", "README.md", "papanda/README.md", "papanda/PROMPT.md",
    "papanda/SPEC.md", "papanda/VIDEO.md", "papanda/PRIVACY.md",
    "papanda/FEATURES.md", "papanda/COMPARISON.md",
    "papanda/demo-data.json", "papanda/demo.py", "papanda/_demo_runtime.py",
    "README.en.md", "papanda/README.en.md", "papanda/PROMPT.en.md",
    "papanda/SPEC.en.md", "papanda/VIDEO.en.md", "papanda/PRIVACY.en.md",
    "papanda/FEATURES.en.md", "papanda/COMPARISON.en.md",
)


def sanitize_snapshot(app: Path, source: Path) -> None:
    """Remove personal credits/history from filming UI, retaining the license file."""
    footer = app / "fastapi_app/templates/partials/footer.html"
    text = footer.read_text(encoding="utf-8")
    text = "\n".join(line for line in text.splitlines() if "ui.designed_by" not in line)
    text = re.sub(
        r"\{\{ _\('ui.footer_version'\).*?\}\}",
        "Papanda · демонстрационные данные · {{ release_version }}", text,
    )
    footer.write_text(text, encoding="utf-8")
    base = app / "fastapi_app/templates/base.html"
    text = base.read_text(encoding="utf-8")
    text = re.sub(r'<link\b[^>]*(?:fonts\.googleapis|fonts\.gstatic)[^>]*>', "", text)
    text = text.replace("<body", '<body data-demo="fictional"', 1)
    base.write_text(text, encoding="utf-8")
    # release.py needs only a dated release heading, not private development history.
    changelog = (source / "CHANGELOG.md").read_text(encoding="utf-8")
    release = re.search(r"^## \d+\.\d+\.\d+ \(\d{4}-\d{2}-\d{2}\)$", changelog, re.MULTILINE)
    if release is None:
        raise ValueError("Source changelog has no release heading")
    (app / "CHANGELOG.md").write_text(
        "# Demo\n\n" + release.group() + "\n- Вымышленная демонстрационная база.\n",
        encoding="utf-8",
    )


def export_public() -> Path:
    """Publish an explicit file list; never traverse .demo, environments or databases."""
    output = KIT.parent / "public-kit.zip"
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in PUBLIC_FILES:
            archive.write(KIT.parent / name, name)
    print(f"Public kit: {output} ({len(PUBLIC_FILES)} files; no application or databases)")
    return output


def runtime_env(run: Path, port: int) -> dict[str, str]:
    """Override inherited production paths before the first application import."""
    system_keys = {"PATH", "PATHEXT", "SYSTEMROOT", "SYSTEMDRIVE", "WINDIR",
                   "COMSPEC", "TEMP", "TMP", "LANG", "LC_ALL"}
    env = {key: value for key, value in os.environ.items() if key.upper() in system_keys}
    # Settings names are case-insensitive, including on non-Windows systems.
    overrides = {
        "DATA_DIR": str(run / "data"),
        "DATABASE_URL": "sqlite+aiosqlite:///" + (run / "data/db/papanda.db").as_posix(),
        "ALLOWED_ORIGINS": json.dumps([f"http://127.0.0.1:{port}", f"http://localhost:{port}"]),
        "PYTHONPATH": str(run / "app"),
        "PYTHON_DOTENV_DISABLED": "1",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PAPANDA_ENV": "prod",
        "LOG_LEVEL": "WARNING",
        "OPENAI_API_KEY": "",
        "PAPANDA_DEMO_ROOT": str(run),
    }
    env.update(overrides)
    return env


def invoke(run: Path, command: str, port: int) -> None:
    subprocess.run(
        [sys.executable, "-B", str(KIT / "_demo_runtime.py"), command, "--port", str(port)],
        cwd=run / "app", env=runtime_env(run, port), check=True,
    )


def prepare(source: Path, anchor: date, port: int) -> Path:
    source = source.resolve()
    if not (source / "fastapi_app/main.py").is_file():
        raise ValueError("--source must point to the Papanda source directory")
    for required in ("CHANGELOG.md", "requirements.txt", "LICENSE"):
        if not (source / required).is_file():
            raise ValueError(f"Missing source file: {required}")
    DEMO.mkdir(exist_ok=True)
    run = DEMO / "runs" / f"{anchor.isoformat()}-{uuid.uuid4().hex[:8]}"
    run.mkdir(parents=True, exist_ok=False)
    app = run / "app"
    app.mkdir()
    copied = []
    for original in sorted((source / "fastapi_app").rglob("*")):
        relative = original.relative_to(source)
        if original.is_symlink() or any(part in EXCLUDED for part in relative.parts):
            continue
        if not original.is_file() or original.suffix.lower() not in EXTENSIONS:
            continue
        if source not in original.resolve().parents:
            raise ValueError(f"Source escapes application directory: {relative}")
        target = app / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, target)
        copied.append(relative.as_posix())
    for name in ("CHANGELOG.md", "requirements.txt", "LICENSE"):
        shutil.copyfile(source / name, app / name)
        copied.append(name)
    sanitize_snapshot(app, source)
    shutil.copyfile(KIT / "demo-data.json", run / "demo-data.json")
    manifest = {
        "kind": "papanda-fictional-video-demo", "anchor": anchor.isoformat(),
        "timezone": "Asia/Qyzylorda", "copied_files": copied,
        "ready": False,
    }
    (run / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    invoke(run, "seed", port)
    manifest["ready"] = True
    (run / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    temporary = DEMO / f"current-{uuid.uuid4().hex}.tmp"
    temporary.write_text(json.dumps({"run": str(run)}), encoding="utf-8")
    temporary.replace(DEMO / "current.json")
    print(f"Demo prepared: {run}", flush=True)
    return run


def current_run(path: Path | None) -> Path:
    run = (path or Path(json.loads((DEMO / "current.json").read_text(encoding="utf-8"))["run"])).resolve()
    # Only explicitly generated local runs can be launched, never arbitrary app paths.
    if run.parent != (DEMO / "runs").resolve():
        raise ValueError("Run must be inside this kit's .demo/runs directory")
    manifest = json.loads((run / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("kind") != "papanda-fictional-video-demo" or not manifest.get("ready"):
        raise ValueError("Demo preparation did not complete")
    if not (run / "data/db/papanda.db").is_file():
        raise ValueError("Demo database is missing; prepare a new run")
    return run


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "run", "check", "export"))
    parser.add_argument("--source", type=Path, help="Papanda source directory (prepare only)")
    parser.add_argument("--date", type=date.fromisoformat, dest="anchor")
    parser.add_argument("--port", type=int, default=8011)
    parser.add_argument("--run-dir", type=Path, help="Previously prepared run in this kit")
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        parser.error("--port must be between 1024 and 65535")
    if args.command == "export":
        export_public()
    elif args.command == "prepare":
        if args.source is None:
            parser.error("prepare requires --source")
        anchor = args.anchor or datetime.now(ZoneInfo("Asia/Qyzylorda")).date()
        prepare(args.source, anchor, args.port)
    else:
        run = current_run(args.run_dir)
        print(f"Demo database: {run / 'data/db/papanda.db'}", flush=True)
        if args.command == "run":
            print(f"Open http://127.0.0.1:{args.port}/ — Ctrl+C to stop", flush=True)
        invoke(run, args.command, args.port)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"Demo error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
