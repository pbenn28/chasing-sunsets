---
title: "Artificial Intelligence Data Center Moratorium Act (House)"
short_name: "AI Data Center Moratorium Act (H.R.9442)"
bill_numbers: ["H.R. 9442"]
congress: 119
topic: "Data Centers & Energy"
status: "committee"
chamber_origin: "House"
introduced_date: "2026-06-24"
last_action: "Cosponsor added (Rep. Shomari Figures, D-AL); referred to House Energy and Commerce and Foreign Affairs Committees"
last_action_date: "2026-07-22"
sponsors: ["Rep. Alexandria Ocasio-Cortez (D-NY)"]
cosponsor_count: 13
committees: ["House Energy and Commerce", "House Foreign Affairs"]
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 1.0
    D: 0.0
    F: 5.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 1.0
    D: 1.0
    E_f: 0.6
    P: 0.6
  likelihood:
    p_committee: 0.3
    p_enact: 0.05
    basis: "base_rate_heuristic_no_live_lookup"
  rationale:
    A: "Doesn't regulate the act of training or deploying a model at all — its entire mechanism is a construction and expansion freeze on data-center facilities, a physical input rather than developer conduct. The future safety-review legislation it seeks to compel is a precondition for lifting the moratorium, not a standard this bill itself imposes."
    B: "Contains no preemption language anywhere. The one mention of 'State' requires a data center to certify it hasn't used federal, state, or local subsidies — a disclosure requirement, not a preemption clause. The bill's enforcement tools (subpoenas, inspections, conditioning DOE permitting on compliance) act on the Secretary of Energy's own federal permitting leverage rather than displacing state or local zoning and siting authority; it even requires that affected communities be able to approve or reject construction once the moratorium lifts."
    C: "Unlike its Senate companion, this version doesn't include a DOE quarterly-reporting requirement — its governance-capacity content is limited to the safety-review precondition for lifting the moratorium."
    D: "No export-control, chip-access, or geopolitical content."
    E_consumer: "No consumer-harm, deepfake, NCII, or algorithmic-discrimination content."
    F: "A nationwide moratorium on constructing or expanding AI data centers above 20MW of power capacity, halting new compute buildout entirely until Congress acts — as sweeping a restriction on compute capacity as this kind of bill gets. It constrains buildout rather than easing it: nothing expedites permitting, subsidizes construction, or preempts local siting review, and any future construction is further conditioned on worker protections, local community approval, a subsidy ban, and ratepayer and environmental safeguards."
    R: "Uses the same nationwide 20MW threshold as its Senate companion, aiming to capture essentially all large-scale AI data center construction."
    Depth: "The moratorium itself is the bill's entire substance — every other provision exists to support or condition that freeze."
    E_f: "The moratorium implies agency-level enforcement of the construction bar, but the text doesn't spell out a penalty schedule or private right of action."
    P: "A nationwide construction moratorium tied to future federal legislation — a framework later bills could point to if it's enacted."
    likelihood: "13 cosponsors is a meaningful number, but all are Democrats from the party's progressive wing with no Republican support in sight, in a GOP-controlled House that isn't inclined to move it."
  confidence: high
  text_source: full_text
  scored_at: "2026-08-01"
tags: ["data centers", "moratorium", "energy", "labor"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/house-bill/9442"
summary: "House companion to Sanders' Senate bill; Ocasio-Cortez-led moratorium on new AI data center construction."
timeline:
  - date: "2026-03-25"
    event: "Sanders and Ocasio-Cortez jointly announce the bill concept (House version not yet introduced)"
  - date: "2026-06-24"
    event: "H.R. 9442 introduced by Rep. Ocasio-Cortez with 9 original cosponsors; referred to Energy and Commerce and Foreign Affairs Committees"
  - date: "2026-07-13"
    event: "Rep. Maxine Waters added as cosponsor"
  - date: "2026-07-22"
    event: "Rep. Shomari Figures added as cosponsor, bringing the total to 13"
---
The House companion to S. 4214, using the same moratorium mechanism: halting construction or expansion of "AI data centers" (facilities for large-scale AI development, or any facility exceeding 20 megawatts of power capacity with high-density computing) until Congress enacts legislation establishing federal AI safety review, worker protections including prevailing wage and union rights, local community approval requirements, a ban on public subsidies for such facilities, and protections against increased utility costs or environmental harm.

Rep. Ocasio-Cortez introduced it three months after Sen. Sanders introduced the Senate version, with nine original cosponsors and four more added since — all Democrats, several from the party's progressive wing.
