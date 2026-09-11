---
title: Guarding the U.S. against Adversarial Robotics Dominance Act of 2026 (GUARD Act)
short_name: GUARD Act (Robotics)
bill_numbers:
- H.R. 9129
congress: 119
topic: Chips & National Security
status: introduced
chamber_origin: House
introduced_date: '2026-06-03'
last_action: Introduced and referred to the House Committee on Energy and Commerce
last_action_date: '2026-06-03'
sponsors:
- Rep. John Moolenaar (R-MI)
- Rep. Jay Obernolte (R-CA)
- Rep. Jennifer McClellan (D-VA)
cosponsor_count: 2
committees:
- House Energy and Commerce
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 1.0
    D: 4.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.5
    D: 0.20
    E_f: 0.60
    P: 0.60
  likelihood:
    p_committee: 0.40
    p_enact: 0.14
    basis: "base_rate_adjusted"
  rationale:
    A: "Binds robotics hardware/communications-equipment makers and importers, not AI model developers — the review and Covered List mechanism governs physical humanoid/quadruped robot imports and their communications equipment, not the training or deployment of AI models themselves. 0."
    B: "No preemption or savings-clause language identified in press coverage; this is a national-security import-control scheme administered through FCC/national-security-agency review, not an AI-developer regulatory scheme, so the implicit-preemption floor doesn't apply (A=0, well under the +2 trigger)."
    C: "Directs national security agencies to conduct a review process of foreign-adversary humanoid/quadruped robots on a one-year timeline, with automatic FCC Covered List placement as a default outcome if review isn't completed — a real, dated review mandate with a reporting deadline, but not a new standing agency, database, or dedicated evaluation body of the kind that would score higher. +1 (studies/reviews with real deadlines) rather than +2/+3, since the mechanism reuses the existing FCC Covered List framework rather than building new government capacity."
    D: "The bill's entire substance is external/geopolitical: it directs national-security review of humanoid and quadruped robots (and their communications equipment/control software) produced by entities connected to countries of concern, and adds them to the FCC's Covered List — which functions as an import prohibition — either following an adverse determination or automatically after one year if no review is completed. This is a hard control with real bite (Covered List placement bars the equipment from the U.S. market/federal procurement, mirroring the existing Huawei/ZTE telecom precedent), but it's an import-side prohibition rather than a location-verification-plus-criminal-penalty regime for products already in the field, so it lands at +4 (new restriction on advanced-technology access) rather than the +5 tier reserved for hard controls with location-verification/KYC-on-compute and criminal diversion penalties."
    E_consumer: "No deepfake, NCII, companion-bot, algorithmic-discrimination, or election-integrity content. Robots are physical hardware subject to an import/national-security review, not AI systems interacting with consumers in the sense this axis measures — 0."
    F: "No domestic data-center, permitting, interconnection, siting, or ratepayer provisions — this is an import-control bill aimed at foreign-made hardware, not a domestic compute-buildout constraint."
    R: "Covers humanoid and quadruped robots (and associated communications equipment/control software) from entities headquartered in, controlled by, or affiliated with countries of concern — a meaningful but still narrow slice of the broader robotics/AI-hardware import universe, since it's confined to two specific robot form factors rather than robotics or AI hardware generally."
    Depth: "Depth = max(|A|,|B|,|C|,|F|,E)/5 excludes axis D by design. With A=0, B=0, C=1, F=0, E=0, the binding component is C=1, giving Depth = 1/5 = 0.20 — understating the bill's real weight, which sits almost entirely in axis D (+4), excluded from Depth by the same logic that excludes it from the safety composite."
    E_f: "Enforcement runs through the FCC Covered List mechanism (a federal agency action with real market-access consequences — Covered List equipment can't receive FCC equipment authorization, effectively barring U.S. sale), closer to 'agency rulemaking + civil penalties' than a purely voluntary framework, though there's no private right of action."
    P: "Extends an established precedent — the FCC Covered List framework built for Huawei/ZTE telecom equipment — into an entirely new hardware category (humanoid/quadruped robotics), which is a first-in-kind application likely to be copied for other adversarial-hardware categories (drones, other robotics form factors) as Congress works through the China Select Committee's broader hardware-security agenda."
    likelihood: "No GovTrack numeric prognosis found for H.R. 9129. Introduced June 2026 with bipartisan sponsorship (2 Republicans, 1 Democrat) and Select Committee on China backing, plus industry endorsements (AUVSI, FDD) tracked on the Committee's own endorsements page as of July 2026 — signals of momentum-building typical of bills still being staged for a legislative vehicle rather than bills with an active floor path. No markup or committee action reported as of early September 2026, roughly three months after introduction. Scored toward the lower-middle of the base rate for single-committee-referred bills with multiple organizational endorsements but no scheduled markup."
  confidence: low
  text_source: summary
  scored_at: "2026-09-09"
