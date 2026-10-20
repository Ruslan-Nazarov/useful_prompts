# Specification: the papanda time management app

[Русский](SPEC.md)

Build an independent local application using this specification,
[FEATURES.en.md](FEATURES.en.md), and [VISUAL.en.md](VISUAL.en.md). They jointly
define core functionality, 64 interactions, and appearance. Always spell `papanda`
in lowercase.

## 1. Workspace

One installation, one user, a local SQLite database, and browser access. Core
workflows require no account, internet, AI API, or external calendar. Seven widgets
cover chronology, activities, notes, today/tomorrow, tasks with the main/fallback
undertakings, habits, and sticky notes.

Use a 12-column movable/resizable grid with per-widget collapse, border colors,
and visibility. Persist geometry, collapsed state, and expanded height without
shifting neighbors on reload. Use one column on phones. Every widget has cloud
navigation listing enabled sections; a jump expands, scrolls to, focuses, and
highlights its destination. Menus escape card clipping and support mouse, touch,
and keyboard. Widget headers open each section's full view.

## 2. Main undertaking, fallback, and tasks

Each undertaking stores kind, title, start, creation, and a note. Calculate calendar
elapsed duration and expose years/months/days plus total months/days/hours. Editing
a title preserves creation time. Completing one preserves a history snapshot and
moves all attached sticky notes, including archived ones, into its history. The
other undertaking stays active. History can be edited; a new undertaking inherits
no old links. Duplicate completion requests and stale forms cannot complete a
replacement record.

A task stores title, state, creation, order, and set. A set stores name, creation,
and selection. Implement create/edit/complete/reactivate, completed views,
confirmed deletion, reorder, and set switching. Quick input uses the selected set.
Sticky notes belong to specific tasks. Nested subtasks are outside the base model.

## 3. Events and calendar

An event stores title, date/time, importance, completion, order, color label,
series ID, recurrence rule, and end. Color and importance are independent. Support
today/tomorrow, a month, record viewing/editing, and drag rescheduling with rollback
on failure. Long titles and busy days must not break the calendar.

Support daily, weekly, selected-weekday, monthly, and yearly repeats ending by date
or count. Future occurrences need not be duplicated rows. Edited/completed individual
occurrences retain their state; a date exception does not delete a series. Moving
an occurrence does not create duplicates. Distinguish single-occurrence and series
operations explicitly.

Color labels have editable names. A same-color event tree groups overdue, today,
upcoming, and completed records; create/edit/complete in place. Important in the
header shows the nearest event and a count, opening full titles/dates. Its horizon
is configurable; zero means today only.

## 4. Habits

Store title, period start, optional end, and completion. Active habits show elapsed
duration. Completing fixes the end and retains the period in completed history.
Support editing, deletion, and linked sticky notes. This is not a daily check-in
tracker: daily execution, plans, and misses belong to activities.

## 5. Activities and day routines

A set stores name, creation/edit/archive dates, automatic weekdays, today's manual
selection, active state, and archive. An activity stores text, order, start/end,
no-time state, weekdays, task link, and set. Execution logs record activity and
actual completion timestamp. Give schedule start time its own field in a new schema
rather than overloading record creation time.

Workday, research, and weekend sets may differ. Automatic weekdays cannot conflict.
Manual selection lasts for today; the next day uses the schedule. Support cloning,
inactive-set inspection without selection, editing, and archive. Preserve activities
and logs in the archive. Restore only available weekdays rather than taking them
from another set.

Highlight current/next intervals, durations, and overlaps, with a jump to the current
time and refresh without page reload. Store daily check-ins by local date and make
repeated requests idempotent. Weekly totals distinguish planned, completed, missed,
upcoming, and extra completions. Today and future dates are not misses. Frequent
misses use a period and three configurable thresholds. Selection/check-ins do not
change the content-edit timestamp.

## 6. Notes and editing

A note stores title, body, category, pinning, creation, update, and PDF export date.
Provide categories, search, lists, pinned cards, and an expanded editor. Formatting
includes bold, lists, quotes, tables, and alignment. Keep tools accessible while
scrolling, with top/bottom jumps and date/time insertion at the cursor. Ctrl+Enter
saves and Ctrl/Cmd+B toggles bold.

Two quick spaces after text insert a period and space, within 700 ms. Ignore paste,
held keys, indentation, and existing punctuation. The gear-menu preference defaults
to enabled, persists in the browser, and synchronizes across editors. Replacement
participates in undo and autosave.

