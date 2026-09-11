---
title: AI Advertising Disclosure Act
short_name: AI Advertising Disclosure Act
bill_numbers:
- H.R. 10146
congress: 119
topic: Deepfakes & Synthetic Media
status: introduced
chamber_origin: House
introduced_date: '2026-08-24'
last_action: Referred to House Committee on Energy and Commerce
last_action_date: '2026-08-24'
sponsors:
- Rep. Seth Magaziner (D-RI)
- Rep. Eleanor Holmes Norton (D-DC)
cosponsor_count: 1
committees:
- House Energy and Commerce
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 4.0
  impact_components:
    R: 0.85
    D: 0.80
    E_f: 1.00
    P: 0.60
  likelihood:
    p_committee: 0.10
    p_enact: 0.02
    basis: "base_rate_adjusted"
  rationale:
    A: "The obligation runs against 'covered entities' deploying AI chatbots/generative-search tools with 50,000+ monthly active users, requiring disclosure of commercial arrangements that influence AI-generated responses, an internal real-time registry of those arrangements, and a user-facing mechanism to ask whether a given response was commercially influenced. This binds deployers of consumer-facing AI products on how they present outputs — closer to a disclosure/transparency mandate on AI systems than a domain-general advertising rule, but it regulates sponsored-content presentation rather than model training or deployment conduct in the frontier-safety sense, so it lands at the disclosure-only rung (+1) reduced slightly to +0.5 to reflect that the mandate is about ad-disclosure practice layered onto AI tools rather than AI governance per se — closer to a procurement/consumer-protection rule than a developer conduct standard, but with a real registry-and-user-query mechanism that pushes it just above a pure procurement condition."
    B: "No preemption or field-occupation language in the bill text; it explicitly states it does not preempt state consumer-protection laws providing greater protections, and grants state AGs parens patriae enforcement authority (albeit paused while a federal action is pending). This is an ordinary savings clause bolted onto a substantive bill, so it scores +1 under that rung; the implicit-preemption floor doesn't apply since A does not reach +2."
    C: "No new agency, testbed, or standing government database — FTC's role is rulemaking and enforcement of an existing statute (FTC Act unfair/deceptive-practices authority) rather than a new capacity-building institution; scores 0."
    D: "No export-control, chip-access, or geopolitical content."
    E_consumer: "Establishes FTC rulemaking backed by civil penalties, a private right of action (actual damages or statutory damages up to $1,000/violation, treble damages for willful violations, mandatory attorney's fees), and state AG parens patriae suits — a broad, multi-channel enforcement scheme close to the private-right-of-action ceiling, but scoped specifically to AI-tool sponsored-content disclosure rather than a fully general cross-sector private right of action, landing at 4 rather than 5."
    F: "No data-center, permitting, or energy content."
    R: "Covers any AI chatbot or generative-search tool with over 50,000 monthly active users — a low threshold that captures essentially all consumer-facing generative AI products used at any meaningful scale, not just frontier-lab flagship products, so reach is high but not fully universal given the user-count floor."
    Depth: "max(|A|=0.5, |B|=1, |C|=0, |F|=0, E=4)/5 = 0.80, driven almost entirely by the E axis."
    E_f: "Private right of action with statutory damages, treble damages for willful violations, and mandatory fee-shifting — the strongest tier on the enforceability ladder."
    P: "Would be the first federal AI-specific sponsored-content disclosure framework, arriving after New York's synthetic-performer disclosure law but addressing a different problem (commercial influence over AI outputs, not synthetic actors); a plausible template if enacted, but self-contained to AI advertising disclosure rather than a broad institutional precedent, landing at the joins-an-established-template rung given the closely analogous state momentum (NY, and pending FTC guidance) on AI/ad disclosure generally."
    likelihood: "Introduced August 24, 2026, referred to House Energy and Commerce with only one cosponsor (Del. Norton) and no Senate companion identified. No GovTrack prognosis page yet exists given how recently it was introduced. Base rate for a single-committee-referral bill with minimal cosponsorship and roughly four months left in the 119th Congress's second session is very low; FTC-authority disclosure bills with private rights of action also tend to draw industry opposition that slows movement in a Republican-controlled House Energy and Commerce Committee."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- deepfakes
- ai chatbots
- advertising disclosure
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/10146
- label: Introduced text
  url: https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr10146ih.xml
- label: Nextgov/FCW tech bills roundup
  url: https://www.nextgov.com/policy/2026/08/tech-bills-week-identifying-sponsored-content-ai-tools-reshoring-biotech-manufacturing-and-more/415703/
summary: Requires AI chatbots and generative-search tools with 50,000+ monthly users to clearly disclose when a response reflects a paid commercial arrangement, backed by FTC rulemaking, a private right of action, and state AG enforcement.
timeline:
- date: '2026-08-24'
  event: Introduced by Rep. Magaziner (with Del. Norton); referred to House Energy and Commerce
- date: '2026-09-10'
  event: Added to tracker. Bill remains in committee with one cosponsor and no Senate companion identified.
---

The bill requires "covered entities" operating AI chatbots or generative-search tools with more than 50,000 monthly active users to disclose, clearly and conspicuously and in plain language, whenever a response reflects a paid or otherwise commercial arrangement — including sponsored product mentions, affiliate links, or training/retrieval data shaped by a paid deal. Covered entities must maintain a real-time internal registry of commercial arrangements and let users ask, mid-conversation, whether a given response was commercially influenced. The FTC must issue implementing regulations within 180 days of enactment (and every three years thereafter) and enforces violations as unfair or deceptive practices; the bill also creates a private right of action (actual or statutory damages up to $1,000 per violation, trebled for willful violations, with mandatory attorney's fees) and lets state attorneys general sue on residents' behalf. It expressly preserves state consumer-protection laws that provide greater protection.
