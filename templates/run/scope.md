# <Run name>: scope

Run `<YYYY-MM-DD>_<slug>` | started <date, time, timezone> | materials through <date>

## What this run answers

(At most two or three headline questions.)

## Question list

- <Area 1>: <Q1>, <Q2>, …
- <Area 2>: …
- Cross-cutting: …

A persona whose material doesn't reach a question answers "no judgment" — that is a
legitimate answer; don't force one.

## Personas

| ID | Persona |
|---|---|
| | |

## The user's context (only this)

(Copy from `workspace/context/user_profile.md` only — nothing added, nothing guessed. List
unknowns explicitly and require conditional branches on them.)

**Unknown:**

## The user's latest expectations (binding on this run)

(Copy the most recent relevant entries from `workspace/context/preferences.md` and
`workspace/context/calibration_log.md`.)

- Output language: <the language this run is written in>.
- Ratio of domain/industry analysis to personal-path advice: <default: about two-thirds
  domain, one-third personal path — override here if `preferences.md` says otherwise>.

## Claims to test

(Claims the user heard from someone else and wants checked. Attribute generically — "a
friend," "a mentor" — never by name.)

## Rubric

`rubric.json` in this folder is pre-registered before Round 1 and frozen once personas submit.
It defines options, dimensions, levers, pairwise pairs, conditional-question lists, and
aggregation rules. Field reference: `docs/data-formats.md`; filled-in example:
`templates/run/rubric.json`.

## Deliverables

(Filename, length, and sections for each file type — see `templates/`.)

## Evidence rules

- Labels: `[quoted]`, `[synthesized]`, `[inferred]` (or the run-language equivalents — see
  `docs/glossary.md`). Keep the person's own view, the agent's extrapolation, and outside
  evidence distinct.
- Check `evidence/brief.md` before searching; cite its `F` numbers; log anything new in your
  own sources table.
- Quotes: only text actually read; under 15 English words (or the equivalent in the run's
  language); at most one quote per source.
- web-search budget: <n> searches per person for Round 1 (later rounds: see
  `protocol/03_debate_tables.md`). Prefer fetching a primary source over searching for one.
- A site that refuses access is logged as "could not access" — never bypassed with a cache,
  proxy, or scrape workaround.
- Write the sources table with a CSV library, not a hand-formatted string.

## Independence

- Round 1: read only your own persona folder, this file, `evidence/brief.md`, and
  `workspace/context/`. Not other personas' files, not previous runs' reports.
- Round 2 onward: see `protocol/03_debate_tables.md`.

## Paths

- Input: <where source material lives>
- Evidence brief: `evidence/brief.md`
- Output: `workspace/runs/<run>/`

## Writing

Write in <the run's language>. Plain, dense, no repetition. Keep technical terms in their
original language; tables are fine; no marketing tone.
