# Debate tables

Debate tables sit between independent scoring (R1) and private re-scoring (R3). Personas who
disagree argue it out, in the open, under their own names, across several structured rounds,
seated at tables built around one specific disagreement (a crux) rather than a free-for-all.

## Four principles

1. **Experience is a legitimate argument.** A persona may argue from what they lived through.
   Judge an experience argument by whether the analogy holds, not by discounting it or averaging
   it against other views. A protocol that discounts lived experience by default ends up
   indistinguishable from asking the underlying model for advice directly — the persona layer
   loses its point.
2. **Interests are shown, never used as an argument or a discount.** A persona's stake in an
   option is a dated fact, printed at the top of every post. It is not a rhetorical weapon
   ("you only say that because...") and not a reason to shave points off a score, including one's
   own. Readers weigh interests themselves; the protocol does not pre-weigh them.
3. **Persuasion by argument yes, herding by numbers or names no.** A score should move because a
   specific argument held up, cited by post ID — not because many people moved, or because of who
   moved. Multi-round, back-and-forth debate is kept specifically because it gives real
   persuasion room to happen; cutting rounds short to save time cuts into the thing the protocol
   is trying to produce.
4. **Evidence can be self-checked, on a budget.** A persona may look something up mid-debate, but
   only to verify one claim already on the table, not to study the field. Each check is logged
   (query, URL, date, a short verbatim sentence, which claim it bears on) and private until the
   persona chooses to cite it. A hard ban on checking pushes everyone back to re-arguing the same
   shared brief round after round; an earlier run that banned self-checks during debate saw zero
   new sources across more than 130 posts. An unlimited budget has the opposite failure: it turns
   a persona into a research analyst wearing a costume.

## Steps

| Step | What | Who | Output | Template |
|---|---|---|---|---|
| R0 | Card extraction | Persona agent | `card.yaml` | `templates/rounds/r0_card.md` |
| R1 | Independent scoring | Same persona agent, continued; baselines | `r1/<ID>.json`, `.md`; `baselines/` | `templates/rounds/r1.md`, `baseline.md` |
| X | Crux map and seating | Fresh agent, no persona material | `cruxes.json`, `tables.json` | `templates/rounds/crux.md` |
| A | Opening | Persona agent, continued | `board/A/<table>/<ID>.md` | `templates/rounds/debate.md` |
| B | Exchange (+ interjections) | Persona agent, continued | `board/B/<table>/...` | `templates/rounds/debate.md` |
| ② | In-debate fact-check | Fresh agent | `evidence/errata_B.md` | `protocol/04_fact_check.md` |
| C | Closing | Persona agent, continued | `board/C/<table>/<ID>.md` | `templates/rounds/debate.md` |
| S | Scribe notes (two versions) | Fresh agent, no persona material | `board/summary/`, `board/summary_full/` | `templates/rounds/r3_scribe.md` |
| OT | Overtime | Persona agent, continued; sharpest pair only | `board/overtime/<table>/...` | `templates/rounds/debate.md` |
| R3 | Private re-score | Persona agent, continued; baselines | `r3/<ID>.json`, `.md` | `templates/rounds/r3_scribe.md` |
| ③ | Post-R3 fact-check | Fresh agent | `audit.md` | `protocol/04_fact_check.md` |
| J | Judging | Fresh agent | `judge/<table>.md`, `judge/scores_<batch>.json` | `templates/rounds/judge_audit.md` |

Fact-check pass ① (the evidence brief) runs before R0/R1; see `protocol/04_fact_check.md`.

## Seating

Table size and seats per persona are parameters, not constants: `rubric.json` `seating.table_size`
(default `[4, 6]`) and `seating.seats_per_persona` (default `2`). Target table count is about
`n_personas × seats_per_persona ÷ average(table_size)` — for 16 personas at the defaults, roughly
6-7 tables.

Rules the crux agent (X) applies, and `tools/sim.py tables` checks:

