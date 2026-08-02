---
title: "FRONTIER Act (Frontier Risk Oversight, National Transparency, Independent Evaluation, and Reporting Act)"
short_name: "FRONTIER Act"
bill_numbers: ["H.R. 9925"]
congress: 119
topic: "Frontier Safety & Oversight"
status: "committee"
chamber_origin: "House"
introduced_date: "2026-07-23"
last_action: "Referred to the House Committees on Energy and Commerce and on Science, Space, and Technology"
last_action_date: "2026-07-23"
sponsors: ["Rep. Jay Obernolte (R-CA)", "Rep. Lori Trahan (D-MA)"]
cosponsor_count: 5
committees: ["House Energy and Commerce", "House Science, Space, and Technology"]
scoring:
  axes:
    A: 4.0
    B: -4.0
    C: 4.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.95
    D: 0.80
    E_f: 0.80
    P: 1.00
  likelihood:
    p_committee: 0.15
    p_enact: 0.04
    basis: "base_rate_adjusted"
  rationale:
    A: "Large developers must write, publish, and annually update a frontier AI framework and file a compliance disclosure statement with Commerce before operating a covered model at all; very large developers must also retain a licensed third-party verifier for ongoing assessment of their safety practices. On top of that, the Secretary of Commerce can issue an emergency order suspending or restricting a developer's training, deployment, or internal use of a specific model on a finding of imminent catastrophic risk, enforceable with civil penalties up to $10 million per day and criminal penalties for willful violations."
    B: "States and localities are barred from imposing any new requirement on AI developers covering frontier-model risk disclosure, third-party safety auditing, or safety-incident reporting, with no expiration date. States keep their existing authority over deployer conduct (consumer protection, civil rights, contract, criminal, and privacy law), minors' online safety, government procurement, and any law that doesn't single out AI developers specifically — but the core lane state AI-safety bills usually occupy is closed off for good."
    C: "Creates a new Under Secretary of Commerce for AI Security to run the whole regime: licensing and policing third-party verification organizations, receiving mandatory incident and risk reports, and issuing emergency orders. GAO is separately tasked with an annual public report on the health of the verification-organization market."
    D: "No export-control or chip-access provisions."
    E_consumer: "No deepfake, NCII, discrimination, or election-related content — the bill is scoped entirely to frontier developers."
    F: "No data-center, permitting, siting, or energy content."
    R: "Covers developers whose models are trained past a fixed compute threshold, which is designed to capture essentially the whole frontier-model tier rather than a narrow slice of it."
    Depth: "Driven by the frontier-conduct mandate, the preemption clause, and the new Under Secretary office, all of which push well off neutral."
    E_f: "Backed by civil penalties (up to $1 million per day for transparency violations, up to $10 million per day for violating an emergency order) pursued by the Attorney General or an opted-in state Attorney General, plus criminal penalties for willful violations of an emergency order — enforcement runs through government action rather than a private right of action."
    P: "Would stand up the first ongoing federal licensing-and-verification regime for frontier AI models, together with a durable federal ceiling on what states can require of developers in the same space — the kind of framework and preemption line later bills tend to be measured against or built on top of."
    likelihood: "A fresh bipartisan pairing introduced days before this writing, with the lead sponsor chairing the House Science Committee's Research and Technology Subcommittee — enough to plausibly reach a hearing, but still at the earliest possible stage with five cosponsors and no companion in the Senate. It's also one of several competing frontier-AI proposals moving in the same Congress, which further limits its near-term odds."
  confidence: high
  text_source: full_text
  scored_at: "2026-08-01"
tags: ["frontier models", "federal framework", "audits", "incident reporting"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/house-bill/9925"
summary: "Would create the first federal oversight regime for the most advanced AI models — audits, incident reporting, transparency requirements, and a permanent federal ceiling on state AI-safety rules for developers."
timeline:
  - date: "2026-07-23"
    event: "Introduced by Rep. Obernolte with Rep. Trahan and 4 other original cosponsors"
  - date: "2026-07-23"
    event: "Referred to the House Energy and Commerce and Science, Space, and Technology Committees"
---
The FRONTIER Act would build the first standing federal regulatory framework aimed specifically at "frontier" AI models — defined by a compute threshold (models trained using more than roughly 10^26 operations). Developers of covered models would have to publish model cards, maintain risk-management frameworks, submit to independent third-party audits, and report critical safety incidents to the government within 24 hours. A new Under Secretary of Commerce for AI Security would run the regime, including a licensing system for the third-party organizations that verify developer compliance and emergency authority to suspend a model's development or deployment if it poses an imminent catastrophic risk.

The bill also bars states from imposing their own frontier-model transparency, third-party auditing, or incident-reporting requirements on developers, with no sunset on that limit — while leaving states free to regulate how AI is deployed or used, protect minors online, and set their own procurement rules. It's a narrower, actually-introduced descendant of the sponsors' own 269-page discussion draft, the Great American AI Act, which covered similar ground on frontier governance and preemption alongside broader workforce and cybersecurity titles this bill leaves out. Obernolte chairs the House Science Committee's Research and Technology Subcommittee, giving the bill a plausible path to a hearing even this early in its life.
