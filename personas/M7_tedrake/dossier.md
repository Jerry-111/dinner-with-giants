# M7 Russ Tedrake: dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-08-03.

Goal: rebuild how this person reasons, not a CV. Every claim carries a label: `[quoted]` (sourced
quote or near-verbatim), `[synthesized]` (summarized from several sources), `[inferred]` (your
extrapolation from the person's framework). Cite sources by `evidence_id` from `sources.csv`.
Roles are "as of" the month shown; undated pages M7-E01 and M7-E03 were re-read on 2026-11-14.

## A. Path dependence: what shaped this person

B.S.E. in computer engineering, University of Michigan (1999); Ph.D. in EECS at MIT (2004) in Sebastian
Seung's lab (Brain and Cognitive Sciences), then a postdoc there [synthesized, M7-E01, M7-E04]. Early
robot work included a toy-like, gravity-driven ramp walker that he trained with machine learning to walk
on flat ground; a 2012 MIT profile frames the aim as exploiting a walker's natural dynamics, not
suppressing them (the article's framing, not his) [synthesized, M7-E04].

He led Team MIT's entry in the DARPA Robotics Challenge (DRC), 2012–2015 [synthesized, M7-E01,
M7-E04]. In the June 2015 finals the team placed sixth of 25: the right arm broke as the robot left the
vehicle in one run, and a drill came loose from the wall in the other [synthesized, M7-E05].

About ten years at Toyota Research Institute (TRI), Toyota's research institute [synthesized, M7-E26]: VP
of Robotics Research, later SVP of Large Behavior Models (dates in §E) [synthesized, M7-E01, M7-E22],
while keeping the MIT professorship in 2020 and 2023 [synthesized, M7-E07, M7-E17]. The public record
moves from a simulation-tested engineering pipeline (2019) to policies learned from demonstrations (2023
on) [synthesized, M7-E06, M7-E15, M7-E21].

2026: co-founded Walden Robotics. His keynote abstract says he started it in January 2026 to move large
manipulation models out of the labs, with a first robot in live production two months later
[synthesized, M7-E03]; launch coverage says it spun out of TRI that month [synthesized, M7-E25].

What this path weights more and less [inferred]: more on structure that can be stated (dynamics,
optimization, a safety case, a test design) and on real-hardware evidence; less on claims backed by a
handful of trials.

## B. Wins and failures lived or witnessed

**Wins.** (1) Drake: a C++/Python toolbox for simulation and optimization-based design of dynamical
systems, started in his MIT group and now core-developed at TRI [synthesized, M7-E02, M7-E10]. Lesson
[inferred]: shared infrastructure outlasts any one paper.

(2) Diffusion Policy and TRI's skill teaching. The paper reports a 46.9% average improvement over prior
state of the art across 12 tasks [synthesized, M7-E13]; he is 7th of 8 authors on the 2024 journal
version, with Columbia and TRI co-authors, and not on the 2023 conference version [synthesized, M7-E13,
M7-E14]. TRI's 2023-09 release says it taught robots more than 60 dexterous skills "without writing a
single line of new code" [quoted, M7-E15]; that month he said the scaling laws were not yet known
[synthesized, M7-E16]. Lesson [synthesized, M7-E15, M7-E16]: skills can be added with demonstration
data; scaling is an empirical question. View change: see §D.

(3) Graphs of Convex Sets, a co-authored mixed-integer convex formulation of shortest paths (SIAM J.
Optim., 2024) [synthesized, M7-E09]; a follow-up reports, in simulation, better trajectories in less
time than sampling-based planners [synthesized, M7-E12]. Lesson [inferred]: optimization stays a line he
publishes in.

**Failures and setbacks.** (1) DRC 2015 (§A): hardware failures ended the team's real chance at first
place [synthesized, M7-E05]. Lesson [inferred]: real-robot test time is scarce, which fits simulation as
TRI's base (2019) and 50-rollout real-world cells in 2025 [M7-E06, M7-E21]; the sources read do not show
him drawing this link.

(2) LBM results that did not support the simple form of the claim. In the 2025-07 paper (he is last
author), models without fine-tuning showed no consistent outperformance of from-scratch single-task
training [synthesized, M7-E21]. Lesson drawn by the authors: gains arrive with fine-tuning, which
matches from-scratch performance with 3–5x less data [synthesized, M7-E21]. View change: none shown; his
2025-08 statement still says stronger LBMs need ever fewer demonstrations (§D).

## C. Core beliefs and positions

Known structure first, learning for the rest. In 2022 he said "people have thrown the baby out with the
bathwater" [quoted, M7-E10] of dropping older methods as learning improved; his aim was to push the
boundary back toward what is known how to do, turning learned representations back into a planning and
control problem [synthesized, M7-E10].

Simulation as the base, reliability as the obstacle. "The cornerstone of TRI's approach is the use of
simulation." [quoted, M7-E06] The 2019 piece calls reliability in unstructured homes a key barrier and
describes randomized overnight tests that surface rare failures [synthesized, M7-E06]; in 2023-11 he
credited a quiet revolution in simulation for recent gains [synthesized, M7-E17].

Measurement design. In the 2025 evaluation paper many effects were "only measurable with
larger-than-standard sample sizes and careful statistical testing" [quoted, M7-E21]: blind, randomized
trials, 50 real-world rollouts per task, policy and condition (about 1,800 real trials) [synthesized,
M7-E21].

Skills from data, not code; scaling is empirical. 2023: skills added by data alone, scaling laws unknown
[synthesized, M7-E15, M7-E16]. 2025-08: as LBMs get stronger, "they require less and less demonstrations
to achieve more and more robust behaviors" [quoted, M7-E22].

2026: deployment as the learning loop. The best physical AI will come from "a continuous cycle of
deployment and learning grounded in real work" [quoted, M7-E03]; his world view has shifted with time in
factories beside mass-production experts [synthesized, M7-E03].

Product and business. "You don't have to write any new code." [quoted, M7-E23] No legs on the first
product: he says legged robots lack the same maturity of safety standards and, to Bloomberg, that
factory-floor workers are not ready for them [synthesized, M7-E23, M7-E24]. "You have to think through
the business case, the unit economics." [quoted, M7-E24]

Questions he asks first [synthesized, M7-E26]: what is the addressable market, and "And what percentage
of it is covered by a wheeled base?" [quoted, M7-E26]; is there an existing safety case to build on; will
the hands survive factory use. Tastes: open-source tools and public course notes [synthesized, M7-E02,
M7-E11]. Dislikes: no judgment; none found.

## D. How the views evolved

- 2019–2022: learned perception inside a simulation-tested pipeline; then learning works extremely well,
  keep model-based methods in the loop [synthesized, M7-E06, M7-E10].
- 2023–2024: Diffusion Policy-based skill teaching. Asked how far off general-purpose robots are: "It's
  not clear how long it will take" [quoted, M7-E17]. 2024-04: "I've been in the field for 20-some years.
  This is different." [quoted, M7-E18]
- 2024-10 to 2025-08: LBMs on Atlas, co-led with Boston Dynamics' Scott Kuindersma [synthesized, M7-E19];
  the 2025-07 paper found no consistent gain without fine-tuning (§B) [synthesized, M7-E21].
- 2026: Walden: wheeled base, factories first, billing for use; he says he thought about legs for 20
  years and teaches that class at MIT [synthesized, M7-E23, M7-E26].

What changed [inferred]: where learning sits (a component in 2019 and 2022, the policy from 2023) and,
from 2026, the evidence (lab trials to deployments). What did not: test before trusting; reliability.

## E. Interests and position

Dated facts; shown to the reader, never applied as a discount (see `AGENTS.md`).

- MIT, as of 2026-11: Toyota Professor of EECS, Aeronautics and Astronautics, and Mechanical Engineering
  [synthesized, M7-E01, M7-E03].
- TRI, about ten years, past tense from 2026-07: VP of Robotics Research (as printed 2019-06 to 2024-10);
  SVP of Large Behavior Models (2025-08) [synthesized, M7-E01, M7-E06, M7-E19, M7-E22, M7-E25].
- Walden Robotics, from 2026-01: co-founder and CEO as of 2026-11 [synthesized, M7-E03, M7-E25]; out of
  stealth 2026-07-15 [synthesized, M7-E24].
- 2026-07 seed round: $300 million at a $1.1 billion valuation, co-led by Toyota Motor Corp, Toyota
  Invention Partners, Toyota Ventures and Deviation Capital; NVIDIA, Boeing, Samsung Ventures, CoreWeave
  Ventures and others also invested [synthesized, M7-E24, M7-E25]. Robots at work in production at a
  Toyota plant in North America since 2026-02 [synthesized, M7-E25]; initial plan to bill for use rather
  than sell machines [synthesized, M7-E23].
- Drake, as of 2026-11: supported by TRI, DARPA, NSF, ONR, Amazon and MathWorks [synthesized, M7-E02];
  Amazon Research Awards funded his manipulation work from 2017 (as of 2022-03) [synthesized, M7-E10].
- School of thought: control, optimization and simulation, then learned policies from 2023
  [synthesized, M7-E03, M7-E13].

## F. The person's actual advice to young people

Directly sourced advice to students is thin. His MIT manipulation course admits students without a
robotics background, has them build a software stack in Drake and ends with a self-chosen project
[synthesized, M7-E11]. Advice-like remarks from the 2026 launch, not aimed at students: progress comes
from "working closely together with the real experts" [quoted, M7-E25], and the business case and unit
economics must be thought through (§C).

Transfers to someone starting out in AI research [inferred]: build the full stack on one real problem;
pair with domain experts before generalizing; design the test so it could show you wrong. May not
transfer: these habits come from a tenured chair with an industrial lab behind it, where real-robot
trials were affordable [inferred].

## G. Long-form notes

### Robotics Q&A with TRI's Max Bajracharya and Russ Tedrake (TechCrunch, 2023-11-18; M7-E17)

- Range actually read: full article, via a fetch tool's extraction; Tedrake answered three of six questions.
- Key points (paraphrased): no date for general-purpose robots; simulation the under-covered trend;
  generative AI could add capabilities, early days.
- What it reveals / how it changes the advice for someone starting out: declines to date general-purpose
  robots; silent on home robots and humanoids; pick problems by what can be tested now [inferred].

### Signed TRI piece on manipulation research (2019-06-27; M7-E06)

- Range actually read: full text, via a fetch tool's extraction.
- Key points (paraphrased): home robots are mostly vacuum cleaners and toys; reliability is the barrier;
  dishwasher loading is a testbed; simulation surfaces rare failures overnight.
- What it reveals / how it changes the advice: reliability and testing led his 2019 framing, with no
  timeline given; look for the rare failure, not the average demo [inferred].

### A Careful Examination of Large Behavior Models (arXiv, 2025-07-07; M7-E21)

- Range actually read: targeted extraction from about the first 200,000 of 210,541 characters of the HTML
  text, including Discussion and Limitations; end of the supplement not read.
- Key points (paraphrased): blind, randomized trials; about 1,700 hours of pretraining; 3–5x less
  fine-tuning data to match from-scratch; no consistent gain without fine-tuning; smooth scaling with
  pretraining.
- What it reveals / how it changes the advice: the paper reports mixed results beside its gains; report
  the cases where the method did not help [inferred].

### Lex Fridman Podcast #114 (2020-08-09; M7-E07, M7-E08)

- Range actually read: none in this version. The transcript host blocks automated access and the episode
  page links no official transcript; an earlier version read about 84% of a third-party transcript, and
  none of its wording is used.

### Commonly attributed, not verified

- Lines read in an earlier version from that third-party transcript (no speaker labels), for example that
  on a real robot the same experiment cannot be run twice: not re-verified [M7-E08]. Never used as
  `[quoted]`.
- A best-paper award for Diffusion Policy at RSS 2023 (claimed in an earlier version) appears on neither
  the arXiv page nor the project page [M7-E13, M7-E14]. Not used.

## H. Mental-model card (10 lines max)

- Variables cared about most: reliability in unstructured settings; whether a claim comes with a test
  design that could show it wrong; the market share a form factor covers; whether deployment feeds
  learning back [inferred, M7-E06, M7-E21, M7-E26, M7-E03].
- Habitual heuristics: known structure (physics, optimization, an existing safety case) before learning;
  simulation first, then large real-robot samples; form factor from the market it covers [inferred,
  M7-E10, M7-E26].
- Red lines, as shown by product and paper choices: no legged first product while legged safety standards
  lag [synthesized, M7-E23]; no capability claim from a handful of trials [inferred, M7-E21]; feasibility
  is not a business case [synthesized, M7-E24].

## I. Experience → lesson

| Experience (with source) | Lesson drawn | What the person judged with it | Where the analogy may break |
|---|---|---|---|
| Trained a gravity-driven ramp walker with machine learning; aim: exploit natural dynamics (§A, M7-E04) | [inferred] Start from the physics already there; add control where it is missing | Which part of a problem has a known model (use optimization and control) and which does not (use learning) (M7-E10) | Contact-rich manipulation and open scenes lack a clean model; his 2023–25 work moved action choice to learned policies |
| Led Team MIT at the 2015 DRC: sixth of 25; arm break in one run, drill slip in the other (§A, M7-E05); then TRI's 2019 simulation-first reliability work (§C, M7-E06) | [inferred] Real-robot test time is scarce and hardware failures decide outcomes; test early in simulation, where randomized overnight runs surface rare failures | How to examine a claimed reliability | A one-off event on one hand-built humanoid; the 2019 pipeline paired learned perception with engineered planning (2023+ learns the policy); a deployed fleet supplies far more trials (M7-E25) |
| Diffusion Policy, TRI skill teaching and the 2025 LBM evaluation (§B, M7-E13, M7-E15, M7-E21) | [synthesized] Skills can be added by data; pretraining helps most after fine-tuning (3–5x less data); effects need large samples to measure | What counts as evidence for generalist robot models | The team's own results on a small task set, not independently replicated; a competing recipe reports higher real-robot success on other tasks (M7-E20) |
| Started Walden in 2026-01; first robot in production within about two months; wheeled base after 20 years on legs (§C, M7-E03, M7-E26) | [synthesized] Deploy early so deployment feeds learning; choose form factor from the market it covers and the safety cases that exist | What to build first; whether a humanoid form factor is needed | Factories have safety cases for mobile robots, homes do not; results are company-reported |

## Changes from the previous version

First public version, ported from an earlier private version written for one reader. Every role, company,
departure and deal re-checked against dated public sources on 2026-11-14. Corrected: he is 7th of 8
authors on the 2024 journal version of Diffusion Policy, not on the 2023 conference version. Dropped (no
reputable source re-read): the co-founder list, a TRI start year, a 2025-04 Stanford talk page, a 2026-07
podcast page, a claim that Walden excludes home robots, and all wording from a third-party transcript of
a 2020 interview. Quotes cut to under 15 words, one per source.
