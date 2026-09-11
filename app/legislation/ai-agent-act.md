---
title: "AI Access, Gatekeeper Exchange, and Nondiscriminatory Transfer Act of 2026"
short_name: "AI AGENT Act"
bill_numbers: ["S. 5051"]
congress: 119
topic: "Frontier Safety & Oversight"
status: "committee"
chamber_origin: "Senate"
introduced_date: "2026-07-21"
last_action: "Read twice and referred to the Senate Committee on Commerce, Science, and Transportation"
last_action_date: "2026-07-21"
sponsors: ["Sen. Mark Warner (D-VA)"]
cosponsor_count: 0
committees: ["Senate Commerce, Science, and Transportation"]
scoring:
  axes:
    A: 0.5
    B: -1.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.5
  impact_components:
    R: 0.5
    D: 0.50
    E_f: 0.6
    P: 0.6
  likelihood:
    p_committee: 0.15
    p_enact: 0.02
    basis: "base_rate_heuristic_no_live_lookup"
  rationale:
    A: "The bill's real obligations run against 'large online platforms' (>50M US users/month) and custodial-agent providers, not against frontier AI developers as such -- it's a competition/interoperability and consumer-agent-fiduciary bill that happens to be triggered by AI agents rather than a frontier-model conduct standard. The closest fit is Sec. 3(d)'s FTC registration requirement for custodial-agent providers, which is a mandated process with real enforcement (FTC deregistration, UDAP violations) -- but it binds a narrow category of agent-facing intermediaries, not frontier model training/deployment generally, so it lands well below a +2 mandated-process rung on the frontier-developer axis. Scored low-positive rather than 0 because the FTC registration/certification regime is still a real, AI-specific process obligation, just scoped to a downstream layer rather than frontier developers."
    B: "Sec. 4(h) is an explicit conflict-preemption clause: 'shall preempt any State law only to the extent that such State law is inconsistent with the provisions of this Act.' That is narrower than field preemption -- it doesn't wipe out non-conflicting state AI or agent-liability laws -- but it is not a savings clause either, since it affirmatively preempts wherever state law and the Act diverge. Matches the −1 conflict-preemption-only rung exactly."
    C: "Corrected 2026-09-09 under the frontier/systemic-risk guardrail. Sec. 4(c)'s NIST technical-standards directive (agent delegation credentials, identity verification, auditable action records) and Sec. 4(g)'s standing FTC-led interagency working group are real process-oriented capacity-building, but what they build capacity to observe and govern is agent-fraud liability allocation and delegation-credential standards for a consumer-facing agent-commerce niche -- not frontier-scale training, catastrophic/CBRN risk, loss-of-control, or systemic AI oversight capacity. The guardrail's C treatment applies even to a genuine, well-drafted standing information flow when its subject is a narrow sectoral/consumer domain rather than frontier risk: score near the floor and let axis E carry the bill's real severity. Previously scored 2.0 (enforcement-staffing/whistleblower-channel rung); corrected down to 1.0 (studies/advisory-committee-with-real-deadline rung) to reflect that this is agent-commerce oversight capacity, not frontier/systemic AI oversight capacity."
    D: "No export-control, chip-access, or foreign-adversary provisions; the interagency working group and NIST standards directive are domestic-market and domestic-agency processes."
    E_consumer: "Corrected 2026-09-09: under the frontier/systemic-risk guardrail, this is exactly the axis this bill's real content belongs on, since Sec. 3(g)'s non-waivable fiduciary-style duties of care and loyalty on custodial AI agent providers toward individual users -- data-privacy safeguards, a bar on self-dealing/harm, restrictions on secondary commercial use of user data -- are a consumer/agent-conduct harm mandate, not a frontier-risk one. Enforcement is FTC UDAP authority with per-affected-user penalties (Sec. 4(f)) -- real agency-enforced liability for specific conduct, just short of a private right of action or criminal liability, so it sits between the 'criminal liability for specific conduct' (3) and 'labeling only' (1) rungs. Previously scored 1.0, which undersold the bill's real enforcement teeth once the corrected, lower A/C scores mean E is doing more of the work of representing this bill's actual severity; corrected up to 2.5."
    F: "No data-center, compute, siting, or energy provisions anywhere in the bill."
    R: "The >50,000,000-monthly-user threshold for 'large online platform' captures only the handful of largest tech platforms, and the custodial-agent-provider duties apply industry-wide but to a still-nascent, narrow slice of the AI industry (agent providers specifically, not frontier model developers generally) -- a real but bounded reach within its own class."
    Depth: "Recomputed after the frontier/systemic-risk guardrail correction — now driven by axis E (consumer/near-term harm) at 2.5/5."
    E_f: "FTC enforcement under UDAP authority (Sec. 4(f)) with penalties assessed per affected user is agency rulemaking plus civil penalties -- real teeth, but short of a private right of action, which the bill explicitly omits."
    P: "Establishes a durable registration/certification and interoperability framework for AI agents that, if enacted, would likely become the template other agent-interoperability proposals build on -- a first-in-nation framework for this specific niche, though not a preemption ceiling or brand-new permanent institution."
    likelihood: "Introduced solo by Sen. Warner with zero cosponsors as one piece of his six-bill 'Framework for America's AI Future' package; referred to Senate Commerce on introduction (7/21/26) and was not among the five bills that committee marked up on 8/5/26. No hearing, markup, or added cosponsor found as of early September 2026. GovTrack.us and congress.gov's live cosponsor tracker were both unreachable (403) for a fresh check, so likelihood remains a base-rate heuristic consistent with sibling bill S. 5061 in the same package."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags: ["AI agents", "interoperability", "FTC", "fiduciary duty", "NIST", "custodial agents"]
