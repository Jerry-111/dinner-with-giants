# Report: AI research directions (run `2026-10-28_ai-research-directions`)

> **Notice.** This is an adapted version of a real run. Every persona output in this folder is a
> simulation based on public material, not the person's own words. None of the people simulated
> here has reviewed, endorsed or contributed to their persona (`README.md`, `RESPONSIBLE_USE.md`).
> Twenty persona agents and two no-persona baselines (Z1, Z2) are all instances of one model;
> agreement among them is not independent evidence (`RUN_METADATA.md`). Interests are shown in
> each post's header as dated facts; they are never applied to raise or lower a score
> (`scope.md`, principle 2).

Written from the run's public files only. A one-page version is `reader/page.md`. Persona IDs
map to names in `scope.md`; each is named in full the first time it appears below, and by ID
alone after that. Judgments that are this writer's own are marked `[writer]`.

## Headline results

**Field-level ranking.** Ranking the 16 directions by the four public dimensions (impact,
bottleneck, academic edge, window), under both weight sets in `rubric.json` (`equal`:
25/25/25/25; `impact_heavy`: 38.9/27.8/16.7/16.6), gives the same top seven in the same order
under both weightings (`summary.md`, "Rank by weight set"):

| Rank | Direction | equal | impact_heavy |
|---|---|---|---|
| 1 | D05 Evaluation science | 1 | 1 |
| 2 | D06 Embodied AI and robot learning | 2 | 2 |
| 3 | D03 Agent learning and self-improvement | 3 | 3 |
| 4 | D08 World models and spatial intelligence | 4 | 4 |
| 5 | D09 Simulation and synthetic data | 5 | 5 |
| 6 | D07 Generative policies and world action models | 6 | 6 |
| 7 | D13 Interpretability, alignment and safety | 7 | 7 |
| 8–9 | D11 Multimodal understanding / D02 Post-training and RL | 8 / 9 | 9 / 8 |
| 10 | D14 AI infrastructure and co-design | 10 | 10 |
| 11 | D01 Pre-training and foundation models | 11 | 11 |
| 12 | D10 Autonomous driving | 12 | 12 |
| 13 | D04 Agent systems and ecosystem | 13 | 13 |
| 14 | D12 Multimodal generation | 14 | 14 |

D15/D16 are scored `overall`-only and have no per-dimension weighted rank. No direction's rank
moves 3+ places between weight sets (`summary.json`, `sensitivity_flips: []`); only D11 and D02
trade 8th/9th. Evaluation science (D05) and embodied AI (D06) rank first and second under both
weightings (`README.md`).

**`overall` medians.** Each persona's `overall` is its own weighting of the dimensions, scored
for one early-career researcher's situation — undergraduate-to-master's stage, choosing a
direction now (`scope.md` Q2). In the original run this weighting also included a career-capital
dimension removed for privacy, so `overall` is a researcher-facing judgment, not a second
field-level ranking (`README.md`, "Read with care"):

| Option | R1 median (n) | R3 median (n) | R3 rank | Changed |
|---|---|---|---|---|
| D05 Evaluation science | 8 (20) | 8 (20) | 1 | 3 |
| D06 Embodied AI | 8 (15) | 8 (15) | 2 | 1 |
| D08 World models | 6.5 (18) | 7 (18) | 3 | 11 |
| D09 Simulation/synthetic data | 7 (17) | 7 (17) | 4 | 7 |
| D02 Post-training/RL | 6 (17) | 6 (17) | 5 | 9 |
| D03 Agent self-improvement | 7 (17) | 6 (17) | 6 | 6 |
| D07 Generative policies/WAM | 6 (17) | 6 (17) | 7 | 7 |
| D15 AI for science | 6 (12) | 6 (12) | 8 | 0 |
| D11 Multimodal understanding | 5.5 (18) | 5.5 (18) | 9 | 1 |
| D13 Interpretability/safety | 5 (14) | 5 (14) | 10 | 0 |
| D10 Autonomous driving | 5 (11) | 5 (11) | 11 | 0 |
| D14 Infrastructure/co-design | 5 (18) | 5 (18) | 12 | 0 |
| D04 Agent systems/ecosystem | 5 (19) | 5 (19) | 13 | 0 |
| D16 Recommendation/retrieval | 4 (10) | 4 (10) | 14 | 0 |
| D01 Pre-training | 4 (20) | 4 (20) | 15 | 3 |
| D12 Multimodal generation | 4 (18) | 4 (18) | 16 | 0 |

