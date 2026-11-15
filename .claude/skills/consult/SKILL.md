---
name: consult
description: Quick consult — what would one to four personas ask and say about a specific question the user faces, without running the full protocol. Use when the user asks "what would <persona> think about …", "ask Karpathy and LeCun about …", "ask the panel about …", or wants a fast second opinion from personas in personas/ (the bundled library) or workspace/personas/ (their own).
---

# Consult

Follow `protocol/08_consult.md`. Rules are in `AGENTS.md`; read its hard rules first.

1. Read `workspace/context/` (user profile, preferences, calibration log) if it exists.
   Otherwise use only what the user said in chat; ask a question back only if the consult
   cannot be answered without it.
2. Pick the persona folders: `personas/` (the bundled library) or `workspace/personas/` (the
   user's own). If the user named people, use them. For a panel, pick two to four personas with
   different lenses (the `lens` line in each `card.yaml`).
3. Use one real sub-agent per persona. Each reads only its own folder, the user context and the
   question.
4. Each answer follows `templates/run/consult.md`: the questions the persona would ask first, its
   judgment with labels, where it would push back, its interests (shown, not discounted), sources.
   One screen each.
5. For a panel, end with where they disagree and what evidence would settle it.

Every persona output starts with the simulation notice. Save the answers under
`workspace/runs/<YYYY-MM-DD>_consult_<topic>.md`.

Reply in chat, short enough to read on one screen:

1. One line per persona: its name and its answer in a sentence.
2. **Where they disagree:** two to four bullets, each with what would settle it.
3. `Saved: <path>`.

Long answers stay in the file.
