---
title: Defense AI Reliability and Reporting Act
short_name: Defense AI Reliability and Reporting Act
bill_numbers:
- H.R. 10189
congress: 119
topic: Government Use & Procurement
status: introduced
chamber_origin: House
introduced_date: '2026-08-31'
last_action: Referred to the House Committee on Armed Services
last_action_date: '2026-08-31'
sponsors:
- Rep. Sara Jacobs (D-CA)
- Rep. Nathaniel Moran (R-TX)
- Rep. George Whitesides (D-CA)
cosponsor_count: 2
committees:
- House Armed Services
scoring:
  axes:
    A: 0.5
    B: 0.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 1.0
  impact_components:
    R: 0.5
    D: 0.20
    E_f: 0.40
    P: 0.60
  likelihood:
    p_committee: 0.30
    p_enact: 0.10
    basis: "base_rate_adjusted"
  rationale:
    A: "CORRECTED under the newly added frontier/systemic-risk guardrail (rubric: 'Guardrail: frontier/systemic risk vs. near-term consumer harm'). The prior pass scored this A=2.0 on the reasoning that the incident-reporting-with-corrective-action mechanism 'genuinely governs AI' rather than using AI as a domain-general tool — and that distinction still holds; this is not a CyberTipline-style false positive. But the newly added guardrail asks a further, independent question: even where a mechanism is genuinely AI-specific, does it reach frontier-scale training, catastrophic/systemic risk, or AI governance broadly — or is it bounded to one institutional buyer's own procurement/operations? Here, new 10 U.S.C. 2224b binds only AI systems DoD itself develops, tests, procures, fields, or operates (R is independently scored 0.5 precisely because 'this universe is a small slice of AI activity'). It creates no authority over frontier developers, no gate on training or deployment for the industry generally, and no obligation reaching any AI system outside DoD's own pipeline. The loss-of-control-flavored definitions ('failing to respond to a disengage command,' 'concerns regarding system control and autonomy') describe a real and serious failure mode, but the guardrail is explicit that alarming-sounding language does not itself justify a high rung when the mechanism's actual reach is one buyer's own systems — that is structurally the same government-use/procurement pattern as the +0.5 rung ('binds the buyer, not the builder'), just with a more serious incident-severity floor than a typical procurement bill. Corrected to 0.5."
    B: "No preemption or savings-clause language anywhere in the text. With A corrected to 0.5 under the frontier/systemic-risk guardrail (see A rationale), this is now well below the +2 threshold that would even raise the implicit-preemption floor question, so the analysis is simpler than in the prior pass: this bill governs only DoD's own internal AI systems, not private developers or deployers, so it does not displace any plausible field of state AI regulation. B remains 0 (silent)."
    C: "CORRECTED under the frontier/systemic-risk guardrail. The prior pass scored this 3.0 on the theory that a standing, recurring reporting mechanism into a designated oversight function textually matches the '+3: standing information flows... into a government database' rung regardless of scope. But axis C, like A, is meant to track *systemic* AI governance capacity — the guardrail's disjunctive test (frontier training / catastrophic risk / loss-of-control / systemic AI oversight capacity) is about capacity that reaches AI governance broadly, not a single agency's internal incident-tracking office for its own systems. The designated official (new (d)) and the annual reports to the defense committees (new (i)) build real, recurring infrastructure — but it is scoped entirely to DoD's own AI pipeline, structurally the same bounded-institution pattern as FAIRR's FSOC-reporting regime or a procurement-compliance reporting rule, not a cross-sectoral or industry-wide oversight body. Corrected to 1.0 (studies/advisory-with-real-deadlines tier) — a genuine, recurring reporting duty, but bounded to one buyer's own systems rather than building government capacity to govern AI as such."
    D: "No export control, chip access, or foreign-adversary content — this is purely a domestic DoD internal-process bill."
    F: "No compute, energy, permitting, or siting content."
    E_consumer: "CORRECTED under the frontier/systemic-risk guardrail: E_consumer is an impact-only axis for near-term harm to specific populations/sectors, and this bill's genuine severity — mandatory corrective action and validated mitigation before continued operational use, triggered by incidents that can include death or bodily harm (new (i) casualty-incident narratives) — belongs here rather than being (over-)credited on A/C. This is not the deepfake/NCII/companion-bot/discrimination/election harm class the rubric's E ladder is written around, and it doesn't reach the public directly (the affected population is service members, DoD civilians, and contractors operating or subject to DoD AI systems), so it doesn't approach the top of the ladder — but it is a real, enforced safety-incident regime with a documented casualty-reporting channel, not zero. Raised to 1.0 (just above 'no consumer/near-term harm content') to reflect that a bounded-population safety mechanism exists, without overstating it as reaching general consumers."
    R: "Scored as a developer-facing-style bill but one whose target universe is narrow by design: it reaches only AI systems developed, tested, procured, fielded, or operated within the Department of Defense, not the frontier AI industry generally or the government's AI use as a whole. R=0.5 reflects that within its own (DoD-AI) universe coverage is comprehensive, but that universe itself is a small slice of AI activity."
    Depth: "max(|A|,|B|,|C|,|F|,E)/5 = max(0.5, 0, 1.0, 0, 1.0)/5 = 0.20. Recomputed after the A/C/E_consumer corrections under the frontier/systemic-risk guardrail — this is now a modest-depth bill, consistent with a bounded, DoD-internal reporting regime rather than a systemic AI-governance mechanism."
    E_f: "Unchanged by the guardrail correction (this component measures enforcement mechanism strength, not AI-governance scope): the corrective-action/validation-before-continued-use requirement (new (f)(2)) and whistleblower-style retaliation protection (new (g)(2)) are administered internally by DoD with no civil penalties, AG enforcement, or private right of action — an obligation with process consequences (can't keep operating without validated mitigation) but no stated monetary or legal penalty, landing at 0.4."
    P: "Extends an established legislative pattern — DoD/NDAA-style AI incident-reporting and testing provisions have appeared in prior defense authorization contexts — into a permanent, standing statutory program (new 10 U.S.C. 2224b) rather than a one-off pilot; scored at 0.6 (joins/extends an established template) rather than 0.8, since AI incident-reporting mandates for military systems are not a first-in-nation novelty at this point."
    likelihood: "Introduced 2026-08-31 with bipartisan original cosponsors (Whitesides, D-CA; Moran, R-TX) and referred to House Armed Services; no committee markup yet as of this scoring pass, and it is very recently introduced (just over a week old). GovTrack does not yet show a modeled prognosis for this bill. Base-rate adjustment: standalone member bills referred to Armed Services rarely advance on their own, but DoD AI-reliability/incident-reporting provisions of this type are a strong candidate for insertion into the annual NDAA, which is the more likely enactment vehicle — p_enact is set modestly above a typical standalone-bill base rate to reflect that possibility, while p_committee reflects the low odds of this specific bill number getting an independent markup before any NDAA cutoff."
  confidence: medium
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- defense
- procurement
- incident reporting
- national security
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/10189
- label: GovInfo (Introduced in House, 2026-08-31)
  url: https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr10189ih.xml
