---
title: "AI Incident Reporting Act"
short_name: "AI Incident Reporting Act"
bill_numbers: ["H.R. 9477"]
congress: 119
topic: "Frontier Safety & Oversight"
status: "committee"
chamber_origin: "House"
introduced_date: "2026-06-25"
last_action: "Referred to the House Committee on Energy and Commerce"
last_action_date: "2026-06-25"
sponsors: ["Rep. Nathaniel Moran (R-TX)"]
cosponsor_count: 2
committees: ["House Energy and Commerce"]
scoring:
  axes:
    A: 2.0
    B: -1.0
    C: 3.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.85
    D: 0.60
    E_f: 0.80
    P: 0.60
  likelihood:
    p_committee: 0.14
    p_enact: 0.04
    basis: "base_rate_adjusted"
  rationale:
    A: "Developers of Commerce-designated 'covered models' must report seven categories of dangerous incidents — control-evasion/shutdown resistance, model-weight theft or exfiltration, offensive-cyber capability, autonomous AI-development self-improvement, CBRN weapons uplift, near-miss harm events, and any other Secretary-designated risk — within 7 days of discovery, with immediate notice for imminent/ongoing risk. This is a mandated process with real enforcement (Secretary investigative authority, civil penalties up to $2,000,000 per violation, per-day continuing-violation exposure, AG referral for collection/injunction) — squarely the +2 'mandated process with enforcement: incident reporting' rung. It is not pre-deployment gating (no license or audit required before release) and not government shutdown/recall authority over deployed models, so it does not reach +3 or +4."
    B: "No preemption or savings-clause language was found anywhere in the bill's full text — it is entirely silent on state authority. Because this bill scores A = +2 and establishes a federal regulatory scheme (a standing, mandatory incident-reporting regime into a federal agency, run by the Secretary of Commerce with investigative and penalty authority), the implicit-preemption floor applies: silence here is not neutral, since a comprehensive federal reporting scheme can preempt conflicting state incident-reporting or disclosure mandates by implication even with zero preemption text. B therefore floors at −1 (conflict preemption only) rather than 0, and nothing in the text supports a more negative score than that floor — there is no express field-preemption or moratorium language."
    C: "Establishes exactly the kind of standing information flow this rung is written for: mandatory incident reports flowing into the Secretary of Commerce, with a 48-hour congressional-notification trigger for the most serious incidents (routed to House/Senate leadership and the Energy and Commerce, Science, and Intelligence committee chairs) and 30-day notice for routine reports. This is a durable government capacity to observe AI behavior at the frontier, matching the +3 rung precisely — it does not go further to +4/+5 because it doesn't fund a dedicated new evaluation body or agency, just a reporting-and-investigation function inside Commerce."
    D: "No export-control or chip/compute-access content — the bill is a domestic incident-reporting mandate, not a geopolitical lever."
    E_consumer: "No deepfake, NCII, discrimination, or election-related content — the bill is scoped entirely to frontier/advanced-model developers and national-security-relevant incidents, not consumer-facing near-term harms."
    F: "No data-center, permitting, siting, or energy content."
    R: "Covered models are defined by Commerce-set capability thresholds intended to capture models posing significant national-security or public-safety risk — designed to reach essentially the frontier-model tier rather than a narrow slice, though the exact threshold is left to future agency designation rather than fixed in statute, introducing some uncertainty relative to a bright-line compute trigger."
    Depth: "Driven by the incident-reporting mandate (A) and especially the new standing information flow into Commerce (C), which is the largest of the moving axes; B's floor is a comparatively small magnitude."
    E_f: "Backed by Secretary investigative authority (orders, record demands, corrective-action requirements) and civil penalties up to $2,000,000 per violation with per-day continuing-violation exposure, enforced via AG referral for collection or injunctive relief — agency rulemaking-and-civil-penalties enforcement, not a private right of action, matching the 0.8 rung."
    P: "Would be the first standing federal early-warning system specifically for dangerous frontier-AI incidents (shutdown evasion, weight theft, CBRN uplift), joining a template other 2026 frontier-oversight bills (e.g. the FRONTIER Act) have also converged on, rather than a wholly novel, self-contained mechanism — a first-in-nation framework likely to be built on or copied by later bills."
    likelihood: "No GovTrack.us prognosis page content could be retrieved for this specific H.R. 9477 (119th Congress) as of this check, so likelihood is base-rate adjusted rather than GovTrack-corroborated. The bill has only 2 cosponsors, sits in a single committee (Energy and Commerce) with no scheduled markup roughly eleven weeks after its June 25, 2026 introduction, and has no identified Senate companion — a single-sponsor-dominated bill with modest bipartisan signal at this early stage, consistent with typical low base rates for House bills that haven't yet attracted a bipartisan cosponsor bloc or committee attention."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags: ["incident reporting", "frontier models", "federal framework", "national security"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/house-bill/9477"
  - label: "GovInfo (full text)"
    url: "https://www.govinfo.gov/app/details/BILLS-119hr9477ih"
  - label: "Sponsor press release (Rep. Moran)"
    url: "https://moran.house.gov/news/documentsingle.aspx?DocumentID=2784"
summary: "Would require developers of Commerce-designated advanced AI models to report dangerous incidents — shutdown evasion, model-weight theft, CBRN uplift, offensive-cyber capability, and autonomous self-improvement — to the Secretary of Commerce within 7 days, with expedited notice for imminent risks and 48-hour congressional notification for the most serious cases."
timeline:
  - date: "2026-06-25"
    event: "Introduced by Rep. Nathaniel Moran with 2 original cosponsors; referred to the House Energy and Commerce Committee"
---
The AI Incident Reporting Act would direct the Secretary of Commerce to designate "covered models" — AI systems meeting capability thresholds that pose significant risks to national security or public safety — and require their developers to report seven categories of dangerous incidents within 7 days of discovery, or immediately for imminent or ongoing risk of serious harm. Reportable activity includes models attempting to evade human oversight or resist shutdown, unauthorized theft or exfiltration of model weights, capabilities enabling offensive cyber operations against critical infrastructure, autonomous acceleration of AI research and development, CBRN (chemical, biological, radiological, nuclear) weapons uplift, near-miss incidents averted only by external luck rather than developer safeguards, and any other category the Secretary designates.

For the most serious incidents, Commerce must notify House and Senate leadership and relevant committee chairs (Energy and Commerce, Science, and Intelligence) within 48 hours; routine reports get a 30-day notification window. The Secretary can investigate, demand records and testimony, and order corrective action, backed by civil penalties of up to $2,000,000 per violation with each day of continuing violation counted separately, enforced through Attorney General referral. Reported information is shielded from FOIA and state disclosure laws and can't be used against a developer in unrelated civil or criminal proceedings, preserving trade-secret and privilege protections. The bill contains no preemption or state-savings-clause language at all. Introduced by Rep. Nathaniel Moran (R-TX) on June 25, 2026 with two original cosponsors, it was referred to the House Energy and Commerce Committee and has not yet received a hearing or markup.