- Both sides of the crux are present at the table, in roughly equal numbers.
- Every persona sits in the minority (or against their own table's majority) at least once
  across their seats.
- A `not_independent` group (`rubric.json`) is never the sole representative of one side of a
  table.
- Seat only personas with an actual stake in the crux: a R1 score on its options, or a `cruxes`
  entry that raised it. Anyone else who sits in does so as an observer, labeled as such in
  `tables.json` `why`; judges weigh an observer's posts accordingly.
- Where `rubric.json` defines `groups` (for example two labs, or two schools of thought), mix
  members across a table rather than seating a whole group together.

## Per-post rules

- **Four-line header**, pulled from `card.yaml`: table/round/name line, `stance_line`,
  `interest_line`, the simulation notice.
- **At least one experience argument per post**, with all four parts: what happened (cite the
  dossier section, with its evidence label); what it taught the persona; why it applies to the
  decision at hand; where the analogy might break. A post missing this is incomplete, not merely
  weak.
- **Rebut an experience argument by breaking the analogy** — name exactly where the two
  situations differ. Attacking the person's identity or interest instead is not a rebuttal, and
  is flagged by judges as `not_an_argument`.
- **Verdicts are per point, and binary.** Break an opposing post into its specific points; mark
  each `accept` or `reject` in the closing JSON's `responses`, with the post ID and point. There
  is no "partially" — a half-right post gets split into an accepted point and a rejected one. The
  gap matters: a lighter, critique-only mode used in an earlier protocol version produced
  essentially no outright rejections across a full pass of exchanges; moving to multi-round named
  tables with binary per-point verdicts produced dozens of rejections, dozens of score changes,
  and a double-digit count of "empty concessions" (accepted in text, score unchanged) that the
  lighter mode had no way to even notice.
- **Source challenges are a legitimate move.** Any persona may ask "is this evidence from you or
  your own organization — is there an independent source?" The challenged persona either
  produces an independent source (a self-check is allowed for this) or retracts that point
  (`retracted` in the closing JSON). This is productive: in one run, a handful of source
  challenges, combined with the in-debate fact-check, produced over a dozen retractions, against
  none the round before challenges were encouraged.
- **Self-checks are budgeted and logged.** Defaults: 3 at R1, 2 per debate round at B and C (none
  at A), 1 per overtime turn, 1 at R3 — a run may change these in `scope.md`. Each is logged in
  the post's closing JSON `searches`: query, URL, publish date, a verbatim sentence under 15
  words, which claim it is for, and whether it supports, refutes, or is unclear on that claim. A
  site that refuses access is not routed around; log "could not access." Usage rises sharply once
  self-checks are tied to a source challenge rather than left as a free-floating option — a
  challenged persona who must either check or retract uses the budget; one who merely may check
  often doesn't. Self-checks are suspended entirely during a fidelity test, since looking
  something up mid-test would let the persona see its own future.
- **Length limits**: post body ≤400 words, not counting the closing JSON; interjections ≤150
  words; overtime posts ≤300 words.

## Three rounds, interjections, overtime, cross-table replies

- **A (opening):** one post per table — a claim, an argument with at least one experience
  component, the persona's relevant R1 scores, and what fact would change their mind.
- **B (exchange):** reply to 1-3 people per table, including the strongest opposing post; close
  by asking one named persona a question. **Interjections** — a short post at a table the persona
  does not sit at — are allowed only when the persona has an argument or evidence that table
  hasn't seen yet; a scribe discards duplicates. **Interjections are capped per table, per side**
  (a reasonable default is 2): left uncapped, they cluster onto whichever side is already winning
  and manufacture exactly the herding principle 3 forbids. In one run, every interjection at one
  table landed on the same side, and the next persona to move cited "the others already moved"
  rather than an argument.
- **C (closing):** concessions (who persuaded, the argument restated in the persona's own words,
  which score moves), held positions (why), answers to questions and challenges, the fact that
  would resolve a remaining disagreement, an optional bridging question, and — for anyone still in
  the minority after three rounds — a mandatory paragraph on why. The closing JSON carries
  `intended_moves`, compared later against what R3 actually changes.
- **Overtime:** the orchestrator picks the sharpest unresolved pair per table (from the scribe
  notes) for 2-3 more turns. **Cross-table replies** also live here: if a persona's argument was
  cited or rebutted at a table they don't sit at, they get one reply, filed into that table's
  overtime folder.

## Simultaneous writing

Every persona writes a round at the same time as everyone else, and the next round starts only
once the orchestrator has every post from this one. Within a round, instructions tell each agent
not to list the round's directory and not to read anyone else's post from the same round — today
this is enforced by instruction; a scripted orchestrator can enforce it mechanically by gating the
release of the next round's instructions on every post being in.

## Scribe notes: two versions

A fresh agent with no persona material writes two files per table:

- **Persona-facing** (`board/summary/<table>.md`): consensus; what's still disagreed (and whether
  it's a factual, values, or timing disagreement); the one or two strongest arguments per side by
  post ID; the fact that would settle it; anything new (bridges, decisive experiments); and the
  minority opinion, verbatim. **It never says who persuaded whom or whose score moved.** This is
  deliberate: in an earlier run, a note that named whose position had shifted became a talking
  point other personas cited in later rounds ("even so-and-so moved") — the exact social-proof
  move principle 3 exists to block. Leaving it out at the source is more reliable than asking
  personas to ignore it.
- **Full** (`board/summary_full/<table>.md`): everything above, plus who persuaded whom (by post
  ID), empty concessions, score changes justified only by headcount or fame, strong arguments
  nobody answered, the interjection tally (received / carried new material / deduped),
  source-challenge outcomes, and the experience arguments that appeared at the table — for
  fact-check ③ to sample.

## R3: private re-score

Each persona reads every table's persona-facing notes (not just their own two tables) plus the
fact-check errata, then re-scores alone — they cannot see anyone else's R3. Every score change
must cite the specific post and point and restate that argument in the persona's own words;
"others changed" or "the room agrees" does not count as a reason, and the tooling tags changes
that give no better one. A point accepted in text whose score did not move goes in
`held_despite`, with why. One self-check is allowed. Scores stay the persona's honest judgment —
no self-discount for an option the persona has a stake in.

## Concurrency

Run at most 7 agents at once. Ramp up rather than launching everyone together — 3, then 6, then 7
— since a persona agent that has already read its own dossier and written R1 is carrying a large
context, and reviving several such agents at once is the likeliest way to trip the API's rate
limiting (HTTP 429). On a 429, back off about 3 minutes, then resume at the same ramp. Give each
persona its own scratch subdirectory for drafts and notes; a shared scratch space lets one
persona's draft get overwritten by another's, or lets a persona glimpse a fragment of a table it
doesn't sit at.

## Light mode: pairwise critique

For a smaller run — fewer personas, or a quick pass that doesn't justify full debate tables — use
pairwise critique instead of seating tables. Pair personas across differing perspectives, not
within the same `groups` entry. Two waves, each sent to every pair at once:

1. **Critiques**, all sent concurrently (`<A>_on_<B>.md`, `templates/rounds/critique.md`): the strongest
   point of the other's method that this persona also accepts; 2-3 disagreements, each with the
   other's judgment, why this method disagrees, the evidence, and what result would settle it;
   whether this changes the persona's own judgment; questions for the other side to answer
   directly.
2. **Replies**, sent only after every critique in wave 1 has arrived (`<A>_reply.md`,
   `templates/rounds/reply.md`): accept/reject per point with reasons, answers to the questions, and the
   final position, stated explicitly even if it didn't change.

Do not send a reply before all critiques are in. An earlier run resumed agents serially instead of
together, so one side's replies went out before the other side's critiques had even arrived — six
critiques went completely unanswered as a result. The fix is procedural, not a reminder to agents:
gate wave 2 on wave 1 being complete for everyone.

When aggregating, count a post-critique change of position in the score tables; an earlier review
caught two such changes that had been missed.
