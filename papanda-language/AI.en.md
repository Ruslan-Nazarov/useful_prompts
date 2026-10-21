# AI protocol and result trust

[Русский](AI.md)

Complete reference templates are in reference/ai-prompts/*.ts.txt. They contain
TypeScript interpolations and are not runnable modules. Implement equivalent
builders; never send literal `${...}` placeholders. aiPrompt defines explanations
and short/detailed pronunciation; sentencePrompts defines composition/annotation
and language constraints; sentenceQuality defines independent audit;
sentenceCurriculum defines tasks. These assignment specifications take precedence
over historical implementation comments.

## Transport and server

Client knows only EXPO_PUBLIC_GEMINI_PROXY_URL ending /v1/generate. Empty means
offline. POST JSON with Content-Type application/json and X-Install-Id, body:

```json
{"prompt":"...","provider":"gemini","generationConfig":{"temperature":0.2,"maxOutputTokens":4096,"responseMimeType":"application/json","responseJsonSchema":{"type":"object"}}}
```

Optional provider is gemini/cerebras/groq. HTTP 200 returns {text}, not a trusted
card. Errors have safe error text, code, retryable and optional daily flag. Use
400/413 for validation/size, 429 for quota, 502/504 for upstream failure/timeout;
support OPTIONS and GET /health without secrets/raw private upstream responses.

Limits: body 256000 bytes, including chunked; prompt 1..60000 characters;
temperature 0..2, topP 0..1, maxOutputTokens 1..16384; thinkingBudget 0..8192,
includeThoughts boolean, responseJsonSchema object, responseMimeType application/json.
Reject unknown providers. Gemini uses its native parameters; Cerebras/Groq adapters
use chat completions with schema instructions/JSON object mode. If object mode
requires an object, wrap arrays in documented {items:[...]} and normalize at the
adapter boundary instead of requesting incompatible top-level arrays.

Keys stay in GEMINI_API_KEY/CEREBRAS_API_KEY/GROQ_API_KEY Worker secrets.
DEFAULT_PROVIDER/model names are server configuration. Choose supported models
from provider documentation at deployment; snapshot names do not promise availability.
At most one configured fallback provider per admitted request. Upstream attempts
time out after 20 s, client attempts after 45 s. Client makes at most four attempts
with cancellable min(1500*2^(attempt-1),10000) ms pauses. Do not retry daily quota,
retryable=false or ordinary 4xx; bound retries for transient network/408/permitted 429.

SQLite Durable Object QUOTA/QuotaLimiter, migration v1-quota, atomically reserves
per-install hourly/daily and global daily budgets: initial configurable 40/200/1500.
Concurrent requests cannot exceed global quota. Rejected requests do not consume
global budget; one admitted request counts once even with fallback. This counts
client requests, not tokens/all upstream calls. Use UTC hour/day server windows,
distinct from local study days. Install IDs are client-controlled identifiers,
not authentication; CORS is not access control. Global budget is mandatory; never
imitate authentication with a secret embedded in a public app.

## Sentence pipeline

Default batch 8, permitted size 1..20. Sequence: core, attribute, object,
circumstance, negative, reading, question, complex. First four ordinary tasks
develop one thought. Plan backwards from a natural optional-object sentence to a
complete core. A requested word makes task-1 usage; use the lexeme/expression
naturally, including questions/negation/multiple clauses if appropriate. Other
tasks do not develop usage. Dictionary supports lemma lookup, not random-word
scene construction or grammar-level inference.

1. COMPOSE_SENTENCES receives task IDs/focus/goal/develops, prior accepted context,
   avoidance list, target and feedback. Return taskId+sentence without annotation.
   Reject unknown/duplicate/missing IDs, blank source and >600 characters.
2. REVIEW_AND_ANNOTATE receives unchanged drafts/tasks/language rules/actual book
   passages. Return same text/taskId, review natural/taskFit/analysisReliable=true,
   whole grammatical Russian translation and tokens. Omit doubtful cards; this
   pass may not change source spelling.
3. Local validation checks shape/language/unchanged source/token coverage/roles/
   clause indices/lemmas/parts/duplicates/requested lexeme/task fit and chain
   preservation. Preserve task order even if model order differs. Chunk large
   catalog work so UI/cancel remain responsive. Schema does not prove meaning.
4. AUDIT_SENTENCE_CARDS is a separate call given completed cards/context/tasks,
   without annotator self-assurance. Require exactly one verdict per candidate:
   taskId, natural, translation, roles, morphology, chain, reason. All five booleans
   must be true. Missing/duplicate/malformed verdicts mean rejection.
5. At most two rounds total: initial plus one repair with concrete feedback.
   Reconsider a failed chain together, never join scenes. Preserve a longer
   previously validated prefix over failed shorter repair. Accepted independent
   cards remain useful; do not fill quotas with weak data. Targeted generation
   fails unless task-1 contains the requested lexeme.

Check compound/separated predicates, predicate negation, nominal predicates,
implicit subjects, passive subjects, case/agreement, French elision, German verb
frames, Kazakh bare objects/analytic negatives and Latin cases. A prepositional
location is not automatically an object. Articles are not “this/one”; auxiliary
do is not lexical “does”; Қыз ұйықтаған жоқ translates as “Девочка не спала”,
not a concatenated participle/“нет”. Whole Russian translation preserves meaning,
tense and polarity in grammatical Russian; token glosses explain source structure.

## Explanations and book grounding

Provide exact sentence/translation/current tokens, clauses, roles, lemmas and
parts. Locally select up to 11000 characters of method/general scheme/relevant
language/role and lexical-marker passages, each with real chapterId/blockId and
book:// URL. For Latin identify the general-method fallback, not a nonexistent chapter.

Explain this phrase calmly in Russian: entire predicate first, subject and useful
additions, observable evidence. No compulsory praise, abstract conclusion or full
word passport in the main narrative. Collapsible “words and endings” holds all
word/function-element detail; legacy unsplit answers remain readable. At most two
book links overall. A collapsed transmitted-source list is available independently
of model format compliance. Clearly label output as AI explanation.

Whitelist links against exactly transmitted addresses. Invented/excess links,
HTML, tables or untranslated grammar terms trigger one repair including the prior
answer and specific defects. Then strip unsupported links. Never attribute AI
claims to authored text; retain actual source list even if layered formatting fails.
Valid link existence does not verify correct rule application.

Pronunciation is textual: short Russian spelling/stress and at most two tips,
<=60 words; detailed mode separately. Cache by exact word/language/mode. Closing
or changing cards cancels requests; errors offer retry.

## Concurrency, prefetch and privacy

Every task owns AbortSignal and context revision: language/mode/card/content/
annotation/text position. Check revision at each commit. Close/change/delete/cache
clear/import/reset invalidates old responses. Coalesce identical background jobs
where useful; explicit target tasks own transport and priority. All tabs/card
actions/cancel stay responsive. Explanation cache includes content/annotation/
reveal context, not ID alone.

With configured AI, prefetch is single-flight, checks no more often than every
25 s, tops up below 6 generated cards per active language, batch 8, sequential
languages with 2 s gaps. Errors preserve offline queues. Restrict work to active
app lifecycle and disclose background requests. Do not prefetch personal reading
texts, associations or whole progress. Send personal source only on its analysis
action. Privacy docs list actual payloads/providers. Cancel stops local waiting
and writes; it cannot recall already transmitted text or promise quota refunds/
stopped upstream computation.
