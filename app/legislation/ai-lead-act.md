---
title: "AI LEAD Act (Aligning Incentives for Leadership, Excellence, and Advancement in Development Act)"
short_name: "AI LEAD Act"
bill_numbers: ["S. 2937"]
congress: 119
topic: "Frontier Safety & Oversight"
status: "committee"
chamber_origin: "Senate"
introduced_date: "2025-09-29"
last_action: "Read twice and referred to the Senate Committee on the Judiciary"
last_action_date: "2025-09-29"
sponsors: ["Sen. Dick Durbin (D-IL)", "Sen. Josh Hawley (R-MO)"]
cosponsor_count: 0
committees: ["Senate Judiciary"]
scoring:
  axes:
    A: 2.0
    B: -1.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 3.0
  impact_components:
    R: 0.90
    D: 0.60
    E_f: 1.00
    P: 0.80
  likelihood:
    p_committee: 0.33
    p_enact: 0.13
    basis: "govtrack_corroborated"
  rationale:
    A: "Creates a federal products-liability cause of action against AI developers for negligent design, failure to warn, breach of express warranty, and strict liability for defective/unreasonably dangerous products, plus bars contractual waivers of this liability. This is a substantive, enforceable conduct standard on developers — reasonable-care and warning obligations backed by real enforcement (private suits, state AG, U.S. AG) — but it is not pre-deployment gating by an outside party (no licensing, audit, or certification-before-release requirement) and not government shutdown/recall authority, so it lands at the +2 'mandated process with enforcement' rung rather than +3 or +4."
    B: "Section 304 text: 'This Act supersedes State law only where State law conflicts with the provisions of this Act,' paired with an express carve-out that 'nothing in this Act shall prevent a State from enacting or enforcing protections... stronger than such protections under this Act' aligned with the same harm-prevention/accountability/transparency principles. That is textbook conflict preemption with a genuine savings clause for stronger state law, matching the −1 rung exactly. Because there's an express savings clause, the implicit-preemption floor (which would otherwise apply since A ≥ +2) is not needed — the actual text already resolves the question in states' favor rather than being silent."
    C: "No new agency, evaluation body, incident-reporting channel, or enforcement staffing is created — enforcement runs through existing courts and existing state/federal AG offices using ordinary civil litigation, not a new government capacity to observe or evaluate AI."
    D: "No export-control or chip/compute-access content."
    E_consumer: "The liability framework is not limited to frontier developers — it reaches any 'covered product' causing harm to any person, i.e. ordinary consumers and deployers, through a private right of action plus state/federal AG enforcement with damages, restitution, and civil penalties. That is a broad private right of action across sectors, the top rung on this axis, even though the bill's headline framing is about AI developers generally rather than a named consumer-harm category like deepfakes or NCII."
    F: "No data-center, permitting, siting, or energy content."
    R: "Covers any developer or deployer of a 'covered product' (broadly defined as software/data systems/tools using ML or computational methods to make predictions or recommendations affecting decisions) — a sweeping definition that reaches nearly the entire commercial AI industry, not just frontier labs, though some ambiguity remains around narrow non-AI software at the edges."
    Depth: "Driven primarily by E (broad private right of action, 3/5) and secondarily by A (new liability exposure, 2/5); B's −1 conflict-preemption-only score is the smallest magnitude among the moving axes."
    E_f: "Backed by a genuine private right of action (individual and class claims) plus state AG and U.S. AG enforcement authority, with damages, restitution, attorney's fees, and civil penalties available — the top rung on this component by definition."
    P: "Would be the first federal products-liability statute purpose-built for AI harms, creating a durable framework (negligence/warranty/strict-liability causes of action, anti-waiver provision, 4-year discovery-rule statute of limitations) that plaintiffs' bars and other legislators would likely measure future AI liability proposals against — a first-in-nation framework likely to be copied or extended, short of also creating a permanent institution or a hard preemption ceiling."
    likelihood: "GovTrack.us gives S. 2937 a 33% chance of clearing committee and a 13% chance of enactment — well above the typical single-bill base rate, reflecting the bipartisan Durbin-Hawley pairing (an unusual left-right combination that has previously moved tech-liability bills like KOSA and the STOP CSAM Act) and continued news-cycle attention to AI harm litigation. No committee markup has occurred as of this check, roughly eleven months after introduction, and no House companion has been identified — but the sponsor pairing and sustained advocacy from groups like CCDH keep this above a typical single-sponsor bill's odds."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags: ["liability", "products liability", "private right of action", "preemption"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/senate-bill/2937"
  - label: "Sponsor press release (Sen. Durbin)"
    url: "https://www.durbin.senate.gov/newsroom/press-releases/durbin-hawley-introduce-bill-allowing-victims-to-sue-ai-companies"
  - label: "GovTrack.us"
    url: "https://www.govtrack.us/congress/bills/119/s2937"
summary: "Would create a federal products-liability framework letting people harmed by AI systems sue developers and deployers for negligent design, failure to warn, breach of warranty, or defective/unreasonably dangerous products — while barring companies from contracting around that liability."
timeline:
  - date: "2025-09-29"
    event: "Introduced by Sen. Durbin with Sen. Hawley; read twice and referred to the Senate Judiciary Committee"
---
The AI LEAD Act (Aligning Incentives for Leadership, Excellence, and Advancement in Development Act) would treat AI systems as products for liability purposes, creating a federal cause of action against developers who fail to exercise reasonable care in design, provide inadequate warnings, break an express warranty, or ship a product that is defective or unreasonably dangerous. Deployers face the same liability if they substantially modify a covered product or intentionally misuse it outside its intended purpose. The bill bars developers from using contracts or terms of service to waive or limit this liability — closing off a defense tech companies have relied on — and gives individuals, classes of plaintiffs, state attorneys general, and the U.S. Attorney General standing to sue for damages, restitution, injunctive relief, attorney's fees, and civil penalties, subject to a four-year discovery-based statute of limitations.

On preemption, the bill supersedes state law only where state law actually conflicts with it, and expressly preserves states' ability to enact or enforce AI protections stronger than the federal floor, so long as they align with the same harm-prevention, accountability, and transparency principles. Sponsored by Sens. Dick Durbin and Josh Hawley — an unusual bipartisan pairing that has previously teamed up on other tech-accountability bills — it was introduced in the Senate on September 29, 2025 and referred to the Senate Judiciary Committee, where it has not yet received a markup.
