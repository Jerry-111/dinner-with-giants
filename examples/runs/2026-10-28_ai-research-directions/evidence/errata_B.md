v6 fact-check ②: after round B, before round C. The fact-checker did not read the persona material. 2026-10-28.

## Table 1 Claim check (the claims most cited in round B and driving acceptance)

| # | Post | Claim | Verdict | What the primary source says | URL |
|---|---|---|---|---|---|
| 1 | X7, accepted by several | Yue et al. (NeurIPS 2025 Oral): RLVR mainly raises pass@1/sampling efficiency; at large k the base model overtakes the RL model; new reasoning comes from distillation, not RLVR | confirmed | The arXiv page's "Journal reference" field self-reports NeurIPS 2025 Oral; the abstract says RLVR does not introduce new reasoning patterns, while distillation can introduce the teacher's new patterns | arxiv.org/abs/2504.13837 |
| 2 | X7, accepted by several | s1: AIME24 from 50.0 to 56.7, only 7 H100 GPU-hours | confirmed | Body text Table 1/§5.1: 50.0 without BF, 56.7 with the 4x Wait setting; s1-32B needs only 7 H100 GPU-hours (fine-tuning on the full 59K data takes another 394 hours; do not mix the two numbers) | arxiv.org/abs/2501.19393 |
| 3 | X7, accepted by several | DeepSeek-R1 uses RL (GRPO) to elicit long chain-of-thought reasoning, which can be distilled into small models | confirmed | §2.2.1 confirms GRPO is used; §2.4/Table 5 give concrete scores for distillation into each Qwen/Llama size; R1-Zero is said to have naturally learned to solve problems by using longer thinking time | arxiv.org/abs/2501.12948 |
| 4 | X4 core (C4/K2/M1/M2) | METR: on a strong NanoGPT baseline, 70-90% of the cost of most self-improvement trajectories is experiment compute | confirmed | The blog's original sentence: "experiment cost comprised around 70-90% of the cost of most trajectories"; the same post attributes this to a "possibly inefficient harness" (translated), not necessarily an inherent feature of RSI; the debate did not mention it | metr.org/blog/2026-07-21-expenditure-horizon |
| 5 | X5, accepted by C2/M7 | OpenVLA-OFT: LIBERO 76.5% → 97.1%, 26x throughput, on real-robot ALOHA up to 15 percentage points above the comparison method | partly confirmed | The first two are confirmed; the ALOHA difference is "up to 15% (absolute)" in the original, the largest single-item difference (an upper bound), not an average; the debate's "up to" is accurate; guard against it being simplified to "15 points higher on average" | arxiv.org/abs/2502.19645 |
| 6 | X5, accepted by both C2 and M7 | REPA representation alignment speeds up SiT training convergence by more than 17.5x | confirmed | Abstract: without CFG, REPA reaches in under 400K steps the quality that SiT-XL originally needed 7M steps to reach, about 17.5x or more | arxiv.org/abs/2410.06940 |
| 7 | X6, cited repeatedly (C5/K3/K5) | MimicGen: about 200 human demonstrations synthesize 50,000+, 18 tasks | confirmed | The abstract confirms about 200 human demonstrations generating over 50,000, 18 tasks; the numbers match | arxiv.org/abs/2310.17596 |
| 8 | X4, K2 cites followups Q5 | Darwin Gödel Machine: about $22,000 over two weeks; SWE-bench 20.0% → 50.0%; Polyglot 14.2% → 30.7% | partly confirmed, risk of an embedded error: the cost was not verified at a primary source | The arXiv abstract confirms the two scores; neither the abstract nor the Sakana website has a cost figure or the two-week claim; only one second-hand blog with no stated source gives the same $22,000 | arxiv.org/abs/2505.22954; sakana.ai/dgm (no cost figure) |
| 9 | X4, cited by K2 | AlphaEvolve continuously reclaims about 0.7% of global compute on Borg scheduling | confirmed (official self-report, not independently audited) | DeepMind blog: "reclaims about 0.7% of Google's worldwide compute on average", running for over a year | deepmind.google/blog/alphaevolve-...-designing-advanced-algorithms |
| 10 | X5 (accepted by C1/M4/M6; M6 also challenges) | The LBM paper validates D07 with blind randomized real-robot trials | partly confirmed | arXiv:2507.05331 (TRI team) confirms "blind, randomized trials" covering simulation and real robots; it is the team's own paper, and no replication outside the team was found | arxiv.org/abs/2507.05331 |
| 11 | X3, C1 self-check | Khosla Ventures is a repeat investor in General Intuition; the valuation was reported within weeks to go from about $2B (a $300M round) to nearly $6B pre-money; "claims to have pioneered this category" is not confirmed by independent reports | partly confirmed | The Dealroom 2026-06-18 headline can be found and lists KV as an existing investor; that round closed on 2026-06-26 at $320M/$2.3B (not "~$2B"); the $6B is a pre-money figure still under negotiation; neither article contains the words pioneer/created | dealroom.co/news/135165...; /146571... |
| 12 | X3, K1 accepts "VISTA does not count as D08 evidence" | VISTA: a visual-memory harness takes frontier models on ARC-AGI-3 from 40.68 to 100 on a human-normalized scale, across 25 public games, with no model change and no training | confirmed | arXiv:2610.02200 has Kaiming He among its authors; the abstract has Claude Opus 5.0's Relative Human Action Efficiency rising from 40.68 to 100.00, all 25 public games cleared, with 57.4% fewer actions than human novices; it describes only the visual-memory harness and does not mention training | arxiv.org/abs/2610.02200 |
| 13 | X5, accepted by M6 | Diffusion Policy was later adopted by π0 and GR00T N1 | partly confirmed, with a mix-up | π0's core is flow matching, not Diffusion Policy itself; GR00T N1's action head is a diffusion transformer / flow-matching DiT; the lineages are related, but no source was found in which either calls itself an adopter of Diffusion Policy | arxiv.org/abs/2410.24164 (π0); the GR00T N1 information comes from the model card, not a primary paper |
| 14 | X6, K3 | Physical Atari: after switching to a second robot built from the same blueprint, all 6 games got worse; Pong and Kangaroo needed about 12 hours to partially recover, and for the other four not even the speed of recovery was measured | partly confirmed, wrong number embedded | arXiv:2606.19357 confirms all 6 games got worse after switching to another identically built body; but the paper has no "12 hours" figure; the only "12" is a 3D-printing time / n-step return, unrelated to recovery time; continued learning was measured on only two games (unnamed), and naming Pong/Kangaroo is speculation | arxiv.org/abs/2606.19357 |