sources:
  - label: "Official bill text (GovInfo)"
    url: "https://www.govinfo.gov/content/pkg/BILLS-119s5051is/pdf/BILLS-119s5051is.pdf"
  - label: "Sponsor press release (discussion draft)"
    url: "https://www.warner.senate.gov/newsroom/press-releases/warner-unveils-discussion-draft-of-legislation-to-create-innovative-market-for-secure-artificial-intelligence-agents/"
summary: "Warner bill creating a 'custodial user agent' framework with non-waivable fiduciary duties for AI agent providers, mandatory large-platform interoperability, NIST technical standards, and FTC registration of agent providers."
timeline:
  - date: "2026-06-29"
    event: "Sen. Warner releases discussion draft"
  - date: "2026-07-21"
    event: "S. 5051 introduced as part of Warner's six-bill AI package; read twice and referred to Senate Commerce"
  - date: "2026-08-05"
    event: "Senate Commerce marks up five other AI/kids-safety bills; S. 5051 not included"
---
The AI AGENT Act would create a "custodial user agent" framework governing AI agents that act on a user's behalf across online platforms. Custodial agent providers would owe users non-waivable duties of care and loyalty — safeguarding data privacy, avoiding self-dealing or foreseeable harm, and not repurposing user data for advertising or other secondary commercial uses — enforced by the FTC as unfair-or-deceptive-practices violations, with penalties assessed per affected user. Providers must register with the FTC before operating.

Separately, the bill requires "large online platforms" (more than 50 million U.S. users in a month) to offer fair, reasonable, and nondiscriminatory interfaces letting users delegate account and commerce interactions to third-party custodial agents, and directs NIST to publish technical standards for agent delegation credentials, identity verification, and auditable action records within 180 days of enactment. State law is preempted only where it directly conflicts with the Act; there is no private right of action, and an FTC-led interagency working group is tasked with developing future proposals on agent-fraud liability allocation, which the bill itself leaves unresolved.

It is one piece of Sen. Mark Warner's six-bill "A Framework for America's AI Future" package, introduced the same day as the Secure AI Development Act (S. 5061) and the SAFE AI Act (S. 5057).
