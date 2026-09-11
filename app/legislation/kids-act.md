---
title: "Kids Internet and Digital Safety Act (KIDS Act)"
short_name: "KIDS Act"
bill_numbers: ["H.R. 7757"]
congress: 119
topic: "Children & Chatbots"
status: "passed_one_chamber"
chamber_origin: "House"
introduced_date: "2026-03-03"
last_action: "Received in the Senate, read twice, and referred to the Committee on Commerce, Science, and Transportation"
last_action_date: "2026-07-13"
sponsors: ["Rep. Brett Guthrie (R-KY)", "Rep. Frank Pallone (D-NJ)"]
cosponsor_count: null
committees: ["House Energy and Commerce", "House Judiciary", "Senate Commerce, Science, and Transportation"]
scoring:
  axes:
    A: 0.5
    B: -1.0
    C: 0.5
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 3.0
  impact_components:
    R: 0.9
    D: 0.60
    E_f: 0.8
    P: 0.6
  likelihood:
    p_committee: 0.60
    p_enact: 0.22
    basis: "base_rate_adjusted"
  rationale:
    A: "CORRECTED 2026-09-09 per the frontier/systemic-risk-vs-near-term-consumer-harm guardrail. Title IV requires AI chatbots to disclose they aren't human, bars them from claiming to be licensed professionals, mandates crisis-hotline referrals when a minor raises self-harm or suicide, and requires 'take a break' prompts after three hours of continuous use, backed by FTC and state-AG enforcement. This is a real, enforced conduct standard, but its subject is child-safety disclosure/crisis-referral/design (screen-time break prompts), not frontier-scale training, catastrophic/CBRN risk, loss-of-control, or systemic AI oversight -- it doesn't touch frontier model training or release. Per the guardrail this belongs near A's floor (rarely above +0.5-+1); previously scored 1.0, corrected to 0.5 for consistency with comparable child-safety conduct mandates elsewhere in this cluster (e.g. chatbot-act.md, chat-act.md) now scored at the same level."
    B: "Sec. 704 preempts state law only where it actually conflicts with the Act, while expressly preserving state tort, contract, and product-liability law and any state or local law that protects minors more than this Act does -- the same conflict-preemption-plus-savings-clause structure is written permanently into COPPA. States remain free to legislate more protectively; only direct conflicts are barred. This is an express textual conflict-preemption clause (not an implicit-preemption-floor inference tied to axis A), so the A correction above doesn't change this score: -1.0 stands on its own textual merits."
    C: "CORRECTED 2026-09-09 per the frontier/systemic-risk-vs-near-term-consumer-harm guardrail. The four-year NIH study observes chatbots' mental-health effects on minors -- a narrow child-safety research pipeline, not a mechanism building government capacity to observe or evaluate frontier-scale or systemic AI risk. Per the guardrail this belongs near C's floor (rarely above +0.5-+1) despite textually resembling the '+1' study rung. Previously scored 1.0; corrected to 0.5."
    D: "No export-control, chip-access, or geopolitical-competition content."
    E_consumer: "Reaches a wide swath of consumer AI products -- social media, gaming, and chatbots alike -- with FTC and state-AG civil enforcement behind specific mandates like crisis-hotline referrals, non-human disclosure, and break prompts. Stronger than a bare labeling rule, though enforcement is civil rather than criminal and there's no broad right for individuals to sue."
    F: "No data-center, permitting, or energy/ratepayer content."
    R: "Covers essentially the full universe of chatbot and social/gaming platforms serving minors in the US with no revenue-floor or small-developer carve-out, though the chatbot-specific Title IV is just one part of this larger 14-bill package."
    Depth: "Driven mainly by the breadth of its consumer-protection provisions -- the mix of mandated disclosures, crisis referrals, and FTC/state-AG enforcement gives it real structural weight."
    E_f: "Enforced through the FTC's own authority plus state attorney general civil actions (with the FTC getting right of first refusal) -- agency-style enforcement backed by civil penalties, though there's no private right of action."
    P: "Consolidates roughly 14 prior bills, including a revised SAFE BOTs Act, into the first House-passed federal framework addressing AI-chatbot conduct toward minors -- likely to be a reference point for future state and federal chatbot-safety bills, though it doesn't create a permanent new institution."
    likelihood: "REVISED 2026-09-09: passed the House 267-117 under suspension of the rules with bipartisan leadership backing (Guthrie/Pallone), and p_committee (0.60, reflecting the bill's already-pending referral) is unchanged. But p_enact is revised down materially: as of this check, H.R. 7757 remains parked in Senate Commerce with no markup scheduled, and Senate sponsors -- including Sen. Markey and other KOSA backers -- have publicly called the House version 'dead' in its current form because the revised text omits KOSA's duty-of-care provision. Rather than taking up H.R. 7757 itself, Senate Commerce instead advanced its own separate kids'-safety package (KOSA, the CHATBOT Act, and the Youth AI Privacy Act) out of committee by voice vote on 2026-08-05 -- a competing vehicle carrying much of the same subject matter but built on the Senate's preferred duty-of-care framework rather than the House's text. That divergence means H.R. 7757's path to enactment now most plausibly runs through a House-Senate conference reconciling two substantially different bills rather than the Senate simply adopting the House text, which lowers its odds of enactment in its current form even though the broader subject area (kids' online/chatbot safety) has real momentum. No GovTrack prognosis update found reflecting this divergence as of this check."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags: ["child safety", "chatbots", "SAFE BOTs", "platform regulation"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/house-bill/7757"
summary: "House passed the KIDS Act 267-117, requiring platforms and AI chatbots to protect minors online; Senate review pending."
timeline:
  - date: "2026-03-03"
    event: "Introduced in the House by Rep. Brett Guthrie"
  - date: "2026-03-05"
    event: "Advanced from House Energy and Commerce subcommittee"
  - date: "2026-06-22"
    event: "Guthrie and Pallone announce bipartisan agreement on revised text"
  - date: "2026-06-29"
    event: "House passes H.R. 7757 (as amended) under suspension of the rules, 267-117"
  - date: "2026-07-13"
    event: "Received in the Senate; referred to the Senate Commerce Committee"
  - date: "2026-09-09"
    event: "Re-verified: H.R. 7757 remains parked in Senate Commerce with no markup scheduled; Senate sponsors have called the House text 'dead' over its omission of KOSA's duty-of-care provision, and Senate Commerce instead advanced its own separate KOSA/CHATBOT Act/Youth AI Privacy Act package by voice vote on 2026-08-05 as its preferred vehicle."
---
The KIDS Act bundles roughly fourteen previously separate child-online-safety bills — including a revised version of the SAFE BOTs Act — into one package requiring social media, gaming, and AI chatbot platforms to build in safeguards for minors: parental controls, limits on harmful content exposure, and age-appropriate design.

Its chatbot-specific provisions (Title IV) require AI chatbots to disclose that they are not human, bar them from claiming to be licensed professionals, mandate crisis-hotline referrals when a minor raises self-harm or suicide, and require "take a break" prompts after three continuous hours of use. The bill also directs a four-year NIH study on chatbots' mental-health effects on minors. It passed the House by a wide bipartisan margin and is now before the Senate Commerce Committee, with no distinct Senate companion bill — the same H.R. 7757 simply continues through that chamber.

**Update 2026-09-09:** H.R. 7757 has stalled in Senate Commerce with no markup scheduled. Senate sponsors have called the House text "dead" for omitting KOSA's duty-of-care provision, and the committee instead advanced its own separate kids'-safety package (KOSA, the CHATBOT Act, and the Youth AI Privacy Act) on 2026-08-05, setting up a likely conference fight over which framework prevails rather than simple Senate concurrence with the House bill.
