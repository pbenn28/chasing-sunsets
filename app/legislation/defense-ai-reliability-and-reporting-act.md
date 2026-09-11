---
title: Defense AI Reliability and Reporting Act
short_name: Defense AI Reliability and Reporting Act
bill_numbers:
- H.R. 10189
congress: 119
topic: Government Use & Procurement
status: introduced
chamber_origin: House
introduced_date: '2026-08-31'
last_action: Referred to the House Committee on Armed Services
last_action_date: '2026-08-31'
sponsors:
- Rep. Sara Jacobs (D-CA)
- Rep. Nathaniel Moran (R-TX)
- Rep. George Whitesides (D-CA)
cosponsor_count: 2
committees:
- House Armed Services
scoring:
  axes:
    A: 2.0
    B: 0.0
    C: 3.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.5
    D: 0.60
    E_f: 0.40
    P: 0.60
  likelihood:
    p_committee: 0.30
    p_enact: 0.10
    basis: "base_rate_adjusted"
  rationale:
    A: "Unlike the tax bills in this batch, this mechanism genuinely governs AI: new 10 U.S.C. 2224b requires DoD to build a standing, department-wide program for reporting, tracking, analysis, and remediation of 'covered AI incidents' and 'covered AI vulnerabilities' — defined expansively to include a system operating outside safety/legal/mission guardrails, failing to respond to a disengage command, or 'rais[ing] concerns regarding system control and autonomy' (Sec. 2, new (j)(2)). This is a mandated process with real teeth: Department-wide incidents trigger a documented corrective action plan and mandatory validation of mitigation *before continued operational use* (new (f)(2)) — a functional deployment restriction tied to the incident-reporting finding. That lands squarely at the '+2: mandated process with enforcement — incident reporting... whistleblower protection' rung; it doesn't reach +3 because there's no outside pre-deployment gate (no independent verifier/certifier required before initial fielding), only post-hoc corrective action tied to incidents already found."
    B: "No preemption or savings-clause language anywhere in the text, but this bill governs only DoD's internal AI systems and does not establish a generally-applicable federal regulatory scheme over private AI development — so the implicit-preemption floor's trigger condition ('establishes a federal regulatory scheme' governing AI generally, with A >= +2) is a closer call than usual given A=2.0. On balance this is scored 0 rather than -1: the regime binds only the federal government's own military AI systems (akin to a procurement/internal-operations rule), not private developers or deployers whose conduct states might otherwise wish to regulate, so it does not displace any plausible field of state AI regulation the way a private-sector conduct standard would."
    C: "New (d) requires the Secretary to designate an official who receives and standardizes reports, conducts trend analysis, and issues guidance/alerts; new (i) requires annual unclassified reports to the congressional defense committees for 2027-2031 with incident counts, trends, and detailed casualty-incident narratives. This is a standing, department-wide information flow into a designated oversight function with recurring statutory deadlines — the '+3: standing information flows, mandatory incident reporting into a government database' rung, since it creates an ongoing tracking/reporting infrastructure rather than a one-off study."
    D: "No export control, chip access, or foreign-adversary content — this is purely a domestic DoD internal-process bill."
    F: "No compute, energy, permitting, or siting content."
    E_consumer: "No consumer-facing content — the bill governs DoD's internal use of AI systems, not products or services reaching the public."
    R: "Scored as a developer-facing-style bill but one whose target universe is narrow by design: it reaches only AI systems developed, tested, procured, fielded, or operated within the Department of Defense, not the frontier AI industry generally or the government's AI use as a whole. R=0.5 reflects that within its own (DoD-AI) universe coverage is comprehensive, but that universe itself is a small slice of AI activity."
    Depth: "max(|A|,|B|,|C|,|F|,E)/5 = max(2.0, 0, 3.0, 0, 0)/5 = 0.60. Meaningful depth driven by the incident-reporting-with-enforcement (A) and standing-reporting-infrastructure (C) provisions."
    E_f: "The corrective-action/validation-before-continued-use requirement (new (f)(2)) and whistleblower-style retaliation protection (new (g)(2)) are administered internally by DoD with no civil penalties, AG enforcement, or private right of action — an obligation with process consequences (can't keep operating without validated mitigation) but no stated monetary or legal penalty, landing at 0.4."
    P: "Extends an established legislative pattern — DoD/NDAA-style AI incident-reporting and testing provisions have appeared in prior defense authorization contexts — into a permanent, standing statutory program (new 10 U.S.C. 2224b) rather than a one-off pilot; scored at 0.6 (joins/extends an established template) rather than 0.8, since AI incident-reporting mandates for military systems are not a first-in-nation novelty at this point."
    likelihood: "Introduced 2026-08-31 with bipartisan original cosponsors (Whitesides, D-CA; Moran, R-TX) and referred to House Armed Services; no committee markup yet as of this scoring pass, and it is very recently introduced (just over a week old). GovTrack does not yet show a modeled prognosis for this bill. Base-rate adjustment: standalone member bills referred to Armed Services rarely advance on their own, but DoD AI-reliability/incident-reporting provisions of this type are a strong candidate for insertion into the annual NDAA, which is the more likely enactment vehicle — p_enact is set modestly above a typical standalone-bill base rate to reflect that possibility, while p_committee reflects the low odds of this specific bill number getting an independent markup before any NDAA cutoff."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- defense
- procurement
- incident reporting
- national security
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/10189
- label: GovInfo (Introduced in House, 2026-08-31)
  url: https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr10189ih.xml
- label: Sponsor press release
  url: https://sarajacobs.house.gov/news/press-releases/rep-sara-jacobs-introduces-bipartisan-legislation-to-address-ai-weaknesses-and-failures-at-pentagon
summary: Would direct the Secretary of Defense to establish a department-wide program for reporting, tracking, and remediating AI incidents and vulnerabilities across DoD's development, testing, procurement, and operational use of AI systems.
timeline:
- date: '2026-08-31'
  event: Introduced in the House by Rep. Jacobs with Reps. Moran and Whitesides; referred to House Armed Services
---

The bill would add a new section 2224b to title 10, U.S. Code, directing the Secretary of Defense to establish a centralized, department-wide program for reporting, tracking, analysis, and remediation of "covered AI incidents" and "covered AI vulnerabilities" arising anywhere in DoD's development, testing, procurement, fielding, or operation of AI systems. Covered incidents are defined broadly — unintended operational/safety/security harm, operating outside authorized guardrails, failing to respond to a disengage command, or raising "concerns regarding system control and autonomy." A designated official receives and standardizes reports and conducts trend analysis; department-wide incidents require a documented corrective action plan and validated mitigation before continued operational use. The program must include a protected, non-punitive disclosure process for service members, civilian employees, contractors, and subcontractors, with anti-retaliation protection. Annual unclassified reports (with optional classified annexes) go to the congressional defense committees from 2027 through 2031, including detailed narratives for any incident causing death or bodily harm.
