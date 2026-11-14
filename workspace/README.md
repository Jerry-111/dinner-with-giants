# workspace/

Your own material lives here. Everything in this folder except this README is git-ignored, so
your context, your personas and your runs stay on your machine unless you move them out.

```
workspace/
  context/      # user_profile.md, preferences.md, calibration_log.md (templates in templates/context/)
  personas/     # your persona folders: <ID>_<slug>/ (templates in templates/persona/)
  runs/         # your runs: <YYYY-MM-DD>_<slug>/ (create with `python3 tools/sim.py new-run --slug …`)
```

Start with:

```bash
mkdir -p workspace/context
cp templates/context/*.md workspace/context/
```

Then fill in `workspace/context/user_profile.md` with only what you are willing to give the agents.
Leave unknowns as "unknown": the protocol turns them into conditional branches instead of guesses.

Do not put immigration or identity documents, financial details or health information here or
anywhere in the repository.

Want version control for your workspace? Make it its own private repository (for example
`git init workspace/` and push to a private remote). Never push it to a public one.
