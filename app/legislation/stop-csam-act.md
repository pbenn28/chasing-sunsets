---
title: Strengthening Transparency and Obligations to Protect Children Suffering from Abuse and Mistreatment Act of 2025 (STOP CSAM Act)
short_name: STOP CSAM Act
bill_numbers:
- S. 1829
- H.R. 3921
congress: 119
topic: Children & Chatbots
status: committee_passed
chamber_origin: Both
introduced_date: '2025-05-21'
last_action: S. 1829 reported by the Senate Judiciary Committee and placed on the Senate calendar
last_action_date: '2025-06-26'
sponsors:
- Sen. Josh Hawley (R-MO)
- Sen. Dick Durbin (D-IL)
cosponsor_count: 28
committees:
- Senate Judiciary
- House Judiciary
scoring:
  axes:
    A: 0.5
    B: 1.0
    C: 0.5
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 4.0
  impact_components:
    R: 1.00
    D: 0.80
    E_f: 1.00
    P: 0.60
  likelihood:
    p_committee: 1.0
    p_enact: 0.6
    basis: "govtrack_corroborated_adjusted"
  rationale:
    A: "Binds electronic communication and remote computing service providers -- platforms, hosts, and storage -- not the labs that train or release AI models. It expands mandatory CyberTipline reporting, adds an annual FTC/DOJ reporting regime for large platforms, and creates civil liability for platforms that host or facilitate CSAM, including AI-generated material, but a developer that never distributes or hosts content incurs nothing under it. The one open question is whether a model provider could itself count as a covered service when its own model generates the material -- an unsettled reading that would, if courts adopt it, create a real, if narrow, channel of developer exposure; this score assumes the narrower and more likely reading that these terms describe network and storage intermediaries, not model developers."
    B: "Sec. 7 preserves state and tribal authority specifically over CSAM and child-exploitation law -- states can still enforce or go further than this Act's floor on that one subject. It has nothing to do with, and no effect on, states' authority to regulate frontier AI development, which is what this axis tracks."
    C: "Adds new CyberTipline reporting duties and an annual FTC/DOJ reporting regime for large platforms -- real infrastructure, but built entirely around detecting and responding to CSAM rather than observing or evaluating AI systems. AI-generated CSAM reports moving through this channel offer a narrow, incidental window into one category of model misuse, not new AI-oversight capacity."
    D: "No export-control, chip-access, or other geopolitical-competition content."
    E_consumer: "Creates a new private right of action letting victims of child sexual exploitation sue interactive computer service providers that host or facilitate CSAM, including AI-generated CSAM. The right of action is confined to this one harm category rather than spanning deepfakes, NCII, companion bots, discrimination, or election integrity more broadly, but it's a substantial step beyond criminal liability alone."
    F: "No data-center, permitting, interconnection, ratepayer, or fab-siting content."
    R: "Applies to 'interactive computer services' broadly, with the FTC/DOJ annual-reporting mandate keyed to large providers (over 1 million monthly users and $50 million in annual revenue) -- a threshold wide enough to capture essentially the whole universe of platforms that meaningfully intersect with CSAM at scale."
    Depth: "Driven by the new private right of action against platforms (E) -- the direct legal exposure it creates is the bill's most consequential feature, well beyond its narrow effect on AI-specific governance."
    E_f: "Creates a private right of action for victims against providers -- real, direct legal exposure rather than reporting obligations alone."
    P: "Expands and formalizes the existing CyberTipline/NCMEC federal reporting framework rather than inventing a wholly new institution, while adding a new private right of action on top of it."
    likelihood: "Already cleared the Senate Judiciary Committee unanimously and sits on the Senate calendar -- a completed step, not a forecast (p_committee unchanged at 1.0). RE-VERIFIED 2026-09-09: as of this check, the FY2027 NDAA (S. 4784 / H.R. 8800) still has not reached final passage -- the House passed its own FY2027 NDAA on a 216-212 vote in July 2026, and the Senate version cleared the Armed Services Committee (18-9) and heads toward the floor, but no Senate floor passage or House-Senate conference agreement has been confirmed. There is no reporting that the STOP CSAM rider Hawley added to the Senate manager's amendment package on 2026-07-14 has been struck or amended since -- it appears to still be riding in the pending Senate NDAA text, but because the underlying NDAA vehicle itself has not reached the floor or a conference agreement, the rider's fate is still unresolved rather than confirmed. p_enact is nudged down slightly from 0.65 to 0.6 to reflect that over a month has passed with the NDAA still stalled pre-floor-passage and no independent floor or unanimous-consent action on S. 1829/H.R. 3921 directly -- the bill's enactment path still runs entirely through a must-pass vehicle that has not yet moved, and conference is a point where riders are traditionally at the most risk of being dropped."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- CSAM
- child safety
- platform liability
sources:
- label: Congress.gov (Senate)
  url: https://www.congress.gov/bill/119th-congress/senate-bill/1829
- label: Congress.gov (House)
  url: https://www.congress.gov/bill/119th-congress/house-bill/3921
- label: Sen. Hawley press release (NDAA rider)
  url: https://www.hawley.senate.gov/hawley-negotiates-inclusion-of-stop-csam-act-in-senate-ndaa/
summary: Bipartisan bill expanding CSAM protections and letting victims sue tech platforms; cleared Senate committee.
timeline:
- date: '2025-05-21'
  event: S. 1829 introduced by Sen. Hawley with Sen. Durbin
- date: '2025-06-11'
  event: H.R. 3921 introduced
- date: '2025-06-26'
  event: S. 1829 ordered reported by Senate Judiciary; placed on calendar
- date: '2026-07-14'
  event: Sen. Hawley announced STOP CSAM Act text was added to the FY2027 NDAA manager's amendment package pending in the Senate; the NDAA itself remained stalled on the floor over unrelated disputes, and no direct floor or unanimous-consent action on S. 1829/H.R. 3921 itself has occurred
- date: '2026-09-09'
  event: Re-verified -- FY2027 NDAA (S. 4784/H.R. 8800) still has not reached Senate floor passage or a House-Senate conference agreement; House passed its own FY2027 NDAA 216-212 in July 2026. No reporting found that the STOP CSAM rider has been stripped from the pending Senate text, but its fate remains tied to the still-unresolved NDAA vehicle.
---

The STOP CSAM Act revises the federal framework for preventing online child sexual exploitation. It expands protections and remedies for child victims, broadens CyberTipline reporting duties for interactive computer services, requires large providers to report annually to the FTC and DOJ, and creates new liability letting victims pursue civil action against providers that host or facilitate CSAM — including, increasingly, AI-generated material.

**Update 2026-09-09:** The bill's enactment path still runs through the FY2027 NDAA rider Sen. Hawley negotiated in July 2026; as of this check that NDAA has not reached Senate floor passage or a conference agreement, so the rider's ultimate fate remains pending rather than resolved.
