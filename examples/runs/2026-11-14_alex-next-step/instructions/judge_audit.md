# J judging, and ②③ fact-check: instructions for agents

`examples/runs/2026-11-14_alex-next-step` = this run's folder. Neither kind of agent has read persona material, and neither reads
`personas/` now (except the experience check in pass ③, which reads only dossier sections A, B,
G, I), `examples/runs/2026-11-14_alex-next-step/r1/`, or `examples/runs/2026-11-14_alex-next-step/r3/`. Write in the run's language (set in `scope.md`).

## Judging

Rules: `protocol/10_judge.md`. Key points:

- See names. Read `examples/runs/2026-11-14_alex-next-step/board/A|B|C/<table>/` and `examples/runs/2026-11-14_alex-next-step/board/overtime/<table>/` for your
  assigned tables, plus `examples/runs/2026-11-14_alex-next-step/cruxes.json` and `examples/runs/2026-11-14_alex-next-step/evidence/`.
- Write `examples/runs/2026-11-14_alex-next-step/judge/<table>.md` (≤2KB) per table; write a scorecard per post into
  `examples/runs/2026-11-14_alex-next-step/judge/scores_<batch>.json`, four 1-5 scores plus `flags`.
- Treat experience analogies and data the same way: judge analogies by whether the structure
  matches and whether limits are disclosed; judge data by its source and methodology.
- Flag `not_an_argument` for posts that only cite the other side's interest without engaging
  their evidence; flag `social_reason` for "others changed too." Never weight a score by who
  said it.
- Reply: `J<n> complete: <tables>; most lopsided table: <table>`.

## Fact-check ② (after B, before C; due within 40 minutes)

Rules: `protocol/04_fact_check.md`. Key points:

- Read all A and B posts plus `examples/runs/2026-11-14_alex-next-step/evidence/`.
- Check the 10-15 claims cited most in B, or that drove a concession, against primary sources.
- Sample 20 of the personas' own self-checks: from each post's closing JSON `searches`, open the
  URL, check whether `sentence` actually appears on that page and whether `result` is judged
  correctly.
- Write `examples/runs/2026-11-14_alex-next-step/evidence/errata_B.md`: a table (number, post, claim, verdict, what the primary
  source says, URL); a "needs correction" list; which tables it affects.
- Do not route around a site that refuses access; log "could not access."
- Reply: `fact-check ② complete: <n> claims; confirmed a, partly b, wrong c, not found d;
  sampled <m> self-checks, <k> misread`.

## Fact-check ③ (after R3)

- Read `examples/runs/2026-11-14_alex-next-step/board/C/`, `examples/runs/2026-11-14_alex-next-step/board/overtime/`, and the new claims in `examples/runs/2026-11-14_alex-next-step/r3/*.md` (md
  only, not json) that pass ② did not cover.
- **Experience check**: pull 20 experience arguments from `examples/runs/2026-11-14_alex-next-step/board/summary_full/*.md`; grep
  the matching persona's dossier §A, §B, §G, §I to confirm the story is actually there. List
  what you can't find; relabel it `[inferred]`.
- Write `examples/runs/2026-11-14_alex-next-step/audit.md`: a table; a "needs correction" list; an "experience check" section;
  which tables' conclusions it affects.
- Reply: `fact-check ③ complete: <n> claims; confirmed a, partly b, wrong c, not found d;
  sampled <m> experience arguments, <k> not found`.
