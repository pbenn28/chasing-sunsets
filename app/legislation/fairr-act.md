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
    C: 3.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 1.0
  impact_components:
    R: 0.20
    D: 0.60
    E_f: 0.60
    P: 0.60
  likelihood:
    p_committee: 0.30
    p_enact: 0.08
    basis: "base_rate_adjusted"
  rationale:
    A: "Places no conduct standard on AI developers. Every obligation in the bill runs against financial regulators (FSOC, the Office of Financial Research, the SEC, NCUA, FHFA) and against financial institutions in their capacity as AI deployers/vendors-of-record — e.g. the SEC-directed AI governance measures (testing, deployment monitoring, human oversight) and the 30-day third-party AI-vendor notification requirement bind regulated financial firms, not the developers who build the underlying models. Per the domain-general-mechanism guardrail, this is financial-stability regulation that touches AI as its subject matter, not AI-developer governance, so it scores 0 rather than being credited on axis A."
    B: "No state-law preemption language anywhere in the text — it amends only federal financial-stability statute (the Financial Stability Act of 2010) and directs federal regulators (FSOC, SEC, NCUA, FHFA, OFR). The implicit-preemption floor does not apply because axis A scores 0, well under the +2 threshold that triggers it."
    C: "Gives FSOC new statutory coordinating duties to identify AI-related threats to financial stability and develop regulatory-gap recommendations; directs the Office of Financial Research to study financial-institution AI use; requires a mandatory FSOC report to Senate Banking and House Financial Services within 180 days followed by a 30-day congressional comment window; directs the President's Working Group on Financial Markets to run AI-disruption stress-test exercises; and grants NCUA/FHFA enhanced examination authority over credit unions' and housing-finance entities' third-party AI vendors, backed by a standing 30-day vendor-relationship notification requirement. This combination of a mandatory reporting flow into Congress, a recurring stress-testing exercise, and new examination authority for existing regulators lands at +3 (standing information flows into government oversight) rather than +4, since it coordinates and directs existing bodies rather than authorizing and funding a wholly new dedicated evaluation body."
    D: "No export-control, chip-access, or foreign-diversion content — purely a domestic financial-regulation bill."
    F: "No data-center, permitting, siting, water, or energy content."
    E_consumer: "Identifies AI-enabled deepfake/synthetic-media manipulation and AI-agent transaction risk as financial-stability threats FSOC must track, but this is a risk-identification and regulatory-coordination provision, not a private right of action, criminal liability, or a labeling mandate reaching individual consumers directly — scored at the low end of the ladder, just above 'no consumer/near-term harm content,' as an end-user-adjacent risk-monitoring mention rather than a labeling requirement itself."
    R: "Reach is confined to SEC/NCUA/FHFA-regulated financial institutions and their AI vendors — a real but narrow slice of the AI-deployer universe relative to the frontier-developer or general-consumer classes other bills are normalized against, so R sits well below 1.0."
    Depth: "max(|A|,|B|,|C|,|F|,E) / 5 = max(0, 0, 3.0, 0, 1.0)/5 = 0.60."
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
