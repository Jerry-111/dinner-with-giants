# Shared evidence brief: Alex's next step

> Corrections after fact-check ①: see evidence/errata.md.

Shared evidence brief, compiled 2026-11-14. Scope: external, dated facts for the
`2026-11-14_alex-next-step` run (a fictional computational-biology master's student choosing
among four career options), so personas and the baseline analyst can reason about 2026 conditions
their own eras cannot supply. Claims to test, referenced below as tags: **ClaimA** — a friend's
"If you don't start a PhD now, you never will." **ClaimB** — a former manager's "A startup teaches
you more in one year than a big lab does in three."

Facts are numbered F1, F2, … and are never deleted, edited, or renumbered here. Any later
correction goes to `evidence/errata.md`; this file stays as originally compiled.

## PhD economics and outcomes in the US

**F1 — The US all-field PhD median time to degree was 8.6 years from the bachelor's degree (7.2
years from the start of graduate school) in academic year 2023.**
Source: NCSES, *Survey of Earned Doctorates 2023* (NSF 24-336), trend table. ncses.nsf.gov/pubs/nsf24336.
As of: academic year 2023 (published Dec 2024). Bears on: O3, Q1, L5.

**F2 — Computer and information sciences doctorates had a median of about 8.0 years from
bachelor's degree to completion in academic year 2023 — not meaningfully shorter than the
all-field average.**
Source: NCSES, *Survey of Earned Doctorates 2023* (NSF 24-336), Table 8 series. As of: academic
year 2023. Bears on: O3, Q1, ClaimA. Caveat: read from a fragmented table extract; treat as
approximate.

**F3 — Biological and biomedical sciences doctorates had a median of roughly 7.6–7.8 years from
bachelor's degree to completion in academic year 2023, somewhat faster than computer science.**
Source: NCSES, *Survey of Earned Doctorates 2023* (NSF 24-336), broad-field and subfield tables.
As of: academic year 2023. Bears on: O3, Q1, ClaimA. Caveat: two NCSES tables gave slightly
different values (7.6 vs. 7.8); neither subfield exactly matches "protein ML."

**F4 — The FY2026 NIH predoctoral (NRSA) stipend is $29,364/year ($2,447/month), flat across all
experience levels, for awards starting October 1, 2025.**
Source: NIH, Guide notice NOT-OD-26-044. grants.nih.gov/grants/guide/notice-files/NOT-OD-26-044.html.
As of: FY2026. Bears on: O3, L5. Caveat: a biomedical/life-science training-grant floor, not a
computer-science figure; many programs pay above it.

**F5 — The NSF Graduate Research Fellowship (GRFP), open to computational-biology and most CS
applicants, pays a $37,000/year stipend plus a $16,000/year payment to the institution for tuition
and fees.**
Source: NSF, GRFP program page. nsf.gov/funding/initiatives/grfp. As of: 2027 competition cycle
(page updated Oct 2026). Bears on: O3, L5. Caveat: a competitive top-tier award, not the median
PhD stipend — compare against F4 for the lower end.

**F6 — Ten-year PhD completion in the US has historically run under 75% of entrants; one
multi-university study of underrepresented-minority STEM students found completion between about
45% (physical/math sciences) and 63% (life sciences).**
Source: Council of Graduate Schools, PhD Completion Project / Doctoral Initiative on Minority
Attrition and Completion (DIMAC), as summarized by AAAS. aaas.org/phd-completion-project. As of:
DIMAC cohorts through roughly 2015. Bears on: O3, Q1, ClaimA. Caveat: dated (circa 2015) and
scoped to one subpopulation at 21 universities; no more recent cross-institution completion study
was found.

**F7 — Of 2023 engineering doctorate recipients with definite postgraduation plans, 80% had
non-postdoc industry/business commitments and 10% had academic commitments — the highest
industry share and lowest academic share of any broad field; biological and biomedical sciences
recipients had the lowest rate of any field for having definite postgraduation commitments at all
(68%).**
Source: NCSES, *Survey of Earned Doctorates*, 2023 report (NSF 25-300), postgraduation-trends
section. ncses.nsf.gov/pubs/nsf25300. As of: academic year 2023 (published Dec 2024). Bears on:
O1, O3, Q1. Caveat: reported by broad field (engineering; biological/biomedical sciences), not by
computer science or protein ML specifically.

