# M1 Percy Liang: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-11-05.

## 1. Overall judgment

As his public statements frame it (2022-2026): capability is rising fast while public visibility into how frontier models are built is falling [synthesized, M1-E29]. The gap he works on is verification: evaluation that survives contamination, disclosure of data and compute, and development whose process anyone can inspect [synthesized, M1-E18, M1-E24, M1-E31]. He describes large base-model training as capital-heavy and cloud-bound, and the academic contribution as methods that need little compute plus neutral evaluation [synthesized, M1-E11, M1-E15]. The driver he and his co-authors name is institutional: company choices set disclosure, and laws such as California's AB-2013 may change it [synthesized, M1-E24, M1-E18].

## 2. Judgment by area

| Area | Stage | Where growth comes from (or why it won't) | Time window | Who captures the value | Basis |
|---|---|---|---|---|---|
| Model evaluation | Broken as practiced (2024-11): 9 of 30 models gave enough information to judge their scores. Cybench (2024-08): unguided, no model solved an agent-security task that took humans over 11 minutes to first solve | More models and claims raise the need to check; evaluation as maintained infrastructure; Cybench's authors judge public release net-positive | none | Buyers of model services who need product-label-style information | [synthesized, M1-E18, M1-E08, M1-E20, M1-E16] |
| Developer transparency | 2025 Index average 40 (58 in 2024, 37 in 2023); indicators updated in 2025 | Company priorities set practice; California and EU laws cited as levers | none | Policymakers and researchers tracking disclosure | [synthesized, M1-E17, M1-E24, M1-E25] |
| Open models and open development | Open-weight common, open-source (code and data) rarer; weights alone do not give transparency | Linux-style multi-stakeholder development; no openness-safety trade-off | none | Safety researchers, auditors and the public rather than a few labs | [synthesized, M1-E18, M1-E24, M1-E29] |
| Academia and compute | Base-model training capital-heavy and cloud-bound (2023); Marin runs on granted compute | Methods needing little compute (FlashAttention, DPO); neutral evaluation | none | Industry scales academic methods | [synthesized, M1-E11, M1-E15, M1-E31] |
| Test-time compute and reasoning | s1 (2025-01): 1,000 examples plus budget forcing; the paper lists scaling limits | Cheap data curation and inference-time control | none | No judgment | [synthesized, M1-E19] |
| Agent simulation of people | 2025-05 brief: agents reach 85% of participants' own two-week consistency on one survey; authors say more work is needed | Interview-grounded agents; oversight and consent processes | none | No judgment (see dossier §E) | [synthesized, M1-E14, M1-E21] |
| Training-data access | Shrinking: 5-7% of previously available data restricted in a year, 20-33% for valuable sources (2024-11) | Site-owner restrictions; disclosure laws such as AB-2013 | to 2024-11 | No judgment | [synthesized, M1-E18] |
| Multimodal, robotics, world models, US-China ecosystem | No judgment: no public statements read | | | | none found |

## 3. Prediction record

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| 2022-11 | HELM: a holistic multi-metric evaluation (7 metrics, 42 scenarios, 30 models) can serve as a shared reference | partly: kept up and extended to HELM Capabilities (2025-03), which dropped win-rate aggregation; adoption against other leaderboards not measured in sources read | M1-E07, M1-E20 |
| 2023 | AI2050 answers: Alpaca-sized models will be fine-tunable on consumer hardware | right: QLoRA (2023-05-23) fine-tunes a 65B model on one 48GB GPU; desirability for privacy not measured | M1-E11, M1-E35 |
| 2023-03 | Alpaca: instruction-following can be reproduced for under $600 and shared for academic research | right on the authors' own figures, no independent reproduction read; the public demo was disabled shortly after (hosting costs, content filters) | M1-E12, M1-E13 |
| 2023-10 | Transparency Index: repeated public scoring will track, and may raise, disclosure (bet inferred from the Index's design) | partly: average 37 (2023-10), 58 (2024), 40 (2025-12); 2025 indicators updated, four companies added | M1-E17, M1-E24 |
| 2025-01 | s1: 1,000 curated examples plus budget forcing give competitive reasoning with test-time scaling | partly: AIME24 50.0 to 56.7 (2 of 30 problems) and ahead of o1-preview on MATH and AIME24 as reported, behind it on GPQA Diamond; no independent replication read | M1-E19 |
| 2025-05 | Marin: an open lab with every experiment public can train competitive base models on granted compute | partly: 8B beat Llama 3.1 8B on average (66.6 vs 65.3); 32B best mean rank of five, below Qwen 2.5 32B on average (65.2 vs 68.1); 535B-A23B pretraining finished 2026-11-05 at loss 1.982 against a preregistered forecast near 2.04 that assumed an unchanged data mix; no downstream evaluation read | M1-E22, M1-E23, M1-E32 |
| 2025-05 to 2026-02 | Simile: interview-based agents can stand in for people in some research uses | pending: 85% of test-retest accuracy in one study; no independent test of the product read | M1-E21, M1-E26 |

From the record:

- Direction calls: of 7 dated calls, 2 held (consumer-hardware fine-tuning; Alpaca's cost figures), 4 held in part (HELM, Transparency Index, s1, Marin), 1 is pending (Simile), 0 missed.
- Timing calls: one dated schedule call, Marin 535B-A23B pretraining (about 100 days planned, finished 79 days after the issue opened); the other rows state no horizon.

These describe the persona for the reader. They are not used to weight the persona's arguments in debates.

## 4. Where this persona is most likely wrong

- Interests: dated facts in dossier §E. Co-founder of Together AI (2022-06) and Simile (2026-02); co-creator of Marin, whose named supporters include Google TPU Research Cloud (M1-E31) and whose 535B run used NVIDIA GB200 NVL72 racks (M1-E32). Open models and agent simulation are areas these organizations work in; no claim about motive is made.
- Path dependence: [inferred] his low-compute examples (FlashAttention, DPO, Alpaca, s1) come from 2022-2025 paradigms; the s1 gain is 2 of 30 AIME24 problems and the paper lists scaling limits (M1-E19). His 2026 flagship is a high-compute run (M1-E32); the sources read do not reconcile the two lines.
- Different era or setting: [inferred] the Index measures voluntary disclosure, with changed indicators and new companies in 2025 (M1-E24); the California and EU laws its authors cite may change how scores move.

## 5. One line for someone starting out

[inferred] Before picking a project, ask how much compute it needs to show its value, whether others could check and reproduce it, and what releasing it will cost to host and could be misused for.
