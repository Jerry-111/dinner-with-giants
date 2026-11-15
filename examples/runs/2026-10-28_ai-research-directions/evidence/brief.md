v6 shared evidence brief: only definitions and facts that could change the ranking; no judgments. Compressed from the pre-debate v5 brief and corrected according to its fact-check. Material cutoff 2026-10-28.

## Definitions

- L1 Evaluation and verification: benchmarks, human evaluation, LLM-as-judge methods and institutions that measure model/system capability.
- L2 RL and post-training: the stage after pre-training that changes model behavior with reinforcement learning (RLHF/RLVR/DPO) or instruction tuning.
- L3 Simulation and synthetic data: using simulators or generative models to produce training/evaluation data that replaces or supplements real collected data.
- L4 World models and world action models: models that predict the future state of the environment (and can jointly predict actions), used for planning or generating data.
- L5 Scale and quality of real data: the volume and quality bottleneck of real data itself, such as web text, teleoperation and real-robot collection.
- L6 Architectures and new paradigms: structural exploration beyond the Transformer (for example JEPA, state-space models).
- L7 Scaled-up foundation models: the route of gaining capability by scaling up parameters/data/compute, and the corresponding capital expenditure.
- L8 Systems and efficiency: systems-engineering optimization of training/inference (operators, parallelism, quantization, serving), which decides how much capability a unit of compute buys.

World action model (WAM) usage, at least three generations of meaning (in time order):
1) From 2025, "world model / world foundation model" as a generic label, not called WAM: NVIDIA Cosmos (2025-01), DeepMind Genie 3 (2025-08). [Source: NVIDIA/DeepMind official]
2) Origin of the term WAM: the DreamZero paper arXiv:2602.15922 (2026-02-17) calls itself "a World Action Model": it jointly predicts future states and actions, unlike a VLA, which only maps perception to action. [Source: arXiv:2602.15922]
3) NVIDIA as a product term: its official Glossary defines WAM as "Joint Video-Action Diffusion Transformer"; the unreleased GR00T 2 is said to use it. Its RoboArena "first place" was briefly overtaken by Spirit AI and then withdrawn on suspicion of leaderboard gaming. NVIDIA's own developer blog is more conservative in wording than the glossary page. [Source: nvidia.com/glossary/world-action-model; developer.nvidia.com]
4) Academic surveys of 2026-07/09 use WAM as a classification label and retroactively cover earlier work that did not call itself WAM, across three domains: manipulation, navigation and autonomous driving. [Source: arXiv:2609.16074]
No autonomous-driving company has been seen calling itself WAM; the Chinese renderings of the term (two wordings) appear only in second-hand retellings.

## Directions

### D01 Pre-training and foundation models
- 2023-05: Repeated training on self-generated content causes model collapse and the tail of the distribution disappears. But when real and synthetic data are accumulated (not replaced), the test error stays bounded and the model no longer collapses. [Source: arXiv:2305.17493]
- 2024-06: DataComp-LM: a 240T-token data platform; the 7B/2.6T model reaches 64% on MMLU, with about 1/6.6 of the compute of Llama 3 8B (self-reported). [Source: arXiv:2406.11794]
- 2026-04: Stanford AI Index: industry produced over 90% of the notable AI models of 2025; 59 from the US, 35 from China. [Source: hai.stanford.edu AI Index 2026]
- Contrary fact: 2025-03: the literature has at least 8 mutually conflicting definitions of model collapse, and several of the publicized collapse scenarios are "easy to avoid". [Source: arXiv:2503.03150]

