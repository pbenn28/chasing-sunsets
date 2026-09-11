---
title: "Open-Source AI Leadership Act"
short_name: "Open-Source AI Leadership Act"
bill_numbers: ["H.R. 10152"]
congress: 119
topic: "Chips & National Security"
status: "committee"
chamber_origin: "House"
introduced_date: "2026-08-27"
last_action: "Forwarded by the Subcommittee on Commerce, Manufacturing, and Trade to the full House Energy and Commerce Committee by voice vote"
last_action_date: "2026-09-01"
sponsors: ["Rep. Gabe Evans (R-CO)"]
cosponsor_count: 0
committees: ["House Energy and Commerce"]
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 2.0
    D: 2.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.40
    D: 0.40
    E_f: 0.40
    P: 0.50
  likelihood:
    p_committee: 0.55
    p_enact: 0.12
    basis: "base_rate_adjusted"
  rationale:
    A: "Places no conduct standard on AI developers of any kind. It directs Commerce to designate a coordination point of contact, review existing programs, identify adoption barriers, and enter voluntary agreements/support arrangements to promote adoption of 'qualified open models' — pure capacity-building and coordination with no strings attached to any developer, and Section 4 goes further by affirmatively barring Commerce from using the Act to ban, restrict, or make any open model unavailable. This lands at 0 (studies, task forces, definitions) rather than −0.5 (capacity and money with no obligations) because no subsidy or compute grant is authorized — it is coordination and monitoring, not a financial transfer."
    B: "No state or local government mentioned anywhere in the bill; it runs entirely through the Secretary of Commerce's own coordination and reporting authority. The implicit-preemption floor does not apply because axis A scores 0, well under the +2 trigger threshold."
    C: "Establishes a standing Commerce single point of contact for open-model adoption, a monitoring framework with adoption benchmarks, and a mandatory comparative report to Congress on foreign-adversary vs. qualified open models due within 18 months of enactment and then annually for up to 10 years before sunsetting. This is more than a one-off study (rung +1) because of the recurring annual reporting cycle and dedicated coordination role, but stops short of a genuinely new evaluation body or enforcement authority (rung +4), so it lands at +2 — closer to 'enforcement staffing/new authority for an existing regulator' in substance (a standing coordination and reporting function inside Commerce) than to a one-time study."
    D: "The bill's core national-security hook is the mandatory Commerce assessment and annual public report comparing 'foreign adversary models' (from China, Russia, North Korea, Iran, per the 10 U.S.C. §4872(f) cross-reference) against U.S. qualified open models on training-data risk, infosec, supply-chain vulnerability, and national-security implications. This is squarely an assessment/coordination mechanism (rung +1 to +2) rather than a hard control — it creates no new export restriction, licensing requirement, or diversion penalty — so it's scored at the top of that assessment band given the recurring, statutorily mandated (not merely discretionary) nature of the comparative reporting."
    F: "No data-center, permitting, siting, water, or energy-allocation content."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election-integrity content; the bill is an industrial-policy and adoption-promotion measure aimed at the open-model ecosystem, not consumer-facing AI harms."
    R: "Targets the open-weight AI model ecosystem specifically (both as a class Commerce is directed to support and as the yardstick against which foreign-adversary models are compared) rather than the frontier-developer universe broadly, and its mechanisms (coordination, voluntary agreements, monitoring) reach only as far as entities that choose to engage with Commerce's support programs — a real but partial slice of the addressable AI industry."
    Depth: "max(|A|,|B|,|C|,|F|,E) / 5 = max(0, 0, 2.0, 0, 0)/5 = 0.40."
    E_f: "Obligations run against the Secretary of Commerce (report deadlines, program design) rather than against private parties, and industry participation in the adoption-support programs is voluntary — scored as an obligation with a stated deadline but no penalty structure for any private actor, above 'voluntary' but below AG- or agency-enforcement-with-penalties tiers."
    P: "A sector-specific, self-contained Commerce coordination-and-reporting program with a 10-year sunset on its comparative reporting requirement — not a permanent institution, but a plausible template other national-security-flavored AI adoption bills could copy given the current China-competition framing driving similar proposals."
    likelihood: "Confirmed advancing through committee: passed the House Energy and Commerce Subcommittee on Commerce, Manufacturing, and Trade by voice vote on 2026-09-01, forwarded to the full committee — a genuine, verified procedural advance, though not yet a full-committee markup or vote (contrary to a loose reading of 'advancing through committee' as already having cleared the full committee). Trade press (Ripon Advance, South China Morning Post, The Star/Reuters) corroborates the subcommittee voice vote and notes bipartisan engagement in markup (Rep. Trahan raised and reportedly received assurances on concerns about the Secretary's discretion) even though she is not a formal cosponsor. No GovTrack prognosis page was retrievable (direct fetch returned HTTP 403; no cached page found via search), so this estimate uses a base rate for single-sponsor House bills that clear a subcommittee by voice vote, adjusted up for the bipartisan markup dynamic and the China-competition framing that has proven popular this Congress, but down for the sole sponsorship, the pending full-committee step, and the SCMP-reported House recess ahead of the midterms narrowing the floor-time window this year."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- open source
- China
- export competitiveness
- Commerce Department
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/10152
- label: GovInfo BILLSTATUS bulk data
  url: https://www.govinfo.gov/bulkdata/BILLSTATUS/119/hr/BILLSTATUS-119hr10152.xml
- label: GovInfo bill text (introduced)
  url: https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr10152ih.xml
- label: Ripon Advance, subcommittee advance
  url: https://riponadvance.com/featured/house-subcommittee-advances-evans-open-source-ai-leadership-act/
- label: South China Morning Post
  url: https://www.scmp.com/news/us/economy-trade-business/article/3366035/congress-advances-new-bill-give-us-edge-open-source-ai-race-china
summary: Would direct the Secretary of Commerce to coordinate and promote adoption of U.S.-developed open-weight AI models, and to assess and annually report to Congress on the risks of "foreign adversary" open models from China, Russia, North Korea, and Iran compared to U.S. alternatives.
timeline:
- date: '2026-08-27'
  event: Introduced and referred to House Energy and Commerce Committee (Subcommittee on Commerce, Manufacturing, and Trade)
- date: '2026-09-01'
  event: Subcommittee markup held; forwarded to full committee by voice vote
---

The bill would direct the Secretary of Commerce to designate a single point of contact to coordinate adoption of "qualified open models" — U.S.-developed, open-weight AI models not controlled by a covered adversary nation — across industry, other federal agencies, states, and foreign partners, and to build a monitoring framework with adoption benchmarks. Separately, it requires Commerce to identify and assess risks posed by "foreign adversary models" from China, Russia, North Korea, and Iran (training-data provenance, infosec, supply-chain vulnerability, safety-feature efficacy, national-security implications) and publish a public comparative report to Congress within 18 months of enactment, then annually for up to 10 years. The bill explicitly bars the Secretary from using the Act's authority to ban, restrict, or make any open model unavailable. It passed the House Energy and Commerce Subcommittee on Commerce, Manufacturing, and Trade by voice vote on 2026-09-01 and awaits full-committee action.
