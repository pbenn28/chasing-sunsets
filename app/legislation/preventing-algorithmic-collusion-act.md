---
title: Preventing Algorithmic Collusion Act of 2025
short_name: Preventing Algorithmic Collusion Act
bill_numbers:
- S. 232
congress: 119
topic: Civil Rights & Labor
status: committee
chamber_origin: Senate
introduced_date: '2025-01-23'
last_action: Read twice and referred to the Senate Committee on the Judiciary
last_action_date: '2025-01-23'
sponsors:
- Sen. Amy Klobuchar (D-MN)
cosponsor_count: 8
committees:
- Senate Judiciary
scoring:
  axes:
    A: 1.0
    B: -1.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.5
  impact_components:
    R: 0.60
    D: 0.50
    E_f: 0.80
    P: 0.40
  likelihood:
    p_committee: 0.08
    p_enact: 0.02
    basis: "base_rate_adjusted"
  rationale:
    A: "Corrected under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: this bill's real subject is pricing-algorithm collusion — a narrow antitrust/commercial-practice harm falling on consumers in specific markets, structurally the same category (AI already in ordinary deployment causing a bounded, sectoral harm) the guardrail says belongs on E rather than driving A up. It is genuinely AI-specific (unlike the domain-general-mechanism guardrail's CyberTipline example) but, per the frontier-vs-narrow-harm guardrail, AI-specificity and frontier/systemic relevance are different questions — nothing here reaches frontier-scale training, deployment-scale systemic risk, or loss-of-control. Previously scored 2.0 by matching the audit/disclosure/penalty mechanism to A's 'mandated process with enforcement' rung; corrected down to 1.0, reflecting that this is a real, enforced conduct standard but on a narrow antitrust target, not frontier stringency."
    B: "Says nothing about preempting or preserving state authority; the only related clauses simply preserve existing federal antitrust law. This −1 is the mechanical implicit-preemption floor (A ≥ +2 previously triggered it; even at the corrected A = 1.0, the underlying fact pattern — a federal enforcement scheme with no express savings clause — still supports treating this as narrowing state latitude at the margins) and is unaffected by the frontier-vs-narrow-harm guardrail, which speaks to affirmative savings-clause scoring (capping generous clauses), not to this floor rule."
    C: "Corrected under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: the DOJ/FTC transparency and reporting tools this bill creates are scoped entirely to policing one antitrust practice (pricing-algorithm collusion via nonpublic competitor data), not to building systemic AI oversight or evaluation capacity — the category the guardrail says belongs on E. Previously scored 2.0 by reading 'new authority for existing regulators' as matching C's rung 2 in isolation; corrected down near C's floor to 1.0."
    D: "No export-control or geopolitical content."
    E_consumer: "Bumped from 2.0 to 2.5 as part of the A/C correction under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: with the bill's real severity now concentrated on this axis rather than split across A/C, its civil-penalty-backed prohibition plus DOJ/FTC audit-demand power and a litigation presumption sit meaningfully above a bare disclosure rule (rung 1) though still short of criminal liability (rung 3) — 2.5 reflects real enforceable teeth without a private right of action or criminal exposure."
    F: "No data-center, permitting, or energy content."
    R: "Reaches pricing algorithms across many consumer-facing industries, but only where they're built on nonpublic competitor data — a real but bounded slice of the pricing-algorithm landscape."
    Depth: "Recomputed after the frontier/systemic-risk guardrail correction — now driven by axis E (consumer/near-term harm) at 2.5/5."
    E_f: "DOJ/FTC enforcement backed by civil penalties and a legal presumption gives this real bite, though it stops short of creating a private right of action."
    P: "A narrow antitrust fix aimed at one practice — pricing-algorithm collusion via nonpublic data — rather than a broad AI-governance framework."
    likelihood: "Re-verified 9/9/26: S. 232 itself has had no markup or vote and remains parked in Senate Judiciary with no floor action — no direct committee movement on this specific bill. However, the surrounding policy area heated up materially since 8/1: the Senate Judiciary Crime & Counterterrorism Subcommittee held a bipartisan hearing on 8/4/26 ('Your Data, Their Profit: The Consumer Cost of AI Surveillance Pricing,' chaired by Hawley with Durbin as ranking member), producing a stated bipartisan Hawley-Blumenthal intent to draft new surveillance-pricing legislation, and DOJ signaled in June 2026 that criminal enforcement of algorithmic pricing collusion remains on the table. None of that is committee action on S. 232 itself — it's a related but distinct proposal (real-time 'surveillance pricing' vs. S. 232's narrower nonpublic-competitor-data collusion prohibition) — but it signals rising bipartisan salience in the same policy neighborhood that could pull S. 232 or its provisions into a future vehicle. p_committee nudged up slightly (0.07 to 0.08) to reflect that salience; p_enact held, since no actual legislative vehicle exists yet and any successor bill would likely be a fresh Hawley-authored text rather than S. 232 advancing as-is."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- antitrust
- pricing algorithms
- collusion
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/232
- label: Senate Judiciary Committee — AI surveillance pricing hearing (related, distinct proposal)
  url: https://www.judiciary.senate.gov/committee-activity/hearings/your-data-their-profit-the-consumer-cost-of-ai-surveillance-pricing
summary: Prohibits pricing algorithms that use nonpublic competitor data to facilitate collusion.
timeline:
- date: '2025-01-23'
  event: Introduced in the Senate
- date: '2025-01-23'
  event: Read twice and referred to the Judiciary Committee
- date: '2026-08-04'
  event: 'Related but distinct development: Senate Judiciary Crime & Counterterrorism Subcommittee holds bipartisan hearing on AI "surveillance pricing" (not a hearing on S. 232 itself); Hawley and Blumenthal signal intent to draft new legislation'
- date: '2026-09-09'
  event: Re-verified — no markup or committee vote on S. 232 itself since referral
---

The bill makes it unlawful to use or distribute a pricing algorithm that uses, incorporates, or was trained with nonpublic competitor data, and creates transparency and reporting tools letting the DOJ or FTC require detailed disclosures about pricing algorithms. It establishes a legal presumption to aid antitrust enforcement and provides civil penalties.

Update (9/9/26): S. 232 itself has not moved since referral, but the adjacent "surveillance pricing" issue gained bipartisan momentum after an August 2026 Senate Judiciary subcommittee hearing, with Sens. Hawley and Blumenthal signaling plans for a new, broader bill on real-time AI pricing.
