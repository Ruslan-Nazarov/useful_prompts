# papanda features and interaction details

[Русский](FEATURES.md)

This catalog supplements [SPEC.en.md](SPEC.en.md) with 64 interface behavior
requirements. The specification defines the core modules and data model; the
small interactions below are also part of the assignment. Maintain an
implementation checklist by number and verify behavior through the interface.
Visible button labels alone do not satisfy a requirement.

## Navigation and workspace

| No. | Detail | Behavior and benefit |
|---|---|---|
| 1 | **Cloud navigation on each widget** | Jump to another enabled section from the current widget without returning to a top menu. |
| 2 | **A jump expands a collapsed destination** | Arrive at the content even if the destination had been folded away. |
| 3 | **The destination receives focus and a brief highlight** | The move is easy to follow visually and with the keyboard. |
| 4 | **The cloud opens on hover or click** | Supports mouse and touch; arrow keys, Home/End, and Escape also work in the menu. |
| 5 | **Widgets can be moved and resized** | Allocate screen space to the work that matters now. |
| 6 | **Layout, collapsed state, and expanded height persist** | Reloading does not push neighbors away with temporary expanded sizes; expanding restores the earlier height. |
| 7 | **Each widget can have its own border color** | Create visual landmarks; color is stored with the layout. |
| 8 | **Collapsed headers retain navigation and expand controls** | Even a folded widget remains a useful navigation point. |
| 9 | **Seven widgets have independent visibility settings** | Build a quieter screen by hiding sections you do not need. |
| 10 | **Routine success actions avoid celebratory popups** | The changed card shows the result; errors and required guidance remain visible. |

## Input and the note editor

| No. | Detail | Behavior and benefit |
|---|---|---|
| 11 | **Double space inserts a period and a space** | Two quick presses after text end a sentence. This is double space, not a screen double tap. |
| 12 | **Replacement is sensitive to input context** | Ignores paste, held keys, indentation, and existing punctuation; recognition window is up to 700 ms. |
| 13 | **The double-space preference is stored in the browser** | Enabled by default, controlled through the gear menu, and synchronized across editors and tabs. |
| 14 | **Undo/redo history is saved with the note** | Reopen the editor after a server restart and continue from the saved position, with up to 100 steps and a total-size limit. |
| 15 | **Undo includes formatting and inserted structures** | Tables, lists, quotations, alignment, and inserted dates participate alongside text edits. |
| 16 | **Autosave starts from the first unsaved change** | Continuous typing cannot postpone saving forever; the interval is configurable. |
| 17 | **A small dot communicates save state** | Orange means unsaved edits; green means saved. A tooltip explains it. |
| 18 | **A stale editor is prevented from overwriting newer content** | Protects a note edited in multiple windows; show a conflict message and let the user retain their own edits. |
| 19 | **A menu inserts the date or date and time at the cursor** | Useful for experiment logs, meetings, and annotations inside a long note. |
| 20 | **Buttons jump to the top and bottom of long text** | Save scrolling while the toolbar stays accessible. |
| 21 | **The widget editor can be hidden while pinned notes remain visible** | Switch between reading and writing without losing the draft or stopping autosave. |
| 22 | **One click reads a card; a double click edits it** | Pinned notes and chronology can open directly in editing mode. The pair must target the same card at a nearby position. |
| 23 | **Card gestures have keyboard equivalents** | Enter/Space opens viewing; Shift plus activation opens editing. Keyboard input does not wait for double-tap recognition. |
| 24 | **Ctrl+Enter saves; Ctrl/Cmd+B toggles bold** | Common operations remain available through both shortcuts and buttons, including undo/redo. |
| 25 | **Notes export to PDF with export metadata** | Share content outside the application; the export date stays in the detailed view rather than cluttering cards. |

## Sticky notes as linked context

| No. | Detail | Behavior and benefit |
|---|---|---|
| 26 | **Sticky notes attach to multiple kinds of record** | Events, tasks, habits, notes, the main undertaking, and its fallback can each carry context. |
| 27 | **Attachment counts appear beside records** | Discover context without opening every item. |
| 28 | **A note can become a sticky note and back again** | Expand a quick thought into reference material or bring material onto the dashboard; preserve links, category, color, and pinned state when converting back. |
| 29 | **Formatted note content remains readable in a sticky note** | Conversion is more than copying plain text. |
| 30 | **Text and checklist blocks can alternate** | Write an introduction, steps, and a conclusion; insert the next block at the cursor. |
| 31 | **Enter on an empty list item ends the list** | Return naturally to ordinary text. |
| 32 | **Enter splits an item; Backspace/Delete merges adjacent items** | Edit the checklist as text instead of filling separate little forms. |
| 33 | **Pasting multiple lines creates list items** | Turn a clipboard plan into a checklist without empty lines or foreign HTML shifting checkbox positions. |
| 34 | **Check items directly in viewing mode** | Avoid opening the editor for one completed action; requests are serialized and failures roll the check back. |
| 35 | **Table sticky notes support cell colors** | Suitable for small comparison matrices or compact plans. |
| 36 | **List/table preview depth is configurable** | Choose how many items, rows, and columns appear in cards. |
| 37 | **Copy produces readable text, including lists and tables** | Move content to another application without exposing its internal storage format. |
| 38 | **Archiving preserves its date and supports restoration** | Follow a thought's lifecycle; repeated archive requests do not rewrite its historical date. |

