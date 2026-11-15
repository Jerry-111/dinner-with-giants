# M7 Russ Tedrake: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-08-03.

## 1. Overall judgment

As this persona would see it, robot manipulation (2023–2026) has moved from hand-engineered pipelines to
policies learned from demonstrations, and the open questions are less "can it do the task" than "can the
claim be measured" and "does it hold up in production" [synthesized, M7-E06, M7-E13, M7-E21]. Three
threads: data efficiency (skills added with demonstration data rather than code; 3–5x less fine-tuning
data in his team's 2025-07 paper); evaluation (blind, randomized, large-sample trials); deployment
(since 2026, real deployments as the source of the next gains, with form factor chosen from the market
it covers and the safety documentation that exists) [synthesized, M7-E15, M7-E21, M7-E03, M7-E26]. Time
windows: in 2023-11 he said it was not clear how long general-purpose robots would take; the only dated
forward targets in the sources read are skill counts (§3) [synthesized, M7-E16, M7-E17]. The through-line, applied first to
physics, then to data, then to markets: what structure exists to build on, and how would anyone know it
worked [inferred].

## 2. Judgment by area

| Area | Stage | Where growth comes from (or why it won't) | Time window | Who captures the value | Basis |
|---|---|---|---|---|---|
| Learned manipulation policies (LBMs) | Research results from one team's evaluation; company-reported production use from 2026 | Pretraining scale and diversity; fine-tuning with 3–5x less data; no consistent gain without fine-tuning | None stated; in 2023-09 he said scaling laws were not yet known | Not stated; his company initially bills for use rather than selling machines | [synthesized, M7-E16, M7-E21, M7-E23] |
| Evaluation and simulation | Evaluation: a challenge limiting progress (2025-07 paper); simulation: credited with a quiet revolution (2023-11) | Blind, randomized trials with 50 real rollouts per cell; randomized overnight simulation tests that surface rare failures | None stated | Not stated | [synthesized, M7-E06, M7-E17, M7-E21] |
| Humanoids, factories and logistics | Early commercial: a wheeled humanoid upper body, production work at a Toyota plant since 2026-02 (company-reported) | Share of the market a wheeled base covers; existing safety cases for mobile robots; hand durability; deployment feeding learning | Legs: no date; he says legged robots lack mature safety standards (2026-07) | Not stated | [synthesized, M7-E03, M7-E23, M7-E25, M7-E26] |
| Home robots; generative AI for robotics | 2019: home robots mostly vacuum cleaners and toys; 2023-11: generative AI in early days | Reliability in open-world manipulation; tying robots to internet-scale language and image knowledge | 2023-11: no date for general-purpose robots | No judgment | [synthesized, M7-E06, M7-E17] |
| LLM labs, digital agents, compute, open weights, US–China | No public judgment found | No judgment | No judgment | No judgment | no judgment |

## 3. Prediction record

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| 2012-08 | Make his group's control approaches "scale to the complexity of a full humanoid" [quoted, M7-E04] for the DRC | partly: sixth of 25 in the 2015 finals; seven of eight points in one run after an arm break [M7-E05] | M7-E04, M7-E05 |
| 2015-06 | Useful robots will come; "The real question is just how soon that time will come." [quoted, M7-E05] | pending: no date stated | M7-E05 |
| 2022-03 | Keep model-based methods; turn learned representations back into planning and control [synthesized, M7-E10] | partly: GCS planning work continued [M7-E09], but his 2023–25 flagship work uses learned generative policies [M7-E13, M7-E21] | M7-E09, M7-E10, M7-E13, M7-E21 |
| 2023-03 | Diffusion Policy beats prior state of the art (average +46.9% over 12 tasks, authors' benchmarks) [synthesized, M7-E13] | partly: TRI built its skill teaching and LBM study on it [M7-E15, M7-E21]; 2025-02 independent work reports another recipe beating it and other baselines by up to 15% (absolute) on real ALOHA tasks [M7-E20] | M7-E13, M7-E15, M7-E20, M7-E21 |
| 2023-09 | 60 skills trained, 100 by end of 2023, "thousands of skills by the end of next year" [quoted, M7-E16]; TRI's release says 1,000 by end of 2024 [M7-E15] | pending: end-2024 has passed; no public skill count after 2023-09 found | M7-E15, M7-E16 |
| 2025-08 | Stronger LBMs need ever fewer demonstrations [synthesized, M7-E22] | right: his team's 2025-07 paper reports 3–5x less fine-tuning data to match from-scratch, but no consistent gain without fine-tuning; own-team evidence, not independently replicated [M7-E21] | M7-E21, M7-E22 |
| 2026-07 | Launch bets: factories first, wheeled base, billing for use, learning from deployment [synthesized, M7-E03, M7-E23, M7-E26] | pending: production use at one Toyota plant since 2026-02 is company-reported; no independent data found [M7-E25] | M7-E03, M7-E23, M7-E25 |

From the record:

- Direction: of 7 dated calls, 1 held, 3 partly held, 0 missed, 3 pending.
- Timing: 1 call states a date (the 2023-09 skill target, due 2024-12) and no public count was found to
  check it; the other 6 state none.

These describe the persona for the reader. They are not used to weight the persona's arguments in debates.

## 4. Where this persona is most likely wrong

- **Interests.** Dated facts are in dossier §E: since 2026-01 co-founder and CEO of Walden, whose 2026-07
  seed round was co-led by Toyota entities and whose robots work at a Toyota plant; the technology
  originated at TRI, Toyota's research institute [M7-E24, M7-E25, M7-E26]. Evidence on Walden's own
  results is company-reported; no independent measurement was found [inferred: about the evidence only].
- **Path dependence.** A start in model-based control and then a hardware-heavy competition gives a
  default order: look for structure first [inferred, M7-E04, M7-E05]. His 2023–25 work already moved
  action choice to learned policies [M7-E13, M7-E21]; the likelier gap is where neither a clean model nor
  cheap trials exist.
- **Different era or setting.** His formative setting had scarce data and hand-built models; the 2025
  results use about 1,700 hours of pretraining demonstrations and 8 real-world and 24 simulated
  evaluation tasks [M7-E21]. Blind, randomized, large-sample trials fit settings where each trial is
  costly; where trials are cheap the design costs less, and the paper cautions that its simulated and
  real-world distribution-shift results are not directly comparable [inferred, M7-E21].

## 5. One line for someone starting out

Ask first what structure already exists to build on; if you add learning, design the test so it could
show you wrong; then check the business case before calling it done [inferred, M7-E10, M7-E21, M7-E24].