(Medians and IQRs are `summary.md`'s; IQR dropped here for space, see that file for the full
figures.) D08 moved most (11 of the 18 personas who scored it) and climbed 5th to 3rd; D01
overtook D12 on an unchanged median because D01's IQR narrowed while D12's held `[writer]`.
Run-wide: 48 `overall`
changes in R3, each citing its cause; 15 retractions; 6 source challenges; 377 per-point verdicts
(242 accept, 133 reject, 2 legacy "partial"); 0 empty concessions (`summary.md`).

## Lever allocation (Q1)

Each persona split 100 points across eight levers for what most decides AI progress over the
next 5–10 years (`rubric.json`); medians moved little (`summary.md`):

| Lever | R1 median (IQR) | R3 median (IQR) |
|---|---|---|
| L1 Evaluation and verification | 20 (15–25) | 19 (15–23.5) |
| L4 World models / world action models | 15 (10–20) | 15 (10–19.25) |
| L5 Scale and quality of real data | 15 (10–15.25) | 15 (10–16) |
| L2 RL and post-training | 10 (6.75–15.75) | 10 (6.75–17.25) |
| L3 Simulation and synthetic data | 10 (8–15) | 10 (8.75–15) |
| L7 Scaled-up foundation models | 10 (5–13.25) | 10 (5–13.25) |
| L8 Systems and efficiency | 9 (5.75–10) | 9 (5.75–10) |
| L6 Architectures and new paradigms | 7.5 (5–10) | 7.5 (5–10.25) |

No lever's median moved more than one point (`summary.md`).

## Q2: academic foundation models

All 20 personas took the `conditional` position in both rounds (`summary.json`). The score
converged: median 6.0 in both rounds, but IQR narrowed from 0.25 to 0.0 (min 5, max 7 unchanged)
(`summary.md`). Which of the five conditions (C1–C5, `rubric.json`) personas required moved
after the X2 table:

| Condition | R1 (of 20) | R3 (of 20) | Moved |
|---|---|---|---|
| C1 Narrow-domain model, not general pre-training | 20 | 20 | no |
| C5 Open weights with a path to outside adoption | 20 | 20 | no |
| C2 Credible third-party evaluation already exists | 14 | 14 | no |
| C3 A team of 2–4 with complementary skills | 12 | 15 | +3 |
| C4 Lab compute at scale (e.g. 64 H100s for months) | 12 | 18 | +6 |

C4 (compute) and C3 (team) both gained; C1/C2/C5 held. This matches X2's consensus that a
genuinely new foundation model needs team and compute alongside evaluation, not evaluation alone
(`board/summary/X2.md`; `cruxes.json` X2). M4, M5, M8 and C4 each name this as why they added C3
and/or C4 in R3 (`r3/M4.json`, `r3/M5.json`, `r3/M8.json`, `r3/C4.json`, `changes`).

## Pairwise comparisons that moved

Personas picked a winner in 11 standing match-ups each round (`rubric.json`). Four win rates
moved (`summary.md`, `tables.json`):

| Comparison | R1 win rate | R3 win rate | Note |
|---|---|---|---|
| D07 vs D08 | D07 .45 / D08 .55 | D07 **.55** / D08 .45 | flipped: D07 now wins more often head-to-head |
| D02 vs D03 | D02 .25 / D03 .75 | D02 **.40** / D03 .60 | D03 still wins, by less |
| D04 vs D03 | D04 .20 / D03 .80 | D04 **.25** / D03 .75 | same direction, small move |
| D05 vs D08 | D05 .70 / D08 .30 | D05 **.80** / D08 .20 | gap widened |

D07 overtaking D08 head-to-head despite D08's median still sitting above D07's (7 vs 6) tracks
the X5 table below `[writer]`. The other seven comparisons held.

## The seven tables

### X1 — Evaluation vs. data and world models as the top lever

