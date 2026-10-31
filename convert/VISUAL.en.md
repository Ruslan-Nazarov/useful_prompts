# Visual Specification: convert

[Русский](VISUAL.md)

Reproduce the appearance of `convert` in Windows 11 Fluent Design style alongside the behavioral requirements from [SPEC.en.md](SPEC.en.md) and [FEATURES.en.md](FEATURES.en.md). The design is tailored for a modern desktop interface: clean light background, subtle borders, rounded card corners, legible typography, and crisp status feedback.

Exact design tokens are available in [reference/design-tokens.json](reference/design-tokens.json).

---

## 1. Overall Window Layout

- **Window Dimensions**: default 1120 × 780 px, minimum size 920 × 640 px.
- **Main Layout**: two-column layout:
  - Left: fixed vertical navigation sidebar (210 px wide) with a white background `#FFFFFF` and subtle separator `#E2E4EA`.
  - Right: main content area (`QStackedWidget`) on a neutral light background `#F3F4F8`.
- **Title and Branding**: at the top of the sidebar is the application title "Конвертер" (font size 18 px, weight 800, brand color `#5D46E2`).
- **Icon**: document vector icon with blue badge and conversion arrows (`assets/convert.ico`).

---

## 2. Color Palette and Materials

| Element | Color (HEX) | Role |
|---|---|---|
| **Window Background** | `#F3F4F8` | Workspace canvas backdrop |
| **Card Surface** | `#FFFFFF` | White panels with `#E5E7EB` border and 12 px radius |
| **Sidebar Surface** | `#FFFFFF` | Left navigation container |
| **Brand Primary** | `#5D46E2` | Primary buttons, active navigation, logo |
| **Brand Hover** | `#4F39C9` | Hover state for primary action buttons |
| **Active Nav Background** | `#EEECFB` | Soft violet background for selected sidebar button |
| **Primary Text** | `#1F2937` | Headings, document titles, table cell text |
| **Secondary Text** | `#4B5563` | Mode descriptions, input labels |
| **Muted Text** | `#6B7280` | Placeholder tips, counters, inactive descriptions |
| **Success** | `#059669` | Completion status "✓ Готово", green "Open Result" button |
| **Error** | `#DC2626` | Status "❌ Ошибка", error dialogs and tooltips |
| **Warning** | `#D97706` | Status "Отменено" (cancelled), alerts |

---

## 3. Navigation Sidebar

- Vertical button list with left alignment (`text-align: left`) and no standard button borders.
- Button padding: 12 px vertical, 18 px horizontal, 8 px corner radius.
- Normal state: text color `#4B5563`, transparent background.
- Hover state (`:hover`): background `#F3F4F8`, text color `#111827`.
- Selected state (`:checked`): background `#EEECFB`, text color `#5D46E2`, weight 600.
- Navigation tabs:
  1. `📄 Конвертер` (Converter) — primary conversion queue window.
  2. `🛠️ Инструменты PDF` (PDF Tools) — quick cards for standalone PDF utilities.
  3. `📊 Статистика & Albert` (Statistics & Albert) — usage dashboard and launcher integration.

---

## 4. Main "Converter" Tab

### Top Parameter Bar
- White card with 12 px corner radius.
- Conversion mode dropdown: 220 px width, 8 supported directions. Accompanied by descriptive gray text explaining format specifics (e.g. raster pages in DjVu).
- Resolution (DPI) selector: `150`, `300`, `400`, `600`.
- Quality profiles: "Компактное" (compact), "Сбалансированное" (balanced), "Максимальное" (best).

### Queue and Thumbnail Workspace
- Split into two visual zones:
  - Left: document queue table (`QTableWidget`) on white background with `#E5E7EB` grid lines.
    - Columns: `Имя файла` (file name, stretches), `Направление` (mode), `Размер` (source size), `Итог` (output size), `Статус` (status).
    - Row hover: soft gray highlight `#F9FAFB`.
    - Row selection: highlighted row immediately renders its live preview on the right.
  - Right: live preview panel (270 px wide):
    - Thumbnail canvas 250 × 190 px with aspect ratio preservation (`KeepAspectRatio`).
    - Subtitle details: document name, size, page count, and page dimensions in points.
    - Displays extracted cover art for FB2, and rendered first page for EPUB and PDF.

### Bottom Action Bar
- Output destination folder: line edit with "Обзор..." (Browse) button. Default placeholder: "Рядом с исходным файлом" (Next to source file).
- Progress indicator (`QProgressBar`): height 8 px, smooth blue-purple gradient.
- Status bar: textual feedback on the ongoing operation.
- Right action buttons:
  - "Очистить очередь" (Clear queue) — neutral gray button.
  - "Отменить" (Cancel) — cancellation button (enabled only during conversion).
  - "Начать конвертацию" (Start conversion) — large primary accent button `#5D46E2` with bold white text.
  - "📂 Открыть результат" (Open result) — prominent green button (`#059669`) that activates upon successful completion.

---

## 5. "PDF Tools" Tab

- Responsive grid of 4 large tool cards (2 × 2) on white surface with subtle shadow:
  1. **Склейка PDF (Merge)** — combine multiple PDFs with outline preservation.
  2. **Разделение PDF (Split)** — extract page ranges or split into single pages.
  3. **Фотографии в PDF (Images to PDF)** — convert images (JPG/PNG/WEBP/TIFF/BMP) into a single PDF.
  4. **Сжатие и оптимизация (Compress)** — reduce file size safely without degrading text readability.
- Each card features: distinct color icon, bold title (15 px, semibold), 2-line explanation, and an action button at the bottom.

---

## 6. "Statistics & Albert" Tab

- 4 top summary cards:
  - `Запусков приложения` (Application launches)
  - `Обработано файлов` (Processed documents)
  - `Общий объём данных` (Total data volume)
  - `Сэкономлено места` (Saved disk space)
- Operations history table (last 50 operations: timestamp, operation, format, source size, result size, status).
- System integration card:
  - Windows Explorer context menu integration with live status indicator and toggle button.
  - Albert launcher manual sync button and JSON export button.
