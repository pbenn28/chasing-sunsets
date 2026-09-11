---
title: Generative AI Terrorism Risk Assessment Act
short_name: Generative AI Terrorism Risk Assessment Act
bill_numbers:
- H.R. 1736
congress: 119
topic: Frontier Safety & Oversight
status: passed_one_chamber
chamber_origin: House
introduced_date: '2025-02-27'
last_action: "Received in the Senate, read twice, and referred to the Senate Committee on Homeland Security and Governmental Affairs"
last_action_date: '2025-11-20'
sponsors:
- Rep. August Pfluger (R-TX)
cosponsor_count: 2
committees:
- House Homeland Security
- Senate Homeland Security and Governmental Affairs
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 0.5
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.30
    D: 0.10
    E_f: 0.20
    P: 0.20
  likelihood:
    p_committee: 0.55
    p_enact: 0.30
    basis: "govtrack_corroborated"
  rationale:
    A: "Places no obligation on AI developers at all — DHS is the actor required to produce annual threat assessments and disseminate fusion-center intelligence. There is no disclosure, audit, incident-reporting, or process requirement running against anyone who builds or deploys generative AI, so this doesn't clear even the +1 'disclosure only' rung; it scores 0 as a pure study/reporting mandate, per the rubric's 'studies, task forces, definitions' rung."
    B: "No preemption or savings-clause language anywhere in the text (confirmed against the reported House text). The implicit-preemption floor doesn't apply because this bill doesn't clear A ≥ +2 or establish a regulatory scheme over private conduct — it's an intelligence-assessment mandate directed entirely at DHS itself, so B is genuinely silent/neutral rather than floored."
    C: "Requires DHS to produce a recurring (annual, 5-year) assessment and brief Congress within 30 days each time, and to systematically review and disseminate fusion-center intelligence on generative-AI-enabled terrorism threats. That is a real standing information flow, but its object is counterterrorism/homeland-security intelligence sharing, not observation of AI development or deployment — applying the domain-general-mechanism guardrail, this is counterterrorism infrastructure that happens to name generative AI as a threat vector, not an AI-governance capacity build. Capped at the ±1 ceiling for a narrow, contingent AI-specific channel (DHS must specifically track and report on generative-AI use by terrorist groups, which is more concrete than a generic mention), landing at +0.5 rather than the full +1 because the deliverable is a report/briefing rather than an enforcement or evaluation function."
    D: "No export-control, chip-access, or foreign-technology-diffusion content."
    E_consumer: "No consumer-facing deepfake, NCII, companion-bot, or discrimination content — this is a counterterrorism intelligence bill, not a consumer-harm bill."
    F: "No data-center, compute, permitting, siting, or energy content."
    R: "Federal bill, but the entire obligation runs against one federal agency (DHS) rather than against any class of AI developers or deployers — there is no 'target universe' of covered entities being reached the way a developer-facing or consumer-facing bill would reach one, so R is scored low to reflect that this is government-internal capacity rather than industry-wide coverage."
    Depth: "max(|A|, |B|, |C|, |F|, E) / 5 = max(0, 0, 0.5, 0, 0) / 5 = 0.10 — the only nonzero axis is the narrow +0.5 on C."
    E_f: "DHS faces a statutory reporting deadline (annual assessments, 30-day briefings) but there's no rulemaking, civil penalty, or private right of action attached — an obligation with a real deadline but no stated penalty for noncompliance beyond ordinary oversight pressure."
    P: "A time-limited (5-year sunset), single-agency reporting requirement focused on one narrow threat vector — not a framework likely to be copied elsewhere or a permanent institution, though it does set a template DHS could extend to other tech-threat categories."
    likelihood: "Verified 9/9-9/10/26: H.R. 1736 passed the full House by voice vote under a motion to suspend the rules on 2025-11-19 (as amended), following House Homeland Security Committee ordering it reported 2025-09-03 (H. Rept. 119-373). It was received in the Senate on 2025-11-20 and referred to the Senate Committee on Homeland Security and Governmental Affairs, where it has seen no further action as of this writing. GovTrack's own prognosis model puts H.R. 1736's overall enactment probability at 37% — a notably high figure for a non-appropriations bill, reflecting its voice-vote passage, low fiscal cost (CBO: under $500K through 2030), and lack of any partisan flashpoint. p_enact is set slightly below GovTrack's 37% anchor at 30% to reflect that Senate Homeland Security has taken no action in the ~9.5 months since referral and this class of narrow DHS-reporting bill often stalls even when uncontroversial; p_committee is set higher (0.55) reflecting that voice-vote House passage plus a germane, low-controversy Senate committee of jurisdiction makes committee movement plausible if leadership prioritizes floor time."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- terrorism
- DHS
- fusion centers
- homeland security
- passed House
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/1736
- label: GovTrack.us
  url: https://www.govtrack.us/congress/bills/119/hr1736
- label: House Report 119-373
  url: https://www.congress.gov/committee-report/119th-congress/house-report/373/1
- label: CBO cost estimate
  url: https://www.cbo.gov/publication/61821
summary: Requires DHS to conduct periodic assessments of terrorist organizations' use of generative AI and enhance information-sharing through the National Network of Fusion Centers.
timeline:
- date: '2025-02-27'
  event: Introduced by Rep. August Pfluger; referred to House Homeland Security
- date: '2025-09-03'
  event: Ordered reported by House Homeland Security Committee (H. Rept. 119-373)
- date: '2025-11-19'
  event: Passed the full House, as amended, by voice vote under suspension of the rules
- date: '2025-11-20'
  event: Received in the Senate, read twice, and referred to the Senate Committee on Homeland Security and Governmental Affairs
---

The Generative AI Terrorism Risk Assessment Act requires the Secretary of Homeland Security, in consultation with the Director of National Intelligence, to produce an annual assessment — for five years after enactment — of the threat posed by foreign terrorist organizations' use of generative AI, including AI's role in spreading extremist messaging, radicalization and recruitment, and enhancing the development or deployment of chemical, biological, radiological, or nuclear weapons. Congress must be briefed within 30 days of each submission. DHS must also review information gathered by the National Network of Fusion Centers relevant to generative-AI-enabled terrorism threats, incorporate it into its assessments, and disseminate relevant findings back down to state and local fusion centers, coordinating with the FBI and the broader intelligence community. The bill directs DHS to ensure its activities comply with existing privacy, civil rights, and civil liberties protections, but places no obligation of any kind on AI developers themselves.

H.R. 1736 passed the full House by voice vote on 2025-11-19 under a motion to suspend the rules, after House Homeland Security ordered it reported in September 2025. It was received in the Senate on 2025-11-20 and referred to the Senate Committee on Homeland Security and Governmental Affairs, where it remains as of this writing with no further action recorded.
