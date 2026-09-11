---
title: Workforce Transparency Act of 2026
short_name: Workforce Transparency Act
bill_numbers:
- S. 4476
congress: 119
topic: Research, Education & Workforce
status: introduced
chamber_origin: Senate
introduced_date: '2026-04-30'
last_action: Read twice and referred to the Senate Committee on Health, Education, Labor, and Pensions
last_action_date: '2026-04-30'
sponsors:
- Sen. Mark Warner (D-VA)
- Sen. Ted Budd (R-NC)
cosponsor_count: 1
committees:
- Senate Health, Education, Labor, and Pensions
scoring:
  axes:
    A: -1.0
    B: 0.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.55
    D: 0.20
    E_f: 0.20
    P: 0.40
  likelihood:
    p_committee: 0.30
    p_enact: 0.08
    basis: "base_rate_adjusted"
  rationale:
    A: "The bill text (BILLS-119s4476is.xml) creates an elective process for AI system providers and enterprise customers to submit aggregated, de-identified workforce-usage data to DOL, and expressly states it 'shall not be construed to require' any provider or customer to participate, with no adverse inference against non-participants. This codifies a voluntary/light-touch practice in lieu of any mandate — the rubric's −1 rung — rather than +1 disclosure-only, because disclosure-only assumes participation is required; here it is opt-in by design, which is a materially weaker posture than a mandatory transparency rule."
    B: "No preemption or savings-clause language anywhere in the bill text — it is silent on state authority throughout. The implicit-preemption floor does not apply because A is negative, not ≥ +2: this is an opt-in federal data-collection program, not a regulatory scheme that could preempt state AI law by implication."
    C: "Directs DOL (via BLS, coordinating with the Census Bureau) to build and maintain a public aggregated database of AI workforce-usage data and issue annual reports to Congress — a standing information flow into a government body, though participation on the input side is voluntary and there is no enforcement or evaluation authority attached, so this sits at the incident-reporting/standing-information-flow rung on the strength of the reporting duty alone, tempered by the fact the underlying data flow depends entirely on voluntary submissions rather than a mandatory reporting stream."
    D: "No export-control, chip-access, or other geopolitical-competition content anywhere in the bill."
    E_consumer: "No deepfake, NCII, companion-bot, algorithmic-discrimination, or election-integrity content — this is a workforce-data-collection bill with no near-term consumer-harm provisions."
    F: "No data-center, permitting, interconnection, or ratepayer content."
    R: "Because participation is voluntary, actual reach depends entirely on how many AI providers and enterprise customers opt in — named industry backers (Anthropic, Google, Microsoft, OpenAI, BSA) suggest meaningful voluntary uptake among large developers, but reach among the broader universe of 'enterprise customers' is inherently uncertain and self-selected rather than comprehensive, landing well below a mandatory-disclosure bill's reach."
    Depth: "max(|A|=1, |B|=0, |C|=1, |F|=0, E=0)/5 = 0.20 — driven jointly by the voluntary-codification rung on A and the new (if voluntary-fed) reporting stream on C, both modest in magnitude."
    E_f: "Purely voluntary: no rulemaking, no civil penalty, no private right of action attaches to non-disclosure. The only enforcement hook — DOL may seek injunctive relief against a participant that knowingly and willfully misrepresents submitted data — polices bad-faith participants, not non-participation, so this stays at the voluntary rung rather than climbing to an obligation-with-penalty rung."
    P: "A sector-specific, self-contained DOL/BLS data-collection program modeled on no clear existing multi-state or federal template; it could inform future mandatory-disclosure proposals (e.g. the competing AI-Related Job Impacts Clarity Act) but isn't itself a permanent institution or a framework other jurisdictions would copy, landing at the sector-specific/self-contained rung."
    likelihood: "Introduced 2026-04-30 with bipartisan sponsorship (Warner-Budd) and cosponsor Budd sitting on the HELP Committee of referral — a modestly positive committee-alignment signal — but only one cosponsor and no hearing, markup, or floor action identified as of 2026-09-10, roughly 4.5 months after introduction. GovTrack's prognosis page could not be fetched (403, not retried per source-blocking guidance) and no third-party source quoted a GovTrack percentage for this bill, so this is base-rate-adjusted rather than GovTrack-anchored. The voluntary, industry-backed design (endorsed by Anthropic, Google, Microsoft, OpenAI, and BSA) makes this more passable than competing mandatory-disclosure bills in the same space, which nudges p_enact modestly above the bare committee-referral base rate, but single-committee bills with one cosponsor and under five months of runway left in this Congress still rarely reach the floor."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- workforce
- DOL
- voluntary disclosure
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/4476
- label: Introduced text (GovInfo)
  url: https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4476is.xml
- label: Warner press release
  url: https://www.warner.senate.gov/newsroom/press-releases/warner-budd-introduce-legislation-to-collect-data-on-ais-impact-guide-lawmakers/
- label: Budd press release
  url: https://www.budd.senate.gov/2026/04/29/budd-warner-introduce-bipartisan-legislation-to-collect-data-on-ais-impact-on-the-american-workforce-to-guide-lawmakers/
summary: Creates a voluntary framework for AI developers and enterprise customers to submit aggregated, de-identified workforce-usage data to the Department of Labor, which would publish a public database and annual reports to Congress.
timeline:
- date: '2026-04-30'
  event: Introduced by Sens. Warner and Budd; referred to Senate HELP Committee
- date: '2026-09-09'
  event: Added to tracker. No hearing, markup, or floor action identified since introduction.
---

The bill creates an elective process for "covered AI system providers" and their enterprise customers to voluntarily submit aggregated, de-identified workforce data to the Department of Labor — covering AI-usage by task (e.g. writing, coding, research, translation), geographic and age-range distribution, and usage trends over time, while excluding personal data, employer-specific performance metrics, and trade secrets. DOL, through the Bureau of Labor Statistics and in coordination with the Census Bureau, would build and maintain a public database from the submissions and issue annual reports to Congress on AI's workforce impact. Participation is explicitly non-mandatory — the bill bars agencies from drawing any adverse inference against non-participants — and the only enforcement mechanism is the Secretary of Labor's authority to seek injunctive relief against a participant who knowingly and willfully misrepresents submitted data. The bill has drawn industry backing from Anthropic, Google, Microsoft, OpenAI, and the Business Software Alliance, and is positioned as a lighter-touch alternative to competing mandatory AI-job-impact disclosure bills.
