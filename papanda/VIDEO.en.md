# Video script: from scattered tasks to one working screen

[Русский](VIDEO.md)

This is a reference translation. The actual recording and demo records remain in
Russian. Target length is roughly 6–8 minutes, depending on delivery.

## Before recording

Run `demo.py prepare`, `demo.py check`, and `demo.py run` as described in the README.
Open port 8011 in a separate browser profile. Select Russian, use 100% zoom, and
open a window around 1440×900 or 1920×1080. Disable OS notifications. All records
and Atlas metrics are fictional.

Confirm the anchor date matches the recording day. Inspect the main undertaking,
schedule, a task with a sticky note, and a pinned note; close the dialogs before
the opening shot. Keep PROMPT.md and SPEC.md ready. Do not connect a personal
Google Calendar. Record only the application window, avoiding the desktop,
terminal, and editor with local paths. Publish using [PRIVACY.en.md](PRIVACY.en.md).

## Recording sequence

| Time | Shot and action | Point to convey |
|---|---|---|
| 0:00–0:30 | Overview; main undertaking «Довести Атлас до клиентского демо» | I need to see why I am working today, as well as the task list. |
| 0:30–1:15 | Open the main undertaking and «Сравнить поиск на 40 вопросах» | This is the week's outcome; this is the next concrete step. |
| 1:15–2:00 | Today/tomorrow, calendar, important client demo | Appointments have times; tasks have outcomes. Keep both nearby. |
| 2:00–2:45 | Activities, habits, and missed activities in the weekly review | This is an imperfect working day, with a visible record of what happened. |
| 2:45–3:45 | Pinned demo-plan note and a task-linked sticky note | Questions, criteria, and thoughts stay with the work they explain. |
| 3:45–4:30 | Add «Проверил цитаты; завтра разберу ошибки поиска» to chronology | The journal explains how work developed beyond completed checkboxes. |
| 4:30–5:15 | Complete a task and refresh | Changes are saved in a working application. |
| 5:15–6:30 | Open the kit, PROMPT.md, and SPEC.md | Viewers can build an application suited to their own needs with an AI agent. |
| 6:30–7:00 | Return to the overview | Start with the main undertaking, tasks, schedule, and notes; expand as needed. |

Avoid promising an exact copy from a single prompt or a fixed number of minutes.
If showing a from-scratch build, record an actual run: empty folder, first launch,
an error and its fix, then a persistence check. The existing Papanda demo is not
proof that another agent has already executed the prompt. Screenshots may serve
as visual references, but do not replace the specification.

Choose 3–5 close-up examples from the ten episodes at the end of
[FEATURES.en.md](FEATURES.en.md). The full catalog contains 64 details; it does
not have to be narrated in sequence. See [COMPARISON.en.md](COMPARISON.en.md)
for grounded product comparisons.

## Suggested description, translated for reference

> This video shows Papanda, my local tool for planning time, taking notes, and
> reviewing my work. The example uses fictional records for an AI developer.
> The kit includes a prompt, requirements, and demo data to help you build your
> own similar application with an AI coding agent. Start with the README.
>
> Kit: https://github.com/Ruslan-Nazarov/useful_prompts

## Another take

Stop the server, then repeat `prepare` and `run`. Each take gets a fresh database;
the earlier take remains in `.demo/runs/`. To return to it, pass its absolute path
with `--run-dir`. Never import the demo into a personal database.
