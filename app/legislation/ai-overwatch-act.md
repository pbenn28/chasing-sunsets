---
title: "AI OVERWATCH Act (Oversight of Verified Exports and Restrictions on Weaponizable Advanced Technology to Covered High-Risk Actors Act)"
short_name: "AI OVERWATCH Act"
bill_numbers: ["H.R. 6875", "S. 4456"]
congress: 119
topic: "Chips & National Security"
status: "committee_passed"
chamber_origin: "House"
introduced_date: "2025-12-18"
last_action: "Passed the House Foreign Affairs Committee, 42-2-1; Sen. Banks announced provisions were included in the Senate FY2027 NDAA manager's amendment, but that underlying bill (S. 4784) failed a cloture vote and has seen no further Senate floor action since"
last_action_date: "2026-01-21"
sponsors: ["Rep. Brian Mast (R-FL)", "Sen. Jim Banks (R-IN)"]
cosponsor_count: null
committees: ["House Foreign Affairs", "Senate Banking, Housing, and Urban Affairs"]
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 3.0
    D: 4.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.95
    D: 0.60
    E_f: 0.80
    P: 0.80
  likelihood:
    p_committee: 0.95
    p_enact: 0.45
    basis: "base_rate_adjusted"
  rationale:
    A: "Regulates the export-licensing process for AI chips rather than placing any obligation on AI developers themselves — nothing here touches how frontier systems are built, disclosed, or deployed."
    B: "The bill contains no preemption or savings-clause language of any kind. It's a federal export-licensing and congressional-review regime for chip exports, not a regulatory scheme aimed at AI developers, so there's no state law here for it to conflict with or preserve."
    C: "Requires the Commerce Department to notify Congress at least 30 days before approving an export license for a covered AI chip to a country of concern, and the license can't take effect until that window runs or Congress votes to block it — a real, standing check on the executive's licensing power."
    D: "A genuine export-control measure: mandatory pre-license certification and a congressional disapproval window for advanced AI chips headed to countries of concern, with outright denial for the most capable restricted chips."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election-integrity content anywhere in the bill — it's entirely a chip-export licensing and congressional-review regime."
    F: "No data-center, permitting, interconnection, or ratepayer content of any kind."
    R: "Covers essentially all export, reexport, and in-country transfers of the covered and restricted AI chip tiers to named countries of concern, with no revenue floors or carve-outs narrowing that scope."
    Depth: "Driven mainly by the new congressional review mechanism — a meaningful but bounded change to how chip exports get approved, not a sweeping overhaul."
    E_f: "A license can't take effect until the review window closes or Congress blocks it, and violations of the underlying export-control regime carry Commerce's standard civil and criminal penalties — enforcement runs through a federal regulator with real teeth, not just a paperwork requirement."
    P: "Would create the first standing congressional review mechanism specifically for AI chip exports, and it's already being bundled with other export-control bills (the Chip Security Act, the MATCH Act) that could make it a template for AI-specific export oversight going forward."
    likelihood: "Re-verified 2026-09-09: Sen. Banks confirmed (press release, ~7/15/2026) that AI OVERWATCH, the Chip Security Act, and the MATCH Act were bundled into the Senate FY2027 NDAA manager's amendment. But the underlying vehicle stalled: cloture on the motion to proceed to the Senate NDAA (S. 4784) failed 50-46 on 7/14/2026, and per CRS's Sept. 1, 2026 status report the Senate has taken no further procedural steps since — no floor passage, no conference. The House-passed NDAA (H.R. 8800, passed 216-212 on 7/22/2026) does not include these chip-export provisions. An Aug. 28 Heritage Action-led coalition letter was still lobbying to \"ensure\" the three bills' inclusion, indicating advocates themselves don't yet treat it as locked in. GovTrack does not publish a prognosis for either bill. Net effect: the vehicle this bill was riding is now stuck, not moving — path to enactment is real but more uncertain than a month ago, since NDAA passage itself (not just inclusion in it) is now the binding constraint. Lowered p_enact slightly (0.55→0.45) to reflect that stall; p_committee held near-certain since House committee passage already happened and Senate Banking hasn't blocked the companion."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags: ["export controls", "chip exports", "China", "national security"]
sources:
  - label: "House Foreign Affairs Committee"
    url: "https://www.congress.gov/bill/119th-congress/house-bill/6875"
  - label: "Sen. Banks press release, AI OVERWATCH Act secured in Senate NDAA"
    url: "https://www.banks.senate.gov/news/press-releases/banks-secures-ai-overwatch-act-in-senate-ndaa/"
  - label: "CRS, FY2027 NDAA Status of Legislative Activity (Sept. 1, 2026)"
    url: "https://www.congress.gov/crs-product/IN12704"
  - label: "Daily Signal, Heritage Action coalition letter urging AI OVERWATCH/Chip Security Act/MATCH Act inclusion in NDAA (Aug. 28, 2026)"
    url: "https://www.dailysignal.com/2026/08/28/heritage-action-joins-letter-urging-ai-protections-against-china/"
summary: "Would give Congress a 30-day window to review and block AI chip export licenses to China and other adversaries; passed House committee 42-2-1."
timeline:
  - date: "2025-12-18"
    event: "H.R. 6875 introduced in the House by Rep. Brian Mast"
  - date: "2026-01-21"
    event: "Passed the House Foreign Affairs Committee, 42-2-1"
  - date: "2026-04-30"
    event: "Senate companion S. 4456 introduced by Sen. Jim Banks"
  - date: "2026-07-14"
    event: "Reporting indicates AI OVERWATCH provisions may be folded into a Senate NDAA (FY2027) manager's amendment; described as still in flux"
  - date: "2026-07-14"
    event: "Cloture on the motion to proceed to the Senate FY2027 NDAA (S. 4784) fails 50-46"
  - date: "2026-07-15"
    event: "Sen. Banks announces AI OVERWATCH Act provisions included in the Senate NDAA manager's amendment"
  - date: "2026-07-22"
    event: "House passes its own FY2027 NDAA (H.R. 8800, 216-212), which does not include AI OVERWATCH provisions"
  - date: "2026-08-28"
    event: "Heritage Action-led coalition letter urges Congress to ensure AI OVERWATCH Act (with Chip Security Act, MATCH Act) inclusion in the final NDAA — indicating inclusion was still not settled"
  - date: "2026-09-09"
    event: "Re-verified — Senate NDAA remains stalled post-cloture-failure with no further floor action per CRS; no conference yet exists"
---
The AI OVERWATCH Act would give the House Foreign Affairs Committee and Senate Banking Committee a 30-day window to review, and potentially block, licenses for exporting advanced AI chips to China and other countries of concern. It was introduced after President Trump greenlit shipments of Nvidia's H200 AI chips to China, a decision that split Republican China hawks from the administration's own chip-export posture.

Its House version passed committee by a lopsided 42-2-1 vote, but its Senate companion has seen no markup, and as of late July 2026 reporting describes its provisions as possibly being folded into the Senate's FY2027 defense authorization bill rather than advancing as standalone legislation — a vehicle switch this page's GAIN AI Act entry shows doesn't guarantee survival to a final bill.

Update (September 2026): Sen. Banks confirmed AI OVERWATCH was added to the Senate NDAA manager's amendment, but the Senate NDAA itself stalled after a failed cloture vote on July 14, 2026 and has seen no further floor action; the House-passed NDAA does not include these provisions, leaving the bill's fate tied to a defense bill that is currently stuck rather than moving toward conference.
