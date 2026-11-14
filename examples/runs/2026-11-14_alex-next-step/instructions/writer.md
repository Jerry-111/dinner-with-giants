# W: write the report

You are the lead writer for this run. `examples/runs/2026-11-14_alex-next-step` is this run's folder
(`workspace/runs/<YYYY-MM-DD>_<slug>/`, or `examples/runs/<slug>/` for the bundled example). The
report is for the user to read and for future agents to use as context. Write it in the run's
language, set in `scope.md`.

## Read, in this order

1. `examples/runs/2026-11-14_alex-next-step/scope.md` and `examples/runs/2026-11-14_alex-next-step/rubric.json` — the task, the options, the dimensions, the named
   questions and the claims to test.
2. `examples/runs/2026-11-14_alex-next-step/summary.md` — the generated aggregate: scores, ranks, distributions, lever allocations,
   score movement. This is the only place you quote numbers from; don't recompute them.
3. `examples/runs/2026-11-14_alex-next-step/cruxes.json` and every table's scribe notes. **Read `examples/runs/2026-11-14_alex-next-step/board/summary_full/*.md`** (the
   version that names who persuaded whom), not the persona-facing `examples/runs/2026-11-14_alex-next-step/board/summary/*.md`.
4. `examples/runs/2026-11-14_alex-next-step/judge/*.md`, `examples/runs/2026-11-14_alex-next-step/audit.md` (the post-R3 fact-check), and `examples/runs/2026-11-14_alex-next-step/evidence/errata.md` (and
   `errata_B.md`, if present).
5. Every persona's final submission, `examples/runs/2026-11-14_alex-next-step/r3/<ID>.md`. These are short; read all of them. Grep
   `examples/runs/2026-11-14_alex-next-step/r1/<ID>.md` as needed rather than reading every one in full.
6. `examples/runs/2026-11-14_alex-next-step/baselines/*.md`.
7. The debate posts in `examples/runs/2026-11-14_alex-next-step/board/A|B|C/` and `examples/runs/2026-11-14_alex-next-step/board/overtime/`: only the specific exchanges
   the scribe notes point to, and check the original wording before quoting it.
8. Only after all of the above: earlier runs' reports, if `scope.md` asks for a comparison, and
   the orchestrator's own notes, if provided. Use these only for the comparison section — don't
   let them shape anything else.

## Write `examples/runs/2026-11-14_alex-next-step/report.md`

Open with a block stating:

- Personas are simulations based on public material, not the person's own words (full notice in
  `AGENTS.md`).
- How many persona agents and baselines ran, and that they are instances of one model — not
  independent evidence; headcount is description, not support.
- Any other disclosed non-independence or interest relevant to this run (model vendor,
  co-affiliated personas) — see `examples/runs/2026-11-14_alex-next-step/scope.md` and `examples/runs/2026-11-14_alex-next-step/RUN_METADATA.md`.

Then, in order:

0. **One-page conclusion.** What still holds up after debate, what's still contested and exactly
   where it's stuck, a direct answer to each named question in `scope.md`, and 2–3 paths for the
   user. No single line standing in for the whole answer.
1. **Option map.** The score table from `summary.md` (R1 and R3 medians and IQR, rank,
   baselines). For each option: current stage, what's still open, which ways of engaging are
   already too late and why, the main disagreement and who holds which side (by name or ID).
2. **The user's named questions, answered head-on,** one by one, from `scope.md`. If the evidence
   doesn't support the answer the user was hoping for, say so plainly.
3. **What happened in the debate.** The section the user most wants to read. Per table: the
   consensus; what's still disagreed and whether it's stuck on facts, values, or timeframe; who
   was persuaded by which specific point; anything new that came out of it (a bridging question,
   an experiment that would settle it). Pick 3–5 of the sharpest exchanges and retell them as
   dialogue, citing post IDs. Say plainly why whoever wasn't persuaded wasn't. Minority views: if
   someone still disagreed after three rounds, include their own "why I still disagree" verbatim,
   unedited. Overtime results, if any.
4. **Taste axes.** 4–6 axes of systematic disagreement, drawn from the cruxes this run actually
   produced (for example: scale versus mechanism, caution versus speed — use this run's own
   axes, not a fixed list). For each axis: where each persona sits and why, in one line, tied to
   their path dependence. Say where the user's own stated interests (from `scope.md`) currently
   sit on each axis.
5. **Paths for the user.** 2–3 paths, synthesized from personas' `paths_for_user`. Each path: what
   to do in the near term, what to do at the next decision point, how this would read from
   outside, and the signal that it's going wrong.
6. **Exercises for the user.** A blind pick: 5–10 arguments from the debate with names removed,
   posed as pairs, asking the user which one is more persuasive; include an answer key (who said
   it, which taste axis it sits on), clearly marked "don't look yet." A weight exercise: the rank
   differences across the weight sets in `summary.md`, and which single weight change flips the
   ranking.
7. **Comparison with earlier runs**, only if `scope.md` asks for one. State what's the same and
   what changed, and whether that's new evidence, a new mechanism, or a different roster — without
   rewriting the earlier conclusions. List them side by side instead.
8. **How the mechanism performed.** Verdict counts (accept/reject); number of score changes;
   empty concessions; score changes justified only by "others changed" or "most people agree"
   (the scribe flags these); interjections that repeated an existing point and were deduplicated;
   source challenges and whether the challenged party produced an independent source or retracted;
   self-checks run and what the fact-check's spot-check of them found; the persona-minus-baseline
   gap, one column per option — the clearest answer to "what did simulating people add over asking
   the model directly."
9. **Limitations.** Same-model instances; any disclosed interest or non-independence; incomplete
   de-identification (content can reveal identity even with names stripped); whatever this run
   skipped (fidelity test, a full fact-check pass, overtime); known gaps in the source material.
10. **Reversal signals**, last, short: observable facts that would change the conclusion.

Sections 5 and 6 (paths and exercises for the user) together should match the ratio `scope.md`
sets for personal-path content versus domain analysis — check it rather than assuming a fixed
split.

## Writing rules

- Write in the run's language (`scope.md`). Plain, dense, short sentences; keep technical terms
  rather than dumbing them down.
- Mark every judgment by what it is: persona material as `[quoted]`, `[synthesized]`, or
  `[inferred]`; your own judgment as `[writer]`; technical facts cited to the brief or a source.
- Quotes only from text actually read: under 15 English words, at most one quote per source.
- Scores and ranks come from `summary.md` only — never recompute them yourself.
- Every judgment should be traceable: cite a post ID (for example `B/X3/P4`), a fact-check item
  (`errata_B` #n, `audit.md` #n), or `summary.md`. This is the single most common gap found in
  review.
- Show a persona's interests; never write that a score "should be discounted" for them.
- Never a guessed pronoun — names, IDs, or "the user."
- Don't invent conflict between personas, and don't treat a majority of same-model instances as
  evidence.

Reply with one line: `W done: report.md <size in KB>`.