**F8 — New AI PhD graduates in the US and Canada grew 22% from 2022 to 2024, and — reversing
roughly a decade of industry pulling ahead — most of that growth went into academic jobs, not
industry; of 2024 graduates with definite plans, about 62.75% went to industry, 31.59% to
academia, and under 5% to government.**
Source: Stanford HAI, *The 2026 AI Index Report*, Chapter 7 (Education). hai.stanford.edu/ai-index/2026-ai-index-report.
As of: published 2026, data through 2024. Bears on: Q1 (direct), O1, O3, ClaimA. Caveat: covers
"AI PhDs" broadly, not protein ML; a secondary source's claim of a 77% industry-share peak in 2022
is not confirmed by the report's own published highlights.

**F9 — Industry research-scientist job postings' actual PhD requirements were not pinned down by
a solid source in this search; see open questions.**
Bears on: O1, Q1.

## Startups

**F10 — Seed-stage graduation to a Series A within about two years has fallen: roughly 30% for
companies that raised seed rounds around 2018, versus roughly 15% for 2022–2023 seed cohorts; the
newest (2024) cohorts' one-year conversion (9–13%) is the best since 2021 but still well below the
2018 pace.**
Source: Carta, seed-to-Series-A data series. carta.com/data. As of: cohorts through 2024, posts
from 2024–2025. Bears on: O2, Q2 (C1, C4), L5, ClaimB (startup survival is a precondition for "a
startup teaches more"). Caveat: Carta's own pages returned HTTP 403 during this search; figures
come from indexed summaries, and different Carta posts give different numbers for similar 2018
cohorts (25.9% vs. 30.6%) — directional, not exact.

**F11 — The median initial equity grant for a startup's first ("founding") engineer is about 1.5%
of the company; the middle half of grants falls between roughly 0.6% and 4.1%.**
Source: Carta, "The Median First Engineer Equity Grant Is 1.54 Percent." carta.com/data. As of:
December 2025 cap-table analysis. Bears on: O2, L2, L5. Caveat: direct page access was refused
(HTTP 403); figure comes from an indexed summary of Carta's analysis.

**F12 — Early-stage biotech financing weakened into 2026: one tracker counted the fewest disclosed
biotech seed-and-Series-A rounds for a first half in a decade (1H 2026); disclosed early-stage
private biotech funding ran about $3.97B across 137 deals in 1H 2026, down from about $5.40B a
year earlier, even as total biotech venture funding grew overall.**
Source: BioCentury and BiopharmIQ reporting on biotech venture data. biocentury.com; biopharmiq.com.
As of: first half of 2026. Bears on: O2, Q2 (C1), L5. Caveat: trade-press reporting on proprietary
deal trackers, not a funder's own primary release.

## Large AI labs and protein science

**F13 — The 2024 Nobel Prize in Chemistry was split between computational protein design (work
originating at the University of Washington's Institute for Protein Design, built on the Rosetta
software) and protein structure prediction (Google DeepMind's AlphaFold2 system).**
Source: The Nobel Prize, official announcement. nobelprize.org. As of: announced October 9, 2024.
Bears on: O1, O3, O4, Q1.

**F14 — The AlphaFold Protein Structure Database (EMBL-EBI, built with Google DeepMind) reached
over 214 million predicted structures — covering nearly all of UniProt — in a count published in
2024; EMBL-EBI's live site gives two different, undated totals: about 200 million in one place and
about 260 million in another.**
Source: EMBL-EBI / Google DeepMind, "AlphaFold Protein Structure Database in 2024," *Nucleic Acids
Research*; EMBL-EBI site, alphafold.ebi.ac.uk. As of: count published 2024 (underlying data to
September 2023); live-site figures undated. Bears on: O1, O3, O4, L3, L4. Caveat: the live
database's two totals are not reconciled here.

**F15 — A privately held firm's ESM3, a generative protein-design language model, launched in
June 2024; only its smallest 1.4-billion-parameter checkpoint is openly downloadable under a
non-commercial research license, while larger 7B and 98B-parameter versions are reachable only
through the company's hosted API.**
Source: Launch coverage distributed via a major cloud provider's press office and a wire service.
press.aboutamazon.com; businesswire.com. As of: launch June 25, 2024. Bears on: O1, O3, O4, L3,
L4. Caveat: no official company blog post was directly reachable in this search; secondary
sources disagree on whether the larger models' license permits any commercial use.

## Open-source science funding

**F16 — One major science funder's open-source-software-for-science program has run multiple
cycles since 2019: the first cycle awarded $5M across 32 recipients; a later cycle awarded $11.1M
across 35 grants; the most recent cycle whose terms this search found set individual awards at
$100,000–$400,000 in total costs over two years.**
Source: Chan Zuckerberg Initiative / Chan Zuckerberg Biohub press releases. chanzuckerberg.com/science;
biohub.org. As of: cycle amounts current to their announcement years (approx. 2019–2022); the
$100K–$400K range's cycle and date could not be confirmed. Bears on: O4, L5. Caveat: the current
(2025–2026) cycle number and exact award range were not confirmed in this search.

**F17 — NSF's Pathways to Enable Open-Source Ecosystems (POSE) program funds open-source projects
directly: Phase I awards run up to about $300,000 for one year to plan an ecosystem; Phase II
awards run up to $1.5M over two years to execute it; a 2023 cohort of 19 Phase II projects totaled
over $26M (about $1.37M average).**
Source: National Science Foundation, POSE program pages and award announcements.
nsf.gov/funding/initiatives/pathways-enable-open-source-ecosystems. As of: 2023–2025
solicitations. Bears on: O4, L5.

## Compute

**F18 — Industry built more than 90% of "notable" AI models (the AI Index's own term) in both 2024
and 2025, while academic institutions (alone or in collaboration) built the rest and still led in
the most-cited published research; several of the largest industry labs no longer disclose the
training compute behind their most resource-intensive systems, and no direct academia-vs-industry
FLOPs comparison was found in the accessible report pages.**
Source: Stanford HAI, *The 2026 AI Index Report*, Chapters 1 and 2. hai.stanford.edu/ai-index/2026-ai-index-report.
As of: published 2026, data through 2025. Bears on: O1, O3, O4, L3, Q1, ClaimB (resource access
cuts both ways). Caveat: model-production share is the closest available proxy for a compute gap;
a direct FLOPs ratio may exist in the full chapter PDF, which this search could not parse as text.

## Open questions the brief cannot answer

- Whether, and how often, research-scientist roles on large AI labs' science teams actually
  require a PhD rather than accepting a strong publication or engineering record instead.
- A direct, dated FLOPs or dollar-value comparison of compute available to an academic PhD lab
  versus a large AI lab's science team in 2026.
- Completion rate, time-to-degree, and industry-placement data specific to protein ML or
  computational biology — all data found is for "biological sciences," "computer science," or
  "AI" broadly, not this cross-section.
- Base rates for what happens to solo or two-person maintainers of open-source scientific
  toolkits after a dedicated independent year: how many attract a co-maintainer, a grant, or an
  acquisition offer, versus stalling.
- The current (2026) open-source-for-science grant cycle's exact award range, and any
  sponsorship-income benchmark (for example a code-hosting platform's sponsorship program) for a
  project near the scale in this run's user profile.
- A verified academia-vs-industry compute ratio for frontier-model training, net of the
  non-disclosure noted in F18.

## Sources

- NCSES, *Survey of Earned Doctorates 2023* (NSF 24-336) — ncses.nsf.gov/pubs/nsf24336
- NCSES, *Survey of Earned Doctorates*, 2023 report (NSF 25-300) — ncses.nsf.gov/pubs/nsf25300
- NIH Guide notice NOT-OD-26-044 (FY2026 stipends) — grants.nih.gov/grants/guide/notice-files/NOT-OD-26-044.html
- NSF, Graduate Research Fellowship Program — nsf.gov/funding/initiatives/grfp
- Council of Graduate Schools / AAAS, PhD Completion Project — aaas.org/phd-completion-project
- Stanford HAI, *The 2026 AI Index Report* — hai.stanford.edu/ai-index/2026-ai-index-report
- Carta, Data (seed-to-Series-A and founding-engineer-equity series) — carta.com/data
- BioCentury; BiopharmIQ — biocentury.com; biopharmiq.com
- The Nobel Prize, 2024 Chemistry announcement — nobelprize.org
- EMBL-EBI / Google DeepMind, AlphaFold Protein Structure Database — alphafold.ebi.ac.uk
- Launch coverage via a major cloud provider's press office and a wire service (open protein
  language model) — press.aboutamazon.com; businesswire.com
- Chan Zuckerberg Initiative / Chan Zuckerberg Biohub, open-source-for-science grants —
  chanzuckerberg.com/science; biohub.org
- National Science Foundation, Pathways to Enable Open-Source Ecosystems —
  nsf.gov/funding/initiatives/pathways-enable-open-source-ecosystems
