---
title: AI Labeling Act of 2026
short_name: AI Labeling Act
bill_numbers:
- S. 4915
congress: 119
topic: Transparency & Copyright
status: committee
chamber_origin: Senate
introduced_date: '2026-06-24'
last_action: Read twice and referred to the Senate Committee on Commerce, Science, and Transportation
last_action_date: '2026-06-24'
sponsors:
- Sen. Brian Schatz (D-HI)
- Sen. John Curtis (R-UT)
- Sen. Mark Warner (D-VA)
cosponsor_count: 2
committees:
- Senate Commerce, Science, and Transportation
scoring:
  axes:
    A: 1.0
    B: 0.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.0
  impact_components:
    R: 0.95
    D: 0.40
    E_f: 0.80
    P: 0.80
  likelihood:
    p_committee: 0.30
    p_enact: 0.08
    basis: "base_rate_adjusted"
  rationale:
    A: "Guardrail check (frontier/systemic risk vs. near-term consumer harm): the mandate here — visible/embedded labels and machine-readable provenance metadata on AI-generated content, chatbot self-disclosure, plus an anti-circumvention ban (Sec. 3(a)) — is a content-labeling/deepfake-provenance regime. Its subject is exactly axis E's paradigm case (deepfakes, AI-generated content labeling), not frontier-scale training, catastrophic risk, or systemic AI oversight; nothing in it reaches the underlying model's training, capabilities, or deployment risk. The previous 2.0 scored the mechanism's textual match to the '+2 mandated process with enforcement' rung (real FTC/DOJ enforcement, statutory damages) without asking whether the mandate's subject was frontier governance at all. Per the guardrail, a real enforced conduct mandate whose subject is content labeling belongs near the floor — rarely above +0.5-+1. Scored 1.0; the bill's actual severity is carried on E_consumer (unchanged at 2.0)."
    B: "Guardrail check: with A now scored well below +2, the implicit-preemption floor (which triggers only at A ≥ +2) no longer applies — the previous -1.0 floor read was downstream of the inflated A score. On its own terms, the bill has no preemption language, and Sec. 5(g)(2)'s preservation of state AG enforcement authority under existing law doesn't speak to a state's power to set its own AI-labeling standard, but also doesn't cut against one. Even setting the floor logic aside, this is a content-labeling-specific regulatory scheme (FTC/NIST labeling standards), not a frontier-AI regulatory scheme — so even if a scheme-silence argument applied, it would only ever reach an implicit floor on state labeling authority specifically, not on frontier AI regulation broadly, which is what axis B is meant to track. Scored 0 (silent), up from -1.0."
    C: "Guardrail check: the NIST-led working group developing binding technical standards for labeling, detection, interoperability, and enforcement is real, dedicated standing capacity — but capacity to govern content-labeling and provenance-detection specifically, not systemic AI oversight capacity in the frontier/catastrophic-risk sense the guardrail describes. A standing information flow whose subject is deepfake-labeling standards belongs near the floor on this axis (rarely above +0.5-+1) even though it's a genuine ongoing program rather than a one-off study. Scored 1.0, down from 2.0."
    D: "No export-control, chip-access, or geopolitical content."
    E_consumer: "An end-user labeling and disclosure mandate (chatbot self-identification, visible/machine-readable content labels) backed by civil penalties and a private right of action for AI providers/platforms harmed by circumvention — stronger than a bare labeling-only rung 1, since the anti-circumvention regime carries real statutory damages, but the private right of action runs to injured providers/platforms, not to individual consumers directly, so it doesn't reach the broad-private-right-of-action rung 5. Scored 2, between labeling-only and criminal liability."
    F: "No data-center, permitting, siting, or energy provisions."
    R: "Applies to any provider of a generative AI system and any covered online platform of consequential size, with no revenue or size floor identified in the text — reaches essentially the entire developer- and platform-facing universe for AI-generated content."
    Depth: "Recomputed after the frontier/systemic-risk guardrail correction — now driven by axis E (consumer/near-term harm) at 2.0/5."
    E_f: "FTC rulemaking plus civil penalties (up to $25,000 per violation, treble for repeat violations) plus a private right of action for harmed providers/platforms — a strong enforcement stack, just short of a broad consumer-facing private right of action."
    P: "A first-in-nation-style comprehensive federal labeling/provenance framework (NIST technical standards, FTC enforcement, anti-circumvention regime) that revives and expands the 2023 AI Labeling Act — likely to be a durable template other labeling bills get measured against, even though it hasn't passed."
    likelihood: "Bipartisan three-senator sponsorship (Schatz-D, Curtis-R, Warner-D) but still sitting at its initial Commerce Committee referral as of this scoring pass, roughly 2.5 months after introduction, with no hearing or markup yet reported. GovTrack.us was unreachable for this pass; base-rate adjustment for a bipartisan-but-not-leadership-priority Commerce Committee bill in a Congress already crowded with competing AI-transparency proposals (CLEAR Act, TRAIN Act) suggests modest committee odds and low enactment odds this Congress."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- deepfakes
- transparency
- labeling
- provenance
- FTC
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/4915
- label: Sen. Schatz press release
  url: https://www.schatz.senate.gov/news/press-releases/schatz-curtis-warner-introduce-bipartisan-legislation-to-provide-more-transparency-on-ai-generated-content
- label: Bill text (GovInfo)
  url: https://www.govinfo.gov/app/details/BILLS-119s4915is
summary: Requires visible and machine-readable labeling of AI-generated content and chatbot self-disclosure, enforced by the FTC, DOJ, and state AGs.
timeline:
- date: '2026-06-24'
  event: Introduced in the Senate by Sen. Schatz with Sens. Curtis and Warner; referred to Commerce, Science, and Transportation
- date: '2026-09-09'
  event: "Verified: no hearing or markup reported since referral; still at initial committee stage."
---

The AI Labeling Act of 2026 would require generative AI providers to apply clear, visible disclosures to "covered AI-generated content" (digital images, video, and audio created or substantially modified by generative AI in a way that would matter to a reasonable viewer and would not obviously appear AI-made), and to bind machine-readable provenance metadata — identifying the system, version, and creation/modification date — into that content. AI chatbots must clearly disclose that users are interacting with an AI system. Covered online platforms must display the disclosures, prevent their removal in transit, and help users see content-provenance information.

A National Institute of Standards and Technology-led working group, coordinated with the FTC, must publish technical standards for labeling, detection, interoperability, and enforcement within a year of enactment. The bill bans knowingly falsifying or stripping required disclosures and bans building or selling tools designed mainly to do so. The FTC enforces violations as unfair or deceptive trade practices; the U.S. Attorney General may bring civil actions; state attorneys general may sue to protect their residents (after notifying federal authorities); and AI providers or platforms harmed by circumvention may bring a private action. Penalties include statutory damages up to $25,000 per violation (treble for repeat violations within three years), injunctive relief, and device impounding. The bill contains no state-preemption clause; it preserves state AGs' ability to bring separate state-law proceedings, but says nothing about whether states may impose their own, potentially stricter, AI-labeling regimes.

This is a revival and expansion of the 2023-2024 AI Labeling Act, reflecting continued bipartisan interest (Schatz-D, Curtis-R, Warner-D) in content-provenance requirements as deepfake and AI-chatbot concerns have intensified.
