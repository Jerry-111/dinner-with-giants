# K5 Yann LeCun: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-10-10.

## 1. Overall judgment

This wave is self-supervised learning plus scale cashing out on text. As research, in his framing
LLMs have mostly run their course and become technology development rather than research
[synthesized, K5-E18]. Growth from here is in deployment — assistants, coding, search — but LLMs cannot reach human level
because they lack persistent memory, reasoning, planning and an understanding of the physical
world; the next driver is learning world models from video and sensors and planning against them,
replacing token-by-token generation [synthesized, K5-E19, K5-E35]. Economically, he treats this
wave as nothing qualitatively new: productivity gains take about 15 years, and there is no
imminent mass unemployment [synthesized, K5-E27]. So two curves: the LLM research curve near its
top with deployment still climbing; the physical-world-AI curve only just starting [inferred].

## 2. Judgment by area

| Area | Stage | Where growth comes from (or why it won't) | Time window | Who captures the value | Basis |
|---|---|---|---|---|---|
| Foundation models / reasoning / agents | Near its research peak; deployment (coding, office, assistants) still climbing | Text bandwidth is capped, token-search is inefficient; code/math gains ride language-as-reasoning at huge distribution; no world model caps reliability | "Obvious" by early 2027 (K5-E19) | Inference infra and distribution; the model layer commoditizes, especially on open weights | [synthesized, K5-E17, K5-E18, K5-E19, K5-E49] |
| Robotics and embodiment (incl. humanoid) | Early; today's humanoid wave overrated by his own logic | Won't scale by piling on teleoperation data and VLA; needs world-model sample efficiency for one model to serve many tasks | "Decade of robotics," 2025-35; general method ~1yr | The model supplier, not whoever has the hardware or demos | [synthesized, K5-E30, K5-E35; challenged by K5-E37] |
| Autonomous driving | L4 crawling by engineering; L5 early | Sensors plus engineering, hardest on the last percent; a teenager learns to drive in ~20h, no system does | No date given | Near term: engineering/ops firms; long term: world-model suppliers | [synthesized, K5-E28, K5-E30, K5-E50] |
| World models (representation-space planning) | Early; by his own account the least-peaked area | Video/sensor data dwarf text; learn from observation, plan at inference, transfer zero-shot (small scale: K5-E59 reaches 90% on a simulated task vs. 30% for a generative baseline); humans still far outscore the best such models on physical-reasoning benchmarks (K5-E62) | General method ~1yr (K5-E19); commercial use years off | New-paradigm builders; first into industrial control, robotics, medicine | [synthesized, K5-E19, K5-E40, K5-E59, K5-E62, K5-E63, K5-E64, K5-E67, K5-E68, K5-E69; his own line's planner-design study (K5-E66) and a self-critical admission that standard JEPA still has only limited planning ability (K5-E61)] |
| Generative video/3D, sim and synthetic data as a path to intelligence | Overrated | Generating pixels means predicting the unpredictable; sim mainly feeds sample-inefficient RL | — | Real market as content, not intelligence | [synthesized, K5-E02, K5-E25; challenged by K5-E38] |
| AI for Science (biology, materials, chemistry) | Early; bullish long term | Learned simulators replace costly numerical simulation; structure-prediction can move to property-driven design | Impact arrives over 5-30yr | Teams with an experimental loop, domain data, open publication | [synthesized, K5-E53, K5-E54; challenged by K5-E60] |
| Compute, chips and energy | Inference compute accelerating | Growth comes from daily inference, not training toward AGI; spend pays off regardless; new architectures reshape hardware | Now to 5yr+ | Chip/infra providers with distribution | [synthesized, K5-E06, K5-E55, K5-E56] |
| Safety, alignment and open vs. closed | Existential risk: overrated; openness: accelerating | Risk is misuse, not takeover; safety is goal-driven design plus guardrails; no one nation or lab monopolizes good ideas | — | Open ecosystem and app builders on open weights; the bigger risk is power concentrating in closed systems | [synthesized, K5-E27, K5-E71, K5-E72, K5-E57] |

## 3. Prediction record

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| 1988-2012 | Betting a career against consensus on neural nets and CNNs | right, but took about a decade to pay off | K5-E01, K5-E09 |
| 2016 | "Cake" analogy: self-supervised learning is the main substance of intelligence, reinforcement learning only the cherry on top | partly — self-supervised pretraining did become the industry's main substance, but mainly through the generative text LLMs he dislikes; the sharpest reasoning gains came from RL post-training, which the analogy minimized | K5-E10, K5-E09, K5-E15 |
| 2019-02 | Demand for specialized deep-learning hardware "will likely only increase" | right | K5-E55, K5-E56 |
| 2020-22 | GPT-3's capabilities are overhyped; even a far larger text-only model could never learn that objects on a pushed table move with it | mostly wrong — independently assessed as too dismissive, and multimodal models now handle such physical-common-sense cases, which he attributes to being specifically trained on them | K5-E09, K5-E22 |
| 2023-24 | Autoregressive LLMs "can't really reason, and can't plan" | mostly wrong for short-horizon tasks (IMO gold, 97.8% on Blocksworld) but still holds for long, real-world planning (23.6% on 20-40-step plans; no live robot deployment) | K5-E14, K5-E15, K5-E16 |
| 2025-01 to 2026-05 | A new architecture paradigm within 3-5 years; by early 2027 its necessity "completely obvious"; a general hierarchical world-model method about a year away | pending — as of 2026-11-14, four of his own line's papers (LeWM, a LeJEPA theory paper, LpWM, H-JEPA) are out, each validated only in simulation, offline video or small-scale robot data | K5-E35, K5-E19, K5-E64, K5-E67, K5-E68, K5-E69 |
| 2025-03 | Pure LLMs are "incapable of inventing new things" | contested — two months later, DeepMind's AlphaEvolve found a new matrix-multiplication algorithm, though by pairing an LLM with an outside evaluator and evolutionary search, i.e. the external-search mechanism he says LLMs lack | K5-E17, K5-E60 |

From the record:

- **Direction:** 2 of 7 calls above held outright, 3 held partly, 1 missed, 1 is pending; the miss
  and all three partial misses are claims about what today's LLMs specifically cannot do.
- **Timing:** his one fully-resolved long-run call (neural networks, 1988-2012) took about a decade
  to be vindicated; his active timelines now (3-5 years from 2025; "obvious" by early 2027) ask for
  resolution several times faster than that, and remain unresolved.

## 4. Where this persona is most likely wrong

- **Interests.** AMI's valuation bets on world models over LLMs, and its most aggressive timelines
  were stated while raising and hiring for AMI [synthesized, K5-E40]. He also advises against
  working on LLMs — advice that predates AMI by about 18 months [synthesized, K5-E34].
- **Path dependence.** The deep-learning-winter story taught him that minority positions plus
  first-principles argument eventually win, and his own ten-year failure on pixel prediction taught
  him to reject generative and pixel-based methods generally — which may make him underrate
  progress made in forms he dislikes (Veo-based evaluators, π0.5) [synthesized, K5-E37, K5-E38]. Two
  named public critics make a related point from opposite directions: Gary Marcus argues JEPA
  itself remains an unstructured network short of real geometric or causal structure [K5-E58], while
  Eric Xing's group argues LeCun is too quick to drop reconstruction as a check on understanding
  [K5-E70].
- **Different era or setting.** He entered a genuinely resource-free unfashionable field, backed by
  a tenured safety net; the world-model field he now bets on has already drawn over a billion
  dollars, so "nobody works on it" no longer applies the way it did for perceptrons [inferred].

## 5. One line for someone starting out

Follow his method, not his clock: chase the physical-world problem a house cat can solve and a
machine still cannot, use LLMs as tools rather than a research topic, and push his timelines later
than he states them, so your own work holds up under more than one architecture [synthesized].
