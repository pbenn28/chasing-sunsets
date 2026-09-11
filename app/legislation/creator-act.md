---
title: "Creative Rights Ensuring Artists' Technique and Originality are Reserved Act (CREATOR Act)"
short_name: "CREATOR Act"
bill_numbers: ["H.R. 9112"]
congress: 119
topic: "Deepfakes & Synthetic Media"
status: "introduced"
chamber_origin: "House"
introduced_date: "2026-06-02"
last_action: "Referred to the House Committee on the Judiciary"
last_action_date: "2026-06-02"
sponsors: ["Rep. Beth Van Duyne (R-TX)", "Rep. Yvette Clarke (D-NY)", "Rep. Valerie Foushee (D-NC)", "Rep. Burgess Owens (R-UT)"]
cosponsor_count: 4
committees: ["House Judiciary"]
scoring:
  axes:
    A: 0.0
    B: -1.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 4.0
  impact_components:
    R: 0.75
    D: 0.80
    E_f: 1.00
    P: 0.60
  likelihood:
    p_committee: 0.09
    p_enact: 0.04
    basis: "govtrack_corroborated"
  rationale:
    A: "Creates a new civil right for visual artists against 'stylistic impersonation' and imposes liability on those who commercially exploit or distribute AI-generated impersonations of a specific artist's style -- but the bill text explicitly exempts development, distribution, licensing, or provision of a general-purpose AI system from liability unless the provider intentionally configured that system to generate impersonations of a specifically identified artist. That express carve-out means an ordinary frontier model developer incurs no obligation under this Act at all; only a narrow, deliberately-built impersonation tool could trigger it, and even then the liability runs against the tool's commercial exploitation, not against training or deployment conduct generally. No disclosure, audit, or reporting standard is imposed on developers as such, so this scores 0 rather than reaching even the ±1 guardrail ceiling -- the AI-specific channel here is defined out of the bill's own liability scheme for the general-purpose case."
    B: "Section preempts state-law causes of action only 'to the extent that such causes of action impose liability for conduct that constitutes stylistic impersonation as defined in this Act' -- narrow conflict preemption confined to the one new cause of action the bill itself creates. It expressly preserves state right-of-publicity/misappropriation claims based on name, likeness, or voice, and state unfair-competition/consumer-protection law generally. This doesn't rise to field preemption in even one domain (right-of-publicity law generally survives intact) -- it only forecloses states from independently criminalizing/civilly punishing the specific 'stylistic impersonation' tort this Act invents, so it lands at 'conflict preemption only.' The implicit-preemption floor doesn't separately apply since axis A scores 0, well under +2."
    C: "No new agency, evaluation body, or regulator staffing -- enforcement runs entirely through private civil suits by artists and rights-holders, not through any government oversight capacity."
    D: "No export-control, chip-access, or geopolitical-competition content."
    E_consumer: "Creates a private right of action with statutory damages of $10,000-$100,000 per work for intentional commercial infringement, rising to $50,000-$150,000 per work for willful violations involving intentional targeting and commercial exploitation -- a real, substantial private right of action with meaningful statutory damages, comparable to NO FAKES Act's private-suit mechanism but confined to one harm category (AI stylistic impersonation of visual artists) rather than spanning multiple consumer-harm types, so it lands at the same 'broad private right of action, one domain' level rather than the maximum multi-sector rung."
    F: "No data-center, permitting, interconnection, energy, or siting content."
    R: "Covers visual artists broadly and binds anyone who commercially exploits or publicly distributes a stylistic impersonation in or affecting interstate commerce -- a wide target class for this harm type -- but the bill's own safe harbors (commentary/criticism, parody/satire, research/education, platform notice-and-takedown safe harbor, and the general-purpose-AI carve-out) narrow real-world reach somewhat relative to a bill with no such exemptions, landing below NO FAKES Act's 0.95 but still capturing most commercial stylistic-impersonation conduct."
    Depth: "Recomputed after the frontier/systemic-risk guardrail correction — now driven by axis E (consumer/near-term harm) at 4.0/5."
    E_f: "Statutory damages available directly to artists and rights-holders through a private right of action -- the strongest enforcement rung on this scale, matching NO FAKES Act's enforcement mechanism."
    P: "A new, narrow federal IP-adjacent right layered onto existing right-of-publicity and copyright frameworks rather than a wholly new institution -- if enacted it would be a first-in-nation federal framework for 'stylistic impersonation' specifically, likely to be watched as a template given the parallel Andersen v. Stability AI-style litigation already underway, but its narrow scope (one right, one artist class) keeps it below a 'permanent institution or preemption ceiling' rung."
    likelihood: "GovTrack's prognosis for H.R. 9112 (checked 2026-09-09) gives roughly a 9% chance of advancing past committee and a 4% chance of enactment -- adopting GovTrack's figures directly. Introduced 2026-06-02 with bipartisan sponsorship (Van Duyne R-TX, Clarke D-NY, Foushee D-NC, Owens R-UT) and 4 cosponsors, referred to House Judiciary, with no markup or hearing reported as of this check roughly three months later. The bipartisan Congressional Creators Caucus backing and active stakeholder support (Adobe, artist groups) modestly outperform a typical single-sponsor bill at this stage, consistent with GovTrack's above-median prognosis for a newly introduced bill, but it remains far from advancing."
  confidence: low
  text_source: summary
  scored_at: "2026-09-09"
