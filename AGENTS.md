# AGENTS.md

For any coding agent working in this repository (Claude Code, Codex, or similar).

## What this repo is

A protocol for getting a second opinion on a decision from simulations of people whose views are
already public — run through independent scoring, structured debate, fact-checking, judging, and
a written report, orchestrated by a coding agent. It works for any decision and any set of
personas; nothing in the protocol itself is tied to one person's choice.

## Read first

1. `workspace/context/user_profile.md` — the user's own background and decisions already made, if
   it exists.
2. `workspace/context/preferences.md` — what output they want, if it exists.
3. `workspace/context/calibration_log.md` — their feedback over time, newest at the bottom, if it
   exists.

If `workspace/context/` is empty or missing, either ask the user for this directly, or use the
bundled example (`examples/`) to see the shape of a complete run: a fictional decision between a
few concrete options, simulated by a persona pack built from people whose own writing is public
domain.

Then, by task:

| Task | Read |
|---|---|
| Quick "what would persona X say about this" | `protocol/08_consult.md` |
| A full run | `protocol/00_overview.md`, then follow its steps |
| Build or update a persona | `protocol/02_persona_research.md` |
| Run debate tables | `protocol/03_debate_tables.md` and `templates/rounds/` |
| Fidelity test (does the persona sound like the person) | `protocol/11_fidelity_test.md` |
| Reader pack for the user | `protocol/07_reader_pack.md` |
| Tooling (`tools/sim.py`) | `tools/README.md` |

## Hard rules

1. **Simulation is not the person.** Every persona-authored file and post opens with a notice:
   "Simulation based on public material; not the person's own words." (Chinese runs:
   "基于公开材料的模拟，不是本人言论。") Never present a persona's output as the real person's
   statement, and never write an agent's inference as if it were the person's own stated view.
   In particular, a persona never "confesses" in the first person ("I admit my stake biases
   me"): interests are third-person dated facts, and any judgment about motives is third-person
   and `[inferred]`.
2. **Three labels, kept separate.** `[quoted]` (a sourced quote or near-verbatim statement),
   `[synthesized]` (summarized from several public sources), `[inferred]` (the agent's
   extrapolation from the person's framework). Keep the persona's own view, the agent's inference,
   and plain technical evidence visibly apart — never blend them into one unlabeled claim.
   (Chinese runs may use 【原话】【归纳】【推断】; the tooling accepts either.)
3. **Quote rules.** Quote only text actually read. English quotes under 15 words; at most one
   quote per source. If you could only read part of a source, say what part — a description of a
   talk is not the same as having watched it.
4. **Don't invent conflict.** If the person hasn't addressed something publicly, write "no
   judgment" or label it `[inferred]` — don't manufacture a position for them.
5. **Don't bypass access restrictions.** If a source refuses access, don't route around it with
   fetch tricks, proxies, third-party readers, or archives. Record it as inaccessible and move on.
6. **Round-one independence.** In the independent-scoring round, each persona agent reads only
   its own persona folder, the run's shared brief (`scope.md`, `rubric.json`,
   `evidence/brief.md`), and `workspace/context/` — not other personas' folders or submissions.
7. **Disclose interests and non-independence.** If the model doing the analysis is made by the
   same organization as a simulated person, or that person works there, say so in the run's
   limitations, every time — not just once. Several instances of one model are not independent
   evidence of agreement; report headcount as description, never as support. Personas who share an
   employer, lab, or long collaboration cannot be the only representation of one side of a debate
   table (`rubric.json`'s `not_independent` list; checked by `tools/sim.py tables`).
8. **Privacy.** `workspace/context/` holds only what the user has given you, and it is
   git-ignored — it does not leave the user's machine unless they move it. Never write immigration
   or identity documents, financial details, or health information anywhere in the repository,
   including in `workspace/`.
9. **The user decides.** Where the output touches the user's own choice, give conditional
   branches and reversal signals — don't decide for them. Treat decisions the user has already
   made (`workspace/context/user_profile.md`) as a given; don't re-litigate them every run.
10. **Don't discount on the reader's behalf.** A persona's score is that persona's real judgment.
    Interests go in the `conflict` field and in the report — shown, never subtracted. An
    experience argument ("I lived through this, here's the lesson, here's why it applies") is a
    legitimate argument: judge it on whether the analogy holds here. Rebut it by breaking the
    analogy, never by citing the arguer's identity or interest.

**Living public figures.** Simulating a real, living person carries its own risks —
misrepresentation, the appearance of a real endorsement. Follow `RESPONSIBLE_USE.md` for who you
can simulate and how. In short: evaluate arguments and dated predictions, never the person's
honesty, motives or character; every role, company, departure or deal has a source and an "as of"
date; and where a simulated person is linked to the vendor of the model running the simulation
(Claude is trained by Anthropic), say so. A persona never comments on its own recent news, legal
or governance matters; its interest line shows only dated facts that bear on the question.

## Output conventions

- Write in the run's language, set once in `scope.md`. Dense, plain sentences; keep domain terms
  rather than dumbing them down.
- The ratio of domain analysis to personal-path content is set per run in `scope.md`.
- Every run lives in its own folder, `workspace/runs/<YYYY-MM-DD>_<slug>/` (or
  `examples/runs/<slug>/` for the bundled example), and must have a `RUN_METADATA.md`: timeline,
  inputs, independence notes, and what this run skipped.
- Persona material lives in `workspace/personas/<ID>_<slug>/`. When you revise a persona, write
  what changed from the previous version in the file itself (the dossier, the card, and the views
  file each have a place for it).
- Write `sources.csv` with Python's `csv` module, using the fixed columns in
  `docs/data-formats.md` — don't hand-format it.
- Save intermediate results as files, not just in conversation, so the next agent (or the next
  round of this one) can pick them up without replaying your context.

## Delivery

- The full record — report, evidence, debate, persona material — stays in Git / `workspace/`, as
  context for future runs.
- The user reads a one-page reader pack (`protocol/07_reader_pack.md`), not the full record.
- Ask the user before publishing anywhere outside the repository, every time — even to a
  destination used before.
