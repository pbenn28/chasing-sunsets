---
title: H.R. 334 — To establish standards for generative-AI artificial or prerecorded voice systems
short_name: AI Voice Call Standards (H.R. 334)
bill_numbers:
- H.R. 334
congress: 119
topic: Deepfakes & Synthetic Media
status: committee
chamber_origin: House
introduced_date: '2025-01-13'
last_action: Referred to the House Committee on Energy and Commerce
last_action_date: '2025-01-13'
sponsors:
- Rep. Rick Allen (R-GA)
cosponsor_count: 0
committees:
- House Energy and Commerce
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 0.5
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.0
  impact_components:
    R: 1.0
    D: 0.4
    E_f: 0.8
    P: 0.4
  likelihood:
    p_committee: 0.15
    p_enact: 0.02
    basis: "base_rate_adjusted"
  rationale:
    A: "Corrected 9/9/26 under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: this mandate binds the party placing an AI-generated robocall — caller-ID disclosure and a 5-second line-release requirement under 47 U.S.C. 227(d)(3) — not any developer of frontier or advanced AI systems, and it has no connection to training, deployment-scale risk, or systemic AI oversight. It's a domain-general robocall/telemarketing compliance duty that happens to name generative-AI voice systems as one covered category. Previously scored 1.5 (treating it as a 'mandated process with enforcement'); corrected down to a token +0.5 disclosure-only floor, with the real severity captured on E_consumer instead."
    B: "Contains no preemption or state-law language of any kind; it's a straightforward federal amendment to telecom rules."
    C: "Corrected 9/9/26 under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: the FCC gaining enforcement authority over a new category of robocalls is not a standing AI-oversight information flow — it's the existing robocall-enforcement apparatus absorbing one more covered call type, with no observation of model training or deployment risk. Previously scored 2.0 by literally matching 'new authority for an existing regulator'; corrected down near the floor, since the mechanism's object is robocall abuse, not AI governance."
    D: "No export-control, chip-access, or geopolitical content."
    E_consumer: "Addresses AI-generated robocalls with a concrete compliance requirement beyond a simple label, though it stops short of criminal penalties or letting individuals sue."
    F: "No data-center, permitting, or energy content."
    R: "Covers all generative-AI voice call systems nationwide under the Communications Act, with no size threshold or carve-out."
    Depth: "A modest, single-purpose tweak to robocall rules -- it doesn't reach into deeper structural territory."
    E_f: "Enforced through FCC rulemaking backed by civil penalties under the existing Communications Act framework."
    P: "A narrow, self-contained standard for AI voice calls rather than a broader template other bills would build on."
    likelihood: "A single-sponsor bill (Rep. Rick Allen) with no cosponsors and no movement since its January 2025 committee referral. A May 2026 CRS report on robocall legislation in the 119th Congress (R48941) confirms no hearings specific to robocalls, AI-generated or otherwise, have been held at all — corroborating live-lookup evidence of continued dormancy rather than the prior pass's heuristic-only estimate."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- AI voice
- FCC
- disclosure
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/334
summary: House bill directing FCC standards for generative-AI voice call systems.
timeline:
- date: '2025-01-13'
  event: Introduced in the House and referred to Energy and Commerce
- date: '2026-09-09'
  event: Re-verified — CRS report (R48941, May 2026) confirms no robocall-related hearings held in the 119th Congress; no further action on this bill
---

H.R. 334 would amend the Communications Act of 1934 to establish technical and procedural standards for artificial or prerecorded voice systems created through generative AI, giving the FCC authority over such systems — for example, requiring AI-generated voice messages to identify the caller's number and to release a recipient's line within five seconds after they hang up.

*(The bill's introduced text carries no short title; it is sometimes referred to informally as the “CLEAR Voices Act” in third-party summaries.)*
