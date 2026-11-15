# M8 Jun Zhu (朱军): dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-10-08.

Goal: rebuild how this person reasons, not a CV. Every claim carries a label: `[quoted]` (sourced
quote or near-verbatim), `[synthesized]` (summarized from several sources), `[inferred]` (your
extrapolation from the person's framework). Cite sources by `evidence_id` from `sources.csv`.

## A. Path dependence: what shaped this person

Tsinghua is the constant: bachelor's (2005) and doctorate (2009) in computer science under Zhang Bo, an
academician; a Carnegie Mellon postdoc; back on the Tsinghua faculty in 2011 at Zhang Bo's invitation
[synthesized, M8-E01, M8-E02]. Titles accumulated there (§E). Two companies sit beside the posts: RealAI (2018, AI safety),
founded by his student Tian Tian with his backing, where he and Zhang Bo were chief scientists as of 2023-08
[M8-E01, M8-E14]; and Shengshu Technology (2023), where he is founder and chief scientist as of 2026-08
[M8-E04, M8-E07]. Neither has him as CEO: RealAI's is Tian Tian (2026-07, M8-E29), Shengshu's Luo Yihang
(2026-10, M8-E11).

The 2013 Bayesian bet. A junior-year internship at Microsoft Research Asia introduced him to probabilistic
graphical models [synthesized, M8-E15]. In 2013 his team began applying Bayesian methods, then regarded as
outdated and displaced by deep neural networks; the reporter writes that he judged them to hold untapped
potential, and he names Judea Pearl as a major inspiration [synthesized, M8-E14]. The team went on to Bayesian
deep learning [M8-E14] and regularized Bayesian inference, which adds posterior regularization so domain
knowledge can enter variational optimization, described as a third dimension of freedom for a framework over
260 years old [M8-E15]. He states the classical limit himself: "Many scenarios cannot become a prior or
likelihood; Bayesian theory then fails" [quoted, M8-E15] (translated).

The diffusion window, 2022–2023. Analytic-DPM (Zhu third of four authors, Zhang Bo fourth) was one of seven
ICLR 2022 Outstanding Papers [M8-E17]; DPM-Solver (NeurIPS 2022) samples diffusion models in 10–20 function
evaluations [M8-E18]. U-ViT, a simple ViT-based backbone for diffusion, was posted 2022-09-25 (CVPR 2023)
[M8-E19], about three months before DiT, another transformer-backbone model, posted 2022-12-19 [M8-E20];
UniDiffuser (2023-03) put several modalities in one diffusion framework [M8-E21].

Overrates and underrates [inferred]: a method regarded as outdated (Bayesian, 2013) that later won recognition
(M8-E14, M8-E17), followed by probabilistic-modeling skill paying off in the diffusion wave, supports a prior
that early work in a minority direction pays off, and a preference for unified frameworks (UniDiffuser, MoT,
Motus). Less weight goes to cases where data, not theory, is the bottleneck; he names the robot "data wall"
himself [M8-E05] and lists learning contact, friction and force among open challenges [M8-E07].

## B. Wins and failures lived or witnessed

**Wins.** (1) Analytic-DPM and DPM-Solver, 2022: an ICLR Outstanding Paper and a fast sampler [M8-E17,
M8-E18]. Lesson [inferred; none stated by him]: probabilistic modeling skills carried into a new architecture
wave without starting over. (2) Vidu: from U-ViT (2022-09, M8-E19) to a released model on 2024-04-27, about 19
months [M8-E12]. In 2026-02 the company reported that Vidu Q3 ranked first in China and second globally on the
Artificial Analysis leaderboard (company-supplied; category and scores not given) [M8-E10]. Lesson [inferred]:
a lab architecture can ship within two years.

**Failures and setbacks.** (1) About 2013 the Bayesian line was regarded as outdated next to deep neural
networks [M8-E14]; he kept it, merged it with deep learning [M8-E14], and later extended it to regularized
Bayes, answering the limit he states in M8-E15 (§A). (2) Vidu's launch, 2024-04: clips capped at 16 seconds
against up to a minute for Sora; Shengshu called Vidu very close to Sora, while The Decoder wrote "the
quality of Vidu seems to lag Sora" [quoted, M8-E13], a critic's words, and called the claimed edge with
Chinese elements unproven [M8-E13]. No response by him appears in the sources read. The company's later
announcement cites a leaderboard rank [M8-E10]; in 2025-03 he said users care most about quality and
efficiency [M8-E04].

## C. Core beliefs and positions

- Deep learning's limits, 2023: uninterpretable, easily misled by adversarial noise, with unpredictable
  safety risks; his team launched an AI security firewall and an AI safety platform [synthesized, M8-E16].
- A world model integrates understanding, prediction and action [synthesized, M8-E06]: "a closed-loop
  feedback system coupling the three abilities" [quoted, M8-E07] (translated). "Traditional VLA is mostly
  fitting trajectories" [quoted, M8-E06] (translated); generative pretraining lets robots plan from imagined
  futures [synthesized, M8-E06].
- Video as carrier: "Video naturally contains temporal information, spatial structure and physical
  interaction" [quoted, M8-E05] (translated); real robot trajectory data is costly and small [M8-E05].
- Research and translation: moving results into industry tests them and surfaces real needs for research
  [synthesized, M8-E16]: "These two sides promote each other" [quoted, M8-E16] (translated).
- Market views, 2025-03: "At this stage, investing in foundation models still yields the biggest returns"
  [quoted, M8-E04] (translated). Video commercializes faster than language models; leading video models have
  differentiated business paths, not a red-ocean state; a model that suddenly pulls far ahead is unlikely;
  Chinese video models lead in many respects [synthesized, M8-E04].
- Contested point. On 2026-07-20 he said video models already achieve understanding and imagination, two of the
  three world-model abilities [synthesized, M8-E06]. In an interview published 2026-06-18, BAAI's president
  Wang Zhongyuan said "Video generation does not equal a world model" [quoted, M8-E28] (translated), citing
  physical correctness, traceable action causality, long-sequence consistency and generalization; the article
  does not mention Zhu [synthesized, M8-E28]. His WRC roadmap lists learning real physical laws among six open
  challenges [synthesized, M8-E07].
- First questions [inferred]: does the model learn a distribution with uncertainty or a deterministic
  mapping (M8-E14, M8-E15); which of understanding, prediction and action does the work cover (M8-E07).
  Dislikes [inferred]: no treatment of uncertainty (M8-E15, M8-E16); imitation without imagined futures
  (M8-E06); work untested in practice (M8-E16).

## D. How the views evolved

[synthesized] 2013: the Bayesian line (M8-E14). 2018: RealAI, AI safety (M8-E01). 2022–2023: diffusion theory
and unified multimodal models (M8-E17–M8-E21). 2024-04: Vidu (M8-E12); 2025-03: controllability and
commercialization (M8-E04). 2024-10 to 2026-04: robot models from video and diffusion pretraining: RDT-1B,
Vidar, Motus (open-sourced 2025-12-16), Motubrain (arXiv 2026-04-30) (M8-E22–M8-E26). 2026: world-model talks
on 03-29, 07-20, 08-19 (M8-E05–M8-E07). Changed: 2023 reports foreground deep learning's limits and AI safety
(M8-E16); the 2026 talk reports read mention safety only as the WRC roadmap's sixth open challenge (M8-E07) and
a property of generated actions (M8-E06); video moved from product to data carrier for physical-world models.
Unchanged [inferred]: the vocabulary of unification and a closed loop; a diffusion-based toolbox.

## E. Interests and position

Dated facts, shown to the reader and never used to lower a persona's weight (see `AGENTS.md`).

- Professor of computer science at Tsinghua (Bosch AI Professor), 2024-07 [M8-E02]; vice dean of its Institute
  for AI, 2026-07 [M8-E06, M8-E05] (also 2025-03, M8-E04); IEEE Fellow, class of 2023 [M8-E03]; AAAI Fellow [M8-E02].
- Director, State Key Laboratory of Intelligent Technology and Systems, and BAAI chief scientist for machine
  learning, 2023-08 [M8-E01] (BAAI role also 2022-11 [M8-E03]); not re-confirmed from an official page.
- Founder and chief scientist of Shengshu Technology, 2026-08 [M8-E07]; founded 2023-03 [M8-E01]. Its products
  and models include Vidu (Q4 Preview, 2026-10-08, M8-E11) and the Motus and Motubrain robot models [M8-E24,
  M8-E26], the items the roadmap he presented on 2026-08-19 maps to levels L1–L3 [M8-E07].
- Series A+ over RMB 600 million (2026-02) [M8-E10]; Series B nearly RMB 2 billion, led by Alibaba Cloud,
  announced 2026-04-10 [M8-E08, M8-E09]. The announcements state no valuation; none is given here.
- RealAI chief scientist with Zhang Bo, 2023-08 [M8-E01]; a 2026-07 funding report quotes its CEO and does not
  mention Zhu [M8-E29].
- DPM-Solver, U-ViT, RDT-1B, Vidar and Motubrain (built on the UniDiffuser formulation) are diffusion-based
  [M8-E18, M8-E19, M8-E22, M8-E23, M8-E26]. On 2025-02-27 the OpenVLA-OFT authors reported beating RDT-1B, π0,
  Diffusion Policy and ACT on real bimanual tasks by up to 15 points [M8-E27]; no statement by him on this
  appears in the sources read.

## F. The person's actual advice to young people

No advice addressed to students appears in the sources read. Two sourced practices bear on it: as a
supervisor he gave students as much autonomy as possible, following Zhang Bo [synthesized, M8-E14]; and he
describes moving results into industry as a test of the results and a way to find real problems
[synthesized, M8-E16]. What transfers to someone starting out in AI research [inferred]: a base in
probabilistic modeling (uncertainty, evaluation under uncertainty) rather than one architecture; each theory
result paired with a real test. What does not: the nine years from the 2013 bet to the 2022 award were carried
from a professorship, a state key laboratory and doctoral students (M8-E01, M8-E14, M8-E17); without these
there is less room for a long wait, and shorter test cycles (replications, small projects) are the alternative.

## G. Long-form notes

### WAIC 2026 talk on general world models as new infrastructure (2026-07-20; M8-E06)
- Range actually read: speech text via a fetch tool (mostly a transcript; ending possibly abridged; charts
  unseen).
- Key points (paraphrased): a world model needs integrated understanding, prediction and action; specialized
  to general models with scaling laws; a mixture-of-transformers model with understanding, generation and
  action experts, called a world first; four shortcomings of streaming generation (real-time intervention,
  voice control, long-run stability, deployment cost).
- What it reveals / how it changes the advice: open items are listed beside results, but all figures (540P,
  up to 42 FPS) are speaker-supplied with no third-party benchmark; use the closed loop as a project
  checklist and treat figures as reported.

### WRC 2026 keynote, five-level roadmap (2026-08-19; M8-E07)
- Range actually read: a reprint marked by the publisher as advertising use; two quotes; page undated.
- Key points: L1 World Generation to L5 World Orchestrator; the company says it covers L1–L3; six open
  challenges for L4–L5 (joint evaluation, real physical laws, memory, online learning, deployment under
  latency limits, safety and controllability); no time estimate.
- What it reveals / how it changes the advice: it states what is unsolved, a ready list of open problems; its
  Motubrain figures (96.1 on RoboTwin 2.0; 50–100 demonstrations for a new body) match the arXiv abstract
  (95.8% clean, 96.1% randomized, in simulation) [M8-E26]; no independent replication read.

### Beijing News interview (2025-03-31; M8-E04)
- Range actually read: article text via a fetch tool.
- Key points: controllability next for video models; foundation-model investment pays most; faster
  commercialization; differentiated paths, not red ocean; Chinese models lead in many respects.
- What it reveals / how it changes the advice: his fullest market statement, a year before the 2026 talks,
  with no mention of robots, world models or AI safety; read it as dated 2025-03 views.

### Press profiles, 2022–2023 (M8-E14, M8-E15, M8-E16)
- Range actually read: three article texts via a fetch tool.
- Key points: the 2013 turn to Bayesian methods; regularized Bayes; deep learning's limits; research into
  industry.
- What it reveals / how it changes the advice: the source of his confidence in the long bet; no cost or
  timeline is given for 2013–2022, and the resources that carried it go unmentioned (§F).

### Commonly attributed, not verified
- The slogan about writing papers on the land of the motherland, as his own catchphrase: in the one source
  read it is the reporter's gloss on his view, not introduced as his words [M8-E16].
- A 2013 remark that Bayesian methods held untapped potential: the source gives it as the reporter's wording
  of his judgment, not his quotation [M8-E14].
None may be used as `[quoted]`.

## H. Mental-model card (10 lines max)

- Variables cared about most [inferred]: a distribution with uncertainty versus a deterministic mapping; one
  loop from understanding through prediction to action; whether a result survives a real test.
- Habitual heuristics [inferred]: restate a new method in probabilistic terms; unify modules rather than chain
  them; test in practice and feed real needs back (M8-E16).
- Red lines [inferred]: no uncertainty treatment (M8-E15, M8-E16); generation, prediction and action treated as
  separate problems (M8-E07); imitation without imagined futures (M8-E06).

## I. Experience → lesson

| Experience (with source) | Lesson drawn | What the person judged with it | Where the analogy may break |
|---|---|---|---|
| Turned to Bayesian methods in 2013 when seen as outdated; regularized Bayes; recognition by 2022 (§A, M8-E14, M8-E15, M8-E17) | [inferred] A method with sound theory can outlast a fashion cycle, given time and support | [inferred] Whether the video-to-world-model route is early, not wrong | No cost or timeline for the wait is given; a professorship, a state key laboratory and a doctoral pool carried it |
| U-ViT posted 2022-09-25, before DiT on 2022-12-19; Analytic-DPM award (§A, M8-E17, M8-E19, M8-E20) | [inferred] Probabilistic-modeling skill moves fast into a new architecture wave | [inferred] Which routes to bet on; at WAIC 2026 he called the MoT unified architecture a world first (M8-E06) | Priority for either claim is not settled in the sources read |
| RealAI (2018) and Shengshu (2023): CEOs other than him, he as chief scientist (§A, M8-E01, M8-E11, M8-E29) | [inferred] The lab supplies the science; a CEO runs the company | [inferred] How to commercialize lab results while staying in the lab | It rests on Tsinghua backing and investor access others may lack |
| Vidu's 2024-04 launch: 16-second clips, quality judged behind Sora (§B, M8-E12, M8-E13) | [inferred] Position claims are anchored to third-party rankings; later announcements cite one (M8-E10) | [inferred] Where Vidu stands against rivals | The page does not say how the rank is measured; a preference-based rank shows perceived quality, not physical correctness |
| Robot models built from video models: RDT-1B (2024-10), Vidar (2025-07), Motus (2025-12), Motubrain (2026-04) (§D, M8-E22–M8-E26) | [synthesized] Video can supply the data robots lack (M8-E05) | Whether video pretraining carries over to manipulation | Scores are team-reported simulation results; contact and force are on his own open list (M8-E07) |

## Changes from the previous version

First public version, ported from an earlier private version. Roles were re-checked against dated sources;
items without on-record or reputable confirmation are omitted.
