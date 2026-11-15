# M1 Percy Liang: dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-11-05.

Goal: rebuild how this person reasons, not a CV. Labels: `[quoted]` sourced quote, `[synthesized]` summary of
several sources, `[inferred]` extrapolation from the person's framework. Cite `evidence_id` from `sources.csv`.

## A. Path dependence: what shaped this person

MIT (BS 2004, MS 2005), then a UC Berkeley PhD (2011) [synthesized, M1-E01]. His early research was semantic parsing, mapping natural language to executable programs (a 2016 article, accepted to Communications of the ACM) [synthesized, M1-E04], then robustness; a 2022-01 podcast outline follows that order [synthesized, M1-E05]. [inferred] The habit this left: treat structure and checkable intermediate representations as the route to understanding a system.

The turn was GPT-3. In a 2022 recap he said emergent abilities in next-token models "caught me and also, I think, many researchers, by surprise" [quoted, M1-E08]; the recap's author says this led him to found CRFM [synthesized, M1-E08]. In 2021-08 he was last of 114 authors on the CRFM report that introduced the term foundation models, calling them "critically central yet incomplete" [quoted, M1-E06]; CRFM's launch announcement names him director [synthesized, M1-E03].

Later work, by date only: HELM (2022-11, first of 50 authors), Together AI (launched 2022-06), Alpaca (2023-03), Generative Agents (2023-04), Marin (begun 2024, public 2025-05), Simile (Series A 2026-02) [synthesized, M1-E07, M1-E09, M1-E12, M1-E14, M1-E31, M1-E22, M1-E26]. [inferred] Often a research framing came first and shared infrastructure or a company followed; no source read states a plan.

Alpaca's public demo was pulled shortly after release, citing "hosting costs and the inadequacies of our content filters" [quoted, M1-E12]; The Register reported it on 2023-03-21 [synthesized, M1-E13]. [inferred] Later releases carry written risk arguments (Cybench: public release should do more for security than harm [synthesized, M1-E16]; Marin publishes failed experiments [synthesized, M1-E31]); no source ties either to Alpaca.

[inferred] The framework favors method-level leverage, measurement and open process; his examples (FlashAttention, DPO, Alpaca, s1) are all cases where scale did not decide the result.

## B. Wins and failures lived or witnessed

**Wins.** (1) Evaluation as maintained infrastructure: HELM scored 30 models on 42 scenarios with 7 metrics [synthesized, M1-E07]; HELM Capabilities (2025-03) covers five scenarios and 22 models [synthesized, M1-E20]. (2) Low-compute results: Alpaca (2023-03) cost under $500 in API calls plus under $100 to fine-tune a 7B model on 8 A100s [synthesized, M1-E12]; in s1 (2025-01; he is 8th of 10 authors), 1,000 questions and 26 minutes on 16 H100s (about 7 GPU-hours) took Qwen2.5-32B-Instruct to 56.7% on AIME24 with budget forcing, from 50.0% without [synthesized, M1-E19]. He names FlashAttention and DPO as academic methods needing little compute [synthesized, M1-E15]. (3) Marin: the 8B base (2025-05-19) averaged 66.6 against 65.3 for Llama 3.1 8B on 19 tasks in the project's own runs [synthesized, M1-E22]; the 32B (2025-10-28) had the best mean rank of five models but a lower average than Qwen 2.5 32B (65.2 vs 68.1) [synthesized, M1-E23]; the 535B-A23B pretraining finished 2026-11-05 per the project's issue tracker [synthesized, M1-E32].

**Failures.** (1) Alpaca's demo (§A): the release page listed a content filter and output watermarking as mitigations and said they can be circumvented [synthesized, M1-E12]; no stated change of view found. (2) Transparency Index: average 37 (2023-10, 10 developers), 58 (2024 edition, 14), 40 (2025-12, 13 companies); the 2025 edition updated indicators and added four companies, all in the bottom half [synthesized, M1-E17, M1-E24]. The authors say practice is set mainly by each company's priorities, cite California and EU laws, and offer the Index for tracking disclosure under new rules [synthesized, M1-E24, M1-E25]. (3) Marin's runs: the 8B retrospective lists mid-run mistakes; the 32B run had repeated loss spikes, a diverged optimizer swap and GSM8k test questions in one cooldown dataset, all reported openly [synthesized, M1-E22, M1-E23].

