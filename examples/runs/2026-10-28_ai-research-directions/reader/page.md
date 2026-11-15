# AI research directions — one page

> Adapted from a real run. Every persona output is a simulation based on public material, not
> the person's own words; none of the people simulated has reviewed or endorsed it. Twenty
> persona agents and two no-persona baselines (Z1, Z2) are instances of one model — agreement
> among them is not independent evidence. Material cutoff: 2026-10-28. Persona IDs map to names
> in `scope.md`; full record: `report.md`, `board/summary/`, `judge/`, `r3/`.

**Bottom line.** Evaluation science (D05) and embodied AI (D06) rank 1st and 2nd across all 16
directions under both weight sets tested, before any personal weighting (`summary.md`). Each
persona's `overall` score adds its own weighting for one early-career researcher's situation and
is not a second field ranking (`scope.md`, `README.md`).

## Field ranking (top 7, either weighting)

D05 Evaluation science, D06 Embodied AI, D03 Agent self-improvement, D08 World models, D09
Simulation/synthetic data, D07 Generative policies/WAM, D13 Interpretability/safety. No
direction's rank moves 3+ places between weight sets (`summary.json`).

## The seven tables, in short

| Table | Crux | Where it landed |
|---|---|---|
| X1 | Evaluation (L1) vs. data/world models as top lever | Both needed; K3 still ranks evaluation below levers that produce capability (`r3/K3.json`) |
| X2 | Academic impact: evaluation alone, or team + compute | Converged: a new foundation model needs both (`board/summary/X2.md`) |
| X3 | World models: proven, or price ahead of evidence | Not yet proven; valuations run ahead (General Intuition $320M/$2.3B); C5/C6 still split on what that implies (`r3/C5.json`,`r3/C6.json`) |
| X4 | Agent self-improvement: real, or compute spend as story | Mostly thin evidence; DGM's $22K figure withdrawn; K2 still bets on 2027 (`evidence/errata_B.md`) |
| X5 | Physical AI: representations (D08) vs. action policies (D07) | 3–3; D07 gained after a Diffusion-Policy misattribution was corrected (`evidence/errata_B.md` #13) |
| X6 | Can simulation replace scarce real robot data | Yes for non-contact/long-tail; no for contact; smallest gap of any table |
| X7 | Does RLVR teach new reasoning | No — it resamples (Yue et al., confirmed); dispute is how much reliability is worth (`r3/C3.json`) |

## What changed minds

- RLVR's mechanism question settled toward "resampling, not new reasoning," but several
  personas (K6, M2, M6, K2, C1) then raised D02 anyway for the separate reason that reliable,
  cheap execution is itself economically decisive (`overtime/X7/1_C3`).
- D08 is the most-moved option in the run (11 of the 18 personas who scored it), in both
  directions — lowered by C3/K1/K2/K4/M4/M8/C6 on valuation-ahead-of-evidence grounds, raised by
  C1/C5/M1/M7 on narrower readings of what the evidence actually rules out.
- D07 overtook D08 in head-to-head pairwise preference (.45→.55) after personas retracted the
  claim that Diffusion Policy was adopted by π0/GR00T N1 (`summary.md`).

## Versus the no-persona baselines

Persona medians differ from baseline `Z1` by a mean absolute 0.906 points and from `Z2` by 0.969
(0–10 scale). Biggest gaps: personas score multimodal generation (D12) 3 points lower than
either baseline; they score AI for science (D15) and agent systems (D04) 2 points higher
(`summary.json`). `[writer]` This is roughly where named path-dependent experience (skepticism
about consumer generative media; direct stakes in science and agents work) moves the needle most.

## Late entry (Q5) — a sample

Already-too-late modes, attributed by ID (full table in `report.md`): general pre-training from
scratch (C1, C3, K5); calling any realistic video generator a "world model" (K6, M5); competing
purely on consumer image/video realism (C1, C2, K1); chasing public leaderboard rank (C1, K3).

## Research taste (Q6) — a sample

Each is one simulated persona's advice (full list in `report.md`):

- **C5 (Sergey Levine):** work somewhere your method fails for real, every week.
- **C6 (Demis Hassabis):** pick falsifiable problems and set a forced test window.
- **K4 (Andrej Karpathy):** ask first whether a result can be gamed, then whether it looks good.
- **K5 (Yann LeCun):** ask if you can build and test it now, not whether you can publish it.
- **M8 (Jun Zhu):** settle "real structure vs. interpolation" with ablation, not a probe.

## Fact-checks and experience check

Fact-check ②: 14 claims checked after round B, 8 confirmed, 6 partly confirmed, 4 corrections, 6
source challenges (`evidence/errata_B.md`). Fact-check ③: 11 new claims after R3, 9 confirmed, 2
partly confirmed; an experience check of 20 "I lived through this" arguments found 16 matched
their persona's dossier as told, 4 had a mismatched detail, 0 were not found (`audit.md`).

## Limitations

One model plays all 20 personas and both baselines — not independent evidence. K3 read design
material at R0 that others did not; a shared scratch directory briefly leaked a fragment of one
table's draft to another agent. Only 14+11 claims and 20 experience arguments were independently
checked; the rest were not. `overall` reflects one early-career researcher's weighting and, in
the original run, a now-removed career-capital dimension. Interest lines are dated 2026-10-28;
some roles have since changed (`RUN_METADATA.md`).