Store text/formatting history, undo position, and redo branch in the database with
the note, up to 100 steps with a total-size cap. Group consecutive typing. Editing
after undo replaces the redo branch. Buttons and Ctrl/Cmd+Z, Ctrl/Cmd+Shift+Z,
Ctrl/Cmd+Y agree. Empty undone content may be saved and then redone.

Autosave starts at the first unsaved change; continuous typing cannot postpone it
indefinitely. Orange means changed, green means server-confirmed save. Attempt
save on close/leave and do not present failure as success. Prevent stale-editor
overwrites. Hiding the widget editor retains the draft and autosave. Single-click
cards to view and double-click to edit; a same-card nearby-position recognition
window up to 250 ms avoids flashing the viewer. PDF retains readable formatting
and Cyrillic text.

## 7. Linked sticky notes and conversion

Store title, content, type, color, order, creation, archive date, and owner link.
Types: text, alternating prose/checklists, tables with cell colors, formatted notes.
Owners include tasks, events/series, habits, notes, main/fallback undertakings, and
completed undertaking history. Show attachment counts beside owners.

Enter splits at the cursor; empty Enter ends a list; Backspace/Delete removes
empty items or merges neighbors; multiline paste creates items. Preserve block order
and checkbox states. Serialize quick check requests and roll back failed updates.
Archive views are not ordinary editors; restore preserves content. Repeated archive
requests retain the date. Copy readable text, not JSON. Configure preview items,
rows, and columns.

Note ↔ sticky conversion preserves links, color, category, pinning, and formatting.
Show one active representation; conversion back restores properties. Repeated
clicking must not create copies. Completed undertakings retain their sticky context.

## 8. Chronology, header, and quick input

Chronology records contain text and a chosen date/time. Group multiple entries into
a day, then month/year. Count days and entries separately. Default day cards show
a date, count, and one preview line. All-word search normalizes case and Russian
е/ё and expands matching days. Date/year/month filters combine; expanded days
survive regrouping. Saving clears obstructing filters, expands and scrolls to the
specific entry, and highlights it for a configurable duration. Full-view creation
uses the selected date and widget draft; default to yesterday.

Quick input provides text, date, Tomorrow, category, color, and recurrence. Categories
cover events, important events, tasks, habits, Wink, counters, and both undertakings.
Counters store label, date, until/since direction, and selection; cycle through
several and remember the choice for the session. Wink resurfaces a random active
short entry with archive/restore operations. Hide empty header information cards.

## 9. Settings

Settings have search, explanations, defaults, limits, and reset. Validate on client
and server and save a group atomically. Retain input on failure and reveal a
search-hidden invalid field. Missing values use defaults. Changes affect partial
widget refreshes too. The names below identify unambiguous settings; internal
identifiers may differ if behavior is preserved.

| Setting | Default | Allowed values |
|---|---|---|
| Important horizon, days (`important_days_ahead`) | `3` | 0–365 |
| New event time (`event_default_time`) | `09:00` | HH:MM (00:00–23:59) |
| Default recurrence horizon, years (`event_repeat_years`) | `10` | 1–50 |
| Default recurrence count (`event_repeat_count`) | `10` | 1–365 |
| Events per calendar cell (`calendar_events_per_day`) | `4` | 1–20 |
| Autosave interval, seconds (`note_autosave_interval_seconds`) | `30` | 1–3600 |
| Pinned note limit (`pinned_notes_limit`) | `10` | 1–500 |
| Recent note limit (`recent_notes_limit`) | `10` | 1–500 |
| Note search limit (`note_search_limit`) | `500` | 1–2000 |
| Chronology default days ago (`chronology_default_days_ago`) | `1` | 0–365 |
| Chronology highlight, seconds (`chronology_highlight_seconds`) | `5` | 0–60 |
| Activity history, days (`observation_history_days`) | `28` | 7–365 |
| Minimum expected completions (`observation_missed_min_expected`) | `3` | 1–365 |
| Minimum misses (`observation_missed_min_count`) | `2` | 1–365 |
| Miss threshold, percent (`observation_missed_percent`) | `50` | 1–100 |
| Activity time refresh, seconds (`observation_refresh_seconds`) | `60` | 5–3600 |
| Sticky notes per page (`sticker_page_size`) | `20` | 1–200 |
| Preview checklist items (`sticker_preview_items`) | `2` | 1–30 |
| Table preview rows (`sticker_preview_rows`) | `3` | 1–30 |
| Table preview columns (`sticker_preview_columns`) | `2` | 1–8 |
| Widget tips (`show_widget_tips`) | `true` | true / false |
| Events widget (`plugin_events`) | `true` | true / false |
| Tasks widget (`plugin_tasks`) | `true` | true / false |
| Habits widget (`plugin_habits`) | `true` | true / false |
| Notes widget (`plugin_notes`) | `true` | true / false |
| Chronology widget (`plugin_chronology`) | `true` | true / false |
| Activities widget (`plugin_observations`) | `true` | true / false |
| Sticky notes widget (`plugin_stickers`) | `true` | true / false |
| Notification duration, seconds (`toast_duration_seconds`) | `3.5` | 1–60 |
| Maximum visible notifications (`toast_max_visible`) | `3` | 1–10 |
| Google past days (`google_calendar_past_days`) | `30` | 0–365 |
| Google future days (`google_calendar_future_days`) | `365` | 1–730 |
| Google import on startup (`google_calendar_sync_on_start`) | `true` | true / false |