## C. Core beliefs and positions

- "Open" has parts: Llama 3 and Mixtral are open-weight, not open-source, which needs the processing code and data [synthesized, M1-E18]. Open weights do not guarantee transparency: IBM and AI21 Labs, open developers, are very transparent; DeepSeek, Meta and Alibaba quite opaque; open developers are more transparent than closed ones on average [synthesized, M1-E24].
- Evaluation: "Current model evaluation is fundamentally broken." [quoted, M1-E18] He cites a study he co-authored in which 9 of 30 models gave enough information to judge their scores, and GPT-4 scoring perfectly on pre-2021 Codeforces problems and 0% on newer ones [synthesized, M1-E18]. Models sold as services need spec-sheet-style benchmarks [synthesized, M1-E08].
- Yardstick: "I don't think it is productive to use humans as the goal post anymore" [quoted, M1-E11]. Models are tools to be mapped for strengths and risks; debates over understanding can distract from urgent harms [synthesized, M1-E11].
- Academia invents methods that industry later scales and can be a neutral third-party evaluator [synthesized, M1-E15]; CRFM's mission should be decentralized [synthesized, M1-E08].
- No openness-safety trade-off: open models support safety research and auditing; policy should follow evidence of marginal risk [synthesized, M1-E18].
- Data: 5-7% of previously available training data was restricted in one year, 20-33% for valuable sources; he notes California's AB-2013 will require training-data disclosure [synthesized, M1-E18].
- Reproducibility: described in 2022 as a strong proponent, through CodaLab Worksheets [synthesized, M1-E05].
- Questions asked first [inferred]: What does this benchmark measure, and who set it? Can data, code and process be inspected? How much compute does validation take?

## D. How the views evolved

Before 2020: semantic parsing, then robustness (§A). After GPT-3 he stopped treating robustness as his main line: he could keep breaking systems, but "that's not where the action is" [quoted, M1-E15]. 2021-22: CRFM, the report, HELM; the 2022 recap's author says he was unsure whether CRFM would audit systems or advise lawmakers [synthesized, M1-E08]. 2023: he expected base models to need substantial capital and cloud training, and Alpaca-sized models to become fine-tunable on consumer hardware [synthesized, M1-E11]. 2024: the three-part account of openness and the evaluation critique [synthesized, M1-E18]. 2025: s1; Marin public; a brief on simulating human behavior with agents saying current architectures must go further before reliable use [synthesized, M1-E21]; the Index decline [synthesized, M1-E24]. 2026: Simile; the abstract of his ICLR 2026 Marin talk opens "As AI capabilities skyrocket, openness plummets" [quoted, M1-E29]; the 535B-A23B run [synthesized, M1-E32].

Unchanged [synthesized]: public process and reproducibility (CodaLab 2022; Marin 2025), evaluation as shared infrastructure (HELM 2022; HELM Capabilities 2025), academia as method-inventor and neutral evaluator. Changed: project scale (8B, 32B, then a 535B mixture of experts) and commercial roles (Together AI 2022; Simile 2026) [synthesized, M1-E32, M1-E09, M1-E27].

## E. Interests and position

Dated facts; shown to the reader and never used to reduce an argument's weight (see `AGENTS.md`).

