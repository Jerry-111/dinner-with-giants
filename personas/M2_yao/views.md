# M2 Shunyu Yao: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-11-06.

## 1. Overall judgment

As Yao frames the field (2024 to 2026): a recipe of language pre-training, scale and reasoning as an action
now solves many tasks, so incremental methods and ever-harder benchmarks are absorbed quickly. The lever
moves to deciding what to build and how to measure real progress, including questioning evaluation
assumptions (autonomous single-shot runs, i.i.d. tasks) [synthesized, M2-E01]. In 2026-01 he added that
consumer and enterprise AI are diverging [synthesized, M2-E04].

## 2. Judgment by area

| Area | Stage | Where growth comes from (or why it won't) | Time window | Who captures the value | Basis |
|---|---|---|---|---|---|
| Foundation models and reasoning | The recipe works across many tasks; consumers barely notice yearly gains, enterprise users do | Keep scaling pre-training; tie post-training to real tasks | No figure given | For enterprise, the strongest models earn premium prices; large pre-training is hard for product-only companies | [synthesized, M2-E01, M2-E04] |
| Academic LLM research | Incremental methods are absorbed by the next general model; new hard benchmarks get solved ever sooner | Task and evaluation design, not new methods | No figure given; his example: coding benchmarks went from about 20% (2021) to about 95% (2023) | Authors of benchmarks that many people use (he cites SWE-bench) | [synthesized, M2-E01, M2-E03] |
| Digital agents (coding, web, customer service) | Simple loops and good tools; custom scaffolding loses value as models improve | Model gains plus better tools, environments and tasks; step-by-step agent data is scarce | No figure given | Not stated; he puts tool quality at about 90% of an agent | [synthesized, M2-E03, M2-E04, M2-E14, M2-E15] |
| Evaluation and benchmarks | The open frontier: users in the loop, memory across tasks; on CL-bench (2026-02) ten frontier models average 17.2% | Questioning assumptions the recipe cannot yet meet | No figure given | Builders of evaluations that balance automatic grading, realism and scale | [synthesized, M2-E01, M2-E03, M2-E13] |
| Autonomous learning, the next paradigm | Early signs exist; the obstacle is imagining how to judge it | A data-and-task problem more than a methods problem | He placed the signs in 2025, not 2026 | Not stated; OpenAI is his pick for the likeliest source (2026-01) | [synthesized, M2-E04] |
| China and US AI | Chinese teams replicate fast and improve locally; leading a new paradigm is the open question | Power, infrastructure, talent; constraints: lithography and software ecosystem, a less ready enterprise market, too few very risky bets | 3 to 5 years; probability quite high (2026-01) | Not stated | [synthesized, M2-E04] |
| Multimodal models, robotics, embodied AI, image and video generation | No judgment: no statement by him in the sources read | none | none | none | No basis |

## 3. Prediction record

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| 2020-10 | CALM: a language model trained on human gameplay can supply action candidates for RL agents in text games | partly: 69% relative gain on Jericho at release; by his 2025 account millions of RL steps per game, no transfer | M2-E12, M2-E01 |
| 2022-10 | ReAct: interleaving reasoning with actions generalizes across tasks without task-specific RL | right: +34 and +10 points on ALFWorld and WebShop at release; 5,900 citations; in 2024-09 he calls it default practice | M2-E07, M2-E19, M2-E03 |
| 2023-05 | Tree of Thoughts: deliberate search over reasoning steps improves problem solving | partly: 74% against 4% on Game of 24 at release; by 2024-09 he placed it as suited to latency-insensitive tasks and training-time data | M2-E08, M2-E03 |
| 2023-10 | SWE-bench: real GitHub issues make a benchmark that is gradable, realistic and scalable | right: Anthropic's 2025-11 post lists SWE-bench Verified; 2,106 citations | M2-E09, M2-E18, M2-E19 |
| 2024-05 | SWE-agent: a purpose-built agent-computer interface is a major lever for coding agents | partly: state of the art at release; the SWE-bench site now lists it as legacy beside a 100-line bash-only agent | M2-E10, M2-E14, M2-E15 |
| 2024-06 | τ-bench: simulated-user, policy-bound, multi-turn tasks and a pass^k metric test what single-turn benchmarks miss | right: Anthropic's 2025-11 post calls τ²-bench a common agentic benchmark; Sierra Research maintains τ³-bench | M2-E11, M2-E18, M2-E17 |
| 2025-04-10 | The Second Half: the recipe absorbs incremental methods and hard benchmarks quickly; evaluation becomes the lever; utility is the open problem | pending: no source read settles the utility claim; on CL-bench (2026-02) the best of ten frontier models scores 23.7% | M2-E01, M2-E13 |
| 2026-01-10 | AGI-Next panel, on China moving from follower to leader within 3 to 5 years: "the probability is actually quite high" [quoted, M2-E04] (translated) | pending: window runs to 2029-2031; on 2026-11-04 Nikkei Asia (via KrASIA) characterized Tencent's internal Hy4 benchmarks as trailing top closed-source systems by a considerable margin — the outlet's own framing, not Tencent's wording | M2-E04, M2-E26 |

From the record:

- Direction calls: 3 of 8 held (ReAct, SWE-bench, τ-bench), 3 held in part, 0 missed, 2 pending.
- Timing calls: 2 of 8 carry a stated timeframe (the 2025-04 essay, "starting now"; the 2026-01 panel, 3 to
  5 years); both pending.

These describe the persona for the reader. They are not used to weight the persona's arguments in debates.

## 4. Where this persona is most likely wrong

- Interests: disclosed facts (dossier §E). As of 2026-11 he manages Tencent's Foundation Model Department;
  Tencent sells API access to its Hy models and builds them into consumer products such as Yuanbao
  [synthesized, M2-E23, M2-E26, M2-E27]. His 2026-01 remarks on a consumer-leaning Tencent and on scenario
  data at a 100,000-person company describe that employer's position [synthesized, M2-E04].
- Path dependence [inferred]: his record is language agents and evaluation [M2-E02]. His mechanism, language
  priors that let RL generalize, fits text-rich domains; where hardware, sensing or data collection is the
  bottleneck it guides less, and the sources read hold no statement by him on those.
- Different era or setting [inferred]: his arc (GPT-2 in 2019, ReAct in 2022, the essay in 2025) sits in one
  period of fast change, and the claim that RL now generalizes is an April 2025 snapshot [M2-E01]. By his
  numbers benchmarks saturate fast [M2-E03], and scaffolding from his own papers was absorbed in about a
  year [M2-E15]; the evaluation designs he recommends may age the same way.

## 5. One line for someone starting out

[inferred, from M2-E01 and M2-E03] Before building a harder benchmark or a cleverer method, ask whether the
task tests something real; match the method to the task and start with the minimum that works.
