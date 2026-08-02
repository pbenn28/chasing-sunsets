---
title: "Artificial Intelligence Data Center Moratorium Act (Senate)"
short_name: "AI Data Center Moratorium Act (S.4214)"
bill_numbers: ["S. 4214"]
congress: 119
topic: "Data Centers & Energy"
status: "committee"
chamber_origin: "Senate"
introduced_date: "2026-03-25"
last_action: "Read twice and referred to the Senate Committee on Commerce, Science, and Transportation"
last_action_date: "2026-03-25"
sponsors: ["Sen. Bernie Sanders (I-VT)"]
cosponsor_count: 0
committees: ["Senate Commerce, Science, and Transportation"]
scoring:
  axes:
    A: 0.0
    B: -2.0
    C: 3.0
    D: 0.0
    F: 5.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 1.0
    D: 1.0
    E_f: 0.8
    P: 0.6
  likelihood:
    p_committee: 0.15
    p_enact: 0.02
    basis: "base_rate_heuristic_no_live_lookup"
  rationale:
    A: "Doesn't regulate the act of training or deploying a model. Its operative provisions — a construction/upgrade moratorium and DOE reporting on data-center facilities — act on a physical input, not developer conduct. Lifting the moratorium is conditioned on Congress later passing separate safety-review and worker-protection legislation, but that's a trigger for future action, not a standard this bill itself imposes."
    B: "Never uses the word 'preempt' and has no express savings clause, but Section 3(b) bars any construction or upgrading of covered AI data centers nationwide until Congress enacts specified follow-on legislation, with no carve-out letting a state or locality authorize construction on its own during the freeze. Combined with DOE's authority to condition future permitting on compliance, this effectively locks state and local siting and permitting authority out of the picture for as long as the moratorium runs."
    C: "Directs the Secretary of Energy to issue quarterly public reports on data centers' energy and water use, emissions, and labor practices — a standing, mandatory information flow into a federal reporting regime."
    D: "No export-control, chip-access, or geopolitical content."
    E_consumer: "No consumer-harm, deepfake, NCII, or algorithmic-discrimination content."
    F: "A nationwide moratorium on constructing or upgrading any AI data center above 20MW of capacity — a hard stop on new compute buildout until Congress acts. It restrains growth rather than accelerating it: nothing here subsidizes construction, expedites permitting, or preempts siting review in industry's favor — the bill halts construction outright."
    R: "A broad 20MW facility-size threshold intended to capture essentially all large-scale AI data center construction nationwide."
    Depth: "The moratorium is the bill's central and most consequential provision — the reporting mandate and preemption effects both flow from it."
    E_f: "The moratorium mechanism and DOE reporting requirement imply real enforcement teeth, closer to agency rulemaking backed by penalties than a bare, unenforced obligation."
    P: "A nationwide construction moratorium tied to future federal legislation — a first-of-its-kind framework that, if enacted, other bills would likely reference or copy."
    likelihood: "Zero cosponsors four months after introduction, with no hearings or other signs of momentum — a lone-sponsor bill with little visible traction."
  confidence: high
  text_source: full_text
  scored_at: "2026-08-01"
tags: ["data centers", "moratorium", "energy", "labor"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/senate-bill/4214"
summary: "Would halt new AI data center construction nationwide until Congress passes AI safety and worker-protection legislation."
timeline:
  - date: "2026-03-25"
    event: "Sanders and Rep. Ocasio-Cortez jointly announce the bill; S. 4214 introduced in the Senate"
  - date: "2026-03-25"
    event: "Read twice and referred to Senate Commerce Committee"
---
This bill would impose an immediate moratorium on constructing or upgrading "AI data centers" — facilities used for large-scale AI development or operation, or any facility exceeding 20 megawatts of power capacity with high-density computing or advanced cooling — until Congress separately enacts legislation establishing federal pre-release AI safety review, worker and economic benefit-sharing protections, and safeguards against AI data centers raising utility bills or harming the environment. It would also direct the Secretary of Energy to issue quarterly public reports on AI data centers' energy and water use, emissions, and labor practices.

It has a genuine House companion, H.R. 9442 (tracked separately on this page), introduced three months later by Rep. Alexandria Ocasio-Cortez with the same moratorium mechanism and threshold.
