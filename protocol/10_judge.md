# Judging

A judge is a fresh agent — no persona material, no debate authorship — that scores every post in
its assigned tables against a fixed rubric.

## Judges see names

Earlier runs tried stripping names before judges read the posts. It didn't work: a post's content
gives the author away anyway — their own organization, their own signature method, their own
well-known positions — and in one such run, most tables still had someone address an opponent by
their real name inside the post body. Anonymizing the byline while leaving the content intact
doesn't remove the name effect, it just hides it from the rubric meant to measure it, and the
resulting judge scores compressed into a narrow band that told the orchestrator little. So judges
read posts with names attached, and the rubric instead forbids weighting by identity directly
(see below) rather than relying on anonymization to do that job.

## What judges read

- `cruxes.json`, for their assigned tables' cruxes.
- `evidence/brief.md` and both errata files.
- Every post at their assigned tables: A, B, C, interjections, overtime.

## What judges do not read

- `personas/` (any persona's own material).
- `r1/`, `r3/` (score submissions).
- Scribe notes (`board/summary/`, `board/summary_full/`) — a judge forms its own view of who
  argued better, not one borrowed from the scribe.

## Per-table verdict: `judge/<table>.md`

Up to 2KB, written in the run's language (set in `scope.md`). Covers:

- Which side's argument is better supported by evidence — "roughly even" or "depends on X" are
  acceptable answers, but say what X is.
- The two strongest and two weakest arguments, by post ID.
- Factual errors or exaggerations, by post ID, with the evidence-brief or errata entry that
  contradicts them.
- Process: did each side answer the other's strongest point; did anyone answer a question
  directed at them; did anyone only post without responding to anyone; was airtime roughly even;
  any unexplained score swing; did interjections stack onto one side.

## Per-post scorecard: `judge/scores_<batch>.json`

```json
{"posts": {"B/X1/P3": {"claim_clear": 4, "evidence_holds": 3, "answers_strongest": 4, "source_independent": 2, "flags": ["source_challenged"]}}}
```

- Four scores, 1-5 each. `answers_strongest` is `null` for A posts — there's nothing to answer
  yet.
- `evidence_holds` treats an experience analogy and a data citation the same way: an analogy is
  judged by whether its structure actually matches and whether its limits are disclosed; data is
  judged by its source and methodology.
- `source_independent`: is the evidence independent of the speaker and their own organization.
- `flags` (optional, any number): `not_an_argument` (named the opponent's interest instead of
  engaging their evidence), `social_reason` (cited headcount or "others already moved" instead of
  an argument), `retracted` (withdrawn after a source challenge), `source_challenged` (raised
  one), `experience_unverified` (filled in later by fact-check ③ when the dossier doesn't support
  the story).

## No weighting by identity

A judge never adjusts a score because of who wrote the post. Interests are visible on the card
for the reader to weigh; they are not a judging input. This is the same rule debate posts follow
(principle 2 in `protocol/03_debate_tables.md`), applied to the judge instead of the debaters.

## Merging batches

Each judge agent covers 3-4 tables. The orchestrator merges every batch's `scores_<batch>.json`
into one `judge/scores.json`, which `tools/sim.py aggregate` reads. A judge's one-line reply:
`J<n> complete: <tables>; most lopsided table: <table>`.
