---
title: Data Infrastructure Energy Measurement and Standards Act
short_name: Data Infrastructure Energy Measurement and Standards Act
bill_numbers:
- H.R. 9372
congress: 119
topic: Data Centers & Energy
status: committee_passed
chamber_origin: House
introduced_date: '2026-06-18'
last_action: Ordered to be reported (amended) by the House Science Committee, 34-1
last_action_date: '2026-06-25'
sponsors:
- Rep. Suhas Subramanyam (D-VA)
cosponsor_count: 6
committees:
- House Science, Space, and Technology
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 1.0
    D: 0.0
    F: 1.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.90
    D: 0.20        # Depth — unrelated to axes.D
    E_f: 0.20
    P: 0.40
  likelihood:
    p_committee: 1.00
    p_enact: 0.32
    basis: "govtrack_corroborated"
  rationale:
    A: "Contains no provisions regulating the training or deployment of an AI model. Its substance — directing NIST, with DOE, to develop best practices, definitions, and technical standards for measuring data-center energy and water use — is about a physical input (electricity, water, infrastructure), not developer conduct, and there's no disclosure mandate, procurement condition, or incident-reporting obligation placed on AI developers themselves."
    B: "The bill's only mention of states is a data-sharing collaboration clause directing NIST to promote exchange of metrics with academia and industry at the federal and state level — not an authority or preemption provision. It is a bounded measurement and best-practices program, not an ongoing regulatory scheme, so it doesn't raise preemption questions either way."
    C: "Directs NIST, working with DOE, to run a research and measurement program — a technical precursor to future oversight, but it creates no new enforcement authority, incident database, or dedicated evaluation body."
    D: "No export-control, chip-access, or geopolitical-competition content."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election-integrity content — the bill is entirely about data-center energy and water measurement methodology."
    F: "Directs NIST and DOE to develop best practices, definitions, and technical standards for measuring data-center (including AI training and inference) energy and water use, aimed at improving demand forecasting and siting decisions. It builds measurement infrastructure and a real technical deliverable, but doesn't yet impose a binding reporting mandate on any operator, and it neither restricts nor accelerates buildout directly."
    R: "A federal, comprehensive bill covering data centers broadly, including energy and water use from AI training and inference workloads, with no revenue or size threshold narrowing its reach — though its near-term deliverable is a research and standards program rather than an immediately binding rule."
    Depth: "Driven about equally by its NIST research mandate and its energy-measurement standards — a modest, foundational bill rather than a sweeping one."
    E_f: "Imposes no penalty, rulemaking, or enforcement mechanism on any private party — it directs an agency to produce methodologies and best practices that aren't binding on data-center operators."
    P: "A routine, bounded NIST measurement-standards exercise within the agency's existing wheelhouse — not a new institution, a first-in-nation framework, or a multi-state template, just a sector-specific, self-contained effort."
    likelihood: "Re-checked 2026-09-09: no House floor vote, Rules Committee scheduling, or additional cosponsors found since the 8/10 addition of Rep. Stanton. The main new development is that sponsor Rep. Subramanyam folded this bill into a broader four-bill 'National Data Center Plan' package he unveiled 2026-09-08 (alongside the Responsible Data Center Siting Act, Data Center Fair Share Act, and Data Infrastructure Risk Reduction Act), which press coverage frames as building on this bill's already-bipartisan traction. That's a mild positive signal for eventual floor action but is not itself committee or floor movement, so p_committee stays at 1.00 (already achieved) and p_enact ticks up slightly to reflect the sponsor's active push rather than any procedural step forward."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- data centers
- energy
- NIST
- measurement
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/9372
- label: Hoodline (National Data Center Plan coverage, 9/9/26)
  url: https://hoodline.com/2026/09/virginia-congressman-wants-tech-giants-not-homeowners-to-foot-data-center-bills/
summary: Directs NIST to develop best practices for measuring data center energy use and forecasting demand.
timeline:
- date: '2026-06-18'
  event: Introduced and referred to House Science
- date: '2026-06-25'
  event: Ordered reported (amended), 34-1
- date: '2026-08-10'
  event: 'Four cosponsors added since committee passage: Rep. Dina Titus (7/14), Del. Eleanor Holmes Norton (7/20), Rep. Angie Craig (7/22), Rep. Greg Stanton (8/10)'
- date: '2026-09-08'
  event: 'Sponsor Rep. Subramanyam unveiled a four-bill "National Data Center Plan" package folding in H.R. 9372 alongside three new companion bills (Responsible Data Center Siting Act, Data Center Fair Share Act, Data Infrastructure Risk Reduction Act); no House floor vote scheduled yet.'
---

The bill directs NIST to develop best practices for measuring data-center energy use and to study data availability for improving energy-demand forecasting. It was included in the House Science Committee's June 2026 AI package because it targets the energy footprint of AI and data-center infrastructure, though its text is framed around data centers and energy measurement generally. Update (9/9/26): sponsor Rep. Subramanyam has since folded this bill into a broader four-bill "National Data Center Plan" package announced 9/8/26, though it has not yet reached a House floor vote.
