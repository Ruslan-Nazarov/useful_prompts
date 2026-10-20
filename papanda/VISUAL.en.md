# papanda visual specification

[Русский](VISUAL.md)

Reproduce papanda's appearance alongside SPEC.en.md and FEATURES.en.md. Values
below come from application styles and templates. Follow this concrete appearance
brief rather than inventing a different interface with similarly named sections.

Exact reference files:

- [reference/design-tokens.json](reference/design-tokens.json): CSS variables, colors, fonts, radii, shadows, and component dimensions.
- [reference/default-layout.json](reference/default-layout.json): initial seven-widget geometry.
- [reference/example-layout.json](reference/example-layout.json): populated-example geometry matching `dashboard_layout` in demo-data.json.

These are styling parameters and fictional-example settings, not personal records.

## 1. Overall appearance

Use a warm light `#FFF5EC` page, white rounded cards, soft neutral shadows,
orange `#F2994A` accents, and dark slate text. The main screen is a working card
workspace, without a sidebar, promotional hero, oversized greeting, or landing page.
The application name is `papanda`.

Quick input sits at the top, with small counters, Important, Wink, and a language
selector beside it or on the following row. Movable widgets fill the area below.
The main undertaking belongs inside Tasks rather than a separate oversized banner.
Sticky notes resemble small paper notes inside their own widget.

## 2. Colors and effects

| Role | Value |
|---|---|
| Page | `#FFF5EC` |
| Card | `#FFFFFF` |
| Subtle surface | `#FDFBF9` |
| Primary/active | `#F2994A` |
| Dark accent | `#D87D2D` |
| Soft highlight | `#FFF3E0` |
| Headings | `#1E293B` |
| Body text | `#475569` |
| Secondary text | `#64748B` |
| Faint labels | `#94A3B8` |
| Light/medium border | `#F1F5F9` / `#E2E8F0` |
| Success/error/warning | `#10B981` / `#EF4444` / `#F59E0B` |

Card shadow: `0 10px 25px -5px rgba(0,0,0,.05), 0 8px 10px -6px rgba(0,0,0,.05)`.
Strong shadow: `0 20px 50px -12px rgba(0,0,0,.12)`. Light: `0 2px 4px rgba(0,0,0,.02)`.
Radii: 8, 12, 18, 24 px; cards use 24 px and icon buttons 8 px. Glass surfaces
use white at .85 opacity, 16 px blur, and a white .3 border.

Do not replace the warm background with gray, orange with blue/purple, or white
cards with a dark theme. Additional colors identify events and sticky notes.

## 3. Typography

Use Inter for UI with system fallback (`Segoe UI`, Roboto, sans-serif), Outfit for
heading roles, and Fira Code / JetBrains Mono / Courier New for the editor's
monospace option. Scale: 12, 14, 16, 18, 20, 24, 32 px. Body 16 px with line-height
1.5. Widget titles are 1.1rem (17.6 px at a 16 px root), weight 500; ordinary dialog
headings around 1.15rem. Always support fallback fonts. For close text metrics,
use consistent font files served locally under their licenses.

Avoid promotional-size widget titles. Dates, counts, and secondary labels remain
visually quieter than main content.

## 4. Grid and cards

Center the workspace at a maximum width of 1600 px. Use 12 columns, 45 px rows,
10 px grid margins, 20 px container padding, and 10 px card-wrapper padding.
White cards have 24 px internal padding, a 2 px border, and 24 px radius. Header
bottom spacing is 12 px. Content scrolls inside the card while controls remain accessible.

Layout `x`, `y`, `w`, `h` values are grid units. Use default-layout for a fresh
installation and example-layout with the fictional fixture. Do not shrink text
to fit all seven cards above the fold. User-saved geometry overrides presets.

Default top row: chronology left, notes center, today right; tasks, habits, and
sticky notes below, with a tall activity block on the left. The populated example
puts tasks, today/tomorrow, and notes across the top. These are two saved layouts
of one visual system.

A collapsed widget occupies two rows and retains its title, cloud, and expand
controls. It must not retain an empty 250 px content area.

## 5. Header and controls

Header padding: 12 px vertical, 32 px horizontal; principal gap 24 px. Quick input
is a light group with 18 px radius: a wide text field, 125 px date control, small
Tomorrow, recurrence, category, color, and an orange OK button. Focus adds an
orange border and a soft .15 glow.

Information cards are small white rectangles of consistent height with colored
accents and short labels. Long values truncate within the card; expanded content
reveals the full title. The language control stays within the page.

Widget headers place a section icon and quiet title on the left, compact actions
on the right. Typical icon buttons are 32×32 px with 8 px radius. Cloud navigation
uses a thin outline icon and a white floating menu above the grid. Delete controls
use soft red; ordinary controls do not compete with the primary action. Hover
slightly changes background/border/text, with at most a 1 px lift. Keyboard focus
is visible; touch actions cannot rely on hover.

## 6. Section contents

- **Tasks:** a full-width set selector, then softly orange main/fallback blocks with
  elapsed duration, followed by task rows.
- **Today/tomorrow:** vertical rows and a Tomorrow divider; compact actions on the
  right. Event colors are labels rather than full-widget fills.
- **Habits:** title left, a small pale duration badge right, compact actions.
- **Activities:** set selector and tools, view mode, totals, time intervals and
  activity text, distinct Now/Next markers, expandable weekly review.
- **Notes:** editor hidden by default behind its toggle; pinned items are warm pale
  cards with category, title, preview, and date. Save state is a small dot and the
  formatting toolbar is compact.
- **Sticky notes:** roughly 130×130 px, 10×12 px padding, `#fff9c4` or a chosen
  pastel, 2 px radius, -1.5° rotation, 20 px folded corner, and 12 px gaps. Hover
  straightens and scales to 1.05. Expanded notes are around 400 px wide, at least
  280 px tall, with 32 px padding and no rotation.
- **Chronology:** compact date/count/one-line preview, separated expanded entries,
  month/year groups, and a brief green highlight on the saved entry.

## 7. Dialogs, editors, and states

Ordinary dialogs are white, 90% width up to 600 px, maximum 90vh, radius 24 px,
with `rgba(15,23,42,.65)` overlay. Header padding 20×24 px, body padding 24 px,
close control right, and internal scrolling. Expanded editors, calendars, and
full lists may be wider; ordinary dialogs should not automatically become full-screen.
Keep editor tools visible while text scrolls.

Keyboard operations preserve structure and menus escape card overflow. Provide
explicit loading, empty, error, disabled, hover, and focus states. Failed saves
do not show success colors. Typical transitions are 150–300 ms and dialog entrance
around 180 ms; reduced motion removes unnecessary movement.

## 8. Responsive and visual acceptance

At widths ≤768 px, wrap the header, give text input its own row, place information
cards in two columns, and stack widgets in one column. Header padding becomes
12×16 px and grid padding 10 px. Expanded cards grow with content; hide resize
handles. Collapsed cards have no mandatory empty body height.

Check 390, 768, 1440, and 1920 px at 100% zoom with identical data. Capture your
implementation's overview, cloud menu, editor, sticky note, undertaking/history,
chronology, calendar, and phone layout. Compare tokens and the selected geometry,
then padding, radii, text density, wrapping, and control sizes. Explain differences;
matching section names alone is insufficient. This style-derived specification
does not promise pixel-identical rendering across browsers and font installations.
