---
title: "People-First Chatbot Act"
short_name: "People-First Chatbot Act"
bill_numbers: ["H.R. 9619"]
congress: 119
topic: "Children & Chatbots"
status: "committee"
chamber_origin: "House"
introduced_date: "2026-07-09"
last_action: "Referred to the House Committee on Energy and Commerce"
last_action_date: "2026-07-09"
sponsors: ["Rep. Valerie Foushee (D-NC)", "Rep. Greg Casar (D-TX)"]
cosponsor_count: null
committees: ["House Energy and Commerce"]
scoring:
  axes:
    A: 0.0
    B: 1.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 4.0
  impact_components:
    R: 0.60
    D: 0.80
    E_f: 1.00
    P: 0.80
  likelihood:
    p_committee: 0.15
    p_enact: 0.02
    basis: "base_rate_heuristic_no_live_lookup"
  rationale:
    A: "Regulates chatbot operators' data, advertising, and safety-design practices toward consumers — it places no obligation on developers of frontier AI systems as such."
    B: "Section 7 is an explicit savings clause: nothing in the Act preempts state laws, rules, or regulations that are at least as protective of users as this bill. Section 6 separately preserves existing tort, civil-rights, and consumer-protection claims."
    C: "The periodic 'safety assessments' it requires are an obligation on chatbot operators, not a new government reporting or oversight capacity — no agency gains new tools here."
    D: "No export-control or geopolitical content."
    E_consumer: "Bans targeted advertising built on chatbot conversations for all users, not just minors; restricts using minors' chat data to train models without affirmative adult consent; and mandates safety-by-design protections plus periodic safety assessments — a broad, structural mandate touching the business model of any chatbot provider, backed by a private right of action."
    F: "No data-center or energy-buildout content."
    R: "Applies federally, and unlike sibling bills scoped to minors only, its ad-targeting ban covers all chatbot users, giving it broader reach within the consumer chatbot-safety space."
    Depth: "Driven almost entirely by the consumer-protection mandate — the ad-targeting ban, training-data consent rule, and safety-by-design requirements are where this bill's weight sits."
    E_f: "Creates a direct private right of action, with statutory damages up to $10,000 per violation (and floors of $50,000-$250,000 for safety-by-design violations specifically), fee-shifting, and a separate no-fault injury-liability claim against providers — about as strong an enforcement mechanism as this tracker sees."
    P: "Pairs a first-of-its-kind ban on ad-targeting from chatbot conversations with a training-data consent requirement — a framework later chatbot bills would likely borrow from."
    likelihood: "Introduced by two Democratic sponsors with no Republican cosponsors so far and no committee action yet, just weeks after introduction — unlike the bipartisan GUARD and CHATBOT Acts, this one currently lacks cross-party backing, which keeps its near-term prospects weak."
  confidence: high
  text_source: full_text
  scored_at: "2026-08-01"
tags: ["chatbots", "child safety", "data privacy", "advertising"]
sources:
  - label: "Sponsor press release"
    url: "https://foushee.house.gov/media/press-releases/reps-foushee-casar-introduce-legislation-to-protect-children-and-americans-privacy-from-ai-chatbot-harms-and-require-chatbot-safety-assessments"
summary: "Would require safety-by-design protections in AI chatbots, ban targeted ads to users, and restrict using minors' chat data for AI training."
timeline:
  - date: "2026-07-09"
    event: "Introduced by Rep. Foushee with Rep. Casar; referred to House Energy and Commerce Committee"
---
The People-First Chatbot Act would require AI chatbot providers to build in safety-by-design protections against harms like suicide, compulsive use, and emotional dependence; ban using chatbot conversations for targeted advertising to any user, not just minors; restrict using minors' chat data to train AI models (adults would need to affirmatively consent); and require periodic chatbot safety assessments.

Rep. Foushee is also a cosponsor of the House companion to the GUARD Act, and this bill is explicitly framed by its sponsors as complementary to that effort — where GUARD Act focuses on age verification and banning companion chatbots for minors, this bill focuses more on data practices and advertising across the whole user base.
