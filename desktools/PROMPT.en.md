# Build DeskTools for Windows

[Русский](PROMPT.md)

Build a working local desktop application named DeskTools in the current empty
folder. It combines global keyboard and mouse remapping, supported lighting
control, screen OCR, text transformations, and a hotkey text template picker.

Read SPEC.en.md, FEATURES.en.md, VISUAL.en.md, ACCEPTANCE.en.md, SOURCES.en.md,
`reference/design-tokens.json`, and `demo-data.json` completely. Make a plan,
then implement the application. A plan, an initial screen, or one working
feature does not complete the assignment. Finish all 40 requirements and
20 acceptance scenarios.

## Application and workflows

Keep exactly three primary sections, labelled in Russian: «Клавиатура», «Мышь»,
and «Текст и OCR». Open them within one window and preserve input when switching.
A utility menu provides pause, settings, hide, and exit. Closing the window hides
the application; explicit exit removes hooks and ends background work. A second
launch shows the existing instance. Support an external process manager and
disable the tray when PROCESSDOCK_NO_TRAY=1.

The keyboard screen supports adding, editing, disabling, and deleting bindings.
Its editor has two steps: source key/chord and action. Recording starts explicitly
and finishes on the first release of a recorded key. Support Ctrl+Shift+F8 and
Space+В, with left/right modifier distinctions. Ready-made media, volume, copy,
paste, and system commands do not require extra fields. Show only the relevant
parameter for custom keys, text, or an HTTP/HTTPS URL. Preserve separate drafts
when switching action types.

Remapping must work globally with balanced down/up events, normal key repeat,
and correct release when settings change or processing pauses. Text and URLs run
once per press. Two source keys can hold the same output key; release it only
after the final source. Protect against accidental Caps Lock activation while
its remapping is active; explicit pause restores its normal behavior. When
displaying the grave/Ё action, account for the Windows language-switch setting.

The mouse section remaps the wheel click, side buttons, and wheel directions;
left and right buttons retain their ordinary behavior. Support commands, chords,
text, URLs, disabling a button, and toggling lighting. Mouse control starts off.
Example bindings are wheel click → Alt+Tab and side button 5 → play/pause.
Explain possible Synapse conflicts without terminating that application.

Implement lighting only for Razer DeathAdder Essential 1532:006E: green logo and
wheel, shared brightness, manual off, a night interval crossing midnight, and
idle shutdown with restoration on physical activity. Validate HID responses
and read back brightness. Report unsupported models honestly rather than
simulating support. The rest of the application works without this mouse.

Win+S starts region selection for Windows OCR. Use a hook so a system
RegisterHotKey conflict does not disable extraction. Support both Windows keys
without intercepting Win+Shift+S. Esc/right click cancel selection. Support
multiple monitors, including negative coordinates. OCR runs locally with
installed Windows recognition languages and preserves lines. Copy the result,
keep it editable, and optionally show it in the text section.

The text section imports clipboard text, cleans spacing, joins lines while
preserving paragraphs, converts Russian/English keyboard layout, and supports
editing, copying, and insertion into the original field. Ctrl+Alt+Space remembers
the source window and opens this section. Errors preserve entered text.

Create templates through «Текст и OCR → Шаблоны…». The insertion picker itself
opens only with Ctrl+Alt+T, beside the text caret or, when its position is
unavailable, beside the mouse pointer. Keep it inside the monitor work area.
Provide name/content search, list excerpts, and a full preview. Arrows select;
Enter, double-click, or Insert insert; Esc and loss of focus dismiss. An empty
library explains where to add templates. Allow retry after an error. Wait for
activation keys to be released before returning to the original field; leaving
the picker during this wait cancels insertion. Preserve the clipboard. Deliver
Unicode, emoji, and paragraphs as text without an Enter shortcut submitting a form.

## Reliability and appearance

Separate UI, data, decision engines, hook services, HID, OCR, and insertion.
Hooks run on dedicated threads without OCR, disk writes, or network requests.
Health probes do not count as physical activity. Unify temporary suspensions:
saving mouse settings or closing one editor must not resume handlers while
another editor or explicit global pause still requires suspension.

Write settings atomically with a validated backup. Validate limits and UTF-8
size before changing files. Restore a corrupt or missing primary from a valid
backup. Invalid replacement files do not replace active settings. PowerToys
import changes only keyboard bindings, retaining mouse, OCR, and templates.
Use fictional examples in a separate profile. Never commit personal settings,
keys, history, screenshots, or diagnostic data.

Follow VISUAL.en.md and the numeric tokens: dark sidebar, light workspace, white
flat surfaces, rectangular buttons, a dark orange primary action, and Segoe UI.
Below 768 px, navigation moves to the top; long content scrolls. Verify 390,
768, and 1440 px, Tab, focus, empty states, and errors without data loss.
Create original assets or use suitably licensed resources; source application
binary assets are not included.

## Implementation sequence and deliverables

1. Establish reproducible build/start commands, three sections, schema, and persistence.
2. Implement and verify keyboard/mouse engines, editors, and Windows services.
3. Add OCR, text actions, shared safe insertion, and templates.
4. Add lighting with explicit handling of absent hardware.
5. Complete acceptance, fix defects, and prepare a portable build.

Suggested stack: C#/.NET Framework 4.x, WinForms, and Windows PowerShell 5.1 for
Windows OCR. Another stack is acceptable with equivalent behavior. Provide a
README with exact build, start, and test commands, settings location, and updates
without settings loss. Supply F01–F40 and A01–A20 verification tables, separately
reporting real hooks, OCR, hardware lighting, and mixed DPI checks. Buttons,
screenshots, and stub-based tests alone do not establish readiness.
