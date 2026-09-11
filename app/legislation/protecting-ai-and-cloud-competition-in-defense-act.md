---
title: Protecting AI and Cloud Competition in Defense Act of 2025
short_name: Protecting AI and Cloud Competition in Defense Act
bill_numbers:
- H.R. 3434
- S. 1775
congress: 119
topic: Chips & National Security
status: committee
chamber_origin: Both
introduced_date: '2025-05-15'
last_action: Referred to House Committee on Armed Services (H.R. 3434) and Senate Committee on Armed Services (S. 1775); no further action
last_action_date: '2025-05-15'
sponsors:
- Rep. Pat Fallon (R-TX)
- Sen. Elizabeth Warren (D-MA)
cosponsor_count: 3
committees:
- House Armed Services
- Senate Armed Services
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.15
    D: 0.20
    E_f: 0.6
    P: 0.4
  likelihood:
    p_committee: 0.03
    p_enact: 0.01
    basis: "base_rate_adjusted"
  rationale:
    A: "Binds DOD as the buyer, not AI developers generally: covered providers (cloud, data-infrastructure, or foundation-model providers with ≥$50M in DOD contracts over the preceding 5 fiscal years) face competitive-award and data-use conditions only as a term of doing business with the Pentagon. This is the textbook procurement/government-use-conditions rung — it doesn't touch a developer's training, deployment, or release practices outside the DOD contracting relationship, so it doesn't rise to a conduct-standard mandate (+2) despite having real penalties (fines, contract termination) attached to the government-data-training restriction."
    B: "No preemption or savings-clause language anywhere in either bill's text — expected, since this is a defense-procurement statute directed at DOD's own contracting behavior, not a regulatory scheme over AI developers' general market conduct. The implicit-preemption floor doesn't apply because A scores well below the +2 threshold that would trigger it."
    C: "The Chairman of the Joint Chiefs, coordinating with the Under Secretary of Defense for Acquisition and Sustainment, must submit an annual public report to the congressional defense committees for four years starting no later than January 15, 2027, assessing competition, market concentration, and entry barriers in defense AI/cloud contracting, plus exemptions granted — a standing, deadline-bound reporting requirement, but internal DOD-to-Congress oversight rather than a new independent evaluation body or public incident database, landing at the studies/reporting-with-real-deadlines rung rather than higher."
    D: "No export-control, foreign-access, or allied-coordination provisions; this is a domestic defense-contracting competition bill."
    E_consumer: "No consumer or near-term-harm content."
    F: "No compute, energy, data-center, or siting provisions — the bill's data-infrastructure-provider language concerns contracting terms, not physical buildout."
    R: "Reach is narrow and sector-specific by design: only covered providers with ≥$50M in cumulative DOD contracts over five years are bound, and the obligation only applies to that DOD contracting relationship — a small slice even of the frontier-developer population, most of whose revenue and conduct falls outside defense procurement."
    Depth: "Driven by the C reporting requirement and the A procurement-conditions rung; both are real but modest, non-frontier-wide mechanisms — the max of |A|, |B|, |C|, |F|, E lands well below the midpoint of the 0–5 scale."
    E_f: "Violations of the data-training-use restriction carry fines and contract termination — real, if contractually rather than civilly enforced, penalties administered through existing DFARS/acquisition mechanisms rather than agency rulemaking or a private right of action."
    P: "A vendor-lock-in/competition template specific to defense AI and cloud contracting; it echoes a broader federal-procurement-competition tradition (and a 118th Congress predecessor, S. 5436) rather than establishing a genuinely novel or likely-to-be-copied general framework."
    likelihood: "Reintroduced from an identical 118th Congress predecessor (S. 5436) that did not advance, itself a signal of low momentum. Both H.R. 3434 and S. 1775 remain at 'Introduced' status per the Steptoe Federal AI Legislative Tracker (dated 2026-03-16), with no markup, hearing, CBO score, or floor action in either chamber since referral on 2025-05-15. A secondary source suggested this language might have been folded into the enacted FY2026 NDAA (signed 2025-12-18) as a 'section 876,' but this could not be corroborated against congress.gov or law-firm NDAA summaries (WilmerHale, Akin Gump, K&L Gates, Mintz) that specifically covered the NDAA's AI provisions — treating the standalone bills as still pending and NOT enacted. Bipartisan, bicameral sponsorship (Fallon/Jacobs/Deluzio in the House; Warren/Schmitt in the Senate) is a positive signal, but a non-marquee competition/procurement bill sitting in Armed Services committees in both chambers for over a year with no action is a thin base; using historical base rates for reintroduced, twice-unadvanced procurement bills rather than an unverified GovTrack prognosis figure (GovTrack's page could not be independently re-fetched to confirm the exact percentage reported in search snippets)."
  confidence: low
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- DOD
- procurement
- cloud
- foundation models
- competition
sources:
- label: Congress.gov — H.R. 3434
  url: https://www.congress.gov/bill/119th-congress/house-bill/3434
