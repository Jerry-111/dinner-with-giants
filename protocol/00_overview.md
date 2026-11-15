# Protocol overview

A run takes one decision, a roster of personas, and produces a report built from independent
scoring, structured debate, repeated fact-checking, and independent review. The
**orchestrator** (the coding agent session running this protocol — Claude Code, Codex, or
similar) drives every step: it writes the shared files, launches sub-agents in parallel, and
moves files between rounds. It never writes persona content itself.

## Steps

| Step | What happens | Who | Output | Details |
|---|---|---|---|---|
| 0 | Scope: headline questions, persona roster, pre-registered rubric, evidence rules, shared evidence brief | orchestrator; a brief sub-agent | `scope.md`, `rubric.json`, `evidence/brief.md` | `01_scope.md` |
| 1 | Persona research: dossier, views, optional conversation, machine-readable card | one **persona agent** per persona, in parallel | `personas/<ID>_<slug>/` | `02_persona_research.md` |
| 1b | Fidelity test (optional, real people only): predict a real person's post-cutoff public statements from pre-cutoff material alone | a few persona agents; one blind-grading fresh agent | a side run under `workspace/runs/` | `11_fidelity_test.md` |
| 2 | Debate tables: independent scoring → crux map and seating → three named rounds of debate → overtime → private re-scoring | persona agents continue from step 1; a **crux agent** and **scribe** (fresh agents) handle mapping and notes | `r1/`, `board/`, `r3/` | `03_debate_tables.md` |
| 2b | Judging: score every post against a fixed rubric, seeing the posters' names | one or more **judge** fresh agents | `judge/` | `10_judge.md` |
| 3 | Fact-checks: the evidence brief, mid-debate claims, post-re-score claims, plus an experience check against each dossier | a fresh **fact-checker** agent per pass | `evidence/errata*.md`, `audit.md` | `04_fact_check.md` |
| 4 | Digest (optional): compile each topic area across all personas, after debate | one fresh agent per area | one digest file per area | `05_digest.md` |
| 5 | Synthesis: a script aggregates the numbers, a **lead writer** drafts the report, an independent **reviewer** checks it against the record | script; lead-writer agent; reviewer agent | `summary.md`, `report.md`, `review.md`, `RUN_METADATA.md` | `06_synthesis.md` |
| 6 | Reader pack: a short version for the user to actually read | orchestrator — confirm scope with the user before publishing anywhere external | `reader/` | `07_reader_pack.md` |

Full file list: `01_scope.md`, `02_persona_research.md`, `03_debate_tables.md`,
`04_fact_check.md`, `05_digest.md`, `06_synthesis.md`, `07_reader_pack.md`, `08_consult.md`,
`09_review.md`, `10_judge.md`, `11_fidelity_test.md`. Design rationale and the numbers behind
each rule: `docs/design-notes.md`.

Two light modes skip the full run: **consult** (`08_consult.md`: what would these personas ask
and say about one question) and **review** (`09_review.md`: a panel critiques a draft, then
cross-checks each other's critiques).

## Run sizes

| Size | Personas | Debate | Time | Use |
|---|---|---|---|---|
| Consult | 1–4 | none | minutes | "How would X see this specific choice?" — `08_consult.md` |
| Review | 3–5 | two waves: critiques, then a cross-check | 10–30 minutes | "Tear this draft apart before its real audience does" — `09_review.md` |
| Panel | 3–6 | one or two tables (three small ones in the bundled example) | about an hour | A focused decision with a few real options |
| Full run | 12–20 | several tables | several hours | A decision with multiple live cruxes, run once and revisited |

A full run with around 20 personas has taken about 5.5 hours end to end in practice: persona
cards about 40 minutes; independent scoring about 70 minutes; crux mapping 20 minutes; each of
the three debate rounds 25–35 minutes; scribe notes, judging, and fact-checking in parallel
about 30 minutes; private re-scoring about 40 minutes; report, review, and revisions about 50
minutes. These are anonymized reference numbers from one earlier run, not a guarantee — a run
with a slower model, a larger roster, or more rate-limiting will take longer.

## When not to run the full protocol

- **A specific, narrow question about one or two people's view.** Use consult mode
  (`08_consult.md`); it takes minutes, not hours.
- **Persona material is more than about six months stale** and the run needs a time-sensitive
  judgment from it. Refresh just those personas (step 1), not the whole roster.
- **The new question overlaps a previous run.** Read that run's `report.md` and `summary.md`
  first and fill only the gap — don't re-debate settled ground.
- **The decision has no real disagreement to surface.** If one option dominates on every
  dimension anyone cares about, a debate table won't find a crux worth seating; a panel or even
  a consult will say so faster.

## After the run

Reversal signals (`docs/glossary.md`) are for agents to check against periodically — the user
does not need to track them. New feedback from the user goes in
`workspace/context/calibration_log.md` and shapes the next run's `scope.md`.
