---
title: SBA Artificial Intelligence Utilization Act of 2026
short_name: SBA AI Utilization Act
bill_numbers:
- H.R. 8881
congress: 119
topic: Research, Education & Workforce
status: passed_one_chamber
chamber_origin: House
introduced_date: '2026-05-19'
last_action: Passed House; received in Senate and referred to Senate Committee on Small Business and Entrepreneurship
last_action_date: '2026-06-23'
sponsors:
- Rep. Brad Finstad (R-MN)
cosponsor_count: 1
committees:
- House Small Business
- Senate Small Business and Entrepreneurship
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
    R: 1.00
    D: 0.20
    E_f: 0.40
    P: 0.40
  likelihood:
    p_committee: 1.0
    p_enact: 0.35
    basis: "base_rate_adjusted"
  rationale:
    A: "This is a government-use/procurement condition binding the SBA itself, not a conduct standard on private AI developers — it requires the SBA Administrator to report annually on the agency's own AI/ML use, risks, benefits, and human-review safeguards. Scored +0.5 (the 'procurement and government-use conditions' rung) rather than 0 because it does impose a real, recurring obligation, just on the buyer/user (SBA) rather than the builder."
    B: "No preemption, savings-clause, or state-authority language found in the bill summary or committee report — it is a single-agency internal-reporting mandate with no regulatory scheme reaching outside the SBA, so it does not establish anything resembling the 'federal regulatory scheme' that would trigger the implicit-preemption floor (which in any case only applies at A ≥ +2; this bill is at +0.5)."
    C: "Requires an initial report within 90 days of enactment and annual reports thereafter to the House and Senate Small Business committees, detailing AI/ML use cases, risks and benefits, human-involvement safeguards, and whether each tool 'adequately fills a need.' This is a standing information flow into Congress, but it covers only the SBA's own internal AI use, not AI systems or developers generally — lands at the 'studies/GAO reviews with real reporting deadlines' rung (+1) rather than the 'standing information flow into a government database' rung (+3), since it's agency self-reporting on its own tools, not a cross-agency or cross-industry incident-reporting regime."
    D: "No export-control, chip, or foreign-adversary content."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election-integrity content — purely an internal federal-agency AI-transparency bill."
    F: "No data-center, permitting, siting, or energy content."
    R: "Covers 100% of its target class by definition — the target class is the SBA itself, and the bill's reporting mandate applies to the whole agency with no threshold or carve-out."
    Depth: "max(|A|=0.5, |B|=0, |C|=1, |F|=0, E=0)/5 = 0.20."
    E_f: "The report is mandatory with a fixed 90-day-then-annual deadline (an obligation), but there is no civil penalty, rulemaking, or private right of action attached for noncompliance — the GAO report that prompted this bill was itself a response to the SBA ignoring a pre-existing, similarly penalty-free reporting duty, which argues against reading this as more than an 'obligation with no stated penalty.'"
    P: "A one-off, agency-specific reporting mandate for the SBA — not a permanent institution, and not a template likely to be copied outside the small-business-agency context, though similar agency-specific AI-transparency bills have appeared for other agencies in the same Congress (a weak sector-specific pattern, not a first-in-nation framework)."
    likelihood: "Cleared House Small Business Committee 23-0 on 2026-05-20, then passed the full House on 2026-06-23 as part of a package of SBA AI-transparency bills — both strong bipartisan signals. It now sits in the Senate Small Business and Entrepreneurship Committee. p_committee is set to 1.0 since it has already cleared the House in full. p_enact is set at 0.35, above the base rate for a bill that has passed one chamber but not yet received Senate committee action, because: (1) it is narrow, low-cost, and non-controversial (agency self-reporting, no new spending or private-sector mandate) — the profile of bills that do clear the Senate via unanimous consent or a Small Business Committee markup without a floor fight; (2) it responds directly to a GAO finding of SBA noncompliance, giving it a substantive news hook that outlasts the news cycle. It is tempered below 0.5 because no Senate committee action has yet been reported, and many House-passed message bills of this type still stall in the Senate for lack of floor time even when uncontroversial. GovTrack's own prognosis page could not be fetched directly (403 on request) so this estimate leans on the committee-vote and floor-vote signals directly."
  confidence: low
  text_source: summary
  scored_at: "2026-09-09"
tags:
- SBA
- government AI use
- transparency
- reporting
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/8881
- label: House Report 119-681
  url: https://www.congress.gov/committee-report/119th-congress/house-report/681/1
- label: FedScoop — House passes bill to force SBA's hand on AI reporting
  url: https://fedscoop.com/house-passes-small-business-administration-ai-bills/
- label: CBO cost estimate
  url: https://www.cbo.gov/publication/62531
summary: House-passed bill requiring the SBA to annually report to Congress on its own internal use of AI and machine learning, following a GAO finding of past noncompliance.
timeline:
- date: '2026-05-19'
  event: Introduced by Rep. Finstad (with Rep. Latimer)
- date: '2026-05-20'
  event: Ordered reported favorably by House Small Business Committee, 23-0
- date: '2026-06-23'
  event: Passed House; received in Senate and referred to Senate Small Business and Entrepreneurship Committee
---

The SBA Artificial Intelligence Utilization Act of 2026 amends the Small Business Act to require the SBA Administrator to report annually to the House and Senate Small Business committees on the agency's own use of AI and machine learning — including specific use cases, risks and benefits, human-review safeguards, and whether each tool actually fills a genuine agency need. An initial report is due within 90 days of enactment, with annual updates thereafter. The bill followed a GAO report documenting years of SBA noncompliance with existing federal AI use-case reporting requirements. It cleared the House Small Business Committee unanimously (23-0) on May 20, 2026, and passed the full House on June 23, 2026, as part of a package of SBA AI-transparency bills. It is now pending before the Senate Small Business and Entrepreneurship Committee, with no further Senate action reported as of early September 2026.
