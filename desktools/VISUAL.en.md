# DeskTools appearance

[Русский](VISUAL.md)

## Shared system

Use dark side navigation, a neutral light workspace, white flat surfaces, and
compact rectangular actions. Exact values are in `reference/design-tokens.json`.
Card/button corner radius is 0; do not introduce large rounded blocks, gradients,
or decorative shadows.

| Role | Value |
|---|---|
| Canvas / surface | #F7F7F5 / #FFFFFF |
| Sidebar / text | #212420 / #D1D8D2 |
| Selected section / text | #513A24 / #FFB56F, orange left indicator |
| Primary action / hover | #C65300 / #A94400, white text |
| Text / explanation | #272B28 / #636C67 |
| Secondary surface / border | #F2F3F0 / #E1E4DF |
| Selected row | #F7E9DD |
| Focus / error / success | #A94400 / #C43E42 / #198575 |
| Typeface | Segoe UI 14 px; headings 18/24 px bold |
| Button / binding row | 36 px / 32 px |

## Shell

Wide windows have a 208 px left sidebar: name and a small original icon at the
top, three sections, and «Ещё…» at the bottom. The workspace uses 20 px padding,
a section title, a short explanation, and working content. Status/errors remain
accessible at the bottom; long messages wrap.

Below 768 px, navigation moves to the top: name/menu followed by the three
sections in a row. Workspace padding becomes 14 px. Actions wrap and content
scrolls. Long binding tables may scroll horizontally internally, while the
form and primary actions remain accessible.

## Sections and windows

- Keyboard: switch, explanation/count, actions above the table, and columns for
  chord, action, and name. Editing/deletion require selection.
- Mouse: «Кнопки» and «Подсветка» tabs with a flat strip and orange underline.
  Buttons tab has a switch, guidance, and actions above the table. Lighting uses
  labelled native fields, wrapping, and scrolling.
- Text: templates/OCR-hotkey row, then two white blocks. Fields are side by side
  on wide screens and stacked on narrow screens. Source import actions sit above
  its field and transformations below. The result has a count, copy, and insert.
  Both fields are editable.
- Editors: clear labels and an action summary. Keyboard/mouse use two steps and
  conditional parameter fields. Save/cancel and errors remain accessible at the
  bottom; long content scrolls.
- Template picker: approximately 438×540 px, with a border/system close button,
  constrained to the monitor work area. A Ctrl+Alt+T heading, labelled search,
  58 px rows with title/excerpt, full preview, arrow/Enter/Esc guidance, and orange
  Insert action. Selected rows have a soft fill and an orange indicator. This is
  a popup near the insertion point, not a fourth section.

Use native controls or equivalent accessibility. Visible focus, Tab/Shift+Tab,
and arrows must work without a mouse. Explain errors with text, not color alone.
Icons supplement labels. Create an original mark or use licensed resources as
described in SOURCES.en.md.

## Verification

At 390, 768, and 1440 px, check the main window, editors, and picker. Include
long names, multiline text, no selection, empty library/search, storage/insertion
errors, and retained drafts. Separately verify Windows scaling and movement
between monitors with different DPI.
