# Required features

[Русский](FEATURES.md)

96 requirements. Track each ID → implementation path → verification method → actual result. Status: complete/partial/blocked/not tested. These are implementation requirements, not claims that a new app already exists. Details: SPEC.en.md, DATA.en.md, AI.en.md and VISUAL.en.md.

## Startup and navigation

| ID | Requirement |
|---|---|
| F001 | Gate study UI on hydration; storage failure offers retry without overwriting the profile. |
| F002 | Onboarding supports swiping, next, skip and finish; completion survives restart. |
| F003 | Replay onboarding from settings without resetting progress. |
| F004 | Five tabs in the specified order; the central sentence trainer opens first. |
| F005 | Dictionary, workshop and book use nested navigation with return. |
| F006 | Android Back closes a modal first; web actions support keyboard access. |
| F007 | Selection and order of seven languages persist; the last language cannot be deselected. |
| F008 | Changing languages updates all screens and invalidates old tasks. |

## Word cards

| ID | Requirement |
|---|---|
| F009 | One card displays all active translations in configured order. |
| F010 | Memory-weighted selection avoids immediate repetition when alternatives exist. |
| F011 | Finite tours track completed cards, finish, restart and allow return from the end. |
| F012 | A card visit counts once for every active language; rerenders do not add shows. |
| F013 | Learned marks active translations; Undo preserves shows and independent edits. |
| F014 | Association saves after 1500 ms and on leaving, never into another card. |
| F015 | Favorite, editing and detailed word statistics are available on a card. |
| F016 | Tapping a translation opens practice for that word and language. |

## Dictionary and pronunciation

| ID | Requirement |
|---|---|
| F017 | Search all translations, source spelling and associations; show result count. |
| F018 | Add a word with source_language and a stable key without duplicates. |
| F019 | Editing displayed spelling/translations preserves key and progress. |
| F020 | Token lemmas preserve internal hyphens/apostrophes and never use another token’s data. |
| F021 | Missing translations never fall back to another language; blank source words cannot be saved. |
| F022 | AI verification flags doubts without rewriting; editing invalidates the old verdict. |
| F023 | Short pronunciation help is at most 60 words; detailed mode has a separate cache. |
| F024 | Closing/changing a word cancels pronunciation help; errors offer retry. |

## Recognition and review

| ID | Requirement |
|---|---|
| F025 | Target answer stays hidden until revealed; buttons and swipes have equivalent grading. |
| F026 | Unique word/language queue follows the failed/fresh/learned selection algorithm. |
| F027 | Exclude missing translations and snoozed pairs; explain an empty queue. |
| F028 | One answer per animation; grade/show updates only the current language. |
| F029 | Undo restores grade, score and position while preserving shows and edits. |
| F030 | Snooze the current pair for 7 days without a wrong answer/show; confirm the first use. |
| F031 | Store one summary per finished session; closing starts a new queue. |
| F032 | Favorites filter normal practice; today’s review ignores it and offers a return. |

## Sentence trainer

| ID | Requirement |
|---|---|
| F033 | Keep tokens in reading order and reveal clause/role groups in STRICT_ORDER. |
| F034 | Reveal multiword/discontinuous predicates together within their clause. |
| F035 | Step/Flash modes, translation and legend work without leaking hidden answers. |
| F036 | Show only supplied parts; missing segmentation is not claimed as indivisibility. |
| F037 | Recompute dictionary membership and add words from the current token. |
| F038 | Count one dictionary-key exposure per card/language despite repeated tokens/renders. |
| F039 | Queue keeps position on refill; bounded cache preserves coherent series. |
| F040 | Editor validates text/tokens; text changes invalidate stale metadata and explanation. |

## Workshop

| ID | Requirement |
|---|---|
| F041 | Five modes; changing mode/language cancels the old request. |
| F042 | Select the full set of role tokens, including every predicate part. |
| F043 | Checking shows missing/extra indices and progresses through clauses. |
| F044 | Hints give a role question, then validated marker evidence; missing evidence is explicit. |
| F045 | Translation/book rules count as help; disputed answers are excluded from aggregates. |
| F046 | Next exercise prioritizes a weak role in the current language. |
| F047 | Growing series preserve the thought, highlight new occurrences and have offline fallback. |
| F048 | Extend a thought and compare it across seven languages using offline examples and validated AI. |

