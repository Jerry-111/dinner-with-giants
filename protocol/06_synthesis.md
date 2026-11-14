# Synthesis

The run's script aggregates scores first; a lead-writer agent turns that plus the debate record
into a report; an independent reviewer who did not write the report and has not read the debate
checks it; the writer fixes what the review finds. Full instructions:
`templates/rounds/writer.md` (writer), `templates/rounds/review.md` (reviewer).

## Run the aggregate step first

`python3 tools/sim.py aggregate` reads the run folder and writes `summary.json` and `summary.md`:

- per option, R1 and R3 median, quartiles, and rank; rank and flips across the rubric's weight
  sets;
- lever allocations; the distribution of answers to conditional questions; pairwise win rates;
- number of score changes, empty concessions, cases where the intended move (C-round
  `intended_moves`) didn't match the actual R3 change;
- verdict counts (accept/reject);
- the persona-minus-baseline gap, one column per option;
- self-check counts; the judge scorecard's per-dimension distribution.

The report quotes scores and ranks from `summary.md` only — the writer never recomputes them.
The aggregation rules themselves (no headcount as evidence, no weighting by persona, no
extremizing) are pre-registered in `rubric.json`, not decided while writing the report.

## Report structure

See `templates/rounds/writer.md` for the full instructions. In outline:

0. One-page conclusion: what holds up, what's contested, the named questions answered, 2–3 paths
   for the user.
1. Option map: the score table plus a per-option read (stage, what's still open, what's already
   too late, the main disagreement and who holds which side).
2. The user's named questions, answered head-on.
3. What happened in the debate: per-table consensus and disagreement, who persuaded whom, 3–5
   exchanges retold as dialogue with post IDs, minority views kept verbatim, overtime results.
4. Taste axes: systematic disagreement among personas, each axis tied to path dependence; where
   the user's stated interests currently sit.
5. Paths for the user.
6. Exercises for the user: a blind pick over de-identified arguments, and the rank sensitivity
   across weight sets.
7. Comparison with earlier runs, if the scope asks for one — side by side, without rewriting the
   earlier conclusions.
8. How the mechanism performed: verdict distribution, score changes, empty concessions, score
   changes justified only by "others changed," interjections deduplicated, source-challenge
   outcomes, self-checks and their spot-check results, persona-minus-baseline gap.
9. Limitations.
10. Reversal signals.

## Traceability

Every judgment needs a pointer back to its source: a post ID (`B/X3/P4`), a fact-check item
(`evidence/errata_B.md` #n, `audit.md` #n), or `summary.md`. This is the most common gap an
independent review finds — write the citation in on the first pass rather than adding it after
review.

## Independent review loop

The reviewer reads `<run>/report.md` against `summary.md`, the persona-facing scribe notes, the
judge scorecards, `audit.md`, `evidence/errata.md`, and `r3/*.json` — not the writer's working
notes, and not the full (named-persuasion) scribe notes, since the reviewer should be checking
what's verifiable from the same material a careful reader could check. The reviewer writes
`<run>/review.md`: one row per problem, ranked by severity, with the location, the evidence, and a
suggested fix — the reviewer does not rewrite the report directly. The writer resolves every row
before delivery. If time allows, run a second review pass after the fixes land.

## Length

The full report is written for the archive and for future agents to use as context — it can run
long. What the user reads is the one-page reader pack from the next step
(`protocol/07_reader_pack.md`).
