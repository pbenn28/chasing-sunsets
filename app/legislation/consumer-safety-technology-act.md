---
title: Consumer Safety Technology Act
short_name: Consumer Safety Technology Act
bill_numbers:
- H.R. 1770
- S. 2766
congress: 119
topic: Government Use & Procurement
status: passed_one_chamber
chamber_origin: House
introduced_date: '2025-03-03'
last_action: Received in the Senate; read twice and referred to the Committee on Commerce, Science, and Transportation
last_action_date: '2025-07-15'
sponsors:
- Rep. Darren Soto (D-FL)
cosponsor_count: 3
committees:
- House Energy and Commerce
- Senate Commerce, Science, and Transportation
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.85
    D: 0.20
    E_f: 0.40
    P: 0.40
  likelihood:
    p_committee: 0.55
    p_enact: 0.28
    basis: "govtrack_corroborated"
  rationale:
    A: "All three titles direct federal agencies (CPSC, Commerce, FTC) to pilot or study AI/blockchain tools for their own consumer-protection work — CPSC using AI internally to track injury trends, hazards, and noncompliant imports. This binds the government-as-buyer/user, not AI developers, matching the procurement/government-use rung rather than any conduct standard on developers; confirmed against the engrossed full text, which contains no developer-facing obligation anywhere."
    B: "Full engrossed text (govinfo.gov BILLS-119hr1770eh) contains no state-law, state-authority, or preemption/savings-clause language of any kind. A stays at 0.5, well below the +2 threshold that would trigger the implicit-preemption floor, so B is correctly silent rather than floored."
    C: "Title I requires CPSC to report to Congress within a year of the pilot's conclusion; Title II requires a Commerce/FTC blockchain study reported within 6 months of completion; Title III requires an FTC report within a year on token-marketplace enforcement. Three time-bound studies/reports to Congress, not a new agency or standing enforcement authority, matching the 'studies... with real reporting deadlines' rung."
    D: "No export-control or geopolitical-competition content."
    E_consumer: "The CPSC pilot targets consumer-product injuries and unsafe imports generally (using AI as a detection tool), not the deepfake/NCII/companion-bot/discrimination/election-integrity harms this axis measures, and creates no new consumer right or liability. Scored 0."
    F: "No data-center, permitting, siting, or energy content."
    R: "A federal bill directing CPSC, Commerce, and FTC action with no sector carve-outs — but its substance is three narrow pilot/study mandates rather than a rule reaching the whole AI industry, so R sits high but not at 1.0."
    Depth: "Depth = max(|A|,|B|,|C|,|F|,E)/5 = max(0.5,0,1,0,0)/5 = 0.20, driven by the modest C (reporting-study) score since A is only a government-use condition and every other axis is 0."
    E_f: "Reporting mandates to Congress with no stated penalty for the agencies involved and no rulemaking or civil-penalty authority created — an obligation with no attached enforcement teeth, matching the 0.4 rung."
    P: "Three sector-specific, self-contained pilot/study programs (consumer product safety, blockchain, token marketplaces) rather than a first-in-nation template or a permanent institution."
    likelihood: "Passed the House 336-36 on July 14, 2025 (Roll Call No. 192, confirmed via the House Clerk's official record), a lopsided bipartisan margin reflecting the bill's non-controversial government-use/study content. Received in the Senate and referred to Commerce, Science, and Transportation on July 15, 2025, with a real (though not textually identical) companion, S. 2766, introduced by Sen. John Curtis (R-UT) with Sen. Lisa Blunt Rochester (D-DE) on September 10, 2025 — no Senate markup or floor action identified since. GovTrack's own modeled prognosis for H.R. 1770 is approximately 28%, which this estimate adopts directly as the anchor: a House-passed, non-controversial, bipartisan bill with an active if not-yet-moving Senate companion sits well above the base rate for introduced bills, but Senate floor time for a low-profile House-passed measure is still the binding constraint."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- CPSC
- blockchain
- consumer product safety
- pilot program
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/1770
- label: House Clerk roll call 192 (336-36)
  url: https://clerk.house.gov/Votes/2025192
- label: Senate companion S. 2766
  url: https://www.congress.gov/bill/119th-congress/senate-bill/2766
- label: GovTrack prognosis
  url: https://www.govtrack.us/congress/bills/119/hr1770
summary: House-passed (336-36) bill directing a CPSC AI pilot program plus Commerce/FTC blockchain and token studies; Senate companion S. 2766 pending in Commerce Committee.
timeline:
- date: '2025-03-03'
  event: Introduced in the House by Rep. Darren Soto (D-FL); referred to Energy and Commerce
- date: '2025-07-14'
  event: Passed the House 336-36 (Roll Call No. 192) under suspension of the rules
- date: '2025-07-15'
  event: Received in the Senate; referred to Commerce, Science, and Transportation
- date: '2025-09-10'
  event: Senate companion S. 2766 introduced by Sen. John Curtis (R-UT) with Sen. Lisa Blunt Rochester (D-DE); referred to Senate Commerce
- date: '2026-09-09'
  event: Verified via House Clerk roll call, engrossed full text, and Senate companion status — no Senate committee action identified since referral
---

The bill directs the Consumer Product Safety Commission to establish a one-year pilot program exploring AI tools to track consumer-product injury trends, identify hazards, monitor for recalled products, and flag noncompliant imports at ports of entry. It also requires the Department of Commerce (with the FTC) to study blockchain applications for consumer protection and fraud prevention, and requires the FTC to report on its own enforcement posture toward the "token marketplace." All three components direct federal agencies to pilot or study these technologies for their own consumer-protection work; none impose obligations on private AI developers. The bill passed the House 336-36 on July 14, 2025, and has a Senate companion, S. 2766, introduced by Sen. John Curtis (R-UT) with Sen. Lisa Blunt Rochester (D-DE) on September 10, 2025, currently pending in the Senate Commerce Committee.
