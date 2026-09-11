---
title: AI-Ready Bio-Data Standards Act
short_name: AI-Ready Bio-Data Standards Act
bill_numbers:
- S. 4069
- H.R. 7907
congress: 119
topic: Healthcare
status: introduced
chamber_origin: Senate
introduced_date: '2026-03-12'
last_action: Referred to committee; no further action in either chamber
last_action_date: '2026-03-12'
sponsors:
- Sen. Todd Young (R-IN)
- Rep. Ro Khanna (D-CA)
cosponsor_count: 2
committees:
- Senate Commerce, Science, and Transportation
- House Science, Space, and Technology
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
    R: 0.85
    D: 0.20        # Depth — unrelated to axes.D
    E_f: 0.40
    P: 0.40
  likelihood:
    p_committee: 0.10
    p_enact: 0.03
    basis: "govtrack_corroborated"
  rationale:
    A: "Places no obligation on private AI developers or biotech companies. The bill's scope is limited to federal agencies (NIST, USDA, DOD, DOE, NASA, NIH, NSF, etc.) and recipients of federal research funding — it directs NIST to define 'AI-ready' data and directs those agencies to adopt data-management policies for their own grant programs, not to regulate commercial AI training or deployment."
    B: "The bill is silent on state authority throughout — no preemption or savings-clause language anywhere in the full text (read in full from the GPO print, BILLS-119s4069is.pdf). It governs only federal-agency and federal-grantee conduct, so there is no state-law interaction to preempt or preserve. The implicit-preemption floor does not apply because the bill does not score A ≥ +2."
    C: "Directs NIST to produce a public inventory of existing biotech standards/datasets (1 yr), agency-specific data management policies across at least six federal science agencies (2 yrs), a 12+ member advisory group, biennial NIST/NSF test-and-evaluation, FAR revisions, annual reports to Congress, and a GAO impact report at 5 years — substantive standards-and-reporting infrastructure with real deadlines, comparable to the AI-Ready Federal Data Guidelines Act's NIST guidelines mandate, though it stops short of a funded evaluation body or mandatory incident-reporting stream into an oversight database."
    D: "No export-control, dual-use-research, or biosecurity content despite Sen. Young's role chairing the National Security Commission on Emerging Biotechnology — the bill text is purely a data-standardization and interoperability mandate, with no diversion-control or foreign-access provisions."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election-integrity content, and no individual consumer rights or disclosures — the bill only governs federal research-data practices."
    F: "No data-center, permitting, interconnection, or energy-allocation content anywhere in the bill."
    R: "A federal bill directing NIST and at least six major federal science agencies (USDA, DOD, DOE, NASA, NIH, NSF) to overhaul biological-dataset practices — near-full federal reach within the federally funded biotech-research universe, though narrower than a bill touching the entire economy, hence 0.85 rather than 0.90+."
    Depth: "The only real structural teeth are the standards/reporting mandate (axis C = 1.0); every other axis is 0, so Depth tracks that single active axis, same as comparable NIST-standards bills."
    E_f: "Federal agencies operate under fixed statutory deadlines (1-year inventory, 2-year data policies, annual and 5-year reports) with GAO and congressional oversight, but there is no civil penalty, no rulemaking with penalties, and no private right of action attached to any provision."
    P: "A 10-year sunset clause terminates the entire section, and the bill is sector-specific (federally funded biological/biotech research data) and self-contained rather than a first-in-nation framework or a new permanent institution — the sunset caps this below the 'joins an established template' rung."
    likelihood: "No GovTrack prognosis was independently located for either bill number; both remain at the referred-to-committee stage roughly six months after introduction (2026-03-12) with no markup or floor action in either chamber as of September 2026. Using historical base rates for narrow, bipartisan-but-not-leadership-prioritized data-standards bills referred to Commerce/Science committees, p_committee is set low given no scheduled markup, and p_enact lower still consistent with the pattern seen in comparable NIST-standards bills that stall without committee action within two Congresses. The bicameral, bipartisan sponsor pairing (Young-R/Luján-D in Senate; Khanna-D/Obernolte-R in House) is a modest positive signal but has not yet translated into committee movement."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- biotechnology
- NIST
- data standards
- healthcare
sources:
- label: Congress.gov (S. 4069)
  url: https://www.congress.gov/bill/119th-congress/senate-bill/4069
- label: Congress.gov (H.R. 7907)
  url: https://www.congress.gov/bill/119th-congress/house-bill/7907
- label: S. 4069 full text (GPO)
  url: https://www.congress.gov/119/bills/s4069/BILLS-119s4069is.pdf
- label: Sen. Young press release
  url: https://www.young.senate.gov/newsroom/press-releases/young-colleagues-introduce-bill-to-ensure-american-leadership-in-ai-and-biotech/
summary: Directs NIST to develop standards, definitions, and data-management frameworks so federally funded biological and biotech datasets are usable to train AI models.
timeline:
- date: '2026-03-12'
  event: Introduced in Senate (S. 4069, Sen. Young with Sen. Luján) and House (H.R. 7907, Rep. Khanna with Rep. Obernolte); referred to committee in both chambers
- date: '2026-09-10'
  event: Verified — no markup or floor action in either chamber since introduction
---

The bill directs the NIST Director to establish, within two years, definitions of "AI-ready" biological data, biomanufacturing, and biotechnology, along with data-management resources and cybersecurity frameworks so federally funded biological datasets can be used effectively to train AI models. It requires a one-year inventory of existing biotech standards and datasets, agency-specific data-management policies across USDA, DOD, DOE, NASA, NIH, NSF and other agencies, a 12-plus-member advisory group, biennial NIST/NSF testing and evaluation, Federal Acquisition Regulation revisions, and annual reports to Congress plus a five-year GAO impact report. The section sunsets ten years after enactment. It has bipartisan, bicameral sponsorship (Sen. Young with Sen. Luján; Rep. Khanna with Rep. Obernolte) but has not advanced beyond committee referral in either chamber.
