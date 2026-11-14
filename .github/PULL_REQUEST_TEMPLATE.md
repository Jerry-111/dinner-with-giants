## What and why

<!-- One topic per pull request. -->

## Checklist

- [ ] `python3 -m unittest discover -s tests -v` passes
- [ ] `python3 tools/sim.py lint examples` passes
- [ ] `python3 tools/sim.py privacy-scan .` passes (and I ran it with my own `--denylist`)
- [ ] Data-format changes are reflected in `docs/data-formats.md`, `schemas/`, tests and templates
- [ ] `CHANGELOG.md` updated under "Unreleased"
- [ ] No living-person personas, no personal data, no long verbatim excerpts
