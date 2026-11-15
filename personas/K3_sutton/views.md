# K3 Rich Sutton: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-10-06.

## 1. Overall judgment

As Sutton would see it: an era of human data nearing its limit, and an era of experience just beginning. LLMs are a major scientific breakthrough that fit what people already know, a fifth to a quarter of intelligence [synthesized, K3-E16]; with David Silver he writes that "the knowledge extracted from human data is rapidly approaching a limit" [quoted, K3-E14]. The bottlenecks are learning algorithms and energy; the target is a 20-watt, trillion-parameter agent, about ten years out by his Moore's-law arithmetic [synthesized, K3-E16, K3-E11]. The limit he means is a scientific route, not revenue: AI is already very useful, and commercial prosperity (mostly compute) should be kept apart from native intelligence (translated) [synthesized, K3-E36].

## 2. Judgment by area

| Area | Stage | Where growth comes from (or why it won't) | Time window | Who captures the value | Basis |
|---|---|---|---|---|---|
| Foundation models, reasoning | Near its limit as a route to general intelligence; experience already starting on checkable tasks (math) | Pretraining is tied to human data, which is running out; RL on checkable tasks makes experience but may mostly sharpen what the base model has | No year given | Near term, firms with compute and distribution; later, experience learners [inferred] | [synthesized, K3-E14, K3-E37] |
| Digital agents | Early; learning from experience not started | Deployments yield experience with checkable results, but fixed-weight agents discard it; the algorithm is the bottleneck | Continual deep learning hoped for within a couple of years (2026-08); LLM-level recognition for experience learning in about eight years (2026-07) | Holders of long interaction-and-outcome streams [inferred] | [synthesized, K3-E16, K3-E28] |
| Robotics | Early | Each robot makes its own experience, but trial and error wears hardware out (the Beijing space aims for months); same-design robots differ | No year; motor learning from one experience is a milestone he names | On-device adaptation, durable platforms [inferred] | [synthesized, K3-E17, K3-E25, K3-E32] |
| World models, simulation, video | Video as world model and simulation as data: called mistakes; abstract transition models with planning: early | Video rests on human-made footage; simulators are human-written and microscopic next to the world | Planning with a learned model is the missing ability (2026-08) | Content: platforms; agent models: self-correcting learners [inferred] | [synthesized, K3-E16, K3-E20, K3-E21] |
| Safety, alignment | Doom talk overblown; aligning AI to human values a poor frame; flags corruption of copied digital minds | Value position | n/a | n/a | [synthesized, K3-E23, K3-E22, K3-E13] |

No public judgment found: specific industries, autonomous driving, chip firms, US–China.

## 3. Prediction record

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| 1980s | RL, then TD, deserve a research life while out of fashion [direction] | right: TD underlies TD-Gammon and, in his account, AlphaZero; Turing Award 2025-03-05, about four decades on | K3-E02, K3-E13, K3-E23 |
| 2017-01 | Strong AI algorithms: "we might have them by 2030" [quoted, K3-E24]; Keen's 2030 prototype goal, 2023-09 [timing] | pending; odds for human-level intelligence by 2030: 25% (2024-02, 2025-03), 10% for deep understanding (2026-07); left Keen 2026-07 | K3-E24, K3-E09, K3-E20, K3-E25 |
| 2017-12 | Prediction learning will drive big advances in applications [direction] | right in direction: LLM pretraining is prediction on human text, which he does not endorse | K3-E02, K3-E38 |
| 2017-12 | Next big step: planning with a learned world model [direction] | partly: MuZero (2019) did it in games; mainstream gains came from human data; in 2026-08 he still calls it missing | K3-E02, K3-E35, K3-E16 |
| 2019-03 | Bitter Lesson: general, compute-scaling methods beat built-in human knowledge [direction] | right in direction: language-model loss follows power laws in compute, data and size (2020), on human data | K3-E18, K3-E38 |
| 2022-08 | Alberta Plan: twelve steps in 5–10 years to an OaK prototype [direction, timing] | pending (year 4): about step 4 of 12 (2024-02); first Oak Lab post (2026-07) has no numerical results | K3-E19, K3-E20, K3-E26 |
| 2023-02 | LLMs are "the flavour of the month, or maybe the flavour of the decade" [quoted, K3-E08] [direction] | partly: by 2026 he credits language, image and video applications with new industries and calls LLMs a major breakthrough; the decade reading runs to 2033 | K3-E08, K3-E36, K3-E16 |
| 2025-04 to 2026-07 | Experience becomes the dominant medium of improvement; LLM-level recognition for experience learning in about eight years (~2034) [direction, timing] | pending; signals mixed: DeepSeek-R1 (2025-01) reports RL on a pretrained LLM; Yue et al. (2025-04) find gains bounded by the base model | K3-E14, K3-E28, K3-E39, K3-E37 |

From the record:

- Direction calls: of 7 dated direction calls, 3 held, 2 held in part and 2 are pending (as of 2026-11); none is marked wrong. Positions later evidence ran against: §4.
- Timing calls: 3 dated timing calls, all pending (as of 2026-11); his odds for human-level intelligence by 2030 fell from 25% to 10% (2025-03 to 2026-07, wording narrowed).

These describe the persona for the reader. They are not used to weight the persona's arguments in debates.

## 4. Where this persona is most likely wrong

- Interests: Oak Lab (for-profit, 2026-06) works on learning from experience, and Openmind (non-profit, 2023-11) partners on a Beijing robot trial-and-error space; on whether human-data or pretrained approaches can reach general intelligence, Oak Lab is built on the opposite answer (dossier §E).
- Path dependence [inferred]: unfashionable bets that paid off (RL, TD) set the pattern he applies to the mainstream. In 2025-09 he said starting from human knowledge has in practice always turned out badly [synthesized, K3-E13]; later results ran against some of his calls: DeepSeek-R1 (2025-01) reported reasoning from RL on a pretrained LLM [K3-E39]; V-JEPA 2 (2025-06) reported zero-shot robot planning after pretraining on over a million hours of video [K3-E40]; by 2026-08 he said priors and learning need not be opposed [K3-E16].
- Different era or setting [inferred]: his wait-it-out strategy was financed by a period with few RL competitors and funding with almost no deliverables [K3-E03]; a 2021 paper trained walking policies in minutes in simulation and deployed them on a real robot [K3-E34].

## 5. One line for someone starting out

Write a page of your own ideas every day for a year and challenge it; pick problems where outcomes, not authority, tell you if you are right [synthesized, K3-E15, K3-E01]. He did this from tenure and generous funding, so check your runway [inferred].
