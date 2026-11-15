# M8 Jun Zhu: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-10-08.

## 1. Overall judgment

As he would see video generation and world models in 2026 [synthesized, M8-E04, M8-E06, M8-E07]: video
generation went from proof of concept to industry in about two years; the largest shift is from specialized to
general models that follow scaling laws. Video models already achieve understanding and imagination, two of the
three abilities a world model needs; the third, action, is the current work, with robot models built on video
pretraining. His roadmap runs from L1 world generation to L5 world orchestrator; his company reports coverage of
L1–L3, and he lists six open challenges for L4–L5 [M8-E07]. Drivers: data (internet video, then first-person
video, then robot data), unified architectures, inference efficiency [M8-E05, M8-E06]. In
2025-03 he saw video commercializing faster than language models, with no red-ocean state [M8-E04]. A named
critic holds that video generation is not a world model [M8-E28].

## 2. Judgment by area

| Area | Stage | Where growth comes from (or why it won't) | Time window | Who captures the value | Basis |
|---|---|---|---|---|---|
| Video generation | Proof of concept to industry in about two years; controllability next | Stronger base models plus back-end techniques; efficiency work | No dates stated | Leading models, each on a differentiated business path | [synthesized, M8-E04, M8-E06] |
| Generative models for robotics | Early: video pretraining, then few-demonstration adaptation | Video as data carrier past the robot data wall; planning from imagined futures | No dates stated | No judgment | [synthesized, M8-E05, M8-E06, M8-E26] |
| Robots and embodied AI | Team-reported results on a simulation benchmark and nearly ten robot bodies; no independent evaluation read | Video pretraining plus 50–100 trajectories per new body | No dates stated | No judgment | [synthesized, M8-E07, M8-E26] |
| World models and simulation | L1–L3 covered per the company; L4–L5 open, six challenges listed | A closed loop coupling understanding, prediction and action | No time estimate | No judgment | [synthesized, M8-E07] |
| China–US ecosystem | Chinese video models lead in many respects (2025-03); company-reported rank first in China, second globally (2026-02) | Not stated | Already the case, per the 2025 statement | No judgment | [synthesized, M8-E04, M8-E10] |
| Language models; digital agents; multimodal understanding | No judgment | No judgment | No judgment | No judgment | [synthesized] no statement in the sources read |

## 3. Prediction record

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| 2013 | Bayesian methods, then seen as outdated, still hold untapped potential; his team begins applying them to AI | right in direction, about nine years to the 2022 ICLR award: Bayesian deep learning and regularized Bayes (M8-E14, M8-E15), then an ICLR 2022 Outstanding Paper (M8-E17) | M8-E14, M8-E15, M8-E17 |
| 2022-09 | A simple ViT-based backbone can replace the U-Net in diffusion models (U-ViT) | right in direction: DiT, a transformer-backbone diffusion model, followed 2022-12-19 (M8-E20); Vidu shipped on U-ViT 2024-04-27 (M8-E12) | M8-E19, M8-E20, M8-E12 |
| 2024-04-27 | Release Vidu on U-ViT as China's first long-duration, high-consistency, high-dynamics video model, called very close to Sora's level by the company | partly: 16-second clips against up to a minute for Sora; a critic judged quality behind Sora (M8-E13); company-supplied second-place global rank for Vidu Q3 in 2026-02 (M8-E10) | M8-E12, M8-E13, M8-E10 |
| 2024-10 | Build a diffusion foundation model for bimanual manipulation (RDT-1B) | partly: the OpenVLA-OFT authors reported beating it on real bimanual tasks by up to 15 points (2025-02-27, M8-E27) | M8-E22, M8-E27 |
| 2025-03-31 | Video models commercialize faster than language models; a model that suddenly pulls far ahead is unlikely | pending: only a company-supplied ranking read (second-place global rank, 2026-02); no independent revenue or leaderboard history | M8-E04, M8-E10 |
| 2026-03-29 | Video is the way past the robot data wall; Motus is the physical-world model on that route | pending: Motus (open-sourced 2025-12-16; README 87.02% on RoboTwin 2.0) and Motubrain (95.8% clean, 96.1% randomized) are team-reported simulation scores | M8-E05, M8-E25, M8-E26 |
| 2026-07-20 | Real-time streaming generation with voice control and unlimited-length dialogue works now (540P, up to 42 FPS) | pending: speaker-supplied figures; no third-party evaluation read | M8-E06 |
| 2026-08-19 | Five-level roadmap: L1–L3 covered by the company; six challenges listed for L4–L5 | pending: no time estimate; no outside evaluation read | M8-E07 |

From the record:

- Direction calls: of 8 dated calls, 2 resolved right (2013 Bayesian bet, 2022 ViT-based backbone), 2 partly, 4
  pending; the four pending calls (2025-03 to 2026-08) rest on company-reported or speaker-supplied evidence.
- Timing calls: about nine years from the Bayesian bet to the ICLR award (2013 to 2022); 19 months from
  U-ViT to a shipped Vidu (2022-09 to 2024-04). None resolved as early or late; four are pending.

These describe the persona for the reader. They are not used to weight the persona's arguments in debates.

## 4. Where this persona is most likely wrong

- **Interests** (disclosed facts, §E). Founder and chief scientist of Shengshu, whose Vidu, Motus and Motubrain
  are the products at L1–L3 of the roadmap he presents (M8-E07); Alibaba Cloud led its 2026-04 round (M8-E08);
  Tsinghua posts (M8-E02, M8-E06).
- **Path dependence** [inferred]. A method regarded as outdated (Bayesian, 2013) later won recognition, and
  probabilistic-modeling skill then paid off in the diffusion wave (M8-E14, M8-E17). The 2026 route depends on
  video pretraining carrying over to physical interaction; his own roadmap lists learning contact, friction and
  force as open (M8-E07), and BAAI's president Wang Zhongyuan argues video generation is not a world model
  (2026-06-18; the article does not mention Zhu) (M8-E28). The OpenVLA-OFT authors reported their recipe beating
  RDT-1B and Diffusion Policy on real bimanual tasks (M8-E27); no statement by him on it was read.
- **Different era or setting** [inferred]. The professor-plus-company route rests on Tsinghua posts, a state key
  laboratory and doctoral students (M8-E01, M8-E02), a 2010s academic path; it is hard to follow for someone
  starting out in 2026 without comparable backing.

## 5. One line for someone starting out

[inferred] Do not train and evaluate generation, prediction and action separately, and first ask whether a
result measures learned physical or causal structure or only interpolation inside the training distribution;
his long bets were held from a professorship and a state laboratory, which a newcomer lacks.
