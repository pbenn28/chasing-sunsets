---
title: Content Origin Protection and Integrity from Edited and Deepfaked Media Act of 2025 (COPIED Act)
short_name: COPIED Act
bill_numbers:
- S. 1396
congress: 119
topic: Deepfakes & Synthetic Media
status: committee
chamber_origin: Senate
introduced_date: '2025-04-09'
last_action: Read twice and referred to the Senate Committee on Commerce, Science, and Transportation
last_action_date: '2025-04-09'
sponsors:
- Sen. Maria Cantwell (D-WA)
- Sen. Marsha Blackburn (R-TN)
- Sen. Martin Heinrich (D-NM)
cosponsor_count: 2
committees:
- Senate Commerce, Science, and Transportation
scoring:
  axes:
    A: 0.5
    B: -1.0
    C: 0.5
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.0
  impact_components:
    R: 0.90
    D: 0.40
    E_f: 0.80
    P: 0.80
  likelihood:
    p_committee: 0.35
    p_enact: 0.12
    basis: "base_rate_adjusted"
  rationale:
    A: "Corrected under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: the provenance-attachment mandate, anti-tampering rule, and unauthorized-training bar are all about synthetic-content authenticity and copyright — a deepfake/creator-harm domain that axis E exists to capture — not about frontier-scale training, catastrophic risk, or systemic AI oversight. Nothing here reaches frontier-model training or deployment-scale risk; the 'active process requirement' previously read against A's '+2 mandated process' rung is really a labeling/provenance regime aimed at synthetic-media authenticity. Previously scored 2.0; corrected down to sit near the guardrail's floor (rarely above +0.5-1), landing at 0.5 given the mandate is real and enforced even though its object isn't frontier/systemic risk."
    B: "The bill preserves states' ability to enforce their own civil and criminal law and creates a state-AG enforcement role, but doesn't affirmatively guarantee states can impose their own, potentially stricter, provenance requirements. Combined with the federal regulatory scheme it builds (NIST standards plus FTC/state-AG/private enforcement) and the absence of a clear savings clause, the practical effect leans toward crowding out independent state provenance/labeling rules specifically — not state authority to regulate frontier AI development broadly, which this bill never reaches. Consistent with the frontier/systemic-risk-vs-near-term-consumer-harm guardrail's symmetric logic (a narrow-domain mechanism shouldn't be scored as a deep move on state AI-regulatory authority just because it's unconditional within its own topic), this stays at the mildest preemption rung, -1 (conflict preemption only), rather than any deeper field-preemption value."
    C: "Corrected under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: the NIST provenance/watermarking standards and the FTC/state-AG enforcement authority are a standing information/enforcement flow aimed at synthetic-content authenticity and copyright, not at frontier or systemic AI oversight capacity. Previously scored 2.0 (enforcement staffing/new authority for an existing regulator); corrected down to sit near the guardrail's floor (rarely above +0.5-1), landing at 0.5 since the mechanism's object is deepfake/provenance and copyright enforcement, which axis E is meant to carry."
    D: "No export-control, chip-access, or geopolitical-competition content."
    E_consumer: "Bars stripping or tampering with provenance data and bars unauthorized AI training on protected works, enforced by the FTC and state AGs — more substantive than a bare labeling requirement, though enforcement is civil rather than criminal and there's no private right of action."
    F: "No data-center, permitting, or energy content."
    R: "A federal bill reaching AI content-creation tools, large platforms, and AI training practices broadly, with no revenue or sector carve-outs."
    Depth: "max(|A|=0.5, |B|=1.0, |C|=0.5, |F|=0, E=2)/5 = 0.40, driven mainly by the E axis (consumer/creator harm), not by any frontier-developer or governance-capacity axis."
    E_f: "Enforcement runs through FTC rulemaking and civil-penalty authority alongside state-AG civil enforcement."
    P: "Would be the first federal content-provenance framework of its kind (NIST standards plus platform obligations), likely to serve as a template for later provenance mandates even though it doesn't itself create a permanent institution."
    likelihood: "A bipartisan three-sponsor pairing (Cantwell, Blackburn, Heinrich) helps its odds, but the bill has sat with no committee action since introduction in April 2025 — as of 9/9/26, 17 months of inactivity in Senate Commerce, with no markup announced. That continued dormancy weighs against near-term movement despite the bipartisan support."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- provenance
- watermarking
- synthetic media
- NIST
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/1396
summary: Bipartisan Senate bill requiring AI content-provenance standards and protecting creators' work from unauthorized AI training.
timeline:
- date: '2025-04-09'
  event: Introduced and referred to Senate Commerce Committee
- date: '2026-09-09'
  event: Re-verified — no committee markup scheduled or held since introduction
---

The COPIED Act would direct NIST to develop standards for content provenance, watermarking, and synthetic-content detection, and require certain AI tools to let users attach provenance information to content they create or significantly modify. It would prohibit large platforms from stripping or tampering with that information and bar unauthorized use of provenance-protected copyrighted works to train AI, with FTC and state-AG enforcement.
