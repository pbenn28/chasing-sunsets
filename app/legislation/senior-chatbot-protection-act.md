---
title: "Senior Chatbot Protection Act of 2026"
short_name: "Senior Chatbot Protection Act"
bill_numbers: ["S. 5117"]
congress: 119
topic: "Children & Chatbots"
status: "introduced"
chamber_origin: "Senate"
introduced_date: "2026-07-23"
last_action: "Read twice and referred to the Senate Committee on Commerce, Science, and Transportation"
last_action_date: "2026-07-23"
sponsors: ["Sen. Mark Kelly (D-AZ)", "Sen. Jim Justice (R-WV)"]
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
    P: 0.60
  likelihood:
    p_committee: 0.20
    p_enact: 0.05
    basis: "base_rate_adjusted"
  rationale:
    A: "RE-SCORED 2026-09-09 under the frontier/systemic-risk-vs-near-term-consumer-harm guardrail: Sec. 3's disclosure, high-stakes-decision-detection, crisis-detection, training-data-consent, and deceptive-design provisions are a real, FTC-enforced conduct regime, but its subject is senior-specific chatbot-safety harms in ordinary deployment, not frontier-scale training, catastrophic/CBRN risk, or systemic AI oversight capacity. The guardrail directs axis A to the floor (rarely above +0.5-+1) for exactly this pattern even where the mandate is well-drafted and enforced. Scored at 0.5 rather than 0.0 to reflect that it is a real, enforced conduct mandate on chatbot providers (above pure disclosure), but not frontier-developer stringency."
    B: "RE-SCORED 2026-09-09 under the same guardrail: Sec. 5(d)'s savings clause and Sec. 9's broader remedy-preservation language are textually unconditional, but both are scoped to protecting 'users' of this Act's chatbot-safety regime specifically, not to states' authority over AI regulation generally — they guarantee states may enact more-protective senior/chatbot-safety law, which the guardrail explicitly identifies as capped at the '+1 ordinary savings clause' rung rather than '+3,' regardless of how unconditional or broadly worded the clause is within its own narrow topic."
    C: "RE-SCORED 2026-09-09 under the same guardrail: Sec. 4's NIH/FTC 'material adverse incident' reporting regime is a genuine standing information flow, but it observes senior-chatbot-safety incidents (high-stakes-decision and crisis events), not frontier or systemic AI risk — the guardrail's worked example is precisely this pattern. Following the STOP CSAM Act's precedent for an analogous annual FTC/DOJ reporting regime (scored C=0.5), this drops to 1.0, reflecting a somewhat more built-out dual-agency (NIH+FTC) public-data-publication structure than STOP CSAM's regime, but still held near the floor rather than at +3."
    D: "No export-control or geopolitical content."
    E_consumer: "Sec. 3's disclosure, high-stakes-decision, and crisis-intervention mandates plus Sec. 5's enforcement structure — FTC UDAP authority, civil penalties up to $50,000 per knowing/reckless violation, and a parallel state-AG (and other state consumer-protection officer) parens patriae track that can obtain damages and restitution — give this real teeth beyond a labeling-only regime, close to the criminal-liability-equivalent '3' rung, though there's no broad private right of action for individual users and a 60-day cure period softens first-violation exposure."
    F: "No data-center or energy content."
    R: "A federal bill covering any 'artificial intelligence chatbot' made available to individuals in the US, with the same narrow-purpose/predetermined-response exclusion pattern as comparable bills — R near 1.0 for the chatbot-provider class it targets, though its substantive protections are keyed to 'older adults' (65+) and high-stakes-decision/crisis contexts specifically, a narrower population than a general child-safety bill."
    Depth: "Driven jointly by the strong savings clause (B=+3), the standing NIH/FTC incident-reporting regime (C=+3), and the disclosure/crisis-intervention mandate (A=+2, E=3) — a substantively deep bill across several axes at once, similar in profile to the SAFE KIDS Act."
    E_f: "FTC UDAP enforcement with specified civil penalties up to $50,000 per violation (Sec. 5(b)), plus a state-AG/consumer-protection-officer civil action track seeking damages and restitution — agency rulemaking plus civil penalties, the '0.8' rung; no private right of action for individual users."
    P: "Addresses a genuinely distinct harm population (older adults and high-stakes-decision/crisis interactions) rather than joining the already-crowded child-chatbot cluster, but its disclosure-plus-incident-reporting structure closely mirrors the SAFE KIDS Act's template rather than breaking new structural ground; scored at the cluster-standard 0.60."
    likelihood: "Introduced 2026-07-23 with a single cosponsor (Justice) and referred to Senate Commerce; no committee markup found as of 2026-09-09. GovTrack's prognosis page (govtrack.us/congress/bills/119/s5117) returned HTTP 403 on lookup, so no external model number is available and none is asserted here. The bill has drawn an unusually broad and fast-forming outside coalition for a newly introduced bill — AMA, APA Services, National Council on Aging, Alliance for Retired Americans, Consumer Federation of America, and others publicly endorsed it within weeks of introduction — which is a positive signal for committee attention relative to a typical freshly introduced bill, but Senate Commerce has so far prioritized the child-focused chatbot cluster (CHATBOT Act package) for markup, and this bill addresses a different population (seniors) that hasn't yet had a comparable committee vehicle. p_committee and p_enact are set modestly above a bare single-cosponsor baseline to reflect the coalition support, but well below bills that have already reached markup."
  confidence: low
  text_source: full_text
  scored_at: "2026-09-09"
