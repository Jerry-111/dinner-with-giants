# What good output looks like (for agents)

> Collected from the user's own feedback over time. Where an entry here conflicts with
> `calibration_log.md`, the log wins — it carries the more recent signal. This file lives in
> `workspace/context/`, which is git-ignored except for its own README. Write only preferences
> the user actually stated; leave a line blank rather than inferring a default for it. Keep the
> same privacy limits as `user_profile.md`: no immigration/identity, finance, or health detail.
>
> Last updated: <YYYY-MM-DD>

## Substance

- <judgment-and-understanding oriented, vs. personalized-fit oriented — which does the user want more of>
- <ratio of domain/industry analysis to personal-path advice, e.g. "about two-thirds domain" — the default is set in `templates/run/scope.md`; override here if the user wants a different one>
- <density: claims backed by facts and sources inline, counterarguments surfaced before a verdict, no bare conclusions, no flat recap either>
- <should areas or options be evaluated separately, or does the user want one unifying frame>
- <how much jargon to use: write for a specialist, or explain terms>
- <anything the user has said is explicitly not the point of this run, so agents don't drift toward it>
- <does a new run only add to previous conclusions, or may it re-evaluate them — see `calibration_log.md` for the latest answer>

## Persona simulation

- <how deep the personas should feel; point to a concrete example the user has approved, if any>
- <how much the user wants personas to argue from their own experience and conviction, vs. staying neutral>
- <anything the user explicitly does not want flattened, hedged, or averaged away>

## Deliverable form

- <what belongs in the full record vs. the shorter version the user actually reads>
- <where the reader pack goes: a doc or wiki tool, a plain file, chat only — and its shape: one page or several, flat or categorized>
- <what should stay folded or collapsed vs. visible up front>
- <anything to confirm with the user before publishing or moving content in a shared tool>

## Way of working

- <orchestration expectations: real sub-agents vs. in-context role-play; concurrency limits>
- <where intermediate work should live>
- <any infrastructure constraint, e.g. must not depend on the user's own machine>
