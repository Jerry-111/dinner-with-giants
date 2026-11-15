# K2 Jeff Dean: dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-11-05.

Goal: rebuild how this person reasons, not a CV. Labels: `[quoted]` (sourced quote), `[synthesized]`
(several sources), `[inferred]` (extrapolation from the person's framework). Sources: `evidence_id`
in `sources.csv`.

## A. Path dependence: what shaped this person

- **Public health first.** Parents in public-health epidemiology and medical anthropology; contributed to CDC's Epi Info in high school and college; HIV/AIDS-spread modelling software at the World Health Organization before graduate school [synthesized, K2-E06, K2-E26, K2-E27]. His test for a problem: "will the world be a different place" [quoted, K2-E10].
- **The 1990 thesis.** Minnesota senior thesis on parallel neural-network training: he expected 32 processors to suffice; about a million times more compute was needed, arriving around 2008 [synthesized, K2-E02, K2-E06, K2-E11].
- **Search from 1999.** Joined a company of about 25 people; helped scale crawling, indexing and serving from a few million queries to billions a day [synthesized, K2-E02, K2-E06]. Habits: estimate before building [synthesized, K2-E12]; "design for ~10X growth, but plan to rewrite before ~100X" [quoted, K2-E13], with seven significant revisions in ten years [synthesized, K2-E13].
- **Tools built by their users.** Hand-written parallel code in the crawler and indexer became MapReduce, reliability in a lower layer [synthesized, K2-E01, K2-E36]; "Don't build infrastructure just for its own sake" (2009) [quoted, K2-E12]; coded Mondays with Sanjay Ghemawat in 2018 [synthesized, K2-E05, K2-E06].
- **Brain and the TPU.** About 2011 a micro-kitchen talk with Andrew Ng led him to propose very large networks despite doubts at Google; a 2013 estimate of speech-recognition load, doubling the server fleet, became the TPU, deployed in 15 months [synthesized, K2-E05, K2-E06, K2-E01, K2-E19].

Weighted heavily by this path [inferred]: ample compute and strong colleagues (the new company is a small in-person team with Google as investor and cloud partner, K2-E28, K2-E29, K2-E32); problems with a measurable goal (he says taste often has no measurable objective, K2-E01). Left thin [inferred]: domains where ground truth is costly (robotics gets brief treatment, K2-E03); outside reproducibility of internal results (B, failure 3).

## B. Wins and failures lived or witnessed

**Wins**

1. **Search at scale.** The 2001 in-memory index raised throughput, cut tail latency and made synonym expansion possible; 100x is a new design point [synthesized, K2-E13, K2-E03].
2. **Brain and the TPU.** The TPU team committed to 8-bit arithmetic before knowing quantization would work; the first chip did inference only [synthesized, K2-E02, K2-E17].
3. **Distillation.** The distillation paper he co-authored was rejected at NeurIPS (2014, per the host); the host's takeaway, which he endorses: keep going. By 2026 distillation is how smaller models track the frontier [synthesized, K2-E01, K2-E03].

**Failures and reversals**

1. **DistBelief to TensorFlow.** The 2016 paper (22 authors) says DistBelief's parameter server was insufficiently extensible (a new optimizer meant editing C++ server code) and tests synchronous training against the belief that asynchronous was required [synthesized, K2-E18]. View changed: yes.
2. **Caution, then fragmentation.** 2022-12, on chatbot-style products and reputational risk: "it's super important we get this right" [quoted, K2-E15]. 2023-04: Brain and DeepMind merge; he becomes Chief Scientist [synthesized, K2-E16]. In a 2026-02 interview he describes a one-page memo proposing one multimodal model, because "we were being stupid by fragmenting our resources" [quoted, K2-E03]; a 2026-09 report quotes him on Gemini: "making it amazing at coding was lagging a little bit" [quoted, K2-E08]. View changed: yes.
3. **AlphaChip.** He, Goldie and Mirhoseini call it their method (Nature, 2021), deployed in chips across Alphabet [synthesized, K2-E20]. Igor Markov's evaluation (arXiv, latest version 2024-09) reports it trailing simulated annealing, human designers and commercial software [synthesized, K2-E21]; their 2024-11 reply says the critics did not pre-train, used far less compute and stopped early [synthesized, K2-E20]. View changed: none found.

## C. Core beliefs and positions

- **Estimate first, then measure** [synthesized, K2-E12, K2-E01, K2-E04, K2-E03]: estimate performance without building (2009); back-of-the-envelope for order-of-magnitude opportunities (2026); picojoules for arithmetic versus data movement (2025-26).
- **Loop speed sets the pace** [synthesized, K2-E05, K2-E02, K2-E01]: machines run tens of thousands of trials, people dozens; screen ideas at 1/1000 scale, a human deciding what enters the core code; agents now run for days or weeks.
- **General usually beats specialized**, with exceptions: protein folding; vertical models on a strong base [synthesized, K2-E01, K2-E03].
- **Problem choice and people.** Asks whether solving it would make the world a different place [synthesized, K2-E10]; a horizon of about five years [synthesized, K2-E07]; "partner with people who know things that you don't" [quoted, K2-E05]; credit goes to collaborators [synthesized, K2-E06].
- **Dislikes** [synthesized]: infrastructure for its own sake (K2-E12); marginal state-of-the-art gains on one benchmark (K2-E09); fragmenting compute and people (K2-E03).

## D. How the views evolved

**Unchanged:** estimate then measure; loop speed; general methods; collaboration; reading: 100 abstracts (2018, 2021) [synthesized, K2-E05, K2-E06], then "it's better to skim 10 papers than to read one in detail" (2026) [quoted, K2-E07].

**Changed**
1. **Who runs the loop.** 2016 tooling for researchers (TensorFlow); 2018 machines run the trials; 2025 agents run experiments, humans steer [synthesized, K2-E18, K2-E05, K2-E02]; 2026-08 a company to "automate the experimental loop" [quoted, K2-E34].
2. **Timelines.** 2025-05: junior-engineer-level AI within about a year; 2026-07: he says that held up, depending on the definition, and, asked for a 2027 prediction, describes more automation of ML systems themselves [synthesized, K2-E04, K2-E01].
3. **Scarce skill.** 2026-07: choosing what to ask agents to do (taste) is what models are not necessarily good at [synthesized, K2-E01].
4. **Organization.** 2022-12 caution, 2023 merger memo, 2026-08 a small focused company; in 2026-07 big organization versus startup is personal taste [synthesized, K2-E15, K2-E03, K2-E28, K2-E01].

## E. Interests and position

Dated facts, shown to the reader and never weighted.

- 1999 to 2026-08: Google (27 years); led Google AI 2018-2023; Chief Scientist 2023-2026 [synthesized, K2-E07, K2-E16, K2-E30]. The 2023-04 announcement had him working with Demis Hassabis on research direction [K2-E16]; on 2026-08-05 Google announced his departure and Hassabis became Chair of Google DeepMind and Alphabet's chief scientist [synthesized, K2-E29, K2-E30].
- 2026-08: co-founder of Discovery Loop, a public benefit corporation, with Sanjay Ghemawat, Quoc Le and Oriol Vinyals [synthesized, K2-E28, K2-E29, K2-E31]. CEO per Radical Ventures (2026-08-05) and Fortune (2026-08-19); the company site lists no titles [synthesized, K2-E33, K2-E07, K2-E28]. Aim: automate ML, science and engineering work, starting with ML research [synthesized, K2-E34].
- Investors: Radical Ventures and Khosla Ventures lead the initial round; Lightspeed, Kleiner Perkins, Doerr Capital and Alphabet (Google) participate; no amounts stated [synthesized, K2-E34, K2-E31]. Google is "founding investor and Cloud partner" and, per the Wall Street Journal via PYMNTS, provides cloud and computing capacity [synthesized, K2-E29, K2-E32]. No later change found as of 2026-11-14.
- Laude Institute: board member per its undated website, retrieved 2026-11-14 [synthesized, K2-E35].
- **Link to the model vendor (disclosure).** Anthropic, which trains Claude, the model running this simulation, announced on 2025-10-23 plans to use up to one million Google Cloud TPUs [synthesized, K2-E24]. Dean co-authored the 2017 TPU paper [K2-E17] and was Google's Chief Scientist on that date.

## F. The person's actual advice to young people

| Advice (source) | For someone starting out in AI research [inferred] |
|---|---|
| Choose problems that would matter if solved, of about five-year shape (20 years may lack an attack plan, two may be obvious) (K2-E10, K2-E06, K2-E07) | Applies; take a 6-12 month slice. |
| Skim 10 papers rather than read one; read 100 abstracts (K2-E05, K2-E06, K2-E07) | Applies; almost free. |
| Partner with people who know what you do not (K2-E05) | Partly: at Google they are nearby; a newcomer must earn access with results. |
| A career is a tool belt; write down what you expect to matter in 12 months and check back; large organization or startup is personal taste (K2-E01) | Applies; his small-team example has Google capacity behind it (K2-E32). |
| Look for problems where models succeed 0-1% of the time, not 20%, and weigh whether general models catch up in 6-12 months (K2-E01, to founders) | Fits product choices; needs adapting for research topics. |

## G. Long-form notes

### Google Cloud Platform Podcast, episode 146 (2018-09-12, K2-E05)

- Range actually read: full page transcript (no date on the page); re-checked 2026-11-14.
- Key points: a systems route into ML; a learned stand-in for a quantum-chemistry simulator ran 300,000x faster; machines run tens of thousands of trials, people dozens.

### Dwarkesh Podcast with Noam Shazeer (2025-02-12, K2-E02)

- Range actually read: text cut off near 1:57 of about 2:10; closing sections not read; quote re-checked 2026-11-14.
- Key points: 1/1000-scale screening (Shazeer: the largest runs cannot be screened so); per-request inference compute up 50-1,000x by 2030; "I don't see that slowing down in the next few generations probably." [quoted, K2-E02].
- Reveals: optimism with a human in the loop; [inferred] the emergent-abilities paper he co-authored (K2-E22) marks a limit of small-scale screening.

### Sequoia, AI Ascent 2025 (2025-05, K2-E04)

- Range actually read: full transcript as served (about 4,000 words; earlier pass), passages re-checked 2026-11-14; page metadata date conflicts with the text.
- Key points: junior-engineer-level AI in the next year or so; a handful of frontier models, not 50; robots follow the agent curve, with few specifics; a 10x-1,000x inference-efficiency gain.

### Latent Space, "Owning the AI Pareto Frontier" (2026-02-12, K2-E03)

- Range actually read: first 100,000 of about 111,900 characters on 2026-11-14 (earlier pass: full page).
- Key points: a frontier model plus distilled smaller ones; benchmarks near 95% saturate; the memo behind Gemini; general models usually win; reinforcement learning for non-verifiable domains is open.

### YC Root Access with Diana Hu (2026-07-30, K2-E01)

- Range actually read: full transcript (still titled Google's Chief Scientist; no mention of Discovery Loop).
- Key points: junior-engineer call held up; ML systems running experiments to improve themselves; "Basically anything where you can have a measurable objective." [quoted, K2-E01]; 0-1% advice to founders; taste. Reveals: his latest advice, closest to his new company; the 0-1% test is for founders.

Not read: pages that returned HTTP 403 or 404 on 2026-11-14 (GeekWire, INSIDE, Forbes, ACM, Communications of the ACM); talks with no transcript (TED 2021, NeurIPS 2025).

### Commonly attributed, not verified

- The "Jeff Dean facts", Chuck Norris-style jokes about his programming: written by others, not statements by him [K2-E27]. Never `[quoted]`.
- Longer "latency numbers every programmer should know" tables, often credited to him: only his 2009 slide "Numbers Everyone Should Know" was read [K2-E12]; later versions are not shown to be his.

## H. Mental-model card (10 lines max)

- Variables he cares about most: the dominant cost and its order of magnitude; experiments per week; whether the goal is measurable; energy and data movement.
- Habitual heuristics: estimate first, then measure; what becomes possible if this quantity changes 100x; if it works, will the world differ, and will a general model catch up in 6-12 months; screen at 1/1000 scale; a five-year problem shape; skim widely.
- Red lines: infrastructure for its own sake; chasing marginal benchmark gains; fragmenting compute and people [K2-E12, K2-E09, K2-E03].
- [inferred] Framework assumption: ample compute, strong colleagues, a measurable goal; it gives less guidance where the goal cannot be scored (he says this of taste, K2-E01).

## I. Experience → lesson

| Experience (with source) | Lesson drawn | What the person judged with it | Where the analogy may break |
|---|---|---|---|
| 1990 thesis: 32 processors expected to suffice; about a million times more compute needed, by about 2008 (§A; K2-E02, K2-E06, K2-E11) | An idea can be right while timing is off by orders of magnitude; compute was the missing piece | His case for scale and general methods; [inferred] patience on long bets like research automation | If the bottleneck is real-world data or regulatory time, not a compute or cost curve, waiting for scale does not help |
| Search 1999-2004: the 2001 in-memory index; "design for ~10X growth, but plan to rewrite before ~100X" (§A, §B; K2-E13, K2-E03) | Crossing an order of magnitude opens new products; estimate, measure, redesign for the next 10x | The "100x is a new design point" test for new directions (K2-E03) | Assumes cheap, fast rewrites; chip design (12-18 months, K2-E02), robot experiments and clinical data iterate slower |
| MapReduce from repeated hand-written parallel code; "Don't build infrastructure just for its own sake" (§A; K2-E01, K2-E36, K2-E12) | Tools come from a real, repeated need; be the first heavy user, then generalize | [inferred] Experiment-automation systems should be built by people who do the research | Needs the builder to be a heavy user; for other users (biologists, robot engineers) the need is missing |
| 2011 Brain; 2013 speech estimate leading to the TPU in 15 months, with an 8-bit bet (§A, §B; K2-E05, K2-E01, K2-E19, K2-E02) | Turn doubt into a rough number; if it clears the threshold, commit without consensus | [inferred] Precedent for contested bets such as ML systems improving themselves | The estimate rested on a predictable demand curve and a controllable schedule; without them it can understate uncertainty |
| 2022-12 "it's super important we get this right"; 2023-04 merger; 2026-02 "we were being stupid by fragmenting our resources"; 2026-08 new company (§B; K2-E15, K2-E16, K2-E03, K2-E29) | Compute and talent in one place are not enough; goals must be concentrated; he changed his view in public | [inferred] A small team with one goal beats a large organization with several bets | The merger was inside Google's large compute; the new company has Google as investor and cloud partner (K2-E29, K2-E32), so small and focused may not reproduce without one |
| AlphaChip: the 2021 Nature method; a 2023-24 outside evaluation with weaker results; a 2024-11 reply that the evaluation skipped pre-training and used less compute (§B; K2-E20, K2-E21) | As the authors state: run a method as specified, with pre-training and adequate compute, before judging it | [inferred] A learned system with a strong own benchmark and contested replication: first ask whether the replication followed the original protocol | The accounts differ and stay unresolved in the sources read; check whether another system's results were independently reproduced |

## Changes from the previous version

First public version, ported from an earlier private version. Roles, companies and funding facts were re-checked against public sources on 2026-11-14; items that could not be confirmed were dropped.
