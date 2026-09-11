---
title: MedShield Act of 2025
short_name: MedShield Act
bill_numbers:
- S. 1085
congress: 119
topic: Healthcare
status: committee
chamber_origin: Senate
introduced_date: '2025-03-14'
last_action: Referred to the Senate Committee on Health, Education, Labor, and Pensions
last_action_date: '2025-03-14'
sponsors:
- Sen. Mike Rounds (R-SD)
- Sen. Martin Heinrich (D-NM)
committees:
- Senate Health, Education, Labor, and Pensions
scoring:
  axes:
    A: -0.5
    B: 0.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.90
    D: 0.20        # Depth — unrelated to axes.D
    E_f: 0.40
    P: 0.60
  likelihood:
    p_committee: 0.10
    p_enact: 0.02
    basis: "base_rate_adjusted"
  rationale:
    A: "The Act directs HHS to build and run a government pandemic-preparedness program ('MedShield') that leverages AI for pathogen surveillance, vaccine/therapeutic development, and distribution modeling, gathering innovations 'across the public-private ecosystem.' The obligation runs against the Secretary of HHS, not against AI developers, and authorizes appropriations ($300M FY2025 rising to $500M FY2029) with no conduct standard, audit, or disclosure requirement placed on any private AI developer — this is capacity and money for a government program to use AI, not an obligation on the entities that build it, matching the −0.5 rung ('capacity and money with no obligations attached')."
    B: "Entirely silent on state authority to regulate AI — the bill is a federal biodefense program directed at HHS, FEMA coordination, and allied-nation partnership, with no state regulatory dimension and no savings clause. Implicit-preemption floor does not apply since axis A is negative, well below the +2 trigger."
    C: "Section 3 directs HHS to implement a standing, continuously operating program — 'The Program shall continuously operate and monitor threats' — integrating AI-enabled pathogen surveillance and interagency/international coordination, with a mandatory implementation-plan report to four congressional committees within 180 days of enactment. This is a new standing federal capability with appropriated funding and a reporting deadline, closer to the +1 'studies, GAO reviews, advisory committees with real reporting deadlines' rung than to +4/+5 — it is a continuously operating program rather than a one-off study, but it does not evaluate, audit, or oversee AI systems generally; it builds an operational biodefense capability that itself uses AI, not a government capacity to govern AI. Scored +1, reflecting the mandatory reporting deadline and standing-program structure while recognizing this is fundamentally a capability-building program not an oversight body."
    D: "No export-control or chip-access content; the international-coordination language (consulting 'allies and partners') is about biodefense cooperation, not AI-specific geopolitical competition or compute/chip access."
    E_consumer: "No provisions on deepfakes, NCII, companion bots, algorithmic discrimination, or election integrity — this is a biodefense/pandemic-preparedness program."
    F: "No data-center, compute-hardware, siting, or energy content."
    R: "A federal program (R baseline 1.0) intended to operate as a comprehensive, government-wide biodefense capability spanning HHS, FEMA's National Response Framework, and international partners — broad reach within its own class of 'federal AI-enabled government capability' bills."
    Depth: "Depth is driven by the largest-magnitude axis among A/B/C/F/E_consumer — here C at +1.0 (0.2 on the 0-1 scale) is the largest magnitude, reflecting a real but modest shift: a new standing program with funding and a reporting deadline, not a major oversight institution."
    E_f: "The bill imposes a mandatory reporting deadline (180 days post-enactment, to four named committees) with no civil penalty or private right of action if HHS fails to deliver — an obligation with a deadline but no penalty structure, matching the 0.4 rung ('obligation with no stated penalty'), rather than the 0.2 'voluntary' rung, since the reporting requirement is a binding 'shall submit,' not discretionary."
    P: "A sector-specific biodefense/pandemic-preparedness program implementing a specific NSCAI recommendation, self-contained within HHS's existing FEMA-coordination role — reintroduced from the 118th Congress (as S.5222, MedShield Act of 2024) without having advanced, suggesting a durable but narrow legislative template rather than a first-in-nation framework; scored at the upper end of sector-specific given the multi-year appropriations structure (FY2025-FY2029) that gives it more durability than a single-year authorization."
    likelihood: "Verified 2026-09-10: introduced 2025-03-14 by Rounds and Heinrich (co-chairs of the Senate AI Caucus), referred to HELP, no committee action (hearing or markup) recorded since referral. This is a reintroduction of a substantially identical bill from the 118th Congress (S.5222, MedShield Act of 2024) that also did not advance past committee referral — that base rate of non-advancement across two consecutive Congresses, combined with only one cosponsor and no scheduled hearing, supports a low enactment probability consistent with the tracker's prior confirmation of this bill as substantially AI-relevant."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- healthcare
- pandemic preparedness
- biodefense
- nscai
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/1085
- label: Sen. Rounds press release
  url: https://www.rounds.senate.gov/newsroom/press-releases/rounds-reintroduces-legislation-to-leverage-artificial-intelligence-for-pandemic-preparedness-and-response
summary: Bipartisan Senate bill directing HHS to implement an AI-driven pandemic preparedness and response program ("MedShield") per National Security Commission on AI recommendations.
timeline:
- date: '2025-03-14'
  event: Introduced by Sen. Rounds (with Sen. Heinrich), read twice and referred to Senate HELP Committee
---

The MedShield Act of 2025 would direct the Secretary of Health and Human Services to implement a continuously operating pandemic preparedness and response program, "MedShield," that uses artificial intelligence and other technologies for global pathogen surveillance, accelerated vaccine and therapeutic development, distribution-strategy optimization, and rapid manufacturing scale-up — implementing a specific recommendation from the National Security Commission on Artificial Intelligence's final report. The Secretary must develop an integration plan in coordination with FEMA's National Response Framework and international allies/partners, and report that plan to four congressional committees within 180 days of enactment. The bill authorizes appropriations rising from $300 million in FY2025 to $500 million in FY2029. It is a reintroduction of the MedShield Act of 2024 (118th Congress), which did not advance past committee referral.
