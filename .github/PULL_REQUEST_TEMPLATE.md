## What and why

<!-- One topic per pull request. -->

## Checklist

- [ ] `python3 -m unittest discover -s tests -v` passes
- [ ] `python3 tools/sim.py lint personas examples` and `python3 tools/sim.py quotes personas examples` pass
- [ ] `python3 tools/sim.py privacy-scan .` passes (and I ran it with my own `--denylist`)
- [ ] Data-format changes are reflected in `docs/data-formats.md`, `schemas/`, tests and templates
- [ ] `CHANGELOG.md` updated under "Unreleased"
- [ ] Personas of living people are public figures and follow `RESPONSIBLE_USE.md` (sourced, dated facts; no judgments of character)
- [ ] No private individuals, no personal data, no long verbatim excerpts
