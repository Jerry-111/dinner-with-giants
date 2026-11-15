# K2 Jeff Dean: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-11-05.

## 1. Overall judgment

As this persona would see the field: the current wave is the delayed payoff of an idea he tried in 1990, when parallel neural-network training was short by about a million times the compute [inferred, K2-E02, K2-E11]. On pace: he does not expect this to slow down over the next few model generations [synthesized, K2-E02]. The next driver is automating the experiment loop, which he says covers essentially any task with a measurable objective [synthesized, K2-E01]. Constraints move to energy and data movement, latency, and domains with no automatic scoring [synthesized, K2-E03, K2-E04, K2-E01].

## 2. Judgment by area

| Area | Stage | Where growth comes from (or why it won't) | Time window | Who captures the value | Basis |
|---|---|---|---|---|---|
| Foundation models and inference | Still improving | Algorithms matter at least as much as hardware (K2-E04); distillation lets a new Flash match the prior Pro (K2-E03). Limits: the largest runs cannot be screened at 1/1000 scale (K2-E02); benchmarks near 95% give diminishing returns (K2-E03) | Next few generations | A handful of frontier models, not 50 (K2-E04); [inferred] platforms that distill and serve | [synthesized]; value [inferred] |
| Digital agents (coding, research) | Accelerating | Any measurable objective can run as an automated experiment loop; agents run for days or weeks (K2-E01); task length at 50% success doubles about every 7 months (K2-E25). Slower: reinforcement learning for non-verifiable domains is open (K2-E03); taste often has no measurable objective (K2-E01) | 2026-27 | [inferred] Whoever picks the tasks and owns the evaluator | [synthesized]; value [inferred] |
| Robotics and embodied AI | Early | "similar things will happen in physical robotic agents as well" [quoted, K2-E04]; a general base plus small amounts of robot data (K2-E03); useful in one room first, then about 10x cheaper (K2-E04). [inferred] Real-world data arrives slower than software loops | About 20 useful tasks in a room within 1-2 years of 2025-05; pending | [inferred] Owners of base models plus real-world data and deployment | [quoted] K2-E04; [synthesized]; rest [inferred] |
| Compute, chips and energy | Accelerating | Per-request inference compute up 50-1,000x, plus one to two orders of magnitude each from adoption and model size, by 2030 (K2-E02); data movement costs far more than arithmetic (K2-E03, K2-E04); 10x-1,000x inference-efficiency gains are possible (K2-E04) | To 2030 | [inferred] Efficient inference hardware and energy; Google's seventh-generation TPU is described as the first built for inference (K2-E23) | [synthesized]; value [inferred] |
| Science, education, healthcare | Early | A network trained on a costly simulator ran 300,000x faster for quantum chemistry (K2-E05); a specialized protein-folding model sits outside the general mix (K2-E01); vertical models can sit on a strong base, in healthcare via holders of non-public data (K2-E03); an education demo was good about 30% of the time, a strong sign (K2-E04). Thin application layers can be overtaken within 6-12 months (K2-E01, to founders) | [inferred] Years; no dates given | [inferred] Teams that own the verification loop (goal, simulator, data); holders of private data | [synthesized]; rest [inferred] |

No judgment found in the parts read of K2-E01, K2-E03 and K2-E04: safety and alignment as a separate track, autonomous driving, US-China competition, humanoid robots, the term "world model" [synthesized].

## 3. Prediction record

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| 1990 | Senior thesis: parallel neural-network training works; 32 processors expected to suffice | partly: it worked, but needed about a million times more compute, available around 2008 | K2-E02, K2-E06, K2-E11 |
| 2013 | Speech-recognition load would double the server fleet; build an 8-bit inference chip, quantization unproven | right: TPU in datacenters since 2015; seventh generation 2025-04; Anthropic plans up to one million TPUs (2025-10) | K2-E01, K2-E02, K2-E17, K2-E23, K2-E24 |
| 2021-10 | Pathways: one sparse, multimodal model for many tasks | partly: Gemini is multimodal from the start (K2-E08); more organic, modular models remain a vision with no results shown (K2-E02) | K2-E14, K2-E08, K2-E02 |
| 2021 | Reinforcement learning places chip macros well (AlphaChip, Nature) | partly, disputed: authors report use in chips across Alphabet (K2-E20); Igor Markov reports it trailing simulated annealing, human designers and commercial software (K2-E21) | K2-E20, K2-E21 |
| 2022-12 | Google should move more conservatively than a startup on chatbot-style products: "it's super important we get this right" [quoted, K2-E15] | partly: Brain and DeepMind merged within five months (K2-E16); in 2026-02 he called the earlier fragmentation of resources stupid (K2-E03) | K2-E15, K2-E16, K2-E03 |
| 2025-05 | AI at a junior engineer's level is probably possible within about a year | right, by his 2026-07 assessment (held up, depending on the definition); no independent test cited | K2-E04, K2-E01 |
| 2025-05 | About 20 useful robot tasks in a room within a year or two, then about 10x cheaper | pending (window ends about 2027-05) | K2-E04 |
| 2026-07 | Asked for a 2027 prediction: much more automation of ML systems themselves, improving through many experiments | pending | K2-E01 |

From the record:

- Direction: 3 of 8 dated calls held (1990, 2013, 2025-05); 2 held in part or are disputed (Pathways, chip placement); 1 position changed within five months (2022-12); 2 pending.
- Timing: of 2 resolved dated timing calls, 1 came early by about 18-20 years (1990) and 1 held (2025-05, by his own assessment); 2 pending.

## 4. Where this persona is most likely wrong

- Interests: dated facts in dossier §E. [inferred] His work ran on Google's compute, colleagues and distribution; Discovery Loop keeps Google as founding investor and cloud partner (K2-E29, K2-E32), so advice on team size and focus may not transfer to groups without a large backer.
- Path dependence: [inferred] His record is in domains with a measurable goal and a loop that runs in data centers (search, TPU, Gemini); the framework gives less guidance for real robots, wet labs or human subjects. Small-scale screening has a limit: emergent abilities appear only at larger scale (K2-E22).
- Different era or setting: [inferred] He joined a company of about 25 people (K2-E02) whose search served a few million queries (K2-E06); a newcomer starts without the compute, colleagues and infrastructure he had.

## 5. One line for someone starting out

Write down what you expect to matter in the next 12 months and check in a year; pick a problem of about five-year shape; screen ideas small and skim widely; check whether you have the compute and collaborators his advice assumes.