- label: Sponsor press release
  url: https://sarajacobs.house.gov/news/press-releases/rep-sara-jacobs-introduces-bipartisan-legislation-to-address-ai-weaknesses-and-failures-at-pentagon
summary: Would direct the Secretary of Defense to establish a department-wide program for reporting, tracking, and remediating AI incidents and vulnerabilities across DoD's development, testing, procurement, and operational use of AI systems.
timeline:
- date: '2026-08-31'
  event: Introduced in the House by Rep. Jacobs with Reps. Moran and Whitesides; referred to House Armed Services
---

The bill would add a new section 2224b to title 10, U.S. Code, directing the Secretary of Defense to establish a centralized, department-wide program for reporting, tracking, analysis, and remediation of "covered AI incidents" and "covered AI vulnerabilities" arising anywhere in DoD's development, testing, procurement, fielding, or operation of AI systems. Covered incidents are defined broadly — unintended operational/safety/security harm, operating outside authorized guardrails, failing to respond to a disengage command, or raising "concerns regarding system control and autonomy." A designated official receives and standardizes reports and conducts trend analysis; department-wide incidents require a documented corrective action plan and validated mitigation before continued operational use. The program must include a protected, non-punitive disclosure process for service members, civilian employees, contractors, and subcontractors, with anti-retaliation protection. Annual unclassified reports (with optional classified annexes) go to the congressional defense committees from 2027 through 2031, including detailed narratives for any incident causing death or bodily harm.
