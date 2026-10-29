# DeskTools — local Windows tools

[Русский](README.md)

An assignment kit for an AI coding agent: build your own desktop application
with keyboard and mouse remapping, local OCR, text transformations, and a hotkey
template picker. Supported Razer lighting is a separate capability. The interface
has three sections: Keyboard, Mouse, and Text and OCR.

| File | Purpose |
|---|---|
| [PROMPT.en.md](PROMPT.en.md) | Starting assignment, behavior, and implementation sequence |
| [SPEC.en.md](SPEC.en.md) | Architecture boundaries, data, workflows, and limits |
| [FEATURES.en.md](FEATURES.en.md) | 40 verifiable requirements F01–F40 |
| [VISUAL.en.md](VISUAL.en.md) | Appearance and responsive layout |
| [ACCEPTANCE.en.md](ACCEPTANCE.en.md) | 20 acceptance scenarios A01–A20 |
| [SOURCES.en.md](SOURCES.en.md) | Basis of the kit and third-party resources |
| [reference/design-tokens.json](reference/design-tokens.json) | Colors, typography, and dimensions |
| [demo-data.json](demo-data.json) | Explicitly fictional settings and templates |

Each assignment document has a Russian counterpart. User examples remain in
Russian. The documentation language does not change the default Russian UI.

## Build your application

1. Create an empty folder and copy the entire kit, including `reference/`.
2. Open it in an agent with filesystem and terminal access. Send PROMPT.en.md.
3. The agent reads the other documents and implements the application through acceptance.
4. Start the application using its instructions. Complete ACCEPTANCE.en.md and
   inspect the F01–F40 table: implementation, verification, outcome, and limits.

Target Windows 10/11 with Windows OCR support and installed recognition languages.
Suggested stack: C#/.NET Framework 4.x and WinForms, a compatible compiler, and
Windows PowerShell 5.1. Another stack is acceptable if it implements real global
Windows input rather than a window mockup. Normal operation needs no internet,
API keys, cloud service, or separate driver. The agent and setup of its tools
may require internet access and payment.

Load demonstration data only through an explicit command into a separate profile.
Never replace personal settings. Templates and text bindings are stored in plain
text; do not use a shared project folder for secrets.

## Continue development

> Compare the application with SPEC.en.md, FEATURES.en.md, and VISUAL.en.md.
> Fix omissions and regressions without losing settings. Complete ACCEPTANCE.en.md.
> Record implementation and actual verification for every F/A ID, distinguishing
> engine tests from live Windows input.

The kit defines behavior and appearance; implementations may differ between agents.
HID verification needs the exact supported mouse, and global input verification
needs an interactive Windows desktop. Record missing hardware or desktop access
as a limitation instead of substituting a successful stub.