## Personal texts

| ID | Requirement |
|---|---|
| F049 | Paragraph splitting proposes editable boundaries rather than accepting them automatically. |
| F050 | Explicitly confirm segment boundaries before saving. |
| F051 | Limit to 10 texts, 20 sentences, 6000 total characters and 600 per sentence. |
| F052 | Read one segment at a time and restore position after restart. |
| F053 | Analyze only by explicit action and bind results to exact text/language/position. |
| F054 | Saved analyses work offline and are included in backups. |
| F055 | Navigation/deletion cancels work; late responses cannot resurrect deleted text. |
| F056 | Confirm deletion; cancellation preserves text and cards. |

## Book

| ID | Requirement |
|---|---|
| F057 | All 66 materials, author/title and separate license are available offline. |
| F058 | Section/chapter/heading contents and adjacent-chapter navigation. |
| F059 | Section/global search opens and highlights the exact block. |
| F060 | Tables support cards or internally scrolling grids with merged cells. |
| F061 | Font size 15..23, up to 100 bookmarks and reading continuation after restart. |
| F062 | Open a rule from an exercise and return to the same step marked assisted. |
| F063 | Open practice from language chapters with return; explain ru/la limitations. |
| F064 | Stable addresses/hashes, safe stale-bookmark filtering and unchanged source text. |

## AI and concurrency

| ID | Requirement |
|---|---|
| F065 | Worker-only secrets; validated HTTP/body/config and normalized {text} response. |
| F066 | SQLite Durable Object enforces atomic quotas; fallback/timeouts are bounded. |
| F067 | Composition → annotation → local validation → independent audit. |
| F068 | At most one repair round; invalid development chains are regenerated together. |
| F069 | Requested lexeme is present; task IDs, order and duplicates are validated. |
| F070 | Expose phases/cancel; fetch/backoff/validation remain interruptible; stale commits are rejected. |
| F071 | Explain the predicate/core first, collapse word details/sources and use actual book links. |
| F072 | Bounded background work, foreground priority, clear data disclosure and offline fallback. |

## Statistics

| ID | Requirement |
|---|---|
| F073 | Volume, seen words, coverage, known by language and known across active languages. |
| F074 | Exposure distribution averages practiced languages using specified boundaries. |
| F075 | Exact iMW formula, safe zero cases and overall averaging across studied pairs. |
| F076 | Local-day counters/dates; opening charts does not create learning events. |
| F077 | Latest iMW snapshot per day; history capped at 180. |
| F078 | Daily workouts aggregate correct/total and success rate; retain at most 200 summaries. |
| F079 | Due review excludes today/snooze/missing translation, ranks by weight and explains reasons. |
| F080 | Structure skills separate independent/assisted/errors; iMW is not claimed as objective proficiency. |

## Data and recovery

| ID | Requirement |
|---|---|
| F081 | Built-in catalogs are separate from progress; new profiles never inherit author history. |
| F082 | Runtime validation/migrations precede commits; stable keys and shared projections. |
| F083 | Version-1 export with app/version/exportedAt and detached declared progress fields. |
| F084 | Import up to 10 MiB UTF-8; validate linked texts/numbers/languages and conflicts. |
| F085 | Preview/cancel do not mutate data; explicit replacement describes its scope. |
| F086 | Save restore point first; failure blocks import; serialize recovery operations. |
| F087 | Recovery works after restart, resets runtime state and cancels old tasks. |
| F088 | Confirmed statistics reset preserves content, edits, associations and favorites. |

## Interface and delivery

| ID | Requirement |
|---|---|
| F089 | Follow design tokens; role colors remain independent of brand accent. |
| F090 | Handle 320/390/768/1440 widths, long words, seven languages, safe areas and keyboards. |
| F091 | Scrollable modals with reachable close; accessible hidden/selected/disabled states. |
| F092 | Book/offline practice require no key; user text is never executed. |
| F093 | Lockfiles, CI, pure algorithms and mocked network with reproducible commands. |
| F094 | Document setup, development, content, privacy, recovery and release for a new owner. |
| F095 | Use owner-specific identifiers/env/signing; distinguish APK from JS export in reports. |
| F096 | Report all F/A IDs with actual evidence, limitations and source licenses. |
