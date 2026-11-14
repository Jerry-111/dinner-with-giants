---
name: consult
description: Quick consult — what would one to three personas say about a specific choice the user faces, without running the full protocol. Use when the user asks "what would <persona> think about …", "ask the panel about …", or wants a fast second opinion from personas that already exist in examples/personas/ or workspace/personas/.
---

# Consult

Follow `protocol/08_consult.md`. Rules are in `AGENTS.md`; read its hard rules first.

1. Read `workspace/context/` (user profile, preferences, calibration log). If it does not exist,
   ask the user for the minimum context, or use only what they said in chat.
2. Pick the persona folders (`workspace/personas/` or `examples/personas/`). For a panel, pick
   personas with different lenses.
3. Use one real sub-agent per persona. Each reads only its own folder, the user context and the
   question.
4. Each answer follows `templates/run/consult.md`: the questions the persona would ask first, its
   judgment with labels, where it would push back, its interests (shown, not discounted), sources.
   One screen each.
5. For a panel, end with where they disagree and what evidence would settle it.

Every persona output starts with the simulation notice. Save the answers under
`workspace/runs/<YYYY-MM-DD>_consult_<topic>.md` and reply with conclusions and the path.
