# convert — Desktop Document Converter and PDF Master

[Русский](README.md)

Specification kit for building your own standalone document conversion desktop application based on `convert`:
supports DjVu ↔ PDF, PDF ↔ DOCX, DOCX → PDF, FB2 → DOCX/PDF, EPUB → DOCX/PDF, alongside dedicated PDF manipulation tools (merge, split, images-to-PDF, compress). Built in Windows 11 Fluent Design style on PySide6 (Qt 6), operates 100% offline without Microsoft Office or internet dependencies, and includes local telemetry and Windows Explorer integration.

---

## Kit Contents

| File | Description |
|---|---|
| [PROMPT.en.md](PROMPT.en.md) | Primary prompt for AI agent: architectural blueprints, implementation steps, and requirements |
| [SPEC.en.md](SPEC.en.md) | Technical specification: format engines, worker process isolation, atomic safe-write, SQLite schema, Albert CLI |
| [FEATURES.en.md](FEATURES.en.md) | Catalog of 36 interaction & reliability details: Drag & Drop, previews, cross-drive support, PDF Tools |
| [VISUAL.en.md](VISUAL.en.md) | Visual design specification: Fluent Design colors, sidebar, cards, typography, and status feedback |
| [reference/design-tokens.json](reference/design-tokens.json) | Exact numeric and hex values for styling tokens |

---

## Prerequisites

1. A computer running Windows 10/11 x64, a code editor, and an AI coding agent with tool access to read/write files and execute commands.
2. Python 3.12+ (dependencies `PySide6`, `pymupdf`, `python-docx`, `reportlab`, `pdf2docx` installed by the agent).
3. Precompiled native utilities `ddjvu`, `c44`, `djvm` (from DjVuLibre) and `pdf2djvu` (placed in a `tools/` directory).
4. Internet access is only needed by your agent during initial package installation; the resulting desktop application itself runs **100% offline**, requiring zero cloud accounts, external APIs, or Microsoft Office.

---

## How to Build

1. Create an empty directory and copy this specification kit into it (`PROMPT.en.md`, `SPEC.en.md`, `FEATURES.en.md`, `VISUAL.en.md`, and the `reference/` folder).
2. Open the directory in your agentic IDE and send the full text of `PROMPT.en.md`.
3. The agent will read the specifications, draft an architecture plan, and generate the full codebase:
   - conversion core with atomic cross-volume drive handling;
   - isolated worker process for DOCX generation;
   - PyMuPDF tools suite (Merge, Split, Images-to-PDF, Compress);
   - PySide6 graphical user interface;
   - SQLite metrics engine and Windows HKCU shell integration.
4. Launch the application via `python app.py` or the bundled `start.cmd`.
5. Test conversion workflows with sample documents and verify the UI against [VISUAL.en.md](VISUAL.en.md).
6. Verify compliance with the checklist in [FEATURES.en.md](FEATURES.en.md).

---

## Privacy and Safety

This kit contains zero personal data, API keys, secrets, author system paths, or private document snapshots. All technical specifications are generalized and safe for direct public deployment.
