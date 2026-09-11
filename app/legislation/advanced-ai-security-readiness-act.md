---
title: Advanced AI Security Readiness Act
short_name: Advanced AI Security Readiness Act
bill_numbers:
- H.R. 3919
- S. 3202
congress: 119
topic: Chips & National Security
status: committee
chamber_origin: House
introduced_date: '2025-06-11'
last_action: Referred to the House Permanent Select Committee on Intelligence
last_action_date: '2025-06-11'
sponsors:
- Rep. Darin LaHood (R-IL)
cosponsor_count: 4
committees:
- House Permanent Select Committee on Intelligence
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 1.0
    D: 0.20
    E_f: 0.4
    P: 0.4
  likelihood:
    p_committee: 0.10
    p_enact: 0.03
    basis: "base_rate_adjusted"
  rationale:
    A: "Places no obligation on AI developers. It directs the NSA's AI Security Center to write an internal 'AI Security Playbook,' consult developers for input, and report to Congress — and the bill itself says that consultation doesn't create any regulatory or enforcement authority."
    B: "Doesn't touch state AI regulation at all. It's an internal executive-branch playbook-and-reporting exercise, not a federal regulatory scheme, so there's nothing here to preempt or preserve."
    C: "Tasks the NSA's AI Security Center with delivering progress and final reports to Congress on a fixed schedule (90 and 270 days after enactment) — a real but modest reporting obligation, not a standing evaluation body or incident database."
    D: "Aimed at counterintelligence — protecting model weights and data centers from theft — rather than export controls or chip access."
    E_consumer: "No consumer-facing or near-term-harm content."
    F: "Mentions AI data centers only as a place where theft risk gets assessed, not as a compute, energy, or siting provision."
    R: "A federal measure with no carve-outs, applying uniformly wherever it applies."
    Depth: "A narrow, low-stakes measure — its only real content is the reporting deadline, with no obligations on industry."
    E_f: "The only obligation runs to the NSA itself — produce a playbook, report to Congress — with no penalty attached for missing it."
    P: "A one-off interagency playbook and reporting requirement, self-contained rather than the seed of a lasting institution."
    likelihood: "Re-verified 2026-09-09: still sitting in House Permanent Select Committee on Intelligence and Senate Select Committee on Intelligence with no markup scheduled, over a year (H.R. 3919) and ~10 months (S. 3202) after referral. GovTrack does not publish a prognosis for either bill. Checked whether provisions were folded into the FY2027 NDAA (House passed H.R. 8800 7/22/2026 216-212; Senate cloture on S. 4784 failed 7/14/2026 50-46, and per CRS's Sept. 1 status report the Senate has taken no further procedural steps since — no conference exists to fold anything into yet) — found no evidence this bill's playbook-and-reporting language was incorporated into either chamber's NDAA text. Slightly lowered p_committee (0.12→0.10) to reflect base-rate decay as the bill ages further past its referral with no chamber action and no vehicle currently available to carry it."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- national security
- model theft
- NSA
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/3919
- label: Congress.gov (Senate companion)
  url: https://www.congress.gov/bill/119th-congress/senate-bill/3202
- label: CRS, FY2027 NDAA Status of Legislative Activity (Sept. 1, 2026)
  url: https://www.congress.gov/crs-product/IN12704
summary: Directs the NSA to build an “AI Security Playbook” to protect advanced AI from theft.
timeline:
- date: '2025-06-11'
  event: Introduced in the House
- date: '2025-06-11'
  event: Referred to the House Permanent Select Committee on Intelligence
- date: '2025-11-19'
  event: Senate companion S. 3202 introduced by Sen. Todd Young, read twice, and referred to the Senate Select Committee on Intelligence
- date: '2026-09-09'
  event: Re-verified — no committee markup on H.R. 3919 or S. 3202; not incorporated into FY2027 NDAA (House-passed H.R. 8800 or stalled Senate S. 4784)
---

The bill directs the NSA Director, acting through the AI Security Center, to develop an “AI Security Playbook” of strategies to defend advanced AI technologies — including model weights and core design insights — from theft by threat actors. It requires progress and final reports to Congress with classified and unclassified components, and grants no new regulatory or enforcement authority.
