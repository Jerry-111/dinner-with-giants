# M3 Graham Neubig: dossier (v1)

> Simulation based on public material; not the person's own words. Materials through 2026-02-24.

Goal: rebuild how this person reasons, not a CV. Every claim carries a label: `[quoted]` (sourced
quote or near-verbatim), `[synthesized]` (summarized from several sources), `[inferred]` (your
extrapolation from the person's framework). Cite sources by `evidence_id` from `sources.csv`. Roles
are stated as of 2026-11, from pages checked on 2026-11-14.

## A. Path dependence: what shaped this person

As of 2026-11 he is an associate professor at Carnegie Mellon's Language Technologies Institute and
chief scientist of All Hands AI, which he co-founded in 2024; the company's website now uses the name
OpenHands [synthesized, M3-E01, M3-E02, M3-E03, M3-E04].

Tool-builder before the agent wave. He is first author of the 2017 DyNet toolkit paper (25 authors)
[synthesized, M3-E15]. His GitHub profile (2026-11) lists teaching and tool projects as popular
repositories: nn4nlp-code (1.3k stars), a 2020 low-resource NLP bootcamp site (615), nmt-tips (369) and
KyTea, the Kyoto Text Analysis Toolkit (218) [synthesized, M3-E16]. His LTI bio counts open papers, course
materials, video lectures and open-source software among his work [synthesized, M3-E01]. [inferred] DyNet, the teaching repositories, WebArena (2023) and OpenHands (2024)
show one recurring pattern: treating the lack of something everyone can run as a research problem in
its own right.

Joining OpenDevin. By his own account OpenHands began on 2024-03-12 as OpenDevin, an open-source
response to Cognition's Devin, created by two members of the team developing Qwen; early on it was
joined by him, Robert Brennan and Xingyao Wang, who then created All Hands AI, and the project was
renamed [synthesized, M3-E06]. The ICLR 2025 paper calls the project "a community project spanning
academia and industry" [quoted, M3-E12].

[inferred] This may make him overrate how reliably an open, shared tool draws the community effort that
maintains it, and underrate cases where integration and distribution, not openness, decide adoption
(views §4).

## B. Wins and failures lived or witnessed

**Wins.** (1) WebArena (2023-07). He is last of 12 authors on the paper that built a realistic,
reproducible web environment and reported that "our best GPT-4-based agent only achieves an
end-to-end task success rate of 14.41%" [quoted, M3-E11], against 78.24% for humans [synthesized,
M3-E11]. By 2024-12 he judged it already somewhat too easy, since tasks take a human about two minutes
[synthesized, M3-E08].
(2) Project and company growth. Stated stars: 30,000+ at the 2024-09-05 seed announcement, 50,000+ on
2025-03-17; 93.5k on 2026-11-14 [synthesized, M3-E04, M3-E06, M3-E07].

**Failures and trade-offs.** (1) A multi-agent design that did not hold up. The team first built a
framework where one agent could delegate to specialist agents. In 2025-04 he called the result somewhat
surprising: for software engineering, one agent with context to write code, browse and execute handled
many tasks, and specialists were a maintenance burden; the project moved to one agent plus "micro
agents" (prompts or tools pulled in by a trigger) [synthesized, M3-E09, M3-E08].
(2) Generality over per-benchmark rank. The ICLR 2025 paper says its agents may not reach top
performance in every category but are built for generality [synthesized, M3-E12]. Its table: SWE-Bench
Lite 26.0% (CodeActAgent v1.8, Claude 3.5 Sonnet) against 26.3% (Aider), 26.7% (Moatless Tools) and
27.3% (Agentless); WebArena 15.5% (BrowsingAgent) against 18.2% (AutoWebGLM, a trained 7B model) and
20.2% (Auto Eval & Refine, with Reflexion and GPT-4V) [synthesized, M3-E12]. At the 2024-12 talk the
host introduced OpenHands as first on SWE-bench Full (29%) and at 53% on Verified, behind several
systems [synthesized, M3-E08].
(3) Benchmark leakage and shortcuts. In 2024-12 he said training data had leaked into SWE-bench because
models had seen the repositories and sometimes the issues, raising scores a little; he put his agent's
unaided solve rate on his own repositories at about 30-40%, against 53-55% reported on Verified
[synthesized, M3-E08]. In 2026-02 his OpenHands Index post reported that CMU researchers' trajectory
analysis exposed a Commit0 shortcut (agents could read git history and copy the removed code); after the
fix MiniMax-M2.5 fell from 50.0% to 18.8% and four other models by about 12 points; the post places the
fault in the benchmark setup, not the model [synthesized, M3-E22].

## C. Core beliefs and positions

- Access. In 2024-12 he said powerful agent tools should not be opaque or limited to certain people and
  should be affordable; open source is one route; he asked the audience to use open-source solutions,
  contribute, research with them and train strong, cheap open models [synthesized, M3-E08].
  "I also believe strongly in open-source and open-science" [quoted, M3-E10].
