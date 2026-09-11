---
title: AI Accountability and Personal Data Protection Act
short_name: AI Accountability and Personal Data Protection Act
bill_numbers:
- S. 2367
congress: 119
topic: Transparency & Copyright
status: committee
chamber_origin: Senate
introduced_date: '2025-07-21'
last_action: Read twice and referred to the Senate Committee on the Judiciary
last_action_date: '2025-07-21'
sponsors:
- Sen. Josh Hawley (R-MO)
- Sen. Richard Blumenthal (D-CT)
cosponsor_count: 2
committees:
- Senate Judiciary
scoring:
  axes:
    A: 1.0
    B: 1.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 5.0
  impact_components:
    R: 1.0
    D: 1.0
    E_f: 1.0
    P: 0.4
  likelihood:
    p_committee: 0.28
    p_enact: 0.05
    basis: "base_rate_adjusted"
  rationale:
    A: "Guardrail check (frontier/systemic risk vs. near-term consumer harm): the mandate here is express prior consent before personal data can be used to train AI — a privacy/consent tort, not a mechanism aimed at frontier-scale training, catastrophic/CBRN risk, loss-of-control, or systemic AI oversight. Its subject is personal-data protection, which is exactly what axis E exists to hold. This is a genuine borderline case rather than an automatic floor discount, though: unlike a chatbot bill's child-safety mandate (which binds one narrow sector), this constrains a training *input* — personal data — across the entire AI industry, with no sectoral or demographic carve-out, so it isn't purely a narrow-population consumer bill either. That universality earns it some residual A weight rather than a full drop to 0, but the mandate still doesn't touch frontier-scale capability, compute, or catastrophic-risk conduct, so it lands well below the previous 2.0 (a 'mandated process with enforcement' read that took the private-right-of-action language at face value without asking whether the underlying subject was frontier governance). Scored 1.0 — real, universal, enforceable, but a consent/disclosure-type constraint on an input rather than governance of frontier development itself; the bill's true severity belongs on E_consumer (unchanged at 5.0)."
    B: "Guardrail check: Section 4's savings clause ('nothing in the Act preempts or limits any state law, rule, regulation, or common-law doctrine') is the standard form of an ordinary savings clause — by construction it only speaks to what this Act itself would otherwise preempt, and this Act's entire subject is personal-data-training-consent. Per the guardrail, a savings clause scoped to the bill's own narrow topic doesn't earn the '+3 affirmative guarantee' rung just because its wording is unconditional; it says nothing about states' authority to regulate frontier AI development broadly. There is no independent language here preserving state AI-regulation authority outside this bill's own lane, so this caps at the ordinary-savings-clause rung. Also, since A now scores well below +2, the implicit-preemption floor that would otherwise have been irrelevant to a +3 read doesn't change this conclusion either way. Scored 1.0, down from 3.0."
    C: "A private right of action only — no new agency, database, or enforcement staff is created, so it doesn't expand government's own capacity to monitor or enforce. Consistent with the frontier/systemic-risk guardrail as well: even if some capacity mechanism existed here, a personal-data-consent regime is not systemic AI oversight capacity — but the bill contains no such mechanism at all, so this remains 0 unchanged."
    D: "No export-control, chip-access, or geopolitical content."
    E_consumer: "Gives individuals a broad federal right to sue any AI or tech company that uses their personal data without consent."
    F: "No data-center, permitting, or energy content."
    R: "Covers any AI training activity affecting interstate or foreign commerce — as drafted, that reaches essentially the entire industry."
    Depth: "The private right of action to sue over unconsented data use is what gives this bill its teeth; nothing else in the text goes further."
    E_f: "Enforcement runs entirely through individual lawsuits rather than agency action or fixed penalties."
    P: "A self-contained data-training tort that pairs with the similarly-themed GUARD Act from the same sponsors, rather than a wholly new framework or permanent institution."
    likelihood: "Introduced in July 2025 by a bipartisan Hawley-Blumenthal pairing but still sitting at its initial Judiciary Committee referral over a year later with only two cosponsors — sponsorship pedigree without visible momentum. GovTrack.us was unreachable (403) for this pass; no committee markup, hearing, or floor action has been reported through September 2026, and DOJ's September 1, 2026 statement of interest backing AI-training-as-fair-use in the NYT v. OpenAI litigation signals the administration favors the opposite policy direction, which if anything lowers already-thin odds. Estimate remains base-rate-adjusted, nudged down slightly for lack of any forward motion in fourteen months."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- copyright
- personal data
- private right of action
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/2367
- label: "DOJ statement of interest, NYT v. OpenAI (context on copyright/AI policy climate)"
  url: https://ipwatchdog.com/2026/09/03/doj-sides-with-openai-warns-obstacles-to-ai-development-threaten-national-security/
summary: Creates a private right to sue over AI training on personal data without prior consent.
timeline:
- date: '2025-07-21'
  event: Introduced in the Senate
- date: '2025-07-21'
  event: Read twice and referred to the Judiciary Committee
- date: '2026-09-09'
  event: "Re-verified: no committee markup or floor action since referral; still 2 cosponsors as of last available check."
---

The bill establishes a federal civil cause of action letting individuals sue over the appropriation, use, collection, sale, or other exploitation of their personal data without express prior consent, aimed at AI training on personal and copyrighted works. It applies to activity affecting interstate or foreign commerce and is framed by its sponsors as empowering creators to sue AI and tech companies. Sens. Hawley and Blumenthal, who also co-lead the GUARD Act tracked here, jointly announced it.

Update (September 2026): still sitting at its initial Judiciary Committee referral with no markup scheduled; the Justice Department's September 1, 2026 fair-use filing in NYT v. OpenAI underscores an administration posture unfavorable to this bill's underlying theory.