**Crux.** Is evaluation (L1) the lever most worth betting on for the next 5–10 years, or do data,
simulation and world models matter more (`cruxes.json` X1)? Seated: C2 (Bill Gurley), K3 (Rich
Sutton), K5 (Yann LeCun), K6 (Patrick Collison), M1 (Percy Liang), M7 (Russ Tedrake) — 4 for
evaluation-first, 2 for data/world-models-first (`tables.json`).

**Strongest arguments.** Evaluation-first: M7 argues real-robot trials cannot be rerun, so
statistical design matters as much as the model (`A/X1/M7`); C2 argues an unstable judge —
GPT-4o-mini flips its answer 13.6% of the time on repeat — is itself the case for betting on
evaluation (`B/X1/C2`). Data/world-model-first: K5 argues the 2000s deep-learning comeback came
from a new way of modeling, not from fixed evaluation (`A/X1/K5`); K3 argues benchmarks and
judges only say whether a score is high, not whether the model knows if it is right (`A/X1/K3`).

**Conceded, retracted, fact-checked.** K3 retracted its claim that Oak Lab's first paper proves
credit assignment in the stream of experience works, after C2's source challenge found no
independent replication (`A/X1/K3`→`B/X1/C2`→`C/X1/K3`; `evidence/errata_B.md` table 3) — the
table's only checkable new claim. K5 and K3 each raised D05 after conceding C6's interjection
that the ImageNet evaluation, not just a new model, got the deep-learning comeback recognized
(`B/X1/C6_interjection`; `r3/K5.json`, `r3/K3.json`).

**Still disputed.** K3 still disagrees evaluation should outrank the levers that produce
capability, since it only certifies (`r3/K3.json`). What would settle it: whether, by 2027–28, an
independent team shows a world model's representation is actually used by a policy on
long-horizon real-robot tasks, not just leading inside the training distribution (`cruxes.json`
X1).

### X2 — Academic impact: third-party evaluation, or team plus compute?

**Crux.** Does an academic lab's narrow foundation model count as real impact only with
third-party evaluation, or is a team plus compute enough (`cruxes.json` X2)? Seated: C6 (Demis
Hassabis), K1 (Vinod Khosla), K2 (Jeff Dean), M4 (Saining Xie), M5 (Kaiming He), M8 (Jun Zhu),
split 4 (evaluation-as-bar) to 2 (team-plus-compute) (`tables.json`).

