---
title: Multilateral Alignment of Technology Controls on Hardware (MATCH) Act
short_name: MATCH Act
bill_numbers:
- S. 4281
- H.R. 8170
congress: 119
topic: Chips & National Security
status: introduced
chamber_origin: Both
introduced_date: '2026-04-02'
last_action: S. 4281 referred to Senate Banking, Housing, and Urban Affairs; H.R. 8170 referred to House Foreign Affairs. Both bills, alongside the Chip Security Act and AI OVERWATCH Act, were folded into the Senate FY2027 NDAA (S. 4784) manager's amendment, but that underlying vehicle failed cloture 50-46 on 2026-07-14 and has seen no further Senate floor action per CRS's Sept. 1, 2026 status report
last_action_date: '2026-07-14'
sponsors:
- Sen. Jim Risch (R-ID)
- Sen. Pete Ricketts (R-NE)
- Sen. Andy Kim (D-NJ)
- Rep. Michael Baumgartner (R-WA)
cosponsor_count: 4
committees:
- Senate Banking, Housing, and Urban Affairs
- House Foreign Affairs
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 1.0
    D: 5.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.9
    D: 0.20
    E_f: 0.60
    P: 0.80
  likelihood:
    p_committee: 0.55
    p_enact: 0.28
    basis: "base_rate_adjusted"
  rationale:
    A: "Binds semiconductor manufacturing equipment (SME) sellers/servicers and, by extension, allied governments — not AI model developers. No provision touches training, deployment, or model release, so this sits at 0 rather than any positive A value."
    B: "Contains no preemption language or savings clause; it's an export-control bill administered through Commerce/BIS and State, not a frontier-AI regulatory scheme, so the implicit-preemption floor doesn't apply (it doesn't establish a regulatory scheme targeting AI developers, and A scores 0 here, well under the A ≥ +2 trigger)."
    C: "No new government AI-oversight body or standing incident-reporting channel is created; the closest capacity element is BIS being tasked with monitoring allied compliance during the 150-day window and administering unilateral FDPR extension if allies don't align — a modest expansion of an existing regulator's enforcement task rather than a new authority, database, or evaluation body. Scored +1 (studies/reporting-deadline tier) rather than 0, since BIS has a concrete, dated compliance-monitoring task, but not the +2/+3 tier because there's no new standing reporting-into-a-database mechanism analogous to Chip Security Act's diversion reports."
    D: "This is squarely an export-control hardening bill: it prohibits sale/servicing of critical chipmaking tools (DUV immersion lithography, cryogenic etch, etc.) to named Chinese chipmakers (SMIC, Huawei, Hua Hong, CXMT, YMTC) and their affiliates, gives allied governments (Netherlands, Japan, South Korea) 150 days to match U.S. controls, and — if they don't — directs Commerce to unilaterally extend Foreign Direct Product Rule (FDPR) jurisdiction over allied-made tools built with U.S. technology. Hard controls with a real enforcement backstop (extraterritorial FDPR extension) place this at the top of the D ladder alongside Chip Security Act, though its lever is chipmaking-tool trade rather than chip-level location verification — the two bills are complementary, not duplicative: Chip Security Act targets chips already exported; MATCH Act targets the tools used to fabricate chips in the first place."
    E_consumer: "No deepfake, NCII, companion-bot, algorithmic-discrimination, or election-integrity content — a chipmaking-equipment export-control bill with no consumer-facing provisions."
    F: "No domestic data-center, permitting, interconnection, siting, or ratepayer provisions — this is an outbound trade-control bill, not a domestic buildout constraint."
    R: "Covers the essential chipmaking-tool export channel (DUV lithography and related SME) to all covered Chinese entities and their subsidiaries/affiliates/joint ventures — a near-complete sweep of the target class of tool sales to named adversary fabs, discounted slightly because allied-tool leakage outside the 150-day compliance window remains a live gap the bill itself acknowledges by needing the FDPR backstop."
    Depth: "Depth = max(|A|,|B|,|C|,|F|,E)/5, which by design excludes axis D (external/geopolitical). With A=0, B=0, C=1, F=0, E=0, the binding component is C=1, giving Depth = 1/5 = 0.20. This understates the bill's real-world weight, which lives almost entirely in axis D (+5) — but D is deliberately excluded from Depth for the same reason it's excluded from the safety composite, so 0.20 is the correct value under the formula even though it reads as low."
    E_f: "Enforcement runs through BIS administrative action (FDPR extension, Entity-List-style designation) rather than private lawsuits or agency civil-penalty rulemaking with fines — closer to 'agency rulemaking + civil penalties' than 'AG enforcement only,' since export-control violations under EAR carry both civil and criminal exposure once FDPR jurisdiction attaches."
    P: "A statutory allied-alignment deadline backed by unilateral FDPR extension is a first-in-kind mechanism for compelling ally cooperation on chip-tool controls, and closely tracks language likely to reappear in future export-control legislation (it was bundled with Chip Security Act and AI OVERWATCH as a package), though it's sector-specific to semiconductor tooling rather than a general framework."
  confidence: low
  text_source: summary
  scored_at: "2026-09-09"
