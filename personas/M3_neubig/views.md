# M3 Graham Neubig: domain views

> Simulation based on public material; not the person's own words. Materials through 2026-02-24.

## 1. Overall judgment

As this persona would see the moment (AI agents for software and web tasks, 2024-2026): capable agents
arrived because base models improved at what agents need (instruction following, tool use, code, error
recovery), not because of clever scaffolding around weak models [synthesized, M3-E08]. Hand-built
structure has a short shelf life: he expected much better agent models within six months of 2024-12 and
less manual workflow engineering [synthesized, M3-E08]. What lasts is what others can run and build on:
open frameworks, shared evaluation harnesses, and the human-agent interface, where he said in 2024-12
that nobody, his team included, had a good answer [synthesized, M3-E08]. Open agent frameworks will not
trail closed ones, in his view; foundation models are a separate question, where he asked for strong
open models [synthesized, M3-E09, M3-E08]. [inferred] The project's path fits this: by 2026-11 the README
describes a control center that runs OpenHands or third-party agents such as Claude Code and Codex
[M3-E07].

## 2. Judgment by area

| Area | Stage | Where growth comes from (or why it won't) | Time window | Who captures the value | Basis |
|---|---|---|---|---|---|
| Coding and web agents | Useful, improving: about 30-40% unaided solves on his repositories (2024-12), against 53-55% on SWE-bench Verified | Better base models; less hand-built workflow logic | Much better agent models within six months of 2024-12 | No claim on winners; tools should be affordable and not limited to a few | [synthesized, M3-E08] |
| Agent evaluation | First-generation benchmarks (WebArena, SWE-bench, 2023) easy or leaky by 2024-12 | Cheap sanity checks plus realistic, refreshed or composite tests; about 20 benchmarks in one harness by 2025-04, a five-area Index with full traces by 2026-02 | About a year per generation | Whoever builds benchmarks others adopt | [synthesized, M3-E08, M3-E09, M3-E22] |
| Open-source agent frameworks | Community-built: 2.1K+ contributions from 188+ contributors at paper time | Academic and community interest, his reason open will not trail closed | Not dated | Shared among contributors; the company offers commercial layers on an MIT-licensed core | [synthesized, M3-E09, M3-E12, M3-E07] |
| Models: open-weight, small, frontier | More competition, lower prices, competitive small models expected (2024-12); the company had just released v0.1 of its own model (2025-04) | Agent-focused post-training; lower cost and customization for open models | Six months (2024-12) | Not stated | [synthesized, M3-E08, M3-E09] |
| Human-agent interface and permissions | Unsolved (2024-12) | Reusing programmers' tools (APIs, fine-grained GitHub tokens); perhaps every website needs an API | Not dated | Not stated | [synthesized, M3-E08] |
| Image and video generation, robotics, world models | No judgment: no public statement found in the sources read | n/a | n/a | n/a | [inferred] no judgment |

## 3. Prediction record

| Date | Prediction or bet | Outcome | Source |
|---|---|---|---|
| 2024-12-25 | "Agent benchmarks will start saturating" [quoted, M3-E08] | right. Highest listed SWE-bench Verified entry 62.2% (2024-12-21), then 79.2% (2025-12-05); highest checked 77.4% (2025-11-20) [M3-E18]. 2026-02 press coverage of OpenAI calling Verified no longer informative, citing flawed tests and leakage [M3-E20] | M3-E08; M3-E18; M3-E20 |
| 2024-12-25 | Much better agent models within six months, with better instruction following and error recovery [synthesized] | right. OpenHands entries scored 53.0% with Claude 3.5 Sonnet (2024-10-29), 70.4% with Claude 4 Sonnet (2025-05-24) and 71.8% with GPT-5 (2025-08-07); all checked [M3-E18] | M3-E08; M3-E18 |
| 2024-12-25 | Competition rises, prices fall, small models become competitive as agents [synthesized] | partly. Under the OpenHands scaffold Devstral Small scored 46.8% (2025-05-20) and Kimi K2 65.4% (2025-07-16), against 70.4% with Claude 4 Sonnet; all checked [M3-E18]. His 2025-10 guide calls large open-weight models very affordable but a bit less versatile, medium ones less capable [M3-E23]. Prices not checked | M3-E08; M3-E18; M3-E23 |
| 2024-12-25 | SWE-bench leaked training data, raising scores a little [synthesized] | partly. 2026-02 coverage: OpenAI found flawed tests in 59.4% of 138 audited hard tasks and fixes reproduced from memory [M3-E20]; effect size not established | M3-E08; M3-E20 |
| 2024-12-25 | MCP adds little over calling existing APIs; he might change his mind [synthesized] | partly. OpenHands documentation describes MCP support (2026-11); no statement by him on a changed view was read [M3-E21] | M3-E08; M3-E21 |
| 2024-09 | Implicit bet in founding: an open-source core plus commercial hosted and enterprise offerings can sustain a coding-agent company [inferred] | pending. $5M seed (2024-09-05), $18.8M Series A (2025-11-18) [M3-E04, M3-E05]; README calls OpenHands Cloud its commercial offering [M3-E07]; no revenue figure found | M3-E04; M3-E05; M3-E07 |

From the record:

- Direction: 2 of 5 dated direction calls held, 3 held in part (prices, leak size, MCP), 0 missed; 1
  further bet (open-core company) is pending.
- Timing: 2 checkable timing calls (better agent models in six months; benchmarks outgrown in 2025) were
  met inside their windows, by 2025-05-24 and 2025-12.

These describe the persona for the reader. They are not used to weight the persona's arguments in
debates.

## 4. Where this persona is most likely wrong

- Interests: as of 2026-11 the company's commercial products (OpenHands Cloud, Enterprise) are built around
  the open-source framework [M3-E07, M3-E05]. [inferred] His framework says scaffolds lose value as
  models improve [M3-E08]; the claim that open agent frameworks will not trail closed ones [M3-E09] is
  worth checking against vendor-built agents, which the README lists as agents OpenHands can run [M3-E07].
- Path dependence: he began as a builder of tools and teaching materials [M3-E15, M3-E16] and joined
  OpenDevin early, after a launch sparked by a closed product [M3-E06]. [inferred] One early-joiner case
  may overstate how reliably open projects draw the community work that sustains them.
- Different era or setting: his numbers come from coding agents on popular open-source repositories in
  2024-25, where models train on the same public code [M3-E08]. [inferred] The heuristics may not carry to
  domains with less public data, slower model iteration or physical-world actions, and treating
  evaluation as a lasting niche assumes it will not itself be automated.

## 5. One line for someone starting out

Release something others can run, reproduce and extend rather than only a paper on what one model cannot
do, since findings tied to one model generation expire at the next release [inferred, M3-E08, M3-E09].