## Main undertaking, time, and context

| No. | Detail | Behavior and benefit |
|---|---|---|
| 39 | **The main undertaking and fallback are independent** | Keep a primary outcome and backup work; completing one does not complete the other. |
| 40 | **An undertaking has elapsed duration, not just a deadline** | Its tooltip shows calendar years/months/days and total full months, days, and hours. |
| 41 | **Completed undertakings have their own history** | Retain the wording, start, creation, completion, and final duration. |
| 42 | **Sticky notes follow the completed undertaking into history** | A new undertaking does not inherit old thoughts; a past stage keeps its explanations, including archived sticky notes. |
| 43 | **Task sets switch a whole working context** | Move between a project, research, and personal tasks. |
| 44 | **A common quick-input line routes text to a chosen category** | Capture something before navigating to its section; category and color are independent. |
| 45 | **Tomorrow changes the quick-input date in one action** | Plan for the next day without opening a date picker. |
| 46 | **An event color opens a related event tree** | The context menu groups same-color events into overdue, today, upcoming, and completed. |
| 47 | **The event tree supports completing, editing, and adding** | It is a working view of a direction, rather than a read-only color filter. |
| 48 | **Important events share one compact header card** | Show the nearest event and a count, then open full titles and dates; the look-ahead horizon is configurable. |
| 49 | **Counters run both until a date and since a date** | See the approaching demo and elapsed project time; selection among several counters is remembered for the session. |
| 50 | **Wink brings back a random active short record** | Resurface an earlier thought without claiming AI recommendation. |
| 51 | **Empty information cards disappear from the header** | Missing content does not leave decorative blank blocks. |

## Activities and chronology

| No. | Detail | Behavior and benefit |
|---|---|---|
| 52 | **Activity sets can be assigned to weekdays** | Workdays and weekends can have different rhythms; a manual choice applies to the current day. |
| 53 | **An activity links to a concrete task** | Connect the planned work with the outcome it serves. |
| 54 | **Current and next activities are highlighted by time** | Orient within the day, with automatic scrolling toward the relevant area. |
| 55 | **Weekly review separates plans, completions, and misses** | Distinguish intentions from what happened; today and future days are not counted as missed. |
| 56 | **Frequently missed activities use a configurable rule** | Set the period, minimum expected completions, miss count, and miss percentage so a single bad day need not trigger a signal. |
| 57 | **Inspect an inactive set without selecting it** | Compare day routines without changing the active context. |
| 58 | **Archived sets preserve activities and execution logs** | Restoring reclaims available scheduled days without taking days away from another set. |
| 59 | **Editing a set is distinct from using it** | Selecting a set or checking an activity does not change the content-edit timestamp; creation, edits, and archive dates are separate. |
| 60 | **Chronology groups entries into calendar-day cards** | Keep several entries per day while counting days and entries independently. |
| 61 | **Compact days expand when search needs them** | One-line previews maintain an overview; grouping supports days, months, and years. |
| 62 | **Chronology search treats Russian е/ё alike and matches all query words** | Find old entries without reproducing the exact spelling. |
| 63 | **Saving a journal entry reveals that specific entry** | Clear obstructing filters, expand its day, scroll to it, and briefly highlight it, including backdated entries. |
| 64 | **A new entry respects the chosen date and retains the widget draft** | Continue a thought from the full view; the default date is yesterday, supporting morning reflection. |

## Required distinctions

- A habit records its start-to-completion period. Daily check-ins and weekly
  statistics belong to activities. A separate daily habit tracker is an extension.
- Task sets contain ordered lists. A same-color event tree is not nested subtasks.
- Russian, English, and Kazakh interfaces cover dynamic dialogs, date labels,
  errors, and empty states.
- Search, settings, backups, event recurrence, and exceptions are specified in
  SPEC.en.md. These 64 details complement rather than replace the core modules.
- Google Calendar is an optional read-only import that preserves local completion
  marks and sticky notes. External voice transcription requires an explicit
  explanation of audio transfer and an API key.
- Core workflows work without an account or either integration.
- A built-in AI chat is outside scope and is not required to manage stored records.
