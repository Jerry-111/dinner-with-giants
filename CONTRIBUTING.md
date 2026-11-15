# Contributing

Thanks for helping. This project is a protocol first and code second, so most useful contributions
are evidence about what works.

## What we welcome

- **Protocol changes backed by a run.** A rule that fixed a failure you observed, with the numbers
  (see "Proposing a protocol change" below).
- **Tooling:** checks, aggregation, lints, tests (`tools/sim.py`, `tests/`).
- **Templates and translations.** Chinese and English are maintained; other languages are welcome
  as `README.<lang>.md` and translated templates.
- **Personas** for the library (`personas/`): public figures with a substantial public record of
  their own views, historical figures, or clearly labeled archetypes, each with a complete
  `sources.csv` and following `RESPONSIBLE_USE.md`.
- **Docs, bug reports, questions.**

## What we do not accept

- Personas of private individuals, minors, or people known mainly for their private lives.
- Persona files that judge a person's character, honesty or motives instead of citing dated
  predictions and outcomes (see `RESPONSIBLE_USE.md`).
- Anything containing personal data: real users' context files, real runs about real people's
  lives, private names, e-mail addresses, local paths.
- Long verbatim excerpts from copyrighted sources.

## Proposing a protocol change

Open an issue with the **Protocol change** template and include:

1. The rule, in one or two lines.
2. The failure it fixes, from a run: what happened, how often, how you measured it.
3. How we will know it worked: the metric and the expected direction, written before the next run
   (for example "share of score changes with a social reason goes down").
4. The cost: extra agents, minutes, tokens.

`docs/design-notes.md` shows the format: rule → what happened → what changed.

## Development

Requirements: Python 3.9 or newer (CI runs 3.10–3.13). The tooling uses the standard library only.

```bash
python3 -m unittest discover -s tests -v
python3 tools/sim.py lint personas examples
python3 tools/sim.py quotes personas examples
python3 tools/sim.py privacy-scan .
```

Run all four before opening a pull request; CI runs them too. For a new or updated persona, also
run `python3 tools/sim.py quotes personas/<ID>_<slug> --fetch`: it fetches each cited page and
looks for every quote verbatim; check the ones it reports by hand.

Writing style for docs and templates: plain, dense English; short sentences; terms from
`docs/glossary.md`; file names and fields from `docs/data-formats.md`. Persona outputs follow the
labels and quote rules in `AGENTS.md`.

## Pull requests

- One topic per pull request; describe what changed and why.
- Update `CHANGELOG.md` under "Unreleased".
- If you change a data format, update `docs/data-formats.md`, the schema in `schemas/`, the tests
  and the templates in the same pull request.
- By contributing you agree that your contribution is licensed under the repository's license.
