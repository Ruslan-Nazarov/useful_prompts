# What belongs in the demo and public kit

[Русский](PRIVACY.md)

Every record in `demo-data.json` was invented from scratch. Alexey, Marina, Dima,
Atlas, meetings, habits, notes, and experimental metrics are fictional. The
author's personal database is not used as source material. Data stays in Russian
for the Russian-language video; the documentation is bilingual.

The builder takes only allowlisted application file types, a release number,
dependencies, and the license file from the source folder. It does not copy data,
`.env`, Git history, logs, tokens, backups, or analytics templates. Database paths
are overridden to point at a new demo directory. The launcher stops if the paths
do not match. Only system launch parameters are inherited from the parent
environment; API keys are not inherited. Voice and Google Calendar routes are blocked.

The filming copy removes the personal credit line from the footer and replaces
development history with a brief demo entry. It does not request external fonts.
The original application's credits are unchanged. The license remains in the
local source snapshot but is not part of the public prompt kit. Record the demo
window in a separate browser profile; keep personal tabs, source files, license
contents, and absolute local paths out of the recording frame.

Publish using the explicit file-list export:

```powershell
python -B papanda/demo.py export
```

From the original Papanda source root:

```powershell
.\.venv\Scripts\python.exe -B prompt-library/papanda/demo.py export
```

This creates `public-kit.zip` containing instructions, prompts, requirements,
the recording script, fictional data, and launcher scripts. Extract it into an
empty folder for the new repository. Databases, application snapshots, local
manifest paths, and `.demo` are not included. `.gitignore` also excludes local
data, while the allowlist makes publication contents explicit.

`demo.py check` verifies SQLite integrity and links, record counts, absence of
users and calendar connections, and basic HTTP page rendering. It does not inspect
browser tabs, desktop notifications, or other material outside the application.
