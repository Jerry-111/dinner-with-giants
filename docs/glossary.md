# Glossary / 术语表

Canonical terms used across the protocol, templates, tooling and examples. When a Chinese term is shown, it is the term used in Chinese-language runs and in `README.zh-CN.md`.

## Roles

| Term | 中文 | Meaning |
|---|---|---|
| user | 用户 / 决策者 | The person whose decision the run is about. Their context lives in `workspace/context/` and never in the public repo. |
| orchestrator | 主执行者 | The coding agent session (Claude Code, Codex, …) that runs the protocol: writes the scope, launches sub-agents, moves files between rounds. |
| persona agent | 人物 agent | A sub-agent that simulates one persona from that persona's folder only. |
| baseline analyst | 基线分析师（Z1、Z2） | A sub-agent with no persona that scores the same options. The persona layer is measured against it. |
| crux agent | 争点 agent | A fresh sub-agent that has read no persona material; turns round-1 disagreements into cruxes and seats the tables. |
| scribe | 记录员 | A fresh sub-agent that writes the two versions of each table's notes. |
| judge | 裁判 | A fresh sub-agent that scores each post with a fixed scorecard. Sees names. |
| fact-checker | 核查 agent | A fresh sub-agent that checks claims against primary sources (three passes). |
| lead writer | 主笔 | A fresh sub-agent that writes the report from the aggregated files. |
| reviewer | 审读 | A fresh sub-agent that did not write the report and did not read the debate; finds problems, does not rewrite. |

## Persona material

| Term | 中文 | Meaning |
|---|---|---|
| persona | 人物 | A reconstruction of how a person (or an archetype) reasons. Always a simulation, never the person. |
| dossier | 人物档案 | `dossier.md`, sections A–I: path dependence, wins and failures, core beliefs, evolution of views, interests and position, advice to young people, long-interview notes, mental-model card, experience → lesson. |
| views | 领域判断 | `views.md`: overall judgment, per-domain judgment table, dated prediction record, where this persona is most likely wrong. |
| conversation | 模拟会谈 | `conversation.md`: a simulated long conversation with the user, ending with a takeaway table. |
| card | 人物卡片 | `card.yaml`: machine-readable summary printed at the top of every prompt and every post. |
| stance line | 立场来源 | One line on the card: lived experience only, no evaluation. Printed at the top of every post. |
| interest line | 利益 | One line on the card: dated facts about the persona's interests. Shown, never used as a discount. |
| sources table | 来源表 | `sources.csv` (and `sources_v<N>.csv` for later versions), fixed columns, written with Python's `csv` module. |
| prediction record | 预测记录 | 4–8 dated predictions with outcomes; used to describe how far direction and timing calls can be trusted. |
| not independent of | 不独立 | Personas sharing a company, lab or long collaboration; cannot be the only representatives of one side at a table. |

## Evidence labels

| Label (English runs) | 中文标注 | Meaning |
|---|---|---|
| `[quoted]` | 【原话】 | A sourced quote or near-verbatim statement. English quotes stay under 15 words; at most one quote per source. |
| `[synthesized]` | 【归纳】 | Summarized from several public sources. |
| `[inferred]` | 【推断】 | The agent's extrapolation from the persona's framework. |
| `[writer]` | 【主笔】 | The lead writer's own judgment in the report. |

The linter accepts either the English or the Chinese form.

## Run files

| Term | 中文 | File |
|---|---|---|
| scope (run brief) | 本轮共同说明 | `scope.md`: the task brief every sub-agent reads. |
| evidence brief | 共享底稿 | `evidence/brief.md`: shared facts, numbered `F1, F2, …`, each with a source. Kept under 20 KB. |
| errata | 核查更正 | `evidence/errata.md`, `evidence/errata_B.md`: corrections from fact-check passes ① and ②. |
| rubric | 预注册评分规则 | `rubric.json`: options, dimensions, scale, levers, aggregation rules, non-independent groups. Frozen once personas submit. |
| options | 选项 | What is being scored (directions, offers, plans…). IDs are defined in the rubric. |
| dimensions | 维度 | Sub-scores per option, defined in the rubric (for example impact, timing, fit). |
| levers | 杠杆 | Optional: each persona splits 100 points across the factors that will most decide the outcome. |
| named questions | 点名问题（Q1…） | Questions the user wants answered head-on. |
| claims to test | 要检验的说法 | Claims the user heard from others and wants checked (attributed only as "a friend", "a mentor", …). |
| reversal signals | 改判信号 / 改主意信号 | Observable facts that would change the conclusion. |
| `RUN_METADATA.md` | 运行记录 | Timeline, inputs, independence and limitations. Required in every run. |

