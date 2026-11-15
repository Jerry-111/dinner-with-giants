v6 fact-check ③: after R3. The fact-checker did not read the persona material (the experience check read only dossier §A, §B, §G and §I). 2026-10-28.

## Table 1 Claim check (new citations in round C / overtime / R3, not covered by errata_B)

| # | Post | Claim | Verdict | What the primary source says | URL |
|---|---|---|---|---|---|
| 1 | C/X5/M4 search | OpenVLA fuses pretrained DINOv2 + SigLIP visual features | confirmed | Abstract: "combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP" | arxiv.org/abs/2406.09246 |
| 2 | R3/M6 self-check | OpenVLA-OFT keeps the same DINOv2 + SigLIP backbone and does not replace the vision encoder | confirmed | Body text, Appendix A-A: "a fused vision backbone (with both SigLIP and DINOv2...)"; OFT's six changes do not touch the encoder | arxiv.org/abs/2502.19645 |
| 3 | followups Q1; C/X2/K2; cited in several X1 posts | GPT-4o-mini/4.1-mini judging the same comparison repeatedly flip with an average probability of 13.6% across 29 tasks; GPT-4o-mini has a significant first-position bias | confirmed | Paper: 29 tasks, 10 categories, average flip rate 13.6%; GPT-4o-mini first-position tendency 72% (p=0.024) | arxiv.org/abs/2606.13685 |
| 4 | followups Q1 | RAND test + JudgeBiasBench: judge models' rankings are unstable across benchmarks; frontier models have error rates above 50% on high-level bias tests | partly confirmed | Second-hand sources (adaline.ai/LayerLens) confirm the ">50% error rate"; "unstable ranking across benchmarks" is a conclusion from RAND's own harness, and the RAND primary paper text could not be found for verification | adaline.ai/blog/llm-as-a-judge-reliability-bias |
| 5 | overtime/X2/1_K2 (experience) | The 2014 distillation paper was rejected by NeurIPS as "unlikely to have a significant impact" and later became the basis of Gemini Flash | partly confirmed | Second-hand sources (a 2025 arXiv position paper, Chinese tech media) confirm the paper was rejected, and Vinyals himself attributes it to "lack of novelty and impact" (translated); no source was found confirming a link to Gemini Flash | arxiv.org/abs/2506.19882 (cited second-hand) |
| 6 | overtime/X7/2_K4 | nanochat's training cost fell about 600x in 7 years | confirmed | GPT-2 (2019) about $43,000/168 hours vs nanochat (2026) about $73/3 hours, about 600x; "600x in 7 years" is K4's own argument framing, not a verbatim quotation | github.com/karpathy/nanochat |
| 7 | persona card headers in several posts (C/X1/M7 etc.) | Walden Robotics seed round about $300 million, valuation about $1.1 billion (2026-07) | confirmed | Official press release: co-led by Toyota and Deviation Capital, with Nvidia and Boeing participating, about $300M/$1.1B | businesswire.com 2026-07-15 (cited second-hand) |
| 8 | overtime/X4/1_C4, 1_K2 | The median rate of algorithmic progress is about 3.5x/year, 95% interval 1.9–37x/year, with the elasticity fitted only on two model families, Qwen-2.5 and Llama-3.1 | confirmed | Paper Appendix G: the log value of the p50 time horizon is 1.265 (about 3.5x/year), and the resampled 95% interval corresponds to about 1.9–37x/year; the elasticity estimate indeed uses only two model families | arxiv.org/abs/2511.19492 |
| 9 | persona card headers in several posts (C4) | Anthropic valuation $965 billion (2026-05) | confirmed | Several media outlets: 2026-05-28 Series H, $65B round, post-money $965B | news.bloomberglaw.com (cited second-hand) |
| 10 | persona card headers in several posts (C6) | Isomorphic Labs Series B of $2.1 billion (2026-05) | confirmed | Official press release: 2026-05-12, Series B $2.1B, led by Thrive Capital | isomorphiclabs.com/press/isomorphic-labs-funding |
| 11 | persona card headers in several posts (M8) | Shengshu Technology valuation above $2 billion, preparing a Hong Kong IPO (2026) | confirmed | After a Series B of about RMB 2 billion in 2026-04, valuation above $2B (the company has not publicly confirmed a specific figure); August reports say a Hong Kong IPO is planned, but the original H1 2026 timetable has been postponed | 36kr.com/cls.cn (cited second-hand) |

