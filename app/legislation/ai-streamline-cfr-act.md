---
title: Leveraging Artificial Intelligence to Streamline the Code of Federal Regulations Act
short_name: AI Streamline the CFR Act
bill_numbers:
- S. 1110
- H.R. 7226
congress: 119
topic: Government Use & Procurement
status: introduced
chamber_origin: Senate
introduced_date: '2025-03-25'
last_action: Referred to House Committees on the Judiciary and Oversight and Government Reform (H.R. 7226); Senate companion remains at Homeland Security and Governmental Affairs
last_action_date: '2026-01-22'
sponsors:
- Sen. Jon Husted (R-OH)
- Rep. Blake Moore (R-UT)
cosponsor_count: 8
committees:
- Senate Homeland Security and Governmental Affairs
- House Judiciary
- House Oversight and Government Reform
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
    P: 0.60
  likelihood:
    p_committee: 0.06
    p_enact: 0.02
    basis: "govtrack_corroborated"
  rationale:
    A: "This bill binds federal agencies as regulators reviewing their own rules, not AI developers — OMB (with NIST) must run an AI system that flags redundant/outdated/conflicting CFR provisions and refer them to the issuing agency, which then has 30 days to decide whether to rescind or amend. No AI developer, provider, or deployer is subject to any obligation here; this is a government-use-of-AI procurement/process condition. Scored at the procurement/government-use rung (+0.5) — it binds the government's own use of AI as a tool, not any builder — rather than 0, because the mandate to actually stand up and run the AI review system (with defined accuracy/transparency/accountability/national-security standards) is a real, if internally-facing, process requirement rather than a pure study or definition."
    B: "No preemption or state-authority language anywhere in the bill text — this is a purely federal-agency-internal administrative process (OMB/NIST/agency rule review) that does not regulate private conduct or touch state law at all, so it is silent on preemption (0). The implicit-preemption floor does not apply because A does not reach +2 and this bill does not establish a regulatory scheme governing private AI development or deployment."
    C: "Directs OMB, in consultation with NIST, to implement and annually run a government-wide AI-based regulatory-review process across the entire CFR, with agencies bound to 30-day response and rescission/amendment deadlines — a standing, recurring administrative process with real deadlines, though it's not an evaluation body dedicated to AI safety, a testbed, or an incident-reporting stream aimed at governing AI development; scored above a plain study (+1) but below a dedicated evaluation body (+4) at the standing-process rung, landing at +1 to reflect the genuine annual recurring statutory duty."
    D: "No export-control, chip-access, or other geopolitical-competition content anywhere in the bill."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election-integrity content — this is a federal regulatory-review process bill with no consumer-facing provisions."
    F: "No data-center, permitting, interconnection, or ratepayer content."
    R: "Applies government-wide across the entire Code of Federal Regulations and every issuing agency, with no sector carve-out or threshold — full reach within its target class (federal regulatory agencies), even though that class itself (government processes) is narrower than a frontier-developer or consumer-facing bill's universe."
    Depth: "max(|A|=0.5, |B|=0, |C|=1, |F|=0, E=0)/5 = 0.20 — a shallow bill: a real but internally-facing government process on C, a light procurement-style touch on A, nothing on the other axes."
    E_f: "Agencies face binding 30-day deadlines to act on flagged regulations once OMB's process identifies them, which is more than a bare obligation with no stated penalty (30-day statutory deadlines carry some structural bite even absent a civil-penalty scheme), but there's no rulemaking-backed civil penalty regime, AG enforcement, or private right of action — landing at the obligation-with-no-stated-penalty rung, since the only 'enforcement' is the ordinary administrative-law expectation that agencies follow statutory deadlines."
    P: "Modeled explicitly on Ohio's state-level AI regulatory-review tool (cited by the sponsor as saving ~$44 million and 58,000 work-hours over a decade); if enacted, a federal-government-wide AI regulatory-review mandate would be a first-in-nation framework at the federal level likely to be watched by other agencies and possibly copied at the state level, landing at the first-in-nation rung given the explicit state-template lineage and government-wide scope."
    likelihood: "GovTrack models S. 1110 at only a 6% chance of enactment. Both the Senate version (introduced 2025-03-25, referred to Homeland Security and Governmental Affairs) and the House version (H.R. 7226, introduced 2026-01-22, referred jointly to Judiciary and Oversight and Government Reform) remain at bare committee referral with no hearing, markup, or floor action identified in either chamber as of 2026-09-10 — roughly 18 months of Senate inaction and 8 months of House inaction. All identified sponsors and cosponsors on both bills are Republican (Husted, Ernst, Blackburn, Budd, Banks, Ricketts, Mullin in the Senate; Moore, Bean in the House), so this is a single-party messaging/efficiency bill rather than a bipartisan one, which further dampens odds of advancing given divided government dynamics. p_enact is set slightly below GovTrack's 6% Senate-version figure to account for the House version's total lack of independent momentum and the bill's stalled multi-committee House referral."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- government use
- regulatory review
- OMB
- NIST
sources:
- label: Congress.gov (Senate)
  url: https://www.congress.gov/bill/119th-congress/senate-bill/1110
- label: Congress.gov (House)
  url: https://www.congress.gov/bill/119th-congress/house-bill/7226
- label: Introduced text (GovInfo)
  url: https://www.govinfo.gov/app/details/BILLS-119s1110is
- label: Husted press release
  url: https://www.husted.senate.gov/media/press-releases/husted-introduces-bill-leveraging-ai-to-increase-efficiency-within-federal-code/
- label: Moore press release
  url: https://blakemoore.house.gov/media/press-releases/congressman-blake-moore-introduces-legislation-to-identify-redundant-and-outdated-rules-in-federal-regulations
- label: GovTrack (S. 1110)
  url: https://www.govtrack.us/congress/bills/119/s1110
summary: Requires OMB, in consultation with NIST, to run an annual AI-based review of the entire Code of Federal Regulations to flag redundant, outdated, or conflicting rules, with issuing agencies given 30 days to rescind or amend flagged provisions.
timeline:
- date: '2025-03-25'
  event: S. 1110 introduced by Sen. Husted with Republican cosponsors; referred to Senate Homeland Security and Governmental Affairs
- date: '2026-01-22'
  event: H.R. 7226 introduced by Rep. Moore; referred to House Judiciary and House Oversight and Government Reform
- date: '2026-09-10'
  event: Added to tracker. GovTrack models a 6% enactment probability for S. 1110; no committee markup or floor action identified for either version.
---

The bill directs the Office of Management and Budget, in consultation with NIST, to implement — within 90 days of enactment and then annually — an AI-based review of the entire Code of Federal Regulations to identify redundant, outdated, or conflicting rules across all federal agencies. The AI system must meet defined standards for accuracy, transparency, accountability, and national-security risk. When the system flags a regulation, it refers the finding to the agency that issued it; that agency has 30 days to determine whether the rule is redundant or outdated, and must then rescind (if redundant) or amend/remove (if outdated) within another 30 days. Final decision-making authority stays with the issuing agency — the AI recommends, it does not auto-repeal. The approach is modeled on a state-level AI regulatory-review tool Ohio adopted under then-Lieutenant Governor Husted, which the sponsor's office credits with roughly $44 million in savings and 58,000 work-hours reclaimed over a decade. The Senate version (S. 1110) has been pending since March 2025 and the House companion (H.R. 7226) since January 2026; neither has seen a hearing, markup, or floor vote.
