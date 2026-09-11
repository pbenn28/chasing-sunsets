---
title: Artificial Intelligence Scam Prevention Act
short_name: AI Scam Prevention Act
bill_numbers:
- S. 3495
congress: 119
topic: Deepfakes & Synthetic Media
status: committee
chamber_origin: Senate
introduced_date: '2025-12-16'
last_action: Read twice and referred to the Senate Committee on Commerce, Science, and Transportation
last_action_date: '2025-12-16'
sponsors:
- Sen. Amy Klobuchar (D-MN)
- Sen. Shelley Moore Capito (R-WV)
committees:
- Senate Commerce, Science, and Transportation
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.0
  impact_components:
    R: 0.90
    D: 0.40
    E_f: 0.60
    P: 0.40
  likelihood:
    p_committee: 0.25
    p_enact: 0.06
    basis: "base_rate_adjusted"
  rationale:
    A: "The bill bars using AI to replicate a person's image or voice with intent to defraud, codifies an FTC ban on AI-assisted government/business impersonation, and requires anyone making a call or text that uses AI to emulate a human to disclose that fact (Sec. 4). Every one of these obligations runs against the person placing the call, sending the text, or committing the fraud — not against a developer of a frontier or general-purpose AI model. This is a domain-general telemarketing/fraud-disclosure mechanism that happens to name AI as the covered technology, not a conduct standard on AI development or deployment as such; per the AI-governance-scoping guardrail, that caps it at 0 on this axis rather than treating the caller-facing AI-disclosure duty as if it were a developer obligation."
    B: "No preemption or savings-clause language anywhere in the bill. It amends the Telemarketing and Consumer Fraud and Abuse Prevention Act and the Communications Act of 1934 but is silent on state authority to regulate AI-enabled scams independently. The implicit-preemption floor doesn't apply because A scores 0, not ≥ +2."
    C: "Establishes a Federal Trade Commission/Federal Communications Commission-chaired Artificial Intelligence Scams Advisory Group with Treasury, DOJ, and CFPB representation, tasked with collecting information and issuing annual reports and recommendations to Congress for five years, plus an annual FTC report to Congress on AI-enabled scams (Sec. 5). This is a real, deadline-driven advisory/reporting structure rather than a study with no follow-through, but it produces reports and recommendations rather than a mandatory incident-reporting database or new enforcement staffing — so it lands at +1 rather than +2 or +3."
    D: "No export-control or geopolitical content."
    E_consumer: "Prohibits AI-enabled impersonation-to-defraud and mandates AI-disclosure on calls/texts, both enforced as FTC unfair-or-deceptive-practice violations (civil, not criminal) with no private right of action — stronger than a bare labeling-only rule because it also bars a category of fraudulent conduct outright, but civil FTC enforcement without criminal liability or a private right of action keeps it below the criminal-liability rung, landing at 2."
    F: "No data-center, permitting, siting, or energy provisions."
    R: "The impersonation ban and AI-disclosure mandate apply to any person using AI to defraud or to emulate a human in a call/text, with no revenue or sector carve-out — a broad, uncapped class."
    Depth: "Bounded by C (1) and E_consumer (2); the bill contains no compute, preemption, or frontier-developer-stringency content, so Depth reflects a modest, consumer/telemarketing-focused reach rather than a structurally deep intervention."
    E_f: "FTC enforcement under its existing unfair-or-deceptive-practices authority, incorporating the full FTC Act's powers and penalties — real agency teeth, but no private right of action and no criminal exposure, placing it at the agency-rulemaking-plus-civil-penalties rung rather than the top of the ladder."
    P: "A sector-specific, self-contained scam-prevention and disclosure framework bolted onto existing telemarketing and communications law, with a five-year sunset on the advisory group — not a new permanent institution or a template obviously destined to spread beyond robocall/impersonation scams."
    likelihood: "A bipartisan Klobuchar(D)-Capito(R) Commerce Committee bill addressing a high-salience problem (nearly $2 billion in phone/text scam losses in 2024 per the findings section), but still at its initial committee referral roughly nine months after introduction with no hearing or markup reported. GovTrack.us was unreachable for this pass; base rates for bipartisan Commerce Committee consumer-protection bills without a scheduled hearing this far into a session support modest committee odds and low overall enactment odds absent attachment to a larger vehicle (e.g., a telecom or FTC reauthorization package)."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- deepfakes
- fraud
- impersonation
- robocalls
- FTC
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/3495
- label: Sen. Klobuchar press release
  url: https://www.klobuchar.senate.gov/public/index.cfm/2025/12/klobuchar-capito-introduce-bipartisan-artificial-intelligence-scam-prevention-act
- label: Bill text (Congress.gov PDF)
  url: https://www.congress.gov/119/bills/s3495/BILLS-119s3495is.pdf
summary: Bars AI impersonation used to defraud, requires AI disclosure on robocalls/texts, and creates an interagency scam-prevention advisory group.
timeline:
- date: '2025-12-16'
  event: Introduced by Sen. Klobuchar with Sen. Capito; referred to Senate Commerce, Science, and Transportation
- date: '2026-09-09'
  event: "Verified: no hearing or markup reported since referral."
---

The Artificial Intelligence Scam Prevention Act would make it unlawful to engage in a deceptive act or practice by impersonating a government official, business, or business official, or to replicate any individual's image or voice — including through AI — with intent to defraud, and to knowingly provide substantial assistance to someone doing either. Violations are treated as FTC unfair-or-deceptive-practices violations, enforced with the full jurisdiction, powers, and penalties of the FTC Act, and the bill preserves the FTC's authority under any other law. It amends the Seniors Fraud Prevention Act to fold AI-enabled scams into existing senior-fraud outreach.

The bill separately amends the Telemarketing and Consumer Fraud and Abuse Prevention Act and the Communications Act of 1934 to extend telemarketing/robocall rules to text messages and video-conference calls, and to require that anyone who places a call or sends a text using AI to emulate a human being must promptly and clearly disclose that AI is being used. It creates an FTC/FCC-chaired Artificial Intelligence Scams Advisory Group (with Treasury, DOJ, CFPB, and industry/consumer-advocacy representatives) that collects information on scam-prevention education, identifies gaps, and reports annually to the relevant House and Senate committees for five years before sunsetting; the FTC must also separately report annually to Congress on AI-enabled scams. No provision addresses state authority to regulate AI-enabled scams independently — the bill is silent on preemption in either direction.
