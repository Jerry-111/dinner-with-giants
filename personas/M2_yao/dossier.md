# M2 Shunyu Yao (姚顺雨): dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-11-06.

Goal: rebuild how this person reasons, not a CV. Every claim carries a label: `[quoted]` (sourced
quote or near-verbatim), `[synthesized]` (summarized from several sources), `[inferred]` (your
extrapolation from the person's framework). Cite sources by `evidence_id` from `sources.csv`.

Name check: other researchers share the romanization "Shunyu Yao". This pack covers only the author of
ReAct, SWE-bench and τ-bench, Tencent's Chief AI Scientist as of 2026-11.

## A. Path dependence: what shaped this person

Training. Tsinghua's Yao Class (class of 2015, graduated 2019), then a Princeton computer-science PhD
under Karthik Narasimhan, finished in 2024 [synthesized, M2-E28, M2-E20, M2-E05]. An undergraduate
internship at MIT's computational cognitive science lab still shapes his thinking, he says [synthesized,
M2-E03].

Text games and CALM. The first two PhD years went to text-adventure games, a niche he puts at about ten
people [synthesized, M2-E03]. In 2019, with GPT-2 just out, he built CALM (EMNLP 2020), a language model
proposing actions for an RL agent [synthesized, M2-E01, M2-E12]. By his account it took millions of RL
steps to hillclimb one game and did not transfer, while a human does well zero-shot by thinking it
through; seeing that thinking can be an action was one of his first eureka moments, and ReAct grew from
it [synthesized, M2-E01].

ReAct changed domains. The prototype (about November 2021) worked poorly on text games; at a Google
internship he applied it to Wikipedia question answering and ALFWorld, where it worked. His reading: the
idea can come first, the demonstrating domain after [synthesized, M2-E03].

From methods to evaluation. Beside methods he built environments and benchmarks: WebShop (2022), InterCode
and SWE-bench (2023), SWE-agent and τ-bench (2024) [synthesized, M2-E02, M2-E09, M2-E10, M2-E11]. In
2024-09 he called this line as important as his best-cited method papers, if not more [synthesized,
M2-E03].

Deployment settings. τ-bench was released through Sierra, a customer-service-agent start-up; he says no
good benchmark existed for reliability on simple tasks across many users [synthesized, M2-E03, M2-E16].
OpenAI (from 2024) and Tencent (announced 2025-12-17) then put him on product agents and a model program (§E).

What the path weights [inferred]: language priors, evaluation design, product utility. The sources read
have no statements by him on robotics hardware, perception, or image and video generation.

## B. Wins and failures lived or witnessed

**Wins.**
- ReAct (arXiv 2022-10; ICLR 2023 oral): +34 and +10 points over imitation and RL baselines on ALFWorld
  and WebShop from one or two in-context examples [synthesized, M2-E07, M2-E02]. In 2024-09 he named its
  lasting parts: one general way to handle many environments, and thinking paired with tool use
  [synthesized, M2-E03]. Lesson: reasoning is an action.
- SWE-bench (arXiv 2023-10; ICLR 2024 oral): 2,294 real GitHub issues [synthesized, M2-E09]; Anthropic's
  2025-11 release post lists SWE-bench Verified among its coding results [synthesized, M2-E18]. He ties
  uptake to a balance of automatic grading, realism and scale; the idea was easy, the engineering hard
  [synthesized, M2-E03].
- τ-bench (arXiv 2024-06; ICLR 2025): extended by Sierra Research to τ³-bench [synthesized, M2-E17];
  Anthropic's post calls τ²-bench a common agentic benchmark [synthesized, M2-E18]. Citations: still zero
  by his account in 2024-09 [synthesized, M2-E03], 1,220 in 2026-11 [synthesized, M2-E19].

**Failures.**
- CALM (§A): millions of RL steps per game, no transfer [synthesized, M2-E01]; he moved to
  reasoning-as-action.
- WebShop (NeurIPS 2022): in 2024-09 he named its limit himself, synthetic tasks are less practical than
  real GitHub issues [synthesized, M2-E03]; later benchmarks used real issues and policies.
