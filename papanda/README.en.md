# papanda — a time management app

[Русский](README.md)

Build your own local application inspired by papanda: a main undertaking and
fallback, tasks, calendar, habits, activities, notes, sticky notes, chronology,
and counters. The kit specifies core functions, small interactions, and appearance.

## Kit contents

| File | Contents |
|---|---|
| [PROMPT.en.md](PROMPT.en.md) | Main agent assignment: 12 modules, relationships, required actions, implementation sequence |
| [SPEC.en.md](SPEC.en.md) | Detailed specification: fields, module behavior, 33 settings, 24 acceptance scenarios |
| [FEATURES.en.md](FEATURES.en.md) | All 64 interactions: cloud navigation, double space, gestures, persistent undo, conversions, and more |
| [VISUAL.en.md](VISUAL.en.md) | Colors, fonts, dimensions, grid, cards, dialogs, and responsive rules |
| [reference/design-tokens.json](reference/design-tokens.json) | Exact visual values extracted from papanda styles |
| [reference/default-layout.json](reference/default-layout.json) | Initial widget geometry |
| [reference/example-layout.json](reference/example-layout.json) | Populated-example geometry |
| [demo-data.json](demo-data.json) | Linked fictional AI developer records for exercising the application |

## What you need

A computer, editor, and AI coding agent with file and command access. The suggested
stack needs Python 3.12+ and a browser; the agent installs dependencies. Internet
is needed for the agent and packages. Core application workflows require no API
keys, Google Calendar, cloud account, or hosting. The agent itself may require an
account and payment under its own terms.

## Build

1. Create an empty project folder. Copy this complete kit: the four assignment
   documents, `reference` directory, and `demo-data.json`.
2. Open it in your editor, give the agent access to the files, and send the entire
   contents of `PROMPT.en.md`.
3. The agent must read SPEC.en.md, FEATURES.en.md, VISUAL.en.md, and the fixture,
   plan, then implement. Completing the first stage does not complete the assignment.
4. Run its exact launch command. Check the main workflow, restart persistence,
   and appearance against the visual specification.
5. Complete the 24 specification scenarios and request a report on all 64 feature
   items. Fix concrete discrepancies rather than equating visible buttons with completion.

To continue:

> Compare the implementation with SPEC.en.md, FEATURES.en.md, and VISUAL.en.md.
> Identify missing/incomplete items, then implement them while preserving working
> behavior and data. Verify functionality and appearance and update the 64-item checklist.

If appearance differs:

> Compare with VISUAL.en.md and reference/design-tokens.json. Correct colors,
> typography, dimensions, cards, grid, and dialogs using the appropriate layout.
> Keep the specified visual system. Check 390, 768, 1440, and 1920 px.

## Example data

The fixture describes a fictional AI developer and Atlas project. Every character,
record, and metric is invented; this is not the author's personal database or a
research benchmark. It remains in Russian while documentation is bilingual.
Adapt it to your schema while preserving links and relative dates. Seed explicitly
into a separate database rather than mixing examples into personal records.
