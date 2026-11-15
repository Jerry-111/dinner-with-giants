# FAQ

**Is this a chatbot or an app?**
No. It is a protocol — Markdown instructions, templates, JSON formats — plus a small Python helper.
Your coding agent (Claude Code, Codex, or any agent that can launch sub-agents and read and write
files) is the runtime. Nothing here calls a model API directly.

**Which agents does it run on?**
It was developed with Claude Code, which can launch real sub-agents and continue them across
rounds. `AGENTS.md` is written for any agent; `CLAUDE.md` adds Claude Code specifics. If your agent
cannot launch sub-agents, use consult mode only: role-playing several personas in one context is
exactly the failure the protocol is built to avoid.

**Why not just ask the model directly?**
That is the baseline every run includes. A no-persona analyst scores the same options; the report
shows the persona − baseline gap per option. If the gap is near zero, the personas added nothing
and the report says so. Earlier runs also tracked how often personas argued from their own
documented experience and how often score changes had only social reasons.

**Are the personas independent experts?**
No. They are instances of one model, conditioned on different evidence. Agreement among them is not
independent confirmation, and every report states this. Running personas on different models is an
open question — contributions welcome.

**How long does a run take, and what does it cost?**
A consult takes minutes. A panel of 3–6 personas takes about an hour. A full run with 20 personas
took about five and a half hours of wall-clock time; persona agents that are continued across
rounds carry large contexts, so token use is high. Start with a panel.

**Why simulate real people at all?**
Because a person's value as an adviser is their bias: the path that shaped them, the bets they
lived through, the question they always ask first. A generic "expert" persona has no path, so it
has no bias worth hearing. Real, well-documented people give the model something specific to be
faithful to, and something you can check: every claim points to a source.

**Are these the real people's views?**
No. Each persona is a reconstruction by one model from the sources in its folder, as of a date.
None of the people simulated here has reviewed or endorsed their persona. Every output carries
the simulation notice; labels show which lines are sourced (`[quoted]`, `[synthesized]`) and
which are the model's extrapolation (`[inferred]`). See `RESPONSIBLE_USE.md`.

**Can I add a living person?**
Yes, if they are a public figure with a substantial public record of their own views, and you
follow `RESPONSIBLE_USE.md`: sourced, dated facts; no judgments of character; no first-person
confessions; the simulation notice everywhere. Private individuals: never without their explicit
permission, and then only in your own `workspace/`.

**I am one of the people simulated here and want my persona removed.**
Open an issue with the Content concern template or report privately through the Security tab. We
remove it; no reason needed.

**Why historical figures too?**
They show the method on people whose own writings are in the public domain, and they are a
useful contrast: their eras are far from 2026, so every experience argument has to say where its
analogy may break. You can seat Faraday next to Karpathy.

**Is the output advice?**
It is structured disagreement: positions, the arguments behind them, the facts that would settle
them, and signals that a path is wrong. You decide. It is not legal, medical, financial,
immigration or employment advice.

**Can runs be in Chinese (or another language)?**
Yes. Set the language in `scope.md`. The Chinese labels 【原话】【归纳】【推断】【主笔】 are
accepted by the tooling.

**Where does my data go?**
Into `workspace/`, which is git-ignored. Run `python3 tools/sim.py privacy-scan . --denylist
<your-terms-file>` before you push anything.

**How do I know a persona sounds like the person?**
For real people with dated public statements, run the fidelity test
(`protocol/11_fidelity_test.md`): rebuild the persona from material before a cutoff date and check
blind whether it predicts what the person said after it, against a name-only prompt.

**How is this different from nuwa-skill, Roast Room or LLM Council?**
Different jobs. nuwa-skill distills one person into a skill you think with; Roast Room runs a
fast, visual business debate with a scored verdict; LLM Council compares several providers'
models. This project seats many people at once and keeps the receipts: every claim labeled by
source type, fact-checks between debate rounds, tables built around the real cruxes, interests
shown but never discounted. The README has a comparison table.