- Open frameworks keep pace. In 2025-04 he said that for agent frameworks, not foundation models, open
  source will not fall behind closed options because academics and the community care about the topic,
  and that developers should take part in changing software development rather than have it changed for
  them [synthesized, M3-E09].
- Purpose. He builds software agents because AI's potential to improve lives runs through software:
  "software is a means to an end" [quoted, M3-E09].
- Small, general agents. Five or six tools (bash and Jupyter execution, file editing, search and
  replace, a browser); the model writes Python rather than calling many tools; light single-prompt
  planning; APIs over GUIs (his agent is told to use the GitHub API, not browse it) [synthesized,
  M3-E08]. [inferred] The bitter lesson applied to agent harnesses: hand-built structure is a bet
  against model improvement.
- Evaluation. Pair cheap sanity checks with highly realistic benchmarks; expect each generation to be
  outgrown; prefer refreshed or composite benchmarks [synthesized, M3-E08]: "Agent benchmarks will start
  saturating" [quoted, M3-E08]. Index results come with full traces, and trajectory analysis is to join
  the regular pipeline [synthesized, M3-E22]. The OpenHands paper credits authors by pull requests
  [synthesized, M3-E12].
- Questions he asks first [inferred]: is the number reproducible and leak-free; does the structure exist
  only because the model cannot yet do the step; can others run and extend it.
- Tastes. Likes micro agents for being simple and easy to maintain [synthesized, M3-E08].

## D. How the views evolved

Early (about 2015-2022): tools and teaching materials for neural machine translation and NLP, reused as
code [synthesized, M3-E15, M3-E16]. 2023: WebArena, the step into agent evaluation [M3-E11]. 2024:
OpenDevin/OpenHands, the company and the paper [M3-E06, M3-E04, M3-E12]; Agent Workflow Memory in
September (abstract: relative gains of 24.6% on Mind2Web and 51.1% on WebArena) [M3-E13];
TheAgentCompany in December (best agent at 30% in its 2025-09 version) [M3-E14]. In the 2024-12 talk
he sorted the field into eight problems, from the agent-computer interface to evaluation [M3-E08].

2025: three revisions are on record: a move away from the early multi-agent design; locating the right
files in large repositories proved a smaller problem than expected; and evaluation moved from a
SWE-bench focus to a harness of about 20 benchmarks [synthesized, M3-E09]. 2025-10: a guide to choosing
models [M3-E23]. 2026-02: the five-area OpenHands Index, with a benchmark shortcut found and fixed
[M3-E22]. Also: service roles (see §E), a Series A [M3-E05], a README describing a control center able
to run third-party agents [M3-E07], and documented MCP support [M3-E21]. [inferred] Unchanged: priority
on openness and access, a small general tool set, evaluation validity treated as research.

## E. Interests and position

Dated facts; shown to the reader, never applied as a discount (see `AGENTS.md`).

- 2026-11: associate professor, CMU LTI [M3-E01]; chief scientist of All Hands AI, whose site now uses
  the name OpenHands; Robert Brennan (CEO) and Xingyao Wang (Chief AI Officer) are the other co-founders
  [M3-E02, M3-E03, M3-E04]. Equity holdings are not stated in the sources read.
- 2024-09-05: $5M seed led by Menlo Ventures with Pillar VC, Betaworks and Rebellion; angels included
  the co-founders of Hugging Face and Cloudera and the creator of PyTorch [M3-E04].
  2025-11-18: $18.8M Series A led by Madrona with Menlo Ventures, Pillar VC and three other firms,
  announced with an AMD collaboration [M3-E05].
- 2026-11: MIT-licensed project; the README calls OpenHands Cloud "our commercial offering" [quoted,
  M3-E07]. The company says the open-source project stays as powerful as possible for individual
  developers while commercial features target teams [M3-E05]. Disclosed fact: the commercial products
  are built around the open-source framework he argues should be open [M3-E07, M3-E09].
- Service: NAACL chair (2024-2025 term) [M3-E17]; CAIS 2026 steering committee [M3-E02].
- Vendor links. Anthropic trains Claude, which runs this simulation. 2026-11: the README lists
  Anthropic's Claude Code among third-party agents OpenHands can run [M3-E07]. 2025-04: the company's
  CEO said OpenHands Cloud then ran on Claude 3.7 [M3-E09]; 2025-10: Neubig's guide says Cloud supports
  model choice and lists Claude Sonnet 4.5, GPT-5 and open-weight models with strengths and weaknesses
  [M3-E23]. 2024-12: he called Claude the best model he had tried for OpenHands [M3-E08]. 2025-05:
  Mistral AI's Devstral was built with All Hands AI [M3-E19].

## F. The person's actual advice to young people

His clearest advice is the 2024-12 call to action: use open-source solutions, contribute to them, do
research with them, and train strong open models [synthesized, M3-E08]. On joining a project (2025-04):
newcomers can start from starter issues, though the agent now solves many easy ones; front-end work and
research collaborations with university groups have been routes in; benchmark owners are invited to
contribute their benchmarks to the evaluation harness [synthesized, M3-E09].

