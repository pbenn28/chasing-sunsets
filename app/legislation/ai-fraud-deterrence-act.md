---
title: AI Fraud Deterrence Act
short_name: AI Fraud Deterrence Act
bill_numbers:
- H.R. 6306
congress: 119
topic: Deepfakes & Synthetic Media
status: committee
chamber_origin: House
introduced_date: '2025-11-25'
last_action: Referred to the House Committee on the Judiciary
last_action_date: '2025-11-25'
sponsors:
- Rep. Ted Lieu (D-CA)
- Rep. Neal Dunn (R-FL)
cosponsor_count: 1
committees:
- House Judiciary
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 3.0
  impact_components:
    R: 0.90
    D: 0.60
    E_f: 0.60
    P: 0.40
  likelihood:
    p_committee: 0.15
    p_enact: 0.04
    basis: "base_rate_adjusted"
  rationale:
    A: "This is a pure sentencing-enhancement bill: it amends the mail fraud, wire fraud, bank fraud, money laundering, and federal-official-impersonation statutes (18 U.S.C. §§ 1341, 1343, 1344, 1956, 912) to add harsher fines/prison terms when the underlying crime 'is committed with the assistance of artificial intelligence.' The obligation runs against fraudsters generally, not against AI developers or deployers — it doesn't touch training, deployment, disclosure, or any developer-facing conduct standard. Per the domain-general-mechanism guardrail, a fraud-penalty statute that merely references AI as a sentencing factor is capped at 0 on this axis; there is no AI-governance channel here at all, contingent or otherwise."
    B: "No preemption or savings-clause language anywhere in the six-page bill. It amends federal criminal statutes only; state fraud law is untouched and not addressed. The implicit-preemption floor does not apply because A scores 0, not ≥ +2."
    C: "No new agency authority, reporting regime, staffing, or evaluation body — it only raises statutory penalty ceilings within the existing federal criminal-enforcement apparatus (DOJ prosecutes under the same statutes as before, just with higher fine/sentence caps)."
    D: "No export-control or geopolitical content; the findings section cites AI-enabled impersonation of U.S. officials in calls to foreign ministers, but the operative text is a domestic sentencing enhancement, not a foreign-access or export control."
    E_consumer: "Adds real criminal exposure — up to 30 years for AI-assisted bank fraud, 20 years for AI-assisted mail/wire fraud and federal-official impersonation, with an explicit AI definition borrowed from the National AI Initiative Act of 2020 — squarely criminal liability for specific AI-enabled conduct (rung 3), even though the underlying frauds (mail, wire, bank fraud, impersonation) are general-purpose rather than AI-specific in origin."
    F: "No data-center, permitting, or energy content."
    R: "The enhanced penalties apply to anyone who commits mail, wire, or bank fraud, money laundering, or federal-official impersonation with AI assistance — a broad, uncapped class with no revenue or sector threshold."
    Depth: "Bounded almost entirely by E_consumer (3); every safety-composite axis (A, B, C, F) scores 0, since the bill's only substantive lever is the criminal-penalty enhancement, which this rubric places on the unsigned consumer-harm axis rather than on frontier-developer stringency."
    E_f: "Backed by criminal prosecution under Title 18 with materially higher fines and sentences than the underlying fraud offenses already carry — real teeth, but no new civil enforcement body, agency rulemaking, or private right of action, so it sits at AG/DOJ-style enforcement rather than the top rung."
    P: "A narrow, self-contained sentencing add-on to existing fraud statutes rather than a new institution, framework, or template — several similar AI-sentencing-enhancement bills exist across recent Congresses (e.g., 118th Congress H.R. 10125 of the same name), so this is iterative, not first-in-nation."
    likelihood: "A bipartisan Lieu(D)-Dunn(R) pairing but only one cosponsor and no committee action reported in the roughly 9.5 months since its November 2025 introduction. GovTrack.us was unreachable for this pass; base rates for single-committee House bills with thin cosponsorship and no hearing scheduled this far into a session point to low odds of markup and very low odds of enactment absent it being folded into a larger vehicle (e.g., an omnibus criminal-justice or AI package)."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- deepfakes
- fraud
- impersonation
- sentencing
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/6306
- label: Rep. Lieu press release
  url: https://lieu.house.gov/media-center/press-releases/reps-lieu-and-dunn-introduce-bill-enhance-penalties-using-ai-commit
- label: Bill text (Congress.gov PDF)
  url: https://www.congress.gov/119/bills/hr6306/BILLS-119hr6306ih.pdf
summary: Raises criminal penalties for mail, wire, and bank fraud, money laundering, and federal-official impersonation when committed with AI assistance.
timeline:
- date: '2025-11-25'
  event: Introduced by Rep. Lieu with Rep. Dunn; referred to House Judiciary
- date: '2026-09-09'
  event: "Verified: no committee action reported since referral; still 1 cosponsor."
---

The AI Fraud Deterrence Act amends existing federal fraud statutes rather than creating any new AI-governance regime. It raises the mail-fraud and wire-fraud fine ceiling from $1 million to $2 million generally, and adds a specific AI-assistance enhancement (fine up to $1 million or up to 20 years' imprisonment) when either offense is "committed with the assistance of artificial intelligence." Bank fraud gets a parallel AI enhancement of up to $2 million or 30 years. Money-laundering penalties get a similar AI-assistance enhancement tied to the value of the funds involved. The bill also amends the federal-official-impersonation statute (18 U.S.C. § 912) to specify that impersonation "including with the use of artificial intelligence" is covered, adds an AI-assistance sentencing enhancement (up to $1 million or 3 years), and includes a rule of construction protecting AI-based satire, parody, or other First-Amendment-protected expressive conduct that clearly discloses it isn't authentic. "Artificial intelligence" is defined by cross-reference to the National Artificial Intelligence Initiative Act of 2020. The bill's findings cite the May 2025 AI voice-cloning impersonation of White House Chief of Staff Susie Wiles and the July 2025 impersonation of Secretary of State Marco Rubio as the impetus.

**Note on a related, separately tracked bill:** this is a distinct bill from the AI Fraud Accountability Act (H.R. 7786, Rep. Buchanan), also tracked on this page. Both respond to the same wave of AI-impersonation-of-officials incidents, but they take different approaches: H.R. 6306 (this bill) is a narrow sentencing enhancement bolted onto existing mail/wire/bank fraud, money-laundering, and federal-impersonation statutes, with no new agency authority. H.R. 7786 instead creates a new civil FTC enforcement track for AI-generated impersonation fraud generally, with international-cooperation language. The two are complementary rather than overlapping — one raises criminal penalties under Title 18, the other builds new civil enforcement authority — and neither bill references the other.
