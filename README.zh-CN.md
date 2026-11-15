<div align="center">

# dinner-with-giants · 大佬怎么看

**你约不到的大佬们，帮你一起拿主意。**<br>
把大佬请上桌，让他们辩论，每句话都留底。

[English](README.md) · **简体中文**

[![CI](https://github.com/Jerry-111/dinner-with-giants/actions/workflows/ci.yml/badge.svg)](https://github.com/Jerry-111/dinner-with-giants/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Personas](https://img.shields.io/badge/personas-26-8a63d2.svg)](personas/)
[![Runs in](https://img.shields.io/badge/runs%20in-Claude%20Code%20%7C%20Codex-d97757.svg)](#快速开始)

<img src="docs/assets/social-preview.png" alt="大佬怎么看：你约不到的大佬们，帮你一起拿主意" width="820">

</div>

如果可以和任何人吃一顿饭，不论在世与否，你会请谁？这个仓库把他们请到你的问题周围：20 位在世的 AI、科技和投资界大佬，加上 6 位历史人物，每一位都从本人的公开记录重建。

每个大佬都有偏见，而这正是他们的价值。黄仁勋看问题，先看算力成本；Yann LeCun 先看机器能不能像人一样从观察世界中学习；Rich Sutton 先问什么能随着搜索和学习一起扩展。
他们各自在一条路上走了几十年，这条路依赖，就是他们的意见值得听的原因。让一个模型直接给"专家建议"，你得到的是所有人的平均，也就等于谁都不是。

**dinner-with-giants 让偏见保持原样。** 每个人物是一个独立的子 agent，从本人公开的访谈、演讲、文章、论文重建，每句话都标明是 `[quoted]`（原话）、`[synthesized]`（归纳）还是 `[inferred]`（推断）。人物先各自独立打分，再按真正的分歧点分桌辩论；新开的核查 agent 在辩论进行中核查事实；同时跑一个不带人物的基线，你能看到这一屋子人比直接问模型多给了什么。

### 为什么是一屋子人，而不是一位导师

就算你真约到其中一位吃饭，也就五分钟，你得到的是一个人的偏见。求职博主、名人导师都一样：一条路径，没时间了解你的细节。

- **完整的个人背景。** 你的情况、偏好，以及过去建议的实际结果，都以纯 Markdown 放在 `workspace/` 里（git 会忽略它）。可以放进你的 Obsidian 库，也可以从 Notion 同步；每次运行都会读，这屋子人对你的了解是以月计，不是以分钟计。
- **问题需要多久就花多久。** consult 几分钟；完整运行会花几个小时打分、辩论、核查、重估。
- **很多种偏见，而不是一种。** 一位顾问的路径会让你看到的世界变偏；一屋子不同路径的人，先各自独立判断再辩论，就不会。
- **随你的工具一起变强。** 协议跑在你已经在用的 coding agent 和模型上，每出一个新模型、新 harness，这屋子人就更敏锐。

它是一套由你的 coding agent 执行的协议：Claude Code 或 Codex 负责启动子 agent。仓库里没有服务器、没有 SDK、不需要 API key。

## 能拿来做什么

| 模式 | 你问 | 你得到 | 时间 |
|---|---|---|---|
| `/consult` | "Karpathy、LeCun 和李飞飞看到这个想法，会先问我什么？" | 每人一屏，最后是分歧在哪、什么证据能定 | 几分钟 |
| `/review` | "让 Gurley、黄仁勋、Collison 把我的 pitch 拆一遍。" | 各自独立的批评、一轮互评、按严重程度排序的修改清单、需要你自己拍板的点 | 10–30 分钟 |
| `/deliberate` | "帮我在这四个选项里选。" | 预注册的评分、辩论桌、三次核查、裁判、私下重估、报告 | 1–6 小时 |
| `/new-persona` | "把某某请上桌。" | 有出处的人物文件夹：档案、带时间的预测记录、卡片 | 约 30 分钟 |

更多用法（事前验尸、pitch 演练、梳理一个有争议的领域、让人把你说服、从不同路径出发的头脑风暴）：[docs/use-cases.md](docs/use-cases.md)。

## 看看效果

### 20 位 AI 大佬、16 个研究方向、7 张辩论桌

**[看这次运行 →](examples/runs/2026-10-28_ai-research-directions/)**

黄仁勋、Dario Amodei、Demis Hassabis、Yann LeCun、李飞飞、何恺明等 20 个人物，从影响、是不是瓶颈、学界还有没有优势、时机四个维度给 16 个 AI 研究方向打分，然后分 7 桌辩论：RLVR 到底有没有教会新推理？世界模型的证据跟不跟得上估值？仿真能不能替代稀缺的真实机器人数据？……

结果：

- **评测科学和具身智能在所有权重下都排第一、第二**；预训练和多模态生成垫底，主要扣在学界优势和时机上。
- **辩论改动了 48 个分数**，每一处都引用了说服它的那一帖，并复述论点。世界模型改动最多：18 人里 11 人改了分。
- **一组两两比较翻转了**：辩论前世界模型以 11 比 9 领先生成式动作策略，辩论后以 9 比 11 落后。
- **这一屋子人不等于直接问模型。** 两个不带人物的基线给多模态生成打 7 分，人物的中位数是 4 分。

这次运行改编自一次为某位用户做的真实运行：从中文译成英文，删去了这位用户的背景、他自己的候选课题和个人问题，分数保持原样。细节见该运行的 README。

### 六位历史人物给一位虚构学生出主意

富兰克林、达尔文、法拉第、居里夫人、Ada Lovelace 和苏轼，从他们本人的公有领域著作重建，讨论一位虚构学生的下一步：大厂 AI 实验室、生物科技创业、读博，还是独立做一年开源。从冻结的评分规则到审读意见，所有文件都在。
**[看这次运行 →](examples/runs/2026-11-14_alex-next-step/)**

## 桌上都有谁

[`personas/`](personas/) 里有 26 个现成人物，每人都有档案、带时间的预测记录、机器可读的卡片和来源表。

| 视角 | 人物 |
|---|---|
| 资本与价值 | Michael Mauboussin · Bill Gurley · Vinod Khosla · Patrick Collison |
| 平台与成本 | 黄仁勋 · Jeff Dean |
| 规模与验证 | Dario Amodei · Andrej Karpathy |
| 经验与世界模型 | Sergey Levine · Demis Hassabis · Rich Sutton · Yann LeCun |
| 学界与评测 | Percy Liang · Graham Neubig |
| Agent | 姚顺雨 |
| 多模态与生成 | 谢赛宁 · 何恺明 · 朱军 |
| 空间智能与机器人 | 李飞飞 · Russ Tedrake |
| 历史人物 | 富兰克林 · 达尔文 · 法拉第 · 居里夫人 · Ada Lovelace · 苏轼 |

每个人物都是基于公开材料的模拟，不是本人言论；被模拟的人都没有审阅或认可过自己的人物。想请别人上桌？跑 `/new-persona`。

## 快速开始

需要 [Claude Code](https://docs.anthropic.com/en/docs/claude-code)（或其他能启动子 agent 的 coding agent）和 Python 3.9+。仓库本身不用安装任何东西。

```bash
git clone https://github.com/Jerry-111/dinner-with-giants.git
cd dinner-with-giants
claude
```

然后在 Claude Code 里：

```
/consult I'm in the second year of an ML PhD. Should I leave to join an AI startup? Ask Jensen Huang, Yann LeCun and Andrej Karpathy.
/review drafts/pitch.md with Bill Gurley, Jensen Huang and Patrick Collison
/deliberate
/new-persona Paul Graham
```

**Codex 或其他 agent：** "先读 `AGENTS.md`，再用 `personas/C3_huang`、`personas/K5_lecun`、`personas/K4_karpathy` 对这个问题做一次 consult：……"

协议和人物文件都是英文；中文运行也支持，在 `scope.md` 里设定语言即可。你自己的背景、人物和运行记录放在 `workspace/`，git 会忽略它（[workspace/README.md](workspace/README.md)）。先从 `/consult` 或 `/review` 开始；完整运行要几个小时，token 用量很大。

## 和别的做法有什么不同

- **保留偏见，不取平均。** 一个人物一个子 agent；第一轮各自打分；同一轮同时发帖；给人物看的桌记录从不写谁说服了谁；改分必须引用说服它的那一帖并复述论点。
- **每句话都有标注。** 引语是真的、而且很短；查不到出处的名言单列为"常被归于此人，未核实"，不当原话用。
- **经验论证是正式论据：** 我经历了什么 → 教会我什么 → 为什么适用于眼前 → 类比在哪里可能不成立。按类比成不成立来评。
- **利益只展示，不打折。** "你有利益所以你错"不算论点；可以质询证据来源。
- **核查卡在重估之前完成**，还会把每个人物讲的经历和它自己的档案对一遍。
- **可以度量：** 评分规则在打分前冻结；每次运行都附一个不带人物的基线；协议版本之间做盲测。在世人物的保真度测试有完整协议，但还没公布结果。

和同类项目分工不同：女娲（nuwa-skill）把一个人蒸馏成 skill，陪你用他的框架想问题；Roast Room 做快速、可视化的商业辩论；LLM Council 比较不同厂商的模型。大佬怎么看是请一屋子大佬围着你的问题辩论，每句话标出处类型、辩论中途核查事实。英文 README 里有完整对比表。

## 负责任地使用

这里的在世人物都是公众人物，只在其公开记录范围内模拟。人物文件和裁判只评论证和有时间的预测，不评价人品；职位和交易都有来源和"截至"日期；和模型厂商的关联会披露（Claude 由 Anthropic 训练）。不要把模拟输出当成真人说过的话。如果你是被模拟的人（或代表本人），想修改或删除自己的人物，请[提交 Content concern](https://github.com/Jerry-111/dinner-with-giants/issues/new?template=content_concern.yml)：我们会删除，不需要理由。完整政策：[RESPONSIBLE_USE.md](RESPONSIBLE_USE.md)。

## 时间与成本

一次 consult 几分钟；一次 review 10–30 分钟；3–6 人的小型运行约一小时。历史人物示例（六人、三桌）端到端约五小时，其中一个半小时在从来源建人物。20 人的完整运行约五个半小时；人物 agent 跨轮续接、上下文很大，token 用量高。建议从小规模开始。

## 局限

- 所有人物都是同一个模型的实例，它们意见一致不构成独立证据。
- 人物是按某个日期、根据读过的材料重建的，可能把本人理解错。
- 轮次隔离靠指令和主执行者的文件交接，不是沙箱。
- 核查是抽样，不是逐条。
- 输出是结构化的分歧，不是专业建议。

## 许可与引用

[MIT](LICENSE) © 2026 Jerry-111。如果在研究或工作中用到这套协议或工具，请引用（[CITATION.cff](CITATION.cff)）。
