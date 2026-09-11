---
title: American A.I. Sovereign Wealth Fund Act
short_name: American AI Sovereign Wealth Fund Act
bill_numbers:
- S. 4825
congress: 119
topic: Government Use & Procurement
status: committee
chamber_origin: Senate
introduced_date: '2026-06-18'
last_action: Read twice and referred to the Senate Committee on Finance
last_action_date: '2026-06-18'
sponsors:
- Sen. Bernie Sanders (I-VT)
cosponsor_count: 0
committees:
- Senate Finance
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.70
    D: 0.20
    E_f: 0.80
    P: 0.80
  likelihood:
    p_committee: 0.01
    p_enact: 0.00
    basis: "govtrack_corroborated"
  rationale:
    A: "The tax-and-equity-seizure mechanism itself does not fit any A rung — it is not a conduct standard on training or deploying AI systems at all; it is a wealth/ownership transfer triggered by revenue thresholds, structurally closer to a tax bill than an AI-conduct bill. The one piece that plausibly touches developer conduct is the FTC-enforced structural-separation mandate (covered companies must divest non-AI holdings, share no officers/directors with non-AI entities, and file supplier/purchase information with the IRS) — a corporate-structure and reporting obligation, not a standard on training or deployment itself. Per the domain-general-mechanism guardrail this caps near the ±1 ceiling; scored +0.5 (procurement/reporting-adjacent, binds structure not conduct) rather than 0, since the separation-and-reporting regime is a real, enforceable obligation on covered entities, just not one that regulates model training or deployment. See below for why the tax's absence from A/B/C/D/F is deliberate, not an oversight."
    B: "No preemption or state-authority language anywhere in the text — this is an IRC amendment and a corporate-governance/commission structure, not a regulatory scheme that would trigger the implicit-preemption floor (it does not establish a federal regulatory scheme over AI development or deployment; it establishes a tax-and-shareholding regime), so B remains 0 rather than the −1 floor."
    C: "The Independent Commission for Democratic AI is a major new federal body, but its mandate is to exercise shareholder voting/governance rights and manage a sovereign wealth fund in companies' equity — it does not observe, evaluate, audit, or receive incident reports about AI systems' behavior or safety. It is public-ownership and corporate-governance capacity, not AI-oversight capacity, so it scores 0 on this axis rather than +5, for the same reason compute subsidies score on A instead of C: capacity to hold equity is not capacity to govern AI."
    D: "No export-control, chip-access, or geopolitical-competition content."
    F: "The tax attaches to AI data centers, computing infrastructure, and AI services by revenue/compute threshold, but it is a tax on equity and revenue, not a constraint or accelerant acting on a physical input (compute hardware, power, siting, water) the way axis F is scored — a 50% one-time equity levy changes who owns the capacity, not how much can be built or how easily, so this scores 0 on F rather than being mis-scored as a buildout constraint."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election content; the dividend to individuals is a fiscal transfer, not a consumer-harm stringency mechanism."
    R: "Applies to any corporation or partnership in an 'applicable AI trade or business' (AI data centers, AI computing infrastructure, AI services trained above 10^25 operations, advanced robotics) with gross receipts over $200M — a threshold clearly aimed at capturing the frontier/hyperscale tier of the industry, so R is high but not full: many mid-sized AI firms and the entire open-source/non-commercial ecosystem fall outside the $200M and compute thresholds entirely, docking it below the FAIR Act's near-total-reach analog."
    Depth: "max(|A|=0.5, |B|=0, |C|=0, |F|=0, E=0)/5 = 0.10 on the strict Depth formula — but this understates what this bill actually does, since its overwhelming real-world magnitude (a one-time transfer of 50% equity in the largest AI companies, ~$7T by sponsor estimate) doesn't load onto any of the five governance/harm axes the rubric measures. Recorded per the formula at 0.10 to stay faithful to the stated methodology; flagging explicitly that Depth as defined is not capturing this bill's actual scale, which is instead a taxation/wealth-distribution event, not an AI-governance event, no matter how large."
    E_f: "Backed by real enforcement: FTC-enforced structural separation within 90 days, a $1M flat penalty for failure to file, and an escalated 60%-equity default for underpayment — among the stronger enforcement postures in the tracker, at the 0.8 agency-rulemaking-plus-penalties band."
    P: "Would create a permanent institution (the Independent Commission for Democratic AI) with standing shareholder-governance authority over the designated companies in perpetuity — the clearest possible case of the 1.0 'creates a permanent institution' rung."
    likelihood: "GovTrack's own modeled prognosis for S. 4825 gives it a 1% chance of passing committee and 0% chance of enactment — explicitly anchoring to that figure here rather than a softer base rate, since GovTrack's own bill-specific model is available and this is exactly the case the rubric asks to anchor to it. Zero cosponsors, referred only to Finance, introduced by an independent senator with no history of bills of this scope advancing, in an election year where the bill functions more as a messaging vehicle than a legislative vehicle."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- excise tax
- sovereign wealth fund
- public ownership
- antitrust
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/4825
- label: Sanders Senate press release
  url: https://www.sanders.senate.gov/press-releases/news-sanders-introduces-legislation-to-create-7-trillion-ai-sovereign-wealth-fund/
summary: Would impose a one-time 50% equity tax on systemically important AI companies and place the resulting stake under a new Independent Commission for Democratic AI to fund public dividends.
timeline:
- date: '2026-06-18'
  event: Introduced and referred to Senate Finance
---

The American A.I. Sovereign Wealth Fund Act would impose a one-time 50% tax — paid in newly issued equity, not cash — on corporations and partnerships in "applicable AI trades or businesses" (AI data centers, AI computing infrastructure, frontier-scale AI services trained above 10^25 operations, and advanced robotics) with more than $200 million in annual gross receipts, with an additional tax triggered on later equity issuances. The seized equity stake, worth an estimated $7 trillion at the sponsor's valuation, would be held by the Treasury and managed by a new, permanently chartered Independent Commission for Democratic AI — a seven-member, Senate/House-confirmed body barred from having financial ties to covered companies — which would exercise all voting and governance rights attached to the shares (including seating board representatives) to advance worker welfare, public safety, competition, and environmental goals, while being barred from coordinating competitive conduct across competitors it holds stakes in. Up to 5% of the fund's average market value could be distributed annually, including direct payments to individuals, but the equity itself could never be sold or used to bail out a covered company. Covered companies would also face an FTC-enforced structural-separation mandate requiring them to divest non-AI holdings and report major AI-related purchases to the IRS.
