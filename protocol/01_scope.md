# Step 0: scope

Produces the files every sub-agent reads before doing anything else: `scope.md` (the task
brief) and `evidence/brief.md` (the shared evidence base), plus the pre-registered
`rubric.json`. Written by the orchestrator, optionally with a dedicated sub-agent for the
evidence file. Template: `templates/run/scope.md`.

## What `scope.md` must say

- **Headline questions.** At most two or three. Then a per-area question list — one earlier
  run used nine topic areas plus five cross-cutting questions. Split by area on purpose: one
  shared framework pointed at every persona flattens them into near-identical advice (see
  `docs/design-notes.md`).
- **Persona roster.** ID and name or description for each. Select on two things only: is there
  enough public material to reconstruct how this person reasons, and does this person cover a
  question nobody else on the roster covers. Fame is not a selection criterion. See
  `02_persona_research.md` for the four kinds of persona and what each can support.
- **The user's context.** Copied only from `workspace/context/user_profile.md`, and say so —
  "only this." List unknowns explicitly and require conditional branches on them; never a
  guess.
- **The user's latest expectations.** Copied from the most recent entries in
  `workspace/context/preferences.md` and `workspace/context/calibration_log.md`. Binding on
  every sub-agent in this run.
- **Output language and ratio.** The language every file in this run is written in (English
  and Chinese both work end to end — see `docs/glossary.md` for the evidence labels accepted in
  each). The ratio of domain/industry analysis to personal-path advice; default is about
  two-thirds domain, one-third personal path, unless `preferences.md` sets a different one.
- **Claims to test.** Claims the user heard from someone else and wants checked. Attribute them
  generically — "a friend," "a mentor," "a colleague" — never by name.
- **Deliverables.** Filename, length, and section list for each file type (see `templates/`).
- **Evidence rules.** The three labels; quote rules (actual text read, under 15 words in
  English or the equivalent in the run's language, one quote per source); the Round-1
  web-search budget per person (later rounds' budgets are set in `03_debate_tables.md`); what to
  do when a site refuses access (log "could not access," never bypass it).
- **Independence.** What Round 1 may and may not read. Later rounds are covered in
  `03_debate_tables.md`.
- **Paths.** Where inputs live, where outputs go.

## Pre-registering `rubric.json`

Before Round 1 starts, write `rubric.json`: options, dimensions, scale, optional levers,
aggregation rules (no headcount as evidence, no weighting by persona identity, no
extremizing), which personas are not independent of each other, and two or three weight sets
for sensitivity analysis. Full field reference: `docs/data-formats.md`; a filled-in example:
`templates/run/rubric.json`. **Frozen once personas submit Round 1** — changing the scoring
rule after seeing scores invites fitting the rubric to a preferred answer.

If the run uses pairwise comparisons, list 10–15 option pairs in the rubric; every persona
picks a side on every pair. If a question is conditional ("under which conditions would you
say yes to…"), pre-list the candidate conditions in `conditional_questions` so personas check
boxes against a fixed list instead of inventing their own.

## The evidence brief

`evidence/brief.md`: shared facts the whole roster would otherwise look up independently —
numbered `F1, F2, …`, each with a source, kept under 20 KB. Put in only definitions and facts
that would change a ranking (an unexpected acquisition, a release, a capacity number); leave
everything else to each persona's own sources and self-checks. Keeping it thin matters: a
thick shared brief is the fastest way to make many independently-written opinions converge on
the same framing before anyone has argued about anything.

## Notes

- "No judgment" is a legitimate answer for a persona whose material doesn't reach a question.
  Say so in `scope.md`, or agents will force an opinion to avoid looking unhelpful.
- Decide the shared web-search budget before the run starts, not mid-run, or whoever asks first
  gets the quota. Favor fetching a primary source over searching for one.