tags: ["AI stylistic impersonation", "artists", "copyright-adjacent", "private right of action"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/house-bill/9112"
  - label: "GovTrack.us"
    url: "https://www.govtrack.us/congress/bills/119/hr9112"
  - label: "Sponsor press release (Rep. Van Duyne)"
    url: "https://vanduyne.house.gov/2026/6/reps-van-duyne-clarke-and-foushee-introduce-bipartisan-creator-act-to-protect-creators-with-visual-artistic-protections"
summary: "Bipartisan bill creating a new federal right for visual artists against AI-generated stylistic impersonation, with statutory damages and a narrow carve-out shielding general-purpose AI developers."
timeline:
  - date: "2026-06-02"
    event: "H.R. 9112 introduced by Rep. Van Duyne with Reps. Clarke, Foushee, and Owens; referred to House Judiciary"
  - date: "2026-09-09"
    event: "Verified -- still at referred-to-committee stage; GovTrack prognosis approx. 9% past committee, 4% enacted"
---
The CREATOR Act would give visual artists (or their rights-holders) an exclusive federal right to authorize the commercial exploitation or public distribution of a "stylistic impersonation" of their distinctive artistic technique -- targeting AI tools and services marketed or used to generate images "in the style of" a specific, identifiable artist. The right excludes protection for ideas, genres, artistic movements, or commonly used visual styles not publicly associated with a particular artist, and it doesn't reach general artistic influence, independent human authorship, or incidental AI assistance.

Violators face statutory damages of $10,000-$100,000 per infringing work for intentional commercial conduct, rising to $50,000-$150,000 per work for willful, targeted commercial exploitation. The bill includes safe harbors for commentary, criticism, parody, satire, and research/education, plus a notice-and-takedown safe harbor for platforms that act quickly on valid infringement notices. Critically, general-purpose AI systems are exempt from liability altogether unless their provider intentionally configured the system to generate impersonations of a specifically identified artist -- an ordinary foundation-model developer isn't exposed just because users can prompt its model to mimic an artist's style.

On preemption, the bill displaces state-law causes of action only to the extent they would separately regulate the same "stylistic impersonation" conduct this Act defines, while expressly preserving state right-of-publicity, misappropriation, and consumer-protection law. Sponsors Beth Van Duyne (R-TX), Yvette Clarke (D-NY), Valerie Foushee (D-NC), and Burgess Owens (R-UT) developed the bill through the bipartisan Congressional Creators Caucus, with backing from artist groups and Adobe.