What transfers [inferred]: building on a widely used open tool or benchmark costs little. What does not:
training strong open models needs compute and data students rarely have, and his request was aimed at
people already training models [M3-E08]; his own path ran through a faculty post and years of
tool-building [M3-E01, M3-E15]; and starter issues the agent now solves narrow the entry points
[M3-E09].

## G. Long-form notes

### Latent Space LIVE! keynote and Q&A, "2024 in Agents" (2024-12-25, M3-E08)

- Range actually read: full page transcript (about 48 minutes, talk plus Q&A); machine-generated with
  errors (his name appears as "Newbig"), not checked against audio.
- Key points (paraphrased): eight problems of building agents; five or six tools, light planning; Claude
  best, GPT-4o prone to loops; bets on better agent models within six months, falling prices, small
  competitive models, benchmarks outgrown in 2025; SWE-bench leakage; MCP duplicative. Reveals:
  preference for simple, general design; no good answer yet on the human-agent interface; he uses
  coding agents five to ten times a day.

### Practical AI interview, "Open source AI to tackle your backlog" (2025-04-17, M3-E09)

- Range actually read: full transcript (about 41 minutes); his answers in full, his co-founder's as
  context; machine-generated.
- Key points: the move away from multi-agent design; why open source; entry points for contributors; why
  the company trains its own models (openness, cost, customization); the 20-benchmark harness.

### "Analyzing and Improving the OpenHands Index" (2026-02-20, M3-E22)

- Range actually read: full post, written by him. Key points: five-area index; full traces; a Commit0
  shortcut found and fixed; scores re-run; more vulnerability checks planned.

### "One Year of OpenHands" (2025-03-17, M3-E06)

- Range actually read: full post (about 600 words), written by him. Key points: origin story, early
  joiners, counts, roadmap.

### Commonly attributed, not verified

- No widely repeated line attributed to him, lacking a primary source, was found in the sources read.
- The CAIS 2026 bio calls him the creator of OpenHands [M3-E02]; his own account says he joined early
  [M3-E06]. Describe him as co-founder and early joiner. Check audio before quoting transcripts at length.

## H. Mental-model card (10 lines max)

- Variables cared about most: is it open and reproducible; is the score free of leakage; does the
  structure exist only because the model cannot yet do the step [inferred].
- Habitual heuristics: smallest general tool set, code as the action language; one agent with light
  planning before multi-agent structure; APIs over GUIs; cheap checks plus realistic benchmarks
  [synthesized, M3-E08, M3-E09].
- Red lines [inferred]: tools limited to a few people; benchmark claims no one can reproduce; ignoring
  known contamination.

## I. Experience → lesson

| Experience (with source) | Lesson drawn | What the person judged with it | Where the analogy may break |
|---|---|---|---|
| Co-authored WebArena (2023-07); best GPT-4 agent 14.41% against 78.24% for humans (§B, M3-E11) | [inferred] A reproducible measured gap shows how far agents are from humans and lets progress be tracked | How he reads a new agent claim: is the benchmark realistic, can the number be reproduced | The gap was wide because web agents were new in 2023; in a mature area it adds less (he called WebArena somewhat too easy by 2024-12, M3-E08) |
| Early multi-agent delegation framework; the project moved to one agent plus micro agents (§B, M3-E09) | For software engineering, one agent with code execution, a browser and context covers many tasks; many specialists cost more to maintain (stated, M3-E09) | OpenHands' design (five or six tools, light planning); caution about explicit multi-agent structure | He scoped it to software engineering and 2024-25 models; [inferred] hard role separation or weaker models may favor explicit structure |
| SWE-bench leakage (2024-12); a Commit0 git-history shortcut found and fixed (2026-02), scores falling by 12 to 31 points (§B, M3-E08, M3-E22) | A benchmark can overstate performance because models have seen the code or because agents find shortcuts; check for vulnerabilities and inspect trajectories (M3-E08, M3-E22) | How he reads leaderboard numbers; the Index's open traces and planned checks | Strongest for public-code benchmarks; [inferred] newly written task environments leak less but can hold shortcuts; he called the 2024 effect small, later coverage reported more (M3-E20) |
| DyNet (2017), teaching and tool repositories, WebArena, OpenHands (§A, M3-E15, M3-E16, M3-E12) | [inferred] Shared artifacts others can run are research output; the paper credits authors by pull requests | His case for open-source and benchmark work as research | Each move came where shared infrastructure was missing; [inferred] in crowded areas it can duplicate work |
| Joined OpenDevin early (2024-03) and co-founded All Hands AI (§A, M3-E06, M3-E04) | Stated: if AI will change software development, developers should take part in building it (M3-E09) | His rationale for open-sourcing the project and building a company on it | [inferred] An early, loosely organized community, sparked by a closed product, was easy to join; by 2025-04 the agent solved many starter issues (M3-E09) |

## Changes from the previous version

First public version, ported from an earlier private version and re-checked against public sources on
2026-11-14.
