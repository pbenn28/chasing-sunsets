---
title: Eliminating Bias in Algorithmic Systems Act of 2026
short_name: Eliminating Bias in Algorithmic Systems Act
bill_numbers:
- H.R. 7110
- S. 3680
congress: 119
topic: Civil Rights & Labor
status: committee
chamber_origin: Both
introduced_date: '2026-01-15'
last_action: House and Senate versions each referred to committee; no further action
last_action_date: '2026-01-15'
sponsors:
- Rep. Summer Lee (D-PA)
- Sen. Ed Markey (D-MA)
cosponsor_count: 22
committees:
- House Oversight and Government Reform
- Senate Homeland Security and Governmental Affairs
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
    R: 0.85
    D: 0.20
    E_f: 0.20
    P: 0.60
  likelihood:
    p_committee: 0.03
    p_enact: 0.01
    basis: "base_rate_adjusted"
  rationale:
    A: "Every obligation in the bill runs to federal agencies (establishing civil-rights offices, reporting) — no source found any provision binding private AI developers directly, so this axis isn't engaged even though the bill's subject is algorithmic bias."
    B: "No preemption or savings-clause language of any kind was found — the bill is entirely agency-facing and doesn't touch state authority to regulate private AI developers. The implicit-preemption floor doesn't apply: A is 0, well short of the +2 threshold that would trigger it."
    C: "Corrected under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail, which the rubric explicitly extends to axis C: the governance capacity this bill builds — agency-internal Offices of Civil Rights, a DOJ interagency working group, biennial reports to Congress — is entirely scoped to bias/discrimination in agencies' own use of 'covered algorithms,' the rubric's own canonical example of a narrow harm domain that belongs on E, not to systemic AI oversight capacity or frontier-risk evaluation. That the mandate applies government-wide across every federal agency doesn't rescue it — breadth-across-agencies is not the same as building capacity to observe/evaluate/enforce AI risk generally, and there is no channel here touching frontier developers or deployment-scale risk at all. Previously scored 2.0 by matching the offices-plus-reporting mechanism to C's literal rung-2/3 wording; corrected down near C's floor to 1.0 to reflect real but narrowly-scoped institutional capacity."
    D: "No export-control or geopolitical content."
    E_consumer: "All obligations run to federal agencies overseeing their own algorithm use, not to distributors, deployers, or developers dealing with consumers, so this bill has no near-term consumer-harm content of the kind this axis measures."
    F: "No data-center, compute, siting, or energy content."
    R: "Federal in scope and applies government-wide to every agency using, funding, or overseeing covered algorithms, with no revenue threshold or sector carve-out narrowing coverage — reaches nearly the entire intended target class."
    Depth: "Recomputed after the frontier/systemic-risk guardrail correction — now driven by axis C (governance capacity) at 1.0/5."
    E_f: "Reporting to Congress with a deadline, but no civil penalty, private right of action, or agency-enforcement mechanism against anyone who fails to comply."
    P: "Establishes a template (agency-embedded civil-rights offices for algorithmic oversight) that is a reintroduction of a 118th Congress bill (S. 3478) and could be copied across agencies or years, but it is not yet a permanent institution with enforcement teeth or a preemption ceiling of its own."
    likelihood: "Introduced 2026-01-15 with 16 House cosponsors (all Democratic) and 6 Senate cosponsors (all Democratic) — a purely single-party sponsorship pattern with no bipartisan pairing found. No hearing, markup, or floor action identified for either chamber as of September 2026. This is a reintroduction of a substantively similar 118th Congress bill (S. 3478) that also died in committee, which anchors the base rate lower rather than higher. No GovTrack prognosis figure could be retrieved (403 on direct fetch); p_enact held near the low end typical for single-party message bills reintroduced without new momentum."
  confidence: low
  text_source: summary
  scored_at: "2026-09-09"
tags:
- civil rights
- algorithmic bias
- federal agencies
- oversight
sources:
- label: Congress.gov (House)
  url: https://www.congress.gov/bill/119th-congress/house-bill/7110
- label: Congress.gov (Senate)
  url: https://www.congress.gov/bill/119th-congress/senate-bill/3680
- label: Rep. Summer Lee press release
  url: https://summerlee.house.gov/newsroom/press-releases/rep-summer-lee-sen-markey-reintroduce-legislation-to-mandate-civil-rights-offices-in-federal-agencies-that-manage-artificial-intelligence
- label: Sen. Markey press release
  url: https://www.markey.senate.gov/news/press-releases/sen-markey-rep-lee-reintroduce-legislation-to-mandate-civil-rights-offices-in-federal-agencies-that-manage-artificial-intelligence
summary: Requires federal agencies that use or oversee AI systems to establish civil-rights offices addressing algorithmic bias and discrimination.
timeline:
- date: '2026-01-15'
  event: H.R. 7110 and S. 3680 introduced and referred to House Oversight and Government Reform / Senate Homeland Security and Governmental Affairs
---

The bill requires every federal agency that uses, funds, or oversees "covered algorithms" to establish a dedicated Office of Civil Rights, staffed with technologists and civil-rights experts, to address bias and discrimination tied to protected characteristics in agency AI use. It also directs the DOJ's Assistant Attorney General for Civil Rights to stand up an interagency working group on covered algorithms and civil rights within a year of enactment, with recurring reports to Congress every two years thereafter covering risks, mitigation, stakeholder engagement, and legislative recommendations. Rep. Summer Lee (D-PA) and Sen. Ed Markey (D-MA) lead a reintroduction of a bill that first appeared in the 118th Congress (S. 3478); it is endorsed by a coalition of civil-rights and tech-policy groups including EPIC, the Leadership Conference on Civil and Human Rights, and CDT, but has drawn no bipartisan cosponsors and no committee action in either chamber since its January 2026 introduction.
