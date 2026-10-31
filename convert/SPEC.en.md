# Technical Specification: convert Document Converter

[Русский](SPEC.md)

Implement a self-contained, local Windows desktop application according to this specification, [FEATURES.en.md](FEATURES.en.md), and [VISUAL.en.md](VISUAL.en.md). The application is built for converting between PDF, DjVu, DOCX, FB2, and EPUB formats, as well as standalone PDF page manipulation and compression.
The application name is always written in lowercase: `convert`.

---

## 1. General Principles and Architecture

1. **100% Offline and Zero External Office Dependency**:
   - The application functions entirely offline without internet connectivity.
   - Conversions between `DOCX → PDF` and `PDF → DOCX` operate without Microsoft Office, Word, or LibreOffice, utilizing lightweight pure Python / C libraries (`python-docx`, `ReportLab`, `pdf2docx`, `PyMuPDF`).
2. **Subprocess Worker Isolation**:
   - Heavy Office conversions (`PDF → DOCX` and `DOCX → PDF`) run inside an isolated subprocess (`--worker`). This protects the main Qt GUI process from crashes or native library memory issues.
   - Inter-process cancellation is handled cooperatively via a signal file (`cancel_file`) polled between page rendering cycles.
3. **Atomic Safe Write**:
   - All intermediate rendering output is created in temporary scratch storage.
   - Output publication is strictly atomic. User cancellations or runtime failures never leave partial, corrupt, or 0-byte files in the target directory.
   - Cross-Volume Move (`WinError 17` on Windows) is fully supported: if scratch space and destination folder reside on different drive letters (e.g. `C:` and `D:`), the write transitions through a sibling staging file in the target directory before atomic replacement.
   - Non-clobber protection: if a file already exists and overwrite is not selected, the system auto-increments suffixes (`_2`, `_3`, etc.).
4. **Non-Blocking Multithreading**:
   - No CPU-bound conversion or analysis task blocks the Qt event loop. Background work executes inside `QThreadPool` via `QRunnable` worker tasks with granular signal emissions.

---

## 2. Supported Conversion Routes

| Route | Engine | Behavioral Guarantees |
|---|---|---|
| **DjVu → PDF** | Native `ddjvu` utility | Pages render as crisp raster images preserving source DPI. Text layer is omitted. |
| **PDF → DjVu** | Native `pdf2djvu` (fallback: `c44` + `djvm`) | Preserves accessible text layer, hyperlinks, and bookmark outlines. If `pdf2djvu` fails, automatically falls back to page-by-page `c44` encoding and multi-page `djvm` assembly. |
| **PDF → DOCX** | `pdf2docx` + `PyMuPDF` | Reconstructs paragraphs, text blocks, columns, tables, and embedded images. Scanned pages remain images (no OCR required). |
| **DOCX → PDF** | `python-docx` + `ReportLab` | Lightweight offline export: typography, styles, tables, page breaks, embedded illustrations, and Windows system fonts (Segoe UI, Arial, Times New Roman). Warns on complex embedded charts. |
| **FB2 → DOCX** | `xml.etree.ElementTree` + `python-docx` | Parses chapters, titles, paragraphs, footnotes, and decodes embedded `base64` illustrations. |
| **FB2 → PDF** | Two-stage pipeline (`FB2 → DOCX → PDF`) | Full book export into a printable PDF with consistent formatting. |
| **EPUB → DOCX** | `zipfile` + OPF manifest / spine + `python-docx` | Traverses chapter items in manifest order, strips HTML tags cleanly, and embeds illustrations. |
| **EPUB → PDF** | Two-stage pipeline (`EPUB → DOCX → PDF`) | Direct printable PDF preserving book structure and cover art. |

---

## 3. PDF Tools Suite

All tools operate through high-performance `PyMuPDF` (`fitz`):

1. **Merge PDFs**:
   - Joins two or more PDF documents into a unified output file.
   - Preserves and merges table-of-contents bookmark trees from all source documents.
   - Deflates uncompressed streams and purges unreferenced objects (`garbage=4`, `deflate=True`).
