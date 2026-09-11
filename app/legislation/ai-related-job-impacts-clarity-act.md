---
title: AI-Related Job Impacts Clarity Act
short_name: AI-Related Job Impacts Clarity Act
bill_numbers:
- S. 3108
congress: 119
topic: Research, Education & Workforce
status: introduced
chamber_origin: Senate
introduced_date: '2025-11-05'
last_action: Read twice and referred to the Senate Committee on Health, Education, Labor, and Pensions
last_action_date: '2025-11-05'
sponsors:
- Sen. Josh Hawley (R-MO)
- Sen. Mark Warner (D-VA)
cosponsor_count: 1
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
    E_consumer: 0.0
  impact_components:
    R: 0.80
    D: 0.20
    E_f: 0.40
    P: 0.60
  likelihood:
    p_committee: 0.30
    p_enact: 0.10
    basis: "base_rate_adjusted"
  rationale:
    A: "A quarterly disclosure mandate — publicly traded companies, federal agencies, and non-public companies meeting Secretary-of-Labor-set thresholds must report AI-driven layoffs, AI-role hires, eliminated unfilled positions, and retraining counts. This is disclosure only, with no substantive standard on how AI is developed or deployed and no audit, licensing, or risk-framework requirement attached — the ceiling for pure disclosure. Note this binds AI *deployers* in their capacity as employers, not frontier *developers* directly, but the guardrail on domain-general mechanisms doesn't apply here since the reporting object is specifically AI-driven job impact, not a generic mechanism that incidentally touches AI."
    B: "No preemption or savings-clause language anywhere in the bill text. The implicit-preemption floor doesn't apply: A scores +1, below the ≥+2 threshold that would trigger the floor, so B stays at 0 (silent)."
    C: "Directs the Department of Labor (via the Bureau of Labor Statistics) to collect, compile, and publish quarterly public reports and biannual analyses — a standing information flow, but into a labor-statistics function rather than an AI-safety oversight body, and BLS gains no enforcement authority over the companies reporting to it. Scored as a studies/reporting-deadline measure rather than the +3 standing-information-flow rung, which the rubric reserves for reporting into a government database used for governance/enforcement purposes; here the object is labor-market statistics, not AI governance capacity."
    D: "No export-control, chip-access, or geopolitical-competition content anywhere in the bill."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election-integrity content — this is a labor-market transparency measure, not a consumer-harm bill."
    F: "No data-center, permitting, interconnection, siting, or ratepayer content."
    R: "Covers all publicly traded companies and federal agencies outright, plus non-public companies above thresholds the Secretary of Labor must set within 180 days — likely capturing most large employers but leaving smaller/private firms' coverage contingent on not-yet-written regulations, so R sits below 1.0 pending that rulemaking."
    Depth: "Driven by the A score (disclosure mandate, 1.0/5) — the deepest single axis, giving Depth = 1/5 = 0.20."
    E_f: "Companies must report, and reports are made public and sent to Congress, but the bill text specifies no penalty, civil fine, or enforcement mechanism for non-compliance — an obligation with no stated penalty."
    P: "A first-in-nation federal framework for standardized AI-driven job-impact reporting; if enacted, a natural template other committees or states could copy for their own labor-market transparency measures, though it's not (yet) a permanent institution beyond the reporting function itself."
    likelihood: "Introduced 2025-11-05 with only one cosponsor (bipartisan pairing: Hawley R-MO, Warner D-VA) and referred to Senate HELP, where it has seen no committee action in the ten months since. GovTrack's bill-specific prognosis was not directly accessible (congress.gov and govtrack.us both returned 403s to automated fetch and were corroborated via WebSearch/press coverage instead), so this uses a base rate for single-sponsor-pair HELP-committee bills with no markup after this long — a bipartisan pairing helps, but a critical think-tank response (Center for Data Innovation) and no visible committee interest are also signals. Low but non-trivial odds of advancing, lower odds of enactment within this Congress."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- workforce
- reporting
- DOL
- transparency
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/3108
- label: Sen. Warner press release
  url: https://www.warner.senate.gov/public/index.cfm/2025/11/warner-hawley-to-introduce-bipartisan-legislation-to-track-number-of-jobs-lost-to-ai
- label: Bill text (Hawley Senate office PDF)
  url: https://www.hawley.senate.gov/wp-content/uploads/2025/11/AI-Related-Job-Impacts-Clarity-Act.pdf
- label: "Center for Data Innovation — critical response"
  url: https://datainnovation.org/2025/11/the-ai-related-job-impacts-clarity-act-will-only-create-confusion/
summary: Bipartisan Senate bill requiring large companies and federal agencies to report AI-driven job displacement quarterly to the Department of Labor.
timeline:
- date: '2025-11-05'
  event: Introduced by Sens. Hawley and Warner; read twice and referred to Senate HELP
---

The bill requires publicly traded companies, federal agencies, and non-public companies meeting size thresholds the Secretary of Labor must set within 180 days to report quarterly on AI-driven job impacts: workers laid off due to AI automation, workers hired for AI-related roles, unfilled positions eliminated by AI, and workers being retrained as a result of AI adoption. The Department of Labor, through the Bureau of Labor Statistics, would publish the disclosures and produce recurring public summary and analysis reports, including reports to Congress. No enforcement mechanism or penalty for non-compliance is specified in the text.
