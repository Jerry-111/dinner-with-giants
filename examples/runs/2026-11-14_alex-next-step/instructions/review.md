# Independent review

You did not write the report and have not read the debate. Your job is to find problems in
`examples/runs/2026-11-14_alex-next-step/report.md`, not to rewrite it.

## Read

- `examples/runs/2026-11-14_alex-next-step/report.md`.
- To check against: `examples/runs/2026-11-14_alex-next-step/summary.md`, `examples/runs/2026-11-14_alex-next-step/summary.json`, `examples/runs/2026-11-14_alex-next-step/cruxes.json`,
  `examples/runs/2026-11-14_alex-next-step/board/summary/*.md` (the persona-facing notes — not `summary_full`, so you're checking what
  a reader without debate access could verify), `examples/runs/2026-11-14_alex-next-step/judge/*.md`, `examples/runs/2026-11-14_alex-next-step/audit.md`,
  `examples/runs/2026-11-14_alex-next-step/evidence/errata.md`, `examples/runs/2026-11-14_alex-next-step/r3/*.json`. Spot-check the original posts in `examples/runs/2026-11-14_alex-next-step/board/A|B|C/`.
- The rules: `AGENTS.md`, `examples/runs/2026-11-14_alex-next-step/scope.md`.

## What to check

1. **Numbers.** Every score, rank, count, and verdict tally in the report against `summary.md`.
2. **Attribution.** Where the report says "X believes," check that `r3` or the post actually says
   that; check for agent inference written up as the person's own view; check that evidence
   labels are correct.
3. **Claimed persuasion.** Where the report says "A was persuaded by B," check that the closing
   round actually shows it: a concession in the C round plus the matching entry in R3 `changes`.
4. **Headcount as evidence.** Any claim supported by "most personas think," without disclosing
   that they're the same model.
5. **Quote rules.** Under 15 English words; at most one quote per source.
6. **Ratio.** Does the mix of domain analysis versus personal-path content match what `scope.md`
   asked for.
7. **The user's named questions.** Answered head-on, not dodged.
8. **Earlier runs.** Comparisons present without rewriting the earlier conclusions, if `scope.md`
   asked for a comparison.
9. **Privacy.** Anything from the user's private context (identity, finances, health) that
   shouldn't be here; anything that should have stayed an ID or a placeholder.
10. **Facts.** Anything that conflicts with `audit.md` or `evidence/errata.md`.
11. **Discounting on the reader's behalf.** Any line saying a persona's judgment "should be
    discounted" or "discounted further" for their interest. Interests are shown, never applied —
    see the hard rules in `AGENTS.md`.
12. **Pronouns.** Any guessed "he/she" for a persona or the user.
13. **Independence claims.** Any claim that several tables, or several personas who sat together
    or read the same notes, "converged independently."

## Write `examples/runs/2026-11-14_alex-next-step/review.md`

- A table: number | location (section and subheading) | problem | evidence (file and line/ID) |
  suggested fix.
- Ordered by severity, at most 25 rows.
- One closing line with your overall judgment.

Reply with one line: `review done: <n> items, <k> severe`.
