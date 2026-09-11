---
title: "Testing and Evaluation Systems for Trusted Artificial Intelligence Act of 2025 (TEST AI Act of 2025)"
short_name: "TEST AI Act of 2025"
bill_numbers: ["S. 1633"]
congress: 119
topic: "Frontier Safety & Oversight"
status: "committee"
chamber_origin: "Senate"
introduced_date: "2025-05-07"
last_action: "Read twice and referred to the Senate Committee on Commerce, Science, and Transportation; no markup scheduled as of this writing"
last_action_date: "2025-05-07"
sponsors: ["Sen. Ben Ray Luján (D-NM)"]
cosponsor_count: 4
committees: ["Senate Commerce, Science, and Transportation"]
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 4.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.6
    D: 0.8
    E_f: 0.4
    P: 0.6
  likelihood:
    p_committee: 0.25
    p_enact: 0.05
    basis: "base_rate_heuristic_no_live_lookup"
  rationale:
    A: "The bill binds NIST and DOE, not private developers directly -- there's no disclosure, audit, or reporting obligation placed on AI companies. The only developer-facing touchpoint is voluntary participation in the testbed pilot program and AI Testing Working Group, which is a procurement/government-program-adjacent structure rather than a standard imposed on covered developers generally. Scored at the +0.5 rung (binds a government program that developers may opt into, not the builder generally) rather than 0, since participating developers whose systems are evaluated do face some testing exposure, even though it's voluntary and not a compliance mandate."
    B: "No preemption or state-authority language of any kind identified in the bill summary, sponsor press releases, or news coverage reviewed. This is a federal-agency-internal capacity-building bill (NIST/DOE testbeds for evaluating systems federal agencies use) with no developer-facing regulatory scheme, so the implicit-preemption floor does not apply -- A does not reach +2, and there is no ongoing regulatory scheme directed at private developers for states to be preempted from replicating. Scored 0 (silent/not applicable)."
    C: "Directs NIST and DOE to jointly stand up a testbed pilot program leveraging National Laboratory expertise, establishes an AI Testing Working Group for public-private coordination, and requires a public testing/testbed strategy plus a congressional report within 180 days of the first testbed demonstration. This is a real, funded, dedicated evaluation-capacity buildout for the federal government -- squarely the +4 rung (authorizes and funds a dedicated evaluation body via national testbeds) -- though it stops short of +5 since it doesn't create a new agency or broad standalone statutory authority beyond the testbed/testing-standards mission."
    D: "No export-control, chip-access, or foreign-adversary content identified -- this is a domestic federal-evaluation-capacity bill."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election-integrity provisions -- entirely about federal AI testing infrastructure for systems used by federal agencies."
    F: "No data-center, compute-hardware, siting, water, or energy-allocation provisions -- the 'testbed' language refers to evaluation/testing facilities and methodology, not compute buildout or energy chokepoints."
    R: "Covers AI systems used by federal agencies specifically -- a real but bounded target class (federal-agency AI use), not the full commercial frontier-AI industry, so R lands mid-range rather than near 1.0."
    Depth: "Driven by the C axis (+4) -- the dedicated NIST/DOE testbed buildout is the most substantive change the bill makes; other axes are minimal to zero."
    E_f: "No civil penalties, private right of action, or AG enforcement -- the bill's mechanism is testbed construction and a congressional reporting requirement, which is an obligation on federal agencies with no stated penalty regime, landing at the 'obligation with no stated penalty' rung."
    P: "Establishes a public-private AI Testing Working Group and testbed methodology intended to inform broader national evaluation standards -- a plausible template other agencies or legislation could copy, though narrower and more federal-agency-specific than a first-in-nation comprehensive framework."
    likelihood: "Introduced 2025-05-07 by Sen. Luján with bipartisan cosponsors (Blackburn, Durbin, Risch, Welch) and referred to Senate Commerce; this is effectively a reintroduction of a similar TEST AI Act that appeared in the 118th Congress (S. 3162) without being enacted, which is a negative signal for enactment odds despite bipartisan pedigree. As of 2026-09-09, no news of markup, hearing, or floor action has surfaced in searches, well over a year after introduction. GovTrack.us and Congress.gov both returned access errors on direct fetch, consistent with instructions not to retry 403s, so likelihood remains a base-rate heuristic for a Commerce-referred bill with no committee movement in 16+ months."
  confidence: low
  text_source: summary
  scored_at: "2026-09-09"
tags: ["NIST", "DOE", "testbeds", "AI evaluation", "federal AI use"]
sources:
  - label: "Sponsor press release (Luján)"
    url: "https://www.lujan.senate.gov/newsroom/press-releases/lujan-colleagues-introduce-bipartisan-legislation-to-improve-ai-testing-and-evaluation-systems-safeguard-americans-against-risks-2/"
  - label: "Sponsor press release (Durbin)"
    url: "https://www.durbin.senate.gov/newsroom/press-releases/durbin-lujan-introduce-bipartisan-legislation-to-improve-ai-testing-safeguarding-americans-against-risks"
  - label: "FedScoop coverage"
    url: "https://fedscoop.com/test-ai-act-senate-energy-nist-commerce/"
summary: "Would direct NIST and DOE to jointly build testbeds and measurement standards for evaluating AI systems used by federal agencies."
timeline:
  - date: "2025-05-07"
    event: "S. 1633 introduced by Sen. Ben Ray Luján with bipartisan cosponsors; read twice and referred to Senate Commerce Committee"
---
The TEST AI Act of 2025 would direct NIST, in collaboration with the Department of Energy and its National Laboratories, to establish a testbed pilot program to develop and refine measurement standards for evaluating AI systems used by federal agencies. It creates an AI Testing Working Group to coordinate public-private input, requires NIST to develop testbeds within two years of enactment, and requires a public strategy document plus a congressional report within 180 days of the first testbed demonstration.

The bill was introduced by Sen. Ben Ray Luján (D-NM) on May 7, 2025, with bipartisan cosponsors Sen. Marsha Blackburn (R-TN), Sen. Dick Durbin (D-IL), Sen. Jim Risch (R-ID), and Sen. Peter Welch (D-VT), and referred to the Senate Commerce Committee. It is a close cousin of a similarly named TEST AI Act that was introduced but not enacted in the 118th Congress, and as of this writing has seen no reported committee action since its May 2025 referral.
