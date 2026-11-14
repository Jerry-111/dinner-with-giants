---
name: new-persona
description: Build or update a persona folder (dossier A–I, views, card, sources) from public sources. Use when the user wants to add a person or archetype to their panel, refresh a persona whose materials are old, or check a persona before a run.
---

# New persona

Follow `protocol/02_persona_research.md`. Rules are in `AGENTS.md`; living public figures also
follow `RESPONSIBLE_USE.md`.

1. Scaffold: `python3 tools/sim.py new-persona --id <ID> --slug <slug>` (creates
   `workspace/personas/<ID>_<slug>/` from `templates/persona/`).
2. Launch one real sub-agent per persona. It reads only `protocol/02_persona_research.md`, the
   templates and the sources it finds; it does not read other personas.
3. Sources first, then writing: long-form material (full interviews, talks, books, letters) beats
   short clips. Record the range actually read. Do not work around access restrictions.
4. Labels on every claim; English quotes under 15 words; at most one quote per source. Check famous
   quotes against a primary source before using them.
5. Write `card.yaml` last, extracting only from the folder's own files.
6. Validate: `python3 tools/sim.py lint workspace/personas/<ID>_<slug>` and
   `python3 tools/sim.py scan --personas workspace/personas/<ID>_<slug>`.

Reply with the folder path, the materials' latest date and where the material is thin.