tags:
- robotics
- humanoid robots
- FCC Covered List
- China
- national security
- import controls
sources:
- label: Congress.gov — H.R. 9129
  url: https://www.congress.gov/bill/119th-congress/house-bill/9129
- label: "Select Committee on the CCP — Moolenaar, Obernolte, McClellan press release"
  url: https://chinaselectcommittee.house.gov/media/press-releases/moolenaar-obernolte-mcclellan-introduce-legislation-to-ban-dangerous-chinese-robots
- label: "Rep. McClellan press release"
  url: https://mcclellan.house.gov/media/press-releases/mcclellan-moolenaar-obernolte-introduce-legislation-ban-dangerous
- label: "DroneLife — Congress Introduces GUARD Act, Extending FCC Covered List Framework to Robotics"
  url: https://dronelife.com/2026/06/04/congress-introduces-guard-act-extending-fcc-covered-list-framework-to-robotics/
- label: "Select Committee on the CCP — GUARD Act Endorsements"
  url: https://chinaselectcommittee.house.gov/guard-act-endorsements
summary: Would direct national-security review of foreign-adversary humanoid and quadruped robots and add them to the FCC's Covered List (an effective import ban) if found to pose a security risk, or automatically after one year if unreviewed.
timeline:
- date: '2026-06-03'
  event: H.R. 9129 introduced by Rep. Moolenaar (with Obernolte, McClellan); referred to House Energy and Commerce
- date: '2026-07-20'
  event: Select Committee on the CCP endorsements page updated with industry backers including AUVSI and FDD
---

**Naming collision note:** this bill's short title, "GUARD Act," is shared by two other, unrelated bills already or concurrently tracked on this page. The already-tracked GUARD Act (S. 3062 / H.R. 8623, "Guidelines for User Age-verification and Responsible Dialogue Act," Sens. Hawley/Blumenthal) is a chatbot age-verification bill with no relationship to this one. A third bill, also called the GUARD Act (H.R. 5466 / S. 3454, a university-research-security bill), is unrelated as well. To avoid collision, this bill is filed under the slug `guard-act-robotics.md`; the acronym "GUARD" here stands for **G**uarding the **U**.S. against **A**dversarial **R**obotics **D**ominance.

H.R. 9129 directs federal national-security agencies to evaluate humanoid and quadruped robots — along with their communications equipment, control software, and connectivity systems — produced by entities headquartered in, controlled by, or affiliated with "countries of concern" (principally China), including subsidiaries, joint ventures, and firms in technology-sharing arrangements with those entities. Reviewed products found to pose an unacceptable national-security risk are added to the FCC's Covered List, the same mechanism previously used to bar Huawei and ZTE telecom equipment from the U.S. market. Products that are not reviewed within one year are automatically added to the Covered List by default, shifting the burden toward exclusion rather than continued market access absent a completed review.

The sponsors argue that humanoid and quadruped robots built by Chinese firms could contain backdoors exploitable for espionage or sabotage as the hardware proliferates into U.S. homes, warehouses, and critical infrastructure, and that extending the existing telecom-equipment security framework to robotics closes a gap before that proliferation happens at scale. The bill has drawn endorsements from industry and national-security groups including AUVSI and the Foundation for Defense of Democracies.
