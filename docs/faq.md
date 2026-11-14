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

**Can I simulate living people?**
For your own use, from public material, following `RESPONSIBLE_USE.md`: keep those personas in
`workspace/` (git-ignored), never present output as the person's words, no endorsements, no
impersonation. This repository does not ship or accept personas of living people.

**Why historical figures in the examples?**
Their own writings are in the public domain, so the example shows the full method — sources,
labeled claims, experience arguments — without putting words in a living person's mouth. The
analogies between their eras and today are part of the point: every experience argument has to
say where it may break.

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
