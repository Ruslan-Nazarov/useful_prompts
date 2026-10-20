# Build your own personal time dashboard with AI

[Русский](README.md)

The goal is to build your own local application inspired by Papanda: understand
what matters now, plan the day, and review where your time went.

## What you need

- A computer, an editor, and an AI coding agent that can create files and run commands.
- An empty project folder the agent can access.
- For the suggested stack, Python 3.12+ and a browser. The agent creates a virtual
  environment and installs dependencies. Internet access is needed for the agent
  and package installation.
- Copies of [PROMPT.en.md](PROMPT.en.md), [SPEC.en.md](SPEC.en.md), and
  [demo-data.json](demo-data.json) in the project folder.

The application does not require API keys, Google Calendar, or paid hosting.
Your AI agent may require an account and payment under its own terms.

## Build it

1. Open an empty folder in your editor and attach the three files to the agent conversation.
2. Send the entire contents of `PROMPT.en.md`.
3. Let the agent finish and run the first stage, then inspect the application in a browser.
4. Continue through the prompt's stages. When something fails, provide the error
   and the action that caused it. Verify persistence before entering personal data.
5. Complete the acceptance checks in `SPEC.en.md`, restart the server, and confirm
   that your changes remain.

A useful follow-up prompt:

> Continue with the next unfinished stage in SPEC.en.md. First inspect what is
> already implemented. Preserve working features and data, make the changes, run
> appropriate checks, and show the exact launch command.

If the agent stops at a mockup:

> Connect every visible action to persistent storage. Check creation, editing,
> and deletion through the interface, and verify persistence after a restart.
> Do not declare the application complete based on a screenshot alone.

`demo-data.json` describes a fictional AI developer and the Atlas project. All
names and metrics are invented for demonstration; they are not research results.
The fixture intentionally remains in Russian because the video is in Russian.
The agent should adapt it to its own storage schema. Technical model names refer
to the original Papanda implementation.

## For the video author: isolated Papanda demo

This path prepares the existing application for filming. Viewers build their own
application using the prompt above. You need a local Papanda source folder and
Python with its dependencies installed.

The builder copies application code and an explicit set of supporting files.
It does not copy the personal database, `.env`, integrations, or analytics templates.
Voice and Google Calendar routes are disabled, and API keys are not inherited.

From the original Papanda root in PowerShell:

```powershell
.\.venv\Scripts\python.exe -B prompt-library\papanda\demo.py prepare --source .
.\.venv\Scripts\python.exe -B prompt-library\papanda\demo.py check
.\.venv\Scripts\python.exe -B prompt-library\papanda\demo.py run
```

Open [the demo](http://127.0.0.1:8011/). Select Russian using the application menu
if necessary. Stop the server with Ctrl+C. Port 8011 separates the demo address
and browser storage from a usual launch on port 8000. Cookies may be shared across
ports, so a separate browser profile is useful for recording.

After moving the kit to its own repository:

```powershell
# First create an environment and install the Papanda source requirements.txt.
python -B papanda/demo.py prepare --source "D:\path\to\papanda"
python -B papanda/demo.py check
python -B papanda/demo.py run
```

Each `prepare` creates a new take in `papanda/.demo/runs/`. It updates `current.json`
only after successful seeding. Earlier takes are retained. Scenario dates are
relative to the current day in Asia/Qyzylorda. To prepare for a specific date:

```powershell
python -B papanda/demo.py prepare --source "D:\path\to\papanda" --date 2026-10-20
```

This sets the record dates, not the application's clock. For recording on a later
day, prepare another take without `--date` so events appear under Today.
Stop the old server before preparing a new take. `run` never resets the database;
actions performed while recording are saved. Commands print the database path.

See [VIDEO.en.md](VIDEO.en.md) for the recording script,
[FEATURES.en.md](FEATURES.en.md) for 64 small product details, and
[COMPARISON.en.md](COMPARISON.en.md) for the comparison with other products.

For publication, use `demo.py export`. It creates `public-kit.zip` from an explicit
allowlist of public files. Extract the archive into the new repository's empty
folder. See [PRIVACY.en.md](PRIVACY.en.md).
