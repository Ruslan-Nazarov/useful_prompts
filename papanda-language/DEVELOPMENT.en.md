# Development, content and maintenance

[Русский](DEVELOPMENT.md)

## Project architecture

Implement these boundaries (directory naming may differ):

```text
App.tsx                 hydration, onboarding and navigation
src/models/             domain contracts
src/constants/          languages, roles and design tokens
src/data/               immutable catalogs and compiled book
src/store/              defaults, validation, migrations, persistence, projections
src/utils/              pure queue, iMW, grouping and comparison algorithms
src/services/           AI transport/pipeline, book lookup, backup/recovery
src/hooks/              cancellable task/editor lifecycle
src/components/         tokens, exercises, book, editors and modals
src/screens/            specification screens
book/                   source materials and original license
scripts/                deterministic book compile and UI harness
tests/                  unit/integration/regression
gemini-proxy/src/        HTTP validation, provider adapters and quota object
gemini-proxy/tests/      mocked upstream and concurrent quota tests
docs/                   architecture, decisions, privacy, recovery and release
```

Do not bury the only iMW/queue/validation implementation in UI components. Use
the same catalog projection after edits/import/undo/hydration. Subscribe components
to relevant state rather than rerendering a large catalog per tap.

## Scripts and CI

Provide book:build (deterministic compile), book:check (read-only freshness check),
type-check, type-check:proxy, test for app/proxy units/integration, check aggregating
these and check:ui running all UI checks against one export. Worker build is dry-run.
CI with Node.js 22+: install both lockfiles, check, mocked web export, all UI checks
and Worker dry-run. Save concise logs/failure screenshots, never real profiles/keys.
Reproduce installation with npm ci. Update Expo/React Native/React together on a
compatible line; re-evaluate overrides/postinstall patches against actual failures.

Automate:

- iMW/zero/corrupt stats, deterministic queue, local days, due/snooze and scoped
  undo preserving unrelated changes.
- Multiple clauses, discontinuous predicates, hints/disputes, repeated added
  tokens and thought-preserving development.
- JSON bounds, UTF-8 backup limit, duplicate keys, corrupt storage, recovery-point
  write failure and restore after restart.
- Malformed AI, missing/duplicate task IDs, bad parts/translation, missing target,
  incomplete audit, bounded repair, fetch/backoff cancellation, stale responses
  after context changes and explicit-task priority.
- Book hashes/IDs/search/addresses/tables/bookmarks/positions, ru/la limitations,
  citations restricted to transmitted sources.
- Worker body/config validation, fallback/timeouts, safe errors and concurrent
  per-install/global budget enforcement.

UI scenarios cover onboarding, navigation, workshop/texts, book, review, sentence
trainer/editor, generation controls, word editing and tours. One static export;
isolated browser profile per scenario; controlled delayed AI phases and blocked
external network. Check 320/390/768/1440 and throttled CPU. Physical APK, native
picker/share/keyboard and live linguistic AI quality require separate evidence.

## Vocabulary and examples

Use sanitized reference/content/words.json with zero counters; never import author
history. Static sentences/chains are instructional content, not user records.
New examples need language grammar, role/POS, surface/parts, meaning, translation
and lemma review. Unknown segmentation stays one word. Begin with a complete
utterance, add details without replacing “sleeps” by “reads” and calling it an
object addition. Track origin/review level; automated validation is not expert
linguistic review. Content updates must not break progress identity.

## Reproducible book pipeline

Supplied: 66 Markdown sources and reference/book/catalog.json. The compiled catalog
can bootstrap reading, but implement your own generator/freshness check. Preserve
sourcePath/sourceHash and chapter/block addressing, never regenerate the author's
book through AI paraphrase. The full original generator is in
reference/book/build-book.cjs.txt; it uses markdown-it/entities and original project
paths, so adapt it rather than calling it as a finished app command.

Compile UTF-8→headings/text/tables with rowSpan/colSpan→stable chapter/block IDs→
source SHA-256→JSON. sourceHash normalizes CRLF to LF, matching the original
generator; manifest.sha256 separately hashes raw file bytes. Enforce LF for generated
JSON via reference/config/gitattributes.example or normalize freshness comparison:
the original strict --check otherwise flags a CRLF checkout as stale on Windows.
Identical inputs must
give identical output. book:check compiles
in memory and compares. Changed blocks may have new IDs; filter stale bookmarks.
Exclude original-site analytics/scripts/filming material. Original docx files are
not required by this package and must not be altered.

## Persistence and concurrency

Validate whole objects before commit. Save recovery point before import; report
success after persistence. Use staging/commit/recovery if transactions are absent.
Replacing progress bumps revision and cancels work; old callbacks cannot commit
into a replaced profile. Undo restores affected fields, not a stale whole object.
Failed migrations must not erase live data.

## Documentation and releases

Generated README: prerequisites, exact commands, offline/online modes, environment,
storage, backups and limitations. docs/architecture.md: ownership/flows;
docs/content.md: catalogs/book/licensing; docs/privacy.md: actual transmitted
data/providers/background behavior/no cloud backup; docs/release.md: SDK, app/native
versions, checks/devices/artifact/hash/limits; docs/decisions.md: deviations.

Report every feature and acceptance ID with implementation and actual evidence.
Do not label blocked/not tested as complete. Deployment instructions do not mean
publication occurred. Before requesting accounts/keys, complete offline code and
independent checks into a reviewable result. Do not include author account IDs,
signing credentials or working private service configuration in a new project.
