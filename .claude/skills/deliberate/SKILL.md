---
name: deliberate
description: Run the persona debate-table protocol on a decision — a panel (3–6 personas, about an hour) or a full run (12–20 personas, several hours). Use when the user wants a structured deliberation, not a quick opinion.
---

# Deliberate

Follow `protocol/00_overview.md` step by step; rules are in `AGENTS.md`, Claude Code specifics in
`CLAUDE.md`.

Before starting, confirm with the user: the decision and its options, the personas, the run size
(panel or full), and the time and token budget. Then:

1. `python3 tools/sim.py new-run --slug <slug>`; write `scope.md` and freeze `rubric.json`
   (`protocol/01_scope.md`).
2. Evidence brief and fact-check ① (`protocol/04_fact_check.md`).
3. Personas: existing folders, or build them first with the `new-persona` skill.
4. Rounds R0 → R1 → X → A → B → ② → C → S → (OT) → R3 → ③ → J (`protocol/03_debate_tables.md`,
   round instructions in `templates/rounds/`). Real sub-agents only; continue each persona agent
   with SendMessage across rounds; release a round only when every post of the previous one is in;
   at most 7 agents at once.
5. `python3 tools/sim.py check r1`, `tables`, `index`, `check r3`, `aggregate`.
6. Report, independent review, reader pack (`protocol/06_synthesis.md`, `protocol/07_reader_pack.md`).
7. Fill in `RUN_METADATA.md`: timeline, what was skipped, independence and limitations.

Ask the user before publishing anything outside the repository.
