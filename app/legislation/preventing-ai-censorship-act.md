---
title: Preventing AI Censorship Act
short_name: Preventing AI Censorship Act
bill_numbers:
- H.R. 9279
congress: 119
topic: Government Use & Procurement
status: introduced
chamber_origin: House
introduced_date: '2026-06-11'
last_action: Referred to the House Committee on the Judiciary
last_action_date: '2026-06-11'
sponsors:
- Rep. Harriet Hageman (R-WY)
cosponsor_count: 0
committees:
- House Judiciary
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 3.0
  impact_components:
    R: 0.30
    D: 0.60
    E_f: 1.00
    P: 0.40
  likelihood:
    p_committee: 0.15
    p_enact: 0.03
    basis: "base_rate_heuristic_no_live_lookup"
  rationale:
    A: "The obligation runs against individual federal employees who coerce or induce an AI provider into viewpoint-based censorship — the AI provider is the object of the coercion, not the regulated party, and the bill places no disclosure, audit, reporting, or other conduct standard on AI developers themselves. Guardrail applied: this is a domain-general government-accountability/First Amendment mechanism that happens to be triggered by AI-related conduct, not an AI-governance obligation on developers, so it scores 0 rather than landing anywhere on the A ladder."
    B: "No state-law or state-AI-regulation language anywhere in the bill; it binds federal employees only. A ≪ +2, so the implicit-preemption floor does not apply."
    C: "Creates a private right of action adjudicated in ordinary federal court, not a new agency, evaluation body, incident-reporting flow, or enforcement staffing at an existing regulator — courts, not the executive branch, do the enforcing here."
    D: "No export-control or geopolitical-competition content."
    E_consumer: "A genuine private right of action with damages and fee-shifting for citizens harmed by federal-employee coercion of AI providers into viewpoint-based suppression, denial of access, or covert data collection — a real remedy, not just labeling. Capped below the 5 rung (reserved for broad, multi-sector PRAs like algorithmic-discrimination bills spanning housing/employment/healthcare/credit) because this PRA is scoped to a single fact pattern (federal-employee coercion of AI providers) and a single defendant class (federal employees), so it lands at 3, matching the 'criminal liability for specific AI-enabled conduct' rung in real-world scope even though the remedy is civil rather than criminal."
    F: "No data-center, permitting, siting, or energy content."
    R: "Targets a narrow slice of the AI landscape: citizens harmed specifically by federal employees pressuring AI providers on viewpoint grounds. It doesn't reach ordinary consumer-facing AI harms, frontier developers' general conduct, or state/local actors at all, so R sits well below what a broad consumer-protection or frontier-developer bill would score."
    Depth: "Depth = max(|A|,|B|,|C|,|F|,E)/5 = max(0,0,0,0,3)/5 = 0.60, driven entirely by the E_consumer private-right-of-action mechanism since every composite-feeding axis is 0."
    E_f: "A private right of action with damages, fee-shifting for prevailing plaintiffs, and an explicit rule-of-construction preserving injunctive relief and other remedies — the strongest enforceability rung available."
    P: "A sector-specific, self-contained accountability mechanism (federal-employee liability for AI-coercion) rather than a first-in-nation framework likely to be copied by states, or a permanent new institution/preemption ceiling."
    likelihood: "Introduced by a majority-party member with House Judiciary referral only, but no cosponsors identified, no committee markup or hearing found as of research (September 2026), and no Senate companion. GovTrack's own page could not be fetched (blocked to automated access), so no external prognosis anchor is available; this estimate rests on base rates for single-sponsor, single-committee messaging bills addressing a live political grievance (federal 'jawboning' of AI providers, echoing Missouri v. Biden-style disputes) — such bills sometimes pass the House on a party-line or near-party-line vote when floor time is found, but rarely see Senate action without a companion, and this one has neither cosponsors nor a companion yet, so both probabilities are set low."
  confidence: low
  text_source: summary
  scored_at: "2026-09-09"
tags:
- first amendment
- federal employees
- private right of action
- censorship
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/9279
- label: Rep. Hageman press release
  url: https://hageman.house.gov/media/press-releases/rep-hageman-introduces-bill-hold-federal-employees-accountable-ai-censorship
- label: FedSmith coverage
  url: https://www.fedsmith.com/2026/06/13/new-bill-would-let-americans-sue-federal-employees-for-ai-censorship/
summary: Creates a private right of action letting citizens sue federal employees who coerce AI providers into viewpoint-based censorship of AI outputs.
timeline:
- date: '2026-06-11'
  event: Introduced in the House by Rep. Harriet Hageman (R-WY); referred to House Judiciary
- date: '2026-09-09'
  event: Verified via sponsor press release and secondary coverage; direct congress.gov and GovTrack fetches blocked to automated access, so text_source is summary and confidence is low pending full-text confirmation
---

The bill would create a private right of action allowing American citizens to sue federal employees, in their individual capacity, who coerce, compel, direct, induce, or encourage an AI provider to suppress or alter AI outputs based on viewpoint, ideology, partisan affiliation, or religious belief, or to deny/degrade access or covertly collect user data for that purpose. Plaintiffs may recover damages and reasonable attorney's fees, and the bill preserves the right to also seek injunctive relief. The obligation runs against federal employees, not against AI companies, which are the object of the alleged coercion rather than a regulated party. No cosponsors or Senate companion had been identified as of this scoring pass.
