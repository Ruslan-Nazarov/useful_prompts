# Behavioral specification

[Русский](SPEC.md)

## 1. Product and method

Local, single-user Android app with web and iOS support. Russian interface and
explanations; practice languages en/it/es/de/fr/kz/la, native gloss ru. Language
labels are in reference/design-tokens.json. No registration or cloud sync is
required. All local modes work without a proxy; online features use build configuration.

The learning unit is a complete thought. Find the entire predicate, then subject,
attributes, objects and circumstances; retain function words. Sentence roles are
not parts of speech. Predicate may include auxiliaries, negation and nominal parts.
Repeated Predicate labels in one clause describe one compound predicate. Do not
force SVO, overt subjects or copulas. Passive subjects can undergo an action.

## 2. Startup and navigation

Wait for persistence validation before opening study UI. Corrupt storage shows
retry without overwriting its old value. First launch has swipeable onboarding,
next/finish/skip; completion persists and can be replayed from settings.
Tab order: Statistics, Words, Sentence Trainer, Recognition, Settings. Start on
the central trainer. Dictionary opens from Words; workshop/book from trainer or
workshop. Nested screens return correctly. Android Back closes the current modal
first. Tabs remain usable during generation. Language changes update dependent
screens and invalidate obsolete work.

## 3. Word cards and dictionary

A card has Russian meaning, source spelling, ordered active translations,
association, favorite, edit and word statistics. Tapping a translation targets that
exact spelling/language in sentence practice. Missing translations are not replaced
with another language's spelling.

A tour completes after N progressed cards, not N renders. Going back works at the
end. Learned marks all active languages. Undo restores only its knowledge change,
preserving shows, favorites, edits, associations and later independent changes.
Buttons/swipes share one action; prevent animation double counting.

Eligible cards have every active translation and are not known in all active
languages. Avoid the previous key when alternatives exist. Weighted random choice:
weight=0.15+1−mean(memoryWeight across active languages). Explain an empty pool.
A card visit increments count/dailyShows once and each active language's show_stats
once; rerenders do not count. Association autosaves after 1500 ms and on leaving,
bound to its original card. Word statistics include total/last/per-language shows.

Dictionary is a virtualized searchable list with count; case-insensitive search
includes source, Russian, all translations and associations. Add/edit source,
Russian meaning, active translations and association. Display edits never rename
the storage key. Reject blank source and duplicate keys. Token additions use the
actual lemma in its language, key user:<code>:<lemma>, preserving internal apostrophes
and hyphens; never reuse another token's meaning. Requested AI verification flags
doubts without automatically rewriting; editing invalidates its previous verdict.

## 4. Recognition and queues

An item is (word key, language). Show Russian/source cue, hide target until reveal.
Known/unknown and right/left swipes update knowledge only for this language and
record one show. Undo restores grade, score and position but retains exposure and
edits. One answer per animation. One summary per completed session; closing starts
a new queue. Once a result is committed, do not recalculate it through old Undo.

Snooze excludes only this pair for 7 days without an incorrect answer or show;
explain/confirm first use. Favorites filter ordinary sessions. Today's review
ignores favorites and provides a return to normal practice. Explain empty queues.

Queue algorithm with injectable random/time:

1. Collect unique translated, unsnoozed pairs; apply favorites or due filter.
2. Split failed (false), fresh (no mark), learned (true).
3. N=session size, K=min(N, configured learned count, learned.length), U=N−K.
   F=min(failed.length,max(ceil(0.6U),U−fresh.length));
   FreshCount=min(fresh.length,U−F).
4. Rank failed/learned by memoryWeight+random()*0.08; calculate noise once before
   sorting. For T selected items shuffle the first max(T+4,3T), then take T.
   Shuffle fresh and take FreshCount.
5. Fill remaining space from unused learned items and shuffle the final queue.
   K is the desired proportion, not a strict upper bound when fresh items run out.

## 5. Statistics and due review

