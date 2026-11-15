# M5 Kaiming He: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-10-01.

## 1. Overall judgment

His 2024 slides draw each era as capability against scalability: deep learning sat below classical ML when under-scaled and above it once out-scaled (2012), self-supervised learning was the next candidate (2018/19), and what comes next after LLMs is left open [synthesized, M5-E13]. In visual generation his group tests diffusion, flow and autoregressive pipelines for assumed necessities (tokenizers, noise conditioning, distillation), mostly at ImageNet scale and from scratch [synthesized, M5-E18, M5-E21, M5-E24, M5-E27, M5-E30]. From late 2025 he adds abstract reasoning, language, agents and physics, and co-authors 2026 papers that start from large pretrained generators [synthesized, M5-E28, M5-E31, M5-E33, M5-E34, M5-E36]. His 2025-12 talk ends on Age of Discoveries slides (no oracle map), so forecasts here are framed as open questions [synthesized, M5-E14]. Anything beyond these is [inferred].

## 2. Judgment by area

| Area | Stage | Where growth comes from (or why it won't) | Time window | Who captures the value | Basis |
|---|---|---|---|---|---|
| Text models and reasoning | No stated view on text pretraining. 2023-11: an LLM alone is not a promising route to abstract math, code tools more so (not his area). 2025-11: ARC as a vision task, 60.4% on ARC-1 from scratch. 2026-05: a diffusion language model paper | Tools or visual priors over scale alone | Not stated | Not stated | [synthesized, M5-E12, M5-E28, M5-E33] |
| Digital agents | Early. VISTA (2026): a visual-memory harness lets frontier multimodal models play unfamiliar games, no weight updates | Harness design; base-model ability is a key factor, say the authors | Not stated | Not stated | [synthesized, M5-E36, M5-E37] |
| Multimodal understanding | 2026 papers: image and video generation pretraining works like LLM pretraining for perception | Generative pretraining plus light instruction tuning | Not stated | Not stated | [synthesized, M5-E31, M5-E34] |
| Image and video generation | Component audit: tokenizer-free, one-step, from scratch. One-step ImageNet-256 FID 3.43 (2025-05), 1.72 (2025-12), 1.54 (2026-02), author-reported | Simpler objectives; maybe end-to-end generation (open question, 2025-06) | Not stated | Not stated | [synthesized, M5-E24, M5-E29, M5-E30, M5-E07] |
| Robotics and embodied AI | One paper: a shared policy trunk pretrained over 52 robot datasets, over 20% gain on unseen tasks (NeurIPS 2024 Spotlight). 2023-11: vision systems lack environment feedback | Pretraining across heterogeneous data | Not stated | Not stated | [synthesized, M5-E19, M5-E12] |
| World models, physics, AI for science | No view on world models. Physics-simulation pretraining on over a million samples (2026-02). AI as a shared language across fields (2025-02) | Tools that transfer across fields | 10+ years (2025-02) | Not stated | [synthesized, M5-E40, M5-E10] |
| Compute, open weights, China-US | Research should adapt to compute growth (if Moore's Law persists). No judgment found on open weights or China-US | Hardware trend, his stated condition | Not stated | Not stated | [synthesized, M5-E13] |

## 3. Prediction record

Outcomes as of 2026-11.

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| 2023-11 (article dated 2023-11-02) | Visual self-supervised learning would scale like language models and be his focus for three years, perhaps his career | partly: no 2024-01 to 2026-11 paper on scaling it, by titles and abstracts read; the ideas appear inside generative papers | M5-E12, M5-E02, M5-E17, M5-E26 |
| 2023-11 | An LLM alone is not a promising route to abstract math; code and symbolic tools more so (he said he is not an expert) | partly: 2025-07-21, Google DeepMind reported a model working end-to-end in natural language at IMO gold-medal standard; the post does not say whether tools were used | M5-E12, M5-E38 |
| 2023-11, 2025-02-07 | AI becomes a basic tool across fields: within 10-20 years (2023); in 10 or more years (2025) | pending (2033 at the earliest) | M5-E12, M5-E10 |
| 2024-06-17 | Vector quantization is not necessary for autoregressive image generation (MAR) | right: the group's 10.5B study (2024-10) finds continuous tokens give better visual quality; independent replication not checked | M5-E18, M5-E20 |
| 2025-05-19 | One-step generation from scratch, no distillation, can approach multi-step models (MeanFlow, FID 3.43) | right: same-group follow-ups report 1.72 and 1.54; NeurIPS 2025 Oral; author-reported | M5-E24, M5-E29, M5-E30, M5-E02 |
| 2025-11-17 | Large-patch Transformers on raw pixels generate well with no tokenizer, pre-training or extra loss (JiT) | pending: CVPR 2026 per his list; no independent replication checked | M5-E27, M5-E02 |
| 2026-02-04 | Evolving the distribution during training gives one-step FID 1.54 latent, 1.61 pixel (Drifting) | pending: NeurIPS 2026 Oral per his list; no independent replication found | M5-E30, M5-E02 |
| 2026-08-05 (blog), 2026-10-01 (arXiv) | A visual-memory harness lets a general multimodal model score 100.00 on 25 public ARC-AGI-3 games (Claude Opus 5.0) | pending: "the private set remains the real test of generalization" [quoted, M5-E37]; no outside verification found | M5-E36, M5-E37 |

From the record:

- Direction calls: 2 of 8 held, 2 held in part, 4 pending, 0 missed. The 2 that held are component claims in his own group's papers, tested by the same group's follow-ups. The 2 that held in part are 2023-11 calls about which sub-field would matter or how another would progress.
- Timing calls: 2 of 8 carry a time horizon. The three-year focus of 2023-11 held in part; the 10-year call of 2025-02 is pending.

## 4. Where this persona is most likely wrong

- **Interests:** dated facts are in dossier §E. Where 2026 co-authored papers build on a company's large pretrained generators (Vision Banana, GenCeption), the sources read show no independent evaluation [synthesized, M5-E31, M5-E34].
- **Path dependence:** [inferred] his heuristics formed on benchmarks with one differentiable objective and one clean metric (ImageNet, FID). Without such a metric (open-ended agents, long-horizon decisions), "remove a component and re-measure" is harder to run; VISTA's authors say the public games are not the generalization test [synthesized, M5-E37].
- **Different era or setting:** [inferred] his slides say to plan for cheaper compute, while most of his group's method results are at academic scale. Whether ImageNet-scale audits carry to frontier-scale training is untested in the sources read, except where industry co-authors ran larger models (M5-E20).

## 5. One line for someone starting out

[inferred, from M5-E13 and the paper series] Pick one thing everyone treats as necessary, remove it at a scale you can run from scratch, and write down what you expect before you look at the result.