## Table 2 Self-check spot check

| # | Post | query/quotation | url | Is the sentence on the page? | Is the result judged right? |
|---|---|---|---|---|---|
| 1 | C/X5/M4 | "OpenVLA fuses pretrained DINOv2 and SigLIP visual features" | arxiv.org/abs/2406.09246 | Mostly: the abstract's original sentence is "a visual encoder that fuses pretrained features from DINOv2 and SigLIP"; M4's is a paraphrase, not verbatim | Right: used to "rebut" M7's "beating the diffusion head shows no extra representation is needed"; OpenVLA-OFT does inherit this strong pretrained representation, so the rebuttal holds |
| 2 | R3/M6 (self-check, no JSON, stated in the text) | "OFT keeps the shared encoder that blends DINOv2 and SigLIP features" | arxiv.org/abs/2502.19645 | No: the paper's text is "a fused vision backbone (with both SigLIP and DINOv2 vision transformers)" / "the shared SigLIP-DINOv2 backbone"; M6 put it in quotation marks but it is in fact a paraphrase, not verbatim | Substance judged right: the paper confirms OFT did not replace the encoder; but the quotation marks present it as a direct quotation, which risks misleading; it should be marked "paraphrase" rather than a quotation |

## Experience check (20 "experience argument" entries sampled from summary_full, at least 2 per table)

| Post (table) | Persona | The experience in one sentence | Dossier location | Result |
|---|---|---|---|---|
| X1 | K5 LeCun | NIPS rejected the workshop in 2007; a self-organized one drew several hundred people | §A4/§G5/§I-4 | found |
| X1 | M7 Tedrake | Led MIT in the DRC with repeated failures | §A2/§B failure 1/§I-2 | found |
| X2 | C6 Hassabis | Founded DeepMind and chose games because evaluation is clean | §A (2010-2016 entry) | found |
| X2 | K2 Dean | MapReduce came from extracting the parallel code the team kept writing by hand | §A row 4/§B success 2/§I-3 | found |
| X2 | M8 Zhu | Vidu's claim to rival Sora was questioned, and it held up only after switching to blind testing | §B failure 2/§I-4 | found |
| X3 | C1 Mauboussin | Witnessed Miller's winning streak and then the crash | §A/§B/§I-4 | found |
| X3 | K1 Khosla | Cleantech portfolio, the KiOR lesson | §B failure 2/§I-5 | found |
| X3 | M5 He | The VISTA paper's harness reaching 100 | §B success 3/§I-5 | found |
| X4 | C4 Amodei | 2017 Big Blob of Compute: the speech RNN worked by piling on resources, not a new mechanism | §A2/§I-1 | found |
| X4 | K2 Dean | 1999–2004: the search index moved into memory; latency crossed a threshold and new features appeared | §B success 1/§I-2 | found |
| X4 | K3 interjection Sutton | Loss-of-plasticity research, a small network that made it into Nature | §B success "small setting, big result" | found ("continual backprop" as an algorithm name does not appear verbatim in §A/B/G/I; the detail is slightly thin) |
| X5 | M6 Li | ImageNet signatory, self-assessed contribution to AlexNet at one third | §A (2012 entry) | found |
| X5 | M7 Tedrake | In 2023, did Diffusion Policy with Shuran Song | §B success 2/§I-3 | found |
| X5 | M4 Xie | MMVP: CLIP is the root of the vision weakness | §B success 2/§I-3 | found |
| X6 | C5 Levine | 2016–18 real-robot grasping 800K+ times, QT-Opt success rate 96% | §A-1/§I-1 | Detail mismatch: the dossier records the 2016 collection (6–14 arms, two months, 800K+ attempts) and QT-Opt itself in 2018 (580K attempts, 96%) as two separate things; this entry wrongly attaches the 800K+ to QT-Opt |
| X6 | K3 Sutton | PA body swap: all six games degraded ("12 hours" has been withdrawn) | §B failure/§I-4 | found |
| X6 | K4 Karpathy | In Tesla's simulation an RL agent exploited a friction loophole to slide | §G1 | Detail mismatch: the dossier has only the general statement "RL agents in simulation exploit loopholes in the physics engine" (translated), and does not name Tesla, friction or sliding |
| X7 | C3 Huang | After AlexNet, judged that neural networks scale and have no ceiling | §A (AlexNet entry)/§I-4 | found |
| X7 | K4 Karpathy | Universe project: RL finds the gap between target and intent; on Dwarkesh, a judge scoring gibberish as full marks | §A2/§B/§G3/§I-2 | Detail mismatch: the dossier records the Universe failure as "reward too sparse, agent bumping around" (translated), not the more specific mechanism of "finding gaps in intent" (reward hacking); the specific claim "a judge gives full marks to gibberish" does not appear; §G3 has only the general statement "LLM judges can be attacked" (translated) |
| X7 | M6 Li | Caltech object recognition: self-assessed the team's contribution at about one third; being able to publish papers does not mean a real breakthrough | §A/§B failure 1 | Detail mismatch (merged): "can publish papers but no breakthrough" is indeed a self-assessment from the Caltech PhD period (2001–2005); "contribution about one third" is in fact a self-assessment from the 2012 AlexNet/ImageNet (Stanford) period; two events from different periods are merged into one sentence |

