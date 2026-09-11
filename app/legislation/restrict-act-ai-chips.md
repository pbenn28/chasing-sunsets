---
title: "Restoring Export and Security Trade Restrictions for Integrated Circuit Technologies Act (RESTRICT Act)"
short_name: "RESTRICT Act"
bill_numbers: ["H.R. 6879"]
congress: 119
topic: "Chips & National Security"
status: "introduced"
chamber_origin: "House"
introduced_date: "2025-12-18"
last_action: "Referred to the House Committee on Foreign Affairs; no markup scheduled as of this writing"
last_action_date: "2025-12-18"
sponsors: ["Rep. Gregory Meeks (D-NY)"]
cosponsor_count: 13
committees: ["House Foreign Affairs"]
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 0.0
    D: 4.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.90
    D: 0.80
    E_f: 0.80
    P: 0.40
  likelihood:
    p_committee: 0.15
    p_enact: 0.05
    basis: "base_rate_adjusted"
  rationale:
    A: "Binds chip exporters and Commerce Department licensing decisions, not AI developers — the bill does not touch model training, evaluation, or deployment conduct at all."
    B: "Silent on state authority; operates entirely through federal export-control law (codifying and hardening existing Federal Register restrictions), with no mention of state AI regulation."
    C: "No new government evaluation body, incident-reporting flow, or enforcement staffing beyond directing Commerce to administer an already-existing licensing regime; it largely codifies restrictions Commerce could already impose administratively rather than building new observation/enforcement capacity."
    D: "Prohibits export of H200-class and other advanced AI chips to China and other arms-embargoed 'countries of concern,' directs Commerce to deny export licenses for such destinations, and creates a license-free transfer pathway for U.S. companies' own overseas facilities in non-restricted countries subject to security conditions — a meaningful new statutory hard control on advanced-chip exports, though it primarily codifies current Federal Register practice rather than adding location-verification or criminal-diversion enforcement on top of it, so it lands at +4 rather than +5."
    F: "No data-center, permitting, siting, or ratepayer content — the bill is entirely an export-control measure."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election-integrity content."
    R: "A federal export-control bill covering the full universe of advanced AI accelerators (H200-class and above) and all 'countries of concern' as defined by existing arms-embargo status — near-total reach within its target class of controlled hardware, with a small discount for the two-year Commerce definitional-update mechanism introducing some scope uncertainty."
    Depth: "Driven by the D-axis export-control score; this is the only axis the bill moves, and it moves it substantially."
    E_f: "Enforcement runs through Commerce Department export-license denial and the existing civil/criminal penalty regime under export-control law (EAR/IEEPA-adjacent authority), not a private right of action."
    P: "A sector-specific, self-contained chip-export restriction rather than a permanent new institution; it could be a template other export-control bills copy, but it doesn't itself create an enduring structure."
    likelihood: "Introduced 2025-12-18 by Rep. Meeks (House Foreign Affairs ranking member) with 13 House Democratic cosponsors, directly responding to the Trump administration's approval of H200 chip sales to China. As of this writing the bill has NOT received a committee markup — a January 21, 2026 House Foreign Affairs markup reported by Roll Call and initially thought to involve this bill was in fact a distinct measure sponsored by Rep. Brian Mast (which passed 42-2); H.R. 6879 itself remains unmarked-up and sits in a Republican-controlled committee as an all-Democrat bill opposing an administration (of the sponsor's own opposing party) decision, which caps its near-term prospects. GovTrack does not publish a numeric prognosis for this bill. p_committee and p_enact are set low and base-rate-adjusted given single-party sponsorship, no committee action in nine months, and the administration's contrary policy stance — though the underlying chip-export-control debate remains live and could resurface via an NDAA rider or similar vehicle, as GAIN AI Act did."
  confidence: low
  text_source: summary
  scored_at: "2026-09-09"
tags: ["chip exports", "China", "national security", "H200", "export controls"]
sources:
  - label: "House Foreign Affairs Committee (Democrats) press release"
    url: "https://democrats-foreignaffairs.house.gov/2025/12/meeks-introduces-bill-to-block-sales-of-advanced-ai-chips-to-china"
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/house-bill/6879"
  - label: "Select Committee on the CCP (Democrats) press release"
    url: "https://democrats-selectcommitteeontheccp.house.gov/media/press-releases/krishnamoorthi-cosponsors-meeks-restrict-act-block-sales-advanced-ai-chips"
summary: "Would statutorily prohibit sales of H200-class and other advanced AI chips to China and other 'countries of concern,' codifying and hardening existing export-control practice."
timeline:
  - date: "2025-12-18"
    event: "Introduced in the House by Rep. Gregory Meeks with 13 Democratic cosponsors"
  - date: "2026-01-21"
    event: "A separate, similarly-purposed chip-export bill from Rep. Brian Mast advances 42-2 in House Foreign Affairs — H.R. 6879 itself is not on that markup and remains unmarked-up"
---

Introduced by House Foreign Affairs Committee Ranking Member Gregory Meeks in direct response to the Trump administration's approval of H200 AI chip sales to China, the RESTRICT Act would statutorily prohibit the sale of the most advanced U.S. AI chips — H200-class and above — to China and other countries under a U.S. arms embargo as of January 1, 2025 ("countries of concern"). It directs the Commerce Department to deny export license applications for advanced integrated circuits to those destinations, largely codifying and hardening restrictions Commerce has applied administratively through the Federal Register rather than creating novel controls from scratch. The bill allows Commerce some flexibility to update covered-chip technical definitions after two years, subject to congressional national-security certification, and creates a license-free pathway for U.S. companies to transfer technology to their own facilities in non-restricted countries, subject to security conditions.

**Naming note:** this H.R. 6879 "RESTRICT Act" is entirely distinct from the well-known 118th Congress "RESTRICT Act" (S. 686), which targeted TikTok and other foreign-linked software/apps rather than AI chip exports. The two bills share an acronym and general "restrict foreign tech" theme but have no textual or substantive relationship — this tracker entry concerns only the 119th Congress AI-chip-export version.

As of this writing, H.R. 6879 has not received a committee markup. A January 2026 House Foreign Affairs Committee markup of AI-chip-export-related legislation that could be mistaken for this bill's advancement was in fact a separate measure from Rep. Brian Mast; Meeks' bill, introduced by a House Democrat and opposing a decision made by the Trump administration, remains without committee action in the Republican-controlled House Foreign Affairs Committee.
