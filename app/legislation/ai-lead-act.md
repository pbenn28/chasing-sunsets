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
    A: 1.0
    B: -1.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 5.0
  impact_components:
    R: 0.90
    D: 1.00
    E_f: 1.00
    P: 0.80
  likelihood:
    p_committee: 0.33
    p_enact: 0.13
    basis: "govtrack_corroborated"
  rationale:
    A: "Corrected 2026-09-09 under the frontier/systemic-risk guardrail. The bill creates a federal products-liability cause of action against developers/deployers for negligent design, failure to warn, breach of express warranty, and strict liability for defective/unreasonably dangerous products, plus bars contractual waivers — a real, enforceable conduct standard. But its subject is not frontier-scale training, catastrophic/CBRN risk, loss-of-control, or systemic AI oversight capacity: it is a general products-liability regime that reaches 'any covered product' causing harm to 'any person,' i.e. ordinary consumer/deployer harm from AI already in ordinary commercial use, exactly the kind of domain-general consumer-harm mandate the guardrail says belongs on axis E rather than A. It textually matches A's +2 'mandated process with enforcement' rung, but the guardrail caps mechanisms like this near the floor (rarely above +0.5-+1) precisely because a real, enforced mandate can still be a consumer-harm bill rather than a frontier-safety one. Previously scored 2.0; corrected down to 1.0 to reflect that this is a general tort/liability regime, not a frontier-developer conduct standard -- axis E now carries the bill's real severity instead."
    B: "Section 304 text: 'This Act supersedes State law only where State law conflicts with the provisions of this Act,' paired with an express carve-out that 'nothing in this Act shall prevent a State from enacting or enforcing protections... stronger than such protections under this Act' aligned with the same harm-prevention/accountability/transparency principles. That is textbook conflict preemption with a genuine savings clause for stronger state law, matching the −1 rung exactly. Reviewed 2026-09-09 under the frontier/systemic-risk guardrail: the savings clause is scoped to this bill's own liability topic rather than state AI-regulatory authority broadly, which under the guardrail would cap an unconditional-sounding savings clause well below the '+3 affirmative guarantee' rung -- but since the score here is already the modest −1 conflict-preemption-only value rather than an inflated positive read, no correction is needed; the guardrail's concern is about over-crediting narrow-domain savings clauses, and this one was never scored at the higher rung to begin with. Now that A is corrected to +1.0 (below the ≥+2 threshold), the implicit-preemption floor no longer independently applies here either, though it wouldn't have changed the outcome since the express savings clause already resolves the question."
    C: "No new agency, evaluation body, incident-reporting channel, or enforcement staffing is created — enforcement runs through existing courts and existing state/federal AG offices using ordinary civil litigation, not a new government capacity to observe or evaluate AI."
    D: "No export-control or chip/compute-access content."
    E_consumer: "Corrected 2026-09-09: this is exactly what E is for under the frontier/systemic-risk guardrail, and is now where this bill's real severity should be read from given the A correction above. The liability framework is not limited to frontier developers — it reaches any 'covered product' causing harm to any person, i.e. ordinary consumers and deployers, through a private right of action (individual and class) plus state AG and U.S. AG enforcement, with damages, restitution, attorney's fees, and civil penalties. That is squarely the top rung on this axis: 'broad private right of action across sectors.' Previously scored 3.0 (the 'criminal liability for specific conduct' rung), which undersold both the bill's own text and its own rationale (which already described it as 'the top rung on this axis'); corrected up to 5.0 to match."
    F: "No data-center, permitting, siting, or energy content."
    R: "Covers any developer or deployer of a 'covered product' (broadly defined as software/data systems/tools using ML or computational methods to make predictions or recommendations affecting decisions) — a sweeping definition that reaches nearly the entire commercial AI industry, not just frontier labs, though some ambiguity remains around narrow non-AI software at the edges."
    Depth: "Recomputed after the frontier/systemic-risk guardrail correction — now driven by axis E (consumer/near-term harm) at 5.0/5."
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
