# Build your own personal time dashboard with AI

[Русский](README.md)

The goal is to build your own local application inspired by papanda: understand
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
The example fixture is in Russian; use it as sample content when building your own app.
The agent should adapt it to its own storage schema. Technical model names refer
to the original papanda implementation.