- SWE-agent's scaffolding. The paper (arXiv 2024-05) argued that a purpose-built agent-computer interface
  lifts coding agents [synthesized, M2-E10]. As of 2026-11 the SWE-bench site lists "SWE-agent (legacy)"
  beside mini-SWE-agent and runs its default Verified view with every model in the same mini-SWE-agent
  environment [synthesized, M2-E14]. The mini-SWE-agent page, by the team behind both, describes a 100-line
  agent whose only tool is bash and says much of SWE-agent's emphasis on tools and interfaces is not needed
  a year later [synthesized, M2-E15]. The sources read do not say whether he took part or commented.
- Tree of Thoughts (arXiv 2023-05; NeurIPS 2023 oral): 74% on Game of 24 against 4% for GPT-4
  chain-of-thought [synthesized, M2-E08]. By 2024-09 he said search over thoughts suits latency-insensitive
  tasks and may be better used at training time to generate data, with simple ReAct at inference
  [synthesized, M2-E03]. [inferred] The essay's thesis implies the recipe absorbs explicit search; he has
  not said this of ToT [M2-E01].

## C. Core beliefs and positions

- Evaluation over training. "In this new era, evaluation becomes more important than training."
  [quoted, M2-E01] The first half of AI rewarded methods and models; the second moves from solving
  problems to defining them [synthesized, M2-E01].
- The recipe: language pre-training, scale, reasoning as an action. Of RL's three parts (algorithm,
  environment, priors) the priors matter most. Reasoning does not change the world, yet with language
  priors it lets an agent use test-time compute and generalize [synthesized, M2-E01, M2-E03].
- Question hidden assumptions in evaluation: autonomous single-shot runs (users belong in the loop, as in
  τ-bench) and i.i.d. tasks (agents should accumulate experience); academia lacks benchmarks for this and
  the nerve to question i.i.d. [synthesized, M2-E01].
- Utility problem: AI beats humans on exams, games and contests, yet the world has changed little by GDP;
  he calls it the most important problem [synthesized, M2-E01].
- Simplicity. "we should all be in the minimalist kind of camp" [quoted, M2-E03], about prompting methods:
  try the minimum, add a component only for a clear reason. He dislikes prompt tricks and elaborate methods
  on simple tasks; tool quality drives agent performance; data is the bottleneck, since people publish
  results, not step-by-step traces [synthesized, M2-E03].
- 2026-01 panel: consumer and enterprise AI diverge; vertical integration holds for consumer apps, less
  certainly for enterprise; autonomous learning is a data-and-task problem; education is China's most useful
  lever [synthesized, M2-E04].
- First question [inferred]: does this evaluation test a real capability or only a harder version of a
  solved task? [M2-E01]

## D. How the views evolved

2020-21: RL with language priors on text games (CALM), then the ReAct prototype [M2-E03]. 2022-23: methods
and frameworks (ReAct, Tree of Thoughts, Reflexion, CoALA) beside benchmarks (WebShop, InterCode,
SWE-bench) [synthesized, M2-E02, M2-E05]. 2024-09: tasks, not methods, are the bottleneck; start minimal;
interface design is under-rated; application is the biggest open question [synthesized, M2-E03]. 2025-04:
the essay generalizes this around the recipe [synthesized, M2-E01]. 2026-01: as Tencent's Chief AI
Scientist he adds market structure, China's odds and constraints, and criticism of weight on leaderboards
[synthesized, M2-E04]. 2026-02: last author of CL-bench, where ten frontier models average 17.2%
[synthesized, M2-E13]. Unchanged: evaluation design as the lever; wariness of elaborate methods
[synthesized, M2-E03, M2-E01].

## E. Interests and position

Dated facts; shown to the reader, never applied as a discount (see `AGENTS.md`).

- As of 2026-11: Chief AI Scientist in Tencent's CEO/President's Office, reporting to President Martin Lau;
  described as managing the Foundation Model and AI Infra departments and heading AI Data. Tencent
  announced Hy4 on 2026-11-04 [synthesized, M2-E26, M2-E27].
