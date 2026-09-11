---
title: Right to Override Act
short_name: Right to Override Act
bill_numbers:
- S. 2997
congress: 119
topic: Healthcare
status: committee
chamber_origin: Senate
introduced_date: '2025-10-09'
last_action: "Read twice and referred to the Senate Committee on Health, Education, Labor, and Pensions"
last_action_date: '2025-10-09'
sponsors:
- Sen. Ed Markey (D-MA)
- Sen. Richard Blumenthal (D-CT)
cosponsor_count: 1
committees:
- Senate Health, Education, Labor, and Pensions
scoring:
  axes:
    A: 0.5
    B: 1.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 3.5
  impact_components:
    R: 0.30
    D: 0.70
    E_f: 1.00
    P: 0.50
  likelihood:
    p_committee: 0.10
    p_enact: 0.02
    basis: "base_rate_adjusted"
  rationale:
    A: "The obligation runs against healthcare employers/covered entities that deploy AI/CDSS tools, not against developers of frontier or general-purpose AI systems — applying the guardrail, this is a sector-specific deployer/employer conduct standard, not frontier-developer stringency. To the extent it touches AI governance at all on axis A's terms, it's closest to the '+0.5 procurement/government-use'-style rung in spirit (binding the buyer/deployer of a tool, not the builder), though this is a private employer rather than a government purchaser, so it's scored at +0.5 as a bounded analogue rather than a genuine developer obligation."
    B: "Contains an explicit, on-point savings clause: 'Nothing in this Act shall preempt a State law or collective bargaining agreement,' and separately preserves medical malpractice claims. This is the rubric's 'ordinary savings clause bolted onto a substantive bill' rung (+1) — express, unambiguous, and specifically on the preemption question, which also forecloses the implicit-preemption floor (moot here anyway since A doesn't reach +2)."
    C: "Enforcement runs through existing HHS and DOL authority (civil monetary penalties under Social Security Act procedures, DOL complaint processing) rather than a new agency, evaluation body, or standing incident database — this expands what existing regulators can penalize, not what they can see or staff, so it scores 0 rather than the +2 'enforcement staffing or new authority' rung; the per-facility internal AI/CDSS oversight committees are a private, not governmental, capacity build."
    D: "No export-control, chip-access, or geopolitical content."
    E_consumer: "A private right of action exists specifically for retaliation/whistleblower violations (Title II, DOL track), with statutory damages of $10,000-$100,000 per violation, treble damages, and attorney's fees — but the core override-mandate and committee-structure provisions (Title I) are enforced only through HHS civil penalties, not a private suit. Because the private right of action is real but confined to the retaliation piece rather than reaching the full scope of the Act's substantive requirements, this lands just below the rubric's top 'broad private right of action across sectors' rung, at 3.5 — criminal liability is not present, so it clears the '+3 criminal liability' rung comfortably but doesn't reach a full, unqualified 5."
    F: "No data-center, permitting, siting, or energy content."
    R: "Confined to one sector (healthcare facilities and health plans using AI/CDSS tools for clinical decisions) — real and plausibly comprehensive within that sector once in effect, but healthcare is a bounded slice of the broader AI-deployment landscape, so R is scored well below 1.0 relative to a bill reaching AI use across the economy."
    Depth: "max(|A|, |B|, |C|, |F|, E) / 5 = max(0.5, 1, 0, 0, 3.5) / 5 = 0.70 — driven by the E_consumer score, since the whistleblower private right of action and its statutory damages are the bill's most stringent single mechanism."
    E_f: "Administrative penalties up to $76,987 per violation (indexed, HHS) plus a private right of action with statutory and treble damages for retaliation — the maximum enforceability rung, combining agency rulemaking/penalties with a genuine private suit."
    P: "Would be a first-in-nation statutory clinician-override right for AI/CDSS tools with anonymity and whistleblower protections attached — a template plausibly copied by states or extended to other high-stakes AI-deployment sectors, but it's sector-specific to healthcare and self-contained rather than a general AI-governance framework, landing at the midpoint 'sector-specific and self-contained' to 'first-in-nation framework likely to be copied' boundary; scored 0.5 to reflect real precedent value without a permanent new institution."
    likelihood: "Verified 9/9-9/10/26: S. 2997 was introduced 2025-10-09 by Sen. Markey with Sen. Blumenthal as the sole cosponsor, and referred to Senate HELP, where it has seen no hearing, markup, or further action in the roughly 11 months since referral. No GovTrack prognosis page with a specific modeled probability was found for this bill as of this writing; in its absence, likelihood is set using the historical base rate for a two-Democrat-sponsored Senate bill in a Republican-controlled Senate with no Republican cosponsor and no companion House bill identified — a class of bill that clears committee only rarely and is enacted well under 5% of the time. Endorsements from National Nurses United, AFT, and CWA give it labor-advocacy visibility but no floor-moving Republican support has been reported."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- healthcare
- clinical decision support
- whistleblower protection
- clinician override
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/2997
- label: Sponsor press release — Sen. Ed Markey
  url: https://www.markey.senate.gov/news/press-releases/senator-markey-introduces-legislation-requiring-human-oversight-of-health-care-decisions-to-protect-patients-and-health-workers
summary: Requires healthcare employers to allow clinicians to override AI clinical-decision-support outputs and protects them from retaliation for doing so.
timeline:
- date: '2025-10-09'
  event: Introduced by Sen. Ed Markey with Sen. Richard Blumenthal; read twice and referred to Senate HELP
---

The Right to Override Act requires covered healthcare entities that use AI/clinical-decision-support systems (AI/CDSS) to adopt policies ensuring AI outputs never substitute for a healthcare professional's independent judgment, and that professionals can override an AI/CDSS output in a timely manner when their judgment warrants it. Covered entities must train staff on override procedures, keep individual override data anonymous (except to inform a patient or in legal proceedings), and establish an internal AI/CDSS oversight committee with at least equal non-manager representation. Section 202 bars retaliation — including intimidation, threats, coercion, or harassment — against workers who exercise rights under the Act, file complaints, seek assistance, or discuss potential violations with coworkers.

Enforcement is split: Title I gives HHS civil-monetary-penalty authority (up to $76,987 per violation, $769,870 for repeat violations, indexed annually) over the override-mandate and committee provisions; Title II gives the Department of Labor complaint-processing authority plus a private right of action for retaliation, with statutory damages of $5,000-$20,000 per adverse-action violation and $10,000-$100,000 per whistleblower violation, trebled for willful conduct, plus back pay, injunctive relief, and attorney's fees. The bill explicitly states it does not preempt any state law or collective bargaining agreement, and leaves medical malpractice claims unaffected. It is endorsed by National Nurses United, AFT, and the Communications Workers of America.
