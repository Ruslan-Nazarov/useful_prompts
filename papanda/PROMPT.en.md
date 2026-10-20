# Prompt: build the papanda time management app

[Русский](PROMPT.md)

You are a software developer. Build a working local, single-user time management
application inspired by papanda in this empty folder. Always write the name
`papanda` in lowercase, including headings and sentence openings.

Read SPEC.en.md, FEATURES.en.md, VISUAL.en.md, reference/, and demo-data.json
in full before coding. The
specification defines modules, data, relationships, and acceptance checks; the
feature catalog adds 64 required interface behaviors. Do not reduce the assignment
to a generic task list, notes editor, and calendar. Their relationships matter.
Complete the whole assignment, not just the first screen. After planning, implement,
run, and continue until you have a verified result.

## Application structure

This is an app for planning and reviewing personal work. One workspace contains a
main undertaking, project task sets, events, habits, daily activities, notes, linked
sticky notes, and chronology. Events have times, tasks describe outcomes, activities
represent recurring work, notes hold knowledge, and chronology records what happened.

Implement these modules:

1. **Main undertaking and fallback.** Two independent current directions with a
   title, start date, creation date, duration, and their own sticky notes. Edit or
   complete either separately. Completion moves the undertaking and its sticky
   notes into history; a new undertaking does not inherit old context. Duration
   tooltips show calendar years/months/days and total days/hours.
2. **Tasks.** Named sets, one selected set, drag ordering, creation, editing,
   completion, and return to active work. Tasks have linked sticky notes. Use an
   ordered list; do not invent a nested-task hierarchy.
3. **Calendar.** Today, tomorrow, month view, time, color labels, importance, and
   completion. Daily, weekly, selected-weekday, monthly, and yearly recurrence;
   endings by date/count; editing or skipping one occurrence. Drag dates with a
   rollback on failure. An event's color opens a tree grouped into overdue, today,
   upcoming, and completed, with working actions inside it.
4. **Habits.** Track a current period from start to completion and its duration.
   Completion preserves the period and moves the record into completed habits.
   Do not substitute daily habit checkboxes: daily execution history belongs to activities.
5. **Activities.** Day-routine sets, weekday schedules, start/end times, task links,
   and daily completion records. Highlight current/next activities. Include weekly
   planned/completed/missed totals, configurable frequent-miss thresholds,
   inactive-set inspection, and archiving that preserves execution history.
6. **Notes.** Titles, categories, search, pinning, compact and expanded editors.
   Support bold, lists, quotes, tables, alignment, date/time insertion, and PDF
   export. Autosave starts from the first unsaved edit, with a save-state dot.
   Undo/redo history persists with the note across reopening and server restarts.
7. **Sticky notes.** Text, alternating prose/checklists, tables with cell colors,
   card colors, readable copy, archive and restore dates. Attach to tasks, events,
   habits, notes, the main undertaking, and fallback. Show attachment counts.
   Note ↔ sticky conversion preserves links, category, color, pinning, and formatted
   content without exposing duplicate active representations.
8. **Chronology.** Multiple entries per day, day/month/year grouping, all-word
   search with Russian е/ё normalization, and date filters. Compact days expand for
   search. Saving reveals, scrolls to, and highlights the specific entry, including
   backdated entries. Default to yesterday and retain drafts between compact and
   expanded editors.
9. **Quick input and header.** One input routes text to a chosen category, with
   date, Tomorrow, recurrence, and color nearby. Include until/since counters,
   compact Important events with a full list, and Wink, a random active short
   record. Empty information cards occupy no space.
10. **Workspace.** Seven movable, resizable, collapsible, hideable widgets with
    individual colors. Persist geometry, collapsed state, and expanded height.
    Every widget has a cloud navigation menu listing other enabled widgets.
    Navigation expands, scrolls to, focuses, and briefly highlights the destination.
11. **Settings and data.** Implement the 33 parameters in SPEC.en.md with search,
    descriptions, limits, defaults, and resets. Russian, English, and Kazakh
    interfaces. Backups, validated restore, and backups before migrations.
12. **Optional integrations.** Google Calendar is an explicitly connected read-only
    import preserving local completion marks and sticky notes. Voice input in
    supported fields requires a configured transcription service and disclosure of
    audio transfer. All core workflows work without either integration.

## Small interactions are requirements

Implement all 64 items in FEATURES.en.md, including:

- Two quick spaces after text become a period and a space, with undo, a gear-menu
  preference, and persisted choice. Paste, indentation, and held keys do not trigger
  replacement. Enable it by default.
- Single-click note/chronology cards to read and double-click to edit, without
  flashing the viewer first. Keyboard activation has no recognition delay; Shift
  plus activation edits.
- Enter on an empty sticky-list item exits the list; multiline paste creates items;
  Backspace/Delete naturally merge neighboring lines.
- Saved status follows server confirmation. A stale editor cannot overwrite newer
  content. Failed drag/check actions revert their visible optimistic changes.
- Hiding the note editor retains the draft and autosave.
- Routine successful actions avoid notification noise; errors remain understandable.

## Appearance is also required

Follow VISUAL.en.md and reference/design-tokens.json: warm #FFF5EC background,
orange #F2994A accent, white 24 px radius cards, soft shadows, compact top input,
and the specified typefaces and sizes. Use default-layout.json for a fresh
installation and example-layout.json for the fictional example. Keep the main
undertaking inside Tasks and use paper-like sticky notes. Do not substitute your
own visual style. Verify the overview, editors, menus, and phone layout against
the visual acceptance criteria, not merely matching section labels.

## Implementation and storage

Suggested stack: Python 3.12+, FastAPI, Jinja2, SQLAlchemy, SQLite, CSS, and plain
JavaScript. Choose another if required by the environment while preserving behavior.
Separate models, data operations, routes, templates, and client logic. Pin dependency
versions you actually test.

Use data/db/app.db for personal storage and a separate fictional example database.
Seed only through an explicit command with an anchor date and intact relationships;
refuse to overwrite an existing database. Restarting must not duplicate or reset
records. Do not read personal files, other databases, .env files, or browser profiles
to create demo data. Never commit secrets, personal data, or real databases. User
content must not execute HTML/JavaScript. Bind to 127.0.0.1. Authentication and a
built-in AI chat are not required for this local single-user workflow.

## Work sequence and completion

1. Read every input document and appearance reference and plan entities and relationships.
2. Build the foundation, database, and working main screen, then complete each
   module's create/read/update and applicable completion/archive operations.
3. Implement links, recurrence/exceptions, history, sticky notes, conversions,
   activity schedules, and every catalog item. Stages are not permission to stop
   at a minimal version.
4. Prepare fictional data and run SPEC.en.md acceptance checks. Verify an empty
   database, restart persistence, save failures, keyboard use, and a narrow screen.
   Prioritize automated tests for dates, recurrence, links, history, and restore.
5. Write a README with installation, launch, database path, backup instructions,
   and exact commands. Include a status and verification method for all 64 items.

A screenshot or a visible button does not establish completion. Do not claim tests
you did not run. Report concrete blockers and preserve working functionality rather
than concealing omitted features. The decisive check: I change the plan, write a
note, complete an undertaking, restart the server, and retain data, history, and links.
