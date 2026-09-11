---
title: Cloud Security Act
short_name: Cloud Security Act
bill_numbers:
- H.R. 9546
congress: 119
topic: Chips & National Security
status: introduced
chamber_origin: House
introduced_date: '2026-06-26'
last_action: Introduced and referred to committee; no markup or floor action reported as of early September 2026
last_action_date: '2026-06-26'
sponsors:
- Rep. Josh Gottheimer (D-NJ)
- Rep. John Moolenaar (R-MI)
cosponsor_count: 1
committees:
- House Judiciary
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 0.5
    D: 3.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.6
    D: 0.10
    E_f: 0.2
    P: 0.60
  likelihood:
    p_committee: 0.35
    p_enact: 0.10
    basis: "base_rate_adjusted"
  rationale:
    A: "Binds cloud infrastructure providers (AWS, Azure, Google Cloud), not AI model developers or trainers — it changes what providers are legally permitted to disclose to the government about customer use, not any obligation on model training or deployment. 0."
    B: "No preemption or savings-clause language; amending the federal Stored Communications Act to permit (not require) voluntary disclosure doesn't establish an AI-developer regulatory scheme, so the implicit-preemption floor doesn't apply (A=0, well under the +2 trigger)."
    C: "The bill creates a legal safe harbor for cloud providers to voluntarily notify Commerce of suspected export-control evasion via chip rental — this is a permissive channel, not a mandatory standing reporting requirement into a database, and there's no new enforcement staffing or agency authority. Scored above 0 (a bare 0 would be reserved for bills with no capacity content at all) but well below the +3 'standing information flows' tier because reporting is voluntary and case-by-case, not mandatory; +0.5 reflects a modest, permissive capacity add."
    D: "Directly targets a chip-export-control enforcement gap: foreign adversaries renting time on export-restricted AI chips through U.S. cloud providers rather than buying the hardware outright, which sidesteps existing chip export controls entirely. The mechanism itself (amending the Stored Communications Act to enable voluntary disclosure to Commerce) is reporting-facilitation rather than a hard mandate — no location verification, no KYC-on-compute requirement, no criminal penalty for cloud providers who don't report. That places it at the 'BIS enforcement resourcing, mandatory export reporting' tier's lower edge — scored +3 rather than +4/+5 because disclosure remains voluntary (a legal permission, not an obligation), so this is meaningfully weaker than a hard-controls regime like the Chip Security Act or MATCH Act."
    E_consumer: "No deepfake, NCII, companion-bot, algorithmic-discrimination, or election-integrity content — a cloud/export-control bill with no consumer-facing provisions."
    F: "No data-center siting, permitting, interconnection, or ratepayer provisions — this concerns who may access compute remotely and what providers may disclose, not domestic buildout of compute capacity."
    R: "Covers major U.S. cloud infrastructure providers as the practical target class (hyperscalers, since only large-scale cloud compute is realistically relevant to advanced-AI-chip rental by state adversaries) — likely captures the great majority of chip-rental exposure via AWS/Azure/Google Cloud/similar, but discounted from 1.0 because the bill doesn't establish a comprehensive rental-access control regime the way the (separately enacted, House-passed) Remote Access Security Act does — this bill is narrower, addressing only the cloud provider's legal ability to report, not a ban or licensing regime on the rental itself."
    Depth: "Recomputed after the frontier/systemic-risk guardrail correction — now driven by axis C (governance capacity) at 0.5/5."
    E_f: "No civil penalty, no mandatory disclosure duty, and no private right of action — this is a voluntary permission structure (a safe harbor), squarely at the 'voluntary' rung rather than 'obligation with no stated penalty,' since providers face no obligation to report at all, only permission to do so without SCA liability."
    P: "Narrowly sector-specific (cloud-provider disclosure permissions layered onto chip export enforcement) and self-contained — it doesn't create a new institution or a preemption ceiling, and isn't yet established as a template other legislation is copying, though it complements a growing family of cloud/remote-access export-control bills (Remote Access Security Act, H.R. 2683, already House-passed) addressing the same loophole from a different angle."
    likelihood: "No GovTrack numeric prognosis found for H.R. 9546. Introduced late June 2026 with only its two lead sponsors listed as backers in press coverage (no broader cosponsor list surfaced), and no markup or committee action reported as of Sept. 2026 — roughly ten weeks with no visible movement. Base-rated as a lower-profile bill relative to the Chip Security Act/MATCH Act/AI OVERWATCH package, which has active NDAA-vehicle attention; this bill has not been reported as part of that bundle. p_committee and p_enact set toward the low end for a two-sponsor, committee-stalled bill in a crowded chip-export-control legislative field, with some upward adjustment for bipartisan (D-NJ/R-MI) sponsorship and Select Committee on China backing."
  confidence: low
  text_source: summary
  scored_at: "2026-09-09"
tags:
- chip exports
- cloud computing
- China
- export controls
- Stored Communications Act
sources:
- label: Congress.gov — H.R. 9546
  url: https://www.congress.gov/bill/119th-congress/house-bill/9546
- label: "Rep. Gottheimer press release"
  url: https://gottheimer.house.gov/posts/release-gottheimer-moolenaar-introduce-bipartisan-bill-to-close-loophole-in-advanced-ai-chip-export-controls
- label: "Select Committee on the CCP press release"
  url: https://chinaselectcommittee.house.gov/media/press-releases/moolenaar-gottheimer-lead-bipartisan-legislation-to-close-loophole-in-advanced-ai-chip-export-controls
- label: "Axios — Gottheimer, Moolenaar roll out AI cloud security bill"
  url: https://www.axios.com/2026/06/26/gottheimer-moolenaar-ai-cloud-security-bill
summary: Would amend the Stored Communications Act to let U.S. cloud providers voluntarily notify Commerce when foreign entities appear to be renting access to export-restricted AI chips to evade export controls.
timeline:
- date: '2026-06-26'
  event: H.R. 9546 introduced by Reps. Gottheimer and Moolenaar
---

The Cloud Security Act targets a specific gap in chip export enforcement: an adversary doesn't need to buy or own an export-restricted advanced AI chip if it can simply rent compute time on one through a U.S. cloud provider like AWS, Microsoft Azure, or Google Cloud — accessing the same computing power without ever taking ownership of, or importing, the hardware. Current export controls restrict the sale of advanced AI chips to countries of concern but don't clearly address rental/remote access through domestic cloud infrastructure.

The bill's mechanism is narrow and permissive rather than a hard mandate: it amends the Stored Communications Act — which currently bars cloud providers from voluntarily disclosing the contents of customer communications to the government — to give providers explicit legal cover to notify the Commerce Department when they suspect a customer is using their cloud services to evade AI chip export controls. It does not create a reporting *requirement*, a licensing regime for compute rental, or new penalties for providers who choose not to report.

**Distinct related bill:** this should not be confused with the Remote Access Security Act (H.R. 2683 / S. 3519), a separate, earlier bill that the House passed 369-22 in January 2026, which extends export-control authority itself to cover remote/rental access to controlled technology. The Cloud Security Act instead solves a narrower, complementary problem — clearing the legal path for providers to report suspected evasion once it's flagged — rather than creating the underlying rental-access control regime.

Note on sourcing: congress.gov blocked automated fetches (403) for this bill during scoring, so the committee referral above (House Judiciary, the customary committee for Stored Communications Act amendments) is inferred rather than independently confirmed, and the score rests on press coverage rather than the bill's official text or status page.
