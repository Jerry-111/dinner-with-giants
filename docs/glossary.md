# Glossary

Canonical terms used across the protocol, templates, tooling and examples.

## Roles

| Term | Meaning |
|---|---|
| user | The person whose decision the run is about. Their context lives in `workspace/context/` and never in the public repo. |
| orchestrator | The coding agent session (Claude Code, Codex, …) that runs the protocol: writes the scope, launches sub-agents, moves files between rounds. |
| persona agent | A sub-agent that simulates one persona from that persona's folder only. |
| baseline analyst | A sub-agent with no persona that scores the same options. The persona layer is measured against it. |
| crux agent | A fresh sub-agent that has read no persona material; turns round-1 disagreements into cruxes and seats the tables. |
| scribe | A fresh sub-agent that writes the two versions of each table's notes. |
| judge | A fresh sub-agent that scores each post with a fixed scorecard. Sees names. |
| fact-checker | A fresh sub-agent that checks claims against primary sources (three passes). |
| lead writer | A fresh sub-agent that writes the report from the aggregated files. |
| reviewer | A fresh sub-agent that did not write the report and did not read the debate; finds problems, does not rewrite. |

## Persona material

| Term | Meaning |
|---|---|
| persona | A reconstruction of how a person (or an archetype) reasons. Always a simulation, never the person. |
| dossier | `dossier.md`, sections A–I: path dependence, wins and failures, core beliefs, evolution of views, interests and position, advice to young people, long-interview notes, mental-model card, experience → lesson. |
| views | `views.md`: overall judgment, per-domain judgment table, dated prediction record, where this persona is most likely wrong. |
| conversation | `conversation.md`: a simulated long conversation with the user, ending with a takeaway table. |
| card | `card.yaml`: machine-readable summary printed at the top of every prompt and every post. |
| stance line | One line on the card: lived experience only, no evaluation. Printed at the top of every post. |
| interest line | One line on the card: dated facts about the persona's interests. Shown, never used as a discount. |
| sources table | `sources.csv` (and `sources_v<N>.csv` for later versions), fixed columns, written with Python's `csv` module. |
| prediction record | 4–8 dated predictions with outcomes; used to describe how far direction and timing calls can be trusted. |
| not independent of | Personas sharing a company, lab or long collaboration; cannot be the only representatives of one side at a table. |

## Evidence labels

| Label (English runs) | Meaning |
|---|---|
| `[quoted]` | A sourced quote or near-verbatim statement. English quotes stay under 15 words; at most one quote per source. |
| `[synthesized]` | Summarized from several public sources. |
| `[inferred]` | The agent's extrapolation from the persona's framework. |
| `[writer]` | The lead writer's own judgment in the report. |

The linter accepts either the English or the Chinese form.

## Run files

| Term | File |
|---|---|
| scope (run brief) | `scope.md`: the task brief every sub-agent reads. |
| evidence brief | `evidence/brief.md`: shared facts, numbered `F1, F2, …`, each with a source. Kept under 20 KB. |
| errata | `evidence/errata.md`, `evidence/errata_B.md`: corrections from fact-check passes ① and ②. |
| rubric | `rubric.json`: options, dimensions, scale, levers, aggregation rules, non-independent groups. Frozen once personas submit. |
| options | What is being scored (directions, offers, plans…). IDs are defined in the rubric. |
| dimensions | Sub-scores per option, defined in the rubric (for example impact, timing, fit). |
| levers | Optional: each persona splits 100 points across the factors that will most decide the outcome. |
| named questions | Questions the user wants answered head-on. |
| claims to test | Claims the user heard from others and wants checked (attributed only as "a friend", "a mentor", …). |
| reversal signals | Observable facts that would change the conclusion. |
| `RUN_METADATA.md` | Timeline, inputs, independence and limitations. Required in every run. |

## Rounds

| Code | Term | Meaning |
|---|---|---|
| R0 | card extraction | Persona agents read their own folder and write `card.yaml`. |
| R1 | independent scoring | Each persona and baseline scores every option alone. |
| X | crux map and seating | Disagreements become 2–9 cruxes; personas are seated at debate tables. |
| A | opening | One post per table per persona. |
| B | exchange | Reply to the strongest opposing post; ask one named persona a question; optional interjections at other tables. |
| — | interjection | A short post at a table one does not sit at; only allowed with a new argument or new evidence. |
| ② | in-debate fact-check | Between B and C, so corrections arrive before anyone changes a score. |
| C | closing | Concessions, holds, answers, the fact that would settle the disagreement, bridges. |
| S | scribe notes | Two versions per table: persona-facing (`summary/`, never says who persuaded whom) and full (`summary_full/`). |
| OT | overtime | The sharpest pair per table goes 2–3 more rounds; cross-table replies also go here. |
| R3 | private re-score | Personas re-score after reading persona-facing notes; every change must cite and restate the argument that caused it. |
| ③ | post-R3 fact-check | New claims plus an experience check (is the story really in the dossier?). |
| J | judging | Per-table verdict and per-post scorecard. |
| W | report | Lead writer; scores only from the aggregated `summary.md`. |
| — | review | Independent review before delivery. |

## Debate mechanics

| Term | Meaning |
|---|---|
| crux | A question that people disagree on and that facts can move. |
| debate table | A named group of 4–6 personas debating one crux. |
| experience argument | What I lived through (with dossier section), what it taught me, why it applies here, where the analogy may break. A legitimate argument, judged by whether the analogy holds. |
| source challenge | "Is this evidence published by you or your own company? Is there an independent source?" The challenged persona produces one or retracts. |
| self-check | A budgeted web search about one specific claim, logged in the post's JSON. |
| retraction | Withdrawing a claim after a source challenge or a correction. |
| verdict | Per point of an opposing post: `accept` or `reject` (no "partially"; the tooling still counts a legacy `partial` value from older runs). |
| empty concession | Accepting an argument in text while leaving the score unchanged. Tracked. |
| social reason | Changing a score because others changed or because a majority agrees. Not counted as persuasion; flagged. |
| `held_despite` | R3 field listing accepted arguments that did not move the score, with the reason. |
| `intended_moves` | C-round field; compared with actual R3 moves. |
| persona–baseline gap | Median persona score minus baseline score per option: what the persona layer adds over asking the model directly. |
| fidelity test | Rebuild a persona from sources before a cutoff date and predict the person's public statements after it; blind-graded. |
| reader pack | A one-page version for the user to read; the full record stays in Git. |
| calibration log | `workspace/context/calibration_log.md`: the user's feedback over time; newest at the bottom; later runs follow it. |
| light mode | A cheaper alternative to debate tables: pairwise critiques in one wave, replies in a second wave sent only after every critique is in (`protocol/03_debate_tables.md`). |
| consult mode | "What would persona X say about my choice?" in minutes, without a full run. |
