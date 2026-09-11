---
title: "Children's Health, Advancement, Trust, Boundaries, and Oversight in Technology Act (CHATBOT Act)"
short_name: "CHATBOT Act"
bill_numbers: ["S. 4407"]
congress: 119
topic: "Children & Chatbots"
status: "committee_passed"
chamber_origin: "Senate"
introduced_date: "2026-04-28"
last_action: "Senate Commerce, Science, and Transportation Committee ordered S. 4407 (as amended by a Cruz-Schatz-Curtis substitute) reported to the full Senate by voice vote during Executive Session 24"
last_action_date: "2026-08-05"
sponsors: ["Sen. Ted Cruz (R-TX)", "Sen. Brian Schatz (D-HI)", "Sen. John Curtis (R-UT)", "Sen. Adam Schiff (D-CA)"]
cosponsor_count: 3
committees: ["Senate Commerce, Science, and Transportation"]
scoring:
  axes:
    A: 0.5
    B: -1.0
    C: 0.5
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.0
  impact_components:
    R: 1.0
    D: 0.40
    E_f: 0.60
    P: 0.60
  likelihood:
    p_committee: 1.0
    p_enact: 0.32
    basis: "base_rate_adjusted"
  rationale:
    A: "CORRECTED 2026-09-09 (known issue) per the frontier/systemic-risk-vs-near-term-consumer-harm guardrail. Requires chatbot companies to build 'family account' infrastructure, verifiable parental consent for teens, parental monitoring of conversations, restrictions on manipulative/engagement-maximizing design, and a ban on targeted ads to minors. This textually matches the '+2 mandated process' rung, but the mandate's subject is parental controls and design restrictions for child safety, not frontier-scale training, catastrophic/CBRN risk, loss-of-control, or systemic AI oversight — nothing here reaches frontier developers as such. Per the guardrail, a real enforced child-safety/consumer conduct mandate like this belongs near A's floor (rarely above +0.5-+1), with severity carried on axis E instead. Previously scored 2.0; corrected to 0.5."
    B: "Section 9(a) preempts state law only where it conflicts with the Act, and Section 9(b)(1) explicitly preserves states' ability to pass laws offering children greater protection — narrow, conflict-only preemption rather than a broad displacement of state authority. This is an express textual conflict-preemption clause (not an implicit-preemption-floor inference tied to axis A), so the A correction above doesn't change this score: -1.0 (conflict preemption only) stands on its own textual merits."
    C: "CORRECTED 2026-09-09 per the frontier/systemic-risk-vs-near-term-consumer-harm guardrail. Section 10's NSF-commissioned study and Section 11's GAO report both examine chatbots' effects on children/teens and this Act's own child-safety effectiveness — a narrow child-safety study pipeline, not a mechanism observing frontier-scale or systemic AI risk or building general government AI-oversight capacity. Per the guardrail, this belongs near C's floor (rarely above +0.5-+1) despite textually resembling the '+1' study rung. Previously scored 1.0; corrected to 0.5."
    D: "No export-control or geopolitical content."
    E_consumer: "A broad parental-control and design-restriction regime for minors' chatbot use, including a ban on targeted advertising to minors — a real cross-sector consumer-protection mandate built on consent and design requirements rather than a private right of action or a new criminal offense."
    F: "No data-center or energy content."
    R: "A federal bill; its family-account, consent, and ad-restriction requirements apply to AI chatbot companies generally, with no size or revenue carve-out."
    Depth: "Driven jointly by the parental-control mandate (A) and the consumer-protection design restrictions (E) — a meaningful compliance regime without reaching into deeper structural territory."
    E_f: "No explicit penalty or private-right-of-action structure is spelled out; enforcement reads as AG/FTC-style, typical of consumer-protection design mandates of this kind."
    P: "Joins an already-established cluster of chatbot child-safety bills — grouped here with the CHAT Act, GUARD Act, and SANDBOX Act — rather than breaking new ground."
    likelihood: "Recomputed 2026-09-09 now that the bill has actually cleared committee: Senate Commerce ordered S. 4407 (as amended) reported to the full Senate by voice vote on 2026-08-05, as part of a four-bill kids'-online-safety package alongside KOSA, the Youth AI Privacy Act, and the AI Toy Safety bill — so p_committee is set to 1.0 (the event has already occurred), up from the stale 0.65 pre-markup estimate. p_enact is raised accordingly but not to a comparably high level: no Senate floor vote has been scheduled as of 2026-09-09, GovTrack's govtrack.us prognosis page returned HTTP 403 on lookup so no external model number is available here (noted rather than guessed), and this bill's committee-passed status doesn't resolve the floor-scheduling bottleneck facing the whole four-bill package — most notably that KOSA in the same package remains contested over the House KIDS Act's missing 'duty of care' language, which could delay floor time for its Senate Commerce package-mates including this bill. Base rate for a bipartisan, chair-authored bill unanimously ordered reported out of its committee of jurisdiction is meaningfully higher than a bill still awaiting markup, but Senate floor time is scarce and contested, so p_enact is set in the 0.30s rather than higher."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags: ["chatbots", "child safety", "parental controls"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/senate-bill/4407"
  - label: "Sponsor press release"
    url: "https://www.commerce.senate.gov/press/rep/release/cruz-schatz-curtis-schiff-introduce-new-bill-giving-parents-control-over-kids-ai-chatbot-use/"
  - label: "Senate Commerce Committee — CHATBOT Act advances to the Senate floor"
    url: "https://www.commerce.senate.gov/press/rep/release/cruz-schatzs-chatbot-act-advances-to-the-senate-floor/"
  - label: "Senate Commerce Committee — Executive Session 24"
    url: "https://www.commerce.senate.gov/meetings/executive-session-24-08-05-2026/"
  - label: "Senate Commerce Committee — Commerce Committee Advances Kids Online Safety Legislation (four-bill package incl. CHATBOT Act, KOSA, Youth AI Privacy Act, AI Toy Safety bill)"
    url: "https://www.commerce.senate.gov/press/rep/release/commerce-committee-advances-kids-online-safety-legislation/"
summary: "Bipartisan Senate bill requiring parental-consent 'family accounts' and parental controls for minors' AI chatbot use."
timeline:
  - date: "2026-04-28"
    event: "Introduced by Sen. Cruz with Sens. Schatz, Curtis, and Schiff; referred to Senate Commerce Committee"
  - date: "2026-08-05"
    event: "Senate Commerce Committee ordered the CHATBOT Act (as amended) reported to the full Senate by voice vote"
---
The CHATBOT Act would require AI chatbot companies to create "family accounts" giving parents oversight of minors' chatbot use, mandate verifiable parental consent for teen users, restrict manipulative or engagement-maximizing design features, let parents monitor a child's chatbot conversations, and ban targeted advertising to minors.

Sen. Cruz chairs the Senate Commerce Committee — the same committee that controls the SANDBOX Act, also tracked on this page — giving this bill a real structural path to a markup that solo-sponsored bills in this cluster lack. It shares a short-title acronym with an unrelated House bill, H.R. 7985 ("Curbing Harmful AI Tools By Offering Transparency Act"), which addresses chatbots falsely claiming professional credentials rather than child safety; the two are not companions.

**Update (2026-09-09):** No Senate floor vote has been scheduled yet. The bill moved as part of a four-bill Senate Commerce package (with KOSA, the Youth AI Privacy Act, and the Children's Artificial Intelligence Toy Safety Act) reported out 2026-08-05 — floor scheduling for the whole package may be affected by the unresolved Senate-House standoff over KOSA's "duty of care" provision, which the House's competing KIDS Act omitted.
