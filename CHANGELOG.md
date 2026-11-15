# Changelog

All notable changes to this project are documented here. The protocol and the tooling share one
version number until they need separate ones.

## 0.1.0 (unreleased)

### Added
- Protocol v1 in English: scope, persona research, debate tables (independent R1, crux-based
  tables, three rounds with interjections and overtime, two-version scribe notes, private R3
  re-score), three fact-check passes, judges, synthesis, reader pack, consult mode, fidelity test.
- Templates for user context, personas, runs and every round.
- `tools/sim.py`: rubric-driven validation, seating checks, aggregation, lints, privacy scan,
  run-to-run comparison and blind-test material.
- `tools/sim.py quotes`: checks every `[quoted]` passage for length, a valid evidence id and one
  quote per source; `--fetch` looks for each quote verbatim on its source page.
- JSON Schemas for every hand-off file.
- Persona library (`personas/`): 20 living public figures in AI research, technology and
  investing, built from their public record, and 6 historical figures built from their own
  public-domain writings.
- Review mode (`protocol/09_review.md`, `/review`): a panel critiques a draft independently,
  cross-checks the other critiques, and a fresh editor compiles a ranked fix list.
- `docs/use-cases.md`: recipes beyond decisions (pre-mortem, pitch rehearsal, mapping a field,
  red-teaming a belief, brainstorming from different paths).
- Two example runs: 20 personas on 16 AI research directions (adapted from a real run,
  translated, with the original user's personal details removed), and six historical figures
  on a fictional student's decision.
- Responsible-use policy for living public figures (no judgments of character; sourced, dated
  facts; vendor links disclosed; takedown on request), contribution guide, issue and
  pull-request templates, CI.

### Changed (from the bundled example run)
- Debate template: source challenges raised in prose must also be logged in the closing JSON;
  the example run's script count was 0 while the judge saw 3.
- `CLAUDE.md`: release the next round on agents' completion replies, not on files that look
  finished.
- `tools/sim.py lint`: long strings inside a post's fenced JSON are no longer reported as long
  quotes.
- `tools/sim.py aggregate`: the sensitivity threshold is read from
  `aggregation.sensitivity_threshold` (default 3).
- `tools/sim.py privacy-scan`: denylist entries may carry inline comments (`term   # note`);
  before this, such entries silently never matched.
- CI matrix is Python 3.10–3.13: GitHub's current Ubuntu runners no longer provide 3.9.
- The persona library moved from `examples/personas/` to `personas/`; the bundled run's paths
  were updated.
- `RESPONSIBLE_USE.md` rule 10: a persona of a living person does not discuss its own recent
  news, legal or governance matters, and interest lines show only facts that bear on the question.
- CI lints and quote-checks `personas/` as well as `examples/`.
