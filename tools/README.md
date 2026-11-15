# tools/sim.py

A single-file, standard-library-only helper CLI for the persona-debate protocol. Every
subcommand is driven by the run's own `rubric.json` (see `docs/data-formats.md`); nothing here
is hard-coded to a particular run, option set, or persona roster.

Requires Python 3.9 or later (CI covers 3.10–3.13; 3.9 is end-of-life and no longer on GitHub's Ubuntu runners, but the tests pass on it locally). No install step and no network access are needed. `pyyaml` is an
optional dependency (see `requirements-dev.txt`) that improves `card.yaml` parsing in `roster`;
without it, a regex-based fallback is used automatically.

Run `python3 tools/sim.py --help` or `python3 tools/sim.py <command> --help` for the full,
authoritative option list. This page is a quick reference.

## Picking a run

Most commands act on one run directory. Pass it with `--run PATH`, or set it once per shell with
the `RUN` environment variable:

```
export RUN=workspace/runs/<date>_<slug>
python3 tools/sim.py check r1
```

There is no built-in default run; one of the two must be given.

## Commands

| Command | What it does |
|---|---|
| `new-run --slug S [--date YYYY-MM-DD] [--root workspace/runs]` | Creates `<root>/<date>_<slug>/`, copying any files found in `templates/run/` and creating the empty subfolders from `docs/data-formats.md`'s run layout. Works even when `templates/run/` is empty. Refuses to touch a target folder that already exists and is not empty. |
| `new-persona --id ID --slug S [--root workspace/personas]` | Creates `<root>/<ID>_<slug>/` by copying `templates/persona/*`, replacing the literal placeholder `<ID>` with the given id in every text file. |
| `roster --personas DIR [DIR...] [--write RUBRIC]` | Reads `id:`, `name:` and `aliases:` out of each `DIR/card.yaml` and prints the resulting `rubric.json` `personas` block as JSON. With `--write RUBRIC`, merges it into that rubric file in place instead of printing. |
| `check r1\|r3 [--baselines] [--run PATH]` | Validates every `r1/*.json` or `r3/*.json` submission against the rubric (see **Rules checked** below). `--baselines` additionally validates `baselines/*_r1.json` or `baselines/*_r3.json`. |
| `tables [--run PATH]` | Validates `tables.json` seating against `rubric.json`'s `seating` block and `cruxes.json`'s sides. |
| `index [--run PATH]` | Writes `board/A/INDEX.md`: one line per opening post, with its claim and persona display name. |
| `anon [--seed N] [--run PATH]` | Writes anonymized copies of every `board/A\|B\|C` post to `judge/anon/...`, replacing persona names, aliases and ids with a seeded, shuffled `P01`, `P02`, ... code. Writes the real mapping to `judge/anon_key.json` (never hand this to a blind judge). Default seed is `0`. |
| `aggregate [--run PATH]` | Writes `summary.json` and `summary.md` (see **Aggregate output** below). |
| `quotes PATH... [--fetch] [--timeout S]` | Checks every `[quoted]` passage: under 15 words, cites an evidence id that exists in the folder's `sources.csv`, at most one quote per source. With `--fetch`, downloads each cited page and looks for the quote verbatim; anything not found is listed to check by hand. Labels written as code (`` `[quoted]` ``) and near-verbatim paraphrases without quotation marks are skipped. |
| `scan [--boards] [--personas DIR [DIR...]] [--run PATH]` | Scans persona cards for `rubric.json`'s `forbidden_words` (default: `discount`, `打折`, `折扣`, `减权`). Add `--boards` to also scan the run's posts. See **Persona-folder discovery** below for the default (no `--personas`) behavior. |
| `lint PATH... [--strict]` | Checks persona-authored Markdown, filenames, JSON and sources CSVs under the given paths (see **Rules checked**). `--strict` turns warnings into errors. Exit 1 on any error. |
| `compare RUN_A RUN_B OUT.json [--exclude IDS]` | Writes pre-registered cross-run comparison metrics (diversity, persona-baseline gap, score churn, verdict mix, search counts, interjection asymmetry, pairwise win counts) to `OUT.json` and prints the headline numbers. `--exclude` takes a comma-separated list of persona ids to drop from both runs (for a sensitivity check). |
| `blind RUN_A RUN_B OUTDIR [--seed N]` | Samples material for blind reviews 1 and 2: every R3 `changes` entry (shuffled, reasons only) to `OUTDIR/changes.json`, and up to 10 non-interjection posts per round (A/B/C) per run (stripped of headers and JSON) to `OUTDIR/posts/`. The answer key is written to `blind_key.json` next to `OUTDIR`, not inside it. |
| `blind-report REPORT_A REPORT_B OUTDIR [--sections "0.,2.,3."] [--seed N]` | For blind review 3: relabels two finished reports A/B, and again with the labels swapped, redacting run-identifying paths (`runs/...`) and version tags (`v3`, `v5`, ...). `--sections` keeps only the `## ` sections whose heading starts with one of the given comma-separated prefixes; omit it to keep every section. The mapping is merged into the same `blind_key.json` used by `blind`. |
| `privacy-scan PATH... [--denylist FILE]` | Flags emails, home-directory paths, common secret formats, Notion urls/ids, and denylist terms (see **privacy-scan** below). Exit 1 on any hit. |

Every subcommand that writes JSON uses stable key order and a trailing newline; every subcommand
prints a one-line summary to stdout.

## Exit codes

| Code | Meaning |
|---|---|
| `0` | Success, and (for `check`, `tables`, `lint`, `scan`, `privacy-scan`) no problems found. |
| `1` | The command ran, but found problems: a failed `check`/`tables`/`lint` rule, a `scan` hit, or a `privacy-scan` hit. |
| `2` | The command could not run at all: no `--run`/`RUN` given, or a required file (`rubric.json`, `tables.json`, ...) is missing or not valid JSON. |
| other | An uncaught `argparse` usage error (bad flags, missing required argument, `--help`). |

## Rules checked

`check r1|r3` (also applied to baseline files under `--baselines`):

- every rubric option is present (a `short_options` entry may carry only `overall` and `one_line`);
- every score is an integer within `scale` (default 0–10), or `null`;
- if the rubric has `levers`, the submission's lever points sum to exactly 100;
- `paths_for_user` length, and (R1 only) `cruxes` length, follow `r1_requirements`;
- every rubric `pairwise` pair has a pick;
- R3 submissions have a `changes` key (an empty list is fine).

A rule is skipped whenever its rubric key is absent.

`tables`:

- every table's member count is within `seating.table_size`;
- every persona sits at exactly `seating.seats_per_persona` tables;
- every table has members on at least two sides of its crux;
- a `not_independent` group never provides the *sole* representation of one side at a table
  (that is, two or more of a table's representatives of one side are never all drawn from the
  same `not_independent` group; a single representative is never flagged on this rule alone).

`lint`:

1. persona-authored Markdown — `r1/*.md`, `r3/*.md`, `board/A|B|C|overtime/*/*.md`,
   `board/summary/*.md`, `board/summary_full/*.md`, `judge/*.md` (not the JSON scorecards), and
   any `dossier.md`, `views.md`, `conversation.md`, `industry.md` — must carry the simulation
   notice ("Simulation based on public material" or "基于公开材料") within its first 8 lines.
   Files under `baselines/` are exempt.
2. **Warning:** an English double-quoted passage of 15 or more words (checked across the whole
   file, including JSON tails, since a long verbatim quote is worth flagging wherever it sits).
3. Non-ASCII filenames are an **error**, except a legacy `..._插话...` interjection filename,
   which is a warning.
4. Every `.json` file must parse.
5. Every `sources*.csv` file's header line must match `docs/data-formats.md` exactly.

## Aggregate output

`summary.json` keys: `n_r1`, `n_r3`, `overall_r1`, `overall_r3` (per option: `n`, `median`, `q1`,
`q3`, `iqr`, `min`, `max`), `rank_r1`, `rank_r3`, `groups_r3`, `weighted` (per weight set: `stats`
and `rank`), `sensitivity_flips`, `moves`, `n_changed_scores`, `levers_r1`, `levers_r3`,
`questions_r1`, `questions_r3`, `conditions` (`{"r1": ..., "r3": ...}`), `pairwise`
(`{"r1": ..., "r3": ...}`, each pair's counts and win rate), `baselines`, `persona_minus_baseline`
(per baseline: the gap to the persona median per option, and the mean absolute gap), `verdicts`,
`n_searches_in_debate`, `persuaded_by`, `empty_concessions`, `intent_vs_actual`,
`source_challenges`, `retracted`, `judge` (scorecard field distributions and flag counts, from
`judge/scores.json` when present).

Ranking is always: higher median first, ties broken by the smaller IQR. A rank move of 3 or more
places across weight sets is flagged in `sensitivity_flips`. The threshold is
`aggregation.sensitivity_threshold` in `rubric.json` (an integer; default 3 when absent).

Verdicts (`accept`/`reject`/`partial`), search results (`supports`/`refutes`/`unclear`) and named-
question positions (`for`/`against`/`conditional`) are accepted in English or Chinese and
normalized to English in the output.

## privacy-scan

Each hit prints as `path:line: rule`, one per line; the matched text is never printed in full. For
pattern-based rules (`email`, `home_path`, `secret:<kind>`, `notion_url`, `notion_id`) the rule
name is followed by a partially masked excerpt in parentheses. For a denylist hit, the rule is
`denylist:L<n>`, where `<n>` is the matching line number in the denylist file — the denylist term
itself is never echoed anywhere, since it may be exactly the private information being protected.

Denylist file format: one entry per line; blank lines and lines starting with `#` are ignored; a
line starting with `re:` is a Python regular expression (case-insensitive); whitespace followed by `#`
starts an inline comment, which is ignored; anything else is a
plain term, matched case-insensitively with a word boundary when the term is ASCII word
characters (so it will not match inside a longer word), and as a plain substring otherwise (for
CJK terms, where a word-boundary regex would not do anything useful).

`.git/` directories, binary files, and the denylist file itself are always skipped.

## Persona-folder discovery

`scan` (without `--boards`) and `roster` work on explicit persona folders. When `scan` is run
without `--personas`, it falls back to the run's own scope: it reads the persona ids out of
`rubric.json`'s `personas` block (when `--run`/`RUN` is set) and looks for `<ID>_*` folders under
`workspace/personas/` and `personas/`, in that order, relative to the
current directory. This is a convenience default, not a protocol rule — pass `--personas`
explicitly whenever the persona folders live somewhere else.

## No network access

None of these commands talk to the network, a database, or any external service, with one
exception: `quotes --fetch` downloads the pages cited in `sources.csv` to look for each quote.
Everything else only reads and writes files under the paths given on the command line.