For a word/language pair s=show_stats[lang], k=(knowledge_stats[lang]===true),
d=max(0, days since that language's last_shown_by_lang, fallback last_shown).
If s<=0, weight=0. Otherwise:

```text
exposure=min(1,s/80)
knownFactor=k?1:0.5
stabilityDays=3*(1+s/10)*(k?3:1)
retention=0.35+0.65*exp(-d/stabilityDays)
memoryWeight=exposure*knownFactor*retention
```

Invalid/missing date gives retention=1. Per-language iMW is 100 times mean weight
of shown pairs in that language. Overall iMW averages all shown active-language
pairs, not language percentages. Empty sets yield zero, never NaN. This is a
heuristic study indicator, not objective proficiency or a proven memory model.

Show volume, seen words, language coverage/known counts, known across all active
languages, today's exposures and exposure distribution. Distribution averages
only practiced languages: 0; (0,5]; (5,15]; (15,40]; (40,80]; >80. Charts show
daily exposures, overall/per-language iMW and workout correct counts/success rate.
Sum workouts on the same day; replace the day's iMW with its latest snapshot.
Use device-local calendar days. Opening statistics adds no shows. Record iMW on
app entry/session completion, at most one point per day.

Due means translated, previously shown, unsnoozed, not shown today locally, and
(not known OR weight<0.65). Sort weakest first; reason is uncertain answer or long
since review. Launch a separate review queue with return to ordinary practice.

## 6. Sentence trainer

Tokens remain in reading order. Reveal groups by (clauseIndex,role), finishing
clause 0 then 1 etc. Role order: Predicate, Subject, Attribute, Attribute_Subject,
Object, Attribute_Object, Circumstance, Adverbial, Conjunction, Preposition,
Particle, Article, Other. Skip empty groups; reveal a discontinuous predicate in
one step. Newly annotated cards require all clause indices. Legacy cards may use
an explicitly identified heuristic fallback; a noun conjunction is not a new clause.

Step and full/Flash modes, independent token-translation toggle, role legend and
whole-sentence explanation. Show only given parts; [wholeWord] means segmentation
unavailable. Color encodes role, not mastery. Previous/next, add unknown token and
dictionary-origin targeting work. Deduplicate dictionary-key shows per card/language;
translation toggles, rerenders and returning from explanations do not multiply them.
Refill preserves position; fresh AI series remain coherent; bounded eviction
preserves a usable series/prefix rather than orphaning its middle.

Editor adds/changes source, language and tokens. Reject blank source, unmatched
surface, unknown roles and nonconcatenating parts. Annotation-only changes preserve
metadata. Source changes invalidate stale translation, goal, task/batch links and
explanation cache. Edited built-ins become user overrides without mutating originals.

## 7. Workshop

Modes: independent parsing, growing series, development, languages, personal text.
Changing language/mode cancels old work. Independent parsing begins with a whole
sentence without translation. Select all indices for the current clause/role,
including every predicate part. Compare sets and report missing/extra indices;
advance through core roles and clauses. Function-word roles are taught in full
analysis, not separate grading steps here.

Hint 1 asks about function; hint 2 gives observable forms with validated
evidence(tokenIndex,form). If a marker is undocumented, say so; position alone
is not proof. Translation/book reading counts as help. Attempts record clause,
role, chosen/expected indices, result and maximum assistance 0..2. Disputed answers
are excluded. Separate independent success, assisted success and errors from word
iMW. Recommend a different current-language card containing the role with the
largest (errors+assisted)/total ratio.

Growing series: core→attribute→object→circumstance. Every step is a natural complete
utterance with unchanged subject, predicate meaning/form, tense, polarity and prior
details. Highlight added occurrences while respecting repeated words. Use coherent
AI batchId/chainStep series, otherwise four authored offline examples per language.
Development adds a learner's detail through validated AI with previous/next steps.
Languages shows one thought on seven languages; translating a personal thought is
a separate validated request. Offline examples are supplied in study-examples.json.

## 8. Personal text

Paste paragraph→propose boundaries→edit one sentence per line→explicitly confirm→save.
Up to 10 texts; 1..20 nonempty segments each; <=6000 characters including separators,
<=600 per segment. Read one segment at a time, persist position. Analyze only by
button; bind the result to exact text/language/position and reject late responses.
Saved cards survive restart and backup, work offline. Deletion needs confirmation;
cancel preserves text and cards.

## 9. Book

66 materials: introduction 1, general scheme 8, en/de/it/fr/es/kz 8 each, Russian 9.
Bundle all text offline with author and original license. Method/scheme serve all
languages; explicitly state no Latin-specific chapter and no Russian practice mode.

Section/chapter/heading contents, previous/next chapters, section/global search,
exact-block jump/highlight. Wide tables default to reading cards, with a grid toggle
and internal horizontal scrolling preserving row/col spans. No page-wide side scroll.
Font 15..23 default 17, up to 100 bookmarks and last location in separate persistence;
filter obsolete addresses safely. Exercises open a role rule and return to the same
step with assistance; language chapters open matching practice with a way back.
AI receives actual excerpts with book://chapterId/blockId addresses. Only links
from the transmitted set are supported. A collapsed real-source list remains
available even when AI fails the requested answer format.

## 10. Settings and bounds

| Setting | Default | UI / persistence bound |
|---|---|---|
| Active languages | en,kz,it, in order | Nonempty unique subset of seven codes |
| Tour size | 10 | 5,10,15,20,30,50 / 1..100 |
| Workout size | 10 | 5,7,10,15,20 / 1..100 |
| Desired learned items | 5 | 0,1,2,3,5 / 0..N |
| Favorites only | false | boolean |
| Snooze explanation seen | false | boolean |
| Book font | 17 | 15..23 |
| Bookmarks | empty | latest 100 |
| Structure attempts | empty | latest 500 |
| AI cards | empty | 80, preserve series integrity |
| Workout snapshots | empty | latest 200 |
| iMW snapshots | empty | latest 180 days |

Settings include export/import/recovery, onboarding replay, app/native build version
and confirmed statistics reset. Reset removes shows, knowledge, snooze, charts and
attempts, preserving custom words/texts/analyses, edited translations, associations
and favorites. Explain the exact reset scope.

## 11. Reliability and boundaries

DATA.en.md defines recovery; AI.en.md defines network behavior. Cancellation stops
fetch/backoff/future commits. Explanation cache depends on content and annotation,
not just ID. Built-ins stay immutable and outside backups. Never execute user/AI
strings as HTML/JavaScript.

Textual short/detailed AI pronunciation guidance is required. System TTS, developer
report transmission, language sticky-note canvases from the early PRD, full UI
localization, authentication and cloud sync are separate extensions, not baseline
requirements of this assignment.
