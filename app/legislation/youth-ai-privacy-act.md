---
title: "Youth AI Privacy Act"
short_name: "Youth AI Privacy Act"
bill_numbers: ["S. 4199"]
congress: 119
topic: "Children & Chatbots"
status: "committee_passed"
chamber_origin: "Senate"
introduced_date: "2026-03-25"
last_action: "Senate Commerce Committee advanced the bill by voice vote, as amended by the Markey substitute (as modified) and amendments from Cruz, Budd, and Lummis"
last_action_date: "2026-08-05"
sponsors: ["Sen. Ed Markey (D-MA)"]
cosponsor_count: null
committees: ["Senate Commerce, Science, and Transportation"]
scoring:
  axes:
    A: 1.5
    B: -1.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 4.0
  impact_components:
    R: 0.90
    D: 0.80
    E_f: 1.00
    P: 0.60
  likelihood:
    p_committee: 0.97
    p_enact: 0.22
    basis: "govtrack_corroborated; post-committee base rate adjusted"
  rationale:
    A: "RE-SCORED 2026-09-09 — FLAGGED: the prior A=2.0 rationale cited 'a data-use limit tied to a forthcoming maximum permitted period of use rule' as part of its basis; that is the same 30-day chatbot-memory retention cap and default-deletion requirement the Cruz amendment struck on a party-line 15-13 vote before the committee ordered the bill reported on 2026-08-05. With that provision gone, the bill's remaining conduct standards are: a ban on compulsive-use design features (push alerts, streaks, typing-bubble simulation), a ban on covert/targeted advertising to minors, and a ban on training on minors' data for commercial/algorithmic purposes, enforced via FTC rulemaking, state AG suits, and a private right of action. These are still real, ongoing conduct mandates on developers/deployers (above simple disclosure) but the loss of the data-retention/deletion mandate — the most concrete, self-executing obligation in the bill — removes its most binding single provision, so this drops from a solid +2 to +1.5: still squarely in the 'mandated process with enforcement' band (+2 rung) by virtue of the surviving design-feature and training-data bans and their private right of action, but scored down half a point to reflect that the substitute is materially weaker than what was scored on 8/1."
    B: "Unchanged from 8/1 scoring — the Cruz amendment targeted the retention-cap provision, not the preemption/savings-clause language. The bill still preempts state law only where a state law directly conflicts with it, and explicitly preserves state laws offering minors greater protection. No adopted amendment altered this provision, so B is not re-scored."
    C: "Unchanged from 8/1 — no new agency, oversight body, or reporting regime is created. Enforcement still relies on existing FTC and state AG authority plus the private right of action."
    D: "Unchanged from 8/1 — nothing in the text touches export controls, chips, or compute."
    E_consumer: "Unchanged from 8/1 — parents/guardians can still sue directly for violations of the surviving data-use and design-feature rules, with actual damages, punitive damages, attorney's fees, and injunctive relief. The struck retention-cap provision was one basis for suit among several; the private right of action itself was not amended, so this remains a meaningful damages-and-injunction remedy."
    F: "Unchanged — no data-center, permitting, siting, or energy provisions appear anywhere in the bill."
    R: "Unchanged from 8/1 — covers any AI chatbot made available to minors, a broad developer/deployer class with no notable carve-outs."
    Depth: "Recomputed from updated axis magnitudes; still driven mainly by the E_consumer private right of action rather than axis A, so the A revision from 2.0 to 1.5 does not change this component (max(|A|,|B|,|C|,|F|,E)/5 is still set by E=4.0)."
    E_f: "Unchanged from 8/1 — enforcement still includes a parent/guardian private right of action for damages and injunctive relief, not just agency action."
    P: "Unchanged from 8/1 — still runs alongside the GUARD Act, CHATBOT Act, and KOSA as part of the same committee markup cluster rather than standing alone as a novel framework."
    likelihood: "MAJOR REVISION 2026-09-09: the bill cleared Senate Commerce Committee by voice vote on 2026-08-05 (ordered reported, as amended by the Markey substitute and the Cruz/Budd/Lummis amendments) — committee passage has already occurred, so p_committee moves from the stale pre-markup estimate of 0.05 to 0.97 (not a full 1.0, reserving a sliver for the formal 'ordered reported' step not yet reflected in a reported calendar number as of this check). GovTrack's own bill page for S. 4199 has not published an updated prognosis reflecting the 8/5 markup as of this check, so this is base-rate adjusted rather than GovTrack-corroborated: post-committee-passage Senate bills in a comparable kids'-online-safety cluster (KOSA, CHATBOT Act) that advanced the same day face a genuine but uncertain path to a floor vote — no floor vote has been scheduled or reported as of 2026-09-09, and the bill would still need Rules/floor time, House concurrence, and presidential signature. p_enact raised from 0.02 to 0.22 to reflect that committee passage substantially de-risks the bill (removing the single biggest chokepoint) while floor time in a crowded kids-safety package, and the House's own competing KIDS Act framework, keep full enactment well short of a lock."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags: ["chatbots", "child safety", "data privacy"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/senate-bill/4199"
  - label: "Sponsor one-pager"
    url: "https://www.markey.senate.gov/imo/media/doc/youth_ai_privacy_act_one-pager.pdf"
  - label: "Senate Commerce Committee press release"
    url: "https://www.commerce.senate.gov/press/rep/release/commerce-committee-advances-kids-online-safety-legislation/"
  - label: "IAPP coverage"
    url: "https://iapp.org/news/a/us-senate-committee-approves-kosa-children-s-ai-safety-bills"
  - label: "K-12 Dive: KOSA clears key Senate panel"
    url: "https://www.k12dive.com/news/kids-online-safety-act-clears-key-senate-panel-with-bipartisan-support/827133/"
summary: "Markey bill setting a federal privacy floor for minors on AI chatbots, limiting data use and engagement-driving features."
timeline:
  - date: "2026-03-25"
    event: "Introduced by Sen. Markey; referred to Senate Commerce Committee"
  - date: "2026-08-05"
    event: "Senate Commerce Committee advanced the bill by voice vote alongside KOSA and other kids'-safety bills, after adopting a Cruz amendment (15-13, party-line) that struck the bill's 30-day chatbot-memory retention cap and default-deletion requirement"
---
The Youth AI Privacy Act would create a federal privacy floor for minors using AI chatbots: requiring clear, repeated disclosure that they aren't talking to a human; restricting chatbots to only using recently collected data — not long-term behavioral profiles — when personalizing responses to minors; and banning engagement-driving features like push notifications designed to increase minors' time on the app.

It sat alongside the GUARD Act and CHATBOT Act as one of three chatbot-safety bills with a Senate Commerce Committee markup on the calendar for early August 2026. On August 5, 2026, the committee advanced it by voice vote as part of a broader kids'-online-safety markup that also cleared KOSA. Before that vote, the committee adopted a Cruz amendment along party lines (15-13) that struck the bill's original 30-day cap on how long a chatbot may retain a minor's interaction data and its default-deletion requirement — a substantive weakening of the bill's core privacy mechanism prior to advancement.

**Update 2026-09-09:** As of this check, no Senate floor vote has been scheduled for the bill; it remains in the post-committee queue alongside KOSA and the other kids'-safety measures cleared the same day.