## 10. Storage, integrations, and accessibility

Give entities stable IDs and enforce foreign-key relationships. Distinguish record
timestamps from user-chosen dates. Display dates consistently in the local zone;
calendar duration calculations handle month ends and leap years. Do not invent
historical timestamps for unknown values.

Keep personal and fictional databases separate. Seed explicitly with an anchor date
and refuse overwrites. In demo-data.json, `$date` is a day offset, `$datetime` an
offset and clock time, and IDs are fixture links. Adapt original `daily`/`weekly`
rules to your schema. The original Observation stores start time inside `created_at`;
move it into a separate field. All characters and metrics are fictional; the fixture
remains in Russian.

Backups include committed SQLite data. Back up before migrations. Validate format,
schema, and links before transactional restore; failure must not clear the working
database. Create test databases only in temporary directories.

If implemented, Google Calendar uses explicit connection, one chosen calendar,
read-only access, and startup/manual import without continuous polling. Recurrences,
cancellations, and moved occurrences do not duplicate events. Preserve local marks
and sticky notes on update and retain the last copy on network failure. Keep secrets
out of databases/backups. Optional dictation inserts into the current field without
breaking lists; disclose external audio transfer explicitly.

Russian, English, and Kazakh cover buttons, dialogs, errors, dates, and refreshed
content. Support Tab, Enter, Space, Escape, and appropriate arrow keys; restore
focus after dialogs. Touch controls cannot depend on hover. Long text does not
cause page-wide horizontal scrolling. Honor reduced motion. Follow VISUAL.en.md.

## 11. Acceptance checks

1. Install in a fresh environment, run exact README commands, and open an empty database.
2. Create/edit/complete/reactivate tasks, reorder, switch sets, and return.
3. Create both undertakings with sticky notes; complete one, preserving the other, history, and links.
4. Change start dates and check duration across month ends and leap days.
5. Create each recurrence type; edit/skip one occurrence and inspect neighboring dates.
6. Drag an event with failure rollback; open its color tree and complete an event there.
7. Complete a habit, retaining its period without altering daily activity logs.
8. Schedule routine sets, manually select today, check next-day behavior, archive, and conflict-free restoration.
9. Check an activity twice for one date without duplication; inspect planned/missed/future/extra totals.
10. Test note formatting, tables, date insertion, double space, and replacement exclusions.
11. Save, close, and restart: undo/redo retain their saved position and branch.
12. A stale editor cannot overwrite newer text; autosave failures never show green success.
13. Test mixed sticky blocks, Enter/Backspace/Delete, multiline paste, quick checks, and archive dates.
14. Convert note to sticky and back, preserving links/color/category/pinning/formatting without duplicates.
15. Save yesterday's journal entry under an obstructing filter: reveal and highlight the correct card.
16. Check grouping, separate day/entry totals, all-word search, and е/ё normalization.
17. Collapse/move/reload a widget, then use cloud navigation to expand/focus/highlight it.
18. Verify all 33 settings, defaults, bounds, and retained input after an error.
19. Back up and restore into a separate database; an invalid file leaves existing data intact.
20. Check Cyrillic, newlines, long text, literal `<script>` without execution, and PDF export.
21. Use the keyboard; verify all three languages and widths 390, 1440, and 1920.
22. Compare colors, geometry, typography, and dialogs with VISUAL.en.md and reference/design-tokens.json.
23. Report implementation/verification/limitations and a verification method for every one of the 64 catalog items.
24. Restart again: no data loss, duplication, or state reset.

Do not replace behavioral verification with searches for expected strings in your own code.