## Rounds

| Code | Term | 中文 | Meaning |
|---|---|---|---|
| R0 | card extraction | 抽卡片 | Persona agents read their own folder and write `card.yaml`. |
| R1 | independent scoring | 独立打分 | Each persona and baseline scores every option alone. |
| X | crux map and seating | 争点与排桌 | Disagreements become 2–9 cruxes; personas are seated at debate tables. |
| A | opening | 开场 | One post per table per persona. |
| B | exchange | 交锋 | Reply to the strongest opposing post; ask one named persona a question; optional interjections at other tables. |
| — | interjection | 插话 | A short post at a table one does not sit at; only allowed with a new argument or new evidence. |
| ② | in-debate fact-check | 核查② | Between B and C, so corrections arrive before anyone changes a score. |
| C | closing | 收束 | Concessions, holds, answers, the fact that would settle the disagreement, bridges. |
| S | scribe notes | 桌记录 | Two versions per table: persona-facing (`summary/`, never says who persuaded whom) and full (`summary_full/`). |
| OT | overtime | 加时 | The sharpest pair per table goes 2–3 more rounds; cross-table replies also go here. |
| R3 | private re-score | 私下重估 | Personas re-score after reading persona-facing notes; every change must cite and restate the argument that caused it. |
| ③ | post-R3 fact-check | 核查③ | New claims plus an experience check (is the story really in the dossier?). |
| J | judging | 裁判 | Per-table verdict and per-post scorecard. |
| W | report | 写报告 | Lead writer; scores only from the aggregated `summary.md`. |
| — | review | 审读 | Independent review before delivery. |

## Debate mechanics

| Term | 中文 | Meaning |
|---|---|---|
| crux | 争点 | A question that people disagree on and that facts can move. |
| debate table | 辩论桌 | A named group of 4–6 personas debating one crux. |
| experience argument | 经验论证 | What I lived through (with dossier section), what it taught me, why it applies here, where the analogy may break. A legitimate argument, judged by whether the analogy holds. |
| source challenge | 来源质询 | "Is this evidence published by you or your own company? Is there an independent source?" The challenged persona produces one or retracts. |
| self-check | 自查 | A budgeted web search about one specific claim, logged in the post's JSON. |
| retraction | 收回 | Withdrawing a claim after a source challenge or a correction. |
| verdict | 判定 | Per point of an opposing post: `accept` or `reject` (no "partially"; the tooling still counts a legacy `partial` value from older runs). |
| empty concession | 空让步 | Accepting an argument in text while leaving the score unchanged. Tracked. |
| social reason | 社会理由 | Changing a score because others changed or because a majority agrees. Not counted as persuasion; flagged. |
| `held_despite` | 文字接受、分数不动 | R3 field listing accepted arguments that did not move the score, with the reason. |
| `intended_moves` | 意图改分 | C-round field; compared with actual R3 moves. |
| persona–baseline gap | 人物 − 基线 | Median persona score minus baseline score per option: what the persona layer adds over asking the model directly. |
| fidelity test | 保真度测试 | Rebuild a persona from sources before a cutoff date and predict the person's public statements after it; blind-graded. |
| reader pack | 读者版 | A one-page version for the user to read; the full record stays in Git. |
| calibration log | 反馈记录 | `workspace/context/calibration_log.md`: the user's feedback over time; newest at the bottom; later runs follow it. |
| light mode | 两两质疑 | A cheaper alternative to debate tables: pairwise critiques in one wave, replies in a second wave sent only after every critique is in (`protocol/03_debate_tables.md`). |
| consult mode | 快速咨询 | "What would persona X say about my choice?" in minutes, without a full run. |
