---
title: Learning Innovation and Family Empowerment with AI Act
short_name: LIFE with AI Act
bill_numbers:
- S. 3063
congress: 119
topic: Research, Education & Workforce
status: introduced
chamber_origin: Senate
introduced_date: '2025-10-28'
last_action: Referred to the Senate Committee on Health, Education, Labor, and Pensions
last_action_date: '2025-10-28'
sponsors:
- Sen. Bill Cassidy (R-LA)
cosponsor_count: 0
committees:
- Senate Health, Education, Labor, and Pensions
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 1.0
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
    p_committee: 0.10
    p_enact: 0.02
    basis: "base_rate_adjusted"
  rationale:
    A: "The bill's facial-recognition provision (Sec. 5) binds schools and their yearbook/edtech vendors, not AI developers generally, and operates as a Spending Clause funding condition (no funds available unless the agency/institution prohibits certain conduct) rather than a direct mandate on a developer -- this is a domain-general school-funding mechanism that happens to touch one AI use case (facial-recognition training on student photos), capping it at the +1 ceiling per the AI-governance-scoping guardrail. Landing at +0.5 rather than the full +1 ceiling because the obligation runs against the school/vendor relationship (procurement-adjacent: the school controls whether it contracts with a compliant vendor) rather than a disclosure mandate running directly against the AI developer itself -- closer to the 'binds the buyer, not the builder' rung than 'disclosure only,' but the underlying prohibition (no training facial-recognition AI on student photos without consent) is a real substantive limit rather than pure paperwork, so it's nudged up half a point from the pure procurement rung."
    B: "No preemption or savings-clause language anywhere in the bill -- every mechanism operates through FERPA funding conditions (Spending Clause), which by design leaves state law fully intact; a state is free to impose its own, stricter student-privacy or biometric rules on top of this floor. The bill doesn't establish a regulatory scheme reaching A >= +2, so the implicit-preemption floor doesn't apply."
    C: "Establishes a Privacy Technical Assistance Center at the Department of Education (Sec. 8) with real duties -- helping schools and vendors comply with FERPA/PPRA, approving voluntary safe-harbor programs with published criteria, and administering a public online resource listing third parties found in violation of student-data-privacy contract terms, complete with an investigation and appeal process. This is a funded, staffed compliance-and-transparency body, closer to the 'authorizes and funds a dedicated evaluation body' rung than a mere study, but it evaluates FERPA compliance rather than AI risk specifically, so it's capped at +1 rather than the higher C rungs that require AI-specific oversight capacity."
    D: "No export-control, chip-access, or geopolitical-competition content."
    E_consumer: "The facial-recognition ban (Sec. 5) is the bill's clearest near-term-harm provision: it conditions federal funds on schools banning use of student photos to train facial-recognition AI without parental consent, and on schools avoiding yearbook vendors that use facial recognition without disclosure and consent. Enforcement is Spending-Clause funding conditions plus Secretary-run investigation/appeal/public-shaming-list machinery (Sec. 7(c)) rather than a private right of action (the bill explicitly disclaims creating one, Sec. 8(b)(4)(7)) or criminal liability, so this sits between the 'end-user labeling requirement only' rung (1) and 'criminal liability' rung (3) -- scored at 2 to reflect that funding-condition enforcement with an investigation/public-listing mechanism is a real, if indirect, consequence beyond pure disclosure."
    F: "No data-center, permitting, siting, or energy content."
    R: "Every FERPA-covered elementary school, secondary school, and local educational agency in the country is covered -- the funding-condition mechanism reaches essentially the entire K-12 system, with no revenue floor or sector carve-out limiting coverage."
    Depth: "Depth = max(|A|,|B|,|C|,|F|,E)/5 = max(0.5, 0, 1.0, 0, 2.0)/5 = 0.40, driven by the E_consumer facial-recognition/funding-condition provisions rather than by axis A or C, which are both modest."
    E_f: "Enforcement runs through Department of Education investigation of complaints, a public violation list, and funding conditions -- closer to 'agency rulemaking/penalties' than a stated private right of action (which Sec. 8 explicitly disclaims for the safe-harbor provisions), landing at the AG/agency-enforcement rung."
    P: "Would be a genuinely novel federal framework specifically addressing facial-recognition training on student photographs and AI-vendor contract transparency in K-12 -- a plausible first-in-nation template other privacy bills could copy, though it's entirely sector-specific to K-12 education rather than a general AI framework."
    likelihood: "Introduced 2025-10-28 with zero cosponsors and referred to Senate HELP, where it has not received a hearing or markup as of 2026-09-09 -- notable in part because Sen. Cassidy chairs HELP, giving it a real if unrealized path to markup should he prioritize it. No GovTrack prognosis is yet published for S. 3063. Using base rates for chair-sponsored, zero-cosponsor Senate HELP bills at this stage of the Congress (chair sponsorship meaningfully raises committee odds relative to a rank-and-file member's bill, but zero cosponsors and no hearing after almost a year cuts against near-term action), with enactment odds low given no companion House vehicle identified and a crowded K-12-AI-privacy field this Congress."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- education
- K-12
- FERPA
- student privacy
- facial recognition
- biometrics
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/3063
- label: Senate HELP Committee press release
  url: https://www.help.senate.gov/rep/newsroom/press/chair-cassidy-introduces-bill-empowering-parents-strengthening-ai-in-the-classroom
summary: Senate HELP Chair Cassidy's bill expanding FERPA parental-consent and facial-recognition protections for K-12 students; introduced, no committee action yet.
timeline:
- date: '2025-10-28'
  event: Introduced by Sen. Cassidy; referred to Senate Health, Education, Labor, and Pensions
---

The LIFE with AI Act (Learning Innovation and Family Empowerment with AI Act) would use FERPA funding conditions to reshape K-12 student-data privacy and parental-consent practices. It requires schools and local educational agencies to provide real-time "instant verification technology" for parental consent, creates a voluntary "Golden Seal of Excellence in Student Data Privacy" certification, simplifies FERPA directory-information opt-outs, and expands the FERPA definition of "education records" to cover data held by any third party acting for or with a school.

Its most AI-specific provision (Sec. 5) bars federal funds to any educational agency or institution that fails to prohibit (1) using student photographs to train facial-recognition systems, including AI-based ones, without prior parental consent, and (2) doing business with yearbook-production vendors that use facial recognition without disclosure and parental consent. Separately (Sec. 7), it requires schools to publicly post proposed third-party edtech contracts before signing them, mandate privacy certifications from vendors, and report noncompliant vendors to the Secretary of Education, who investigates and can place vendors on a public violation list (with an appeal process) for five years. Sec. 8 creates a Privacy Technical Assistance Center at the Department of Education, which may approve independent "safe harbor" compliance programs for edtech vendors. The bill also directs the Institute of Education Sciences to develop AI-integration training resources for teachers and amends the ESEA to add AI literacy (including the harms of AI misuse) as a state technology-plan element, and prioritizes SBIR grants for personalized-learning AI research that doesn't reduce students' critical-thinking skills.
