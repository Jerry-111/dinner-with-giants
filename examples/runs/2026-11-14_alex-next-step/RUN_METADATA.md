# RUN_METADATA: 2026-11-14_alex-next-step

| Item | Content |
|---|---|
| Run | `2026-11-14_alex-next-step` — bundled example |
| Question | Alex's next step: O1 big-lab research engineer, O2 founding ML engineer at a biotech startup, O3 PhD with a new assistant professor, O4 an independent open-source year; Q1 (PhD in an industry-led era), Q2 (conditions for O4) |
| User | Fictional ("Alex"); context in `examples/context/` |
| Personas | H1 Franklin, H2 Darwin, H3 Faraday, H4 Curie, H5 Lovelace, H6 Su Shi — historical, rebuilt from their own public-domain writings (`examples/personas/`); baseline Z1 |
| Materials through | 2026-11-14 (evidence brief); personas' own materials end at their deaths |
| Environment | Claude Code; orchestrator plus one sub-agent per persona, continued across rounds with SendMessage; fresh agents for the evidence brief, fact-checks, crux map, scribe notes, judging, report and review |
| Size | Panel: 6 personas, 3 tables of 4, 2 seats each; overtime skipped |
| Main outputs | `report.md`, `summary.md`, `reader/page.md` |

## Timeline (PT, 2026-11-14)

| Time | Event |
|---|---|
| 02:00 | `scope.md` and `rubric.json` written; rubric frozen before any R1 submission |
| 01:50–02:20 | Persona research: six persona agents in parallel, each from primary sources (R0 cards written as part of research) |
| 02:00–02:28 | Evidence brief (fresh agent): 18 facts, 6 open questions. Used 16 web searches against a budget of 15 (one over, chasing a model-license detail). Startup-funding figures are secondary only: the publisher's pages refused direct access and were not worked around |
| 02:29–02:50 | Fact-check ① on the brief (fresh agent, no persona material): 12 facts checked — confirmed 7, partly confirmed 4 (two wrong numbers inside them: CS time to degree 8.2 not 8.0 years; biology 7.9 not 7.6–7.8), wrong 0, not found 1 (publisher refused automated access). `evidence/errata.md`; one pointer line added to the brief |
| 02:47–03:38 | R1, independent scoring. Starts were staggered as each persona finished research (H1 02:47, H3 and H6 03:14, H4 and H5 03:25, H2 03:33); R1 reads no other persona's work, so staggering does not break independence. Baseline Z1 02:48–03:08. `tools/sim.py check r1`: 6 files, 6 clean |
| 03:39–04:14 | X: crux map and seating (fresh agent, no persona material). Three cruxes, three tables of four, every table a natural 2–2 split; `tools/sim.py tables`: 0 problems |
| 04:15–04:22 | A: 12 opening posts, sent to the six persona agents in two batches of three (rate-limit precaution). During A, H2 edited the pronouns in its own `card.yaml` (wording only; no scores, facts or stance changed); no further persona-file edits were allowed. `tools/sim.py index` → `board/A/INDEX.md` |
| 04:23–04:34 | B: 12 exchange posts and 5 interjections (two at X1, two at X2, one at X3 — within the cap). Two self-checks used (H2, H6) |
| 04:37–04:55 | Fact-check ② (fresh agent, between B and C): 7 claims — confirmed 3, partly confirmed 3 (wrong numbers inside: F12 biotech seed-and-A total is $4.4B per the publisher, not the brief's figures; F10's 2024 conversion figure not matched), wrong 0, not found 1 (a job posting cited without a URL). Both logged self-checks audited; one generalized a 437-respondent self-selected survey to all maintainers. `evidence/errata_B.md`, read by every persona before C |
| 04:56–05:10 | C: 12 closing posts with `intended_moves`. Several retractions followed fact-check ②: a funding-drop figure and a 2024 conversion figure (H4, H2), an unverifiable job posting (H6), a "resourced teams win" framing after the prize-split evidence (H3) |
| 05:11–05:34 | S: scribe notes, two versions per table (fresh agent). Final sizes 1.6–1.8 KB (persona-facing) and 2.5–2.6 KB (full); the persona-facing notes contain no statement of who persuaded whom. **Process slip:** the orchestrator released R3 at 05:24, when the six files had been unchanged for 90 seconds, but the scribe was still trimming them to the size targets until 05:34. Personas therefore read a slightly longer earlier version of the persona-facing notes (same sections, no persuasion statements). Rule added to `CLAUDE.md`: release a round on the agents' completion replies, not on files that look finished |
| 05:11–05:30 | J: judge with per-post scorecards for all 41 posts (fresh agent), in parallel with S and R3. Most lopsided table: X2 (both interjections there pressed the same side) |
| 05:24–05:34 | R3: private re-score (six persona agents, continued); 11 score changes, each citing a post and restating its argument. Baseline Z1 re-scores on the same material (persona-facing notes and both errata files): one change, O1 7→8 |
| 05:36–05:58 | Fact-check ③ (fresh agent): 6 new claims — confirmed 4, partly confirmed 2. Experience check of 12 arguments against dossier §A/§B/§G/§I: 6 as told, 4 with details changed, 2 not found (relabeled `[inferred]`), including the strongest argument on one side of X2. `audit.md` |
| 05:58 | `tools/sim.py aggregate` → `summary.json`, `summary.md`. Logging gap found: personas raised source challenges in prose but left the JSON `source_challenge` field empty, so the script counts 0 while the judge flagged 3 |
| 05:59–06:50 | W: report (fresh lead-writer agent). First draft 47 KB, trimmed to 28.8 KB against the run's target; the writer re-checked that no remaining claim lost its citation |
| 06:51–07:10 | Independent review (fresh agent, has not read the debate): 9 findings, 3 severe (a count, two attributions); none changes the conclusions. Reader pack (fresh agent) in parallel → `reader/page.md` |
| 07:12–07:19 | Lead writer fixes all nine findings; disposition recorded at the end of `review.md`. No second review pass |

## Totals

- Wall-clock: about five hours end to end, about an hour and a half of it building the six
  personas from sources.
- Agents: 17 fresh sub-agents (6 persona research, evidence brief, fact-checks ①②③, baseline,
  crux map, scribe, judge, lead writer, reviewer, reader pack) and about 31 continued turns of
  persona agents (R1, A, B, C, R3) plus one baseline continuation (R3).
- Self-checks logged: R1 and R3 a handful; debate rounds 3 in total.
- Skipped: overtime; the optional per-area digest.

## Independence and limitations

- All personas, the baseline and every checking agent are instances of one model. Agreement among
  them is not independent evidence.
- The personas lived between the 11th and 19th centuries. Their experience arguments are analogies
  across centuries; each post must say where the analogy breaks.
- Persona research and R0 were done by the same agents, which were then continued into the debate.
- Overtime was skipped to keep the example small.
- Alex is fictional. All persona content is a simulation based on public material, not the words
  of the people named.