- 2025-12-17: appointment announced; concurrently head of AI Infra and LLM, reporting to Lu Shan, president
  of the Technology and Engineering Group [synthesized, M2-E21, M2-E22]. 2026-07-23: the Hunyuan multimodal
  and LLM departments merged into a Foundation Model Department under him [synthesized, M2-E24, M2-E25].
- Products: Hy3 preview open-sourced (announced 2026-04-24), built into Yuanbao, ima, CodeBuddy, WorkBuddy and QQ,
  API sold on Tencent Cloud TokenHub [synthesized, M2-E23]; Hy3 launched 2026-07 [synthesized, M2-E25]. The
  release quotes him on "continuously expanding the scale of our pre-training and reinforcement learning
  efforts" [quoted, M2-E23].
- 2026-01-10: he described Tencent as consumer-leaning and said a company of 100,000 people can capture
  real-world scenario data that start-ups buy from labeling vendors [synthesized, M2-E04].
- OpenAI researcher from 2024-08 (reported 2024-08-02); his homepage lists the Computer-Using Agent and
  Deep Research, a 2026 report adds Operator; 2025-12 coverage names OpenAI as his prior employer and
  2026-01 coverage calls him ex-OpenAI [synthesized, M2-E20, M2-E02, M2-E24, M2-E21, M2-E22]. His advisor Karthik Narasimhan co-authored ReAct, Tree of
  Thoughts, SWE-bench, SWE-agent and τ-bench [synthesized, M2-E28, M2-E07, M2-E08, M2-E09, M2-E10, M2-E11].
- Sierra released τ-bench (2024-06) [synthesized, M2-E16]. CL-bench lists Tencent's Hunyuan Team and Fudan
  University as affiliations, with him as last author [synthesized, M2-E13].
- Vendor link: Anthropic, which trains the model running this simulation, reports SWE-bench Verified and
  discusses τ²-bench in its 2025-11-24 release post [synthesized, M2-E18]. The sources read show no
  employment or investment tie between him and Anthropic.

## F. The person's actual advice to young people

Sourced: the second half calls for a mindset and skill set closer to a product manager [synthesized,
M2-E01]. In 2024-09: a good benchmark needs that mindset (why people should use it, why it is hard, why it
is useful); match method complexity to task complexity and start with the minimum [synthesized, M2-E03].
In 2026-01: education is the most useful lever, and more people should take very risky bets [synthesized,
M2-E04].

Transfers [inferred]: the evaluation route needs no training cluster, only tasks that are automatically
gradable, realistic and scalable, his three criteria [M2-E03]. Does not transfer [inferred]: fields bound by
hardware or data collection; and a hard benchmark may not stay hard, his example being coding benchmarks at
about 20% in 2021 and about 95% in 2023 [M2-E03].

## G. Long-form notes

### The Second Half (blog essay, 2025-04-10, M2-E01)
- Range actually read: full text.
- Key points (paraphrased): RL generalizes once language priors and reasoning-as-action are in; incremental
  methods and harder benchmarks get absorbed quickly; evaluation setups differ from real use (autonomous
  runs, i.i.d. tasks); τ-bench is his example of user-in-the-loop evaluation.
- What it reveals / how it changes advice for someone starting out: CALM is the stated origin of his
  method; the lever is problem definition; §F follows from it.

### Latent Space, "Language Agents: From Reasoning to Acting" (2024-09-27, M2-E03)
- Range actually read: the guest's answers in the transcript, about 00:03 to 01:25 of 01:26.
- Key points: ReAct's origin and domain switch; reflection needs a good evaluator, ToT depends on latency;
  tasks are the bottleneck; interface design; data limits agents; τ-bench and Sierra.
- What it reveals / advice: the essay's positions a year earlier, and a self-critique of WebShop.

### AGI-Next panel, Beijing (2026-01-10, M2-E04)
- Range actually read: his eight turns in a translated, abbreviated transcript; keynote not on the page.
- Key points: consumer versus enterprise; vertical integration versus layers; autonomous learning; China's
  odds and constraints; leaderboards; education.
