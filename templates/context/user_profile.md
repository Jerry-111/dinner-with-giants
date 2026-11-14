# <User>: background (for agents)

> Write only what the user has given you. Anything they haven't said is "unknown" — handle it
> with a conditional branch in `scope.md` and in persona prompts, never a guess. This file
> lives in `workspace/context/`, which is git-ignored except for its own README: it never
> leaves the user's machine unless they choose to publish a run's output themselves.
>
> **Do not record:** immigration or citizenship status or other identity details, financial
> details (income, savings, equity), or health information. If a decision genuinely turns on
> one of these, ask the user how much they want written down, and default to leaving it out.
>
> Last updated: <YYYY-MM-DD>

## Now

- <school or employer, stage, role; what the user actually does day to day>
- <relevant experience or track record>
- <how the user wants to be treated: as a specialist or a generalist, at what level of jargon>
- <existing networks or options already open — entry points, not anchors>

## Decisions already made

- <firm decisions the user has already reached, dated, so personas don't re-litigate them>

## Interests

- <what the user is leaning toward, and why; add a date whenever this changes>
- <what the user has ruled out, and why>

## Goals

<what the user is optimizing for, in their own words.>

## Unknown (write these in as conditional branches; never guess)

- <for example: risk tolerance, program timing, location constraints>

## Claims the user wants tested

<Claims the user heard from someone else, to fact-check. Attribute generically — "a friend,"
"a mentor," "a colleague" — never by name.>

- <attribution>: "<claim>"

## Sources

- <where this was collected from: a form, a conversation, an earlier run's calibration log>
