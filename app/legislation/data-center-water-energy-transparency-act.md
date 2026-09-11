---
title: Data Center Water and Energy Transparency Act of 2026
short_name: Data Center Water and Energy Transparency Act
bill_numbers:
- S. 4213
congress: 119
topic: Data Centers & Energy
status: committee
chamber_origin: Senate
introduced_date: '2026-03-25'
last_action: Read twice and referred to the Senate Committee on Energy and Natural Resources
last_action_date: '2026-03-25'
sponsors:
- Sen. Dick Durbin (D-IL)
cosponsor_count: null
committees:
- Senate Energy and Natural Resources
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 0.0
    D: 0.0
    F: 1.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 1.0
    D: 0.20
    E_f: 0.8
    P: 0.6
  likelihood:
    p_committee: 0.15
    p_enact: 0.02
    basis: "base_rate_heuristic_no_live_lookup"
  rationale:
    A: "Binds data-center operators to an energy and water reporting obligation, not developers of AI systems, and imposes no standard on training or deploying a model — a purely input-side disclosure requirement."
    B: "The bill affirmatively preserves state regulatory and enforcement authority over this reporting regime and routes data through states first, with no preemption language anywhere in the text."
    C: "Corrected 2026-09-09 under the frontier/systemic-risk-vs-near-term-harm guardrail: the reporting pipeline funnels data-center energy and water usage (not AI model behavior, training, or deployment data) through states to EPA, DOE, and USDA. It textually matches axis C's '+3 standing information flow' rung, but the mechanism doesn't observe, constrain, or govern AI development or deployment at all — it's a physical-input reporting regime that would exist in identical form for any large power/water consumer, AI-related or not. No genuine AI-specific governance channel is present, so the actual AI-governance effect is 0, not +3. Previously scored 3.0; corrected to 0.0."
    D: "No export-control, chip-access, or geopolitical content."
    E_consumer: "No consumer-harm, deepfake, NCII, or algorithmic-discrimination content."
    F: "Requires data-center operators, including prospective facilities, to disclose and report energy and water use, including five-year usage projections — a disclosure and reporting regime with no siting restriction, capacity cap, moratorium, subsidy, or expedited permitting attached either way."
    R: "A federal bill covering all data-center operators nationwide, including prospective facilities that must report projected five-year usage."
    Depth: "Recomputed after the frontier/systemic-risk guardrail correction — now driven by axis F (capability buildout constraint) at 1.0/5."
    E_f: "Backed by real penalties: a joint EPA/DOE/USDA fine of $20,000 per day for negligent violations of the federal reporting requirement, plus state fines and enforcement under state-run programs."
    P: "A sector-specific reporting-and-aggregation pipeline (operator to state to EPA/DOE/USDA) rather than a permanent institution or a template likely to be copied elsewhere."
    likelihood: "Re-verified 2026-09-09: still no documented cosponsors and no bipartisan pairing; no Senate Energy and Natural Resources Committee hearing or markup found on this bill specifically. No signs of momentum since introduction — holding prior estimate."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- data centers
- energy
- water
- transparency
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/4213
summary: Senate bill requiring data centers to report energy and water use to states and federal agencies.
timeline:
- date: '2026-03-25'
  event: Introduced and referred to Senate Energy and Natural Resources
---

The bill would require data-center operators to report energy and water consumption to the states where they operate, with prospective facilities reporting estimated usage over their first five years. States would aggregate and anonymize the data and submit it to the EPA, DOE, and USDA, which would issue regional analyses; the bill authorizes penalties for non-compliance.
