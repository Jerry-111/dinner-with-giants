Fact-check ②, 2026-11-14, fresh agent; between rounds B and C.

## Claims checked (cited most in B, or driving a concession)

| # | Post | Claim | Verdict | What the primary source says | URL |
|---|---|---|---|---|---|
| 1 | B/X1/H6 | One large-lab AI research-scientist posting had a bachelor's as minimum, PhD only "preferred" (Meta, undated; from an R1 self-check, not opened here) | not found | No URL logged; posting likely expired (a direct Meta job-ID fetch returned 404). Comparable current Meta AI research-scientist postings found by search instead list a doctorate as a *minimum* qualification — the opposite pattern | metacareers.com/jobs/1778470739589957 (404); themuse.com/jobs/meta/research-scientist-* (search) |
| 2 | B/X3/H1,H2,H3,H4 (F10) | Seed-to-Series-A 2-yr conversion ~30% (2018) to ~15% (2022-23) to 9-13% (2024) | partly confirmed | carta.com/data still 403s, as in fact-check ①. Secondary aggregation of Carta's own posts: 2018 cohorts cluster at 26-31% (not one clean "30%"); 2022 near 15%, consistent. **2024 not matched** — closest is 8.2% for Q1-2024 at a *one-year* mark (shorter than the 2-yr window elsewhere), and Carta reportedly calls 2024-25 cohorts too young to read yet | carta.com/data (403); carta.com/data/* posts (search) |
| 3 | B/X3/H1,H3,H4 (F12) | 1H-2026 biotech seed+Series A funding about $3.97B/137 deals, down from about $5.40B | partly confirmed, **wrong numbers** | BioCentury's 1H26 report: biotechs "raised $4.4 billion through seed and series A rounds," down 15% YoY (implies ~$5.2B in 1H25, not $5.40B); deal count given only as the lowest first-half tally in about a decade, no digit. Direction holds; brief's $3.97B/137-deal figures don't match this primary report | biocentury.com/article/660172 |
| 4 | B/X1/H2-interj (F13) | 2024 Nobel Chemistry split evenly: UW protein design vs. AlphaFold2 | confirmed (carried over) | nobelprize.org refused both press-release and summary URLs this pass (403) — recorded inaccessible. Fact-check ① already fetched this same URL and confirmed the even split; the B-round paraphrase matches that confirmed text | nobelprize.org/prizes/chemistry/2024/press-release/ (403 this pass) |
| 5 | B/X1/H2-interj (F8) | 2024 AI-PhD academic placement 31.59%, off a 77% industry peak in 2022 | confirmed (carried over) | Matches errata.md's fact-check ① confirmation from AI Index ch.7 exactly; post cites the *corrected* figure, not the brief's original "unconfirmed" framing | per fact-check ① |
| 6 | B/X1/H1 (F14, F18) | Cites AlphaFold DB scale and industry's >90% notable-model share, generically, for a "compute and data" point | confirmed (carried over) | Matches fact-check ①'s findings; use is narrow (general resourcing point) and doesn't repeat the flagged error (no 2024 figure, no academia-leads-citations claim) | per fact-check ① |
| 7 | B/X2/H6 (Socket/Tidelift) | "60% of open-source maintainers have quit or considered quitting their work" | partly confirmed | Sentence is accurate: the page states "60% of maintainers have quit or considered quitting their maintenance work," rising 2% year over year, sourced to **Tidelift's 2024 survey of 437 self-selected maintainer respondents** — not a representative sample of "open-source maintainers" generally. The post states the figure with no such caveat | socket.dev/blog/the-unpaid-backbone-of-open-source |

## Self-check audit

| Post | Query | Logged sentence found? | Result fair? |
|---|---|---|---|
| B/X2/H2 | PhD admission offer deferral policy | Yes, verbatim | Yes — correctly scoped to "this one program," and matches the page's full approval chain (program + Graduate School, then a dean) |
| B/X2/H6 | Solo- vs. co-maintainer OSS survival/burnout | Yes (exact clause inside a longer sentence) | Partly — "unclear" is reasonable since the stat never actually compares solo vs. co-maintained projects, the query's own subject. But body prose then states it as a flat "60% of open-source maintainers" figure, generalizing a 437-respondent, self-selected survey beyond its population |

## Corrections

- F12: BioCentury's 1H26 report gives $4.4B, down 15% YoY, deal count stated only as the lowest first-half tally in a decade (no digit) — not the brief's $3.97B / 137 deals / $5.40B prior year. Keep the direction; drop the specific figures.
- F10: carta.com still inaccessible. Best secondary reading is ~26-31% for 2018 (not a flat "30%") and ~8.2% for 2024 at a one-year mark, not "9-13%" — flag the unmatched 2024 figure and mixed measurement windows.
- Meta research-scientist posting (crux X1 / F9): unverifiable as logged (no URL, undated, likely expired); comparable current postings found here run the other way — PhD as minimum, not preferred. H6's move toward "O1 may be reachable without the mentor lottery" rests on an unverified, partly-contradicted claim.
- Socket/Tidelift 60%: accurate quote, overstated population — it is a 437-respondent self-selected survey, not "open-source maintainers" at large. Add that qualifier before this travels into C.

## Tables affected

- **X1**: items 1, 4, 5, 6. The Meta posting is the one load-bearing fact on F9 (does O1 need a PhD); treat as unverified, not as support for loosening the O1/O3 forced choice.
- **X2**: item 7 / self-check row 2. The burnout stat's real population (437 Tidelift respondents) should temper the backstop-vs-reversibility exchange.
- **X3**: items 2, 3. Both central F10/F12 numbers need correction. The structural-risk side still stands directionally, but shouldn't lean on the $3.97B/137-deal or 9-13% figures as stated.
