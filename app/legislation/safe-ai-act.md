---
title: "Safeguarding Against Fabricated Exploitation Through Artificial Intelligence Act of 2026"
short_name: "SAFE AI Act"
bill_numbers: ["S. 5057"]
congress: 119
topic: "Frontier Safety & Oversight"
status: "committee"
chamber_origin: "Senate"
introduced_date: "2026-07-21"
last_action: "Read twice and referred to the Senate Committee on Homeland Security and Governmental Affairs"
last_action_date: "2026-07-21"
sponsors: ["Sen. Mark Warner (D-VA)"]
cosponsor_count: 1
committees: ["Senate Homeland Security and Governmental Affairs"]
scoring:
  axes:
    A: 0.5
    B: -1.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 3.0
  impact_components:
    R: 0.4
    D: 0.6
    E_f: 0.6
    P: 0.4
  likelihood:
    p_committee: 0.15
    p_enact: 0.02
    basis: "base_rate_heuristic_no_live_lookup"
  rationale:
    A: "The bill's core mechanism is a federal-procurement/federal-use ban on AI models found to generate CSAM or NCII, plus a NIST-run voluntary vendor testing/benchmark program. Procurement conditions bind the government-as-buyer rather than developers generally -- the textbook procurement rung -- but the NIST testing program is itself a real, if voluntary, AI-specific evaluation process that vendors must pass to sell into government, so this sits at the boundary between the procurement rung and a mandated-process rung; scored just above the pure procurement floor to reflect the added NIST testing layer, without reaching a mandatory pre-deployment gate since the ban is narrowly scoped to CSAM/NCII-generating capability rather than general frontier-model conduct."
    B: "No express savings clause was confirmed in the ~7 pages of text reviewed, and no broad preemption language was found either. Because this bill's substantive mandate (procurement ban plus NIST testing) is narrowly scoped to CSAM/NCII generation rather than a general frontier AI regulatory scheme, the implicit-preemption floor for A ≥ +2 bills does not apply here (A is scored well below +2). Scored −1 to reflect that a federal procurement standard of this kind ordinarily operates alongside, not against, state law in this narrow domain, with no confirmed express protection either way -- treated as conflict-preemption-equivalent rather than 0/silent given the absence of any savings clause in the text reviewed."
    C: "Creates a NIST-led performance-benchmark and voluntary testing program for vendors -- a real evaluation mechanism, but voluntary rather than mandatory, and not backed by a standing database or new enforcement authority. This is a study/advisory-committee-equivalent capacity addition, not a funded evaluation body with compliance teeth."
    D: "No export-control or foreign-adversary provisions; the bill is entirely domestic in scope (federal procurement and government use)."
    E_consumer: "Directly targets CSAM and non-consensual intimate imagery (NCII) generation -- core consumer/near-term-harm territory. Enforcement is tied to federal court determinations that a model generated such content, which functions like a specific-conduct liability mechanism (survivors can seek a judicial determination triggering the procurement ban) rather than a broad cross-sector private right of action, so this lands at the criminal/specific-conduct-liability rung rather than the top rung."
    F: "No data-center, compute, siting, or energy provisions."
    R: "The ban applies only to the federal government's own procurement and use of AI models -- a narrow slice of the overall AI market, even though it's a meaningful lever given the government's purchasing power."
    Depth: "Driven by the CSAM/NCII procurement ban and NIST testing program -- a real but narrowly scoped mechanism rather than an economy-wide change."
    E_f: "NIST testing plus a federal-court-determination trigger for the procurement ban functions like agency rulemaking backed by a concrete enforcement pathway, though it is not a broad civil-penalty regime or private right of action reaching the general public."
    P: "A sector-specific, self-contained procurement rule targeting one harm category (CSAM/NCII) rather than a template likely to be copied wholesale into broader AI governance."
    likelihood: "Introduced by Sen. Warner as one piece of his six-bill package; picked up its only cosponsor, Sen. Jon Husted (R-OH), on 2026-08-07, giving it the only bipartisan cosponsor pairing across the six-bill Warner package found in this research pass. Referred to Senate Homeland Security and Governmental Affairs (a different committee than most of its sibling bills) with no hearing or markup reported as of early September 2026. GovTrack.us and congress.gov were unreachable (403) for a fresh prognosis check; likelihood held at the same base-rate heuristic as sibling bills, nudged by the bipartisan cosponsor but still very early-stage."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags: ["CSAM", "NCII", "federal procurement", "NIST", "survivors", "child safety"]
sources:
  - label: "Official bill text (Sponsor PDF)"
    url: "https://www.warner.senate.gov/wp-content/uploads/2026/07/SAFE-AI-Act.pdf"
  - label: "GovInfo BILLSTATUS"
    url: "https://www.govinfo.gov/bulkdata/BILLSTATUS/119/s/BILLSTATUS-119s5057.xml"
  - label: "Sponsor press release"
    url: "https://www.warner.senate.gov/newsroom/press-releases/warner-rolls-out-comprehensive-ai-legislative-agenda-focused-on-responsible-innovation-workers-and-national-security/"
summary: "Warner/Husted bill establishing NIST-led AI model testing and banning federal procurement or use of AI models found to generate CSAM or non-consensual intimate imagery."
timeline:
  - date: "2026-07-21"
    event: "S. 5057 introduced as part of Warner's six-bill AI package; read twice and referred to Senate Homeland Security and Governmental Affairs"
  - date: "2026-08-07"
    event: "Sen. Jon Husted (R-OH) joins as cosponsor"
---
The SAFE AI Act — the "Safeguarding Against Fabricated Exploitation Through Artificial Intelligence Act of 2026" — would prohibit federal agencies from procuring or using AI models that a federal court has determined are capable of generating child sexual abuse material (CSAM) or non-consensual intimate imagery (NCII). It directs NIST to run a performance-benchmark and voluntary vendor testing program so agencies have a standardized way to evaluate models before purchase, and creates an enforcement pathway tied to judicial findings that a given model generated such content.

Note on naming: an earlier draft description of a bill sharing this number described a much broader proposal to "prohibit use of certain AI models across the federal government." Direct review of the bill's own text (via the sponsor's PDF and the official GovInfo BILLSTATUS record) confirms the narrower CSAM/NCII-procurement-ban framing is the accurate one — the "certain AI models" language refers specifically to models found capable of generating CSAM/NCII, not a general-purpose federal AI ban. There is no separate, competing bill; the two descriptions refer to the same text.

It is one piece of Sen. Mark Warner's six-bill "A Framework for America's AI Future" package, introduced the same day as the AI AGENT Act (S. 5051) and the Secure AI Development Act (S. 5061), and is so far the only bill in that package to pick up a cosponsor.
