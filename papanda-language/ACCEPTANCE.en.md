# App acceptance

[Русский](ACCEPTANCE.md)

36 scenarios. Use an isolated test profile and fictional fixtures.json. Record environment, inputs, actual actions, expected/observed outcome and evidence. Unit tests, web, physical Android/iOS and live AI are separate evidence categories. Never mark a blocked step passed.

## A01. Clean start and replay

F001–F003. Start with empty storage, finish/skip onboarding, restart and replay from settings; progress remains.

## A02. Corrupt storage

F001,F082. Inject invalid JSON/types; show error/retry and preserve the original stored value.

## A03. Navigation and languages

F004–F008. Visit all tabs/nested screens and Back; select/reorder languages, restart and verify the last cannot be removed.

## A04. Word tour

F009–F016. Complete a 5-card tour, return from its end and restart; verify ordered languages, eligibility and no rerender overcount.

## A05. Scoped undo

F013,F015,F027,F029. Grade a word, edit translation/association/favorite, then Undo; only grading rolls back, independent edits/shows remain.

## A06. Association on navigation

F014. Type and leave before 1500 ms; return/restart; text belongs only to its original word.

## A07. Dictionary

F017–F022. Add from a Kazakh/German token, search by translation/association and edit; stable key, no duplicates/false fallback.

## A08. Pronunciation

F023,F024. Mock short/detailed cache, error/retry and close with late response; stale output never appears.

## A09. Queue and grading

F025–F028. Use fixed time/random and failed/fresh/learned/missing/snoozed data; verify selection, hidden answer, button/swipe parity and one grade.

## A10. Snooze

F030. Snooze a pair for 7 days; another language remains eligible; no show/error added; test both sides of expiry.

## A11. Summaries

F031,F078. Finish two sessions on one day; one snapshot each and summed total/correct; fixtures yield 15/11.

## A12. Today review

F032,F079. Test yesterday/today, low/high weights, missing/snoozed and nonfavorites; plan matches queue and review can exit.

## A13. Groups and morphology

F033–F036. Check both negative fixtures: whole predicates, no mixing clauses, concatenating parts and working Flash/translation.

## A14. Dictionary from a sentence

F037,F038. Repeat a word twice and reveal/translate/rerender; one exposure and correct lemma addition without duplicates.

## A15. Series integrity

F039,F068. Refill and overflow cache; preserve position and coherent usable series after eviction.

## A16. Editing and cache

F040,F071. Change annotation and source with the same ID; explanation refreshes and stale metadata disappears.

## A17. Independent parsing

F041–F045. Select an incomplete predicate, inspect missing/extra, use hints/translation/book and return; disputed excluded, assistance counted.

## A18. Weak role

F046,F080. Seed independent/assisted/incorrect/disputed attempts; verify aggregates and next-role recommendation.

## A19. Development and comparison

F047,F048. Offline four-step chains for every language and seven comparisons; highlight new occurrences; AI extension preserves the basis.

## A20. Personal texts

F049–F056. Propose/edit/confirm boundaries, test limits, analyze a segment, cancel a late request, restart/backup and cancel/confirm deletion.

## A21. Book completeness

F057,F058,F064. Offline open all 66 materials, verify author/license/hashes/headings; stale bookmark is filtered.

## A22. Search and reading

F059–F061. Search did/кітап in section/global scope, exact jump, wide table at 320 px and font/bookmark/restart persistence.

## A23. Book ↔ practice

F062,F063. Open role rule, return to same step with assistance; practice from a language chapter and return; explain ru/la.

## A24. Worker

F065,F066. Mock invalid body/config/provider, chunked limit, 429/timeout/fallback; concurrent requests cannot bypass quota and responses expose no secrets.

## A25. AI pipeline

F067–F069. Test full batch and bad JSON/parts/translation/task IDs/audit/required lexeme; at most one repair and no unvalidated cards saved.

## A26. Cancellation and load

F070,F072. Delay every phase/backoff and throttle CPU; tabs/cards/cancel remain usable, target wins and import/reset reject stale responses.

## A27. Explanation and citations

F071. Two layers and actual passages; invented/third citation triggers repair; unsupported links removed and actual sources remain.

## A28. Statistics mathematics

F073–F080. Freeze time: formula/empty profile/zero shows/known/unknown/bad date; fixture weight; distribution boundaries and local midnight.

## A29. Backup round trip

F081–F085. Export → preview → cancel → commit → reload; compare declared fields, conflicts and exclusion of built-in corpus/bookmarks from v1.

## A30. Failure and recovery

F084,F086,F087. Test 10 MiB UTF-8, unknown version and invalid links; restore-point write failure leaves data intact; serialized imports; recovery after restart.

## A31. Migration and reset

F082,F088. Legacy stats/key and duplicate imports; confirmed reset preserves custom content, translations, associations and favorites.

## A32. Visual acceptance

F089–F092. Screenshots at all widths with 7 languages, long forms, keyboard/Back/safe areas/tables/modals; accessibility and offline behavior.

## A33. Clean installation

F093,F094. Fresh checkout installs both lockfiles, runs checks, one web export/all UI and Worker dry-run; README commands reproduce.

## A34. Native release

F095,F096. Owner-specific APK with correct env/package/signature, versionCode/SHA-256; install/upgrade and verify native backup picker/share.

## A35. Separate live AI

F065–F072,F096. With owner service test EN/KZ, cancellation and errors; record model/date/quota/limitations, never present mocks as live checks.

## A36. Handoff

F094,F096. A new reader can launch offline and understand AI setup, recovery, book updates and all F/A statuses without author credentials.

## Completion criteria

Every F-ID has implementation/evidence; every A-ID has a result. Offline readiness requires local scenarios and mocked network scenarios. Network readiness additionally requires A35 against the owner’s service; a verified APK claim requires A34 on a device. Missing accounts/devices do not remove implementation/documentation requirements, but limit what can be verified.
