---
title: Algorithmic Accountability Act of 2025
short_name: Algorithmic Accountability Act
bill_numbers:
- H.R. 5511
- S. 2164
congress: 119
topic: Civil Rights & Labor
status: committee
chamber_origin: Both
introduced_date: '2025-06-25'
last_action: House and Senate versions each referred to committee; no further action
last_action_date: '2025-09-19'
sponsors:
- Sen. Ron Wyden (D-OR)
- Rep. Yvette Clarke (D-NY)
cosponsor_count: 29
committees:
- Senate Commerce, Science, and Transportation
- House Energy and Commerce
scoring:
  axes:
    A: 0.5
    B: 1.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.0
  impact_components:
    R: 0.75
    D: 0.40
    E_f: 0.80
    P: 0.60
  likelihood:
    p_committee: 0.02
    p_enact: 0.01
    basis: "base_rate_adjusted"
  rationale:
    A: "Corrected under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: the impact-assessment mandate tests automated decision systems for bias, privacy, and performance risk — algorithmic discrimination/bias, the rubric's own canonical example of what belongs on axis E, not frontier-scale training, catastrophic risk, or systemic AI oversight. Previously scored 2.0 ('mandated process with enforcement') by reading the mechanism's literal form; under the guardrail a real, enforced impact-assessment regime aimed at a narrow bias/discrimination harm belongs near A's floor. Landing at 0.5 rather than 0 because there is a genuine binding process requirement (documentation, annual FTC reporting) rather than mere disclosure."
    B: "Section 11 expressly states that nothing in the Act preempts state, tribal, city, or local law, and Section 9(b) lets state attorneys general bring their own enforcement actions alongside the FTC. State AI laws are explicitly left intact. Consistent with the guardrail's treatment of B: this is a savings clause scoped to the bill's own bias/impact-assessment subject, not an affirmative guarantee of state authority over frontier AI development generally — it caps at the ordinary +1 rung rather than +2/+3 regardless of how unconditional the clause reads."
    C: "Corrected under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: the FTC reporting pipeline this creates is a standing flow of bias/privacy/performance impact-assessment summaries, not a systemic AI oversight or evaluation capacity — it's agency enforcement of a narrow discrimination-adjacent mandate, the same category the guardrail says belongs on E rather than driving C to its '+3 standing information flow' rung. Previously scored 3.0 by matching the rung's literal wording; corrected down near C's floor to 1.0, reflecting that FTC gains real but narrowly-scoped rulemaking/enforcement authority rather than general AI-governance capacity."
    D: "No export-control or geopolitical provisions."
    E_consumer: "FTC-enforced impact assessments apply across sectors, but the bill relies on agency enforcement alone — no private right of action, no criminal penalties."
    F: "No data-center, permitting, or energy provisions."
    R: "A federal bill, but its assessment mandate only kicks in for 'large entities meeting revenue and data thresholds,' so smaller developers fall outside its reach."
    Depth: "Recomputed after the frontier/systemic-risk guardrail correction — now driven by axis E (consumer/near-term harm) at 2.0/5."
    E_f: "Backed by FTC rulemaking and civil-penalty authority, not a private right of action."
    P: "At least the third time this concept has been introduced since 2019 (the 117th Congress had a version too) — a familiar template being recycled rather than a genuinely new approach."
    likelihood: "As of 9/9/26, both S. 2164 (Senate Commerce) and H.R. 5511 (House Energy and Commerce) remain at initial committee referral with no markup or hearing on either side — congress.gov and GovTrack were both unreachable this pass (403 on both), so this is a base-rate estimate, not GovTrack-corroborated. Sponsorship/cosponsor list is still all-Democratic (Wyden plus Warren, Booker, Heinrich, Luján, Merkley, Hirono, Schatz on the Senate side), same partisan pattern as 8/1. No hearing, markup, or news catalyst has emerged since. p_committee/p_enact held at prior values."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- algorithmic accountability
- FTC
- impact assessments
sources:
- label: Congress.gov (Senate)
  url: https://www.congress.gov/bill/119th-congress/senate-bill/2164
- label: Congress.gov (House)
  url: https://www.congress.gov/bill/119th-congress/house-bill/5511
summary: Directs the FTC to require bias and impact assessments of automated decision systems.
timeline:
- date: '2025-06-25'
  event: S. 2164 introduced and referred to Senate Commerce
- date: '2025-09-19'
  event: H.R. 5511 introduced and referred to House Energy and Commerce
- date: '2026-09-09'
  event: Re-verified — no committee markup or hearing on either S. 2164 or H.R. 5511; both remain pending at initial referral
---

The bill directs the FTC to require covered entities to conduct impact assessments of automated decision systems and “augmented critical decision processes,” testing for bias, privacy, and performance risks. Large entities meeting revenue and data thresholds would maintain documentation and submit annual summary reports, with FTC rulemaking and enforcement. Sen. Wyden leads the Senate version; Rep. Clarke leads the House companion.
