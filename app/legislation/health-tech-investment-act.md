---
title: Health Tech Investment Act
short_name: Health Tech Investment Act
bill_numbers:
- H.R. 6197
- S. 1399
congress: 119
topic: Healthcare
status: committee
chamber_origin: House
introduced_date: '2025-11-20'
last_action: Referred to the House Committees on Energy and Commerce and Ways and Means
last_action_date: '2025-11-20'
sponsors:
- Rep. John Joyce (R-PA)
- Sen. Mike Rounds (R-SD)
cosponsor_count: 6
committees:
- House Energy and Commerce
- House Ways and Means
- Senate Finance
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.85
    D: 0.10        # Depth — unrelated to axes.D
    E_f: 0.40
    P: 0.60
  likelihood:
    p_committee: 0.20
    p_enact: 0.06
    basis: "base_rate_adjusted"
  rationale:
    A: "The bill defines 'algorithm-based healthcare service' (FDA-cleared/approved AI/ML/software-driven clinical tools) and directs CMS to assign these to a new-technology ambulatory payment classification based on manufacturer-submitted costs, locking in that classification for at least 5 years. This is purely a Medicare reimbursement mechanism binding CMS as payer — it imposes no conduct standard, disclosure requirement, or any obligation on AI developers themselves. Because it neither restricts nor obligates developer conduct (it guarantees payment, not compliance), it doesn't fit even the +0.5 'procurement condition binds the buyer' rung, which presumes some condition attached to the payment; here there is none — scored 0."
    B: "No preemption or state-law language anywhere in the text; this is a pure federal Medicare payment statute amending 42 U.S.C. 1395l(t), with no state regulatory dimension at all. The implicit-preemption floor does not apply because axis A is 0, well below the +2 trigger threshold."
    C: "Directs CMS on how to classify and pay for a category of services; does not create any oversight body, incident-reporting channel, or evaluation capacity over AI systems — it is a payment-administration mandate, not a governance-capacity mandate."
    D: "No export-control, chip-access, or geopolitical content."
    E_consumer: "No provisions on deepfakes, NCII, companion bots, discrimination, or election integrity — this is a Medicare payment-classification bill for FDA-cleared devices."
    F: "No data-center, compute, siting, or energy content."
    R: "A federal bill (R baseline 1.0 for federal) targeted at a defined developer-facing class — FDA-cleared/approved AI-enabled devices billed under Medicare Part B outpatient payment — covering essentially all devices meeting that FDA-clearance threshold, so reach within its own narrow target class is high; discounted slightly for the fact that it only touches the new-technology APC pathway, not all AI-enabled care broadly."
    Depth: "Depth is driven by the largest-magnitude axis among A/B/C/F/E_consumer, all of which are 0 here — a payment-administration bill with no governance axis engaged produces minimal Depth; scored low but not zero because it does lock CMS into a specific payment methodology for 5 years, a real (if narrow) constraint on agency discretion."
    E_f: "CMS is statutorily directed ('shall ensure', 'may not remove') to apply this classification — an obligation on the agency with no private right of action or civil penalty; scored as an obligation with a stated agency directive but no penalty structure, closer to the 0.4 rung."
    P: "A sector-specific Medicare payment-classification fix for one category of FDA-cleared technology, self-contained within the Hospital Outpatient Prospective Payment System — not a framework other bills would broadly copy, but does lock in a payment methodology for a minimum 5-year term, which nudges above the pure 0.4 sector-specific rung toward some durability."
    likelihood: "Verified 2026-09-10: House companion H.R. 6197 introduced 2025-11-20 with bipartisan cosponsors (Peters, Van Duyne, Schneider, Obernolte, Craig), referred to Energy and Commerce and Ways and Means, no further action. Senate companion S.1399 (Rounds/Heinrich/Blackburn), introduced 2025-04-09, referred to Finance, no markup as of this scoring — reporting elsewhere notes no progression since referral. Bipartisan, industry-backed (AdvaMed), narrow reimbursement-fix bills of this type have historically moved via must-pass vehicles (e.g., a Medicare extenders package) more often than standalone floor votes, but no such vehicle has attached it yet this Congress."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- healthcare
- medicare
- reimbursement
- fda
sources:
- label: Congress.gov (H.R. 6197)
  url: https://www.congress.gov/bill/119th-congress/house-bill/6197
- label: Congress.gov (S. 1399)
  url: https://www.congress.gov/bill/119th-congress/senate-bill/1399
summary: Bipartisan House/Senate bill creating a Medicare reimbursement pathway for FDA-authorized AI/ML-enabled healthcare algorithms.
timeline:
- date: '2025-04-09'
  event: S. 1399 introduced by Sen. Rounds, referred to Senate Finance
- date: '2025-11-20'
  event: H.R. 6197 introduced by Rep. Joyce, referred to House Energy and Commerce and Ways and Means
---

The Health Tech Investment Act would amend Medicare's Hospital Outpatient Prospective Payment System to guarantee a stable reimbursement pathway for "algorithm-based healthcare services" — services delivered through FDA-cleared or -approved devices that use AI, machine learning, or similarly designed software to generate clinical outputs for screening, detection, diagnosis, or treatment. It requires CMS to assign these services to a new-technology ambulatory payment classification based on manufacturer-submitted costs, and bars CMS from removing that classification for at least five years until adequate claims data exists to reassign it. The bill also codifies a prior CMS "software as a service" payment policy retroactively to January 2023. Sponsors frame it as removing a commercialization bottleneck — reimbursement uncertainty — for AI-enabled medical devices.
