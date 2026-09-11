---
title: "Children Harmed by AI Technology Act 2.0 (CHAT Act 2.0)"
short_name: "CHAT Act 2.0"
bill_numbers: ["S. 5154"]
congress: 119
topic: "Children & Chatbots"
status: "introduced"
chamber_origin: "Senate"
introduced_date: "2026-07-28"
last_action: "Read twice and referred to the Senate Committee on Commerce, Science, and Transportation"
last_action_date: "2026-07-28"
sponsors: ["Sen. Jon Husted (R-OH)", "Sen. Andy Kim (D-NJ)"]
cosponsor_count: 1
committees: ["Senate Commerce, Science, and Transportation"]
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 0.5
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 3.0
  impact_components:
    R: 1.0
    D: 0.60
    E_f: 0.80
    P: 0.60
  likelihood:
    p_committee: 0.15
    p_enact: 0.03
    basis: "base_rate_adjusted"
  rationale:
    A: "CORRECTED 2026-09-09 per the frontier/systemic-risk-vs-near-term-consumer-harm guardrail. Sec. 3-7 impose a tiered, risk-based conduct regime on 'covered entities' operating companion AI chatbots: baseline prohibitions on self-harm encouragement, sexual content with minors, human/professional impersonation, and manufactured emotional dependency (Sec. 3); mandatory age assurance and parental controls (Sec. 4); and heavier obligations for higher-risk tiers, including a Tier III bar on unsupervised minor use and a mandatory risk-management program (Sec. 7(4)). This textually resembles the '+2 mandated process' rung, but the mechanism's subject is child/companion-bot safety, not frontier-scale training, catastrophic/CBRN risk, loss-of-control, or systemic AI oversight — nothing in Sec. 3-7 reaches frontier model development. Per the guardrail, a real, enforced child-safety conduct mandate like this belongs near A's floor (rarely above +0.5-+1) with its actual severity carried on axis E instead. Previously scored 2.0; corrected to 0.5 to reflect a real, FTC/state-AG-enforced mandate that nonetheless has zero frontier/systemic-AI content."
    B: "CORRECTED 2026-09-09: previously floored at -1 via the implicit-preemption-floor rule, which triggers only when A >= +2 and the bill establishes a federal *AI-governance* regulatory scheme with no savings clause. Now that A is corrected to 0.5 (this is a child/companion-bot-safety conduct regime, not a frontier/systemic AI regulatory scheme), the floor's trigger condition no longer holds. Sec. 12(1) neither preempts nor preserves state authority over the Act's core content/design provisions -- it only touches other privacy/security law -- so the bill's actual text is silent on preemption of state chatbot/AI regulation. Corrected from -1.0 to 0.0 ('silent on preemption')."
    C: "CORRECTED 2026-09-09 per the frontier/systemic-risk-vs-near-term-consumer-harm guardrail. Sec. 8's one-time NIST study and Sec. 11's annual FTC compliance report both observe companion-chatbot child-safety compliance and harms (self-harm, manipulation, exploitation) -- a narrow child-safety compliance pipeline, not a mechanism that builds government capacity to observe or evaluate frontier-scale or systemic AI risk. Per the guardrail, this belongs near C's floor (rarely above +0.5-+1) even though it textually resembles the '+1' study rung and the '+3' standing-information-flow rung. Previously scored 1.5; corrected to 0.5 to reflect a real but narrow, non-frontier reporting/study pipeline."
    D: "No export-control or geopolitical content."
    E_consumer: "Sec. 3 and 9 impose broad, specific behavioral prohibitions (self-harm, sexual content, CSAM facilitation, deceptive emotional-dependency design) and data protections (targeted-ad ban, data-sale ban absent parental consent) enforced through FTC UDAP authority plus state-AG parens patriae civil actions that can obtain damages and restitution (Sec. 10(b)) — real cross-sector consumer-protection teeth beyond simple labeling, close to the criminal-liability-equivalent '3' rung given the availability of AG-sought damages, though it stops short of a private right of action for individuals."
    F: "No data-center or energy content."
    R: "A federal bill covering any 'companion AI chatbot' as broadly defined, with explicit carve-outs only for customer-service, business-operations, productivity, narrow voice-assistant, and video-game bots — R near 1.0 for the companion-chatbot class it targets."
    Depth: "Driven by the tiered conduct restrictions (A) and consumer-harm provisions (E) together, offset somewhat by the narrow, non-affirmative preemption posture (B) rather than a strong savings clause."
    E_f: "FTC UDAP enforcement (Sec. 10(a)) plus a parallel state-AG civil-action track that can seek damages, restitution, and injunctive relief (Sec. 10(b)) — agency rulemaking plus civil penalties, the '0.8' rung; no broad private right of action for individual users."
    P: "A revised, tiered-risk successor to Husted's own original CHAT Act (S. 2714), explicitly responding to industry pushback (carve-outs for customer-service/gaming bots) — refines an existing template rather than breaking new ground, joining the already-crowded CHATBOT Act/GUARD Act/SAFE KIDS Act cluster; scored at the cluster-standard 0.60 rather than higher, since the tiering approach modifies rather than originates a framework."
    likelihood: "Introduced 2026-07-28 with a single cosponsor (Kim) and referred to Senate Commerce; no committee markup found as of 2026-09-09. GovTrack's prognosis page (govtrack.us/congress/bills/119/s5154) returned HTTP 403 on lookup, so no external model number is available and none is asserted here. This is itself a successor to Sen. Husted's original CHAT Act (S. 2714, tracked separately on this page), introduced explicitly to address industry objections to the first version — the pivot signals real sponsor engagement but also means the bill is starting the committee process fresh rather than building on any accumulated momentum, and the original CHAT Act itself saw zero committee action in nearly a year. p_committee and p_enact are set low, consistent with a newly introduced, single-cosponsor bill entering an already-crowded field where Senate Commerce has prioritized other chatbot child-safety vehicles (the CHATBOT Act package) for markup."
  confidence: low
  text_source: full_text
  scored_at: "2026-09-09"
