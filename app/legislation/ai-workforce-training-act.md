---
title: AI Workforce Training Act
short_name: AI Workforce Training Act
bill_numbers:
- H.R. 7576
congress: 119
topic: Research, Education & Workforce
status: introduced
chamber_origin: House
introduced_date: '2026-02-13'
last_action: Referred to committee; no further action
last_action_date: '2026-02-13'
sponsors:
- Rep. Josh Gottheimer (D-NJ)
- Rep. Mike Lawler (R-NY)
cosponsor_count: 1
committees:
- House Ways and Means
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
    R: 0.70
    D: 0.20        # Depth — unrelated to axes.D
    E_f: 0.40
    P: 0.20
  likelihood:
    p_committee: 0.05
    p_enact: 0.02
    basis: "govtrack_corroborated"
  rationale:
    A: "Places no obligation on AI developers — it's an employer-side tax credit (30% of qualified AI-training expenses, capped at $2,500/employee/year) available to any employer that provides AI-skills training, with no mandate or standard imposed on the companies that build AI systems."
    B: "No preemption or savings-clause language found in any available source — consistent with a tax bill amending the Internal Revenue Code, which has no occasion to touch state regulatory authority over AI. Confidence on this point is lower than usual given the bill's full text could not be directly confirmed (see text_source), but a tax-credit bill of this type would not plausibly contain preemption language."
    C: "Beyond the tax credit itself, the bill directs Treasury, Labor, and Commerce to run a joint small-business AI-training awareness campaign and requires a congressional report 360 days after enactment, then annually — a real, dated reporting obligation, though it stops well short of a funded evaluation body, standing incident-reporting stream, or new enforcement authority."
    D: "No export-control, chip-access, or other geopolitical-competition content."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election-integrity content — purely an employer-side workforce tax incentive."
    F: "No data-center, permitting, interconnection, or energy content."
    R: "A federal tax credit open to any employer nationwide providing qualifying AI training, so reach is federal, but the $2,500-per-employee cap and the requirement that expenses be 'qualified AI training' likely limits uptake to employers already investing in formal AI-skills programs — reach is real but narrower than an uncapped, universal provision, hence 0.70 rather than 0.90+."
    Depth: "The only active axis is governance-capacity-adjacent reporting (C = 1.0); the tax credit itself is scored on axis A at 0 because it flows to employers generally, not to AI developers, so Depth tracks the single C rung."
    E_f: "The tax credit is self-executing (claimed on a return, subject to ordinary IRS administration) with an anti-double-dipping clause but no civil penalty regime, agency rulemaking with penalties, or private right of action — an obligation/benefit with no distinct stated enforcement penalty beyond normal tax administration."
    P: "A narrow, sector-specific tax-credit bill with no sunset mentioned in available sources but also no institution-building or first-in-nation framework — a one-off IRS Code amendment rather than a template likely to be copied or a permanent new body."
    likelihood: "GovTrack's own modeled prognosis for H.R. 7576 is approximately 2% enactment / 5% committee — anchoring directly to that figure given the bill's very early stage. Introduced 2026-02-13 with a bipartisan two-member sponsor pairing (Gottheimer-D/Lawler-R) but only 1 cosponsor and no markup or floor action in the roughly seven months since introduction, and no Senate companion identified despite an explicit search. This is consistent with historical base rates for single-issue tax-credit bills introduced by rank-and-file members without committee-chair sponsorship or leadership prioritization — most such bills never receive a markup in Ways and Means, which has a large backlog of tax proposals every Congress."
  confidence: low
  text_source: summary
  scored_at: "2026-09-09"
tags:
- workforce
- tax credit
- training
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/7576
- label: GovTrack.us
  url: https://www.govtrack.us/congress/bills/119/hr7576
- label: Rep. Gottheimer press release
  url: https://gottheimer.house.gov/posts/release-gottheimer-introduces-bipartisan-ai-workforce-training-act
- label: FedScoop coverage
  url: https://fedscoop.com/ai-workforce-tax-credit-house-bill/
summary: Creates a 30% federal tax credit, capped at $2,500 per employee per year, for employer-provided AI-skills training.
timeline:
- date: '2026-02-13'
  event: Introduced by Rep. Gottheimer with Rep. Lawler; referred to House Ways and Means
- date: '2026-09-10'
  event: Verified — no markup, floor action, or Senate companion identified since introduction
---

The bill amends the Internal Revenue Code to create a tax credit equal to 30% of an employer's qualified AI-training expenses, capped at $2,500 per employee per year (inflation-adjusted after 2026), covering accredited courses, workshops, certificate programs, and in-house instruction in areas like data literacy, machine learning fundamentals, prompt engineering, and AI ethics. It also directs Treasury, Labor, and Commerce to run a joint public-awareness campaign aimed at small businesses and requires a congressional report 360 days after enactment and annually thereafter. Congress.gov's own bill text could not be directly confirmed against a primary source (repeated 403 responses), so this entry relies on secondary reporting and sponsor press releases; the bill has not advanced beyond committee referral since its February 2026 introduction.
