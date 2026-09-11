---
title: Stop AI Price Gouging and Wage Fixing Act of 2025
short_name: Stop AI Price Gouging and Wage Fixing Act
bill_numbers:
- H.R. 4640
congress: 119
topic: Civil Rights & Labor
status: committee
chamber_origin: House
introduced_date: '2025-07-23'
last_action: "Referred to the House Committees on Energy and Commerce, the Judiciary, and Education and Workforce"
last_action_date: '2025-07-23'
sponsors:
- Rep. Greg Casar (D-TX)
cosponsor_count: 24
committees:
- House Energy and Commerce
- House Judiciary
- House Education and Workforce
scoring:
  axes:
    A: 2.0
    B: 1.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 4.0
  impact_components:
    R: 0.80
    D: 0.80
    E_f: 1.00
    P: 0.60
  likelihood:
    p_committee: 0.06
    p_enact: 0.01
    basis: "base_rate_adjusted"
  rationale:
    A: "Directly prohibits the use of automated/algorithmic systems built on surveillance data for individualized pricing or wage-setting, backed by mandatory 180-day-advance disclosure of the data and logic driving those systems and consumer/worker correction rights — a real, enforceable conduct standard on deployers of these systems (developers and users of pricing/wage algorithms), landing at the 'mandated process with enforcement' rung rather than mere disclosure, since the underlying practice is banned outright (subject to narrow carve-outs) rather than merely disclosed. Stops short of pre-deployment licensing or certification, so it doesn't reach +3."
    B: "Contains an explicit, affirmative savings clause: the bill states it does not preempt state law except where there is a direct conflict, and specifically preserves states' ability to provide 'additional protections' beyond the federal floor, plus explicit preservation of collective-bargaining rights. This is squarely the rubric's 'ordinary savings clause bolted onto a substantive bill' rung (+1) — it falls short of +2/+3 because it doesn't repeal any existing federal preemption or add teeth beyond a standard non-conflict carve-out, but it clearly rules out the implicit-preemption floor since the savings clause is express and on-point."
    C: "Enforcement runs through the FTC (existing authority, unfair/deceptive-practices route), EEOC (existing authority), and state AGs — no new agency, evaluation body, or standing incident-reporting database is created. This is enforcement of a new substantive prohibition through existing regulators' ordinary authority, not a governance-capacity build, so it scores 0 rather than the +2 'enforcement staffing or new authority' rung — the bill gives FTC/EEOC a new rule to enforce, not new tools or staff to enforce it with."
    D: "No export-control, chip-access, or geopolitical content."
    E_consumer: "Backed by a private right of action with statutory damages (greater of actual loss or $3,000/violation), treble damages for willful violations, attorney's fees, a 5-year statute of limitations, and invalidation of pre-dispute arbitration/joint-action waivers — a broad private right of action reaching two distinct harms (consumer pricing and worker wage-setting) across sectors. This sits at the rubric's top E rung (5, broad private right of action across sectors) in mechanism, but is scored at 4 rather than a full 5 because the substantive prohibition itself carves out several common practices (cost-based pricing, published group discounts, opt-in loyalty programs, location/cost-of-living-based wage adjustments), narrowing the practical reach of the private right of action somewhat relative to an unqualified ban."
    F: "No data-center, permitting, siting, or energy content."
    R: "Reaches any company using automated/algorithmic systems for individualized consumer pricing or worker wage-setting based on personal or surveillance data — a broad, sector-agnostic consumer/labor-facing target class, though bounded by the bill's carve-outs (cost-based pricing, public group discounts, opt-in loyalty programs, location-based wage adjustments) that exclude a meaningful slice of current algorithmic pricing practice."
    Depth: "max(|A|, |B|, |C|, |F|, E) / 5 = max(2, 1, 0, 0, 4) / 5 = 0.80 — driven by the E_consumer score, since the private-right-of-action enforcement mechanism is the bill's most stringent single feature."
    E_f: "Private right of action plus FTC/state-AG/EEOC enforcement plus treble damages for willful violations — the maximum enforceability rung; consumers and workers, not just regulators, can sue directly."
    P: "A first-in-nation federal framework banning surveillance-based algorithmic pricing and wage-setting specifically — likely to be watched closely and could be copied at the state level or by a future Congress, but it's sector-specific (pricing/wages) rather than a general AI-governance template, and explicitly preserves rather than displaces state and collective-bargaining frameworks, so it lands at the 'first-in-nation framework likely to be copied' rung (0.8) rather than the top 'creates a permanent institution or preemption ceiling' rung."
    likelihood: "Verified 9/9-9/10/26: H.R. 4640 has 24 Democratic cosponsors (all Democrats; no Republican cosponsors) and was referred on introduction to three House committees (Energy and Commerce, Judiciary, and Education and Workforce) — a multi-committee referral that itself signals a difficult path, since it would need to clear all three under Republican-controlled committees before reaching the floor. No markup or hearing has been scheduled in any of the three committees as of this writing. GovTrack's own prognosis model gives this bill roughly a 1% chance of getting past committee and a near-0% chance of enactment, consistent with a purely Democratic-sponsored bill with no bipartisan cosponsors sitting in a Republican House. p_committee and p_enact are set slightly below/at that anchor given the added friction of a three-committee referral in the current Congress; explicitly noting the GovTrack anchor here rather than a bespoke estimate, since there's no committee or floor signal to adjust it against."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- surveillance pricing
