---
title: Deterring American AI Model Theft Act of 2026
short_name: Deterring American AI Model Theft Act
bill_numbers:
- H.R. 8283
congress: 119
topic: Chips & National Security
status: committee_passed
chamber_origin: House
introduced_date: '2026-04-15'
last_action: Ordered to be reported (amended) by the House Foreign Affairs Committee, 43-0
last_action_date: '2026-04-22'
sponsors:
- Rep. Bill Huizenga (R-MI)
cosponsor_count: 21
committees:
- House Foreign Affairs
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 3.0
    D: 4.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 1.00
    D: 0.60
    E_f: 0.80
    P: 0.40
  likelihood:
    p_committee: 0.97
    p_enact: 0.32
    basis: "govtrack_corroborated"
  rationale:
    A: "Places no obligations on AI developers — its mechanisms (threat-sharing, sanctions, Entity List additions) target foreign entities that steal model weights, with U.S. developers only on the receiving end of Commerce threat-sharing."
    B: "Silent on preemption; the bill never addresses state authority or state law at all, running entirely through federal Commerce, State Department, and sanctions authority."
    C: "Stands up a public State Department 'AI Model Extraction Attackers List,' a mandatory 180-day risk assessment, and required Commerce-to-model-owner threat-sharing — a new standing reporting apparatus with real deadlines."
    D: "Authorizes IEEPA sanctions, including asset freezes, and Commerce Entity List additions against foreign entities caught extracting U.S. model weights — a meaningful new export/trade restriction triggered specifically by model-weight theft."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election-integrity content; the bill is entirely focused on national security and IP theft."
    F: "No data-center, permitting, interconnection, or ratepayer content."
    R: "A federal bill with no revenue floor or sector carve-out — it applies to any foreign entity extracting any U.S. closed-source AI model's technical characteristics and protects any U.S. model owner."
    Depth: "Driven mainly by the new mandatory reporting and attacker-list apparatus it creates -- the bill doesn't reach much further beyond that."
    E_f: "Enforcement runs through executive action — IEEPA sanctions, asset freezes, and Commerce Entity List designation — carrying real economic consequences without requiring a private lawsuit."
    P: "A narrow, self-contained national-security mechanism aimed specifically at AI model-weight theft, rather than a permanent new institution or a template other legislation is likely to copy."
    likelihood: "Re-verified 2026-09-09: cosponsor count has grown from 18 to 21 (19 R / 2 D) since 8/1, but the bill has not moved beyond its April 22, 2026 committee order-to-report — no House floor vote, no Rules Committee action, and no Senate companion introduction found. (A secondary source reference to a Lawler 'Consensus Calendar' motion appears to be a generic description of that procedural mechanism rather than a documented action specific to this bill — that calendar requires 290 cosponsors, far beyond this bill's 21, and applies only to bills unreported by committee, which this one is not, so it is not treated as fact here.) GovTrack does not publish a numeric prognosis. Committee passage was unanimous and uncontroversial national-security subject matter continues to support a high p_committee-equivalent outcome (already achieved), but p_enact is essentially unchanged from 8/1 absent a floor schedule or Senate vehicle."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- model weights
- theft
- sanctions
- national security
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/8283
- label: Legisletter, H.R. 8283 tracker
  url: https://legisletter.org/bill/hr8283-deterring-ai-model-theft-act
summary: Would sanction and counter foreign theft of American closed-source AI model weights.
timeline:
- date: '2026-04-15'
  event: Introduced in the House
- date: '2026-04-22'
  event: Ordered reported (amended) by House Foreign Affairs, 43-0
- date: '2026-09-09'
  event: Re-verified — cosponsor count grown to 21; still no House floor vote or Senate companion
---

The bill aims to prevent foreign adversaries from extracting key technical features — such as model weights — of closed-source, American-owned AI models. It would require federal agencies to identify foreign “entities of concern” illicitly accessing model characteristics, direct Commerce to share threat information with U.S. model owners, mandate a State Department assessment within 180 days, and authorize sanctions.