- label: Congress.gov — H.R. 3434 full text
  url: https://www.congress.gov/119/bills/hr3434/BILLS-119hr3434ih.pdf
- label: Congress.gov — S. 1775
  url: https://www.congress.gov/bill/119th-congress/senate-bill/1775
- label: "Sen. Warren bill text (discussion draft, Warren office)"
  url: https://www.warren.senate.gov/imo/media/doc/bill_text_-_protecting_ai_and_cloud_competition_in_defense_act_of_2025.pdf
- label: "Sen. Warren press release — Warren & Schmitt renew bipartisan fight"
  url: https://www.warren.senate.gov/newsroom/press-releases/warren-schmitt-renew-bipartisan-fight-for-more-competition-in-pentagons-ai-and-cloud-contracting/
- label: "Rep. Fallon press release"
  url: https://fallon.house.gov/news/documentsingle.aspx?DocumentID=1592
- label: "DefenseScoop — Lawmakers introduce bipartisan bill"
  url: https://defensescoop.com/2025/05/16/protecting-ai-cloud-competition-defense-act-2025/
summary: Would require competitive-award procedures and data-rights protections for DOD AI, cloud, and foundation-model contracts of $50 million or more.
timeline:
- date: '2025-05-15'
  event: H.R. 3434 introduced by Rep. Fallon; S. 1775 introduced by Sen. Warren; both referred to their chambers' Armed Services committees
- date: '2025-05-16'
  event: DefenseScoop and sponsor press releases cover the bipartisan, bicameral introduction
- date: '2026-09-09'
  event: Verified — both bills remain at introduced/referred status per Steptoe's federal AI tracker; no evidence of inclusion in the enacted FY2026 NDAA despite one uncorroborated secondary claim
---

The Protecting AI and Cloud Competition in Defense Act of 2025 would require the Department of Defense to use a competitive award process for cloud computing, data infrastructure, and foundation-model contracts once a provider has received $50 million or more from DOD over the preceding five fiscal years. It directs DOD to retain exclusive rights to government data, bars covered providers from using government-furnished data to train their own commercial products without express authorization (with fines and contract termination as penalties), and requires the Joint Chiefs Chairman to report annually to Congress on competition and market concentration in defense AI/cloud contracting starting in 2027. This is a defense-procurement and anti-vendor-lock-in bill that binds DOD's contracting behavior and its covered vendors' data use within that relationship — it does not impose a general conduct standard on AI developers and contains no preemption language.

A reintroduction of a 118th Congress predecessor (S. 5436) that did not advance, sponsored by Rep. Pat Fallon (R-TX) with Reps. Sara Jacobs (D-CA) and Chris Deluzio (D-PA) in the House, and Sen. Elizabeth Warren (D-MA) with Sen. Eric Schmitt (R-MO) in the Senate. Both companion bills remain in their respective Armed Services committees with no further action since introduction.
