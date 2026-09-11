---
title: AI Workforce Projections, Research, and Evaluations to Promote AI Readiness and Employment Act
short_name: AI Workforce PREPARE Act
bill_numbers:
- S. 3339
congress: 119
topic: Research, Education & Workforce
status: introduced
chamber_origin: Senate
introduced_date: '2025-12-03'
last_action: Read twice and referred to the Senate Committee on Health, Education, Labor, and Pensions
last_action_date: '2025-12-03'
sponsors:
- Sen. Jim Banks (R-IN)
cosponsor_count: 3
committees:
- Senate Health, Education, Labor, and Pensions
scoring:
  axes:
    A: 1.0
    B: 0.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 1.0
  impact_components:
    R: 0.90
    D: 0.20
    E_f: 0.40
    P: 0.60
  likelihood:
    p_committee: 0.35
    p_enact: 0.10
    basis: "base_rate_adjusted"
  rationale:
    A: "Amends the WARN Act so that, when AI is 'a substantial factor' in a mass layoff already triggering existing WARN notice thresholds, employers must additionally disclose that AI was a factor, describe the type/use of the AI involved, estimate the share of job loss attributable to it, and describe pre-layoff retraining efforts. This is disclosure only — a 'good-faith statement' standard applies, no new penalty beyond existing WARN Act enforcement is created, and the underlying WARN layoff-notice threshold itself is untouched. Binds employers as AI deployers, not frontier developers, but the disclosure object is specifically AI's role in job loss, so it isn't a domain-general mechanism merely brushing against AI."
    B: "No preemption or savings-clause language anywhere in the bill. A scores +1 (below the ≥+2 implicit-preemption-floor trigger), so B remains 0 (silent) rather than being floored to −1."
    C: "Corrected per the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: the AI Workforce Research Hub is a dedicated, funded evaluation body that textually matches the +4 'authorizes and funds a dedicated evaluation body' rung, but the guardrail requires asking what the body actually observes, not just whether it looks like an evaluation body. The Hub (with Census, BEA, and BLS) forecasts AI's labor-market and employment impact — it is squarely 'protecting a specific population (workers)... from AI already in ordinary deployment,' not building 'systemic AI oversight capacity' (model evals, incident databases, safety testbeds). That places it in the guardrail's floor band for C ('rarely above +0.5–+1, even for a real standing reporting regime'). Rescored to +1 to reflect that it is a real, funded, dated body — the top of the floor band — while the +4 rung is reserved for bodies that actually evaluate frontier/systemic AI risk, which this is not."
    D: "No export-control, chip-access, or geopolitical-competition content anywhere in the bill."
    E_consumer: "Corrected per the frontier/systemic-risk guardrail: with C pulled down to the floor band because the Research Hub's subject (worker/labor-market impact, not frontier AI oversight) belongs on E rather than C, this axis should carry the bill's actual real-world substance instead of sitting at 0. The WARN Act amendment requires employers to disclose AI's role in mass layoffs to affected workers and regulators — a labeling/disclosure-style transparency mandate aimed at a narrow population (workers) rather than deepfake/NCII/companion-bot/discrimination/election harms, but analogous in kind to the 'end-user labeling requirement only' rung. Bumped from 0.0 to 1.0 to reflect that real, if modest, disclosure-based harm mitigation."
    F: "No data-center, permitting, interconnection, siting, or ratepayer content."
    R: "The WARN amendment rides on WARN's own existing mass-layoff thresholds (100+ employees at covered establishments), so its reach is exactly as broad as WARN's current coverage — near-total among the target class of large-scale layoff events — while the Research Hub and forecasting titles apply federal-government-wide with no sector carve-out."
    Depth: "Recomputed after the frontier/systemic-risk guardrail correction — now driven by axis A (frontier developer stringency) at 1.0/5."
    E_f: "The WARN disclosure obligation attaches to an existing statute with its own enforcement scheme (WARN Act civil penalties for notice violations), but the new AI-specific disclosure content itself is governed by a 'good-faith statement' standard with no precision requirement — an obligation with a penalty structure attached via the underlying WARN Act, landing above pure voluntary disclosure but below a dedicated civil-penalty regime built for this provision specifically."
    P: "Creates a new (if four-year-sunset) federal institution — the AI Workforce Research Hub — making this closer to the 'creates an institution' end of the Precedent ladder, tempered by the sunset provision, which is why P lands at 0.60 rather than 1.0."
    likelihood: "Introduced 2025-12-03 with three cosponsors (Hassan D-NH, Hickenlooper D-CO, Husted R-OH) reflecting real bipartisan interest, and referred to Senate HELP, the same committee holding S. 3108. Sen. Banks held a related hearing on AI's workforce impact and there is reported momentum ('Lawmakers want better data on AI's workforce impacts,' Roll Call, 2026-07-29) suggesting continued attention, but no markup or floor vote has occurred in the roughly nine months since introduction. GovTrack's bill-specific prognosis wasn't directly accessible (403 on direct fetch, corroborated via WebSearch instead); this uses a base rate for multi-cosponsor bipartisan HELP bills with hearing-level but not markup-level activity — somewhat better odds than S. 3108's single-cosponsor posture, but still a Congress where most bills at this stage don't advance."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- workforce
- DOL
- WARN Act
- research hub
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/3339
- label: Sen. Banks press release
  url: https://www.banks.senate.gov/news/press-releases/senator-banks-introduces-the-ai-workforce-prepare-act/
- label: Bill text (GovInfo)
  url: https://www.govinfo.gov/content/pkg/BILLS-119s3339is/html/BILLS-119s3339is.htm
- label: "Roll Call — Lawmakers want better data on AI's workforce impacts"
  url: https://rollcall.com/2026/07/29/lawmakers-want-better-data-on-ais-workforce-impacts/
summary: Bipartisan Senate bill creating a DOL AI Workforce Research Hub and amending the WARN Act to require AI-specific disclosure in mass-layoff notices.
timeline:
- date: '2025-12-03'
  event: Introduced by Sen. Banks with cosponsors Hassan, Hickenlooper, and Husted; read twice and referred to Senate HELP
---

The bill creates an AI Workforce Research Hub within the Department of Labor — operating with the Census Bureau, Bureau of Economic Analysis, and Bureau of Labor Statistics — to forecast AI's impact on employment, run scenario planning, and generate policy-relevant analyses, backed by roughly $53.5 million in appropriations through FY2030 and sunsetting after four years. It also amends the WARN Act so that when AI is a substantial factor in a mass layoff already subject to WARN notice requirements, employers must additionally disclose AI's role, describe the AI involved, estimate the share of job loss attributable to it, and describe any pre-layoff retraining efforts, using a good-faith-statement standard rather than a precise-accounting requirement. The amendments take effect for notices issued starting roughly one year after enactment.
