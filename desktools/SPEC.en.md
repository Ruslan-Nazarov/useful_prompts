# DeskTools specification

[Русский](SPEC.md)

## Environment and scope

A local single-user desktop application for Windows 10/11, with a Russian UI and
three main sections. Do not add an AI chat, clipboard history, accounts,
arbitrary program execution, application-specific rules, or mandatory sync.
URLs are limited to HTTP/HTTPS.

Suggested implementation: WinForms/.NET Framework 4.x, dedicated low-level hook
threads, Windows OCR through a hidden PowerShell process, and direct HID only
for the supported device. Architecture may differ; behavior must match.
Unavailable devices or privileges must not stop unrelated features.

## Settings and transactions

Use one local JSON document, schema version 1. Document its location and separate
it from the executable so updates retain settings. Minimum fields:

| Group | Fields |
|---|---|
| General | `version`, `remappingEnabled`, `ocrEnabled` |
| OCR | `ocrLanguage` (empty selects Windows), `ocrSingleParagraph`, `ocrShowResult` |
| Keyboard | `mappings[]`: `name`, `enabled`, `source[]`, `kind`, `keys[]`, `text`, `url`, `exactMatch` |
| Mouse | `mouse.enabled`, `mouse.bindings[]`: `button`, `enabled`, `kind`, `keys[]`, `value` |
| Lighting | `mouse.lighting`: `enabled`, `brightness`, `scheduleEnabled`, `offAt`, `onAt`, `idleMinutes` |
| Templates | `templates[]`: `name`, `text` |

Use Windows virtual key codes; the final source key triggers the action. Left/right
Shift: 160/161, Ctrl: 162/163, Alt: 164/165, Win: 91/92. Held-key order does not
change chord identity; changing the trigger does. Keyboard action kinds are
`keys`, `text`, and `url`; mouse actions additionally include `disabled` and
`lighting`. Mouse buttons: `middle`, `x1`, `x2`, `wheelUp`, `wheelDown`.
Missing legacy sections receive safe defaults: mouse and lighting disabled,
templates empty.

Limits: JSON up to 1 MiB in UTF-8; binding text up to 4096 characters; at most
100 mouse bindings; mouse chords up to 16 distinct keys; at most 200 templates,
names of 1–100 characters, nonblank text of 1–4096. OCR editors allow up to
200,000 characters; direct insertion allows 10,000, with copying for larger text.
Reject whitespace-only templates, invalid URLs, and duplicate enabled sources
before applying changes.

Validate the entire candidate and serialized byte size before writing. Write a
temporary file, flush it, and atomically replace the primary with a backup of the
previous valid version. Failure preserves the active model, primary, backup,
and editor draft. Preserve a corrupt primary separately and restore a validated
backup with an explanation. Invalid reloads leave the previous model active.

PowerToys import is a separate operation covering global keys/chords, Unicode,
and HTTP/HTTPS, without program launching or application rules. Confirm replacement
in the UI and retain other settings sections. First launch may offer an import;
demonstration profiles never read the personal profile.

## Keyboard, mouse, and shared lifecycle

Editors show the assignment summary and explain disabled saving. Recording does
not start while typing a name. Repeated held keys do not duplicate recorded keys;
leaving recording restores the previous chord. Distinguish modifier sides and
support held ordinary keys such as Space+В.

Check longer matching chords first, ahead of standalone mappings. `exactMatch`
forbids extra modifiers. Balance release/restoration of physical modifiers around
actions and ignore self-injected input. Deleting, disabling, or replacing a held
binding releases its output and consumes the corresponding source key-up.
Track every source holding a shared output key.

Editing keyboard, mouse, or templates temporarily suspends both remapping services
and OCR. Global pause is independent; nested suspensions resume only after the
last owner ends. Saving never resumes services early. Ctrl+Alt+T does not open
the picker during pause. Settings changes preserve suspension. Physical mouse
activity remains observable while mouse bindings are disabled.

If PowerToys Keyboard Manager is running, explain the conflict and suspend keyboard
remapping without terminating other processes. Register Ctrl+Alt+Space and
Ctrl+Alt+T without autorepeat and report conflicts. Reserve both shortcuts in
the binding editor. Win+S has priority while OCR
is enabled; Win+Shift+S passes through to Windows.

## OCR, text, and templates

Selection covers the virtual desktop, works in either drag direction and with
negative coordinates, supports cancellation, and rejects tiny regions. Do not
retain captures. Resize large images to the Windows OCR limit; the reference
approach caps the largest side at 4000 px. A separate worker times out after
45 seconds and terminates on cancellation. Delete temporary PNG/JSON files on
success and failure. Never publish a late result after shutdown.

Whitespace cleanup collapses tabs, ordinary spaces, and nonbreaking spaces within
lines and trims edges. Joining replaces isolated newlines with spaces while
preserving blank paragraph separators. Layout conversion follows physical RU/EN
positions; the predominant Russian/Latin letter count selects the direction.
Both fields remain editable; empty actions are disabled. Failed copying or
insertion preserves both fields.

Create templates in an editor opened from the text section. Explicit saving
persists immediately; deletion requires confirmation. Only Ctrl+Alt+T opens the
insertion picker. Provide labelled case-insensitive name/content search, title
and excerpt rows, full preview, and Insert. Select the first result and disable
insertion for empty results.

Position by the system caret or fall back to the pointer. Constrain the window
to that monitor's work area, preferring above the anchor when space below runs
out. Capture the original window and native focus before opening. Wait for key
release, restore the window, and check the target between text batches. Do not
split surrogate pairs. CRLF/LF/CR yield one textual newline, not an Enter shortcut.
Preserve the clipboard. Cancellation/closing stops remaining batches; explain
partial insertion when it has occurred. Native focus checks do not prove that
a DOM field within one HWND stayed unchanged.

## Lighting and distribution

Defaults: lighting disabled, brightness 60%, schedule disabled (23:00–08:00), idle
shutdown disabled. Brightness range: 0–100%; idle: 0–240 minutes. Reject enabled
intervals with identical endpoints. Zero brightness can result from manual off,
night interval, or idle. Use local time and only physical activity for idle,
including TickCount rollover handling.

Support only DeathAdder Essential 1532:006E, zone 4 (logo), zone 1 (wheel), green
only. The Windows HID feature report contains a report ID and 90 payload bytes.
Use the public protocol reference in SOURCES.en.md. Validate command, zone,
status, and checksum; read back writes. Evaluate schedules every 2 seconds,
verify the device every 30 seconds, retry errors after 30 seconds, and provide
manual reconnect. Disabling management restores daytime brightness. Never try
speculative writes to unsupported devices.

Provide reproducible build/test commands, portable startup, and single-instance
behavior. Build archives in a clean staging directory with required assets and
OCR worker, excluding personal files. Normal startup does not download dependencies.