- algorithmic wage-setting
- FTC
- EEOC
- private right of action
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/house-bill/4640
- label: GovTrack.us
  url: https://www.govtrack.us/congress/bills/119/hr4640
- label: Sponsor press release — Rep. Greg Casar
  url: https://casar.house.gov/media/press-releases/news-congressman-greg-casar-introduces-new-stop-ai-price-gouging-and-wage
summary: Bans the use of AI/algorithmic systems for surveillance-based individualized pricing and algorithmic wage-setting, enforced through the FTC, EEOC, state AGs, and a private right of action.
timeline:
- date: '2025-07-23'
  event: Introduced by Rep. Greg Casar; referred to House Energy and Commerce, Judiciary, and Education and Workforce
---

The Stop AI Price Gouging and Wage Fixing Act of 2025 bans the use of automated/algorithmic systems that rely on personal or surveillance data to set individualized consumer prices, subject to carve-outs for cost-based pricing, publicly posted group discounts (seniors, students, veterans, teachers), and opt-in loyalty programs. It separately bans "surveillance-based wage setting" — using automated tools and personal or tracking data to set worker pay — permitting only location and local cost-of-living data as inputs. Companies must publish, 180 days in advance, the data and logic driving their pricing or wage-setting systems and give consumers/workers a way to challenge inaccurate data. Enforcement runs through the FTC (as an unfair-or-deceptive-practice violation), the EEOC (for wage-setting violations), state attorneys general, and a private right of action with statutory damages (the greater of actual loss or $3,000 per violation, trebled for willful violations), plus invalidation of pre-dispute arbitration and joint-action-waiver clauses. The bill contains an explicit savings clause preserving state law except where it directly conflicts, states that it sets only a "minimum standard," and expressly preserves collective-bargaining rights and existing union protections.

**Overlap with the Preventing Algorithmic Collusion Act (S. 232):** both bills target algorithmic pricing, but they aim at different mechanisms and are not duplicative. S. 232 (already tracked) is narrower and antitrust-focused — it prohibits pricing algorithms trained on *nonpublic competitor data* (a collusion-facilitation problem) and is enforced via DOJ/FTC antitrust tools plus a litigation presumption. H.R. 4640 is broader and consumer/labor-protection-focused — it bans surveillance-based individualized pricing regardless of whether competitor data or collusion is involved, extends an analogous ban to algorithmic wage-setting (which S. 232 does not touch at all), and is enforced primarily through a private right of action rather than antitrust doctrine. A pricing algorithm could violate one, both, or neither depending on whether it uses nonpublic competitor data (S. 232's trigger) versus surveillance/personal data for individualized pricing (H.R. 4640's trigger) — the two are complementary rather than redundant.