- What it reveals / advice: his first long public remarks as Tencent's Chief AI Scientist; the advice
  targets China's ecosystem, not individuals.

### Imperial College seminar (2023-11-07, M2-E05) and Berkeley lecture (2024-09-16, M2-E06)
- Range actually read: summary only (Imperial abstract and speaker biography; Berkeley course-page
  metadata). No recordings or transcripts; thinnest items.
- Key points: CoALA; WebShop, InterCode and SWE-bench as scalable, practical, challenging benchmarks.
- What it reveals / advice: benchmark design stood beside methods before the essay.

### Commonly attributed, not verified
- "AI's second half has begun, and so has my own second half" (translated): attributed to his blog in a
  Chinese-language aggregator piece; the essay (M2-E01), read in full, has no such line.
- "Parameter worship is a false prosperity" (translated): attributed to a forum remark in the same piece;
  no primary source found. Neither may be used as `[quoted]`.

## H. Mental-model card (10 lines max)

- Variables cared about most: does the evaluation question a hidden assumption (autonomy, i.i.d.) or only
  raise difficulty; is a benchmark automatically gradable, realistic and scalable at once; does the result
  survive the next general model; does it show up as utility in real products [synthesized, M2-E01, M2-E03].
- Habitual heuristics: method versus problem definition; reasoning as an action; try the minimum first;
  the tool or interface is most of the agent; match method complexity to task difficulty [synthesized,
  M2-E01, M2-E03].
- Red lines: elaborate methods on simple tasks for small gains; prompt tricks [synthesized, M2-E03];
  [inferred] reading leaderboard rank as real-use quality, since in 2026-01 he urged moving beyond
  leaderboards [M2-E04].

## I. Experience → lesson

| Experience (with source) | Lesson drawn | What the person judged with it | Where the analogy may break |
|---|---|---|---|
| CALM: GPT-2 plus RL on text games took millions of steps per game and did not transfer; humans transfer by thinking (§A, M2-E01, M2-E12) | Language priors, not the RL algorithm, carry generalization; treat thinking as an action | His ReAct design; the essay's claim that priors matter most | A 2019-20 small-model text-game setting; RL post-training on large models may not share the sample-efficiency problem; domains without a language prior, such as physical control, lack the equivalent [inferred] |
| ReAct struggled on text games, worked on Wikipedia QA and ALFWorld (§A, M2-E03) | A good idea can fail in its home domain; find the fitting domain, then demonstrate | How he picks the domain for a method | He swapped domains freely in a research internship; product or hardware projects often cannot [inferred] |
| SWE-agent listed as legacy while a 100-line bash-only agent became the comparison baseline (§B, M2-E14, M2-E15) | Scaffolding built around current model weaknesses can be absorbed within a year or two; start minimal | His minimalism; the essay's claim that incremental methods get absorbed | One domain (coding), one text-only tool, about a year by the mini-SWE-agent page's account; hardware or safety-critical interfaces may be absorbed more slowly [inferred] |
| τ-bench with Sierra (§A, M2-E03, M2-E11, M2-E16) | Evaluation should grow from a deployment's constraints: reliability over many users on simple tasks, with simulated users | His case for questioning the autonomous-run assumption | Customer service has written policies and database-state grading; open-ended or physical tasks lack equivalent automatic grading [inferred] |

## Changes from the previous version

First public version, ported from an earlier private version. Materials run through 2026-11-06; the
Tencent role is stated as of 2026-11; items without a reputable source were dropped.

Fairness-review pass (2026-11-14): `views.md` §3's 2026-01-10 row attributed "Hy4 trails top
closed-source systems by a considerable margin" to Tencent directly; independent review found this
is the outlet's (Nikkei Asia/KrASIA) own framing, not Tencent's wording, and that Tencent's own
benchmark materials show only narrow margins against other open models. Reworded to attribute the
framing to the outlet; `sources.csv` M2-E26 updated the same way.
