---
title: "Responsible and Ethical AI Labeling Act (REAL Act)"
short_name: "REAL Act"
bill_numbers: ["H.R. 6571"]
congress: 119
topic: "Transparency & Copyright"
status: "introduced"
chamber_origin: "House"
introduced_date: "2025-12-10"
last_action: "Referred to committee"
last_action_date: "2025-12-10"
sponsors: ["Rep. Bill Foster (D-IL)", "Rep. Pete Sessions (R-TX)"]
cosponsor_count: 1
committees: ["House Oversight and Government Reform"]
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 0.5
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 1.0
  impact_components:
    R: 0.90
    D: 0.20
    E_f: 0.40
    P: 0.40
  likelihood:
    p_committee: 0.10
    p_enact: 0.03
    basis: "base_rate_adjusted"
  rationale:
    A: "Binds federal officials, agency heads, and the President/Vice President when they publish content through official channels -- it places zero obligation on developers of frontier or any other AI systems. This is a government-transparency mandate, not a developer conduct standard, so it scores 0 on the guardrail's own terms (the mechanism doesn't govern AI development or deployment at all, it governs government communications)."
    B: "No preemption or savings-clause language anywhere in the bill, and the implicit-preemption floor doesn't trigger because axis A scores well below +2 -- this bill doesn't establish a federal regulatory scheme over private AI developers of any kind, so there's no scheme whose silence could imply preemption. Genuinely silent on state authority to regulate AI."
    C: "Requires OMB to issue implementing regulations within 180 days and requires the President, Vice President, and agency heads to conduct annual compliance audits reported to Congress and the public. That's a real recurring reporting deadline, but it builds oversight capacity over the government's own communications practices, not over the AI industry or frontier developers -- closer to a GAO-style annual-report mechanism than a new evaluation body or enforcement authority, so it lands at the low end of the 'studies, advisory committees with real reporting deadlines' rung rather than the incident-reporting-database rung above it."
    D: "No export-control, chip-access, or geopolitical-competition content anywhere in the bill."
    E_consumer: "The disclaimer requirement is a labeling mandate aimed at the public that consumes government-published content -- it tells readers/viewers when what they're seeing was AI-generated or AI-manipulated. That's squarely the rubric's 'end-user labeling requirement only' rung: no private right of action, no criminal liability, and the obligation runs against government publishers rather than private industry, so it doesn't reach any higher rung on this axis."
    F: "No data-center, permitting, interconnection, energy, or siting content."
    R: "Covers every federal agency, officer, and employee (plus the President and Vice President) publishing through official government channels -- essentially the entire target class of 'federal government AI-generated public communications,' with narrow, sensible carve-outs for classified content, minor edits, and personal social media unrelated to official duties."
    Depth: "max(|A|,|B|,|C|,|F|,E)/5 = max(0, 0, 0.5, 0, 1.0)/5 = 0.20. No axis pushes far from neutral; this is a narrow, single-purpose disclosure bill."
    E_f: "Obligation with a stated compliance mechanism -- annual audits reported to Congress and the public, and OMB rulemaking -- but no penalty provision, private right of action, or agency civil-penalty authority is specified in the bill or its press materials. That's above pure voluntary self-regulation but below AG or agency civil-penalty enforcement, landing at the 'obligation with no stated penalty' rung."
    P: "Sector-specific and self-contained: a labeling rule for one category of publisher (the federal government) on one category of content (AI-generated/manipulated official communications). Not a first-in-nation template likely to be copied by private-sector regulation, and not a permanent institution or preemption ceiling -- it's a durable but narrow rule once in place, so it sits at the 'sector-specific and self-contained' rung rather than sunsetting or creating lasting precedent beyond its own lane."
    likelihood: "No GovTrack prognosis page was found for H.R. 6571 as of this check. Introduced 2025-12-10 with only one cosponsor (bipartisan pairing: Foster D-IL, Sessions R-TX) and referred to committee with no further action reported as of 2026-09-09 -- nine months with no markup or hearing. Using historical base rates for single-issue, narrow-scope House bills with minimal cosponsorship (most such bills die in committee), p_committee is estimated at 0.10 and p_enact at 0.03. The bipartisan sponsor pairing and low political salience of 'require the government to label its own AI content' modestly help its odds relative to a purely partisan bill, but the near-total absence of cosponsors or committee action nine months in keeps both probabilities low."
  confidence: low
  text_source: summary
  scored_at: "2026-09-09"
tags: ["transparency", "government use", "disclosure", "AI labeling"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/house-bill/6571"
  - label: "Sponsor press release (Rep. Foster)"
    url: "https://foster.house.gov/media/press-releases/foster-sessions-introduce-bipartisan-bill-requiring-government-agencies-label"
summary: "Bipartisan bill requiring federal officials and agencies to disclose when content they publish through official channels is AI-generated or AI-manipulated."
timeline:
  - date: "2025-12-10"
    event: "H.R. 6571 introduced by Reps. Foster and Sessions; referred to committee"
  - date: "2026-09-09"
    event: "Verified -- still at referred-to-committee stage, no markup or further action found"
---
The REAL Act (Responsible and Ethical AI Labeling Act) would require federal officers and employees -- including the President and Vice President -- to attach a "clear, conspicuous, and prominently displayed" disclaimer whenever they publish AI-generated or AI-manipulated images, video, or unreviewed AI-generated text through official government channels. The disclaimer must be in plain language and explain how the content was generated or altered and what technology was used.

The bill carves out exceptions for non-public communications, classified material (subject to recordkeeping safeguards), minor edits that don't change meaning (cropping, brightness), routine AI drafting tools that are reviewed by staff before publication, and personal social-media activity unrelated to official duties. OMB must issue implementing regulations within 180 days of enactment, and the President, Vice President, and agency heads must conduct annual compliance audits reported to Congress and the public.

Sponsors Bill Foster (D-IL) and Pete Sessions (R-TX) frame the bill as a safeguard against the government inadvertently or deliberately misleading the public with synthetic content, while leaving agencies free to keep using AI internally for non-public work.
