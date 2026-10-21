# Data contracts and persistence

[Русский](DATA.md)

[reference/contracts.ts](reference/contracts.ts) defines independent data shapes,
not runtime validation. Validate all external JSON before mutation. Fictional
examples are in fixtures.json; built-ins are in reference/content/.

## Identity and catalogs

Word has stable `eng` key (a legacy name, not necessarily English), displayed `word`,
ru, translations:Record<code,string> and optional source_language. Missing translation
means missing data. Progress contains count, is_learned (0/1), knowledge_stats,
show_stats, last_shown, last_shown_by_lang, snoozed_until_by_lang, association and
favorite. New records use objects, not serialized JSON strings inside JSON.

userWordProgress[key] holds progress and custom_word/custom_ru/custom_translations/
ai_verification overrides. Project base static/custom definition→progress→edits;
never mutate immutable bases. One custom definition per key. On import, the last
custom record wins, replaces a colliding built-in in projection and does not create
duplicates. Preview reports conflicts.

Token contains text, label, role, parts, translation, dictionary_form,
dictionary_word, is_in_my_dict and clauseIndex. Label is a part-of-speech explanation;
role is a sentence member. dictionary_form is the actual token lemma; dictionary_word
is a resolved catalog key or null. Recompute membership against the current catalog
rather than importing somebody else's personal membership. Persisted `kz` remains
stable; external locale may be kk-KZ.

Sentence has id, canonical language label (English/Italiano/etc.), sentence,
reading-order words, source seed/manual/generated and optional whole Russian
translation, learning goal, marker hints, createdAt epoch milliseconds, generation
task/batch IDs and chainStep. Code-based internal models are acceptable if export
mapping is explicit. New AI cards require clauseIndex on every token; legacy offline
cards may use a labeled heuristic. Parts concatenate exactly to surface text with
case. Surface comparison allows surrounding punctuation/French elision, not reordered,
missing or added words. Syntactic validity does not prove linguistic accuracy;
legacy instructional examples have not all had independent expert review.

## Study records

StructureAttempt: id, sentenceId, language, role, clauseIndex, selected/expected
indices, result correct/incorrect/disputed, maximum hintLevel 0..2 and ISO createdAt.
Keep latest 500, update duplicate IDs, exclude disputed attempts from aggregates.

ReadingText: id/title/language, 1..20 nonempty segments, position and index→Sentence
cards. Up to 10 texts, <=600 characters per segment and <=6000 including newlines.
Position is in bounds. Card keys are decimal segment indices; source text and
language must exactly match the referenced segment. Reject cards for other segments.

Daily keys use device-local YYYY-MM-DD. Counters are safe nonnegative integers;
event timestamps are zoned ISO, not ambiguous local strings. Workout total>=correct>=0;
iMW values stay within 0..100.

## Persistence boundaries

papanda-storage contains only PersistedProgress fields. Built-in words/sentences
remain app assets; derived words/sentences are rebuilt. Load→migrate→validate→project→
open UI. Keep nonpersisted ready/error status. Corruption must not trigger a default
state write over the original value.

Separate storage: papanda-onboarded, papanda-book-reader, papanda-before-import
and installation identifier. Do not persist controllers, transient queues/loading
or secrets. Book state holds fontSize, bookmarks and lastLocation, validated against
actual addresses. Baseline progress backup v1 **excludes** book reader state,
onboarding and install ID; the export UI must say so. A future complete-book backup
requires explicit versioning/migration rather than silently changing v1.

## Backup and recovery

Envelope: `{"app":"papanda","version":1,"exportedAt":"<ISO>","data":<PersistedProgress>}`.
See fixtures.json for a full valid sample. Export a detached deep copy. Import
limit is 10*1024*1024 **UTF-8 bytes**, not JavaScript string length. Validate JSON,
app/version, types, finite bounded numbers, arrays, languages, identities, limits
and cross-record links before mutation. Migrate permitted missing legacy fields
to defaults. Reject unknown versions. Never execute strings or merge __proto__.

Choose file→read/validate→preview counts of words/cards/texts/attempts/progress and
key conflicts→explicit Replace or cancel. Cancellation/preview do not mutate state.
Before replacement, durably save the old progress as the sole papanda-before-import
point with savedAt. Failure to save the point forbids replacement. Cancel old jobs,
atomically replace progress, rebuild projections, clear current exercise/targets
and increment a runtime revision. Serialize imports/recovery. Announce success
only after durable completion. Without storage transactions, implement staging,
commit and startup recovery for interrupted writes.

Recovery validates and restores the saved point, cancels jobs and remains available
after restart. Restoring does not delete it; the next import replaces it. It is
not an unlimited version history and uninstall may remove it. Users need exported
external backups. Web uses download/file selection; native uses picker/share with
clear handling when sharing is unavailable.

## Migrations and updates

Do not rename eng/language codes without migration. Migrations are pure, repeatable
old→new functions with a preserved original snapshot. Convert legacy serialized
stats explicitly and handle corruption deterministically. The legacy empty-key→blind
repair preserves edits, maximum counters and latest timestamps; it is source
compatibility, not a general rule for blank words. Accept legacy sentenceReports
only for migration, not as a reason to recreate removed reporting UI.

Content updates remain separate. User sentence overrides win by ID. AI duplicates
are normalized language+text, not random IDs. The 80-card generated cache must evict
whole series or retain documented usable prefixes, never an orphan middle.
