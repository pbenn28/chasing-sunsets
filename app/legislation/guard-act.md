---
title: "Guidelines for User Age-verification and Responsible Dialogue Act (GUARD Act)"
short_name: "GUARD Act"
bill_numbers: ["S. 3062", "H.R. 8623"]
congress: 119
topic: "Children & Chatbots"
status: "committee_passed"
chamber_origin: "Senate"
introduced_date: "2025-10-28"
last_action: "Senate Judiciary Committee unanimously advanced S. 3062; awaiting a full Senate floor vote"
last_action_date: "2026-04-30"
sponsors: ["Sen. Josh Hawley (R-MO)", "Sen. Richard Blumenthal (D-CT)"]
cosponsor_count: 17
committees: ["Senate Judiciary", "House Judiciary", "House Energy and Commerce"]
scoring:
  axes:
    A: 0.0
    B: 3.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 3.0
  impact_components:
    R: 0.95
    D: 0.60
    E_f: 0.80
    P: 0.80
  likelihood:
    p_committee: 0.97
    p_enact: 0.46
    basis: "govtrack_corroborated"
  rationale:
    A: "Places no obligation on frontier or advanced AI developers as such — its duties (age verification, a companion-bot access ban, disclosure) bind any company deploying a consumer chatbot product, and the disclosure duty is a consumer-facing UX requirement rather than a developer-transparency measure like model cards or training-data provenance."
    B: "Includes an unusually strong savings clause: states remain free to enforce any state law or regulation that is at least as protective of chatbot users as this Act, and nothing else in the bill touches state authority. That's an affirmative guarantee that states can go further, not just boilerplate acknowledging their existing power."
    C: "Enforcement runs through civil and criminal penalties on companies rather than through any new federal agency, evaluation body, or incident-reporting pipeline."
    D: "No export-control, chip-access, or geopolitical-competition content."
    E_consumer: "Creates criminal penalties for companies that knowingly make chatbots available that produce sexualized content involving minors or that solicit or induce suicide, self-harm, or violence, plus civil penalties and an outright ban on minors accessing 'AI companion' chatbots, backed by mandatory age verification."
    F: "No data-center, permitting, interconnection, or energy content."
    R: "Covers any company operating an AI chatbot, with no revenue floor or size carve-out — reaching essentially the entire consumer chatbot industry, including the companion-bot category it specifically targets."
    Depth: "Driven almost entirely by its consumer-protection provisions (the companion-bot ban and new criminal liability) rather than by any developer, preemption, or governance-capacity changes."
    E_f: "Backed by civil and criminal penalties for prohibited conduct rather than a private right of action."
    P: "No prior federal law bans minors from AI companion chatbots or mandates chatbot age verification — this would be the first federal framework of its kind, and it's already the lead bill referenced by several other 2026 chatbot-safety proposals."
    likelihood: "Cleared the Senate Judiciary Committee unanimously in April 2026 and is awaiting a full Senate floor vote, with a genuinely bipartisan Hawley-Blumenthal pairing and a cosponsor list that has kept growing since introduction — real momentum, though a floor vote and House action are still needed."
  confidence: high
  text_source: full_text
  scored_at: "2026-08-01"
tags: ["chatbots", "child safety", "age verification", "companion AI"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/senate-bill/3062"
  - label: "Sponsor press release"
    url: "https://www.hawley.senate.gov/senator-hawleys-guard-act-to-protect-kids-from-ai-chatbots-passes-committee-unanimously/"
summary: "Bipartisan Senate bill requiring AI chatbot age verification and banning AI 'companion' chatbots for minors; cleared committee, awaiting a floor vote."
timeline:
  - date: "2025-10-28"
    event: "S. 3062 introduced in the Senate by Sen. Hawley with Sen. Blumenthal and others"
  - date: "2026-04-30"
    event: "Senate Judiciary Committee unanimously advances S. 3062"
  - date: "2026-04-30"
    event: "House companion H.R. 8623 introduced by Rep. Blake Moore and Rep. Valerie Foushee"
---
The GUARD Act would require companies operating AI chatbots to implement real age verification — not just a self-reported birthdate — and, for users identified as minors, prohibit access to "AI companions": chatbots designed to simulate interpersonal, romantic, or emotional relationships. It would also require all chatbots to disclose their non-human, non-professional status at the start of a conversation and periodically afterward, and creates civil and criminal penalties for companies that knowingly make chatbots available that produce sexual content involving minors or that solicit, induce, or coerce suicide, self-harm, or violence.

It's the lead bill in a cluster of 2026 chatbot-safety proposals that also includes the People-First Chatbot Act, the Youth AI Privacy Act, the CHATBOT Act, and the Conversational AI Services Act — all tracked separately on this page — plus overlaps in spirit with the SAFE BOTs Title of the already-passed KIDS Act. Unlike KIDS Act's disclosure-and-break-prompt approach, GUARD Act's core mechanism is an access ban for minors, backed by age verification.

**A note on naming:** several unrelated bills in the 119th Congress also use the short title "GUARD Act" for entirely different subjects (immigration enforcement, elder-fraud, robotics national security). This entry refers specifically to S. 3062 / H.R. 8623, the AI chatbot bill.
