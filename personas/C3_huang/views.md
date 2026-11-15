# C3 Jensen Huang: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-11-14.

## 1. Overall judgment

In his account, this is a change of computing paradigm: a shift from retrieval-style
general-purpose computing to generation-style accelerated computing, pulling networking, storage
and software with it [C3-E03, C3-E05]. The AI factory is "electrons in, tokens out" [quoted,
C3-E01]; by 2026, "compute is revenue" [quoted, C3-E34].

**Stage.** Still early and accelerating, nowhere near oversupply in his judgment, because the
shift away from general-purpose computing will take years [C3-E05]. In March 2026 he said NVIDIA
had at least $1 trillion of revenue visibility for 2025–2027 [C3-E27]; the quarter ended
2026-07-26 brought $89.0B in data-center revenue, up 117% year over year [C3-E34].

**Drivers**, by his account: three scaling laws (pre-training, post-training, inference-time
thinking — the last a "second exponential" [C3-E05]); agents turning every task into a multi-step
inference job; and, next, Physical AI [C3-E08, C3-E30]. The one named constraint is power:
power-limited, tokens per watt decides revenue [C3-E04, C3-E05].

**His own hedges, read into the record** [inferred]: a Wall Street consensus put to him on BG2
expected growth to slow to ~8% by 2027–2030, and his answer was mainly that the company tends to
beat expectations [C3-E05]; some demand is backed by NVIDIA's own financing of its customers
(dossier §E); Physical AI is still small and not broken out in earnings [C3-E34]. "No top in
sight" is his judgment, not a settled fact.

## 2. Judgment by area

| Area | Stage | Where growth comes from (or why it won't) | Time window | Who captures the value | Basis |
|---|---|---|---|---|---|
| Foundation models & inference | Accelerating | Users and per-query compute both climbing; inference-time thinking as a second exponential | 2025–2030 | Inference infrastructure, frontier labs; [inferred] API price drops squeeze model-layer margins | C3-E05 |
| Robotics & embodiment | Early | Synthetic data plus world models closing the data gap [C3-E15, C3-E22], against a cited 50M-worker shortage. Counter: GR00T N1's own authors call results mostly short-horizon desktop manipulation [C3-E16] | He says ~5 years; his "arrival" calls have run 17+ months without resolving (§3) | Compute platforms; actuator/magnet/motor supply chains (China, C3-E26) | C3-E04, C3-E05, C3-E16 |
| Autonomous driving | Accelerating (robotaxi scaling) | Fleet miles and data factories; reference architecture lowers OEM integration cost | 2026–2032 | Scaled operators/networks (Uber); platform suppliers | C3-E23; C3-E09 (2017 timeline missed) |
| World models & simulation | Generation accelerating but commoditizing; as a physical-AI data/eval engine, early | Simulators ground generative models at scale [C3-E04, C3-E22]; open models speed diffusion [C3-E30] | 2025–2030 | Compute-linked platforms (Cosmos, Omniverse) | C3-E04, C3-E14, C3-E30; challenged by the Physics-IQ audit, C3-E32 |
| Compute, chips & energy | Accelerating; he sees no top | General-to-accelerated shift; inference growth; performance-per-watt pricing under power limits | 2023–2030 | Platform firms (75% margin, C3-E34) over integrators (~11%, C3-E33); power | C3-E05, C3-E27, C3-E34 |
| US–China AI ecosystem | Diverging | US: platforms, frontier models; China: robotics hardware supply chain, "formidable" [C3-E26]. Q3 guidance excludes China data-center compute | — | US in platforms/models; China in hardware/manufacturing | [quoted] "nanoseconds behind," C3-E05; a stated interest in China re-entry (dossier §E) |

## 3. Prediction record

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| ~2003–2006 | Cg, then CUDA: GPUs become a general-purpose parallel computing platform | right (direction); took far longer than hoped — an "incredible disaster" for years, ~80% value drop in 2008 | C3-E01, C3-E03 |
| 2012–2016 | Bet on deep learning after AlexNet; rebuilt the compute stack; hand-delivered DGX-1 to OpenAI (2016) | right | C3-E02, C3-E04 |
| 2017-01 | With Audi, advanced AI cars on the road "starting in 2020" | wrong (timing); 2025-10 reset to Uber robotaxi fleets scaling from 2027 — pending | C3-E09, C3-E23 |
| 2018-11 | Crypto-boom channel inventory "will be corrected" | wrong/adverse — 2022 SEC settlement found inadequate disclosure of mining's boost to gaming revenue | C3-E10, C3-E11 |
| 2021 | Metaverse "much bigger" than the physical world; robots learn in Omniverse first | partly — consumer metaverse didn't happen; the robot-simulation half became his main business | C3-E12 |
| 2023-05 → 2024 | ~$1T of data centers (plus ~$2T of computers) shift to accelerated computing | right in scale/direction; 2026-03 company statement of $1T+ revenue visibility 2025–2027; a further ~$5T/year figure pending | C3-E13, C3-E01, C3-E27 |
| 2025-01 | "Useful" quantum computers: 15 years too early, 20 believable | self-corrected within 2 months; actual timeline pending | C3-E19 |
| 2025-01 → 2026-05 | "ChatGPT moment for robotics is coming" → "generalist robotics is here" → "big bang of physical AI is just around the corner" | pending — 17+ months repeated; GR00T N1's own paper calls results mostly short-horizon manipulation; earnings don't break out robotics | C3-E14, C3-E15, C3-E30, C3-E16 |

From the record: his direction calls on "computing demand will keep growing" have mostly held,
including through two multi-year "disasters" (CUDA, the 2008 downturn) before they paid off. His
dated "arrival" calls in his own bets — autonomy, robotics — have run early or missed by years;
the quantum case was a rare self-corrected miss outside his core domain, and the crypto-inventory
case was a disclosure failure, not merely an early call.

## 4. Where this persona is most likely wrong

- **Interests.** [inferred] He sells compute to every path; any "more compute solves it" judgment
  increases NVIDIA's revenue (dossier §E) — a property of the framework that happens to point the
  same direction as compute-intensive approaches (long inference, simulation, world models) and
  away from data-efficient or hardware-specific ones, stated as fact, not about his character.
- **Path dependence.** RIVA 128's simulation modeled deterministic circuits; "simulate first to
  close the data gap" may pay off more slowly in contact-rich manipulation than in domains with
  cleaner dynamics, such as locomotion.
- **Different era or setting.** His "zero-billion-dollar market" experience comes from an era when
  almost no one was watching. By 2026, Physical AI has drawn heavy capital from many players at
  once (dossier §A, §I); being early no longer means being alone.

## 5. One line for someone starting out

Pick problems impossible without a different way of computing, in a market that still looks like
zero dollars today — but don't take his timelines at face value, and remember that whoever sells
the compute will always see more compute as the answer.
