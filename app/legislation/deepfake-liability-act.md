---
title: "Deepfake Liability Act"
short_name: "Deepfake Liability Act"
bill_numbers: ["H.R. 6334"]
congress: 119
topic: "Deepfakes & Synthetic Media"
status: "introduced"
chamber_origin: "House"
introduced_date: "2025-12-01"
last_action: "Referred to the House Committee on Energy and Commerce"
last_action_date: "2025-12-01"
sponsors: ["Rep. Jake Auchincloss (D-MA)", "Rep. Celeste Maloy (R-UT)"]
cosponsor_count: 1
committees: ["House Energy and Commerce"]
scoring:
  axes:
    A: 1.0
    B: 0.0
    C: 0.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 2.5
  impact_components:
    R: 0.85
    D: 0.50
    E_f: 0.60
    P: 0.40
  likelihood:
    p_committee: 0.04
    p_enact: 0.01
    basis: "govtrack_corroborated"
  rationale:
    A: "The core mechanism -- conditioning Section 230 immunity on a platform 'duty of care' for cyberstalking and intimate-privacy violations -- binds interactive computer services (platforms), not AI developers, so it's a domain-general platform-liability mechanism that would cap at 0 under the guardrail. But the bill also amends Section 230(f)(3)'s definition of 'information content provider' to add coverage for content created 'through solicitation, encouragement, or the use of a generative model' -- a genuine, narrow, AI-specific channel that could newly expose a generative-AI provider itself to liability for content its model generates, where none existed before. That's exactly the kind of contingent-but-real AI-specific carve-out the rubric allows to land at the ±1 ceiling rather than 0; it doesn't rise higher because it changes a liability definition rather than imposing any affirmative conduct standard (disclosure, audit, incident reporting) on developers."
    B: "No preemption or savings-clause language, and the implicit-preemption floor doesn't apply because axis A scores well below +2 and the bill doesn't establish an ongoing federal regulatory scheme over AI developers -- it's a Section 230/TAKE IT DOWN Act amendment aimed at platforms. Silent on state authority to regulate AI."
    C: "FTC rulemaking (in consultation with FCC and DOJ) is directed within 180 days of enactment, but it's scoped to defining the platform duty-of-care standard and TAKE IT DOWN Act notice-and-removal process -- domain-general platform-liability rulemaking, not a new AI-oversight body, evaluation capacity, or incident-reporting database aimed at AI systems specifically. No governance-capacity effect on AI beyond that incidental scope, so this scores 0 rather than the 'enforcement staffing/new regulator authority' rung."
    D: "No export-control, chip-access, or geopolitical-competition content."
    E_consumer: "Conditions platform immunity on responsiveness to cyberstalking and intimate-privacy-violation complaints and ties compliance to the TAKE IT DOWN Act's existing notice-and-removal process, with FTC/FCC/DOJ regulatory enforcement (not a new private right of action -- the bill doesn't create one of its own, it leverages TAKE IT DOWN's existing FTC enforcement track, which already carries civil penalties up to roughly $53,000 per violation). That's substantially more than a labeling-only rule but short of a broad private right of action across sectors, and it's confined to one harm category (cyberstalking/NCII deepfakes) rather than spanning multiple consumer-harm types -- landing between the 'end-user labeling' and 'broad private right of action' rungs, closer to the criminal-liability-equivalent rung given the FTC civil-penalty backing."
    F: "No data-center, permitting, interconnection, energy, or siting content."
    R: "Applies to 'interactive computer services' broadly -- essentially any platform hosting user content -- which is close to the full universe of the consumer-facing target class for this harm category, though its practical bite depends on platforms choosing to lose Section 230 protection rather than comply, which is a strong incentive to comply given TAKE IT DOWN Act penalties already in force."
    Depth: "Recomputed after the frontier/systemic-risk guardrail correction — now driven by axis E (consumer/near-term harm) at 2.5/5."
    E_f: "Enforcement runs through FTC (with FCC/DOJ consultation) civil-penalty rulemaking layered onto the existing TAKE IT DOWN Act regime, not a private right of action created by this bill itself -- agency rulemaking plus civil penalties is the correct rung."
    P: "A targeted amendment bolted onto two existing frameworks (Section 230 and the TAKE IT DOWN Act) rather than a new institution or a first-in-nation template -- sector-specific and self-contained within the platform-liability space."
    likelihood: "GovTrack's own prognosis for H.R. 6334 (checked 2026-09-09) gives roughly a 4% chance of advancing past committee and a 1% chance of enactment. Introduced 2025-12-01, referred to House Energy and Commerce, with only one cosponsor (Rep. Maloy, the bill's bipartisan co-lead) and no markup or further action reported over more than nine months. Adopting GovTrack's figures directly rather than adjusting -- a narrow-scope, single-committee bill with minimal cosponsorship at this stage of a Congress matches the base rate GovTrack's model reflects, and nothing in the public record (no hearing scheduled, no companion Senate bill found) suggests upward pressure on those odds."
  confidence: low
  text_source: summary
  scored_at: "2026-09-09"
tags: ["deepfakes", "NCII", "Section 230", "platform liability", "TAKE IT DOWN Act"]
sources:
  - label: "Congress.gov"
    url: "https://www.congress.gov/bill/119th-congress/house-bill/6334"
  - label: "GovTrack.us"
    url: "https://www.govtrack.us/congress/bills/119/hr6334"
  - label: "Sponsor press release (Rep. Auchincloss)"
    url: "https://auchincloss.house.gov/media/press-releases/auchincloss-maloy-introduce-bipartisan-bill-on-section-230-liability-shield"
summary: "Bipartisan bill conditioning platforms' Section 230 immunity on a duty of care for cyberstalking and deepfake/NCII harassment, tied to the TAKE IT DOWN Act's takedown process."
timeline:
  - date: "2025-12-01"
    event: "H.R. 6334 introduced by Reps. Auchincloss and Maloy; referred to House Energy and Commerce"
  - date: "2026-09-09"
    event: "Verified -- still at referred-to-committee stage; GovTrack prognosis approx. 4% past committee, 1% enacted"
---
The Deepfake Liability Act would amend Section 230 of the Communications Act so that a platform only keeps its liability shield if it implements a "reasonable process" for addressing cyberstalking and intimate-privacy violations -- including a clear, accessible complaint process tied to the TAKE IT DOWN Act's existing notice-and-removal requirements, and data logging that can support victims' legal proceedings. Platforms that don't meet this duty of care lose Section 230 protection for the underlying conduct.

The bill also amends Section 230(f)(3)'s definition of "information content provider" to add coverage for content created "through solicitation, encouragement, or the use of a generative model" -- a change that could expose an AI developer or deployer to liability for content its own generative model produces, where Section 230 previously offered a shield. The FTC, in consultation with the FCC and DOJ, must issue implementing regulations within 180 days of enactment.

Sponsors Jake Auchincloss (D-MA) and Celeste Maloy (R-UT) frame the bill around findings that roughly 98% of online deepfake imagery is pornographic and 99% of that targets women, aiming the duty-of-care requirement squarely at platforms that host non-consensual intimate deepfakes and AI-enabled harassment.