tags: ["chatbots", "elder safety", "consumer protection", "disclosure"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/senate-bill/5117"
  - label: "Bill text (GovInfo)"
    url: "https://www.govinfo.gov/content/pkg/BILLS-119s5117is/pdf/BILLS-119s5117is.pdf"
  - label: "Sen. Kelly press release — Kelly Introduces Bipartisan Senior Chatbot Protection Act"
    url: "https://www.kelly.senate.gov/newsroom/press-releases/kelly-introduces-bipartisan-senior-chatbot-protection-act/"
  - label: "Future of Privacy Forum statement on the Senior Chatbot Protection Bill"
    url: "https://fpf.org/blog/fpf-statement-on-the-senior-chatbot-protection-bill/"
summary: "Bipartisan Senate bill requiring AI chatbots to disclose they are not human, restrict deceptive engagement design, and refer users to human professionals for health, legal, financial, or crisis topics — aimed particularly at protecting older adults."
timeline:
  - date: "2026-07-23"
    event: "Introduced by Sen. Kelly with Sen. Justice; referred to Senate Commerce Committee"
---
The Senior Chatbot Protection Act would require AI chatbot providers to clearly and repeatedly disclose that users are interacting with an AI system rather than a human or licensed professional, detect when a user is seeking guidance on a "high-stakes decision" (health care, estate planning, guardianship, or financial transactions) and disclose the chatbot's limitations at that point, detect indicators of crisis (suicidal ideation, intent to harm others, medical emergency) and refer the user to human professionals or crisis services rather than offering advice, and obtain affirmative consent before using conversation data to train AI models or for other secondary purposes. It separately restricts deceptive or manipulative engagement-maximizing design aimed at exploiting older adults' cognitive vulnerabilities, and requires annual incident reporting to NIH and the FTC on "material adverse incidents" tied to high-stakes decisions or crises, broken out by user age band.

Though framed around protecting seniors — its incident-reporting requirement specifically disaggregates data by age band from under-50 through 85+, and it directs NIST to develop voluntary guidance on chatbots interacting with older adults — its baseline disclosure, crisis-detection, and deceptive-design provisions apply to chatbot providers generally rather than being age-gated, giving it a broader practical reach than its title suggests. It has drawn rapid endorsements from a wide coalition including the American Medical Association, APA Services, the National Council on Aging, and the Alliance for Retired Americans. Its savings-clause language (Sec. 5(d) and Sec. 9) is unusually protective of state authority and existing legal remedies, closely paralleling the SAFE KIDS Act's approach.
