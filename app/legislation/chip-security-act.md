---
title: Chip Security Act
short_name: Chip Security Act
bill_numbers:
- H.R. 3447
- S. 1705
congress: 119
topic: Chips & National Security
status: committee_passed
chamber_origin: Both
introduced_date: '2025-05-08'
last_action: H.R. 3447 advanced by the House Foreign Affairs Committee; Senate version referred to committee
last_action_date: '2026-03-26'
sponsors:
- Rep. Bill Huizenga (R-MI)
- Sen. Tom Cotton (R-AR)
cosponsor_count: 8
committees:
- House Foreign Affairs
- Senate Banking, Housing, and Urban Affairs
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 3.0
    D: 5.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.95
    D: 0.60
    E_f: 0.80
    P: 0.80
  likelihood:
    p_committee: 0.95
    p_enact: 0.37
    basis: "govtrack_corroborated"
  rationale:
    A: "The mandate binds chip manufacturers and exporters, not frontier AI model developers — there's no obligation touching AI training, deployment, or model release. Commerce must issue chip-security standards and exporters must report diversion or tampering, a narrow technical process requirement rather than a substantive AI-developer standard."
    B: "Contains no preemption language and no savings clause anywhere in the text — it's silent on state authority in either direction. The bill regulates chip exporters and manufacturers through Commerce/BIS export-control administration, not AI developers, so it doesn't set up the kind of frontier-AI regulatory scheme that would otherwise raise preemption questions."
    C: "Exporters must promptly report to BIS any credible information that a covered product has been diverted or tampered with — a standing reporting channel into a federal database. CBO also estimates BIS needs roughly 10 additional staff to process license applications, catch unlicensed exporters, and handle the new reports, meaning real enforcement capacity is being built out."
    D: "This is the bill's core: it requires location-verification chip-security mechanisms before export, mandatory reporting of diversion or tampering to BIS, and creates new civil and criminal exposure for violators — a hard-controls export regime with real enforcement teeth."
    E_consumer: "No provisions touching deepfakes, non-consensual imagery, companion bots, algorithmic discrimination, or election integrity — a chip-export and national-security bill with no consumer-facing content."
    F: "No data-center, permitting, interconnection, ratepayer, or fab-siting provisions."
    R: "Covers all 'covered integrated circuit products' subject to export licensing under the Export Control Reform Act — effectively the full class of advanced AI chips destined for controlled export destinations, though the defined term may not sweep in every borderline chip."
    Depth: "Driven mainly by the new reporting and enforcement capacity built into Commerce/BIS (C) — a meaningful expansion of the government's ability to track chip diversion."
    E_f: "Commerce/BIS must issue implementing standards, and the bill creates new civil and criminal penalty exposure for violations, per CBO's scoring — enforcement runs through BIS rather than private lawsuits."
    P: "A hardware-embedded, export-triggered location-verification mandate for advanced AI chips has no real statutory precedent and is the kind of technical framework likely to show up again in future export-control and chip-security legislation."
    likelihood: "The House version, H.R. 3447, already cleared the House Foreign Affairs Committee on a unanimous 42-0 vote with 8 bipartisan cosponsors — a widely-discussed approach with real bipartisan interest. The Senate companion, S. 1705, lags well behind. Committee passage for the lead vehicle is no longer in question; what remains is the floor, Senate action, and conference, which still leaves real uncertainty about final enactment."
  confidence: high
  text_source: full_text
  scored_at: "2026-08-01"
tags:
- chip exports
- location verification
- smuggling
- China
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/3447
summary: Would require location-verification tech in exported advanced AI chips to prevent diversion.
timeline:
- date: '2025-05-08'
  event: S. 1705 introduced by Sen. Cotton
- date: '2025-05-15'
  event: H.R. 3447 introduced by Rep. Huizenga
- date: '2026-03-26'
  event: H.R. 3447 advanced by House Foreign Affairs
---

The Chip Security Act would require the Secretary of Commerce to issue standards for “chip security mechanisms,” requiring covered advanced chips to include location-verification capability (via ping-based delay measurement, not GPS) to detect diversion after export. The stated aim is preventing smuggling of advanced AI chips to U.S. adversaries; critics warn it could introduce new cybersecurity vulnerabilities.
