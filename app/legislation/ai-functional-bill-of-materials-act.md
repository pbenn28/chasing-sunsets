---
title: "A bill to provide for the delivery of artificial intelligence functional bills of materials"
short_name: "AI Bill of Materials Act"
bill_numbers: ["S. 5345"]
congress: 119
topic: "Government Use & Procurement"
status: "introduced"
chamber_origin: "Senate"
introduced_date: "2026-08-06"
last_action: "Read twice and referred to the Committee on Armed Services"
last_action_date: "2026-08-06"
sponsors: ["Sen. Elissa Slotkin (D-MI)"]
cosponsor_count: 0
committees: ["Senate Armed Services"]
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
    R: 0.30
    D: 0.20
    E_f: 0.40
    P: 0.40
  likelihood:
    p_committee: 0.30
    p_enact: 0.10
    basis: "base_rate_adjusted"
  rationale:
    A: "Bars DoD from entering, renewing, or extending any contract for AI-utilizing goods or services unless the contractor delivers and maintains an AI functional bill of materials (software, data, and hardware provenance, retrievable within 48 hours of a DoD request). This is a disclosure condition that binds the contractor/vendor as a condition of a government contract, not a standing conduct standard on AI developers generally — squarely the rubric's 'procurement and government-use conditions: binds the buyer, not the builder' rung (+0.5), not the higher disclosure-only rung (+1) which is reserved for developer-facing frameworks/model-card mandates untied to a specific contract relationship."
    B: "Silent on preemption; runs entirely through DFARS rulemaking and DoD contracting authority, never mentions state or local government. The implicit-preemption floor does not apply because A scores well below the +2 threshold that triggers it."
    C: "Requires SecDef to issue implementing DFARS regulations and DISA/DoD CIO guidance within 180 days, and a report to the House and Senate Armed Services Committees within one year on implementation status and feasibility — a bounded, one-time reporting obligation tied to contract compliance, not a standing AI-oversight body or database. Scored as a study/reporting-deadline provision (+1) rather than a standing information flow (+3), since the BOM records flow to contracting officers for procurement compliance, not into a government AI-oversight database with reporting into broader oversight function."
    D: "No export-control, chip-access, or foreign-diversion content."
    F: "No data-center, permitting, siting, water, or energy content."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election-integrity content; scoped entirely to DoD contractor supply-chain transparency."
    R: "Reach is confined to the subset of AI developers and integrators who sell AI-utilizing goods or services to the Department of Defense — a real but narrow slice of the AI industry, not the frontier-developer universe as a whole, so R is scored well below 1.0 despite applying to essentially all DoD AI contracts within that slice."
    Depth: "max(|A|,|B|,|C|,|F|,E) / 5 = max(0.5, 0, 1.0, 0, 0)/5 = 0.20."
    E_f: "Enforcement runs through contracting leverage — DoD simply may not award, renew, or extend a contract absent a compliant AI-BOM — a binding obligation but not backed by civil penalties, agency rulemaking-with-penalties, or a private right of action."
    P: "Sector-specific and self-contained: a DoD-procurement transparency requirement modeled on existing software bill-of-materials policy, extending an established federal-contracting template to AI rather than creating a new permanent institution or a preemption ceiling."
    likelihood: "Introduced 2026-08-06 and referred to Senate Armed Services with no cosponsors and no committee action recorded as of 2026-09-09 — a sole-sponsor bill barely a month old. GovTrack's page for this bill returned HTTP 403 on fetch and no cached prognosis was found, so this estimate uses a base rate for sole-sponsor Senate bills referred to Armed Services with no committee action, adjusted upward slightly because Sen. Slotkin (a Senate Armed Services member) has separately and successfully pushed an AI-bill-of-materials requirement into the FY2027 NDAA (reported as Section 1652), which is the far more likely enactment vehicle for this policy — meaning this standalone bill's own odds of passage as freestanding legislation are low even though the underlying policy idea has real momentum through the NDAA."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- procurement
- supply chain
- defense
- transparency
sources:
- label: GovInfo BILLSTATUS bulk data
  url: https://www.govinfo.gov/bulkdata/BILLSTATUS/119/s/BILLSTATUS-119s5345.xml
- label: GovInfo bill text (introduced)
  url: https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s5345is.xml
- label: LegiScan bill tracking
  url: https://legiscan.com/US/bill/SB5345/2025
summary: Would bar the Department of Defense from awarding, renewing, or extending any contract for AI-utilizing goods or services unless the contractor delivers and maintains a machine-readable "AI functional bill of materials" documenting the software, data, and hardware underlying the system.
timeline:
- date: '2026-08-06'
  event: Introduced and referred to the Senate Committee on Armed Services
- date: '2026-09-09'
  event: No further committee or floor action recorded since introduction
---

The bill would require any contractor delivering AI-utilizing goods or services to the Department of Defense to produce and maintain an "AI functional bill of materials" — a machine-readable inventory of the software (models, dependencies, security controls, access history, performance metrics), data (training/inference datasets, lineage, provenance, country of origin), and hardware (GPUs/TPUs, storage, networking, cloud deployment boundaries) underlying the system, deliverable to DoD within 48 hours of a request. DoD may not enter, renew, or extend a covered contract absent a compliant AI-BOM. The Secretary of Defense must revise the DFARS and issue implementing guidance within 180 days, and report to the Armed Services Committees within a year on implementation. Sen. Slotkin has separately secured a similar AI-BOM requirement's inclusion in the FY2027 NDAA, which is likely the more probable enactment path for this policy.