**Strongest arguments.** Evaluation-as-bar: M5 and M4 independently make the same point — at a
programming club, whether someone learned to code is visible at a glance, but whether a
foundation model was "done right" is not (`B/X2/M5`, `B/X2/M4`). Team-plus-compute: K2 argues
judges are unstable, so building evaluation alongside the work is a legitimate substitute for a
ready-made one (`B/X2/K2`); M8 also cited a supporting experience here — [Removed: the persona's
own company's recent news.] (`B/X2/M8`).

**Conceded, retracted, fact-checked.** Both sides converged: a genuinely new foundation model
needs team and compute alongside evaluation, not evaluation alone — K1 and K2 concede this,
C6/M4/M5/M8 accept it as their own position (`board/summary/X2.md`). K1 lowered D08 after the
observability-gap argument above (`r3/K1.json`); M4, M5 and M8 each lowered D01 for the same
reason (`r3/M4.json`, `r3/M5.json`, `r3/M8.json`). No new round-B numbers were checkable here, but
a baseline's self-check found OpenVLA — R1's small-academic-team precedent — was actually an
18-author, 6-institution project, part of why `Z1` added team as an R3 condition
(`baselines/Z1_r3.json`, `searches`).

**Still disputed.** K1 still does not accept that a pre-existing third-party benchmark must be
required, only that some verification eventually is (`r3/K1.json`). What would settle it:
comparing, by 2027–28, actual outside-adoption rates for evaluation-backed versus
self-built-evaluation academic projects (`cruxes.json` X2).

### X3 — World models: proven to drive decisions, or price ahead of evidence?

**Crux.** Has the claim that predictive representations drive decisions been shown for world
models (D08), or are valuations running ahead of the evidence (`cruxes.json` X3)? Seated: C1
(Michael Mauboussin), C5 (Sergey Levine), C6, K1, M5, M8, split 3–3 (`tables.json`).

**Strongest arguments.** Bet-heavily: K1 cites early tactile-scenario results as self-reported
evidence of improved prediction (`B/X3/K1`); M8 argues Vidar extracts inverse dynamics to serve
actions — purposeful prediction, not pure image quality (`B/X3/M8`). Not-yet-validated: C5 cites
nearly a decade of its own video-prediction-plus-planning work that did not bring deep
understanding (`A/X3/C5`); M7's interjection argues the imagination layer's blind-test yardstick
measures sampling quality, not physical correctness (`B/X3/M7_interjection`).

**Conceded, retracted, fact-checked.** M8 retracted its claim that verified imagination becoming
the foundation for action "has happened twice," after C5's challenge found it to be M8's own
synthesized account, not a checkable fact (`A/X3/M8`→`C/X3/M8`). M5 retracted its claim that the
blind-test yardstick covers physical correctness, rebutted directly by M7's interjection
(`B/X3/M5`→`C/X3/M5`). C1 corrected its own cited General Intuition round from "about $300M at
about $2B" to the actual $320M/$2.3B (`C/X3/C1`; `evidence/errata_B.md` table 1, #11) — though
K1's acceptance of it introduced a new error of its own (`judge/X3.md`).

**Still disputed.** C6 still treats the valuation-ahead-of-evidence gap as a market phenomenon
independent of research judgment; C5 still treats it as a warning about the paradigm itself
(`r3/C6.json`, `r3/C5.json`). What would settle it: whether independent teams, by 2027–28, match
a dedicated action policy's real-robot success rate using the same representation without
fine-tuning an action head (`cruxes.json` X3). Overtime (C5 vs C6) agreed to judge research time
and capital separately, with an 18-month forced test window (`r3/C6.json`).

### X4 — Agent self-improvement: real mechanism, or compute spend as narrative?

**Crux.** Is agent self-improvement (RSI) a real, scarce compounding mechanism, or compute spend
packaged as a story (`cruxes.json` X4)? Seated: C4 (Dario Amodei), K2, M1, M2 (Shunyu Yao), M3
(Graham Neubig); C4 and M1 held "still narrative" throughout, K2 held "real," and M2/M3 were
seated "bet heavily" but posted closer to the middle (`judge/X4.md`).

**Strongest arguments.** Thin-evidence: C4 and M1 both cite METR's finding that, on a strong
baseline, 70–90% of the cost in most self-improvement trajectories is compute spent on trial and
error (`A/X4/C4`, `A/X4/M1`). Bet-heavily: K2 cites AlphaEvolve continuously reclaiming about
0.7% of Google's global compute for over a year (`B/X4/K2`).

**Conceded, retracted, fact-checked.** K2 retracted the Darwin Gödel Machine's "$22,000 over two
weeks" figure after the fact-check traced it only to a second-hand blog with no primary source
(`B/X4/K2`→`C/X4/K2`; `evidence/errata_B.md` table 1, #8), and separately cut its own D03 score
from 8 to 6 after C4 and M1 caught it scoring as settled what it had just called unreliable to
measure (`judge/X4.md`; `r3/K2.json`).

**Still disputed.** K2 still bets independent verification of RSI arrives around 2027, against
C4's default skepticism (`r3/K2.json`). What would settle it: compute-normalized, reproducible,
independent tests showing a self-improving system's edge over random search widening with scale,
rather than sitting inside the 1.9–37×/year noise band the table converged on as too wide to
prove anything (`cruxes.json` X4).

### X5 — Physical AI: bet on representations, or on verifiable action policies?

**Crux.** Bet on abstract world models and representations (D08), or on generative action
policies that can be verified directly (D07) (`cruxes.json` X5)? Seated: C1, C2, M3, M4, M6
(Fei-Fei Li), M7, ending 3–3 after three rounds (`tables.json`; `judge/X5.md`).

**Strongest arguments.** D08 side: M4, backed by a search confirming OpenVLA's backbone, argues
representation quality sets the ceiling — OpenVLA fuses DINOv2 and SigLIP, so its 15-point win
over a diffusion head is a decoding-layer difference, not proof representations don't matter
(`C/X5/M4`; `audit.md` table 1, #1–2). D07 side: M7 cites LBM's blind, randomized real-robot
validation (`A/X5/M7`); M3 argues D07 has the plain test of whether a control task succeeds,
while D08's "readable means usable" test does not exist (`A/X5/M3`).

**Conceded, retracted, fact-checked.** C1, C2, M6 and M7 each retracted the claim that Diffusion
Policy was adopted by π0 and GR00T N1, after the fact-check found π0's core is flow matching and
GR00T N1 a related but distinct lineage (`evidence/errata_B.md` table 1, #13). M4 narrowed its
claim after M8's interjection noted D07 predicts observations and actions jointly, rather than
attaching an action head to a learned representation (`B/X5/M8_interjection`→`C/X5/M4`). `audit.md`
(table 1, #1–2) independently confirmed the shared DINOv2+SigLIP backbone that M4's R3 change
relies on, and that M6 and C2 also cite in their own round-C reasoning (`r3/M6.json`,
`r3/C2.json`).

**Still disputed.** M6 still disagrees the weak claim — bet on the hardest-to-replicate upstream
capability regardless of whose yardstick is ready first — has been rebutted (`r3/M6.json`). What
would settle it: whether a representation-first method without action-head fine-tuning matches an
action-first method's real-robot success rate outside the originating team (`cruxes.json` X5).

### X6 — Can simulation substitute for scarce real robot data?

**Crux.** Can simulation and synthetic data substitute for scarce real robot data, especially
contact and the long tail (`cruxes.json` X6)? Seated: C3 (Jensen Huang), C5, K3, K4 (Andrej
Karpathy), K5 — 2 for "yes, a real lever," 3 for "no, real data is the core" (`tables.json`).

**Strongest arguments.** Pro: K4 argues domain randomization composes new training signal within
a physical prior — a real gain for visual diversity and the long tail — the only argument at the
table everyone accepted (`B/X6/K4`). Con: C5 argues simulated or generated trajectories inject no
new information on their own (`A/X6/C5`); K3 cites Physical Atari, where swapping in a second,
identically built robot body degraded all six games, showing the gap is wider than contact and
touch (`B/X6/K3`).

**Conceded, retracted, fact-checked.** K3 withdrew a fabricated detail — two named games
recovering only partly after about 12 hours — after the fact-check found no such figures in the
source (`B/X6/K3`→`C/X6/K3`; `evidence/errata_B.md` table 1, #14). C3 partly withdrew its "about 6
months of cash left" figure after K3's source challenge; the episode checked out but the number
did not, so C3 kept the story and dropped the figure (`evidence/errata_B.md` table 3). C5 raised
D09 after conceding K4's domain-randomization point, narrowing its own claim that simulation
creates no new information (`r3/C5.json`).

**Still disputed.** K3 still disagrees that "most" of a non-contact gain should count as
simulation's credit — both sides call this empirical, not a values question (`r3/K3.json`). What
would settle it: whether pure-simulation policies on contact-rich tasks can be replicated by a
third party and match a real-data baseline by 2027–28 (`cruxes.json` X6). Overtime (C5 vs K4)
proposed a direct test neither side has run: 200 real seeds alone versus 50,000 simulated
amplifications added (`board/summary/X6.md`).

### X7 — Does RLVR teach new reasoning, or polish and resample?

**Crux.** Does post-training with verifiable rewards (RLVR) teach new reasoning, or mainly
polish and resample what the base model already has (`cruxes.json` X7)? Seated: C3, C4, K4, K6
(Patrick Collison), M2, M6 (`judge/X7.md`).

**Strongest arguments.** K4 cites Yue et al. (NeurIPS 2025 Oral): under strictly verifiable
rewards, at large sample counts the base model's own pass@k matches or beats the RL-tuned model
(`A/X7/K4`). C3 cites s1 raising AIME24 from 50.0 to 56.7 using only 7 H100 GPU-hours, a gain hard
to explain as pure resampling (`A/X7/C3`).

**Conceded, retracted, fact-checked.** C4 formally retracted its argument that RLVR output being
distillable proves it is "not lucky resampling," after K4, K6, M2 and M6 each independently
rebutted it — distillable shows a behavior can be imitated, not that it exceeds the base model's
own distribution (`A/X7/C4`→`C/X7/C4`). K6 withdrew its MongoDB/Ruby-on-Rails analogy, conceding
switching cost is not a capability ceiling (`A/X7/K6`→`C/X7/K6`). `evidence/errata_B.md` confirms
all three facts this table built on (Yue et al., s1's 7 GPU-hours, DeepSeek-R1's GRPO) and finds
no correction needed anywhere in this table — the cleanest factual record of the seven (table 1,
#1–3).

**Still disputed.** With mechanism settled, what remains is value: C3 still scores reliable
execution as a mid-high, decisive lever; K4, K6, M2 and M6 each still file it under efficiency,
below new-paradigm (`r3/C3.json`). Both sides call this a values disagreement, not a factual one
(`board/summary/X7.md`). What would settle it: whether inference-cost declines through 2027–28
trace mainly to reliability/systems investment, or to pre-training scale (`r3/C3.json`).

## What changed minds (R3)

Forty-eight `overall` scores moved between R1 and R3, each citing the post that caused it
(`summary.json`, `moves`). They cluster into a few arguments that moved several personas at once.

**RLVR teaches no new out-of-distribution reasoning (X7 mechanism).** C4 cut D02 from 8 to 6,
retracting its own distillation argument after four rebuttals (`B/X7/K4`, `B/X7/K6`, `C/X7/M2`,
`B/X7/M6`; `r3/C4.json`). C5 and C6 each lowered D02 citing the same large-k result (`A/X7/K4`;
`r3/C5.json`, `r3/C6.json`).

**Reliable execution still carries real economic weight (X7 value question).** K6, M2, M6, K2 and
C1 each raised D02 instead, citing C3's "tokens per watt" framing from overtime — scaled,
reliable execution can be decisive without being a new paradigm (`overtime/X7/1_C3`; `r3/K6.json`,
`r3/M2.json`, `r3/M6.json`, `r3/K2.json`, `r3/C1.json`). M3 raised D02 too, since the same
settlement vindicates evaluation methodology itself (`r3/M3.json`).

**World-model valuations are running ahead of decision-layer evidence (X3).** C3, K2, K4 and M8
each lowered D08 citing the X3 valuation evidence directly (`A/X3/C5`, `board/summary/X3.md`,
`C/X3/C1`, `B/X3/M7_interjection`; `r3/C3.json`, `r3/K2.json`, `r3/K4.json`, `r3/M8.json`). K1
lowered D08 too, combining this with X2's observability-gap argument; M4 cited X3 and X5
together; C6 cited X3 alone (`r3/K1.json`, `r3/M4.json`, `r3/C6.json`). Against this, C1, C5, M1 and M7 each raised D08 instead, on
narrower readings of what the evidence rules out (`overtime/X3/2_C5`, `B/X3/M8`, `B/X1/K5`,
`C/X5/M6`; `r3/C1.json`, `r3/C5.json`, `r3/M1.json`, `r3/M7.json`).

**D07 gained on D08 after the Diffusion-Policy correction and LBM's no-replication finding
(X5).** C2 and M7 each lowered D07 after conceding LBM's validation has no outside replication
(`B/X5/M6` source challenge; `r3/C2.json`, `r3/M7.json`). C1, C5, C6, K2 and K6 each raised D07
instead, citing X5's argument that D07 has a plain pass/fail test while D08's does not, directly
(`A/X5/M3`; `r3/C1.json`, `r3/C5.json`, `r3/C6.json`, `r3/K2.json`, `r3/K6.json`).

**Team and compute, not evaluation alone, for a genuinely new foundation model (X2).** M4, M5
and M8 each lowered D01, and C4 widened its own Q2 conditions to add team, citing the X2
consensus (`B/X2/K2`, `B/X2/M5`, `B/X2/M4`; `r3/M4.json`, `r3/M5.json`, `r3/M8.json`,
`r3/C4.json`).

**Domain randomization is a real, bounded gain; the simulation gap is wider than "contact only"
(X6).** C5, K3, K5, M3 and C2 each raised D09 citing K4's domain-randomization argument and the
accepted legged-locomotion zero-shot transfer (`B/X6/K4`; `r3/C5.json`, `r3/K3.json`,
`r3/K5.json`, `r3/M3.json`, `r3/C2.json`). C3 and K4 lowered D09 instead, citing K3's Physical
Atari evidence that the weak zone is wider than contact and touch (`B/X6/K3`; `r3/C3.json`,
`r3/K4.json`).

**Certification is not production, but it still decides recognition (X1).** K3 and K5 each
raised D05 after accepting C6's interjection that the ImageNet evaluation is what got the
deep-learning comeback recognized (`B/X1/C6_interjection`; `r3/K3.json`, `r3/K5.json`); `Z1` and
`Z2` raised D05 too, for related reasons (`baselines/Z1_r3.json`, `baselines/Z2_r3.json`). M3
lowered D05's impact after its own cited
argument — that certifying is not producing — was turned back on its own score (`A/X1/K3`;
`r3/M3.json`).

## Where the room differs from the no-persona baselines

The two no-persona baselines (`Z1`, `Z2` — same method and brief, no persona identity) score the
same 16 directions without debating. The persona median differs from `Z1` by a mean absolute
0.906 points and from `Z2` by 0.969 points, on the 0–10 scale (`summary.md`,
`persona_minus_baseline`). Largest single gaps, persona median minus baseline (`summary.json`):

| Option | vs Z1 | vs Z2 | Direction |
|---|---|---|---|
| D12 Multimodal generation | −3.0 | −3.0 | personas lower |
| D15 AI for science | +2.0 | +2.0 | personas higher |
| D04 Agent systems/ecosystem | +2.0 | +2.0 | personas higher |
| D01 Pre-training | −1.0 | −1.0 | personas lower |
| D02 Post-training/RL | −1.0 | −1.0 | personas lower |
| D07 Generative policies/WAM | −1.0 | −1.0 | personas lower |
| D16 Recommendation/retrieval | +1.0 | +1.0 | personas higher |

`[writer]` The two largest, opposite-direction gaps suggest what simulating named people adds
over one generic pass: on D12, personas with path-dependent experience of consumer-media
economics (the Second-Life analogy, Sora 2's shutdown: `r3/C2.json`, `r3/K1.json`) converge below
a baseline with no equivalent built-in skepticism. On D15 and D04, personas with direct track
records (`r3/C6.json`, `r3/C4.json`, `r3/K6.json`, and agents specialist M2) pull the median
above a baseline that treats both as generic adjacent fields. The rest (D05, D06, D08, D09, D11,
D13) are where debate and a cold read of the brief land in about the same place.

## Q5: late entry, by direction

Ways of taking part that personas call already too late, absorbed or commoditized, from
`late_modes` in the R3 files, attributed by ID (`r3/<ID>.json`):

| Direction | Already too late | Who said it |
|---|---|---|
| D01 Pre-training | General foundation model from scratch to chase scores; compute is locked up by a few labs | C1, C3, K5 |
| D02 Post-training/RL | Reproducing a standard RLHF/RLVR pipeline with no algorithmic contribution | C2, K3 |
| D03 Agent self-improvement | Packaging score gains as RSI, not compute-normalized or pre-registered | C1, K3 |
| D04 Agent systems | Hand-built scaffolding; vendor CLI agents have absorbed this layer | C1, K3, K6 |
| D05 Evaluation science | Chasing public leaderboard rank, distorted by unequal private-test access and gaming | C1, K3 |
| D06 Embodied AI | Standardized demos or viral videos with no statistical real-robot validation | C2, K6, M7 |
| D07 Generative policies/WAM | Chasing the WAM label itself, now a naming and demo contest, not a method | K3, K6 |
| D08 World models | Calling any realistic video generator a "world model," an overused label | K6, M5 |
| D09 Simulation/synthetic data | Claiming "unlimited" synthetic data with no quantified real-world correlation | C1, K4, M7 |
| D10 Autonomous driving | A small team building an end-to-end demo with no fleet or long-tail data | C2, K4, K5 |
| D11 Multimodal understanding | Chasing MLLM/VQA scores with no error analysis; absorbed within months | K4, M4 |
| D12 Multimodal generation | Competing on consumer image/video realism, a commoditized price war | C1, C2, K1 |
| D13 Interpretability/safety | Basic SAE dictionary learning, after major labs lowered its priority | C4, C6 |
| D14 Infrastructure/co-design | Single-operator or efficiency optimization, soon absorbed into the next generation of frameworks | M2 |

D15–D16 carry no `late_modes` entries; most personas gave them an `overall`-only score or no
judgment (`r3/*.json`).

## Q6: research taste

The most distinct pieces of advice from the R3 files, each a simulated persona's advice,
attributed by ID and name (`r3/<ID>.json`, `taste_advice`):

- **C1 (Michael Mauboussin):** capital price and research opportunity are two clocks; don't let
  a valuation or narrative decide whether a problem is worth working on.
- **C2 (Bill Gurley):** make sure what you build is attributable to you even if you change
  employers; don't let it look good only in one company's own reporting.
- **C5 (Sergey Levine):** study the mechanism by which experience becomes capability; work
  somewhere your method fails for real, every week.
- **C6 (Demis Hassabis):** pick problems that can be evaluated cleanly and falsified, with a
  forced test window, rather than holding a bet indefinitely.
- **K3 (Rich Sutton):** write one page of notes a day and argue with your own ideas in it; keep
  it up for at least a year.
- **K4 (Andrej Karpathy):** ask first whether a result can be gamed, then whether it looks good;
  simulation teaches you how a simulator lies.
- **K5 (Yann LeCun):** ask whether you can build and test it right now, not whether you can
  publish it — learned, it says, from a decade on pixel prediction.
- **K6 (Patrick Collison):** have your model take one outside test it could fail before claiming
  it is useful; don't trust only the ruler you built yourself.
- **M6 (Fei-Fei Li):** find a bold problem that is genuinely your own, not other people's
  questions answered faster — citing years of unremarkable papers before the one that counted.
- **M8 (Jun Zhu):** ask whether a result reflects learned physical structure or is interpolation,
  and settle it with ablation, not a probe — reading out a concept is not the same as using it.

K2's submission adds: write down a prediction and check it a year later, citing a paper backed
after a major conference rejected it.

## Fact-checks and the experience check

Fact-check ② (`evidence/errata_B.md`, after round B) checked the 14 claims most cited that
round: 8 confirmed, 6 partly confirmed, 4 corrections written up; all 6 source challenges found
either no independent source (Oak Lab's paper, "pioneered the category," "pattern happened
twice") or a source real but not independent of the challenged party (LBM, a cash-runway figure).

Fact-check ③ (`audit.md`, after R3) checked 11 new claims from round C, overtime and R3: 9
confirmed, 2 partly confirmed, 0 contradicted. Its experience check tested 20 "lived through
this" arguments against each persona's dossier: 16 matched as told; 4 had a mismatched detail (a
scribe error on C5's QT-Opt numbers, a more specific story than K4's dossier records, two of M6's
self-assessments merged into one); 0 were not found at all.

## Limitations

Taken from `RUN_METADATA.md` and `README.md`:

- **One model.** All 20 persona agents, both baselines, and the support agents are instances of
  one model; agreement among them is not independent evidence. C4 (Dario Amodei) is Anthropic's
  CEO and K4 (Andrej Karpathy) joined its pre-training team in 2026-05 — disclosed, not adjusted
  for.
- **K3 read design material at R0** other personas did not (the orchestrator's design notes and
  the user's topic list); not restarted, and later instructions forbade this.
- **Shared scratch directory** until about 16:50: M4 reported seeing a fragment of table X3's
  material from another agent's overwritten file, and reports not using it. Per-persona scratch
  folders are now required (`CLAUDE.md`).
- **Self-reported change values.** M6's R3 `changes` give D07/D08 `from` values that were its
  round-C intended scores, not R1's actual ones; net change is 0 for both, and `summary.md`'s
  aggregation is unaffected.
- **Format slips.** Two round-C verdicts used a retired "partial" value; K3's and C4's posts ran
  over the length limit.
- **Few self-checks:** 3 in R1, 2 in debate, 0 in overtime, 1 in R3.
- **Limited fact-check coverage:** 14 claims in ②, 11 claims and 20 experience arguments in ③;
  the rest were not independently checked.
- **Table sides did not always match posts.** At X4, M2 and M3 were seated "bet heavily" but
  posted closer to the middle.
- **`overall` reflects one early-career researcher's weighting**, and originally also a
  career-capital dimension removed for privacy; not a second field-level ranking.
- **Interest lines are dated 2026-10-28**; some roles have changed since (`card.yaml` has current
  facts).
