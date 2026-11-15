# K4 Andrej Karpathy: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-10-12.

## 1. Overall judgment

As Karpathy would frame this moment: less like electricity or the industrial revolution, more a
new computing paradigm after hand-written code — Software 2.0 "programs" with data, Software 3.0
with a prompt, and in general whatever can be verified gets automated (dossier §C) [synthesized,
K4-E18]. Far from topping out, he compares today's LLMs to 1960s timesharing and puts the
industry's realized potential in the low single-digit percent (dossier §C) [synthesized, K4-E17].
The driver has moved from scaled pretraining to RL with verifiable rewards plus test-time compute,
now to "environments"; the bottleneck moved from architecture to data, loss and verifiability
[synthesized, K4-E19, K4-E12]. Progress is gradual — digital first, physical later, no visible
kink in GDP — and uneven: spiky where verifiable, reliability climbed one nine at a time
[synthesized, K4-E04, K4-E06]. Competitive edge sits with the data engine, not the data itself
(dossier §B/§C) [synthesized, K4-E20]: frontier labs capture general capability, specialized
players capture value through private data and feedback loops, and thin application layers get
absorbed by the next model [synthesized, K4-E16]. As of October 2026 he also argues the gap
between frontier labs' internal capability and what the public has seen is wide and growing —
"the external world has seen the preview" — though this rests on one X post known only secondhand
[synthesized, K4-E30].

## 2. Judgment by area

| Area | Stage | Where growth comes from (or why it won't) | Time window | Who captures the value | Basis |
|---|---|---|---|---|---|
| Foundation models & pretraining | Accelerating; architecture near a plateau | RLVR plus test-time compute, synthetic "environments," efficiency gains | Next few years, by his account | A handful of frontier labs; open weights trail | [synthesized, K4-E21, K4-E19, K4-E25] |
| Coding agents | Past the inflection point | Code is text, verifiable, tooled; "didn't work" to "works" in ~2 months, winter 2025 | From December 2025 | Model providers, engineers who review output; thin wrappers absorbed | [synthesized, K4-E15, K4-E16] |
| Office & computer-use agents | Early; "year of agents" overstated | Missing multimodality, computer use, continuous learning; no code-diff equivalent for visual tasks | Decade-scale: "this is more accurately described as the decade of agents" [quoted, K4-E04] | Application products with private data and feedback | [synthesized, K4-E17] |
| Research automation | Early | Fixed-metric experiments delegable to an agent; transfer to larger scale unproven | Small scale now; large-scale unresolved | Problem-framers; labs with compute | [synthesized, K4-E13, K4-E14; challenges, K4-E29] |
| Robotics & embodiment | Early, long-run bullish | Wheeled-to-humanoid easier than it looks; gaps are actuators and motion data | Behind digital agents: factory, B2B, home | Hardware-scale firms with fleet data engines | [synthesized, K4-E12] |
| Self-driving | Early deployment, already "a bit AGI" | Linear climb of equal "nines," not exponential; backs Tesla's software bet over Waymo's hardware bet | ~A decade, demo to product | Fleet-scale data-engine firms that deploy widely | [synthesized, K4-E05, K4-E06, K4-E12] |
| World models & simulation | No stated position; as agent input: early | Sim is a ground-truth source but RL exploits its gaps; his own MenuGen was absorbed | — | [inferred] multimodal labs; firms with interaction data | [inferred, K4-E07, K4-E16] |

## 3. Prediction record

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| 2013 | 30-min zero-intervention self-driving demo; expected success soon | wrong (timing) — still not declared solved a decade-plus later | K4-E05 |
| 2016–17 | Universe: agents would operate websites via pixels, mouse, keyboard | partly right — failed then; revived with LLMs, still incomplete (computer use) Oct 2025 | K4-E03, K4-E04 |
| 2017-11 | Software 2.0: neural nets keep eating hand-written software | right (direction) — Autopilot's C++ gave way to nets; extended into "Software 3.0" | K4-E26 |
| 2022-03 | Architecture stays broadly stable, just bigger, for decades; most people fine-tune a handful of foundation models | partly right so far (~4 of a stated 33-year window) | K4-E25 |
| 2022-10 | Vision is necessary and sufficient; most lidar users drop it eventually | pending — not independently checked here | K4-E07 |
| 2024-09 | Tesla actually ahead of Waymo; revenue/scale will show it in ~a decade | pending | K4-E12 |
| 2024-09 | Eureka Labs' first course ships "early next year" (2025) | wrong — still unreleased as of May 2026 | K4-E12, K4-E32, K4-E21 |
| 2025-10 | Decade of agents; coding agents help only marginally with novel code | mixed — the short-term coding claim reversed in ~2 months, by his own account; decade claim pending | K4-E04, K4-E15 |

**Direction** is fairly strong — Software 2.0, foundation-model concentration, computer-using
agents and coding automation all landed right or partly right — but the sample is small (8 calls)
and mostly self-reported in hindsight. **Timing** is mixed and not one-directional: early and too
optimistic on self-driving, Universe and his own course; too cautious on coding agents in October
2025, reversed within two months. He seems to have settled on things moving faster than expected
in verifiable, digital domains, and slower wherever a physical-world long tail is involved; many of
his predictions now use decade-length windows.

## 4. Where this persona is most likely wrong

- **Interests.** Each of these three bullish calls — LLM pretraining, RL "environments," and
  Tesla-style vision-only driving with fleet data — touches an area where he also has a disclosed
  financial or employment interest (dossier §E): his current employer, an investment, and a former
  employer, respectively [K4-E21, K4-E24, K4-E12]; shown here as a dated fact, not used to discount
  the calls.
- **Path dependence.** Having personally lived "general eats specialized" several times (neural
  nets over hand-written Autopilot code, a general image model over his own MenuGen, his own
  pivot from 3D to vision-language), he likely underrates durably specialized approaches —
  world-model-centric methods, learning from video and interaction, long hardware-heavy research
  [inferred].
- **Different era or setting.** His instincts formed in 2010s US frontier labs, when compute was
  comparatively abundant and the field was small. He has barely addressed China's research
  ecosystem, compute-constrained efficiency, or regulatory and capital cycles outside the US — one
  exception being a single approving comment on a Chinese lab's training efficiency [K4-E19].

## 5. One line for someone starting out

Follow verifiability and the data engine: bet on places a general model can't yet reach but where
you can build verification and a closed loop, and stay away from single-point products the next
general model will absorb.
