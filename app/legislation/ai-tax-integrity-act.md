---
title: AI Tax Integrity Act of 2026
short_name: AI Tax Integrity Act
bill_numbers:
- H.R. 9501
congress: 119
topic: Government Use & Procurement
status: committee
chamber_origin: House
introduced_date: '2026-06-29'
last_action: Reported (amended) by the Committee on Ways and Means, H. Rept. 119-801; committed to the Committee of the Whole House on the State of the Union
last_action_date: '2026-09-08'
sponsors:
- Rep. Vern Buchanan (R-FL)
- Rep. Aaron Bean (R-FL)
- Rep. David Schweikert (R-AZ)
- Rep. Steven Horsford (D-NV)
cosponsor_count: 3
committees:
- House Ways and Means
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.9
    D: 0.20
    E_f: 0.40
    P: 0.40
  likelihood:
    p_committee: 0.95
    p_enact: 0.45
    basis: "govtrack_corroborated"
  rationale:
    A: "The operative provision (Sec. 2(a), as reported) directs Treasury to run an 18-24-month pilot using AI as a fraud-detection tool against tax returns — AI is the domain-general mechanism's implementation detail, not its object. Per the AI-governance-scoping guardrail, this doesn't observe, constrain, or govern AI development/deployment at all; it's a procurement/deployment condition on how one federal agency uses a tool internally. Scored 0.5 (procurement/government-use condition, binds the buyer/user not the builder) rather than the 0 a stricter read might justify, because the bill does create a standing federal use-case for AI in a sensitive government function with a mandated accuracy report — enough to clear 0 but nowhere near the +1 disclosure rung, which requires the obligation to run against a developer over its own conduct."
    B: "No preemption, savings-clause, or state-directed language anywhere in the reported text — this is a federal IRS pilot program with no bearing on state authority. The implicit-preemption floor does not apply because A does not reach +2 and the bill does not establish a regulatory scheme governing AI conduct generally."
    C: "The Comptroller General must report to Ways & Means and Senate Finance within 180 days of the pilot's end on fraud-recovery amounts and tool accuracy (Sec. 2(c)) — a real, deadline-bound GAO review, but of one pilot program's performance rather than a standing government-wide AI oversight capacity. Scored at the '+1: studies, GAO reviews... with real reporting deadlines' rung, not higher, since it creates no new agency authority, staffing, or database beyond this single program."
    D: "No export control, chip access, or geopolitical content."
    F: "No data center, compute, permitting, or energy content."
    E_consumer: "No consumer-facing harm content — this is an internal government tax-administration tool, not a product or service reaching individuals as consumers of AI."
    R: "As a federal bill it would apply IRS-wide once implemented; R is high but capped slightly below 1.0 because it's a discretionary pilot program (Treasury 'shall establish,' but scope/rollout details are left to the agency) rather than an immediately binding, full-coverage mandate."
    Depth: "max(|A|, |B|, |C|, |F|, E) / 5 = max(0.5, 0, 1.0, 0, 0) / 5 = 0.20. Low depth — this is a narrow, single-agency pilot-and-study bill."
    E_f: "Treasury and GAO administer this directly with mandated deadlines (180 days to establish, 18-24 month pilot, 180 days to report), but there's no civil penalty, private right of action, or AG enforcement — it's an obligation with a stated deadline but no stated penalty for noncompliance, landing at 0.4."
    P: "Sector-specific and self-contained — a Treasury/IRS pilot program with no institution-building or preemption ceiling, and no clear multi-state or first-in-nation template dynamic since it's federal-only and narrowly scoped to tax administration."
    likelihood: "Ordered reported favorably by Ways & Means 40-0 (unanimous, bipartisan) on 2026-07-01, with the formal committee report (H. Rept. 119-801) filed 2026-09-08 and the bill placed on the Union Calendar (No. 701) awaiting a House floor vote. GovTrack does not yet show a distinct prognosis page result for this bill as of this scoring pass; base-rate adjustment used instead. Bills that clear committee unanimously and reach the floor calendar in this Congress have historically passed the House at a high rate (especially low-controversy administrative/tax-fraud bills with bipartisan cosponsors), so p_committee is set near-certain (already achieved) and p_enact reflects the additional uncertainty of a Senate companion, floor time, and end-of-Congress scheduling risk in a second session."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- procurement
- tax administration
- fraud detection
- IRS
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/9501
- label: GovInfo (Reported in House, 2026-09-08)
  url: https://www.govinfo.gov/app/details/BILLS-119hr9501rh
- label: Ways and Means Committee announcement
  url: https://buchanan.house.gov/2026/07/01/buchanan-bill-to-encourage-use-of-ai-tools-to-detect-tax-fraud-advanced-by-house-ways-and-means-committee/
summary: Would direct Treasury to run an 18-24 month pilot program using AI to detect fraudulent or inaccurate tax returns, with a GAO report on results and accuracy afterward.
timeline:
- date: '2026-06-29'
  event: Introduced in the House by Rep. Buchanan; referred to Ways and Means
- date: '2026-07-01'
  event: Ordered reported favorably by the House Ways and Means Committee, 40-0, as amended by an Amendment in the Nature of a Substitute
- date: '2026-09-08'
  event: Formally reported to the House (H. Rept. 119-801); placed on the Union Calendar awaiting floor action
---

The bill would require the Secretary of the Treasury to establish, within 180 days of enactment, a pilot program using artificial intelligence to identify inaccurate tax returns — including those resulting from identity theft, fraudulent claims for tax credits or refunds, and returns improperly prepared by unidentified third-party preparers. The pilot must run for 18 months to 2 years. Within 180 days after the pilot ends, the Comptroller General (GAO) must report to the House Ways and Means and Senate Finance Committees on the aggregate improper refunds and recoveries attributable to the pilot and on the accuracy of the AI tools used. The bill treats AI purely as a fraud-detection tool for an existing IRS function; it does not regulate AI development or deployment more broadly.
