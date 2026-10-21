# Build papanda — a language learning app

[Русский](PROMPT.md)

You are a mobile app developer. Build a standalone local app inspired by language
papanda in the current project. Always spell `papanda` lowercase. This assignment
is independent of the time management app with the same name.

## Read first

Locate this assignment and fully read SPEC.en.md, FEATURES.en.md, DATA.en.md,
AI.en.md, VISUAL.en.md, ACCEPTANCE.en.md, DEPLOYMENT.en.md, DEVELOPMENT.en.md,
SOURCES.en.md and reference/contracts.ts, fixtures.json, design-tokens.json and
manifest.json. Inspect learning chains, the book introduction/general scheme and
complete original AI templates. Run `node tools/validate-kit.cjs` from the assignment.
Plan entities, relationships, screens, phases and checks; then implement.

Documents cover complementary aspects: SPEC behavior, DATA invariants, AI requests
and trust, VISUAL presentation, FEATURES/ACCEPTANCE completeness and evidence.
Record genuine conflicts and decisions. Do not replace the requirements with
a generic “dictionary, flashcards, AI” feature list.

## Learning principle

Understand how words express one whole thought. Begin with the complete sentence,
find its entire predicate, then subject and additions. Do not require memorizing
all words first. Sentence members differ from parts of speech. A compound predicate
may have multiple separated words; subjects may be implicit. Preserve each
language's grammar instead of imposing universal SVO order or an explicit copula.

## Required implementation

1. Onboarding explains method, roles, words and review; next/skip/finish/replay.
   Gate learning screens until validated progress has loaded.
2. Five tabs: statistics, words, central sentence trainer, word recognition,
   settings. Dictionary, workshop and book use nested navigation with return.
3. Seven practice languages en/it/es/de/fr/kz/la. Persist active language selection
   and order; keep at least one. Russian is the explanation language and a book
   section, not an eighth practice language.
4. Word cards show translations together, finite tours, weak-memory priority,
   favorites, associations, edits, scoped undo and word/language-specific practice.
5. Dictionary searches translations and associations, adds/edits words with stable
   storage keys, shows per-language statistics and offers requested AI verification.
6. Recognition hides answers, supports known/unknown buttons and swipes, undo,
   7-day snooze, session size, learned proportion, favorites and today's review.
   Implement the exact queue and iMW algorithms in SPEC.en.md.
7. Trainer preserves reading order while revealing clause/member groups, supports
   step/Flash/translation/morphemes, dictionary links, queues and validated editing.
8. Workshop supports independent token selection, graded hints with observable
   markers, disputed answers, growing series, extending thoughts, seven-language
   comparisons and next exercises targeting weak roles.
9. Personal texts use editable, explicitly confirmed sentence boundaries, one
   segment at a time, requested AI parsing and persistent positions/cards.
10. Embed all 66 supplied book materials offline: contents/search/exact block links,
    cards/tables/font/bookmarks/resume and rule↔exercise links with assistance
    tracking. Latin has no dedicated book section.
11. Use an owner-controlled server proxy for composition→annotation→local checks→
    independent audit→bounded repair. Explain with actual book passages, core first,
    collapsible word details and sources; provide short/detailed pronunciation
    guidance. Show phases/errors/cancel and reject stale asynchronous results.
12. Keep local progress separate from built-in content. Provide previewed/validated
    backup import, a pre-import recovery point and a safe statistics reset.
    Never initialize a new profile with the original author's learning history.

## Engineering

Reference compatibility line: Expo SDK 54, React Native 0.81.5, React 19.1,
TypeScript, React Navigation, Zustand, AsyncStorage and a Cloudflare Worker with
a SQLite Durable Object. This is a source snapshot, not a latest-version claim.
You may choose a supported compatible line after documenting the choice and
checking official APIs. Do not mix incompatible SDK dependencies. Produce native
Android code, web for convenient validation and an iOS-compatible implementation.

Separate UI, pure study algorithms, base catalogs, progress, book content, AI
transport and server adapters. Commit dependency lockfiles. Supplied contracts
and datasets are inputs, not the finished application architecture. Reassess
dependency overrides/patches instead of copying historical ones blindly.

AI is optional for startup, offline examples, authored chains and the book.
Explain an unavailable online action without losing the exercise. Provider keys
stay server-side. Use your own endpoints, accounts, project IDs and signing keys.
EXPO_PUBLIC variables are client-visible. Personal text is sent only on its
requested analysis action; disclose automatic example prefetch separately.

## Complete the work

1. Build an offline vertical slice: hydration→language→sentence→dictionary→answer→
   restart with preserved data.
2. Finish all learning modes, statistics, editors and settings; integrate book links.
3. Implement export/preview/import/recovery/migrations and failure handling.
4. Implement proxy and AI protocol with mocks; test a real service separately when
   owner configuration is available.
5. Finish VISUAL behavior and all automated/acceptance checks.
6. Deliver launch/development/deployment docs, .env.example, CI and evidence report.

Phases do not authorize stopping at a prototype. Do not present plans as delivery
or screen labels as proof. State concrete account/hardware blockers and continue
independent work. A JavaScript export is not a verified APK.

Deliver app/proxy sources and lockfiles; attributed offline content; exact setup,
data, recovery, development and release instructions; all F-IDs with implementation,
check and actual status (complete/partial/blocked/not tested); all A-ID results,
commands and environment. Provide an APK with version/SHA-256 when the environment
permits. List physically verified devices and unverified platforms separately.

Main acceptance: I can parse offline, add a word, review, read its rule, save my
text, restart and find my progress, position and links. With configured AI I get
validated new examples, can cancel waiting and never lose local data to network failure.
