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
    A: 1.0
    B: 0.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 1.0
    D: 0.20
    E_f: 0.8
    P: 0.8
  likelihood:
    p_committee: 0.28
    p_enact: 0.04
    basis: "base_rate_adjusted"
  rationale:
    A: "Guardrail check (frontier/systemic risk vs. near-term consumer harm): the compelled disclosure here — a new 17 U.S.C. 514 letting a copyright holder subpoena any 'developer' for training material, with a rebuttable presumption of infringement on noncompliance — is a copyright-discovery tool, not a mechanism aimed at frontier-scale training, catastrophic risk, or systemic AI oversight. Its subject is enabling infringement litigation, not observing or constraining frontier development. That caps it near the guardrail's floor even though the legal mechanism (subpoena, evidentiary presumption) is real and enforceable; scored 1.0, aligned with the identically-scoped CLEAR Act rather than the 1.5 previously assigned for the case-by-case subpoena mechanic."
    B: "No preemption or savings-clause language appears anywhere in the bill. The one 'nothing shall be construed' clause just limits subpoena scope to the requester's own copyrighted works and has nothing to do with state authority."
    C: "Creates a private civil-court subpoena mechanism for copyright holders rather than any new government body, database, or regulator."
    D: "No export-control, chip-access, or geopolitical-competition content."
    E_consumer: "Addresses copyright and training-data harms to rights holders, not the deepfake, NCII, companion-bot, discrimination, or election-integrity harms this site otherwise tracks under consumer protection."
    F: "The bill's sole substantive provision is the copyright-subpoena mechanism; nothing touches data centers, permitting, interconnection, or energy."
    R: "Applies to essentially the full universe of AI developers, with no revenue floor or sector carve-out limiting who can be subpoenaed."
    Depth: "Recomputed after the frontier/systemic-risk guardrail correction — now driven by axis A (frontier developer stringency) at 1.0/5."
    E_f: "Any copyright holder can get a subpoena from a federal court clerk on their own, without suing first or waiting on an agency — close to a private right of action, though it compels document production rather than creating a damages claim."
    P: "Modeled directly on the existing DMCA subpoena process, repurposed as a new framework for AI training-data disclosure — adapting an established tool rather than building something entirely new or a permanent institution."
    likelihood: "An unusually bipartisan lineup (Welch, Dean, Moran, plus original cosponsors Blackburn, Hawley, and Schiff) gives it real credibility, but neither chamber's version has seen a markup or floor vote through September 2026. Two offsetting signals since the last pass: Register of Copyrights Shira Perlmutter endorsed the TRAIN Act's subpoena approach in May 2026 Senate testimony, a positive for p_committee; but DOJ's September 1, 2026 statement of interest in NYT v. OpenAI, arguing AI training is fair use and warning that restricting it threatens national security, signals the administration's copyright/AI policy leans firmly deregulatory — a real headwind for enactment even if a committee vote were to happen. GovTrack.us was unreachable (403) this pass, so this stays a base-rate estimate rather than GovTrack-corroborated; p_committee nudged up slightly for the Copyright Office endorsement, p_enact held flat given the offsetting administration signal."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags: ["copyright", "training data", "transparency", "subpoena"]
sources:
  - label: "Congress.gov (House)"
    url: "https://www.congress.gov/bill/119th-congress/house-bill/7209"
  - label: "Congress.gov (Senate)"
    url: "https://www.congress.gov/bill/119th-congress/senate-bill/2455"
  - label: "IPWatchdog — DOJ statement of interest in NYT v. OpenAI (policy-climate context)"
    url: "https://ipwatchdog.com/2026/09/03/doj-sides-with-openai-warns-obstacles-to-ai-development-threaten-national-security/"
summary: "Would let copyright holders subpoena AI companies to check if their work was used to train AI models."
timeline:
  - date: "2025-07-24"
    event: "S. 2455 introduced in the Senate by Sen. Welch, with Sens. Blackburn, Hawley, and Schiff; referred to Senate Judiciary Committee"
  - date: "2026-01-22"
    event: "H.R. 7209 introduced in the House by Rep. Dean, with Rep. Moran; referred to House Judiciary Committee"
  - date: "2026-05-01"
    event: "Legal press (Berkeley Technology Law Journal) confirms the bill remains early-stage in both chambers"
  - date: "2026-05-01"
    event: "Register of Copyrights Shira Perlmutter endorses the TRAIN Act's subpoena mechanism in Senate testimony, calling it 'a very creative idea'"
  - date: "2026-09-01"
    event: "DOJ files a statement of interest in NYT v. OpenAI (S.D.N.Y.) arguing AI training on copyrighted works is fair use, signaling an administration posture at odds with the bill's premise"
  - date: "2026-09-09"
    event: "Re-verified: no markup or floor action in either chamber since introduction."
---
The TRAIN Act would let a copyright holder who has a good-faith belief their work was used without authorization to train a generative AI model obtain a subpoena — issued by a federal court clerk, without first filing a lawsuit — compelling the AI developer to produce copies of, or records identifying, the copyrighted works used in training. It's modeled directly on the existing DMCA subpoena process used to identify online infringers, repurposed here to compel disclosure of AI training data.

The Senate version came first, introduced by Sen. Welch with an unusual bipartisan lineup of original cosponsors (Blackburn, Hawley, and Schiff) in July 2025; the House companion followed six months later from Reps. Dean and Moran. Neither has seen committee action since its introduction.

Update (September 2026): Register of Copyrights Shira Perlmutter praised the bill's subpoena approach in May 2026 testimony, but the Justice Department's September 1, 2026 fair-use filing in the NYT v. OpenAI litigation signals the administration favors leaving AI training largely unregulated — a headwind for this and other copyright-transparency bills even absent any committee action to date.