## Table 2 Self-check spot check (searches; this 1 is the only non-empty one in the whole set)

| # | Post | query | url | Is the sentence on the page? | Is the result judged right? | Issue |
|---|---|---|---|---|---|---|
| 1 | B/X3/C1 | "Khosla Ventures General Intuition world model investment" | dealroom.co/news/135165-...-2b-valuation | Yes, verbatim (the headline is the sentence) | Right: the result "supported" for the "valuation/funding rumor" is correct | C1's post has two further claims, "Khosla is a repeat investor" and "claims to have pioneered not confirmed" (both confirmed by the page); three facts share one search, which is not a misreading but a narrow record |

Of all 86 JSON files, only this one has a non-empty `searches`; the rest are all `[]`. `source_challenge` is non-empty in 6; see Table 3.

## Table 3 Challenged sources (source_challenge)

| Post | Challenged claim | Is there an independent source? | URL |
|---|---|---|---|
| B/X1/C2→K3 | "Oak Lab's first paper proves that credit assignment over the experience stream works" | Not found. Reports of Oak Lab's founding and of Sutton/Javed leaving Keen were found; neither the paper nor a replication outside the team was found | None |
| B/X3/C1, M5→K1 | "claims to have pioneered the world-model category" | Not found. The General Intuition funding reports contain no wording like pioneer/created anywhere | dealroom.co/news/135165... |
| B/X3/C5→M8 | "the pattern from imagination-verification to an action foundation has happened twice" | Not found. It is M8's own synthesized account of its technical path, not a single fact that can be checked externally | None |
| B/X5/M6→M7 | "LBM blind randomized real-robot trial results" | Found but not independent: arXiv:2507.05331 confirms this design; it is the LBM team's own paper, and no replication outside the team was found | arxiv.org/abs/2507.05331 |
| B/X6/K3→C3 | "RIVA had 6 months of cash left on the books and solved it with simulation" | Found but numbers inconsistent: several reports trace to Huang's own Acquired interview and confirm the episode in which, in 1997, before the RIVA128 tape-out, the design was verified in simulation and then taped out directly; but "how much cash was left" is retold inconsistently (6 months / 30 days / a few weeks) | No primary transcript; sourced from multiple retellings of the podcast |

## Corrections needed

1. B/X6/K3 "about 12 hours to partially recover": not found in the paper; it should be deleted and rewritten as "continued learning improved performance on two games; no duration is given and the two games are not named".
2. "Diffusion Policy was later adopted by π0 and GR00T N1" (A/X5/M7; accepted in B/X5/M6): should be changed to "both use flow-matching / diffusion-transformer designs of the same lineage, not a direct adoption of Diffusion Policy".
3. followups.md Q5, Darwin Gödel Machine "$22,000": suggest adding "the cost figure comes from a second-hand blog with no stated source; the primary paper does not give it; to be verified".
4. B/X3/C1 "a $300M round at about $2B": it is a rumor-stage figure; the round actually completed was $320M/$2.3B, and the round C citation should be corrected. The other two points (approaching $6B pre-money; claimed pioneering not confirmed) check out and need no change.
5. OpenVLA-OFT "up to 15 percentage points higher": the wording is already accurate (it says "up to"); a reminder that round C should not simplify it to "15 points higher on average".

## Tables affected

- X3: the General Intuition valuation figure needs one correction step; the VISTA and LBM challenge results are for round C reference.
- X4: METR's 70-90% and AlphaEvolve's 0.7% are both confirmed; Darwin Gödel Machine's $22,000 needs the qualifier "not verified at a primary source".
- X5: OpenVLA-OFT must distinguish "up to" from "average"; REPA confirmed; LBM is not an independent replication; Diffusion Policy/π0/GR00T N1 need correcting.
- X6: the direction of degradation across the six Physical Atari games is confirmed; the "12 hours" that K3 added must be deleted; the RIVA128 episode has sources but the number of months is not established.
- X7: the three core facts, Yue et al., s1 and DeepSeek-R1, are all confirmed; the factual base is the most solid.
- X1, X2: this round had no new numbers or research citations that could be independently checked.
