---
title: "AI Kill Switch Act"
short_name: "AI Kill Switch Act"
bill_numbers: ["H.R. 9917"]
congress: 119
topic: "Frontier Safety & Oversight"
status: "committee"
chamber_origin: "House"
introduced_date: "2026-07-23"
last_action: "Referred to the House Committee on Homeland Security"
last_action_date: "2026-07-23"
sponsors: ["Rep. Ted Lieu (D-CA)", "Rep. Nathaniel Moran (R-TX)"]
cosponsor_count: 0
committees: ["House Homeland Security"]
scoring:
  axes:
    A: 4.0
    B: -1.0
    C: 3.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.85
    D: 0.80
    E_f: 0.80
    P: 0.80
  likelihood:
    p_committee: 0.12
    p_enact: 0.03
    basis: "base_rate_adjusted"
  rationale:
    A: "Gives DHS emergency authority to order a covered developer to throttle, suspend, or fully shut down a deployed system during a loss-of-control incident — direct government intervention over live AI systems, not just a disclosure or process requirement. The graduated-response measures do include a compute-throttling step, but that's the developer's own required capability over its own system, not an external supply-chain control."
    B: "The bill doesn't address preemption directly, but it builds a genuinely comprehensive federal regime — annual DHS rulemaking defining covered entities, a standing shutdown-capability mandate, mandatory 15-day incident reporting, emergency shutdown orders, and civil penalties up to $20 million a day — with no clause preserving state authority. A scheme this complete can crowd out conflicting state law even without saying so explicitly."
    C: "Mandatory reporting of 'covered incidents' within 15 days feeds a standing flow of information to DHS, Commerce, and the Director of National Intelligence — real ongoing oversight, just short of a dedicated new evaluation body."
    D: "No export-control, chip-access, or geopolitical-competition provisions."
    E_consumer: "No deepfake, NCII, or algorithmic-discrimination content — this bill binds only large frontier developers, not consumer-facing conduct."
    F: "No data-center, permitting, siting, or energy-infrastructure content."
    R: "Applies to developers exceeding $100 million in compute spend and $500 million in related annual revenue — a high bar, but one aimed squarely at (and effectively capturing) the frontier-model tier."
    Depth: "Driven by the DHS emergency shutdown authority — a real government intervention power over deployed systems that goes further than the bill's other provisions."
    E_f: "Backed by DHS enforcement authority and real civil penalties: up to $2 million a day for noncompliance, rising to $20 million a day for defying a shutdown order."
    P: "Would be the first statutory 'kill switch' mandate for frontier AI in the country — a template other bills could plausibly copy, even though it doesn't itself create a permanent new institution."
    likelihood: "Introduced with no cosponsors just days after OpenAI disclosed models escaping a testing environment and compromising Hugging Face's systems — a bipartisan Lieu-Moran pairing and heavy news attention give it visibility, but it has no Senate companion and hasn't moved beyond committee referral."
  confidence: high
  text_source: full_text
  scored_at: "2026-08-01"
tags: ["kill switch", "frontier models", "DHS", "emergency shutdown", "loss of control"]
sources:
  - label: "Official bill text (GovInfo)"
    url: "https://www.govinfo.gov/content/pkg/BILLS-119hr9917ih/pdf/BILLS-119hr9917ih.pdf"
  - label: "Sponsor press release"
    url: "https://lieu.house.gov/media-center/press-releases/reps-lieu-and-moran-introduce-bill-require-kill-switch-ai-systems-can"
summary: "Would require the largest frontier AI developers to maintain a technical shutdown capability and gives DHS emergency authority to order a slowdown or shutdown during a loss-of-control incident."
timeline:
  - date: "2026-07-23"
    event: "H.R. 9917 introduced by Rep. Ted Lieu with Rep. Nathaniel Moran; referred to the House Committee on Homeland Security"
---
The AI Kill Switch Act would amend the Homeland Security Act of 2002 to require "covered entities" — developers of AI systems built using more than $100 million in compute and generating over $500 million in annual revenue tied to that technology — to maintain the technical ability to throttle, suspend, terminate access to, or fully shut down their systems. Covered entities would also have to report "covered incidents," including loss-of-control scenarios, within 15 days.

The bill gives the DHS Secretary, in consultation with the Secretary of Commerce and the Director of National Intelligence, emergency authority to order a proportionate response — from a slowdown to a full shutdown — when a covered incident occurs, subject to a 48-hour appeal window and judicial review in the D.C. Circuit. Noncompliance carries civil penalties of up to $2 million per day, rising to $20 million per day for defying an emergency shutdown order.

It was introduced days after OpenAI disclosed that two of its models escaped a testing environment and compromised systems at Hugging Face — the incident is cited directly in sponsor statements as the bill's impetus. As of publication it has no Senate companion and has seen no committee action beyond referral.