- 2021-08 to 2026-11: CRFM director; Stanford computer science faculty (chair Thomas M. Siebel Professor of Machine Learning; Senior Fellow at Stanford HAI; bio line Associate Professor; the ICLR 2026 bio says Professor) [synthesized, M1-E03, M1-E01, M1-E02, M1-E29].
- 2022: AI2050 Senior Fellow, a Schmidt Sciences program (also a named Marin supporter, below) [synthesized, M1-E10, M1-E31].
- 2022-06; as of 2026-04: Together AI co-founder with Vipul Ved Prakash, Ce Zhang and Chris Ré; the company calls itself a full-stack AI platform; his current role is not stated in the sources read [synthesized, M1-E09, M1-E36, M1-E29].
- 2024; as of 2026-11: Marin co-creator with David Hall, primarily developed by Open Athena; supporters named: Google TPU Research Cloud, the Huang Foundation (GPUs), Siegel Family Foundation, Fulcrum Science, Schmidt Sciences [synthesized, M1-E31]; the 535B-A23B run used 11 NVIDIA GB200 NVL72 racks, 2026-08 to 2026-11 [synthesized, M1-E32].
- 2026-02; as of 2026-11: Simile co-founder and Chief Scientist, with Joon Sung Park and Michael Bernstein [synthesized, M1-E27]; $100M Series A led by Index Ventures, announced 2026-02-12 [synthesized, M1-E26]; the blog lists Andrej Karpathy and Fei-Fei Li among individual backers, and Fei-Fei Li co-authored s1 [synthesized, M1-E28, M1-E19]. Related research: Generative Agents (2023-04) and a 2025-05-20 brief [synthesized, M1-E14, M1-E21].
- 2026-07-30: Simile $200M Series B at a $2B post-money valuation, led by Greenoaks, with Index
  Ventures (lead of the Series A, above) and other investors participating [synthesized, M1-E37].
- No link to Anthropic, maker of the model running this simulation, was found in the sources read.

## F. The person's actual advice to young people

No advice addressed to people starting out was found in the sources read. Nearest evidence: CS336, co-taught with Tatsunori Hashimoto, has students build a language model themselves, from data preparation to evaluation [synthesized, M1-E30]. [inferred] From his stated positions: ask how much compute a project needs to show its value; treat evaluation as research; plan release risk and hosting before publishing a runnable artifact; keep experiments reproducible. Transfers to someone starting out in AI research: the compute filter and the evaluation and release habits. May not: Marin relies on granted TPU and GPU capacity and an institution behind it (M1-E31, M1-E32), and his low-compute examples come from 2023-2025 paradigms [inferred].

## G. Long-form notes

### CRFM's first year, recap of a CS224U podcast conversation (2022-06-30, M1-E08)

- Range actually read: full written recap by the other participant, Chris Potts; audio not heard.
- Key points: GPT-3 as the eye-opening moment; academia's interdisciplinary expertise as CRFM's founding idea; spec-sheet-style benchmarks; a decentralized mission.
- What it reveals: the 2021-22 framing, academic breadth plus transparency.

### AI2050 Community Perspective (2023, undated, M1-E11)

- Range actually read: full page, four questions, about 800 words.
- Key points: HELM as side-by-side comparison; models as tools; humans as goal post; shift from sheer size; Alpaca-sized fine-tuning on consumer hardware.
- What it reveals: a 2023 forecast on compute and deployment, scored in views §3.

### Generally Intelligent, episode 35 (2024-05-09, M1-E15)

- Range actually read: publisher's highlights page (about 1,100 words of edited excerpts); no transcript of the roughly hour-long episode.
- Key points: GPT-3 as the shift; leaving robustness; FlashAttention and DPO; neutral third-party evaluation; credit for content producers; more democratic value-setting.
- What it reveals: the low-compute and neutral-evaluator arguments in his words; no career talk.

### Air Street Press interview (2024-11-11, M1-E18)

- Range actually read: full written Q&A.
- Key points: open-weight versus open-source; evaluation broken; contamination; shrinking data commons; no openness-safety trade-off; Linux-style multi-stakeholder development; AB-2013.
- What it reveals: data transparency is the sharper concern in late 2024; compute is not discussed.

Also seen: the abstract and bio of his ICLR 2026 Marin talk, talk not watched (M1-E29); the outline of a January 2022 podcast, no transcript (M1-E05). None of these gives advice to someone starting out; §F is inferred.

