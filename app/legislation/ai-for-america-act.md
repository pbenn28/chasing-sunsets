---
title: AI for America Act
short_name: AI for America Act
bill_numbers:
- H.R. 6304
congress: 119
topic: Government Use & Procurement
status: introduced
chamber_origin: House
introduced_date: '2025-11-25'
last_action: Referred to the House Committees on Science, Space, and Technology, and Energy and Commerce
last_action_date: '2025-11-25'
sponsors:
- Rep. Jennifer Kiggans (R-VA)
cosponsor_count: 2
committees:
- House Science, Space, and Technology
- House Energy and Commerce
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
    R: 0.90
    D: 0.20
    E_f: 0.20
    P: 0.40
  likelihood:
    p_committee: 0.10
    p_enact: 0.02
    basis: "govtrack_corroborated"
  rationale:
    A: "Read against the full engrossed bill text (GPO PDF): every obligation runs to a federal agency (OSTP, NIST), not to AI developers. OSTP must submit a biennial 'Action Plan' addressing leadership, workforce, and partnerships with DOE/NASA/NIST/NSF; OSTP (with Energy/HHS/Transportation) must identify — not repeal — regulatory barriers to AI adoption; NIST must report on measures to detect security risks and ideological bias in AI. None of this is a disclosure, audit, incident-reporting, or procurement condition binding a developer, so A is 0 rather than landing on the ladder at all."
    B: "The full text contains no mention of state law, state authority, or preemption anywhere — confirmed directly from the primary bill text, not inferred from a summary. A stays at 0, far below the +2 threshold that would trigger the implicit-preemption floor, so B is correctly silent."
    C: "Three time-bound reporting mandates to Congress (an Action Plan due by July 31, 2027 with biennial updates, a one-year regulatory-barrier identification report, and a one-year NIST report) — studies and advisory reporting with real deadlines, not a new agency, evaluation body, or enforcement authority, matching the 1.0 rung."
    D: "Rhetorically framed around U.S.-China AI competitiveness, but contains no export-control, chip-access, or allied-coordination mechanism — framing without a lever, so D stays at 0."
    E_consumer: "No deepfake, NCII, companion-bot, algorithmic-discrimination, or election-integrity content."
    F: "DOE and NASA are named only as prospective partners within the OSTP Action Plan's scope — the bill does not itself allocate energy, compute, or siting authority, so it doesn't touch axis F. Corrected against a since-debunked secondary-source claim of a $100M/year NSF research hub, which does not appear anywhere in the actual bill text."
    R: "A federal bill with no sector carve-outs — its three reporting mandates apply across the whole AI landscape OSTP/NIST are asked to survey, even though the substance is thin."
    Depth: "Depth = max(|A|,|B|,|C|,|F|,E)/5 = max(0,0,1,0,0)/5 = 0.20, driven entirely by the modest C (reporting-study) score since every other axis is 0."
    E_f: "Reporting mandates to Congress with no rulemaking directive, civil penalty, or private right of action attached — closer to a study-only obligation than an enforceable one, so E_f sits at the low end rather than the 0.4 'obligation with no stated penalty' rung."
    P: "Three self-contained, sector-specific reporting mandates (AI strategy, regulatory-barrier identification, security/bias detection) rather than a first-in-nation template or a permanent institution."
    likelihood: "Single-sponsor bill referred to two House committees (Science, Space, and Technology; Energy and Commerce) with only 2 cosponsors reported and no hearing or markup identified in the ~9.5 months since introduction as of September 2026 — a June 2026 Science Committee markup covered ten other bill numbers but not H.R. 6304. GovTrack's own prognosis (per search snippet, direct fetch blocked) puts this at roughly 1% chance of enactment and roughly 4% chance of clearing committee, which this estimate adopts as the anchor, rounded slightly for the bipartisan-adjacent framing (aligned with the administration's AI Action Plan messaging) without any concrete legislative movement to offset the base rate for a two-committee-referral messaging bill with no funding and no operative mandate on anyone outside the executive branch."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- national strategy
- OSTP
- NIST
- deregulation
sources:
- label: Congress.gov (full text PDF)
  url: https://www.congress.gov/119/bills/hr6304/BILLS-119hr6304ih.pdf
- label: Rep. Kiggans press release
  url: https://kiggans.house.gov/2025/11/25/kiggans-leads-bill-to-strengthen-u-s-leadership-in-ai/
- label: AIP/FYI bill tracker
  url: https://www.aip.org/fyi/federal-science-bill-tracker/119th/house-of-representatives-6304
summary: Directs OSTP to produce a national AI strategy and identify regulatory barriers, and NIST to report on AI security/bias detection measures; no funding or developer-facing mandates.
timeline:
- date: '2025-11-25'
  event: Introduced in the House by Rep. Jennifer Kiggans (R-VA); referred to House Science, Space, and Technology and Energy and Commerce
- date: '2026-09-09'
  event: Verified against full engrossed text via GPO PDF — no committee markup or hearing identified; corrected a secondary-source claim of a nonexistent $100M NSF research-hub appropriation
---

The bill would direct the Office of Science and Technology Policy to submit a biennial "Action Plan" addressing AI leadership, workforce development, and public-private partnerships with DOE, NASA, NIST, and NSF; direct OSTP, with the Departments of Energy, Health and Human Services, and Transportation, to identify (not repeal) regulatory barriers to AI adoption in healthcare, research, and transportation; and direct NIST to report on measures to detect security risks and ideological bias in AI systems. All obligations run to federal agencies — the bill authorizes no funding and imposes no conduct standard, disclosure requirement, or procurement condition on private AI developers.