tags: ["chatbots", "child safety", "companion ai", "parental controls"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/senate-bill/5154"
  - label: "Bill text (GovInfo)"
    url: "https://www.govinfo.gov/content/pkg/BILLS-119s5154is/pdf/BILLS-119s5154is.pdf"
  - label: "Husted-Kim press release — Husted, Kim lead bipartisan bill to protect children from AI companion chatbots"
    url: "https://www.husted.senate.gov/media/press-releases/husted-kim-lead-bipartisan-bill-to-protect-children-from-ai-companion-chatbots/"
summary: "Bipartisan Senate bill establishing a tiered, risk-based framework restricting companion AI chatbot behavior toward minors; a revised successor to Sen. Husted's original CHAT Act."
timeline:
  - date: "2026-07-28"
    event: "Introduced by Sen. Husted with Sen. Kim; referred to Senate Commerce Committee"
---
CHAT Act 2.0 would establish a tiered, risk-based framework for "companion AI chatbots" — systems whose primary purpose is educational tutoring (Tier I), simulating friendship or companionship (Tier II), or mental-health/therapeutic support (Tier III) — with obligations that scale up by tier. All covered entities must prevent their chatbots from encouraging self-harm or violence, engaging minors in sexually explicit communication, impersonating humans or licensed professionals, or fostering emotional dependency, and must implement age assurance, parental controls, and a not-human disclosure. Tier II adds crisis-escalation protocols, parental notification of suicidal ideation, and a bar on persistent memory for minors; Tier III adds a bar on unsupervised minor use, a mandatory risk-management program, and a prohibition on the chatbot itself providing diagnoses or standalone mental-health care. The FTC enforces the Act as an unfair-or-deceptive-practices violation, with a parallel state-AG civil-action track.

This is a distinct successor bill to the CHAT Act (S. 2714/H.R. 7218), also tracked on this page, introduced by the same lead sponsor (Sen. Husted) roughly ten months later with a new cosponsor (Sen. Kim rather than Sen. Moreno) and a substantially revised approach — the tiered risk structure and carve-outs for customer-service, business, and video-game chatbots directly respond to industry objections to the original bill's blanket approach. S. 2714 itself has seen no committee action since its September 2025 introduction; this bill restarts the committee process rather than amending or replacing the original text through markup.

Unlike the SAFE KIDS Act and the original CHATBOT Act, this bill's only savings-clause language (Sec. 12(1)) is narrow — it preserves other privacy/security law only to the extent that law doesn't conflict with this Act, and says nothing about the Act's core content-restriction and design provisions, which is a materially weaker preemption posture than its Senate Commerce cluster-mates.
