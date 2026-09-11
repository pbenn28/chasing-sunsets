---
title: American Security Robotics Act of 2026
short_name: American Security Robotics Act
bill_numbers:
- H.R. 8189
- S. 4235
congress: 119
topic: Chips & National Security
status: committee
chamber_origin: Both
introduced_date: '2026-04-02'
last_action: Referred to the House Committee on Oversight and Government Reform
last_action_date: '2026-04-02'
sponsors:
- Rep. Elise Stefanik (R-NY)
- Sen. Tom Cotton (R-AR)
- Sen. Chuck Schumer (D-NY)
cosponsor_count: 0
committees:
- House Oversight and Government Reform
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 0.0
    D: 2.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.85
    D: 0.10
    E_f: 0.60
    P: 0.40
  likelihood:
    p_committee: 0.11
    p_enact: 0.04
    basis: "govtrack_corroborated"
  rationale:
    A: "Bars executive agencies from procuring or operating unmanned ground vehicles and humanoid/patrol robots made by foreign-adversary entities — a condition on federal purchasing and government use, not a conduct standard on how any developer (foreign or domestic) builds or trains AI systems generally. This is a procurement/government-use bar, so it lands at the +0.5 rung rather than higher."
    B: "No preemption or savings-clause language found in press materials or available bill text; the bill only binds federal executive-agency procurement and operation, an area with no meaningful state regulatory analog, so this doesn't trigger the implicit-preemption floor (A is well below +2)."
    C: "No new inspection body, incident-reporting channel, or enforcement staffing created — the ban is self-executing against agency procurement/operating decisions rather than building a standing oversight function."
    D: "A binding restriction on federal acquisition and operation of adversary-linked ground-robot/UGV hardware on national-security grounds — narrower than a chip/model-weight export control, but a real geopolitical access restriction rather than a study."
    E_consumer: "No deepfake, NCII, discrimination, or election content — purely a government-procurement, national-security measure aimed at foreign-made robots."
    F: "No data-center, compute, permitting, siting, or energy content."
    R: "Covers the entire executive-agency universe for the specific hardware class (unmanned ground vehicles/robots) from a covered foreign-adversary entity, though narrower in scope than a bill covering all AI systems or all hardware."
    Depth: "Recomputed after the frontier/systemic-risk guardrail correction — now driven by axis A (frontier developer stringency) at 0.5/5."
    E_f: "No stated penalty provision surfaced in press or available text beyond the procurement bar itself; enforcement would run through normal federal acquisition compliance channels (FAR-type bar enforced by contracting officers/IGs) rather than civil penalties or a private right of action."
    P: "A sector-specific, self-contained procurement restriction on one hardware category (ground robots/UGVs from adversary entities) — follows the template of prior foreign-adversary-AI procurement bars rather than establishing new precedent."
    likelihood: "GovTrack.us gives H.R. 8189 an 11% chance of getting past committee and a 4% chance of enactment, in line with base rates for freshman-Congress procurement bills referred to a single committee with zero House cosponsors as of this check. The bipartisan, bicameral pairing (Stefanik in the House; Cotton and Schumer co-leading the Senate companion, S. 4235) is a positive signal relative to a typical single-sponsor bill, and this is the kind of narrow national-security procurement text that sometimes rides on the NDAA — but no evidence of NDAA inclusion or committee action was found as of 2026-09-09, six months after introduction."
  confidence: low
  text_source: summary
  scored_at: "2026-09-09"
tags:
- procurement
- robotics
- foreign adversary
- national security
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/house-bill/8189"
  - label: "Sponsor press release (Rep. Stefanik)"
    url: "https://stefanik.house.gov/2026/3/stefanik-cotton-introduce-bipartisan-bill-to-propel-america-s-robotics-superiority-protect-u-s-national-security"
  - label: "GovTrack.us"
    url: "https://www.govtrack.us/congress/bills/119/hr8189"
summary: "Would bar federal agencies from procuring or operating unmanned ground vehicles and robots — including humanoid robots and autonomous patrol technology — made by foreign-adversary entities, chiefly aimed at Chinese-linked robotics manufacturers."
timeline:
- date: '2026-04-02'
  event: "Introduced by Rep. Stefanik in the House; companion S. 4235 introduced by Sens. Cotton and Schumer in the Senate (2026-03-26/27)"
- date: '2026-04-02'
  event: "Referred to the House Committee on Oversight and Government Reform"
---
The American Security Robotics Act of 2026 would prohibit federal executive agencies from procuring or operating "covered unmanned ground vehicle systems" — remote surveillance vehicles, autonomous patrol technology, mobile robotics, and humanoid robots capable of ground locomotion at a distance from a human operator — when those systems are manufactured by entities tied to foreign adversary nations, principally China. It follows the template of earlier foreign-adversary-AI procurement bars (e.g. the No Adversarial AI Act) but is scoped specifically to ground robotics hardware rather than AI software generally.

The bill was introduced in the House by Rep. Elise Stefanik with a bipartisan, bicameral companion (S. 4235) led by Sens. Tom Cotton and Chuck Schumer in the Senate. As of this check it has no House cosponsors and has seen no committee action since referral to House Oversight and Government Reform on April 2, 2026. Full statutory text (covered-entity definitions, effective date, and any exemptions) was not independently confirmed against congress.gov, which returned a 403 for this pass — scoring here relies on the bill's official summary and sponsor press materials.
