---
title: Children Harmed by AI Technology Act (CHAT Act)
short_name: CHAT Act
bill_numbers:
- S. 2714
- H.R. 7218
congress: 119
topic: Children & Chatbots
status: committee
chamber_origin: Senate
introduced_date: '2025-09-04'
last_action: Read twice and referred to the Senate Committee on Commerce, Science, and Transportation
last_action_date: '2025-09-04'
sponsors:
- Sen. Jon Husted (R-OH)
cosponsor_count: 1
committees:
- Senate Commerce, Science, and Transportation
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 3.0
  impact_components:
    R: 1.0
    D: 0.60
    E_f: 0.60
    P: 0.60
  likelihood:
    p_committee: 0.20
    p_enact: 0.04
    basis: "base_rate_adjusted"
  rationale:
    A: "CORRECTED 2026-09-09 per the frontier/systemic-risk-vs-near-term-consumer-harm guardrail. Requires companies running companion AI chatbots to set up mandatory user accounts, tiered age verification, verifiable parental consent for minors, active monitoring for suicidal ideation, and blocking of sexually explicit content to minors — backed by FTC enforcement. This textually matches the '+2 mandated process' rung, but its subject is child/companion-bot safety (age verification, parental consent, content blocking for minors), not frontier-scale training, catastrophic/CBRN risk, loss-of-control, or systemic AI oversight. Per the guardrail, a real enforced child-safety mandate like this belongs near A's floor (rarely above +0.5-+1), with the actual severity carried on axis E. Previously scored 2.0; corrected to 0.5."
    B: "CORRECTED 2026-09-09: previously scored -1.0 on implicit-preemption-floor-style reasoning (a 'real federal regulatory scheme' with no savings clause), but that reasoning depended on treating the Sec. A conduct mandate as a federal AI-governance scheme triggering the floor (which requires A >= +2). Now that A is corrected to 0.5 (this is a child/companion-chatbot-safety regime, not a frontier/systemic AI regulatory scheme), the implicit-preemption floor's trigger condition doesn't hold, and even setting that aside, the bill's only preemption-adjacent language preserves FTC/state-AG enforcement of this federal standard rather than expressly preempting or expressly preserving states' separate chatbot-regulation authority -- the text is actually silent on preemption. Corrected from -1.0 to 0.0."
    C: "Suicidal-ideation notifications go to parents, not into any government database, and the bill doesn't create new enforcement staffing or an evaluation body — it doesn't add to the government's own oversight capacity."
    D: "No export-control or geopolitical content."
    E_consumer: "A child-safety bill targeting a specific, serious harm — sexually explicit chatbot content reaching minors — enforced through FTC and state-AG action, functioning like a hard access-restriction regime alongside comparable bills such as the GUARD Act, though it doesn't create a new criminal offense outright."
    F: "No data-center or energy content."
    R: "A federal bill applying broadly to AI chatbots serving minors, with no revenue or size threshold."
    Depth: "Driven mainly by the consumer-harm provisions (E) — the sexually-explicit-content safeguard is the bill's most consequential piece."
    E_f: "Sec. 5 gives the FTC UDAP-style rulemaking and enforcement authority, plus a parallel track letting state attorneys general sue for damages and restitution. There's no broad private right of action for individuals, but enforcement runs through both federal and state agencies with real penalties."
    P: "Joins an already-crowded field of chatbot child-safety bills — including the GUARD Act and CHATBOT Act — rather than breaking genuinely new ground on age verification and parental consent."
    likelihood: "No committee markup found on S. 2714 or H.R. 7218 as of 2026-09-09 — both remain at Senate/House committee referral. More significantly, sponsor Sen. Husted has effectively moved on: on 2026-07-28 he introduced 'CHAT Act 2.0' (S. 5154) with Sen. Andy Kim (D-NJ), a revised bill using a tiered risk system and carve-outs for customer-service/gaming bots, explicitly responding to industry pushback on the original text. That the lead sponsor is now championing a successor bill rather than pushing S. 2714 through committee is a negative signal for this specific bill's own path — attention and momentum in this policy area has shifted to the newer vehicle, while the CHATBOT Act and GUARD Act have separately continued to advance in Senate Commerce and Senate Judiciary respectively. No GovTrack prognosis page was checked directly (govtrack.us returned HTTP 403); p_committee and p_enact are lowered from the 8/1 estimate to reflect this apparent sponsor pivot away from the original text."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- chatbots
- child safety
- age verification
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/2714
- label: "Husted-Kim press release — CHAT Act 2.0 (S. 5154), a successor bill introduced 2026-07-28"
  url: https://www.husted.senate.gov/media/press-releases/husted-kim-lead-bipartisan-bill-to-protect-children-from-ai-companion-chatbots/
summary: Senate bill requiring AI chatbots to verify user age and add safeguards protecting minors.
timeline:
- date: '2025-09-04'
  event: Introduced and referred to Senate Commerce
- date: '2025-11-05'
  event: Sen. Bernie Moreno added as cosponsor
- date: '2026-01-22'
  event: House companion H.R. 7218 introduced
- date: '2026-07-28'
  event: "Sen. Husted introduces a successor bill, 'CHAT Act 2.0' (S. 5154), with Sen. Andy Kim (D-NJ) — a revised approach with tiered risk levels and carve-outs for customer-service/gaming bots; S. 2714 itself has seen no further committee action"
---

The CHAT Act would require AI chatbots to implement age-verification measures and establish protections for minor users — including verifiable parental consent before a minor accesses a chatbot, parental notification of any interaction involving suicidal ideation, and blocking minors from chatbots engaging in sexually explicit communication. It is one of several competing chatbot child-safety bills tracked here.

**Update (2026-09-09):** Sponsor Sen. Husted has introduced a successor bill, "CHAT Act 2.0" (S. 5154, with Sen. Andy Kim, D-NJ), that revises this approach with tiered risk levels and industry carve-outs — a signal that momentum has shifted away from this original text toward the newer vehicle.
