---
title: AI Ads Act
short_name: AI Ads Act
bill_numbers:
- S. 5135
- H.R. 9985
congress: 119
topic: Deepfakes & Synthetic Media
status: introduced
chamber_origin: Both
introduced_date: '2026-07-27'
last_action: House version referred to House Administration; Senate version referred to Senate Rules and Administration
last_action_date: '2026-07-30'
sponsors:
- Sen. Adam Schiff (D-CA)
- Rep. Ro Khanna (D-CA)
cosponsor_count: 0
committees:
- House Administration
- Senate Rules and Administration
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
    R: 0.9
    D: 0.60
    E_f: 0.60
    P: 0.40
  likelihood:
    p_committee: 0.10
    p_enact: 0.02
    basis: "base_rate_adjusted"
  rationale:
    A: "The obligation runs against 'any person' who fraudulently misrepresents a candidate, party, or committee's authority or solicits funds under false authority — a campaign-finance-fraud rule that happens to extend an existing prohibition to cover AI-generated content, not a conduct standard on AI developers themselves. Domain-general mechanism guardrail applies; scores 0 rather than the ±1 ceiling because there is no AI-specific channel here at all (the bill doesn't distinguish AI-generated fraud from any other kind in its enforcement structure)."
    B: "No preemption or savings-clause language in the bill text (confirmed against the govinfo-hosted introduced text of both S. 5135 and H.R. 9985). This amends 52 U.S.C. 30124, a narrow amendment to existing federal election law rather than a new regulatory scheme, so the implicit-preemption floor (which applies only where A >= +2) does not trigger."
    C: "No new agency authority, funding, staffing, or reporting flow — the bill only broadens the class of conduct and actors covered by an existing FEC-enforced prohibition."
    D: "No export-control, chip-access, or geopolitical content."
    E_consumer: "Extends the FECA's fraudulent-misrepresentation and fraudulent-solicitation prohibitions to content 'generated in whole or in part' using generative AI, and broadens covered conduct from candidate-on-candidate misrepresentation to fraudulent misrepresentation 'by any person for any purpose.' This is a targeted criminal/civil prohibition under existing FEC enforcement (which can involve civil penalties and, for knowing and willful violations, criminal referral) rather than a broad private right of action, so it lands at 3 rather than 5 — narrower than the private-right-of-action ceiling but stronger than a bare labeling rule."
    F: "No data-center, permitting, or energy content."
    R: "Covers all fraudulent misrepresentation nationwide involving federal candidates/committees, with no revenue or sector carve-outs; scoped to federal candidate fraud specifically rather than all political content."
    Depth: "Driven by the E axis (3/5); A, B, C, F are all 0."
    E_f: "FEC enforcement of the underlying FECA provisions (civil penalties, conciliation, and potential DOJ criminal referral for knowing and willful violations) — stronger than a bare unenforced obligation but not a private right of action, so scored as agency rulemaking + civil penalties rather than the 1.0 ceiling."
    P: "A straightforward extension of an existing 50-year-old federal statute (FECA fraudulent-misrepresentation provisions) to cover AI-generated content specifically — sector-specific and self-contained rather than a novel framework likely to be copied elsewhere."
    likelihood: "Reintroduced July 27-30, 2026 after an identical predecessor (H.R. 9639, 118th Congress) died in House Administration without a hearing or markup in 2024. No GovTrack prognosis page yet exists for either the Senate or House 119th-Congress version given how recently they were introduced; base rate for single-sponsor House Administration/Senate Rules referrals with zero cosponsors and no floor time in a Congress's final months is very low. Both bills currently have zero cosponsors, a weaker starting position than most bills in this tracker."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- deepfakes
- elections
- political ads
sources:
- label: Congress.gov (Senate)
  url: https://www.congress.gov/bill/119th-congress/senate-bill/5135
- label: Congress.gov (House)
  url: https://www.congress.gov/bill/119th-congress/house-bill/9985
- label: Introduced text (S. 5135)
  url: https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s5135is.xml
- label: Introduced text (H.R. 9985)
  url: https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr9985ih.xml
- label: Sen. Schiff press release
  url: https://www.schiff.senate.gov/news/press-releases/news-sen-schiff-rep-khanna-reintroduce-landmark-bill-to-combat-fraudulent-ai-generated-campaign-ads/
summary: Amends federal election law to extend existing fraudulent-misrepresentation and fraudulent-solicitation prohibitions to cover AI-generated campaign content, and broadens the covered conduct to any person misrepresenting a candidate or committee.
timeline:
- date: '2026-07-27'
  event: S. 5135 introduced by Sen. Schiff; referred to Senate Rules and Administration
- date: '2026-07-30'
  event: H.R. 9985 introduced by Rep. Khanna; referred to House Administration
- date: '2026-09-10'
  event: Added to tracker. Both bills remain in committee with zero cosponsors; an identical 118th-Congress predecessor (H.R. 9639) died in committee without a markup.
---

The bill amends the Federal Election Campaign Act of 1971 to clarify that its existing prohibitions on fraudulent misrepresentation of campaign authority and fraudulent solicitation of campaign funds explicitly cover content generated in whole or in part using generative AI. It also broadens the underlying prohibition from candidate-on-candidate misrepresentation to fraudulent misrepresentation of any candidate, party, or committee "by any person for any purpose," removing the requirement that the misrepresentation be damaging to a rival campaign.