### Commonly attributed, not verified

- "AI today is kind of like where we were with the internet in 1993": attributed on a third-party quote-collection page [M1-E34] to an AI2050 profile that, read in full, does not contain it [M1-E10]; no primary source found.
- "Benchmarks serve as the North Star for the AI community": in an AI-assisted recap of a talk, in the article's own voice [M1-E33]; not confirmed as his words.
- "We're living in a crisis in our ability to measure model quality": the recap quotes only the word crisis [M1-E33]; the full line is a direct quote only on the collection page [M1-E34].
- None may be used as `[quoted]`.

## H. Mental-model card (10 lines max)

All lines are [inferred] from §C and §G.

- Variables cared about most: whether claims about models can be checked (what a benchmark measures, train-test overlap, disclosure of data and compute) and whether research can be reproduced and run in the open.
- Habitual heuristics: split "open" into weights, code and data, and use transparency, before judging who is doing what; ask whether a contribution shows its value without much compute, which fits academia; read a benchmark as a statement about what the field should optimize; look for train-test overlap before believing a score.
- Red lines: treating open weights as transparency; treating "beats the human baseline" as the only progress measure; treating contamination or irreproducibility as a minor detail.

## I. Experience → lesson

| Experience (with source) | Lesson drawn | What the person judged with it | Where the analogy may break |
|---|---|---|---|
| GPT-3's abilities surprised him (2020); he dropped robustness as his main line, helped introduce the term foundation models, directed CRFM from 2021-08 (§A, §D; M1-E08, M1-E15, M1-E06) | When a method he did not expect works, move the agenda to it rather than defend the earlier line [inferred] | Whether to leave robustness; later, who defines measurement in a new paradigm [inferred] | Naming worked while the category was unclaimed; where others set definitions, the move differs [inferred] |
| Alpaca's demo pulled shortly after the 2023-03 release over hosting costs and content filters (§A; M1-E12, M1-E13) | A runnable artifact brings hosting cost and misuse exposure a paper does not [inferred] | Later release choices: Cybench's written rationale, Marin's public process (link inferred) | A 7B model behind a moderation API differs in risk from a 535B model [inferred] |
| Cheap results: Alpaca under $600 (2023), s1 in about 7 H100-hours (2025); FlashAttention and DPO as his examples (§B; M1-E12, M1-E19, M1-E15) | A method that shows value without much compute suits academia [synthesized, M1-E15] | His screen for what academia should work on | Two windows only; the s1 AIME24 gain is 2 of 30 problems, the paper lists scaling limits (M1-E19); his 2026 flagship uses 11 GB200 NVL72 racks (M1-E32) |
| Transparency Index averages 37, 58, then 40 (2023-10, 2024, 2025-12); indicators updated in 2025 (§B; M1-E17, M1-E24) | Disclosure follows company choices; scoring alone does not settle it; policy is a lever [synthesized, M1-E24, M1-E25] | Using the Index to track disclosure under new laws | Measures voluntary disclosure, with a changed indicator set and four new companies; scores under legal duties may move differently (M1-E24) |
| Marin's retrospectives report mistakes, loss spikes and GSM8k contamination in public (§B; M1-E22, M1-E23, M1-E31) | Open process, failures included, makes errors findable [inferred] | How Marin is run: experiments on GitHub, preregistered loss targets (M1-E29, M1-E31) | Runs so far are base models on granted compute; frontier-scale competitive or safety limits may restrict sharing [inferred] |

## Changes from the previous version

First public version, ported from an earlier private version. Corrections in the port: Index averages are one edition apart (58 in 2024, 40 in 2025); IBM and AI21 Labs are open developers; the 535B-A23B run finished 2026-11-05; Alpaca takedown reasons come from the primary page.

Fairness-review pass (2026-11-14): added the Simile $200M Series B (2026-07-30, M1-E37) as a
dated interest-line entry in §E and `card.yaml`; the round was omitted from the prior version,
which covered only the earlier Series A.
