---
title: Preventing Algorithmic Collusion Act of 2025
short_name: Preventing Algorithmic Collusion Act
bill_numbers:
- S. 232
congress: 119
topic: Civil Rights & Labor
status: committee
chamber_origin: Senate
introduced_date: '2025-01-23'
last_action: Read twice and referred to the Senate Committee on the Judiciary
last_action_date: '2025-01-23'
sponsors:
- Sen. Amy Klobuchar (D-MN)
cosponsor_count: 8
committees:
- Senate Judiciary
scoring:
  axes:
    A: 2.0
    B: -1.0
    C: 2.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.0
  impact_components:
    R: 0.60
    D: 0.40
    E_f: 0.80
    P: 0.40
  likelihood:
    p_committee: 0.08
    p_enact: 0.02
    basis: "base_rate_adjusted"
  rationale:
    A: "Requires companies to produce audit reports to DOJ/FTC on demand, bars using or distributing pricing algorithms trained on nonpublic competitor data (backed by civil penalties), and creates a rebuttable antitrust presumption along with a disclosure mandate enforceable as an FTC Act violation — a real, enforceable process, though it stops short of requiring pre-deployment licensing or certification."
    B: "Says nothing about preempting or preserving state authority; the only related clauses simply preserve existing federal antitrust law. Because it sets up a genuine federal enforcement scheme without an express savings clause for states, it's treated as implicitly narrowing state latitude at the margins."
    C: "Gives DOJ and FTC new transparency and reporting tools plus a litigation presumption to use against pricing collusion — a boost to existing regulators' authority rather than a new agency or standing database."
    D: "No export-control or geopolitical content."
    E_consumer: "Backs the prohibition with civil penalties rather than criminal liability — more teeth than a bare labeling requirement, but not a criminal statute."
    F: "No data-center, permitting, or energy content."
    R: "Reaches pricing algorithms across many consumer-facing industries, but only where they're built on nonpublic competitor data — a real but bounded slice of the pricing-algorithm landscape."
    Depth: "Driven mainly by the enforcement mechanisms in Secs. 3-6 (audit reports, the use prohibition, and the litigation presumption) — the bill doesn't reach much further than that core antitrust toolkit."
    E_f: "DOJ/FTC enforcement backed by civil penalties and a legal presumption gives this real bite, though it stops short of creating a private right of action."
    P: "A narrow antitrust fix aimed at one practice — pricing-algorithm collusion via nonpublic data — rather than a broad AI-governance framework."
    likelihood: "Re-verified 9/9/26: S. 232 itself has had no markup or vote and remains parked in Senate Judiciary with no floor action — no direct committee movement on this specific bill. However, the surrounding policy area heated up materially since 8/1: the Senate Judiciary Crime & Counterterrorism Subcommittee held a bipartisan hearing on 8/4/26 ('Your Data, Their Profit: The Consumer Cost of AI Surveillance Pricing,' chaired by Hawley with Durbin as ranking member), producing a stated bipartisan Hawley-Blumenthal intent to draft new surveillance-pricing legislation, and DOJ signaled in June 2026 that criminal enforcement of algorithmic pricing collusion remains on the table. None of that is committee action on S. 232 itself — it's a related but distinct proposal (real-time 'surveillance pricing' vs. S. 232's narrower nonpublic-competitor-data collusion prohibition) — but it signals rising bipartisan salience in the same policy neighborhood that could pull S. 232 or its provisions into a future vehicle. p_committee nudged up slightly (0.07 to 0.08) to reflect that salience; p_enact held, since no actual legislative vehicle exists yet and any successor bill would likely be a fresh Hawley-authored text rather than S. 232 advancing as-is."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- antitrust
- pricing algorithms
- collusion
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/232
- label: Senate Judiciary Committee — AI surveillance pricing hearing (related, distinct proposal)
  url: https://www.judiciary.senate.gov/committee-activity/hearings/your-data-their-profit-the-consumer-cost-of-ai-surveillance-pricing
summary: Prohibits pricing algorithms that use nonpublic competitor data to facilitate collusion.
timeline:
- date: '2025-01-23'
  event: Introduced in the Senate
- date: '2025-01-23'
  event: Read twice and referred to the Judiciary Committee
- date: '2026-08-04'
  event: 'Related but distinct development: Senate Judiciary Crime & Counterterrorism Subcommittee holds bipartisan hearing on AI "surveillance pricing" (not a hearing on S. 232 itself); Hawley and Blumenthal signal intent to draft new legislation'
- date: '2026-09-09'
  event: Re-verified — no markup or committee vote on S. 232 itself since referral
---

The bill makes it unlawful to use or distribute a pricing algorithm that uses, incorporates, or was trained with nonpublic competitor data, and creates transparency and reporting tools letting the DOJ or FTC require detailed disclosures about pricing algorithms. It establishes a legal presumption to aid antitrust enforcement and provides civil penalties.

Update (9/9/26): S. 232 itself has not moved since referral, but the adjacent "surveillance pricing" issue gained bipartisan momentum after an August 2026 Senate Judiciary subcommittee hearing, with Sens. Hawley and Blumenthal signaling plans for a new, broader bill on real-time AI pricing.
