---
title: AI Fraud Accountability Act
short_name: AI Fraud Accountability Act
bill_numbers:
- H.R. 7786
congress: 119
topic: Deepfakes & Synthetic Media
status: committee
chamber_origin: House
introduced_date: '2026-03-04'
last_action: Referred to four House committees; a cosponsor was later added
last_action_date: '2026-04-13'
sponsors:
- Rep. Vern Buchanan (R-FL)
cosponsor_count: 2
committees:
- House Energy and Commerce
- House Judiciary
- House Science, Space, and Technology
- House Foreign Affairs
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 0.5
    D: 1.0
    F: 0.0
  unsigned:
    E_consumer: 3.0
  impact_components:
    R: 0.90
    D: 0.60
    E_f: 0.80
    P: 0.40
  likelihood:
    p_committee: 0.25
    p_enact: 0.08
    basis: "base_rate_adjusted"
  rationale:
    A: "Corrected under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: this bill's entire subject is AI-generated impersonation fraud — a narrow consumer-harm domain (fraud/impersonation of officials and private individuals), not frontier-scale training, catastrophic risk, or systemic AI oversight. The FTC enforcement authority it grants runs against fraudulent conduct generally, not against frontier developers, and the underlying criminalized conduct is exactly the kind of near-term harm axis E exists to capture. Previously scored 1.0 by reading the FTC authority as a developer-facing mandated process; corrected down to sit near the guardrail's floor (rarely above +0.5-1), landing at 0.5 to reflect that there is no developer conduct standard here at all beyond an incidental AI-specific enforcement hook."
    B: "The bill's only savings clause is a narrow First Amendment carve-out protecting parody, satire, and journalism — not a state-authority provision — and there's no preemption language anywhere else in the text."
    C: "Corrected under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: the FTC enforcement authority this bill sharpens is scoped exclusively to AI-impersonation fraud, a narrow harm domain, not a standing information flow or enforcement capacity aimed at frontier/systemic AI oversight. Previously scored 2.0 (the 'enforcement staffing/new authority for existing regulator' rung) by reading the FTC-authority grant literally against that rung's wording; corrected down to sit near the guardrail's floor (rarely above +0.5-1), landing at 0.5 since the mechanism's object is fraud enforcement, not AI governance capacity."
    D: "Promotes international cooperation to go after foreign perpetrators of AI-enabled fraud — coordination language, not a hard export or compute control."
    E_consumer: "Criminalizes using realistic AI-generated impersonations, visual or audio, of identifiable people to commit fraud."
    F: "No data-center, permitting, or energy content."
    R: "The fraud-impersonation conduct it targets is broad and not narrowed by revenue or sector thresholds, reaching essentially the full universe of AI-enabled impersonation fraud."
    Depth: "max(|A|=0.5, |B|=0, |C|=0.5, |F|=0, E=3)/5 = 0.60, driven mainly by the criminal liability for AI-generated impersonation fraud (E), not by any frontier-developer or governance-capacity axis."
    E_f: "Backed by FTC enforcement authority plus criminal liability for the underlying fraud — real teeth, even without a private right of action."
    P: "A sector-specific, self-contained fix for impersonation fraud rather than a new institution or a template likely to spread beyond this niche."
    likelihood: "Referred to four separate House committees — Energy & Commerce, Judiciary, Science, and Foreign Affairs — which tends to slow things down, and cosponsorship remains thin with no committee markup in either chamber as of 9/9/26, five months after introduction. A companion bill (S. 3982) exists in the Senate, but neither chamber has scheduled action; the multi-committee referral in the House continues to look like the binding constraint."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- deepfakes
- fraud
- impersonation
- FTC
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/7786
summary: House bill criminalizing AI-generated digital impersonation fraud and empowering the FTC to enforce.
timeline:
- date: '2026-03-04'
  event: Introduced by Rep. Buchanan; referred to four committees
- date: '2026-04-13'
  event: Rep. Jefferson Van Drew added as cosponsor
- date: '2026-09-09'
  event: Re-verified — no committee markup in either chamber since April; still pending in four House committees and Senate Judiciary
---

The bill would establish protections against digital impersonation fraud by criminalizing the use of realistic AI-generated impersonations — visual or audio depictions of identifiable individuals — to commit fraud. It would grant the FTC clear enforcement authority and promote international cooperation to target foreign perpetrators. A Senate companion (S. 3982) also exists.
