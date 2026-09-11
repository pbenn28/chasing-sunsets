---
title: DETECT Act of 2025
short_name: DETECT Act
bill_numbers:
- H.R. 4974
congress: 119
topic: Government Use & Procurement
status: introduced
chamber_origin: House
introduced_date: '2025-08-15'
last_action: Referred to the House Committee on Ways and Means
last_action_date: '2025-08-15'
sponsors:
- Rep. Vern Buchanan (R-FL)
- Rep. David Schweikert (R-AZ)
cosponsor_count: 5
committees:
- House Ways and Means
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 0.5
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.9
    D: 0.10
    E_f: 0.0
    P: 0.20
  likelihood:
    p_committee: 0.25
    p_enact: 0.05
    basis: "base_rate_adjusted"
  rationale:
    A: "The entire operative text (Sec. 2) is a one-time GAO study requirement on the potential of AI to assist IRS fraud detection — it places no obligation of any kind on an AI developer or deployer, and per the AI-governance-scoping guardrail this is a domain-general tax-administration study that merely mentions AI, not an AI governance mechanism. Scored 0 (studies, task forces, definitions), not even the 0.5 procurement rung, because unlike H.R. 9501 there is no program being stood up yet — just a report on feasibility."
    B: "No preemption or savings-clause language; a single-section GAO study bill has no bearing on state regulatory authority. The implicit-preemption floor doesn't apply since A is 0, far below the +2 trigger."
    C: "A single GAO report due 180 days after enactment on the potential for AI to assist IRS fraud detection (Sec. 2) — a real but minimal reporting deadline with no new authority, staffing, or database. Scored at the low end of the '+1: studies, GAO reviews' rung (0.5) because it is even thinner than H.R. 9501's post-pilot GAO report — this is a pure feasibility study with no program to evaluate yet."
    D: "No export control or geopolitical content."
    F: "No compute, energy, or siting content."
    E_consumer: "No consumer-facing harm content whatsoever — purely an internal tax-administration feasibility study."
    R: "Federal bill; if enacted the GAO study would cover the full IRS/Treasury fraud-detection function, so reach is high, but this is discounted slightly given the bill's superseded, largely dormant status relative to its successor H.R. 9501."
    Depth: "max(|A|,|B|,|C|,|F|,E)/5 = max(0, 0, 0.5, 0, 0)/5 = 0.10. Minimal depth — a single-section study mandate is about as thin as a tracked bill gets."
    E_f: "No enforcement mechanism of any kind; it is a one-time study directive with no penalty for delay, scored 0 (study only)."
    P: "Sunsets by design — a one-time report with no institution created and no ongoing framework; sits at the low end of the ladder as a sector-specific, self-contained (in fact largely superseded) study."
    likelihood: "Introduced 2025-08-15 with 5 GOP and no Democratic original cosponsors (Bean, Feenstra, Smith of WA, Moran, Tenney), referred to Ways and Means, and no committee markup has occurred as of this scoring pass. Its substance was effectively absorbed and advanced instead through H.R. 9501 (AI Tax Integrity Act of 2026), which was introduced roughly ten months later by the same lead sponsors, added a live pilot program, and has already been marked up 40-0 and reported to the House. With the same sponsors now pushing the more substantive successor bill through committee, H.R. 4974 itself has a low remaining chance of independent floor action — p_enact set low to reflect that it has likely been legislatively superseded rather than abandoned outright."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- procurement
- tax administration
- fraud detection
- IRS
- GAO study
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/4974
- label: GovInfo (Introduced in House, 2025-08-15)
  url: https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4974ih.xml
- label: Sponsor press release
  url: https://buchanan.house.gov/2025/8/buchanan-schweikert-introduce-legislation-to-strengthen-tax-fraud-detection-and-safeguard-taxpayer-dollars
summary: Would require a one-time GAO report on the potential for AI to help the IRS detect tax fraud; its substance was later folded into and advanced further by H.R. 9501.
timeline:
- date: '2025-08-15'
  event: Introduced in the House by Rep. Buchanan; referred to Ways and Means
- date: '2026-06-29'
  event: Successor bill H.R. 9501 (AI Tax Integrity Act of 2026), adding an actual pilot program, introduced by the same lead sponsors
---

The DETECT Act of 2025 (Digital Evaluation for Tax Enforcement and Compliance Tracking Act) would require the Comptroller General to submit a report, within 180 days of enactment, to the House Ways and Means and Senate Finance Committees on the potential for artificial intelligence to assist the IRS in detecting tax fraud. That is the entire substantive content of the bill — a single-section study mandate with no pilot program, no new authority, and no obligations on AI developers. It has not advanced past committee referral, and its policy goal was carried forward and expanded by the same sponsors' later bill, H.R. 9501, which adds an actual AI fraud-detection pilot program on top of a similar GAO reporting requirement.
