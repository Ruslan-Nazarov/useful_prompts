# Prompt: Build the convert Desktop Document Converter

[Русский](PROMPT.md)

You are an expert desktop application engineer specializing in Python and Qt 6 (PySide6). Create a complete, self-contained, offline Windows application in Windows 11 Fluent Design style named `convert`. Always spell the application name `convert`, strictly in lowercase.

First, thoroughly read [SPEC.en.md](SPEC.en.md), [FEATURES.en.md](FEATURES.en.md), [VISUAL.en.md](VISUAL.en.md), and [reference/design-tokens.json](reference/design-tokens.json). The specification file defines formats, architecture, and data pipelines; FEATURES describes 36 strict behavioral and reliability requirements; VISUAL provides exact colors, typography, layout geometry, and UI tokens. Do not substitute this assignment with a 1-screen toy prototype: implement the full production architecture from document queues and live previews to PDF manipulation tools, telemetry, and shell integration.

---

## 1. Core Application Capabilities

The application provides fast, secure, and offline document processing without internet access and without requiring Microsoft Office or Word to be installed.

Implement the following core modules:

1. **Conversion Queue (8 Directions)**:
   - `DjVu → PDF` (raster page export via bundled native `ddjvu`);
   - `PDF → DjVu` (preserves text and bookmarks via `pdf2djvu` with a reliable fallback to `PyMuPDF` + `c44` + `djvm`);
   - `PDF → DOCX` (reconstructs paragraphs, tables, and images via `pdf2docx` inside an isolated worker process);
   - `DOCX → PDF` (offline layout export using `python-docx` + `ReportLab` using Segoe UI, Arial, Times New Roman);
   - `FB2 → DOCX` and `FB2 → PDF` (XML parser extracting chapters, footnotes, and decoding embedded `base64` art);
   - `EPUB → DOCX` and `EPUB → PDF` (parses OPF manifest, XHTML spine chapters, and illustrations).
2. **Intelligent Settings and Live Preview**:
   - Automatic route selection when dropping files onto the window, preserving explicit user selections (e.g. `FB2 → DOCX`).
   - Live thumbnail preview panel: renders page 1 for PDF and EPUB; extracts embedded cover art for FB2; provides metadata (dimensions, page count, file size).
   - DPI selector (`150`, `300`, `400`, `600`) and quality profiles ("Компактное", "Сбалансированное", "Максимальное").
3. **PDF Tools Suite**:
   - **Merge**: combines multiple PDF documents while merging bookmark trees.
   - **Split**: page-by-page burst or page range extraction (`1-3, 5, 8-10`).
   - **Images to PDF**: builds a single PDF from images (JPG/PNG/WEBP/BMP/TIFF) with aspect ratio fitting (A4 or original size).
   - **Compress**: safe re-encoding of raster XObjects into JPEG with proper `/Filter` and `/ColorSpace` dictionary updates, skipping images with alpha masks.
4. **Atomic Safe Write and Drive Safety**:
   - Never leaves corrupt or 0-byte files: all processing renders to temporary storage before atomic commit.
   - Cross-Volume Drive Handling (Windows `WinError 17`): when `%TEMP%` on `C:` and target folder on `D:` differ, commits through a local staging sibling file in the target directory.
   - Non-destructive naming: automatically increments `_2`, `_3` suffixes if a destination file exists and overwrite is not selected.
5. **Local Telemetry and Albert / ProcessDock Integration**:
   - Local SQLite telemetry database (`%LOCALAPPDATA%\ConvertApp\stats.db`): launch count, data volume, saved storage space, operation log.
   - CLI telemetry pipe for Albert launcher: `--stats` outputs live JSON metrics to `stdout`.
   - Continuous JSON report synchronization to `%LOCALAPPDATA%\ConvertApp\albert_telemetry.json` and ProcessDock bridge files.
6. **Windows Explorer Context Menu Integration**:
   - Registers context menu entries under current user registry hive (`HKCU\Software\Classes\SystemFileAssociations`).
   - Requires zero administrator privileges or UAC elevation; toggleable with one click in settings.

---

## 2. Interaction and Interface Ergonomics

Fulfill the requirements from [FEATURES.en.md](FEATURES.en.md) and [VISUAL.en.md](VISUAL.en.md):

- Interface crafted in Windows 11 Fluent Design style: clean canvas `#F3F4F8`, white 12 px rounded cards, brand violet `#5D46E2`, clear status badges.
- All CPU-bound tasks execute on background `QThreadPool` / `QRunnable` workers with real-time progress feedback. The main Qt GUI thread never freezes.
- Queue mutation protection: row removal and clearing are locked while conversion is in flight.
- "Отменить" (Cancel) button immediately terminates tasks and cleans up scratch files.
- Double-clicking rows or using the context menu allows immediate opening of completed files or inspecting detailed error traces.
- Includes a `start.cmd` launcher script that forwards dragged files (`%*`) directly into the app.

---

## 3. Implementation Order

1. **Core Engines (`converter.py`, `worker.py`, `docx_export.py`, `ebook_export.py`)**:
   - Implement cross-volume atomic `safe_write`.
   - Setup subprocess worker for Word conversion without MS Office.
   - Write FB2 and EPUB structural parsers.
2. **PDF Tools Suite (`pdf_tools.py`)**:
   - Implement `merge_pdfs`, `split_pdf`, `images_to_pdf`, and safe `compress_pdf` using PyMuPDF.
3. **Data Pipelines (`stats_manager.py`, `telemetry.py`, `shell_integration.py`)**:
   - Configure SQLite metrics, JSON export for Albert, and HKCU registry integration.
4. **User Interface (`gui_qt.py`)**:
   - Build PySide6 window with navigation sidebar (Converter, PDF Tools, Statistics).
   - Wire `QThreadPool`, signals, Drag & Drop, and live previews.
5. **CLI and Portability (`app.py`, `build.py`, `start.cmd`)**:
   - Add CLI dispatching (`--stats`, `--worker`, `--self-check`).
   - Setup PyInstaller bundling with native tool integrity checks.