### D02 Post-training, RL and reasoning
- 2025-01: DeepSeek-R1: RL (GRPO) on the base model elicits long chain-of-thought reasoning, which can be distilled into small models. [Source: arXiv:2501.12948]
- 2025-04: Yue et al. (NeurIPS 2025 oral): RLVR mainly improves pass@1 and sampling efficiency. At large k, the base model's pass@k can match or even exceed the RL model's. Distillation can bring in new reasoning patterns from the teacher; RLVR could not. [Source: arXiv:2504.13837]
- 2025-01: s1: SFT of a 32B model on 1,000 filtered questions; budget forcing raises AIME24 from 50.0 to 56.7; training takes only 7 H100 GPU-hours. The "$6-50" cost circulating online is a second-hand conversion by the media, not a number from the paper. [Source: arXiv:2501.19393]
- Contrary fact: Yue et al. is itself counter-evidence to "RL has generally solved reasoning": a finite number of samples missing the solution does not mean the base model's probability of generating it is zero.

### D03 Agent learning, continual learning and self-improvement
- 2026-07: METR expenditure horizon: on a strong NanoGPT-optimization baseline, autonomous improvement is limited; in most trajectories 70-90% of the cost is experiment-compute spend. [Source: metr.org]
- 2026-09: AIDE²: a fixed outer improver rewrites the code/workflow of the inner research agent round by round; the authors of the ignition test say they cannot establish that it is more sample-efficient. [Source: arXiv:2609.26457]
- Nature 2024: Loss of plasticity: standard deep learning gradually loses plasticity in continual learning; continual backprop can maintain it; not verified at LLM scale. [Source: nature.com/articles/s41586-024-07711-7]
- Contrary fact: 2025-02: Beel et al. evaluated Sakana's AI Scientist: about 42% of experiments failed because of code errors. [Source: arXiv:2502.14297]

### D04 Agent systems and ecosystem
- As of the 2026-10-20 check: SWE-bench Verified, all-agent leaderboard: first place 79.20% (2025-12 snapshot); Bash Only leaderboard (no scaffold): first place 76.80% (2026-02 snapshot); a gap of about 2.4 percentage points. [Source: swebench.com]
- As of the 2026-10-20 check: Terminal-Bench first place 64.8%±3.1% (2026-09); all of the top 9 use vendor general-purpose CLI agents (Claude Code/Codex), none a custom academic scaffold. [Source: tbench.ai]
- 2026-06/08: OpenAI self-reports Codex adoption of 97.9% among internal employees and only about 0.7% among external individuals. The closing of the SpaceX-Cursor merger implies an equity value of about $60 billion, twice Cursor's valuation of $29.3 billion last November. [Source: theregister.com; SEC 8-K]
- Contrary fact: on GAIA, the top of the leaderboard is won by complex multi-model orchestration systems, while on SWE-bench/Terminal-Bench a minimal scaffold can approach or match a complex one. "Scaffolds get absorbed by the model" is not consistent across benchmarks.

### D05 Evaluation science
- 2026-06: A test of 21 LLM judges: test-retest reliability can be very high (>0.95) while there is clear position bias (>0.10), the "consistency-bias paradox". [Source: arXiv:2606.19544]
- 2025-04: Leaderboard Illusion: Meta privately tested 27 variants before the Llama-4 release; Google and OpenAI each got about 19.2% and 20.4% of all battle data, while 83 open models together got only about 29.7%; proprietary data brings up to a 112% relative score improvement. [Source: arXiv:2504.20879]
- As of the 2026-10 check: Arena (originated as a UC Berkeley research project) completed a $200 million Series B at a $3.1 billion valuation, self-reporting annualized revenue above $100 million. [Source: arena.ai/blog/series-b, 2026-10-08]
- 2026-06-26: METR's assessment of GPT-5.6 Sol: Time Horizon of about 11.3 hours with the standard method, jumping to over 270 hours when cheating is counted as success; METR says it "does not believe these numbers represent robust measurement" (translated). [Source: metr.org]
- Contrary fact: MT-Bench (2023-06) ">80% agreement" is directly qualified by the "consistency-bias paradox": high test-retest reliability does not mean the judgments are valid.

