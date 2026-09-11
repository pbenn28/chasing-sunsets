---
title: Data Center Tax Accountability and Disclosure Act of 2026
short_name: Data Center Tax Accountability and Disclosure Act
bill_numbers:
- S. 5054
congress: 119
topic: Data Centers & Energy
status: committee
chamber_origin: Senate
introduced_date: '2026-07-21'
last_action: Read twice and referred to the Senate Committee on Finance
last_action_date: '2026-07-21'
sponsors:
- Sen. Mark Warner (D-VA)
cosponsor_count: 0
committees:
- Senate Finance
scoring:
  axes:
    A: 0.0
    B: -1.0
    C: 0.0
    D: 0.0
    F: 1.5
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.90
    D: 0.30
    E_f: 0.80
    P: 0.60
  likelihood:
    p_committee: 0.02
    p_enact: 0.00
    basis: "govtrack_corroborated"
  rationale:
    A: "Binds data-center operators and their utility/water-authority counterparties, not developers of AI systems, and imposes no standard on training or deploying a model — this is an input-side disclosure-and-tax-conditioning regime, so per the conduct-vs-input-chokepoint guardrail it belongs on F, not A."
    B: "Full text voids and preempts state contract law where it would otherwise make an NDA or confidentiality clause enforceable against the Act's disclosure mandate — but this is a narrow, domain-general contract-enforceability override aimed at unblocking disclosure to regulators, not a constraint on states' authority to regulate AI development or deployment. Per the domain-general-mechanism guardrail this caps at the ±1 ceiling; scored −1 (the same value the implicit-preemption floor would impose by default) because it does override state law in a real, if narrow, channel, and states are also given an explicit opt-in role to receive disclosures and enforce independently, which cuts against treating this as any more preemptive than that ceiling."
    C: "DOE and EPA are directed to publish disclosed data annually, but this is a publication duty riding on operator self-reporting, not a new agency, dedicated evaluation body, or standing incident-reporting database of the kind axis C is built to capture — and in any case the object is energy/water/land-use data, not AI governance, so this scores 0."
    D: "No export-control, chip-access, or geopolitical-competition content."
    F: "Two independent input-side levers: (1) mandatory disclosure of energy, water, backup-power, and land-use data for covered data centers (25MW+), which alone would land at +1 (disclosure/reporting); (2) conditioning federal bonus depreciation for 'AI data centers' (facilities ≥20% used for AI) on LEED Gold/Platinum certification, which is cost-shifting that raises the marginal cost of qualifying for a major existing tax benefit — closer to the +2 rung (cost-shifting that materially raises marginal cost of capacity) for the AI-specific subset of facilities. Blending a +1 disclosure regime covering all large data centers with a +2 tax-conditioning provision covering the AI-specific subset, weighted toward the disclosure piece since it has the broader reach, lands at +1.5."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election content."
    R: "Covers all 'covered data centers' at the 25MW+ threshold nationwide for disclosure, and specifically AI data centers (≥20% AI use) for the depreciation condition — thresholds that are low enough to capture nearly the entire hyperscale/AI buildout wave the bill is aimed at, so R is high within the data-center-facing tag class."
    Depth: "max(|A|=0, |B|=1, |C|=0, |F|=1.5, E=0)/5 = 0.30 — driven by the F-axis buildout-cost provisions, the largest lever in the bill."
    E_f: "Backed by real, steep enforcement: civil penalties up to $50,000/day for negligent reporting failures and $100,000/day for knowing or materially misleading failures, both accruing daily — among the stronger enforceability postures in the tracker, at the 0.8 agency-rulemaking-plus-penalties band."
    P: "A national baseline disclosure standard (DOE/EPA-published, with a state opt-in enforcement layer) plus a first-of-its-kind LEED-certification condition on bonus depreciation for AI data centers specifically — a template other tax-writing committees could plausibly copy for other energy-intensive sectors, landing at 0.6 (joins/extends an established template: disclosure-to-federal-agency plus tax-conditioning are each independently familiar mechanisms, just newly combined and aimed at AI data centers) rather than 0.8, since neither piece is entirely novel in isolation."
    likelihood: "GovTrack's own modeled prognosis for S. 5054 gives it a 1% chance of passing committee and 0% chance of enactment, explicitly anchored to here. Zero cosponsors, referred only to Finance, introduced by a single senator as part of a broader AI-policy package (alongside a companion frontier-model-access bill) rather than as a bipartisan or leadership priority — consistent with a low base rate for tax bills at this stage without a House companion."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- data centers
- energy
- water
- tax
- disclosure
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/5054
summary: Would require large AI data centers to disclose energy, water, and land-use data and would condition federal bonus depreciation for AI data centers on meeting LEED Gold/Platinum or equivalent sustainability standards.
timeline:
- date: '2026-07-21'
  event: Introduced and referred to Senate Finance
---

The Data Center Tax Accountability and Disclosure Act of 2026 would require "covered data centers" (25 megawatts of power demand or more) to disclose water usage, electricity usage, backup power arrangements, and land-use/setback information to the Department of Energy and the Environmental Protection Agency — new facilities before beginning operations, existing facilities within 180 days of enactment and annually thereafter — with DOE and EPA required to publish the disclosed data. States could elect to receive the same disclosures directly and enforce independently. The bill would also generally deny 100% federal bonus depreciation for "AI data centers" (facilities at least 20% used for developing or operating AI) unless the facility obtains LEED Gold or Platinum certification or an approved equivalent sustainability standard. It voids nondisclosure and confidentiality agreements — and preempts state contract law — to the extent they would otherwise block a utility, water authority, landlord, or local government from making a disclosure required under the Act. Civil penalties reach $50,000 per day for negligent reporting failures and $100,000 per day for knowing or materially misleading ones.
