# Examples

Two complete runs and one fictional user. Every persona output in them is a simulation based on
public material, not the person's own words.

| Path | What it shows |
|---|---|
| [`runs/2026-10-28_ai-research-directions/`](runs/2026-10-28_ai-research-directions/) | A full 20-persona run, adapted from a real run: 16 AI research directions, seven debate tables with overtime, three fact-checks, judges, private re-scores, two no-persona baselines. Translated from Chinese; the original user's personal details removed. |
| [`runs/2026-11-14_alex-next-step/`](runs/2026-11-14_alex-next-step/) | A complete panel run with six historical figures on a fictional student's career decision: every file from the frozen rubric to the reviewer's findings. |
| [`context/`](context/) | The fictional user Alex's context: profile, preferences, feedback log. A model for your own `workspace/context/`. |

The personas both runs use are in the library at [`../personas/`](../personas/).

## Reading order for a run

1. `reader/page.md`: the one-page version.
2. `report.md`: the full report, with post IDs you can follow.
3. `board/`: the debate itself. `board/summary/` has the scribe's notes per table.
4. `summary.md`: the numbers, including the persona − baseline gap.
5. `scope.md` and `rubric.json`: the question and the frozen rules.
6. `RUN_METADATA.md`: timeline, what was skipped, slips, limitations.
