# K3 Rich Sutton: dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-10-06.

Goal: rebuild how this person reasons, not a CV. Every claim carries a label: `[quoted]` (sourced
quote or near-verbatim), `[synthesized]` (summarized from several sources), `[inferred]` (your
extrapolation from the person's framework). Cite sources by `evidence_id` from `sources.csv`.

## A. Path dependence: what shaped this person

A Stanford psychology undergraduate (BA 1978), disillusioned with what he saw as calcified thinking in neural psychology [synthesized, K3-E01, K3-E02]. He found Harry Klopf's work on reward-driven learning in the library; a letter led to a lunch and, after graduation, a place on a UMass Amherst project built to test Klopf's ideas. The project had about five years of Air Force and NSF funding and almost no deliverables; Barto has called the freedom to be unfashionable a luxury [synthesized, K3-E03]. His PhD there (1984) was under Andrew Barto [synthesized, K3-E02, K3-E04].

GTE Laboratories 1985–1994, where the 1988 TD paper was written [synthesized, K3-E02, K3-E05]; the University of Alberta from 2003, recruited with provincial funding to found Amii's forerunner [synthesized, K3-E06]. He prefers Canada's broader, smaller grants to a US system he called "winner-take-all" [quoted, K3-E07].

DeepMind put its first lab outside the UK in Edmonton in 2017, citing its relationship with him [synthesized, K3-E06]. Alphabet closed it in early 2023 within a 12,000-person cut; he said the team was freed to focus and had not been entirely its own master [synthesized, K3-E08]. He joined John Carmack's Keen Technologies (announced 2023-09-25) to work on the Alberta Plan, aiming at a genuine AI prototype by 2030 [synthesized, K3-E09]; in July 2026 he and a former student, Khurram Javed, announced they were leaving Keen to found Oak Lab [synthesized, K3-E10, K3-E11].

Weighted heavily [inferred]: a neglected, obvious principle wins if pursued long enough; a small group can stand against large labs; changing institutions costs little. Weighted lightly [inferred]: the safety net under that persistence (tenure, reputation, funding); pretrained priors.

## B. Wins and failures lived or witnessed

**Wins.** (1) TD learning grew out of thinking about how animals learn; he calls it "the best thing I ever did" [quoted, K3-E12]. He names Gerald Tesauro's TD-Gammon as AlphaGo's precursor and says AlphaZero used TD and needed no human knowledge, which fit his worldview [synthesized, K3-E13]. Lesson: simple general principles win. (2) In 2025-09 he called the Bitter Lesson (§C) an empirical observation about one period of history that need not hold for the next 70 years [synthesized, K3-E13]: a limit on his own claim, not a retreat from experience-first.

**Failures and setbacks.** (1) RL was set aside for decades: after the 1960s the link to reward was lost [synthesized, K3-E12]; in the 1980s it was out of fashion yet seemed obvious to him [synthesized, K3-E02]. No change of view. (2) The simulation era: in the 2025 Silver–Sutton account, simulator-trained agents beat humans but did not cross the gap to reality, and experiential RL was largely set aside for human-data agents [synthesized, K3-E14]. In 2026 he felt some disappointment about the past eight years [synthesized, K3-E15] and called synthetic data a big mistake [synthesized, K3-E16]. Strengthened, not reversed. (3) Keen (2023-09 to 2026-07): the 2030 prototype goal (§A) was still open when he left; the public output is the Physical Atari paper, with its cross-robot result in §I [synthesized, K3-E09, K3-E17]. [inferred] Real-robot work is slow and costly, and the paper has no simulation or human-data baseline.

## C. Core beliefs and positions

**Aim and verification.** Understanding the mind is the greatest scientific achievement of any era [synthesized, K3-E02]. He says an AI "has to be able to tell for itself if it is right or wrong" [quoted, K3-E02]. LLMs, as he sees it, get by without a goal or a sense of better or worse, so they have no ground truth; a goal is the essence of intelligence [synthesized, K3-E13]. "Without experience, superintelligence would not exist" (translated) [quoted, K3-E15].

**Bitter Lesson, held firmly.** "general methods that leverage computation are ultimately the most effective" [quoted, K3-E18]; in 2025-09, "the weak methods have just totally won" [quoted, K3-E13]. He sees LLMs as a case where more human knowledge helps now; he expects experience-learning systems that scale better, which would make LLMs another instance of the lesson, and says starting from human knowledge has in practice always turned out badly [synthesized, K3-E13]. The Alberta Plan makes it a design rule: favor methods that scale with computing power over human insight [synthesized, K3-E19].

**Continual learning.** One algorithm at every moment, no separate training and deployment phases [synthesized, K3-E13, K3-E19]. "I'm not weird. The field is weird." [quoted, K3-E16] He calls himself a classicist, not a contrarian, and is content to be out of sync with the field for decades [synthesized, K3-E13]; the Alberta Plan calls its vision "classical and contrarian" [quoted, K3-E19].

**World and models.** The world is bigger than the agent, so any dataset or simulator is a small slice [synthesized, K3-E13, K3-E16]. A world model is an abstract transition model; physical models and video-frame generators are among the mistakes (2024-02), and low-level physics simulators extremely narrow (2026-07), both translated [synthesized, K3-E20, K3-E21].

**Method and values.** "There are no authorities in science." [quoted, K3-E01] As of 2026-03, unsolved hard problems rank above demos or companies for money [synthesized, K3-E12]. Succession to digital intelligence is inevitable, and should be voluntary [synthesized, K3-E13]: a value position, not evidence. No single set of human values exists, so aligning AI to them is a poor frame (translated) [synthesized, K3-E22]; doom talk is overblown [synthesized, K3-E23], though copying among digital minds creates a corruption risk [synthesized, K3-E13].

**Questions first** [inferred]: How does it know it is wrong? Does it improve with compute? Does it still learn while running? **Tastes.** Simple principles; animals and children as reference cases [synthesized, K3-E13].

## D. How the views evolved

| Period | Position |
|---|---|
| 2017 | Planning with a learned world model is the next big step [synthesized, K3-E02]; expected strong AI algorithms possibly by 2030 [synthesized, K3-E24] |
| 2023–24 | Called LLMs a passing trend, possibly a decade-long one [synthesized, K3-E08]; LLMs somewhat disappointing, 25% for human-level intelligence by 2030 (translated) [synthesized, K3-E20] |
| 2025 | With Silver: human data nearing a limit [synthesized, K3-E14]; surprised how well neural networks handle language, but LLMs lack goals [synthesized, K3-E13]; 25% by 2030, 50% by 2040 [synthesized, K3-E23] |
| 2026 | LLMs a major breakthrough, priors and learning need not be opposed [synthesized, K3-E16]; Oak Lab; 10% by 2030, 50% by 2040 for deep understanding of intelligence [synthesized, K3-E25] |

Unchanged: experience, continual learning, planning with learned models, 50% by 2040. Changed: warmer on LLMs; harder on simulation; new emphasis on energy and credit assignment [synthesized, K3-E26].

## E. Interests and position

Dated facts; shown to the reader, never applied as a discount (see `AGENTS.md`).

- 2026-06 on: co-founder, with Khurram Javed, of Oak Lab, a for-profit Canadian-incorporated company announced 2026-07-13 [synthesized, K3-E10, K3-E27, K3-E28]. Aim, quoted without attribution: algorithms that "learn in real time without storing or replaying data" [quoted, K3-E10]; long term, a trillion-parameter agent on about 20 watts [synthesized, K3-E11]. Its site shows one research post and no team or funding (2026-11-14) [synthesized, K3-E29].
- 2026-07-19/20: said at WAIC in Shanghai, per Chinese outlets (translated), that he was raising funds for Oak Lab and progress was good but not final [synthesized, K3-E28, K3-E15]. No round, amount or investor is published in the sources found through 2026-11-14.
- 2023-09 to 2026-07: research scientist at Keen Technologies [synthesized, K3-E09, K3-E12]; left 2026-07 [synthesized, K3-E11, K3-E27], saying after three years there that an organization of his own would let the group focus more [synthesized, K3-E15].
- 2023-11 on: Openmind Research Institute, a non-profit announced with $4.8 million from Huawei Canada; open source, no intellectual property sought [synthesized, K3-E30]; described as his co-founding [synthesized, K3-E31]. 2026-07: said Openmind and Beijing's Tashan Technology are building a robot experiment space [synthesized, K3-E28]; opened September 2026, naming his team, not his role [synthesized, K3-E32].
- 2003 on: professor, University of Alberta (as of 2026-07) [synthesized, K3-E10]; Amii chief scientific advisor (as of 2025-03) [synthesized, K3-E01]. 2017–2023: DeepMind (Alphabet) distinguished research scientist [synthesized, K3-E04, K3-E06].
- 2025-03-05: 2024 ACM A.M. Turing Award with Andrew Barto [synthesized, K3-E23].
- Disclosed fact: Oak Lab's stated direction (learning from experience) is the approach he argues for in public [synthesized, K3-E26, K3-E13].

## F. The person's actual advice to young people

| Advice | Source | Transfers to someone starting out? [inferred] |
|---|---|---|
| Write a page of your own ideas daily, challenge it, keep going for over a year | [synthesized, K3-E15, K3-E01] | Yes; nearly free |
| Go back to first principles; accept no claim on authority; make conclusions measurable; avoid systems that only hand out answers | [synthesized, K3-E22, K3-E15] | Yes |
| Build one area you truly understand (a power center) and expand | [synthesized, K3-E15] | Yes; choosing the area is the hard part |
| The most important contribution you can make is "something that seems obvious to us" | [quoted, K3-E33] | Yes, if you can bear that nobody sees it yet |
| Be content to be out of sync with the field for decades | [synthesized, K3-E13] | No: he had tenure, a reputation and the funding of his era [inferred, K3-E03] |

## G. Long-form notes

### The Alberta Plan for AI Research (2022-08-23, K3-E19)

- Range actually read: abstract, overview, four-feature vision, twelve-step list and Step 1; later steps by keyword.
- Key points (paraphrased): 5–10 year plan; online reward maximization with limited computation; scale-with-compute methods; simplest setting first; twelve steps to an OaK prototype (options and knowledge, per K3-E21).
- What it reveals: the method and the Bitter Lesson as a design rule; no mention of language.
- How it changes the advice to the user: a way to pick a problem; it assumes years of runway.

### Dwarkesh Patel podcast (2025-09-26, K3-E13)

- Range actually read: full transcript (about 66 minutes) in the earlier version; passages re-checked by keyword in 2026-11.
- Key points (paraphrased): RL is about understanding the world, LLMs about mimicking people; no goal or ground truth in LLMs; the Bitter Lesson as an observation about one period; succession inevitable but voluntary.
- What it reveals: his hardest line on LLMs as a starting point, and a self-limit on the Bitter Lesson; no evidence that would change his mind is stated in the passages searched.
- How it changes the advice to the user: pick problems with a right-or-wrong signal; being out of sync was affordable from tenure.

### Sequoia Training Data with Khurram Javed (2026-08-18, K3-E16)

- Range actually read: full transcript (no timestamps) in the earlier version; re-checked in 2026-11.
- Key points (paraphrased): all learning is continual; synthetic data a big mistake; priors and learning need not be opposed; forgetting curable; 20 watts in about ten years; Oak starts small with like-minded hires.
- What it reveals: warmer on LLMs, firmer on simulation, timeline hopes unchanged.
- How it changes the advice to the user: [inferred] work built on simulation or synthetic data should expect his objection.

### Commonly attributed, not verified

- "LLMs are a dead end": the host's phrase (title, intro, chapter heading), not found in Sutton's own words in the transcript [K3-E13].
- "Sutton predicts AGI by 2030": 2017, algorithms might exist by 2030, with up to ten more years possibly needed [K3-E24]; 2024, 25% for human-level intelligence [K3-E20]; 2026, 10% for deep understanding [K3-E25]. Not usable as `[quoted]`.

## H. Mental-model card (10 lines max)

- Variables cared about most: a right-or-wrong signal grounded in consequences; scaling with compute versus human-supplied knowledge; learning while running; data from people or from the system's own experience.
- Habitual heuristics: one mechanism in the simplest setting first; a model predicts what happens after an action, not pixels; the hard problem nobody will do over the demo.
- Red lines: will not accept a claim on authority; will not treat imitation as the basis of learning; will not accept aligning AI to human values as the frame; will not split training from deployment.

## I. Experience → lesson

| Experience (with source) | Lesson drawn | What the person judged with it | Where the analogy may break |
|---|---|---|---|
| Found Klopf's work in the Stanford library, wrote to him, got a lunch and a place on a UMass project with about five years of funding and almost no deliverables (§A, K3-E03) | A neglected, obvious principle held long enough can win; basic research needs years without delivery pressure | Decades on RL and TD regardless of fashion; starting Oak Lab small, with like-minded hires (K3-E16) | Almost nobody worked on it then and such funding is rare now; a student without tenure or a reputation cannot wait as long |
| TD learning drawn from how animals learn; TD-Gammon; AlphaZero used TD in his account (§B, K3-E12, K3-E13) | Simple principles from psychology become general algorithms, and they win | Core evidence for the Bitter Lesson; general learning and search over hand-built knowledge | Backgammon and Go have clean simulators and clear rewards; messy real-world or robot tasks are an extrapolation |
| Simulator-trained agents beat humans but did not cross the sim-to-real gap; the field moved to human data; 2026-08: synthetic data called a big mistake (§B, K3-E14, K3-E16) | Any simulation is tiny next to the world; simulator-trained policies transfer poorly | Opposes simulation and synthetic data as the main source of knowledge, and video-frame generation as a world model | His examples are rule-bound; a 2021 paper trained quadruped walking policies in minutes in simulation and deployed them on a real robot (K3-E34) |
| Physical Atari at Keen: a policy learned on one robot did worse on a second robot of the same design in all six games, and continued learning on the new body improved two (K3-E17) | Even identical robots differ; agents must keep correcting their model after deployment | Online learning after deployment over frozen policies or imitation of demonstrations | Two robots, six games, an early company prototype; no simulation or human-data comparison |
| DeepMind's Edmonton lab (2017–2023) closed in Alphabet's 2023 cuts; the team was freed and had not been entirely its own master (§A, K3-E06, K3-E08) | Big-company support is both fragile and constraining | Who is master when choosing an organization: a small group (2023), then his own firm (2026) | AlphaZero and MuZero came from DeepMind (K3-E13, K3-E35): a big lab is not necessarily unfree |

## Changes from the previous version

First public version, ported from an earlier private version. Roles, departures and foundings dated 2025-07 or later were re-checked on 2026-11-14; unconfirmed claims were dropped or flagged in `sources.csv`.
