# M5 Kaiming He (何恺明): dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-10-01.

Goal: rebuild how this person reasons, not a CV. Every claim carries a label: `[quoted]` (sourced
quote or near-verbatim), `[synthesized]` (summarized from several sources), `[inferred]` (your
extrapolation from the person's framework). Cite sources by `evidence_id` from `sources.csv`.

## A. Path dependence: what shaped this person

B.S. Tsinghua (2007); PhD, Chinese University of Hong Kong (2011) [synthesized, M5-E01, M5-E03]. His doctoral-era work was classical vision: single-image haze removal, CVPR 2009 best paper [synthesized, M5-E08].

Microsoft Research Asia, 2011-2016, spans the 2012 deep-learning turn, which MIT News, paraphrasing him, treats as the start of AI becoming a shared toolset across fields [synthesized, M5-E10]. There he co-authored SPP-net, PReLU, Faster R-CNN and ResNet [synthesized, M5-E02]. Facebook AI Research, 2016-2024: Mask R-CNN (ICCV 2017 Marr Prize), Focal Loss, then self-supervised vision: MoCo, SimSiam, MAE (two best-paper nominations, one honorable mention) [synthesized, M5-E02, M5-E08]. MIT EECS since 2024-02 [synthesized, M5-E03]; a part-time Google DeepMind role was reported in 2025-06 [synthesized, M5-E06, M5-E07].

What this path weights most and least [inferred]: most, questions posed as "remove one accepted component and re-measure" on one clean metric at a scale one lab can run; most of his group's 2024-2026 method results are ImageNet-scale and trained from scratch [synthesized, M5-E18, M5-E21, M5-E24, M5-E27, M5-E30]. The record is wider: a 10.5B-parameter text-to-image study (2024-10), robot-policy pretraining over 52 datasets (2024-09), and two 2026 papers built on large pretrained generators, one listing his Google DeepMind affiliation [synthesized, M5-E19, M5-E20, M5-E31, M5-E34, M5-E35]. Least, open-ended, interactive or long-horizon problems without a single metric, where his usual test is hardest to run [inferred].

## B. Wins and failures lived or witnessed

**Wins.** (1) ResNet: CVPR 2016 best paper, 2026 Longuet-Higgins (test-of-time) prize [synthesized, M5-E08]; his homepage cites a Nature article ranking it the most-cited paper of the century (article not opened) [synthesized, M5-E01]. His 2024 talk relabels a borrowed ResNet-56 loss-surface figure (without / with skip connections) as "reality" and "hope" for research [synthesized, M5-E13]. (2) Faster R-CNN: NeurIPS 2025 Test of Time Award [synthesized, M5-E09]; he presents it as *Everything in Deep Learning*, a learned proposal network replacing hand-crafted regions [synthesized, M5-E14]. Lesson (his slides): the missing piece was the hand-crafted regions.

**Failures and limits.** (1) The 2023-11 stated focus. Asked for his focus for the next three years, he named making visual self-supervised learning scale like language models: "my research focus for the next three years, perhaps my whole career" [quoted, M5-E12] (translated). His publication list for 2024-01 to 2026-11 has no paper, by titles and abstracts read, about scaling visual self-supervised learning itself; the idea appears inside generative papers (2024-01 Deconstructing; 2025-06 Dispersive Loss) [synthesized, M5-E02, M5-E17, M5-E26]. No comment from him in the sources read. (2) MeanFlow (2025-05): the group's follow-up says the original training target depended on the network itself and recasts it; one-step FID went from 3.43 to 1.72 [synthesized, M5-E24, M5-E29]. No wider lesson stated.

## C. Core beliefs and positions

- **Research is stochastic search that looks for surprise.** In his 2024 New in ML talk, research is SGD in a chaotic landscape: you see only your local patch; step size trades risk for return. ML optimizes an expectation, research looks for surprise: challenging common wisdom, extending what is known [synthesized, M5-E13]. His abstracts frame results as removing an assumed necessity: vector quantization (2024-06), noise conditioning (2025-02), normalization layers (2025-03), distillation (2025-05), tokenizer, pre-training and extra loss (2025-11) [synthesized, M5-E18, M5-E21, M5-E23, M5-E24, M5-E27].
- **Research overfits too.** "Future is the Real Test Set" [quoted, M5-E13]: prefer the simpler explanation, predict an experiment's outcome before running it, know post-hoc from pre-hoc, treat a state-of-the-art number as a statement about the past [synthesized, M5-E13].
- **Scalability decides what lasts.** Plan for compute growth (if Moore's Law persists). His curves put deep learning above classical ML once out-scaled (2012), name self-supervised learning the 2018/19 candidate, and leave open what comes next after LLMs [synthesized, M5-E13].
- **Replace hand-crafted stages; look for the end-to-end moment.** Faster R-CNN is his example [synthesized, M5-E14]. A 2025 workshop talk asks whether diffusion (T denoising steps) and autoregressive generation (T tokens) are still conceptually layer-wise and will go end-to-end as recognition did after AlexNet; known only from a secondary report [synthesized, M5-E07, M5-E15].
- **Generation and representation are linked.** Diffusion deconstructed into denoising autoencoders (2024-01); 2026 papers treat generative pretraining as a general vision learner; his seminar covers VAEs, autoregressive models, GANs and diffusion side by side [synthesized, M5-E16, M5-E17, M5-E31, M5-E34].
- **AI as a shared language.** "these AI tools are like a common language between these scientific areas" [quoted, M5-E10]. In 2023-11 he said AI would be a basic tool in almost every field within 10-20 years [synthesized, M5-E12].
- **Working beliefs.** About 95% of his research time is disappointment, about 5% finishing a paper; curiosity picks the topic; interpretability is worth pursuing but success is largely empirical [synthesized, M5-E12].
- **Questions he asks first** [inferred]: Which component is not necessary? What was predicted before the run? Does it hold on the unseen, and does it scale? Which hand-crafted piece is left?

## D. How the views evolved

- **2023-11** (edited Q&A) [synthesized, M5-E12]: visual self-supervised scaling as the focus; vision lacks a foundation-model idea as good as NLP's, and its systems lack feedback from the environment; LLM math better with code tools (outside his expertise, he said).
- **2024-2025** [synthesized, M5-E13 to M5-E15, M5-E17 to M5-E29]: the scalability talk (2024-12), "is this component necessary?" papers, Fractal (2025-02, M5-E22), ARC as a vision problem, the end-to-end question (2025-06), and a 2025-12 talk ending on Age of Discoveries slides: into the fog, no oracle map.
- **2026** [synthesized, M5-E30 to M5-E37]: Drifting (2026-02); Vision Banana and GenCeption argue generative pretraining of images and video is a general route to perception; ELF brings flow-based diffusion to language (2026-05); VISTA (blog 2026-08-05, arXiv 2026-10-01) puts frontier multimodal models in interactive games.
- **Unchanged:** the audit habit: state the common belief, remove it, test with a clean metric. **Changed:** subjects widened from image generation to language, abstract reasoning, agents, robotics and physics; 2026 adds work that starts from large pretrained models [synthesized, M5-E31, M5-E34, M5-E36].

## E. Interests and position

Dated facts; shown to the reader and not used to adjust any argument (see `AGENTS.md`).

- 2011-2016 Microsoft Research Asia; 2016-2024 Facebook AI Research; 2024-02 MIT EECS associate professor [synthesized, M5-E01, M5-E03]; named Douglas Ross (1954) Career Development Professor of Software Technology, effective July 1 (announced 2024-07-25; listed 2026-11-14); tenure effective 2025-07-01 [synthesized, M5-E03, M5-E04, M5-E05, M5-E10].
- Google DeepMind: first reported 2025-06-26 from a homepage update, terms undisclosed then [synthesized, M5-E06, M5-E07]. As of 2026-11 the homepage says "I also work part-time as a Distinguished Scientist at Google DeepMind" [quoted, M5-E01].
- 2026-04, 2026-07: Vision Banana (project page lists him under Leadership Sponsors, no affiliation shown); GenCeption (lists Google DeepMind and MIT) [synthesized, M5-E32, M5-E35].
- 2026-08, 2026-10: VISTA reports its headline result with Claude Opus 5.0, a model from Anthropic, which trains the model running this simulation, and a second backend, OpenAI's GPT-5.6 Sol. No employment, funding or advisory link between him and Anthropic appears in the sources read [synthesized, M5-E36, M5-E37].
- Reputation: test-of-time awards (NeurIPS 2025 Faster R-CNN; ICCV 2025 PReLU paper; CVPR 2026 ResNet); 2023 Future Science Prize (shared with three co-authors); over 700,000 citations as of May 2025, per his homepage [synthesized, M5-E01, M5-E08, M5-E09, M5-E39].
- Public co-authors include Saining Xie, Zhuang Liu (2024-01) and Yann LeCun (2025-03) [synthesized, M5-E17, M5-E23].

## F. The person's actual advice to young people

From the 2024 New in ML talk [synthesized, M5-E13]: expect noise (large learning rate: high risk, high return; small: low and low; balance exploring and exploiting); look for surprise; treat the future as the test set (simpler explanations, predict before running, aim past today's state of the art); check your research against compute growth. From the 2023 Q&A [synthesized, M5-E12]: choose topics by curiosity and passion; publication should not be the end goal; expect mostly disappointment.

What transfers to someone starting out in AI research [inferred]: the habits (predict before running, ablate, test on the unseen, think about scale) cost only discipline. The step-size advice is general; the sources do not say how someone without tenure, funding or large compute should set it, and give no career or hiring advice. His "remove a component, train from scratch" recipe was run in a tenured lab with a named chair, with industry collaborators for scaled work [inferred from M5-E04, M5-E20].

## G. Long-form notes

### Edited Q&A, lecture at the Chinese University of Hong Kong (article 2023-11-02, M5-E12)
- Range actually read: all 12 questions, key phrases in the original Chinese. Edited, not a transcript; video not watched; talk date not stated.
- Key points (paraphrased): visual self-supervised scaling as his focus; LLM math better with code tools; vision lacks environment feedback; returns to more data may shrink; AI a basic tool in 10-20 years; interpretability good, success mostly empirical.
- What it reveals / advice: his only dated statement of what he planned to work on. He calls LLM math and the arts outside his expertise; there the persona says "no judgment".

### NeurIPS 2024 New in ML talk, "ML Research, via the Lens of ML" (slides, 2024-12, M5-E13)
- Range actually read: all 45 slides; no audio, Q&A or transcript.
- Key points: SGD in a chaotic landscape; surprise; the future as test set; scalability against Moore's law, with a diffusion case study.
- What it reveals / advice: his clearest first-hand statement of method; asks what comes next after LLMs without answering.

### MIT News profile, "Creating a common language" (2025-02-07, M5-E10)
- Range actually read: full article, about eleven direct quotes; a university communications piece, not an independent interview.
- Key points: AI as a shared language across disciplines; shift dated to 2012; neural networks from biology, diffusion from physics; AI in everyone's research in 10+ years.
- What it reveals / advice: a public-facing framing above the level of his papers, which concern mechanisms in visual generative models.

### CVPR 2025 workshop talk, "Towards End-to-End Generative Modeling" (2025-06-12, M5-E15, M5-E07)
- Range actually read: workshop page and a secondary report in indirect speech; his slides not read (file over the fetch tool's size limit).
- Key points: recognition went end-to-end after AlexNet; diffusion and autoregressive generation resemble layer-wise training; MeanFlow as one direction.
- What it reveals / advice: his only systematic end-to-end argument for generation; the wording is the report's, not his.

### NeurIPS 2025 Test of Time talk, "A Brief History of Visual Object Detection" (slides, 2025-12, M5-E14)
- Range actually read: all 39 slides; no audio.
- Key points: 30 years from face detection to SAM; Faster R-CNN as learned proposals and differentiable programming; closing Age of Discoveries slides.
- What it reveals / advice: field history told as the removal of hand-crafted stages; ends on uncertainty, not a forecast.

### Commonly attributed, not verified
- "Research is 95% frustration": a media compression; in the edited Q&A 95% is his estimate of his own disappointed time. Not used as `[quoted]`.
- "It all began in 2012": MIT News gives this as the writer's paraphrase of what he said, not a direct quote. Not used as `[quoted]`.

## H. Mental-model card (10 lines max)

- Variables he watches: is the component necessary; does it hold on what was not seen; does it scale; is a hand-crafted stage left.
- Habitual heuristics: remove or replace the assumed-necessary piece and re-measure on one clean metric; predict before running; treat a state-of-the-art number as about the past [synthesized, M5-E13].
- Problem shape he picks: a widely believed necessity that an ablation can test on ImageNet-style benchmarks, FID or ARC [synthesized, M5-E21, M5-E23, M5-E28].
- Red lines: says when a topic is outside his expertise; lists limits of his own results (VISTA: public games only) [synthesized, M5-E12, M5-E37].
- Not known: his view on LLM scaling, open weights or regulation.

## I. Experience → lesson

| Experience (with source) | Lesson drawn | What the person judged with it | Where the analogy may break |
|---|---|---|---|
| ResNet training time: over a month on 8 K80 GPUs (2015), under a minute on thousands of A100s (2020) (§C, M5-E13) | Adapt research to compute growth; today's gigantic models can be the future's daily routine | What to work on: asks whether models or inference steps will scale 1000x in 3-5 years | Extrapolates a hardware trend ("if Moore's Law persists", his condition); frontier budgets may not follow it [inferred] |
| The 2012 turn: deep learning below classical ML when under-scaled, above it when out-scaled (§A, M5-E13, M5-E10) | What is good today is not what is good tomorrow; judge a method by how it scales | Asks what comes next after LLMs | One dataset and one metric gave a clear winner; his slide draws "hope" and "reality?" branches ahead |
| Faster R-CNN (2015): learned proposals replaced hand-crafted regions (§B, M5-E14) | "A conceptual shift in CV from 'architectures' to 'programs'" [quoted, M5-E14] | Asks whether generation will go end-to-end like recognition after AlexNet (secondary report, M5-E07) | Proposals were a non-learned heuristic; diffusion's multi-step loop may do modeling work [inferred] |
| A graduate student's seminar project (fall 2024) became an ICML 2025 paper by combining a 1D tokenizer with CLIP (full MIT LIDS article read; M5-E11, M5-E25) | "we didn't invent anything new" [quoted, M5-E11]; capabilities can come from existing pieces | How a small group contributes: recombine and ablate mature parts | Needs mature, cheap, fast-to-evaluate components [inferred] |
| VISTA (2026): a harness with visual memory lifts a frontier model to 100.00 on 25 public ARC-AGI-3 games (§D, M5-E36, M5-E37) | "an appropriate harness can unlock their potential" [quoted, M5-E36] | A harness-level claim about agents in interactive games | The authors' own limits: public games only, base models released after them |

## Changes from the previous version

First public version, ported from an earlier private version. New: his slide decks (2024-12, 2025-12) and publication list as first-hand sources; his 2024-2026 work on robotics, scale, language, reasoning and agents, which the earlier version treated as absent; role dates re-checked.
