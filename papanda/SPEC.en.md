# Requirements for your own application

[Русский](SPEC.md)

## Purpose and scope

A personal local tool: one user, one browser, one SQLite database. The video
illustrates the idea; reproducing Papanda's exact appearance is not required.
SaaS accounts, multi-user roles, billing, and a required AI API are outside scope.

## Behavior

| Area | User action | Persistent state |
|---|---|---|
| Main undertaking | Choose one main outcome, its start date, and a fallback undertaking; complete either | Current undertakings and completion history |
| Tasks | Create project sets, switch sets, reorder and complete tasks | Set, title, status, order |
| Schedule | View today/tomorrow, open a month, set time and color | Event, date/time, importance, status, category |
| Recurrence | Create daily/weekly events; change or skip one occurrence | Rule, series end, exceptions, edited occurrences |
| Habits | Check in today and see consecutive days | Check-in history by local calendar date |
| Activities | Define a Working day set, activity times, task links, and completion | Sets, weekday schedules, execution log |
| Notes | Write a title and body, choose a category, pin, search | Content, creation/edit dates, category, pinned state |
| Sticky notes | Write a thought/checklist and attach it to a task, event, note, or main undertaking | Content, color, link, archive state |
| Chronology | Record a day's outcome and read past entries | Text and chosen date |
| Counters | See days until a demo and since project start | Date, label, counting direction |
| Settings | Toggle blocks and back up/restore data | Settings and a backup file |

Distinguish tasks (outcomes), events (appointments), activities (repeated work),
notes (knowledge), and chronology (what happened). Relationships between them
matter more than adding many cards. Nested tasks, voice input, and integrations
can be added later.

## First screen

Top row: title, today's date, main undertaking, and two counters. Below: schedule
and tasks, then activities/habits, notes, and sticky notes. The journal is accessible
from this screen. Cards form one column on narrow screens. Long text must not
break the layout. Supplement color with text. Give buttons accessible names and
fields labels. Escape closes modal dialogs and returns focus. Saving and errors
must be visible to the user.

## Demonstration data

The fictional character Alexey is an independent AI developer building Atlas,
a document-search assistant. His plans include a client demo, retrieval quality
experiments, learning, rest, and imperfect completion. The fixture remains in
Russian because the video is in Russian. Adapt it to your own schema.

In `demo-data.json`:

- `anchor_timezone` identifies the anchor day's time zone.
- `tables` contains rows for original Papanda models; adapt them to your implementation.
- `{"$date": -3}` means three days before the anchor day.
- `{"$datetime": [2, "14:00"]}` means two days later at 14:00.
- Numeric `id`, `task_id`, `note_id`, and similar fields are stable links within the fixture.
- `recurrence_rule` uses Papanda rules such as `daily` and `weekly`; the end date is separate.
- The original Observation model stores activity start time in the time component
  of `created_at`. Prefer an explicit start-time field in a new implementation.

Seed only on an explicit command. Do not mix demo records into personal data.
Restarting must not add duplicates. A new habit implementation should use daily
check-ins; the original fixture's habit state does not prescribe your architecture.

## Acceptance checks

1. Follow the README commands in a new environment and open the application.
2. Open an empty database: see useful empty states without errors.
3. Create and rename an Atlas task, complete it, switch sets, and return. Verify state and order.
4. Add an event for tomorrow, locate it in the calendar, and edit its time.
5. Create a weekly series, remove one occurrence, and confirm neighboring weeks remain.
6. Complete the main undertaking and find it in history with its original start date.
7. Save a note containing Cyrillic text, newlines, and literal `<script>` text. Preserve
   newlines, prevent script execution, and find the note by searching for «Атлас».
8. Attach a sticky note to a task, check an item, and verify persistence of both link and state.
9. Check in on a habit twice today without creating two completions for the date.
10. Write yesterday's journal entry and inspect chronology order and the activity week.
11. Restart the server and verify persistence. Restarting the demo must not reset edits.
12. Back up, restore into a separate test database, and compare records and links.
    An invalid file must not damage the existing database.
13. Complete core actions with the keyboard and inspect widths of 390 and 1440 pixels.
14. Check midnight boundaries, month ends, leap days, empty input, and long content.

Prioritize automated checks for storage, dates, recurrence, relationship integrity,
and restore. Do not substitute comparisons against your own source strings for
behavioral tests.
