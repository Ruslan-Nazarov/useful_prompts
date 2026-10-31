# Features and Behavioral Details: convert

[Русский](FEATURES.md)

This catalog complements [SPEC.en.md](SPEC.en.md) and enumerates 36 strict requirements for interface behavior and application reliability. When implementing the application via an AI agent, verify each item against real documents.

---

## 1. Document Queue and UI Interaction

| # | Feature | Behavior and Value |
|---|---|---|
| 1 | **Native Drag & Drop** | Dropping supported files (.pdf, .djvu, .djv, .docx, .fb2, .epub) anywhere onto the window immediately appends them to the queue. |
| 2 | **Queue Deduplication** | Adding a document already present in the queue is silently skipped to prevent redundant rows. |
| 3 | **Intelligent Route Auto-Selection** | Adding `.docx` selects `DOCX → PDF`; adding `.djvu` selects `DjVu → PDF`; if the user previously selected `FB2 → DOCX` or `EPUB → DOCX`, that choice is preserved. |
| 4 | **Live First-Page Thumbnail Preview** | Selecting any row immediately renders a visual thumbnail of the first page (PDF, EPUB) or extracted cover artwork (FB2) in the right-hand preview panel. |
| 5 | **Metadata Card Under Preview** | Displays file name, human-readable file size (KB / MB), total page count, and page dimensions in typographic points (pt). |
| 6 | **Queue Mutation Protection During Processing** | Row removal and queue clearing are disabled while conversion is in progress to prevent index desynchronization. |
| 7 | **Table Context Menu** | Right-clicking a row presents: "Open Result", "Show in Folder", "Show Error Detail" (if failed), and "Remove from List". |
| 8 | **Double-Click Row Action** | Opens the completed document in the system default reader. If the row failed, opens a dialog displaying the full error message. |
| 9 | **Color-Coded Status Feedback** | "✓ Готово" (Done) in green `#059669`, "❌ Ошибка" (Error) in red `#DC2626`, "Отменено" (Cancelled) in amber `#D97706`. |
| 10 | **Detailed Status Tooltip** | Hovering over a status cell reveals the full destination path or the complete exception traceback. |
| 11 | **Quick Action: "Open Result"** | As soon as at least one document succeeds, a prominent green button "📂 Открыть результат" activates in the bottom bar. |
| 12 | **Quick Action: "Show in Folder"** | One-click button to open Windows Explorer highlighting the output file. |

---

## 2. Conversion Robustness and Storage Guarantees

| # | Feature | Behavior and Value |
|---|---|---|
| 13 | **Atomic Safe Write** | Results are rendered into temporary staging directories and only atomically committed upon completion. Partial or corrupt files are never left behind. |
| 14 | **Cross-Volume Drive Handling** | Handles differences in volume letters (e.g. `%TEMP%` on `C:` while saving to `D:`). Catches `WinError 17` and transitions safely through a local sibling staging file. |
| 15 | **Non-Destructive Suffix Auto-Naming** | If an output file already exists, the application generates `_2`, `_3` suffixes instead of blindly overwriting user files. |
| 16 | **Isolated Word/DOCX Worker** | DOCX processing runs inside a detached subprocess. Complex layout errors or native memory leaks never crash the GUI. |
| 17 | **Responsive Cancellation** | Clicking "Отменить" (Cancel) halts processing, purges scratch files, and leaves previously completed files intact. |
| 18 | **Pre-Flight Disk Space Check** | Checks destination free disk space prior to execution (requiring at least double the source file size). |
| 19 | **PDF → DjVu Fallback Engine** | If the native `pdf2djvu` utility encounters an unsupported PDF structure, the engine automatically falls back to `PyMuPDF` + `c44` + `djvm`. |
| 20 | **Password-Protected PDF Handling** | Detects encrypted PDFs and alerts the user with an actionable error message rather than freezing. |

---

## 3. PDF Tools Suite

| # | Feature | Behavior and Value |
|---|---|---|
| 21 | **Asynchronous Tool Execution** | Merging, splitting, compressing, and images-to-PDF run on background worker threads without freezing the UI. |
| 22 | **Outline Preservation on Merge** | Merging preserves and concatenates table-of-contents bookmark trees from all inputs into a single structured tree. |
| 23 | **Flexible Page Range Parsing** | The split tool accepts formats like `1-5, 8, 12-20`, `all`, fixes inverted ranges (`5-1` → `1-5`), and eliminates duplicate page indices. |
| 24 | **Proportional Image Fitting** | Converting photos to A4 PDF preserves aspect ratio without stretching or distortion. |
| 25 | **Safe Raster Stream Optimization** | Compressing PDF re-encodes image streams while properly setting `/Filter /DCTDecode`, `/ColorSpace`, and resetting `/DecodeParms`. |
| 26 | **Alpha Channel and SMask Protection** | Transparent images and soft masks (`SMask`) are bypassed during JPEG recompression, avoiding black artifact boxes around transparent logos. |
| 27 | **Detailed Compression Report** | Displays a summary dialog with initial size, final size, and exact saved percentage. |

---

## 4. Telemetry, Integration, and Settings

| # | Feature | Behavior and Value |
|---|---|---|
| 28 | **Self-Contained SQLite Statistics** | Usage metrics are stored locally in `%LOCALAPPDATA%\ConvertApp\stats.db` without network telemetry. |
| 29 | **Saved Storage Space Metric** | The dashboard aggregates cumulative bytes saved across compression and conversion runs. |
| 30 | **CLI Telemetry for Albert Launcher** | `Convert.exe --stats` outputs a structured JSON payload to `stdout` for launcher dashboards. |
| 31 | **Export Report to JSON** | One-click button to export complete operation history for auditing or backup. |
| 32 | **One-Click Shell Integration** | Enables/disables Windows Explorer context menu directly from settings without administrator rights. |
| 33 | **Clean Non-Duplicated Shell Entries** | Uses targeted `SystemFileAssociations`, preventing duplicate menu entries in Windows Explorer. |
| 34 | **Self-Check Diagnostic Mode (`--self-check`)** | Verifies bundled binary tools through a live conversion loop and outputs a JSON health report. |
| 35 | **Batch File Drag & Drop Forwarding** | Dropping files directly onto `start.cmd` forwards arguments (`%*`) into the running application. |
| 36 | **Clean Graceful Window Shutdown** | Closing the window signals cancellation to active tasks and allows thread pools to drain cleanly. |
