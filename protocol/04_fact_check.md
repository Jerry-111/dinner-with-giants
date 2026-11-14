# Fact-checking

Three passes, each run by a fresh agent that has not read persona material or debate posts,
except the experience check in pass ③ noted below.

## Pass ①: evidence brief (before R0/R1)

- When the shared evidence brief (`evidence/brief.md`) is first written, check roughly 15 claims
  most likely to change the ranking: surprising events (acquisitions, launches, scale numbers),
  anything a lever's importance rests on, and field-level numbers.
- Output: `evidence/errata.md`. The brief gets a "corrected after fact-check" pointer at the top
  to the relevant entry; existing entries are never deleted, only corrected.
- Every persona must read this before debate begins.

## Pass ②: in-debate (after B, before C)

- Check the 10-15 claims cited most in the B round, or that drove a concession, against primary
  sources.
- Sample 20 of the personas' own self-checks: open each logged URL, confirm the quoted sentence
  actually appears on the page, and confirm the supports/refutes/unclear call is right. A persona
  who mistook an uncontrolled comparison for a controlled one, for instance, belongs in the
  errata — an earlier run's in-debate check caught exactly this on two load-bearing numbers.
- Output: `evidence/errata_B.md`, read by everyone before C.
- The deadline is load-bearing: this pass has to land before C opens, or its corrections arrive
  too late to change anyone's score. In an earlier run, the in-debate check did not reach the team
  until after the private re-score had already happened, so two corrections to claims that had
  driven concessions never reached anyone's scoring.

## Pass ③: after R3

- Check claims newly cited in C, overtime, and the R3 write-ups (the prose, not the JSON) that
  pass ② did not already cover.
- **Experience check**: sample 20 experience arguments from the full scribe notes
  (`board/summary_full/`); grep the citing persona's dossier — the folder listed in `scope.md` —
  sections A, B, G, I, to confirm the story is actually there. Anything not found gets relabeled
  `[inferred]`, and the report says so. This step reads only those four dossier sections, never
  the persona's domain views or simulated conversation.
- Output: `audit.md`: a table, a "needs correction" list, the experience-check results, and which
  tables' conclusions are affected.

## Rules

- Primary sources only: the original paper or preprint, the official announcement, the
  regulatory filing, the benchmark's own site — not a summary of one.
- Never route around a site that blocks access; log "could not access" instead.
- Four verdict labels: confirmed / partly confirmed / wrong / not found. Call out a wrong number
  explicitly even when the overall claim is otherwise "partly confirmed" — one earlier run buried
  two wrong numbers inside claims it had labeled "partly confirmed," and both slipped into the
  final report because nobody reads past the top-line verdict.
- Fact-checkers never read `personas/` (except the four dossier sections for the experience check
  in pass ③), `r1/`, or `r3/`.
- Write in the run's language (set in `scope.md`).

## Outputs

| Pass | File | Read by |
|---|---|---|
| ① | `evidence/errata.md` | everyone, before debate |
| ② | `evidence/errata_B.md` | everyone, before C |
| ③ | `audit.md` | the lead writer and reviewer |
