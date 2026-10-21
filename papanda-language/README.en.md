# papanda — a language learning app

[Русский](README.md)

A complete assignment for an AI agent building a personal app inspired by papanda.
The central activity is understanding a sentence: start with the whole thought,
find the complete predicate, then its subject and additional members. Vocabulary
and review support this practice; the embedded author's book connects rules to exercises.

This is an implementation assignment, not an executable app. Reference project:
[papanda-language-app](https://github.com/Ruslan-Nazarov/papanda-language-app).
Behavioral snapshot: local version 1.3.0, 21 October 2026.

## Contents

| File | Purpose |
|---|---|
| [PROMPT.en.md](PROMPT.en.md) | Complete starting instruction and implementation sequence |
| [SPEC.en.md](SPEC.en.md) | Screens, workflows, algorithms, settings and product boundaries |
| [FEATURES.en.md](FEATURES.en.md) | All 96 mandatory, individually traceable features |
| [DATA.en.md](DATA.en.md) | Models, identity, persistence, backup and migrations |
| [AI.en.md](AI.en.md) | Composition, annotation, auditing, explanations and cancellation |
| [VISUAL.en.md](VISUAL.en.md) | Navigation, role colors, layout and responsive behavior |
| [ACCEPTANCE.en.md](ACCEPTANCE.en.md) | 36 acceptance scenarios and evidence requirements |
| [DEPLOYMENT.en.md](DEPLOYMENT.en.md) | Local setup, Worker, Android, iOS and web |
| [DEVELOPMENT.en.md](DEVELOPMENT.en.md) | Architecture, tests, content pipeline and releases |
| [SOURCES.en.md](SOURCES.en.md) | Provenance, completeness and original source notices |
| [reference/manifest.json](reference/manifest.json) | Counts, provenance and file SHA-256 hashes |
| [reference/design-tokens.json](reference/design-tokens.json) | Numeric visual baseline |
| [reference/contracts.ts](reference/contracts.ts) | Independent TypeScript data contracts |
| [reference/fixtures.json](reference/fixtures.json) | Fictional progress and regression inputs |
| `reference/content/` | Sanitized words, offline sentences and authored development chains |
| `reference/book/` | 66 source materials, compiled catalog and separate book license |
| `reference/ai-prompts/` | Complete original AI instruction templates |
| `reference/config/` | Environment/build templates without author accounts or keys |
| [tools/validate-kit.cjs](tools/validate-kit.cjs) | Dependency-free assignment integrity check |

All assignment documents have Russian counterparts. The book, learning glosses
and fictional progress remain in Russian. Documentation language does not change
the baseline app's Russian interface.

## Build your app

1. Create an empty project folder. Copy this **entire** directory, including
   reference/ and tools/, into it, for example as assignment/.
2. Run `node assignment/tools/validate-kit.cjs`.
3. Give an agent access to files and a terminal. Send the complete PROMPT.en.md,
   identifying the assignment directory.
4. The agent reads everything, plans and implements through acceptance. A plan
   or first screen is not completion.
5. Follow the generated app README. Verify offline operation first; optionally
   configure your own AI proxy and build an Android APK.
6. Require implementation and evidence for every feature and acceptance ID.

You need a computer, Node.js 22+, npm and a coding agent. Cloud EAS is convenient
for Android builds; local Android requires SDK/JDK and local iOS requires macOS/Xcode.
Provider keys, Cloudflare and Expo accounts are needed only for relevant online
features/build services. Internet is needed for the agent and package installation.
Core learning modes and the book work offline.

## Continuing work

> Compare the implementation with SPEC.en.md, DATA.en.md, AI.en.md and VISUAL.en.md.
> Update every FEATURES.en.md row with implementation, check and actual outcome.
> Fix gaps and run ACCEPTANCE.en.md while preserving data and working behavior.
> Buttons, JavaScript exports and mocked AI responses do not prove a tested APK.

> Compare the UI with VISUAL.en.md and reference/design-tokens.json. Check widths
> 320, 390, 768 and 1440, long words, seven languages, keyboard, safe areas,
> book tables, sentence reveal and modal closing.

Different agents/stacks may produce different results. Learning examples and AI
analyses need review; a valid book link does not prove an explanation is correct.
The assignment validator checks this package, not an app that has yet to be built.
The book retains a separate original license; see SOURCES.en.md.