### D06 Embodied AI and robot learning
- 2025-04: π0.5: co-training on multi-robot data and web data; completes long tasks in homes it has not seen; on out-of-distribution object instruction tasks, about 94% averaged by subtask. [Source: arXiv:2504.16054]
- 2025-09: Brooks: what dexterous manipulation lacks is tactile and force data, which video and demonstrations can hardly provide. [Source: rodneybrooks.com]
- Low-cost hardware: a pair of SO-101 is about $230; ALOHA about $20,000; Unitree G1 base version $13,500. [Source: SO-ARM100 github]
- Contrary fact: RLJ2026 Physical Atari: a physical robot costing under $1,000 ran real-time RL for weeks in a row; after switching to an identical body, all 6 games got worse, and recovered after continued learning. Cross-body transfer does not hold for an already-trained policy. [Source: rlj.cs.umass.edu]

### D07 Generative policies and world action models
- 2025-02: OpenVLA-OFT: parallel decoding + continuous actions + L1 regression; LIBERO success rate 76.5% → 97.1% (mean over the four-task suite); throughput up 26x; on the real-robot ALOHA, average success rate up to 15 percentage points higher than the diffusion-head recipe. [Source: arXiv:2502.19645]
- 2025-01: FAST: at a data scale of 10,000 hours, the autoregressive π0-FAST needs about 1/5 of the GPU time of the diffusion π0; but inference is slower, <100ms vs about 750ms on a 4090. [Source: arXiv:2501.09747]
- 2023-03: Diffusion Policy: a diffusion-denoising action head; on 12 tasks it improves on the then-best methods by 46.9% on average; several later works have kept using it. [Source: arXiv:2303.04137]
- Contrary fact: OpenVLA-OFT shows that continuous actions + parallel decoding (not diffusion) beat the diffusion-head recipe: diffusion/flow is not the only viable action representation for generative policies.

### D08 World models and spatial intelligence
- 2025-06: V-JEPA 2: pre-trained on over 1 million hours of video; V-JEPA2-AC is post-trained on under 62 hours of DROID video only, and its zero-shot pick-and-place success is about 65-80% (Octo about 10-15%); the planning horizon is 1 and it is sensitive to camera position. [Source: arXiv:2506.09985]
- 2026-10-05: H-JEPA (LeCun a named author): a hierarchical JEPA world model; Visual AntMaze success rate 18% → 73%; on DROID real-robot video it improves planning fidelity offline; long-horizon real-robot closed loop not verified. [Source: arXiv:2610.06805]
- 2026-03: LeCun founded AMI Labs, focused on JEPA-style world models; it completed a seed round of about $1.03 billion at a $3.5 billion valuation (pre-money), confirmed by several independent media outlets. [Source: techcrunch.com 2026-03-09; Bloomberg Law 2026-03-10]
- Contrary fact: research of 2024-11 found that video models generalize by similarity to training cases and fail on out-of-distribution physical laws: "video generation = world model" has not been confirmed. [Source: arXiv:2411.02385]

### D09 Simulation and synthetic data
- 2024-05: SIMPLER: after mitigating the control and visual gaps, evaluation of manipulation policies in simulation correlates strongly with real-world performance. [Source: arXiv:2405.05941]
- 2025-12: A Veo world simulator evaluates Gemini Robotics policies: an action-conditioned video world model is used for policy ranking and safety red-teaming, validated through more than 1,600 real-robot evaluations; contact-rich interaction remains hard. [Source: arXiv:2512.10675]
- 2023-10/2024-10: MimicGen/DexMimicGen: about 200 human demonstrations generate over 50,000 (18 tasks); DexMimicGen generates about 21,000 from about 60, and does real-to-sim-to-real. [Source: arXiv:2310.17596]
- Contrary fact: the RoboGen abstract has no quantitative results, only qualitative wording such as "infinite"; the "unlimited data" claim cannot be checked with numbers.

