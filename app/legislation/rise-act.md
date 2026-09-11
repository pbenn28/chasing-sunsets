---
title: Responsible Innovation and Safe Expertise Act of 2025 (RISE Act)
short_name: RISE Act
bill_numbers:
- S. 2081
congress: 119
topic: Frontier Safety & Oversight
status: committee
chamber_origin: Senate
introduced_date: '2025-06-12'
last_action: Read twice and referred to the Senate Committee on Commerce, Science, and Transportation
last_action_date: '2025-06-12'
sponsors:
- Sen. Cynthia Lummis (R-WY)
cosponsor_count: 0
committees:
- Senate Commerce, Science, and Transportation
scoring:
  axes:
    A: -3.0
    B: -2.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.3
    D: 0.6
    E_f: 0.4
    P: 0.4
  likelihood:
    p_committee: 0.15
    p_enact: 0.02
    basis: "base_rate_heuristic_no_live_lookup"
  rationale:
    A: "Gives AI developers a civil-liability safe harbor (Sec. 4) conditioned on publicly disclosing model cards and design specs — the core effect is immunity from suit, not a disclosure mandate, even though disclosure is the price of qualifying for it."
    B: "Sec. 4(d) extends the safe harbor to state-law claims against a qualifying developer, wiping out an entire category of state tort/liability suits in this area rather than just those that directly conflict with federal law. Sec. 5 preserves other, unrelated immunities but doesn't narrow this preemption. It's confined to professional-use AI liability rather than reaching across the economy."
    C: "Creates no government evaluation body, database, or regulator authority — the disclosure runs to the public and to professional users, not into any government capacity."
    D: "No export-control or geopolitical-competition provisions."
    E_consumer: "Addresses liability allocation between AI developers and licensed professionals, not deepfakes, NCII, companion bots, discrimination, or election integrity."
    F: "No data-center, permitting, or energy provisions."
    R: "Federal in scope, but reaches only developers whose systems are used by licensed professionals like doctors, lawyers, engineers, and financial advisors -- a narrow slice of the AI industry."
    Depth: "Driven by the scale of the liability shield -- a real but sector-specific rule for professional-use AI, not an economy-wide change."
    E_f: "The safe harbor is conditioned on ongoing public disclosure, but the bill spells out no separate penalty regime beyond simply losing the shield if a developer doesn't comply."
    P: "A liability rule scoped narrowly to professional use of AI -- self-contained rather than a template for broader AI governance."
    likelihood: "Introduced solo by Sen. Lummis with no cosponsors and no bipartisan partner, sitting in Senate Commerce since June 2025 without hearings or other visible momentum. As of 2026-09-09, no hearing, markup, or new cosponsor has been reported in the six weeks since 8/1; GovTrack.us was unreachable (403) for a fresh prognosis check, so likelihood remains a base-rate heuristic. Estimates held flat given no material change in status."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- liability
- transparency
- safe harbor
- professionals
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/2081
summary: Lummis bill giving AI developers conditional liability immunity if they publicly disclose model documentation.
timeline:
- date: '2025-06-12'
  event: Introduced in the Senate; referred to Senate Commerce
- date: '2025-06-13'
  event: Sen. Lummis publicly announced the bill
---

The RISE Act would create a conditional civil-liability safe harbor for AI developers whose systems are used by “learned professionals” such as physicians, attorneys, engineers, and financial advisors. To qualify for immunity, developers must publicly disclose and maintain model cards and design specifications; the professional retains a duty of due diligence. The safe harbor does not apply to fraud, knowing misrepresentation, or non-professional use.
