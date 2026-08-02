---
title: "Transparency and Responsibility for Artificial Intelligence Networks Act (TRAIN Act)"
short_name: "TRAIN Act"
bill_numbers: ["H.R. 7209", "S. 2455"]
congress: 119
topic: "Transparency & Copyright"
status: "committee"
chamber_origin: "Senate"
introduced_date: "2025-07-24"
last_action: "No committee action recorded since introduction on either chamber's bill"
last_action_date: "2026-01-22"
sponsors: ["Sen. Peter Welch (D-VT)", "Rep. Madeleine Dean (D-PA)", "Rep. Nathaniel Moran (R-TX)"]
cosponsor_count: null
committees: ["House Judiciary", "Senate Judiciary"]
scoring:
  axes:
    A: 1.5
    B: 0.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 1.0
    D: 0.30
    E_f: 0.8
    P: 0.8
  likelihood:
    p_committee: 0.25
    p_enact: 0.04
    basis: "base_rate_heuristic_no_live_lookup"
  rationale:
    A: "Adds a new 17 U.S.C. 514 that compels any 'developer' — defined broadly to cover anyone who designs, produces, or substantially modifies a generative AI model and curates its training data — to disclose training material upon a court-issued subpoena. Noncompliance triggers a rebuttable presumption of infringement, and bad-faith requests can draw Rule 11 sanctions. It's a real, legally compelled disclosure duty, but it works case-by-case at a copyright holder's request rather than as a standing reporting regime."
    B: "No preemption or savings-clause language appears anywhere in the bill. The one 'nothing shall be construed' clause just limits subpoena scope to the requester's own copyrighted works and has nothing to do with state authority."
    C: "Creates a private civil-court subpoena mechanism for copyright holders rather than any new government body, database, or regulator."
    D: "No export-control, chip-access, or geopolitical-competition content."
    E_consumer: "Addresses copyright and training-data harms to rights holders, not the deepfake, NCII, companion-bot, discrimination, or election-integrity harms this site otherwise tracks under consumer protection."
    F: "The bill's sole substantive provision is the copyright-subpoena mechanism; nothing touches data centers, permitting, interconnection, or energy."
    R: "Applies to essentially the full universe of AI developers, with no revenue floor or sector carve-out limiting who can be subpoenaed."
    Depth: "Driven mainly by the developer disclosure duty in axis A — the compelled-subpoena mechanism doesn't reach much further than that."
    E_f: "Any copyright holder can get a subpoena from a federal court clerk on their own, without suing first or waiting on an agency — close to a private right of action, though it compels document production rather than creating a damages claim."
    P: "Modeled directly on the existing DMCA subpoena process, repurposed as a new framework for AI training-data disclosure — adapting an established tool rather than building something entirely new or a permanent institution."
    likelihood: "An unusually bipartisan lineup (Welch, Dean, Moran, plus original cosponsors Blackburn, Hawley, and Schiff) gives it real credibility, but neither chamber's version has seen committee action in the year since introduction, and legal commentary has flagged friction with the administration's deregulation-focused AI agenda."
  confidence: high
  text_source: full_text
  scored_at: "2026-08-01"
tags: ["copyright", "training data", "transparency", "subpoena"]
sources:
  - label: "Congress.gov (House)"
    url: "https://www.congress.gov/bill/119th-congress/house-bill/7209"
  - label: "Congress.gov (Senate)"
    url: "https://www.congress.gov/bill/119th-congress/senate-bill/2455"
summary: "Would let copyright holders subpoena AI companies to check if their work was used to train AI models."
timeline:
  - date: "2025-07-24"
    event: "S. 2455 introduced in the Senate by Sen. Welch, with Sens. Blackburn, Hawley, and Schiff; referred to Senate Judiciary Committee"
  - date: "2026-01-22"
    event: "H.R. 7209 introduced in the House by Rep. Dean, with Rep. Moran; referred to House Judiciary Committee"
  - date: "2026-05-01"
    event: "Legal press (Berkeley Technology Law Journal) confirms the bill remains early-stage in both chambers"
---
The TRAIN Act would let a copyright holder who has a good-faith belief their work was used without authorization to train a generative AI model obtain a subpoena — issued by a federal court clerk, without first filing a lawsuit — compelling the AI developer to produce copies of, or records identifying, the copyrighted works used in training. It's modeled directly on the existing DMCA subpoena process used to identify online infringers, repurposed here to compel disclosure of AI training data.

The Senate version came first, introduced by Sen. Welch with an unusual bipartisan lineup of original cosponsors (Blackburn, Hawley, and Schiff) in July 2025; the House companion followed six months later from Reps. Dean and Moran. Neither has seen committee action since its introduction.
