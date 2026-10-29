# Verifiable DeskTools features

[Русский](FEATURES.md)

For every ID, record implementation location, actual verification, outcome, and
material limitation. A button does not establish behavior. All 40 requirements
are mandatory; hardware checks may remain unverified when the exact supported
device is absent, with that limitation explicitly recorded.

| ID | Requirement |
|---|---|
| F01 | Three sections in one window; switching preserves input and state. |
| F02 | VISUAL.en.md appearance, top navigation on narrow windows, scrolling, Tab, and visible focus. |
| F03 | Single instance; repeated launch opens it; closing hides, explicit exit releases resources. |
| F04 | PROCESSDOCK_NO_TRAY=1 suppresses the tray and balloon notifications; no external manager is required. |
| F05 | Global pause and nested temporary suspensions coordinate keyboard, mouse, OCR, and templates. |
| F06 | Versioned settings are validated and atomically saved after a UTF-8 limit check of 1 MiB. |
| F07 | A valid backup restores a corrupt or missing primary; preserve corrupt files separately. |
| F08 | Load/write failure retains the previous model and input; legacy settings gain safe new sections. |
| F09 | Confirmed PowerToys import covers keys, chords, text, and HTTP/HTTPS, retaining mouse, OCR, and templates. |
| F10 | Explicit recording distinguishes modifier sides, finishes on first release, and cancels without losing the old value. |
| F11 | Ordinary held-key chords including Space+В; repeated recording events never duplicate a key. |
| F12 | Keyboard custom keys, presets, text, and URLs; only relevant fields appear and action drafts survive switching. |
| F13 | Create, edit, disable, and delete; reject duplicate enabled sources regardless of held-key order. |
| F14 | Longer chords precede single keys; exactMatch excludes extra modifiers; ignore self-injected input. |
| F15 | Balance down/up across pause, replacement, deletion, and disabling; release shared output after its final source. |
| F16 | Normal key/media repeat; text and URLs run once per press; restore physical modifiers. |
| F17 | Protect accidental Caps Lock activation only during its active remapping; pause/disabling restores normal behavior. |
| F18 | The grave/Ё label reflects Windows language/layout switching without changing Windows settings. |
| F19 | A dedicated keyboard hook recovers after removal; explain PowerToys conflicts without terminating its process. |
| F20 | Mouse wheel click, x1/x2, and scrolling; preserve left, right, and unassigned buttons. |
| F21 | Mouse commands, chords, text, URLs, disabling a button, and lighting toggle. |
| F22 | Mouse starts disabled; sample Alt+Tab/play-pause bindings, Synapse guidance, and last physical button display. |
| F23 | Held buttons do not repeat; wheel handles complete detents; consume releases even after pause/settings changes. |
| F24 | Mouse editor retains drafts; duplicate sources, invalid URLs, and storage failures preserve the open editor and text. |
| F25 | Lighting only for 1532:006E, logo/wheel, shared green brightness 0–100%, management initially disabled. |
| F26 | Local night interval crossing midnight; inclusive off/exclusive on; reject identical boundaries. |
| F27 | Idle 0–240 minutes, restoration on physical activity, health probes excluded, correct TickCount rollover. |
| F28 | Manual off, reconnect, checking after resume/device return; disabling management restores daytime brightness. |
| F29 | Validate HID command/zone/status/checksum and read back writes; explain/retry errors; unsupported mice do not block the app. |
| F30 | Hook-based Win+S, both Windows keys, OCR priority; pass Win+Shift+S through; RegisterHotKey failure does not disable OCR. |
| F31 | Region drag in either direction across monitors with negative coordinates; Esc/right-click cancellation and tiny-region rejection. |
| F32 | Real local Windows OCR, installed languages, lines/optional paragraph, copying, and optional result display. |
| F33 | Bounded worker lifetime, cancellation, temporary-file cleanup, and no results published after shutdown. |
| F34 | Two editable fields, clipboard import, whitespace cleanup, paragraph-aware joining, and RU/EN layout; disable empty actions. |
| F35 | Ctrl+Alt+Space captures the target; copying/insertion retain text on error and check original window/focus. |
| F36 | Template CRUD in the text section; up to 200 entries, names up to 100, text up to 4096; errors preserve drafts. |
| F37 | Only Ctrl+Alt+T opens the insertion picker near caret/pointer inside monitor work area; name/content search. |
| F38 | Excerpts, full preview, arrows, Enter/double-click/Insert, Esc; explain empty library/search and errors. |
| F39 | Preserve the clipboard, wait for key release, cancel if focus leaves during that wait, handle Unicode/emoji/paragraphs and target changes. |
| F40 | Reproducible build, README, and portable archive with required resources; exclude personal settings, secrets, and diagnostics. |
