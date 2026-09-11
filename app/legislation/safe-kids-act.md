---
title: "Safeguarding AI Features to Ensure Kids' Informed Digital Safety Act (SAFE KIDS Act)"
short_name: "SAFE KIDS Act"
bill_numbers: ["S. 4855"]
congress: 119
topic: "Children & Chatbots"
status: "introduced"
chamber_origin: "Senate"
introduced_date: "2026-06-23"
last_action: "Read twice and referred to the Senate Committee on Commerce, Science, and Transportation"
last_action_date: "2026-06-23"
sponsors: ["Sen. John Curtis (R-UT)", "Sen. Adam Schiff (D-CA)"]
cosponsor_count: 1
committees: ["Senate Commerce, Science, and Transportation"]
scoring:
  axes:
    A: 0.5
    B: 1.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 3.0
  impact_components:
    R: 1.0
    D: 0.60
    E_f: 0.80
    P: 0.80
  likelihood:
    p_committee: 0.35
    p_enact: 0.09
    basis: "base_rate_adjusted"
  rationale:
    A: "RE-SCORED 2026-09-09 under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: Sec. 4's pre-deployment/annual risk assessments, crisis-response protocols, and Sec. 7 third-party audits are a real, enforced mandate, but its subject is child-safety design in deployed chatbots, not frontier-scale training, catastrophic/CBRN risk, or systemic AI oversight — the guardrail directs axis A to the floor (rarely above +0.5-+1) for exactly this pattern, regardless of how well-drafted or enforced the mandate is. Scored at 0.5 rather than 0.0 to reflect that it is still a real, FTC-enforced conduct mandate on chatbot providers (above a pure disclosure-only bill), but it is not frontier-developer stringency."
    B: "RE-SCORED 2026-09-09 under the same guardrail: Sec. 9(a)'s savings clause is textually unconditional but scoped to state law 'at least as protective of users of AI chatbots as this Act' — i.e., it guarantees states may pass more-protective chatbot-safety law, not that states retain authority to regulate frontier AI development generally. Per the guardrail, that caps this at the '+1 ordinary savings clause' rung rather than the '+3 affirmative guarantee with teeth' rung, which is reserved for preservation language that is genuinely general rather than scoped to the bill's own narrow topic."
    C: "RE-SCORED 2026-09-09 under the same guardrail: Sec. 6's FTC third-party incident-reporting mechanism and Sec. 7(c)'s annual aggregated-audit report are a genuine standing information flow, but what they observe is child-safety incidents and audit compliance in deployed chatbots, not frontier/systemic AI risk — the guardrail's own worked example is exactly this pattern (a chatbot bill's FTC incident-reporting requirement matching the '+3' rung textually while not being what that rung describes). Following the STOP CSAM Act's precedent for an analogous FTC/DOJ reporting regime (scored C=0.5), this drops to 1.0, reflecting that the registry is somewhat more structurally built-out (a standing public registry plus researcher data access, not just annual aggregate reporting) than STOP CSAM's reporting regime, but still capped near the floor rather than at +3."
    D: "No export-control or geopolitical content."
    E_consumer: "Sec. 5 bans advertising and cross-context behavioral advertising to child users and bans sale/sharing of children's personal information absent verifiable parental consent, all backed by FTC UDAP enforcement with civil penalties up to $10,000 per violation per user for willful violations (Sec. 8) — a broad cross-sector restriction with real agency-enforced penalties, though not a private right of action, landing between the '3' (criminal-liability-equivalent civil penalty regime) and '5' (private right of action) rungs; scored at 3."
    F: "No data-center or energy content."
    R: "A federal bill covering any 'AI chatbot' made available to a user in the US, with narrow exclusions only for customer-service, internal-enterprise, and narrow-purpose systems — R close to 1.0 for a bill in the developer/consumer-facing chatbot class."
    Depth: "Driven jointly by the strong preemption posture (B=+3), the standing FTC registry/reporting regime (C=+3), and the broad ad/data-sale restrictions (E=3) — a substantively deep bill across multiple axes rather than concentrated in just one."
    E_f: "FTC UDAP enforcement (Sec. 8) with specified per-violation, per-user civil penalties ($1,000 baseline, $10,000 for willful violations) — agency rulemaking plus civil penalties, the '0.8' rung; no private right of action for individuals."
    P: "A first-in-cluster framework: unlike the CHATBOT Act, CHAT Act, GUARD Act, and CHAT Act 2.0, this bill pairs child-safety design mandates with an annual independent third-party audit regime disclosed through a public FTC registry — a more novel accountability structure than parental-consent-only approaches, likely to be referenced by later bills; scored at 0.80 rather than the cluster-standard 0.60."
    likelihood: "Introduced 2026-06-23 with a single cosponsor (Schiff) and referred to Senate Commerce; no committee markup, hearing, or further cosponsor addition found as of 2026-09-09. GovTrack's own prognosis page (govtrack.us/congress/bills/119/s4855) returned HTTP 403 on lookup, so no external model number is available and none is asserted here. Senate Commerce has been actively moving a crowded slate of chatbot child-safety bills (the CHATBOT Act, Youth AI Privacy Act, and AI Toy Safety bill cleared committee 2026-08-05 as a package), but SAFE KIDS was not part of that package and carries a materially heavier compliance regime (independent audits, FTC registry) than the bills that did advance — raising the bar for industry and committee buy-in. p_committee is set moderately (bipartisan sponsor pair, same committee of jurisdiction as bills that have already moved) but below the CHATBOT Act's committee-passed 1.0; p_enact reflects that even bills in the same committee's advancing package face an unresolved floor-scheduling bottleneck (the KOSA 'duty of care' standoff), and this bill has not yet even reached that package."
  confidence: low
  text_source: full_text
  scored_at: "2026-09-09"
