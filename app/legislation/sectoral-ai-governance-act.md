---
title: Sectoral AI Governance Act of 2026
short_name: Sectoral AI Governance Act
bill_numbers:
- H.R. 9125
congress: 119
topic: Government Use & Procurement
status: committee
chamber_origin: House
introduced_date: '2026-06-03'
last_action: Referred to the House Committees on the Judiciary and Oversight and Government Reform
last_action_date: '2026-06-03'
sponsors:
- Rep. Sara Jacobs (D-CA)
cosponsor_count: 3
committees:
- House Judiciary
- House Oversight and Government Reform
scoring:
  axes:
    A: 1.0
    B: -1.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.0
  impact_components:
    R: 0.85
    D: 0.40
    E_f: 0.60
    P: 0.60
  likelihood:
    p_committee: 0.15
    p_enact: 0.03
    basis: "base_rate_adjusted"
  rationale:
    A: "Corrected under the frontier/systemic-risk guardrail. The mechanism — agency heads issuing binding rules on algorithmic decision-making systems 'likely to materially contribute to violations of the federal laws that agency already enforces' — is textually a mandated process with enforcement (ANPRM step, biannual transparency reports), which is what earned the earlier +2 score. But the bill's actual subject, by its own text and example (HUD gating discriminatory rental-screening tools; the same logic extends to lending, employment, and other existing civil-rights/consumer-protection domains), is narrow sectoral/discrimination harm from AI already in ordinary deployment — not frontier-scale training, catastrophic/CBRN risk, loss-of-control, or systemic AI oversight capacity. The guardrail is explicit that AI-specificity (this does bind 'AI' systems) is a different question from frontier/systemic relevance, and that a real enforced mandate on a narrow harm domain should score 'rarely above +0.5-+1.' Corrected to +1: the ANPRM-plus-reporting structure is a genuine standing process (distinguishing it from a pure study), but it doesn't reach frontier or systemic AI risk, so it sits at the top of the guardrail's floor band rather than at +2."
    B: "Full text (Sec. (h)) contains an explicit savings clause: 'Nothing in this Act shall be construed to preempt or limit the authority of a State to regulate the use of an algorithmic decision-making system, except to the extent that the regulation of such system by a State is in conflict with this Act or a rule issued under this Act.' That final clause narrows the savings clause to conflict preemption only — a state law directly conflicting with an agency rule issued under this Act would be preempted — so this does not qualify as the +1 'ordinary savings clause with teeth' rung; it lands at −1 (conflict preemption only), the same rung the implicit-preemption floor would otherwise impose by default."
    C: "Creates no new agency, database, or dedicated evaluation body; the ANPRM process and biannual transparency reports on agency AI-related rules and enforcement actions are real but bounded reporting obligations with statutory deadlines, fitting the +1 rung (studies/reporting with real deadlines) rather than the +3 standing-information-flow rung, since the reports describe agency rulemaking activity rather than incident data flowing from developers into government."
    D: "No export-control, chip-access, or geopolitical-competition content."
    F: "No data-center, compute, siting, or energy content — entirely a rulemaking-authority bill."
    E_consumer: "Corrected under the frontier/systemic-risk guardrail: axis E is precisely where the guardrail says a narrow-domain harm belongs once A/B/C are corrected down from an inflated frontier/systemic read, and 'algorithmic discrimination' is named explicitly in the guardrail's own list of harms E exists to hold. This bill's entire structure is aimed at discriminatory algorithmic screening across sectors already covered by federal civil-rights and consumer-protection law (housing, lending, employment). It is discounted from the 3 'criminal liability for specific AI-enabled conduct' rung to 2 because the protection is mediated and contingent — agencies 'may' issue rules, so nothing is self-executing the way a flat prohibition or private right of action would be — but it is not 0: the ANPRM-plus-transparency-report structure is a real, if indirect, mechanism squarely aimed at algorithmic discrimination, and it would be inconsistent to discount A for the bill's narrow-harm subject matter while also scoring E at 0 for the same reason."
    R: "Applies government-wide across every federal agency with existing enforcement authority over some domain (housing, lending, employment, etc.), so nearly the full universe of 'agencies that could plausibly police algorithmic harms in their sector' is covered; docked slightly because the rulemaking is discretionary ('may issue rules') rather than mandatory, so actual reach depends on which agencies choose to act."
    Depth: "max(|A|=2, |B|=1, |C|=1, |F|=0, E=0)/5 = 0.40 — driven by the agency-rulemaking-authority provision, the largest single lever in the bill."
    E_f: "Rules issued under the Act would carry ordinary agency rulemaking force plus each agency's own existing civil-penalty authority for the underlying statute (e.g., Fair Housing Act penalties), roughly the 0.6 'AG/agency enforcement' band, though enforcement is contingent on agencies actually issuing rules."
    P: "A first-in-kind horizontal framework empowering every sectoral regulator to police AI within its own existing jurisdiction — a structure other agencies or a future Congress could readily extend, landing at 0.6 (joins/extends an established regulatory template — using existing sectoral authority as the enforcement hook) rather than 0.8, since it is bounded to laws agencies already enforce rather than creating anything categorically new."
    likelihood: "Introduced 2026-06-03 with 3 cosponsors, referred to two House committees, no markup or hearing identified as of 2026-09-09; no GovTrack prognosis page located. A House Democrat-sponsored bill with a divided House and no Republican cosponsors faces a difficult path; base-rate for bills at referral stage with this cosponsor profile is low."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- algorithmic decision-making
- agency rulemaking
- civil rights
- procurement
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/9125
summary: Would authorize federal agencies to issue rules governing algorithmic decision-making systems likely to contribute to violations of the federal laws those agencies already enforce.
timeline:
- date: '2026-06-03'
  event: Introduced and referred to House Judiciary and House Oversight and Government Reform
---

The Sectoral AI Governance Act of 2026 would let the head of any federal agency issue rules addressing uses of algorithmic decision-making systems that are likely to materially contribute to violations of federal laws that agency already has authority to enforce — for example, letting HUD require bias testing of AI-driven rental-screening tools before they're used. Agencies would have to seek public input through an Advance Notice of Proposed Rulemaking before issuing a rule and publish biannual transparency reports on their AI-related rules and enforcement actions. The bill preserves state authority to regulate algorithmic decision-making systems except where a state law directly conflicts with the Act or a rule issued under it.
