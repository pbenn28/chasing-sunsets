---
title: "Financial Artificial Intelligence Risk Reduction Act"
short_name: "FAIRR Act"
bill_numbers: ["S. 5358"]
congress: 119
topic: "Government Use & Procurement"
status: "introduced"
chamber_origin: "Senate"
introduced_date: "2026-08-06"
last_action: "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs"
last_action_date: "2026-08-06"
sponsors: ["Sen. Mark Warner (D-VA)", "Sen. John Kennedy (R-LA)"]
cosponsor_count: 1
committees: ["Senate Banking, Housing, and Urban Affairs"]
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.0
  impact_components:
    R: 0.20
    D: 0.40
    E_f: 0.60
    P: 0.60
  likelihood:
    p_committee: 0.30
    p_enact: 0.08
    basis: "base_rate_adjusted"
  rationale:
    A: "Places no conduct standard on AI developers. Every obligation in the bill runs against financial regulators (FSOC, the Office of Financial Research, the SEC, NCUA, FHFA) and against financial institutions in their capacity as AI deployers/vendors-of-record — e.g. the SEC-directed AI governance measures (testing, deployment monitoring, human oversight) and the 30-day third-party AI-vendor notification requirement bind regulated financial firms, not the developers who build the underlying models. Per the domain-general-mechanism guardrail, this is financial-stability regulation that touches AI as its subject matter, not AI-developer governance, so it scores 0 rather than being credited on axis A."
    B: "No state-law preemption language anywhere in the text — it amends only federal financial-stability statute (the Financial Stability Act of 2010) and directs federal regulators (FSOC, SEC, NCUA, FHFA, OFR). The implicit-preemption floor does not apply because axis A scores 0, well under the +2 threshold that triggers it."
    C: "CORRECTED under the frontier/systemic-risk guardrail (rubric: 'Guardrail: frontier/systemic risk vs. near-term consumer harm'). The original 3.0 treated FSOC's mandatory report, the OFR study, the stress-test exercises, and the NCUA/FHFA vendor-notification regime as a 'standing information flow into a government database' (+3) on the theory that a mandatory reporting mechanism into a federal oversight body qualifies regardless of subject. But the guardrail's test is whether the mechanism builds *systemic AI oversight capacity* in the ecosystem-wide sense the composite is tracking (frontier-scale training, catastrophic risk, loss-of-control, or cross-sectoral AI governance) — not sector-bounded financial-stability monitoring. 'Systemic' in FSOC's own vocabulary means systemic to the financial system (contagion, vendor concentration, market disruption), which is a different sense of systemic than the guardrail is protecting; every obligation here runs against financial regulators watching regulated institutions' own AI *use*, never against AI developers, and creates no cross-industry evaluation body or incident database reaching AI generally. That is structurally the same bounded-sector pattern the guardrail flags for chatbot/child-safety/elder-fraud bills, just dressed in financial-stability vocabulary. Corrected to 1.0 (studies/advisory tier — a real, recurring reporting requirement into Congress and stress-test exercises, but bounded to one sector with no new agency or cross-sectoral authority), with the bill's real severity moved to E_consumer."
    D: "No export-control, chip-access, or foreign-diversion content — purely a domestic financial-regulation bill."
    F: "No data-center, permitting, siting, water, or energy content."
    E_consumer: "CORRECTED alongside the C correction: under the frontier/systemic-risk guardrail, the bill's real substance — financial regulators building oversight of AI-enabled deepfake/synthetic-media fraud, AI-agent transaction risk, and AI-vendor concentration risk to consumers' financial institutions — belongs on this axis rather than being under-credited on C. It is still not a private right of action, criminal liability provision, or direct labeling mandate reaching individual consumers, so it doesn't approach the 3-5 rungs, but it is a real, multi-agency regulatory-coordination response (FSOC, OFR, SEC, NCUA, FHFA) to a named consumer/financial-fraud harm channel, not a bare mention — raised from 1.0 to 2.0 to reflect that this axis, not C, is where this bill's actual stringency belongs."
    R: "Reach is confined to SEC/NCUA/FHFA-regulated financial institutions and their AI vendors — a real but narrow slice of the AI-deployer universe relative to the frontier-developer or general-consumer classes other bills are normalized against, so R sits well below 1.0."
    Depth: "max(|A|,|B|,|C|,|F|,E) / 5 = max(0, 0, 1.0, 0, 2.0)/5 = 0.40. Recomputed after the C/E_consumer corrections under the frontier/systemic-risk guardrail."
    E_f: "SEC-directed AI governance measures and NCUA/FHFA examination authority carry agency rulemaking and examination/civil-penalty backing typical of federal financial regulation, but the bill creates no new standalone penalty scheme or private right of action — scored as agency rulemaking with enforcement (0.6, AG/regulator-enforcement-only tier) rather than the top rung."
    P: "Reintroduces, largely unchanged, the FAIRR Act first introduced in the 118th Congress (S. 3554, Dec. 2023) by the same two sponsors — a sector-specific, self-contained financial-regulation framework rather than a first-in-nation template likely to be copied outside the financial-stability context."
    likelihood: "Introduced 2026-08-06 with a single bipartisan original cosponsor (Kennedy) and referred to Senate Banking; no committee action recorded as of 2026-09-09. This is the third consecutive Congress in which materially the same Warner-Kennedy bill has been introduced without reaching a markup, which is the strongest available signal for its prospects. GovTrack's page for this bill returned HTTP 403 on fetch and no cached prognosis was found, so this estimate uses a base rate for bipartisan Senate Banking financial-regulation bills with a single cosponsor and a multi-Congress reintroduction history without committee movement, which skews low."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- financial services
- FSOC
- systemic risk
- regulatory coordination
sources:
- label: GovInfo BILLSTATUS bulk data
  url: https://www.govinfo.gov/bulkdata/BILLSTATUS/119/s/BILLSTATUS-119s5358.xml
- label: GovInfo bill text (introduced)
  url: https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s5358is.xml
- label: Congress.gov, 118th Congress predecessor (S. 3554)
  url: https://www.congress.gov/bill/118th-congress/senate-bill/3554
summary: Would amend the Financial Stability Act of 2010 to give the Financial Stability Oversight Council new coordinating duties to identify and report on AI-related risks to financial stability, and direct the SEC, NCUA, and FHFA to strengthen oversight of financial institutions' AI use and third-party AI vendors.
timeline:
- date: '2026-08-06'
  event: Introduced and referred to the Senate Committee on Banking, Housing, and Urban Affairs
- date: '2026-09-09'
  event: No further committee or floor action recorded since introduction
---

The bill would amend the Financial Stability Act of 2010 to direct FSOC to identify AI-related threats to financial stability (deepfake/synthetic-media manipulation, autonomous-agent transaction risk, AI-infrastructure concentration risk, cyber vulnerabilities) and recommend regulatory responses, with a mandatory report to Senate Banking and House Financial Services within 180 days of enactment. It also directs the Office of Financial Research to study financial-institution AI use, has the President's Working Group on Financial Markets run AI-disruption stress-test exercises, directs the SEC to require AI governance measures from regulated entities, and gives NCUA and FHFA enhanced examination authority over credit unions' and housing-finance entities' third-party AI vendors, with a 30-day vendor-relationship notification requirement. It is a reintroduction, largely unchanged, of the same Warner-Kennedy bill first introduced in the 118th Congress.