tags: ["chatbots", "child safety", "parental controls", "audits"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/senate-bill/4855"
  - label: "Bill text (GovInfo)"
    url: "https://www.govinfo.gov/content/pkg/BILLS-119s4855is/pdf/BILLS-119s4855is.pdf"
  - label: "Sen. Curtis press release — Curtis, Schiff Introduce Bipartisan Legislation to Protect Children from AI Chatbot Risks"
    url: "https://www.curtis.senate.gov/press-releases/curtis-schiff-introduce-bipartisan-legislation-to-protect-children-from-ai-chatbot-risks/"
  - label: "Sen. Schiff press release"
    url: "https://www.schiff.senate.gov/news/press-releases/news-sens-schiff-curtis-unveil-new-bipartisan-legislation-to-protect-children-from-ai-chatbot-risks/"
summary: "Bipartisan Senate bill requiring AI chatbot providers to implement child-safety-by-design, parental controls, and annual independent audits, and banning child-targeted ads and data sale."
timeline:
  - date: "2026-06-23"
    event: "Introduced by Sen. Curtis with Sen. Schiff; referred to Senate Commerce Committee"
---
The SAFE KIDS Act would require providers of AI chatbots to conduct documented pre-deployment and annual child-safety risk assessments, implement crisis-response protocols (including parental notification for imminent risk of suicide or self-harm and referral to external crisis resources), offer a detailed parental-settings program, submit to annual independent third-party child-safety audits reviewed by the FTC, and publish child safety policies. It separately bans advertising and cross-context behavioral advertising directed at children and bans the sale or sharing of children's personal information without verifiable parental consent. The FTC enforces the Act as an unfair-or-deceptive-practices violation, with per-violation, per-user civil penalties running as high as $10,000 for willful violations.

The bill sits in the same crowded Senate Commerce cluster of chatbot child-safety bills as the CHATBOT Act, CHAT Act, and GUARD Act, but is the only one of that group to pair its design mandates with a recurring independent-audit regime feeding a public FTC registry — a heavier compliance structure than the parental-consent-centered approach most of its peers take. Its preemption posture is also unusually protective of state authority: Sec. 9 preserves any state law that is at least as protective of AI chatbot users, and expressly bars providers from treating compliance with the Act as a defense against liability under other law.