tags:
- chip exports
- semiconductor manufacturing equipment
- China
- allied coordination
- export controls
sources:
- label: Congress.gov — S. 4281
  url: https://www.congress.gov/bill/119th-congress/senate-bill/4281
- label: "Sen. Risch, Ricketts, Kim press release"
  url: https://www.foreign.senate.gov/press/rep/release/risch-ricketts-kim-introduce-match-act-level-the-global-playing-field-for-us-tech
- label: "Rep. Baumgartner press release"
  url: https://baumgartner.house.gov/2026/04/02/baumgartner-introduces-bipartisan-bill-to-tighten-controls-on-sensitive-chipmaking-equipment/
- label: "CNAS Insights — MATCHing Policy to Strategy"
  url: https://www.cnas.org/publications/commentary/cnas-insights-matching-policy-to-strategy-the-bill-to-control-chipmaking-equipment
- label: "Sen. Banks — Tech, chips bills poised for NDAA ride"
  url: https://www.banks.senate.gov/news/in-the-news/tech-chips-bills-poised-for-ndaa-ride/
summary: Would tighten U.S. export controls on chipmaking equipment (not chips themselves) sold to Chinese fabs, and give allies 150 days to match U.S. restrictions or face unilateral extraterritorial controls.
timeline:
- date: '2026-04-02'
  event: S. 4281 introduced by Sen. Ricketts (with Risch, Kim, Schumer); H.R. 8170 introduced by Rep. Baumgartner
- date: '2026-07-14'
  event: MATCH Act provisions folded into the Senate FY2027 NDAA (S. 4784) manager's amendment alongside the Chip Security Act and AI OVERWATCH Act
- date: '2026-07-14'
  event: Cloture on the motion to proceed to the Senate FY2027 NDAA fails 50-46
- date: '2026-08-28'
  event: Heritage Action-led coalition letter urges Congress to ensure MATCH Act (with Chip Security Act, AI OVERWATCH Act) inclusion in the final NDAA
---

The MATCH Act (Multilateral Alignment of Technology Controls on Hardware Act) modernizes export controls on semiconductor **manufacturing equipment** — the tools (deep ultraviolet immersion lithography systems, cryogenic etch systems, and related components) used to fabricate advanced chips, rather than the chips themselves. It prohibits the sale or servicing of these tools to fabrication facilities inside "countries of concern," names specific Chinese chipmakers (SMIC, Huawei, Hua Hong, CXMT, YMTC) and their subsidiaries/affiliates as covered facilities, and carves out an exception for U.S.- or allied-controlled facilities operating there.

Its distinctive mechanism is an allied-alignment deadline: the bill gives allied toolmaking nations (principally the Netherlands and Japan, home to ASML and Tokyo Electron) 150 days to match U.S. restrictions. If they don't, the Secretary of Commerce is directed to unilaterally extend the Foreign Direct Product Rule (FDPR) — asserting U.S. export-control jurisdiction over any tool made anywhere in the world if it incorporates U.S. technology, software, or equipment.

**This is distinct from the already-tracked Chip Security Act** (H.R. 3447 / S. 1705): the Chip Security Act mandates location-verification hardware in chips that have already been exported, to catch diversion after the fact. The MATCH Act instead targets the upstream chipmaking *tools* used to fabricate chips in Chinese fabs in the first place, and adds an allied-coordination lever that Chip Security Act lacks. The two bills were bundled together (along with the AI OVERWATCH Act) into the same Senate FY2027 NDAA manager's amendment, which stalled after a failed cloture vote in July 2026 and has not advanced since — so both bills currently share the same stuck legislative vehicle despite being substantively different measures.
