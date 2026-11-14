# A/B/C and overtime: named debate

`examples/runs/2026-11-14_alex-next-step` = this run's folder. You sit at two tables, listed in `examples/runs/2026-11-14_alex-next-step/tables.json`; each table's
crux is in `examples/runs/2026-11-14_alex-next-step/cruxes.json`. Three rounds in order — A opening, B exchange, C closing — then
overtime for the sharpest pairs.

Every round, everyone writes at the same time. Read only the files this instruction names: do
not list a round's directory, and do not read anyone else's post from the round you are
currently writing. Last round's posts become visible only once this round starts.

Write in the run's language (set in `scope.md`).

## Four principles

1. Argue from your own experience — that's the reason this simulation exists. Judge an
   experience argument by whether the analogy holds; never discount it or average it away.
2. Your interests are shown at the top of every post as fact, not argument, and not a discount.
   Others may challenge your evidence's source; nobody may say "you have a stake, so you're
   wrong."
3. Being persuaded by an argument is the goal; being carried along by headcount or fame is not.
   State exactly which argument changed your mind.
4. Evidence can be self-checked, against a budget, logged, and private by default.

## Every post

- **First four lines:** table/round/your name; `Stance: <card.yaml stance_line>`;
  `Interests: <card.yaml interest_line>`; the simulation notice.
- **At least one experience argument:** what happened (cite the dossier section, with its
  evidence label); what it taught you; why it applies here; where the analogy might break.
- **Rebut an experience argument by breaking the analogy** — say where the two situations
  differ. The other person's identity or interest is not a rebuttal.
- **Respond by post ID** (`A/X3/<ID>`), to the strongest opposing point, not the weakest.
- **Verdicts are per point, binary**: break the other post into specific points; mark each
  `accept` or `reject` in the closing JSON `responses`. No "partial" — split a half-right post
  into an accepted point and a rejected one.
- **Source challenges**: ask "is this evidence yours or your own organization's — is there an
  independent source?" The challenged persona produces one (a self-check is allowed) or retracts
  (`retracted` in the closing JSON).
- **Self-checks**: budget 2 per round at B and C (none at A), 1 per overtime turn, for a specific
  claim only — not to study the field. Log in the closing JSON `searches` (query, url,
  published, sentence ≤15 English words verbatim, for_claim, result). Don't route around a site
  that refuses access; log "could not access." Private until cited in the post.
- **Evidence labels** `[quoted]` `[synthesized]` `[inferred]` on every claim; flag it explicitly
  if it conflicts with the evidence brief or errata.
- **Length:** body ≤400 words, not counting the closing JSON; interjections ≤150 words; overtime
  ≤300 words.

## A: opening

File: `examples/runs/2026-11-14_alex-next-step/board/A/<table>/<ID>.md`, one per table.

```
# <table> · A opening · <persona display name> (<ID>)
> Stance: ...
> Interests: ...
> Simulation based on public material; not the person's own words.

**Claim (one line):** ...
**Argument:** ... (≤350 words, with one experience argument)
**My R1 scores on the relevant options:** <O1> 4, <O2> 9 ...
**What fact would change my mind:** an observable fact
```

Closing JSON: `{"searches": []}`.

## B: exchange

First read both your tables' A posts and `examples/runs/2026-11-14_alex-next-step/board/A/INDEX.md` (one-line claim per table,
generated automatically).

File: `examples/runs/2026-11-14_alex-next-step/board/B/<table>/<ID>.md`, one per table — reply to 1-3 people, including the
strongest opposing post at that table; close with a question to one named persona.

**Interjection (optional):** if a post at a table you don't sit at raises something you strongly
disagree with, and you have an argument or evidence that table hasn't seen — read that table's
posts in full, then write ≤150 words to `examples/runs/2026-11-14_alex-next-step/board/B/<other table>/<ID>_interjection.md`, same
closing JSON shape as B. A scribe discards interjections that only repeat what's already on the
table. **Interjections are capped per table, per side** (default 2) — see
`protocol/03_debate_tables.md` for why.

Closing JSON:

```json
{"responses": [{"to": "<ID>", "post": "A/X3/<ID>", "point": "Which point", "verdict": "accept|reject", "why": "..."}],
 "source_challenge": [{"to": "<ID>", "post": "A/X3/<ID>", "claim": "..."}],
 "question_to": "<ID>",
 "searches": []}
```

## C: closing

First read both your tables' B posts in full (including interjections landing on your tables),
especially anyone who named you, questioned you, or challenged you; then read
`examples/runs/2026-11-14_alex-next-step/evidence/errata_B.md`.

File: `examples/runs/2026-11-14_alex-next-step/board/C/<table>/<ID>.md`:

```
**What I conceded:** ... (whose post, which point, restated in your own words, which score moved)
**What I held, and why:** ...
**My experience argument:** one, with all four parts (may combine with "held")
**Answering questions/challenges:** ... (or "none"; for a challenged claim, give an independent source or retract it)
**What would settle my disagreement with <ID>:** an observable fact or experiment, dated
**Bridge (optional):** a question both sides would find worth answering
**If I'm still in the minority:** why I still disagree (required for anyone still outvoted after three rounds)
```

Closing JSON:

```json
{"responses": [{"to": "<ID>", "post": "B/X3/<ID>", "point": "...", "verdict": "accept|reject", "why": "..."}],
 "retracted": [{"post": "A/X3/<ID>", "claim": "..."}],
 "intended_moves": {"<O1>": -1},
 "searches": []}
```

`intended_moves` is what you expect to change at R3 — compared later against what you actually
change.

## Overtime (only if the orchestrator selects you)

The orchestrator picks the sharpest unresolved pair per table from the scribe notes, for 2-3
turns each. File: `examples/runs/2026-11-14_alex-next-step/board/overtime/<table>/<turn>_<ID>.md`, ≤300 words, same posting rules
as above (header, one experience argument, verdicts per point). **Cross-table replies** also go
here: if your argument was cited or rebutted at a table you don't sit at, you get one reply,
filed into that table's overtime folder.

Closing JSON (no `intended_moves` here — that belongs to C only):

```json
{"responses": [{"to": "<ID>", "post": "C/X3/<ID>", "point": "...", "verdict": "accept|reject", "why": "..."}],
 "retracted": [{"post": "B/X3/<ID>", "claim": "..."}],
 "searches": []}
```

## Reply

After each round, one line:

- A: `<ID> A posted at <table>, <table>.`
- B: `<ID> B posted; interjection at: <table or "none">.`
- C: `<ID> C posted; conceded <n>; held <n>; still in the minority at: <table or "none">.`
- Overtime: `<ID> overtime turn <n> posted at <table>.`

## Notes for this run

- Three tables, four seats each; you sit at two. Overtime is skipped in this example.
- Self-check budget: 1 search per round.
- Posts at most 350 words plus the JSON; interjections at most 120 words, at most one per
  persona per round, only with an argument or evidence not yet at that table.