Experience spot check of 20 items: 16 found, 4 detail mismatches, 0 not found.

## Corrections needed

1. summary_full/X6.md, "experience argument" entry: C5 Levine's "2016–18 real-robot grasping 800K+ times, QT-Opt success rate 96%" should be split. 800K+ is the volume collected in 2016 with 6–14 robot arms over two months, while QT-Opt itself (2018) used 580K grasps. The original post overtime/X6/1_C5.md already correctly says "580K"; the error appears only in the summary compression step. Suggested summary wording: "800K+ collected in 2016; in 2018, QT-Opt trained on 580K of them, success rate 96%".
2. summary_full/X7.md, "experience argument" entry: M6 Li's "Caltech object recognition, self-assessed team contribution about one third" should be split into two entries. "Can publish papers but no breakthrough" is a self-assessment from the Caltech PhD period; "contribution about one third" is a self-assessment from the 2012 ImageNet/AlexNet (Stanford) period; they are not the same event.
3. R3/M6.md self-check: "OFT keeps the shared encoder that blends DINOv2 and SigLIP features" is not a verbatim sentence from arXiv:2502.19645; it is M6's own paraphrase. Suggestion: in future, before putting a self-check quotation in quotation marks, check that it matches the original text verbatim; otherwise mark it "paraphrase".
4. The RAND/JudgeBiasBench item in followups.md Q1: suggest keeping its existing qualifier "original paper not verified"; this check also could not obtain RAND's primary text directly and verified only the second-hand retelling.
5. overtime/X2/1_K2.md "the distillation paper … later became the basis of Gemini Flash": the NeurIPS rejection episode has second-hand support, but no independent source was found for the specific causal chain "became the basis of Gemini Flash"; suggest adding "not independently confirmed" when it is cited after round C.

## Which tables' conclusions are affected

- X5: the check confirms the DINOv2 + SigLIP backbone of OpenVLA/OpenVLA-OFT; the argument base on which M4, M6 and C2 this round lowered D08 / raised D07 is solid. The quotation in the R3/M6 self-check needs a "paraphrase" label; this does not affect its conclusion.
- X1, X2: the judge-instability figure in followups Q1 (13.6% flip rate) is confirmed at the primary source, supporting C2's and K2's argument that "the evaluation yardstick is wobbling"; the RAND/JudgeBiasBench part is still limited to second-hand sources, and arguments that rely on it should keep their uncertainty.
- X4: the check of the algorithmic-progress-rate interval in 2511.19492 matches exactly; the judgment C4 and K2 converge on, "the interval is too wide to bet on", holds; K2's experience argument (the 1999–2004 memory threshold) and K3's interjection (loss of plasticity) are both verified and do not affect X4's conclusion.
- X6: the "Tesla friction" detail in K4's post goes beyond what the dossier covers; it does not affect the mechanism conclusion of the argument (a sim can actively teach the wrong thing), but when cited it should be labeled "dossier gives only a general statement; specific case not on record". C5's QT-Opt figure needs to be corrected in a later version.
- X7: K4's post tells the "Universe finds gaps in intent / judge gibberish" experience more specifically than the dossier records it, but this does not change the core facts X7 has converged on (the Yue et al. mechanism; distillation does not prove capability beyond the base distribution).
- X2, X3: the valuation/funding figures for Walden, Anthropic, Isomorphic Labs, Shengshu Technology and others are all confirmed; as the factual basis of the "valuations are running ahead of the evidence" argument they are solid, and the disagreement still lies in value judgments (when to commit) rather than in the facts.
