# Prompt: build my personal time dashboard

[Русский](PROMPT.md)

You are a software developer. Build a fully functional local, single-user time
management application in this empty folder using the attached SPEC.en.md.
Create an independent implementation inspired by Papanda rather than copying
its source code. Read SPEC.en.md and demo-data.json, then start implementing.

My idea: one screen for my main undertaking, daily schedule, tasks, habits, quick
thoughts, and the record of past days. The example user is an AI developer, but the
application should work for anyone. Use a Russian interface by default to match
the reference video, calm modern styling, readable cards, and few unnecessary
actions. English instructions do not imply an English-only application.

Default stack: Python 3.12+, FastAPI, Jinja2, SQLite, SQLAlchemy, and plain CSS and
JavaScript. If the environment requires another stack, explain the choice and
preserve the functional requirements. Pin dependency versions you actually test.
Separate routes, models, data operations, templates, and client code.

Work in stages:

1. Foundation: virtual environment, server, persistent database, and responsive
   dashboard. Implement the main undertaking, tasks grouped into sets, today's
   and tomorrow's events, and notes. Make creation, editing, and deletion work
   through the interface from the beginning.
2. Add habits, a dated journal, date counters, and note categories. Seed a separate
   demo database with the coherent fictional records in demo-data.json.
3. Add linked sticky notes with checklists, weekly activity reviews, and recurring
   calendar events. Test recurrence rules and individual exceptions separately.
4. Complete search, settings, backup/restore, and accessibility. Verify the workflow
   in SPEC.en.md and write a README with exact launch commands.

At each stage, make existing buttons functional. Do not use clickable placeholders.
Do not claim browser or test verification unless you ran it. If a browser is
unavailable, distinguish automated checks from manual checks. Continue beyond the
plan: implement, run, and fix failures. Ask only genuinely blocking questions;
make reasonable decisions for the rest.

Store the personal database at data/db/app.db. Keep the demo database separate.
A normal launch must not clear or replace records. The demo generator takes an
anchor date, preserves record relationships, and refuses to overwrite an existing
database. Handle displayed dates consistently in the local time zone. Do not put
data, .env files, tokens, or secrets into Git. Back up before migrations.
Do not read personal files, browser profiles, or other user databases to seed the
demo. Use only the attached fictional data and newly invented examples.

Do not add cloud authentication, a required AI API, analytics, or external calendar
connections to the core workflow. Bind the server to 127.0.0.1. Render user content
safely: do not execute HTML or scripts from records. Styling should remain usable
when external fonts are unavailable.

The decisive acceptance check: I open the app, change my daily plan, save a note,
stop the server, restart it, and see my changes. Show the database path, launch
command, checks performed, and remaining limitations.
