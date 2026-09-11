---
title: Federal Artificial Intelligence Risk Management Act of 2026
short_name: Federal AI Risk Management Act
bill_numbers:
- H.R. 8819
congress: 119
topic: Government Use & Procurement
status: introduced
chamber_origin: House
introduced_date: '2026-05-14'
last_action: Referred to the House Committee on Science, Space, and Technology
last_action_date: '2026-05-14'
sponsors:
- Rep. Ted Lieu (D-CA)
- Rep. Zach Nunn (R-IA)
- Rep. Don Beyer (D-VA)
- Rep. Marc Molinaro (R-NY)
cosponsor_count: 4
committees:
- House Science, Space, and Technology
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 0.5
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.85
    D: 0.10
    E_f: 0.40
    P: 0.40
  likelihood:
    p_committee: 0.30
    p_enact: 0.08
    basis: "base_rate_adjusted"
  rationale:
    A: "Requires federal agencies, and contractors/organizations operating AI systems on an agency's behalf (national security systems excluded), to use NIST's AI Risk Management Framework in developing, procuring, and using AI systems. This binds the government buyer and its vendors when selling to government, not AI developers generally — a textbook procurement/government-use condition, so it lands at +0.5 rather than higher on the ladder."
    B: "No preemption or savings-clause language anywhere in the bill — it only directs NIST and federal agencies on their own procurement and use practices, and doesn't establish a regulatory scheme reaching outside government. Because A stays below +2, the implicit-preemption floor doesn't apply, so 0.0 (silent) stands."
    C: "Directs NIST to develop standards, guidelines, and tools helping agencies apply the AI RMF to reduce risk in agency AI development, procurement, and use. This is a concrete implementation mandate rather than a mere study, but it doesn't create a dedicated evaluation body, a standing incident-reporting stream, or new enforcement staffing, so it sits at the low end of the 'studies/advisory' rung rather than climbing higher."
    D: "No export-control, chip-access, or geopolitical-competition content anywhere in the bill."
    E_consumer: "No deepfake, NCII, companion-bot, algorithmic-discrimination, or election-integrity content — this is purely a federal procurement and internal-use bill."
    F: "No data-center, permitting, interconnection, siting, or energy content."
    R: "Covers all federal agencies and any contractor or organization operating an AI system on an agency's behalf (short of national-security systems), which is close to the full target class for a government-use bill of this kind."
    Depth: "Modest — a procurement-conditions bill with no penalty regime or new institution behind it; driven by axis A's below-average score."
    E_f: "No stated penalty for an agency or contractor that doesn't follow the framework — this reads as an implementation directive rather than an enforceable mandate with consequences."
    P: "A sector-specific, self-contained procurement mandate tied to an existing NIST framework — not a first-in-nation model or a new permanent institution, but more durable than a one-off study."
    likelihood: "Introduced 2026-05-14 with four bipartisan cosponsors (2 D, 2 R) and referred to House Science. A cosponsor (Rep. Gottheimer) joined 2026-05-29, but as of 2026-09-09 no committee markup or further action has been scheduled. Predecessor versions of this same concept (Federal AI Risk Management Act) were introduced in the 118th Congress (H.R. 6936, S. 3205) and did not advance to enactment, which tempers the outlook; GovTrack does not yet publish a modeled prognosis for this specific bill number, so this estimate uses the historical base rate for bipartisan, narrow-scope government-operations bills referred to House Science, adjusted slightly upward for the bipartisan sponsor mix and prior-Congress momentum on the underlying concept."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- procurement
- NIST
- risk management
- federal agencies
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/8819
- label: Rep. Don Beyer press release
  url: https://beyer.house.gov/news/documentsingle.aspx?DocumentID=6066
summary: Requires federal agencies and their contractors to use NIST's AI Risk Management Framework when developing, procuring, and using AI systems.
timeline:
- date: '2026-05-14'
  event: Introduced and referred to House Science, Space, and Technology
- date: '2026-05-29'
  event: Rep. Josh Gottheimer joins as cosponsor
---

The bill would require federal agencies, and contractors or organizations operating AI systems on an agency's behalf, to apply NIST's Artificial Intelligence Risk Management Framework when developing, procuring, and using AI systems — with national security systems excluded. NIST would be directed to publish standards, guidelines, and tools to help agencies implement the framework. It is a bipartisan revival of a Federal AI Risk Management Act concept first introduced in the 118th Congress.