2. **Split PDF**:
   - Single page mode: dumps every page into `{stem}_page_001.pdf`.
   - Range mode: parses input strings such as `1-3, 5, 8-12` with bounds clamping and deduplication.
3. **Images to PDF**:
   - Converts multiple raster images (JPG, PNG, WEBP, BMP, TIFF) into a unified PDF.
   - Page geometry options: "Original Image Dimensions", "A4 Portrait" (595 × 842 pt), "A4 Landscape" (842 × 595 pt).
   - Preserves image aspect ratios (`keep_proportion=True`).
4. **Compress and Optimize PDF**:
   - Compression profiles: "Compact" (144 DPI, JPEG quality 65), "Balanced" (200 DPI, JPEG quality 80), "High Quality" (300 DPI, JPEG quality 90).
   - Safe XObject re-encoding: if an image compresses by >12%, replaces the byte stream and updates object dictionary keys (`/Filter /DCTDecode`, `/ColorSpace /DeviceRGB`), nullifying `/DecodeParms`.
   - Never breaks alpha channels: images with transparency or soft masks (`SMask`) are safely bypassed.
   - Deep cleaning of unused fonts and garbage streams via PyMuPDF save flags.

---

## 4. Statistics and Telemetry Storage

1. **SQLite Database**:
   - Database location: `%LOCALAPPDATA%\ConvertApp\stats.db` (or `~/.convertapp/stats.db` on non-Windows hosts).
   - `meta` table: tracks total application runs (`launch_count`), initial launch, and latest launch epoch timestamps.
   - `operations` table:
     - `id`: autoincrement primary key;
     - `session_id`: session identifier formatted as `sess_{timestamp}_{pid}`;
     - `operation`: action name (`convert`, `merge`, `split`, `images_to_pdf`, `compress`);
     - `source_format`, `target_format`: lowercase format strings;
     - `source_size`, `target_size`: sizes in bytes;
     - `duration_sec`: wall-clock duration in seconds;
     - `status`: outcome string (`success`, `error`, `cancelled`);
     - `error_message`: diagnostic detail if failed;
     - `timestamp`: UNIX epoch timestamp.
2. **Albert Launcher Integration**:
   - CLI parameter `--stats`: outputs full JSON metrics payload to `stdout` and exits `0`.
   - CLI parameter `--albert-report <path>`: continuously synchronizes session summary to the specified file.
   - Default report synchronization: `%LOCALAPPDATA%\ConvertApp\albert_telemetry.json`.
3. **ProcessDock Bridge**:
   - When a `.bridge/telemetry` directory exists (or via `ALBERT_BRIDGE_DIR`), every action writes an atomic, non-blocking telemetry event file with a UUID.

---

## 5. Windows Explorer Shell Integration

- Context menu entries are registered in the current user hive `HKEY_CURRENT_USER\Software\Classes` without requiring UAC elevation or administrator privileges.
- Document formats (`.pdf`, `.djvu`, `.djv`, `.docx`, `.fb2`, `.epub`):
  `HKCU\Software\Classes\SystemFileAssociations\{ext}\shell\ConvertApp` labeled "Конвертировать документ (Convert)".
- Image formats (`.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.tiff`):
  labeled "Создать PDF из фото (Convert)".
- Invocation command passes `"%1"` to the compiled binary or `pythonw app.py`.
- Unregistration cleanly prunes all registered keys from HKCU without touching system settings.

---

## 6. Packaging and Portability

- Builds into a standalone directory `dist/Convert` with nested `_internal` via PyInstaller.
- Bundles precompiled native binaries (`ddjvu`, `pdf2djvu`, `c44`, `djvm`) inside `tools/`.
- Build script includes automatic self-verification: runs an automated `PDF → DjVu → PDF` loop via the built executable (`--self-check`) before replacing the production build.
