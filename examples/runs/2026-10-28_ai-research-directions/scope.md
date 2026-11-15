# AI research directions: scope

Run `2026-10-28_ai-research-directions` | started 2026-10-28 | materials through 2026-10-28

> **Adapted from a real run.** The original run was made for one private user, in Chinese. This
> public version is a translation with that user's background, own candidate topics and personal
> questions removed (details in [README.md](README.md)). Every persona output is a simulation
> based on public material, not the person's own words.

## What this run answers

1. How do 20 personas with very different paths rate 16 AI research directions on impact,
   bottleneck, academic edge and timing, and where do they disagree?
2. **Q1, levers:** over the next 5–10 years, which levers most decide progress in AI, physical AI
   and agents especially? Is evaluation really the safest bet, or RL, simulation, world models
   or world action models?
3. **Q2, academic foundation models:** academic labs with GPUs can train foundation models (open
   VLAs, video or world models, open LLMs). For a student at the undergraduate-to-master's stage,
   is joining this kind of work the highest-impact path? Under which conditions (C1–C5)?
4. **Q5, late entry:** for each direction, which way of taking part is already too late, and why?
5. **Q6, taste:** one piece of advice on research taste for someone starting out, and the
   experience behind it.

(Q3 and Q4 of the original run were about the original user and are removed.)

## How the run worked

1. **R1:** every persona scores every direction alone, without seeing anyone else.
2. **Crux map:** a fresh agent that had read no persona material grouped the disagreements into
   seven cruxes and seated six personas at each table, two tables per persona.
3. **Three named debate rounds per table:** A opening, B exchange (with interjections from other
   tables), C closing. Everyone at a table posts at the same time.
4. **Overtime:** at each table, the sharpest pair goes another two or three rounds.
5. **R3:** every persona re-scores privately, citing the post and the argument that moved each
   change.

Fact-checks ran on the evidence brief, between rounds B and C, and after R3; judges scored every
post. Two no-persona baselines (Z1, Z2) scored the same directions and did not debate.

## Four principles (set by the user before the run)

1. **Argue from your own experience.** That is why the simulation exists. Path dependence and the
   wins and failures you lived through are legitimate arguments, judged on whether the analogy
   holds here; they are not discounted or neutralized.
2. **Interests are shown, only.** Each post opens with the persona's interests as facts. They are
   not an argument and not a discount. Others may challenge the source of your evidence, never
   say "you have a stake, so you are wrong".
3. **Be persuaded by arguments, not by headcount or fame.** A changed score names the argument
   that changed it.
4. **Check evidence yourself**, only for specific claims, within a budget, and log it.

## Who is at the table

| ID | Persona | Group | ID | Persona | Group |
|---|---|---|---|---|---|
| C1 | Michael Mauboussin | capital and value | K1 | Vinod Khosla | capital and value |
| C2 | Bill Gurley | capital and value | K2 | Jeff Dean | platforms and cost |
| C3 | Jensen Huang | platforms and cost | K3 | Rich Sutton | experience and world models |
| C4 | Dario Amodei | scale and verification | K4 | Andrej Karpathy | scale and verification |
| C5 | Sergey Levine | experience and world models | K5 | Yann LeCun | experience and world models |
| C6 | Demis Hassabis | experience and world models | K6 | Patrick Collison | capital and value |
| M1 | Percy Liang | academia and evaluation | M5 | Kaiming He | multimodal and generative |
| M2 | Shunyu Yao | agents | M6 | Fei-Fei Li | spatial intelligence and robotics |
| M3 | Graham Neubig | academia and evaluation | M7 | Russ Tedrake | spatial intelligence and robotics |
| M4 | Saining Xie | multimodal and generative | M8 | Jun Zhu | multimodal and generative |

Not independent of each other (shared organization or long collaboration), as recorded in
`rubric.json`: M4 and K5; M5, C6 and K2; C4 and K4; M4 and M5.

## Directions

Full definitions in `rubric.json`. A persona whose method does not reach a direction scores it
`null` with one line of reason. D14–D16 were scored briefly (overall only).

| ID | Direction |
|---|---|
| D01 | Pre-training and foundation models |
| D02 | Post-training, RL and reasoning |
| D03 | Agent learning, continual learning and self-improvement |
| D04 | Agent systems and ecosystem |
| D05 | Evaluation science |
| D06 | Embodied AI and robot learning |
| D07 | Generative policies and world action models |
| D08 | World models and spatial intelligence |
| D09 | Simulation and synthetic data |
| D10 | Autonomous driving |
| D11 | Multimodal understanding |
| D12 | Multimodal generation |
| D13 | Interpretability, alignment and safety |
| D14 | AI infrastructure and algorithm-system co-design (short) |
| D15 | AI for science (short) |
| D16 | Recommendation, retrieval and decision optimization (short) |

## Rules every persona followed

1. Every output starts: "Simulation based on public material; not the person's own words."
2. Three labels, kept apart: `[quoted]`, `[synthesized]`, `[inferred]`. The person's views, the
   persona's extrapolation and technical evidence are written separately.
3. Experience arguments: what happened (with the dossier section), what it taught, why it applies
   here, where the analogy may break.
4. Quotes: only text actually read; English quotes under 15 words; at most one per source.
5. No invented positions: where the person has not spoken publicly, "no judgment" or `[inferred]`.
6. Scores are real judgments, never lowered by the persona's own interests; interests go in the
   `conflict` field, shown only.
7. Claude is trained by Anthropic; Dario Amodei is Anthropic's CEO and Andrej Karpathy joined
   its pre-training team in 2026-05. A reminder for the simulator, disclosed where relevant; scores are not adjusted.
