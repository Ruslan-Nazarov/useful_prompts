# DeskTools acceptance

[Русский](ACCEPTANCE.md)

Use fictional data in a separate profile. For each A ID, record outcome, related
F IDs, command/actions, and observation. Distinguish engine tests, UI checks, and
real input into a target Windows window. A screenshot of a button is insufficient.

| ID | Scenario and expected outcome | Requirements |
|---|---|---|
| A01 | Start an empty profile; visit three sections at 390/768/1440 px. Check Tab, focus, navigation arrows, menu Esc, scrolling, and retained input. | F01 F02 |
| A02 | Build using README and inspect the clean portable archive. Launch twice, hide/restore, test no-tray mode, explicitly exit. One instance until exit, no surviving hooks afterward. | F03 F04 F40 |
| A03 | Save a template/binding and restart; corrupt and separately delete the primary JSON. Restore a valid backup with an explanation. | F06 F07 F08 |
| A04 | Try a Cyrillic collection exceeding 1 MiB UTF-8 and a simulated write failure. Preserve both files, model, and draft. Fictional PowerToys import changes keyboard only. | F06 F08 F09 |
| A05 | Record Ctrl+Shift+F8, right Ctrl, and Space+В, including autorepeat. Leaving unfinished recording restores the old chord. | F10 F11 |
| A06 | Create, edit, disable, delete, switch action drafts, and reject a duplicate with reordered held keys and an invalid URL. | F12 F13 |
| A07 | In a test editor, verify exactMatch, longer-chord priority, one-shot text/URL, key repeat, and no self-injection recursion. | F14 F16 |
| A08 | Hold a source during pause/deletion/replacement; leave no output held. Map two sources to one output and release one at a time. | F15 |
| A09 | Check Caps Lock while mapped and paused, grave/Ё labels against available Windows settings, and recovery after removing a test hook. | F17 F18 F19 |
| A10 | Save settings while editing and exercise nested suspension: keyboard, mouse, and OCR never resume early; explicit pause remains. | F05 F19 F35 |
| A11 | Test original buttons and all five assignable mouse sources, holds, release after pause, partial wheel events, action types, and editor errors. | F20 F21 F22 F23 F24 |
| A12 | Explain absent hardware. Verify night/midnight boundaries, idle/activity, manual off, and timer rollover through calculations. | F25 F26 F27 F28 F29 |
| A13 | Only with 1532:006E: read original brightness, change both zones, confirm readback, restore originals in finally, and reject invalid packets. | F25 F28 F29 |
| A14 | Start OCR with both Win+S variants, pass Win+Shift+S through, cancel, drag both ways, reject tiny regions, and test a left-hand monitor. | F30 F31 |
| A15 | Recognize a real test image through Windows OCR; check lines, language, paragraph mode, empty result, copying, and editable result display. | F32 F34 |
| A16 | Cancel OCR before start, during selection, and during the worker; test timeout and shutdown. Clean temporary files and suppress late results. | F33 |
| A17 | Verify whitespace and RU/EN conversion, isolated line joining with paragraph retention, disabled empty actions, and error retention. | F34 |
| A18 | Open the text section from a test field with Ctrl+Alt+Space, insert Unicode/emoji/paragraphs back, and stop on window/native-focus changes. | F35 F39 |
| A19 | Create/edit/delete templates, restart, test limits and save failure; Ctrl+Alt+T places the picker near caret/pointer within the monitor work area. | F36 F37 |
| A20 | Search names/content, select by arrows, insert by Enter/mouse, dismiss by Esc. Check empty states, unchanged clipboard, and cancellation on focus loss while waiting for key release. | F38 F39 F40 |

Run hardware checks only on the supported device. Mark desktop-dependent checks
unverified when an interactive desktop is unavailable. Continue independent
tests; do not replace Windows OCR with a stub. For mixed DPI, separately check
caret coordinates, picker bounds, and region selection across monitors.