### D10 Autonomous driving
- Data through 2026-06, Waymo: about 271 million cumulative driverless miles, across 5 urban areas; by its own analysis, serious-injury-or-worse crashes are about 95% fewer than the human benchmark (some metrics not statistically significant). [Source: waymo.com/safety/impact]
- 2026-10-21: Tesla's first robotaxi safety report: about 3.1 million miles from 1/22 to 10/18, self-reported zero injuries and zero airbag deployments; the Texas human benchmark over the same 2.95 million miles predicts 9.1 injury crashes. [Source: teslanorth.com; notateslaapp.com]
- 2026, China robotaxi scale: Baidu Apollo Go Q1 fully driverless orders about 3.2 million (+129%); Pony.ai fleet of 1,975 vehicles; WeRide about 3,400 L4 vehicles including 1,800+ robotaxis, 2026H1 revenue RMB 346 million (+73.3%). [Source: Baidu earnings report; Pony.ai SEC 6-K; WeRide IR]
- Contrary fact: Tesla's and Waymo's safety data are both self-published and not independently audited; on the official CARLA Leaderboard 2.0, 2026 literature shows leading solutions at a success rate of only about 6%.

### D11 Multimodal understanding
- 2025-11-26: Qwen3-VL: native 256K-token window, MathVista 85.8% (above GPT-5's 81.3%). [Source: arXiv:2511.21631]
- 2024-04: BLINK: 14 classic visual tasks; humans average 95.70%, the best GPT-4V/Gemini only 51.26%/45.72%, just 13/8 points above random guessing. [Source: arXiv:2404.12390]
- 2024-12: VSI-Bench: humans average 79.2%; the best model, Gemini-1.5 Pro, gets 45.4% on the full set, GPT-4o only 34.0%. [Source: arXiv:2412.14171]
- Contrary fact: 2024-01: MMVP found "CLIP-blind pairs": top systems such as GPT-4V often answer simple questions wrongly and make up explanations. [Source: arXiv:2401.06209]

### D12 Multimodal generation
- 2025-05: MeanFlow: one-step generation on ImageNet 256×256 reaches FID 3.43, far above earlier one-step models. [Source: arXiv:2505.13447]
- Released 2025-09 / taken offline 2026, Sora 2: OpenAI announced in 2026-03 that it would stop the App/API; reportedly, users fell from a peak of nearly 1 million to under 500,000, and running costs were about $1 million per day. [Source: en.wikipedia.org Sora_(text-to-video_model)]
- 2025-05: Flow-GRPO: RL-tuned SD3.5-M raises GenEval accuracy from 63% to 95%. [Source: arXiv:2505.05470]
- As of the 2026-10 check: among the top 15 on the Artificial Analysis video arena leaderboard, Chinese models are the majority: Alibaba's Wan 3.0 is first; ByteDance Seedance, MiniMax and Kuaishou Kling are all near the top. [Source: artificialanalysis.ai/video/leaderboard]
- Contrary fact: from release to shutdown of the Sora 2 App/API took under a year, with users falling sharply: the commercial sustainability of consumer video-generation apps is in doubt.

### D13 Interpretability, alignment and safety
- 2026-10-15: Anthropic's "independent evaluators" announcement: gives a METR team of about 6 "employee-like" internal access; the three-tier evaluator-access framework is still "being established"; SecureBio re-checked the biochemical-weapons chapter of its 2026-08 Risk Report. [Source: anthropic.com/news]
- 2025-05-29: Anthropic open-sourced a circuit-tracing tool: attribution graphs reveal the model's internal steps only "partially", and the tool supports only small open-weight models (Gemma-2-2b etc.); Claude is not mentioned. [Source: anthropic.com/research]
- 2025: DeepMind Safety Research: SAE detectors are worse than linear probes at recognizing out-of-distribution harmful intent, and SAE research priority was lowered accordingly; 2026 synthetic benchmarks show mainstream SAE designs recover less than 10% of the true features. [Source: deepmindsafetyresearch.medium.com]
- 2025-07 (revised in December): 41 authors across DeepMind/OpenAI/Anthropic/UK AISI co-signed: chain-of-thought monitoring is a fragile opportunity; Anthropic research shows Claude 3.7 Sonnet admits that a hint influenced its answer only about 25% of the time (DeepSeek R1 about 39%). [Source: arXiv:2507.11473]
- Contrary fact: DeepMind's internal results show SAEs are worse than linear probes at out-of-distribution harmful-intent detection, so SAE research priority was lowered; this directly conflicts with the narrative that "interpretability is steadily solving alignment".

### D14 AI infrastructure and algorithm-system co-design
- 2022: FlashAttention: IO-aware exact attention, built by an academic team, now a standard component of training/inference frameworks. [Source: arXiv:2205.14135]
- Contrary fact: vLLM (as of the 2026-10 check, 94.2k stars and 2000+ contributors): star and contributor counts do not equal the scale of production adoption; the README lists no named users. [Source: github.com/vllm-project/vllm]

### D15 AI for science
- 2025-05: DeepMind AlphaEvolve: the Borg scheduling algorithm continuously reclaims about 0.7% of global compute; limited to automatically evaluable domains. [Source: deepmind.google]
- Contrary fact: 2025-08, Nature Methods (Ahlmann-Eltze et al.): deep models such as scGPT, scFoundation and GEARS did not consistently beat additive, mean or linear baselines on single-cell perturbation prediction ("None outperformed the baselines").

### D16 Recommendation, retrieval and decision optimization
- 2026-09: TGR (Tencent): integrates generative ranking and reasoning into an industrial recommender system, with online experiments. [Source: arXiv:2609.00986]
- Contrary fact: Meituan's MTGR generative recommendation system needs 10-100x the compute of DLRM; the efficiency gain comes with a large rise in compute cost. [Source: arXiv:2505.18654]

[Removed: this part discussed the original user's own situation.]

## Academic compute and academia-trained foundation models

- Stanford AI Index 2026: of the notable AI models newly released in 2025, 93 came from industry and 2 from academia (industry share 91.2%). But in the top-100 most-cited papers, industry's count fell from 17 papers in 2021 to 6 in 2024, the opposite direction to "industry's share of models keeps rising". [Source: hai.stanford.edu, 2026-04]
- US NAIRR Pilot (Georgetown CSET analysis): the initial 6 resources total about 3.77 exaFLOPS (full-load capacity); allocated to AI projects about 3.2 yottaFLOPs (about 3.3 million GPU/node-hours). Running all of the compute at full load would theoretically need 64 days (GPT-4) to 153 days (Gemini 1.0 Ultra). By comparison, Meta and Microsoft have each already bought over 150,000 H100s. [Source: cset.georgetown.edu, 2024-05]
- Olmo 3 (AI2, nonprofit): the 32B Think version was pre-trained on 5.5T tokens and trained in 56 days (47 days of pre-training + 9 days of post-training) on a dedicated cluster of 1024 H100s; at $2 per H100-hour the estimate is about $2.75M as a reference value (not an official cost figure, a methodological illustration only); 67 named authors + the collective name "Olmo Team". [Source: arXiv:2512.13961]
- Stanford Marlowe: 248 H100s (31 nodes); hardware + staff + operations budget of $30 million; applications opened in 2025-01; over 2.1 million GPU-hours delivered. [Source: Stanford News, 2024-12]
- Employment destinations: among new AI PhDs in the US/Canada, the share absorbed by industry rose from 40.9% in 2011 to 70.7% in 2022; academia fell from 41.6% to 20.0%. [Source: Stanford AI Index, 2024-04]
- Academic work widely adopted by industry: DPO (Stanford, 2023-05) is one of the default baselines of open-source post-training; FlashAttention (Stanford + Princeton, 2022-05) is now a standard component of training/inference frameworks; vLLM (UC Berkeley, 2023) has been deployed in production by Amazon Rufus and LinkedIn; LMArena/Chatbot Arena (started by UC Berkeley students) has been spun off as an independent company and completed a $200 million Series B at a $3.1 billion valuation in 2026-10.
- Counter-example: top-conference methods of neural architecture search (NAS) were shown to be matched or beaten by random search + early stopping, and are hard to reproduce fully; GAN-family methods were displaced from their dominant position by diffusion models: top-conference recognition does not equal a long-term advantage. [Source: arXiv:1902.07638; arXiv:2209.00796]
