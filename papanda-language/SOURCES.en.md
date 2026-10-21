# Sources and package contents

[Русский](SOURCES.md)

Prepared from the local working language papanda 1.3.0 on 21 October 2026.
Reference repository:
[Ruslan-Nazarov/papanda-language-app](https://github.com/Ruslan-Nazarov/papanda-language-app).
The working copy contains changes beyond Git HEAD; the manifest explicitly records
this. Do not present it as the contents of a particular public commit.

| Material | Origin / processing |
|---|---|
| 2608 words | src/data/words.json; lexical fields only, zeroed progress, parsed translation objects |
| 210 sentences | sentences.json (170) plus offlineSentences.json (40); reset historical dictionary membership; mismatching legacy parts become whole surface words |
| 28 chain steps and 7 comparisons | developmentExamples/comparisonExamples from studyExamples.ts |
| 66 book materials and catalog | book/ and book.generated.json; source Markdown copied unchanged |
| Book generator | scripts/build-book.cjs as a source-text adaptation reference |
| AI templates | Complete aiPrompt.ts, sentencePrompts.ts, sentenceQuality.ts and sentenceCurriculum.ts source text |
| Branding/metrics | Original logo, mascot, theme/role constants, navigation and screen styles |
| fixtures.json | Newly created fictional progress for acceptance |
| RU/EN documents | New reconstruction assignment derived from current behavior |

manifest.json lists counts and SHA-256 hashes. `node tools/validate-kit.cjs` needs
no source project, network or dependencies. Another agent does not need personal
paths/databases, author accounts or the original checkout.

## Original notices

The upstream app's existing root LICENSE is preserved as
reference/UPSTREAM-LICENSE.txt (MIT with its original notice). This is not a new
license for all materials. The book has a **separate** original book/LICENSE
designated Creative Commons BY-NC-ND 4.0, preserved in full under reference/book/.
Display its author/title from catalog.json. Do not apply the app's MIT notice to
the book. Preserve each material's original notices/terms when distributing;
this package does not relicense the book or grant additional permissions.

Book text, general scheme and Russian glosses remain in their original language.
English development specifications do not replace/translate the book. Table UI
adaptation must not rewrite the author's wording. The instructional corpus is not
claimed error-free: transfer/zeroing/JSON validation are not linguistic editing.
Keep authored book, static examples and AI explanations distinguishable.

## Historical descriptions versus current scope

The early PRD and old reports mention removed/unimplemented features. Mandatory
scope excludes language-note canvases, a FastAPI client, automatically sending
reports to the author, daily habits, cloud sync and system TTS. Current
pronunciation is textual AI guidance. The old approximate 170-card count is
replaced by verified 210; 66 book materials include Russian but no Latin chapter.
No personal metrics, real backups, .env, signing keys/tokens/APKs, filming scripts
or internal audits are included in this public assignment.
