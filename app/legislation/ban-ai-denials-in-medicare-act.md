---
title: Ban AI Denials in Medicare Act
short_name: Ban AI Denials in Medicare Act
bill_numbers:
- H.R. 6361
congress: 119
topic: Healthcare
status: committee
chamber_origin: House
introduced_date: '2025-12-02'
last_action: Referred to the House Committees on Ways and Means and Energy and Commerce
last_action_date: '2025-12-02'
sponsors:
- Rep. Greg Landsman (D-OH)
- Rep. Bonnie Watson Coleman (D-NJ)
cosponsor_count: 1
committees:
- House Ways and Means
- House Energy and Commerce
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: -1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.0
  impact_components:
    R: 0.55
    D: 0.40        # Depth — unrelated to axes.D
    E_f: 0.60
    P: 0.60
  likelihood:
    p_committee: 0.15
    p_enact: 0.03
    basis: "base_rate_adjusted"
  rationale:
    A: "The bill's obligation runs against the Secretary of HHS/CMS, not against any AI developer — it bars the government from testing the WISeR model and amends 42 U.S.C. 1315a(b)(2) to permanently bar CMI from selecting any future prior-authorization payment model 'including through the use of artificial intelligence.' This is a restriction on a government program's use of AI as a decision-making tool in benefits administration, not a conduct standard imposed on a developer of frontier or advanced AI systems — it governs a government purchaser/deployer decision, not developer conduct, so it does not score on axis A even though it is genuinely AI-specific (satisfying the governance-scoping guardrail) rather than a domain-general mechanism that merely mentions AI in passing."
    B: "No state law or preemption content whatsoever — this amends federal Medicare statute and applies only to a federal agency's own program design; entirely silent on state authority. Implicit-preemption floor does not apply since axis A is 0."
    C: "Section 2(b) permanently bars CMS/CMI from selecting any future payment model that would implement AI-based prior authorization under Parts A/B of traditional Medicare — this affirmatively strips the agency's own discretionary authority to adopt an AI tool in this domain, which is the −1 rung ('cuts or lets lapse existing capacity') rather than 0, since CMI currently has broad model-selection authority under 1115A(b)(2) that this bill narrows specifically with respect to AI-based prior authorization."
    D: "No export-control, chip-access, or geopolitical content."
    E_consumer: "This is squarely a near-term consumer-harm bill: it responds to concrete reporting that an AI-driven prior-authorization model (WISeR) could affect roughly 6.5 million traditional Medicare beneficiaries by allowing algorithmic denial of medically necessary services. The bill imposes a hard statutory prohibition (not just a labeling or disclosure requirement) protecting Medicare beneficiaries from AI-driven coverage denials, but it operates through a government-program ban rather than creating a private right of action or criminal liability against any party — closer to a strong statutory prohibition on the specific harm than a labeling-only measure, landing at 2 on the 0-5 unsigned scale (above 1/labeling-only, below 3/criminal liability, since there's no criminal exposure or private suit)."
    F: "No data-center, compute, siting, or energy content."
    R: "A federal bill covering all traditional Medicare Part A/B beneficiaries potentially subject to AI-based prior-authorization models — a substantial, well-defined population (the WISeR pilot alone was slated to affect ~6.5 million beneficiaries across six states), but the bill's mechanism is narrow (CMI model selection only) and doesn't reach Medicare Advantage or private-payer AI denial practices, which are a large share of AI-driven denial complaints; reach within its own consumer-protection class is moderate."
    Depth: "Depth is driven by the largest-magnitude axis among A/B/C/F/E_consumer. Here E_consumer=2.0 is the largest magnitude (0.4 on the 0-1 scale) — a real, permanent statutory prohibition on a specific harm channel, but narrow in scope (traditional Medicare prior-authorization only, not the broader AI-denial landscape)."
    E_f: "The prohibition is self-enforcing as a statutory bar on agency action (CMS simply may not select such a model) — there's a clear legal constraint but no civil-penalty or private-suit mechanism if CMS were to violate it beyond the ordinary APA/ultra vires challenge path; scored at the 'AG enforcement only'-equivalent 0.6 rung, reflecting that the only realistic enforcement avenue is litigation or oversight against the agency, not a private right of action against a developer or insurer."
    P: "Directly responsive to a live, high-profile CMS pilot (WISeR, launched January 2026 across six states) and part of a broader wave of 2025-2026 congressional pushback on AI-driven Medicare/Medicare Advantage denials — if enacted, this would be a first-in-nation categorical statutory ban on AI-based prior authorization in a major federal health program, a template other bills addressing AI claims denials (including in Medicare Advantage or Medicaid) would likely draw on; scored above the sector-specific-and-self-contained rung given its precedent-setting potential, but below 'permanent institution' since it doesn't create new machinery, just prohibits an existing program tool."
    likelihood: "Verified 2026-09-10: introduced 2025-12-02 by Landsman and Watson Coleman, referred to Ways and Means and Energy and Commerce, no committee action recorded as of this scoring. Endorsed by advocacy groups (Social Security Works, Public Citizen, Just Care USA) and part of active bipartisan concern documented in a January 2026 House Energy and Commerce hearing on prior-authorization AI models, but the bill itself has only 1 cosponsor and no GOP co-sponsorship despite bipartisan concern about WISeR generally — narrow sponsor base and late introduction in the term keep enactment odds low, though the live WISeR controversy gives it more attention than a typical single-digit-cosponsor bill."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- healthcare
- medicare
- prior authorization
- consumer protection
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/6361
- label: Rep. Landsman press release
  url: https://landsman.house.gov/posts/landsman-watson-coleman-introduce-bill-to-prohibit-ai-model-from-denying-medicare-procedures
summary: House bill barring HHS from testing the WISeR AI prior-authorization model and permanently barring CMS from adopting future AI-based prior-authorization models under traditional Medicare.
timeline:
- date: '2025-07-01'
  event: CMS publishes notice implementing the WISeR prior-authorization model (90 Fed. Reg. 28749)
- date: '2025-12-02'
  event: Introduced by Rep. Landsman (with Rep. Watson Coleman) and referred to House Ways and Means and Energy and Commerce
- date: '2026-01-01'
  event: CMS WISeR model pilot launches in six states (OH, NJ, OK, TX, AZ, WA)
---

The Ban AI Denials in Medicare Act would bar the HHS Secretary from implementing the CMS "Wasteful and Inappropriate Service Reduction" (WISeR) model — a six-year pilot using AI algorithms to determine medical necessity for select services (including certain skin substitutes and diagnostic knee surgeries) across six states, potentially affecting roughly 6.5 million traditional Medicare beneficiaries — or any substantially similar model. It also permanently amends the Center for Medicare and Medicaid Innovation's model-selection authority (42 U.S.C. 1315a(b)(2)) to bar the Secretary from ever selecting a future payment model that would implement prior authorization, including through the use of artificial intelligence, for items or services covered under Medicare Parts A or B. The bill responds directly to bipartisan concern that CMS quietly launched WISeR via a Federal Register notice in mid-2025 without statutory authorization specific to AI-driven coverage denials.
