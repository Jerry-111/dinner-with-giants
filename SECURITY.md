# Security and privacy reports

This repository contains a protocol, templates and a standard-library Python script. It runs no
server and stores no credentials. The realistic risks are:

- personal data committed by mistake (a user's context, a real run, a local path, an e-mail);
- a secret pasted into a run file;
- content about a real person that should not be public.

## How to report

Use the repository's Security tab → "Report a vulnerability" (private vulnerability reporting).
Please do not open a public issue for personal data or secrets.

We aim to acknowledge reports within 7 days. Personal data and secrets are removed from the
default branch first; history is rewritten when needed.

## Protecting yourself

- Keep your own context, personas and runs in `workspace/` (git-ignored).
- Run `python3 tools/sim.py privacy-scan .` before pushing. Add your own names and terms with
  `--denylist <file>` and keep that file outside the repository.
- Enable GitHub secret scanning and push protection on your fork.
