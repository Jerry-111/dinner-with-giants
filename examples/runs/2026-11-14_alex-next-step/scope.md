# Alex's next step: scope

Run `2026-11-14_alex-next-step` | started 2026-11-14 | materials through 2026-11-14

> **Bundled example.** Alex is fictional. The six personas are historical figures rebuilt from their
> own public-domain writings. Every persona output is a simulation, not the person's words.

## What this run answers

1. Which of Alex's four options holds up best after the debate, and on what does that depend?
2. Q1: Does a PhD still pay off when much frontier ML work happens in industry labs?
3. Q2: Under which conditions is the independent year (O4) the right call?

## Options (from `rubric.json`)

| ID | Option |
|---|---|
| O1 | Research engineer on the science team of a large AI lab |
| O2 | Founding ML engineer at a seven-person biotech startup |
| O3 | PhD with a newly hired assistant professor in protein ML |
| O4 | One independent year growing an open-source protein-ML toolkit |

Dimensions: `learning`, `upside`, `optionality`, `fit` (definitions in `rubric.json`). Scores are
integers 0–10; `null` means no judgment. `overall` is the persona's own weighting.

Levers (split 100 points): L1 mentor quality, L2 scope of ownership, L3 access to compute and data,
L4 public track record, L5 financial runway.

Pairwise picks (every persona picks in each pair): O1–O2, O1–O3, O2–O3, O3–O4, O2–O4.

Conditions for Q2 (tick the ones under which you would say yes to O4): C1 at least 12 months of
savings; C2 an active user community already exists; C3 a senior mentor reviews progress
monthly; C4 an offer can be deferred or re-opened; C5 a co-maintainer joins.

## Question list

- **Learning:** who learns what, from whom, how fast, on each path.
- **Value and risk:** where the upside comes from and who captures it; what failure looks like.
- **Reversibility:** which choices can be undone within two years and which cannot.
- **Timing:** what is already too late to join and what is early.
- **Credit and reputation:** how papers, code and named results build (or fail to build) standing.

A persona whose material does not reach a question answers "no judgment". That is a legitimate
answer; do not force one. Every persona lived in a different era: an experience argument must say
where the analogy may break for a 2026 decision.

## Personas

| ID | Persona | Folder |
|---|---|---|
| H1 | Benjamin Franklin | `personas/H1_franklin/` |
| H2 | Charles Darwin | `personas/H2_darwin/` |
| H3 | Michael Faraday | `personas/H3_faraday/` |
| H4 | Marie Curie | `personas/H4_curie/` |
| H5 | Ada Lovelace | `personas/H5_lovelace/` |
| H6 | Su Shi | `personas/H6_su_shi/` |
| Z1 | Baseline analyst (no persona) | — |

## The user's context (only this)

Copied from `examples/context/user_profile.md`; nothing added, nothing guessed.

- Fictional. 25, finishing a master's in computational biology at a public university; graduates
  May 2027.
- Two years in a university lab building ML models for protein stability prediction; one workshop
  paper as second author.
- Maintains an open-source data-cleaning tool for protein datasets (about 800 GitHub stars, two
  occasional contributors).
- Prefers building tools other people use over writing papers; likes reading experimental results,
  not running wet-lab experiments.
- Decided: stays in protein or biological ML for at least five years; no management in the next
  five years.
- Goals: be trusted for judgment on which protein-ML problems matter; keep the option of founding
  something later; avoid a path that cannot be reversed within two years.

**Unknown** (write conditional branches, do not guess): risk tolerance beyond "moderate"; how Alex
handles long stretches without visible progress; visa or location constraints.

## The user's latest expectations (binding on this run)

From `examples/context/preferences.md`:

- Arguments, not reassurance; the strongest case against each option.
- About two-thirds on how each path works (who learns what, where value and risk come from, what is
  already too late), one-third on Alex's own choice.
- Conditional branches instead of one recommendation; for every path, the early signal that it is
  the wrong one.
- Keep disagreements visible. Plain, dense English.

## Claims to test

- A friend: "If you don't start a PhD now, you never will."
- A former manager: "A startup teaches you more in a year than a big lab in three."

## Rubric

`rubric.json` in this folder was frozen before R1. Field reference: `docs/data-formats.md`.

## Deliverables

- R1: `r1/<ID>.json` and `r1/<ID>.md` (at most 8 KB), per `instructions/r1.md`.
- Debate: `board/A|B|C/<table>/<ID>.md`, per `instructions/debate.md`; each post at most 350
  words plus its JSON.
- R3: `r3/<ID>.json` and `r3/<ID>.md` (at most 3 KB), per `instructions/r3_scribe.md`.

## Evidence rules

- Labels `[quoted]`, `[synthesized]`, `[inferred]`. Keep the persona's documented views, your
  extrapolation and outside evidence apart.
- Check `evidence/brief.md` first and cite its `F` numbers; facts about 2026 come from the brief or
  from a logged self-check, never from the persona's own era.
- Quotes: only text actually read; English quotes under 15 words; at most one quote per source.
- Self-check budget: R1 2 searches; each debate round 1; R3 1. Only for specific claims; log them
  in the JSON `web_searches` / `searches`.
- A site that refuses access is logged as "inaccessible"; never bypassed.

## Independence

- R1: read only your own persona folder, this file, `rubric.json` and `evidence/brief.md`
  (and `evidence/errata.md` if present). Not other personas' files.
- Later rounds: only what each round's instructions list.

## Seating

Six personas, three tables of four, two seats each (`rubric.json` `seating`). Overtime is skipped in
this example to keep it small; `RUN_METADATA.md` records that.

## Paths

- Run folder: `examples/runs/2026-11-14_alex-next-step/`
- Evidence brief: `evidence/brief.md`
- Round instructions: `instructions/`

## Writing

English. Plain, dense, no repetition. Technical terms as they are; tables are fine; no marketing
tone. No "he/she" for personas or for Alex: use names or IDs.
