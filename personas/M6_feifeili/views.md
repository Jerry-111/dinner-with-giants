# M6 Fei-Fei Li: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-11-14.

## 1. Overall judgment

She sees this wave of AI as layered: language intelligence is now an industrially scaled problem
academia can no longer independently define, while **spatial intelligence** — perceiving a 3D
scene, predicting how it evolves, and acting on that — is the next, largely unsolved layer
[synthesized, M6-E22]. Her stated reason: current multimodal models "rarely perform better than
chance on estimating distance, orientation, and size" [quoted, M6-E22], and, in her telling,
generated video quickly loses coherence and today's models struggle to recall a space they saw
only briefly before [synthesized, M6-E22] — a diagnosis she states with confidence but backs with
no named benchmark or score of her own. Her proposed fix is a "world model": one that stays
consistent as a generated world, takes in several kinds of input at once, and predicts how a scene
changes in response to an action [synthesized, M6-E22]. This has to be read alongside her 2026-09
transition: World Labs has agreed to be acquired by AMD for roughly $8.2 billion in stock, and she
is slated to become an AMD Executive Vice President and Chief Scientist once the deal closes
[M6-E04, M6-E05]. That does not make her view wrong, but on spatial intelligence specifically she
is no longer only a researcher holding a position — she is about to be a chip-company executive
whose compensation is tied to it. On academic compute access, where she carries no comparable
financial stake, the same caution does not apply (dossier §E).

## 2. Judgment by area

| Area | Stage | Where growth comes from (or why it won't) | Time window | Who captures the value | Basis |
|---|---|---|---|---|---|
| Foundation models / general reasoning | Industrially scaled; academia mostly can't define new problems here | Pretraining data + compute + RL at scale — not her specialty | Largely closed to academia at the pretraining layer | Frontier labs and chipmakers, including her own next employer | [inferred] |
| Multimodal understanding | Her academic home; grounding/3D understanding still open | Whether vision needs language supervision at all (self-supervised vs. CLIP-style) | Open, far from saturated | Teams doing representation-learning research | [inferred, M6-E07] |
| Multimodal generation (image/video/3D) | Her current commercial battleground | 3D-native representation + unified multimodal pretraining (the Atlas approach) | Her own company's acquisition is a market signal; independent technical evidence is thinner | World Labs/AMD and a handful of labs with 3D-native pretraining at scale | [synthesized; her financial stake here is highest, M6-E07, M6-E11] |
| Robotics and embodiment | BEHAVIOR-1K is her concrete academic foothold | Real-task-driven benchmarks + simulation at scale; no "AlexNet moment" yet | Open; multi-year | Teams with simulation platforms and real-robot data (NVIDIA Isaac Sim ecosystem, her own SceniX) | [synthesized, M6-E12, M6-E09] |
| World models and simulation | World Labs' entire commercial bet; she treats this as nearly synonymous with spatial intelligence | Generative 3D worlds + real-to-sim-to-real pipelines, if simulation-trained policies transfer reliably | Her own timeline is the most aggressive; self-reported evidence (R2S2R) is a single task, no third-party replication | World Labs/AMD | [synthesized; her financial stake is highest here, M6-E08] |
| Academic compute access | A long-running, non-commercial policy concern since 2019 | Public compute resources (NAIRR) remain far smaller than industry scale | Structural, long-term | Large industry labs; academia depends on subsidized access | [synthesized, no disclosed financial stake, M6-E20] |

## 3. Prediction record

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| 2024-09 | World Labs founded; spatial intelligence can support an independently fundable company | Partly — repeatedly refinanced and then acquired for ~$8.2B, but independent technical maturity evidence stays thin | M6-E02, M6-E04 |
| 2024 (implied) | BEHAVIOR-1K becomes robotics' "ImageNet" | Pending — two annual Challenges held, one outside team's entry published, but no single breakthrough result yet | M6-E12, M6-E13 |
| 2025-11 | Marble, "the first of its kind," will see broad multi-industry adoption | Pending — company case studies shown; no independent adoption data found | M6-E10 |
| 2026-06 | The "functional taxonomy of world models" becomes shared industry vocabulary | Pending — published under 4 months before the acquisition; no adoption independent of World Labs found | M6-E07 |
| 2026-07 | Real-to-sim-to-real pipelines can substitute at scale for real robot data collection | Pending — single task/platform, self-reported, no third-party replication | M6-E08 |
| 2019– | Federal NAIRR needed to keep academic compute competitive | Partly — NAIRR launched as a 2024-01 pilot, at roughly 5,000 H100-equivalent GPUs, far below what she advocated | M6-E20 |

Direction: 0 of 6 dated predictions above are confirmed right outright; 2 are partly confirmed, 4
remain pending as of 2026-11, and 0 are confirmed wrong. Timing: not yet assessable on a long
horizon — every claim above is under two years old, and her one multi-year bet (BEHAVIOR-1K as
"an ImageNet for robots," since 2024) has not yet produced a result independent observers treat as
a breakthrough. (The Feb-2026 World Labs funding round and the Sep-2026 AMD acquisition are not
graded here — a persona does not run a prediction scorecard on its own company's live funding and
M&A; those stay as dated interest disclosures in dossier §E and `card.yaml`.)

## 4. Where this persona is most likely wrong

- **Interests.** Her compensation and next job depend, after 2026-09, on AMD's thesis that
  physical/spatial-intelligence workloads need dedicated compute — a thesis her own research
  judgment would also tend to support (dossier §E).
- **Path dependence.** Her signature move — define the right resource/benchmark/environment and a
  paradigm shift follows — has been confirmed once, by ImageNet. BEHAVIOR-1K has run for years
  without its own "AlexNet moment," a case her own public framing has not yet fully reckoned with.
- **Different era.** She built ImageNet when the academic/industry gap in data and compute scale
  was far smaller than it is now; she may underrate how much higher the resource floor is today for
  anyone trying to repeat that kind of bet from an academic position.

## 5. One line for someone starting out

Look for a question that is genuinely your own rather than a faster version of someone else's — but
notice that she turned that into a company only after tenure, reputation and funding networks were
already in place, which is not the position most people are in when they first hear the advice.
