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
    A: 2.0
    B: -1.0
    C: 2.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.0
  impact_components:
    R: 0.95
    D: 0.44
    E_f: 0.80
    P: 0.80
  likelihood:
    p_committee: 0.30
    p_enact: 0.08
    basis: "base_rate_adjusted"
  rationale:
    A: "Requires generative AI providers to apply visible, embedded labels and bind machine-readable provenance metadata (system/version, creation date) to covered AI-generated content, to ensure users can detect that content without undue cost, and to disclose chatbot identity — plus a ban on tools built mainly to strip or falsify those disclosures (Sec. 3(a)). This is a mandated process with real enforcement (FTC unfair/deceptive-practices authority, DOJ civil actions, statutory damages) rather than a bare publish-a-framework disclosure rule, so it lands at +2 rather than +1 — but it stops short of any risk-assessment, audit, or incident-reporting standard on the underlying model itself, so it doesn't reach +3."
    B: "No preemption language anywhere in the text. Sec. 5(g)(2) preserves state AGs' ability to bring their own proceedings under existing state civil/criminal law — that's an enforcement-authority preservation, not an affirmative savings clause protecting states' power to set independent AI-labeling standards, and it doesn't address whether a state could impose a stricter or different labeling regime. Because A scores +2 here, the bill establishes an ongoing federal regulatory scheme (FTC rulemaking, NIST-led technical standards, safe harbors) with no express savings clause on state AI-labeling authority, the implicit-preemption floor applies: B floors at -1."
    C: "Directs a NIST-led federal working group (with FTC) to develop and publish binding technical standards for labeling, detection, interoperability, and enforcement within one year — new, dedicated standards-setting capacity tied to enforcement, not just a study. Scored +2 rather than +3 because the ongoing information flow this creates is technical-standards development, not a mandatory incident-reporting database into government hands."
    D: "No export-control, chip-access, or geopolitical content."
    E_consumer: "An end-user labeling and disclosure mandate (chatbot self-identification, visible/machine-readable content labels) backed by civil penalties and a private right of action for AI providers/platforms harmed by circumvention — stronger than a bare labeling-only rung 1, since the anti-circumvention regime carries real statutory damages, but the private right of action runs to injured providers/platforms, not to individual consumers directly, so it doesn't reach the broad-private-right-of-action rung 5. Scored 2, between labeling-only and criminal liability."
    F: "No data-center, permitting, siting, or energy provisions."
    R: "Applies to any provider of a generative AI system and any covered online platform of consequential size, with no revenue or size floor identified in the text — reaches essentially the entire developer- and platform-facing universe for AI-generated content."
    Depth: "Driven by the A axis (+2) and the enforceable civil-penalty regime backing E_consumer (2) — a real but disclosure/labeling-centered bill rather than one that reaches training conduct or compute inputs."
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
