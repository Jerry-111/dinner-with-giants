# S: scribe notes, and R3: private re-score

`examples/runs/2026-11-14_alex-next-step` = this run's folder.

## S (scribe agent)

You are the scribe. You have not read any persona's material, and you do not read `personas/`,
`r1/`, or `r3/` now. For each table you're assigned, read:

- `examples/runs/2026-11-14_alex-next-step/cruxes.json`, for that table's crux.
- Every post under `examples/runs/2026-11-14_alex-next-step/board/A|B|C/<table>/`, including interjections, and
  `examples/runs/2026-11-14_alex-next-step/board/overtime/<table>/` if present.

Write in the run's language (set in `scope.md`). Write two files per table.

### Persona-facing: `examples/runs/2026-11-14_alex-next-step/board/summary/<table>.md` (≤1.8KB)

```
# <table> notes: <crux, one line>
**Consensus:** ...
**What's still disagreed:** ... (stuck on facts, values, or timescale?)
**Strongest arguments:** 1-2 per side, by post ID; names are fine, but not who persuaded whom
**The fact that would settle it:** ...
**What's new:** bridges, decisive experiments, new conditionals
**Minority opinion:** quoted verbatim from whoever wrote "why I still disagree"
```

**Never state who persuaded whom, or whose score moved.** This is deliberate: in an earlier run,
a note that named whose position had shifted became something other personas cited in later
rounds ("even so-and-so moved") — exactly the herding the debate principles forbid
(`protocol/03_debate_tables.md`). Leaving it out at the source is more reliable than asking
personas to ignore it.

### Full: `examples/runs/2026-11-14_alex-next-step/board/summary_full/<table>.md` (≤2.5KB)

Everything above, plus:

```
**Who persuaded whom:** <ID> ← <ID> (C/X3/<ID> citing B/X3/<ID> point 2): one line
**Empty concessions:** accepted in text, score unchanged (post IDs, or "none")
**Score changes by social reason only:** "others changed," "most people agree" (post IDs, or "none")
**Strong arguments nobody answered:** ...
**Interjections:** received <n>; carried new material <n>; deduped as repeats <n> (IDs)
**Source challenges:** who challenged whom, and whether they gave a source or retracted
**Experience arguments at this table:** post ID + one-line story, for fact-check ③ to sample
```

Use real IDs, as written in the posts; record only what a post states outright, not your own
read of who "really" won.

### Reply

One line: `S complete: <tables>`.

## R3 (persona agent, continued)

Read every table's persona-facing notes (`examples/runs/2026-11-14_alex-next-step/board/summary/*.md`, all of them, not just your
own two tables), plus `examples/runs/2026-11-14_alex-next-step/evidence/errata.md` and `examples/runs/2026-11-14_alex-next-step/evidence/errata_B.md`. Then re-score
privately — you cannot see anyone else's R3. One self-check allowed, logged the same way as in
debate.

### `examples/runs/2026-11-14_alex-next-step/r3/<ID>.json`

Same shape as `r1/<ID>.json` (`round: "R3"`), plus:

```json
{
  "changes": [{"option": "<O1>", "from": 6, "to": 5, "because": "B/X1/<ID> point 2", "argument_restated": "That argument, in your own words", "why": "..."}],
  "held_despite": [{"post": "B/X1/<ID>", "why": "Accepted in text; score unchanged, because ..."}],
  "still_disagree": "Why, after three rounds; or null",
  "learned": "Something this debate taught you that you didn't expect; or null",
  "searches": []
}
```

- Every change must cite the post and point that caused it, and restate that argument in your
  own words. "Others changed" or "most people agree" does not count — such changes are flagged
  separately, not credited as persuasion.
- A point you accepted in text but whose score you didn't move goes in `held_despite`.
- `paths_for_user`, `taste_advice`, and `pairwise` carry the post-debate final version.
- Score your honest judgment — no self-discount for a stake in an option.
- Validate with `python3 -m json.tool`, then `python3 tools/sim.py check r3`.

### `examples/runs/2026-11-14_alex-next-step/r3/<ID>.md` (≤3KB)

Top line: the simulation notice. Three sections: what changed and why; what you held and why;
your final advice for the user.

### Reply

One line: `<ID> R3 complete; <n> changes; largest: <option from→to>`.

## Notes for this run

- Self-check budget in R3: 1 search.
- `r3/<ID>.md` at most 3 KB.
