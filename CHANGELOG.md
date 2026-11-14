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
- JSON Schemas for every hand-off file.
- Example persona pack (public-domain historical figures) and an example run on a fictional
  decision.
- Responsible-use policy, contribution guide, issue and pull-request templates, CI.

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
