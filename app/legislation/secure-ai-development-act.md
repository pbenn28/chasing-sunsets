---
title: "Secure Artificial Intelligence Development Act of 2026"
short_name: "Secure AI Development Act"
bill_numbers: ["S. 5061"]
congress: 119
topic: "Frontier Safety & Oversight"
status: "committee"
chamber_origin: "Senate"
introduced_date: "2026-07-21"
last_action: "Read twice and referred to the Senate Committee on Commerce, Science, and Transportation"
last_action_date: "2026-07-21"
sponsors: ["Sen. Mark Warner (D-VA)"]
cosponsor_count: 0
committees: ["Senate Commerce, Science, and Transportation"]
scoring:
  axes:
    A: 2.0
    B: -1.0
    C: 4.0
    D: 2.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.8
    D: 0.8
    E_f: 0.6
    P: 0.8
  likelihood:
    p_committee: 0.15
    p_enact: 0.02
    basis: "base_rate_heuristic_no_live_lookup"
  rationale:
    A: "Requires frontier AI providers to give the NSA's Artificial Intelligence Security Center access to their models, including weights, 21 days before public release, backed by real teeth: AG referral and a $100,000/day penalty with a 7-day cure period (Sec. 3(e)). NSA doesn't get approval/denial power over release, so this is mandated evaluation access rather than a full licensing gate. A separate, narrow liability shield (Sec. 7(l)) only covers entities sharing threat intelligence under a pilot program -- it isn't a general developer liability shield."
    B: "No provision addresses state AI authority directly, and Sec. 7(j)'s rule of construction is narrow (it concerns intelligence collection and classified information, not state law). Because the bill builds real federal regulatory machinery -- mandatory pre-release NSA access, a frontier-model registry with civil penalties, and a standing AI Risk Board -- without an express savings clause protecting state authority, it leaves the door open to displacing state rules in this space even though it doesn't do so explicitly."
    C: "Establishes a standing Artificial Intelligence Risk Board inside NIST to set risk-evaluation standards, plus a frontier-model registry -- a real, funded evaluation body. Its incident-tracking database is voluntary, so it stops short of a full new-agency-with-major-authority setup."
    D: "Sets up government-industry threat-intelligence sharing focused on foreign-adversary risks to the AI supply chain and updates federal vulnerability-management processes -- standing coordination infrastructure rather than a one-off assessment, though still short of hard export controls."
    E_consumer: "Entirely a frontier-developer and national-security bill -- no deepfake, NCII, companion-bot, discrimination, or election-integrity content."
    F: "No data-center, permitting, siting, water, or energy-allocation provisions; the NSA research test-bed in Sec. 3(f) is a testing facility, not a compute or energy chokepoint."
    R: "Targets 'the most advanced frontier AI models' specifically -- a real but narrower slice of the AI industry than an economy-wide threshold would cover."
    Depth: "Driven mainly by the new NIST Risk Board and registry -- real governance capacity, even though other axes are more modest."
    E_f: "NSA pre-release access and a standards-setting Risk Board point toward real agency-level enforcement, but the incident-tracking piece is voluntary and no civil-penalty regime backs it directly."
    P: "Stands up a new standing institution -- the AI Risk Board inside NIST -- the kind of durable framework other legislation is likely to build on or copy."
    likelihood: "Introduced solo by Sen. Warner with no cosponsors, as one piece of a larger six-bill package, in a Republican-controlled Congress -- it's the most fully fleshed-out bill in that package, but that alone doesn't give it much of a path forward. As of 2026-09-09, no hearing, markup, or new cosponsor has been reported in Senate Commerce since introduction; GovTrack.us was unreachable (403) for a fresh prognosis check, so likelihood remains a base-rate heuristic. Estimates held flat given no material change in status."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags: ["frontier models", "national security", "pre-release testing", "NIST"]
sources:
  - label: "Official bill text (GovInfo)"
    url: "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s5061is.xml"
  - label: "Sponsor press release"
    url: "https://www.warner.senate.gov/newsroom/press-releases/warner-rolls-out-comprehensive-ai-legislative-agenda-focused-on-responsible-innovation-workers-and-national-security/"
summary: "Would require the most advanced AI models to undergo NSA pre-release review and create a federal AI risk board within NIST."
timeline:
  - date: "2026-07-21"
    event: "Sen. Warner unveils a six-bill AI legislative package, \"A Framework for America's AI Future\""
  - date: "2026-07-21"
    event: "S. 5061 introduced, read twice, and referred to Senate Commerce Committee"
---
The Secure AI Development Act would require developers of the most advanced "frontier" AI models to give the National Security Agency access to their models 21 days before public release, and would establish an Artificial Intelligence Risk Board inside NIST to set risk-evaluation standards. It also creates a frontier-model registry, a voluntary safety-incident tracking database, updates federal cybersecurity vulnerability-management processes for AI-specific risks, and sets up government-industry threat-intelligence sharing focused on foreign-adversary risks to the AI supply chain.

It's one piece of a broader six-bill package Sen. Mark Warner rolled out the same day; some sibling bills in that package are still discussion drafts rather than introduced legislation, so this is the most concrete of the set — but it's also the only piece that has actually cleared the bar of formal introduction so far.
