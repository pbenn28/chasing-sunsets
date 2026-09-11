---
title: TAME Extreme Weather and Wildfires Act
short_name: TAME Act
bill_numbers:
- S. 1378
congress: 119
topic: Government Use & Procurement
status: committee_passed
chamber_origin: Senate
introduced_date: '2025-04-09'
last_action: Committee on Commerce, Science, and Transportation reported (amended); written report (S.Rpt. 119-88) filed
last_action_date: '2025-10-21'
sponsors:
- Sen. Brian Schatz (D-HI)
cosponsor_count: 3
committees:
- Senate Commerce, Science, and Transportation
scoring:
  axes:
    A: 0.0
    B: 0.0
    C: 1.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.90
    D: 0.20        # Depth — unrelated to axes.D
    E_f: 0.40
    P: 0.40
  likelihood:
    p_committee: 1.0
    p_enact: 0.41
    basis: "govtrack_corroborated"
  rationale:
    A: "Places no obligation on private AI developers. NOAA is directed to build its own weather-training datasets and may pursue public-private partnerships under Section 2(f), but those partnerships are permissive ('may explore'), not mandatory, and bind NOAA's own conduct, not a developer's. This is the government building and using AI, not regulating anyone who builds it."
    B: "The full bill text (as reported, S.Rpt. 119-88) contains no preemption or savings-clause language anywhere — it is a NOAA-internal directive with no state-facing provisions at all. The implicit-preemption floor does not apply because the bill doesn't score A ≥ +2; it creates no licensing, audit, or certification regime that could conflict with state law."
    C: "NOAA must submit biennial progress reports on dataset and AI-model development through 2035 (Section 2(c)) and a one-year classified/unclassified report assessing economic and intellectual-security risk from foreign access to U.S. weather data (Section 2(g)(3)) — real reporting activity with fixed deadlines, comparable to the AI-Ready Federal Data Guidelines Act's NIST guidelines. It stops short of a funded evaluation body or standing incident-reporting stream, so it lands at the 'studies with real deadlines' rung rather than higher."
    D: "The foreign-access security report (Section 2(g)(3)) concerns intellectual/economic security of weather data, not export controls, chip access, or compute diversion — it doesn't fit this axis's chip/compute-diffusion framing, so it scores 0 rather than a geopolitical-competition rung."
    E_consumer: "No deepfake, NCII, companion-bot, discrimination, or election-integrity content — the bill is entirely about NOAA's internal forecasting infrastructure."
    F: "No data-center, permitting, interconnection, siting, or energy-allocation content anywhere in the bill."
    R: "A federal bill directing the entire national weather/wildfire-forecasting agency (NOAA) to overhaul its AI dataset and modeling practices — full federal reach with no sector or revenue carve-out."
    Depth: "The only real structural teeth are the reporting requirements (axis C = 1.0); every other axis is 0, so Depth tracks the single active axis."
    E_f: "NOAA operates under fixed statutory reporting deadlines (biennial progress reports, a one-year security report) with congressional oversight, but there is no civil penalty, no agency rulemaking with penalties, and no private right of action — an obligation with a deadline but no stated penalty for missing it."
    P: "Adds a dataset/AI-integration mandate onto NOAA's existing statutory forecasting mission — sector-specific (weather/wildfire) and self-contained rather than a first-in-nation framework or a new permanent institution."
    likelihood: "GovTrack's own prognosis for S. 1378 is approximately 41% — anchoring to that figure. The bill cleared committee with a bipartisan amendment (Cruz) on 2025-04-30 and a formal written report followed nearly six months later (2025-10-21), signaling real committee engagement rather than a routine pass-through. It has a bipartisan four-member cosponsor list (2 Democrats, 1 Republican) and a House companion (H.R. 2770, Rep. Scott Franklin, R-FL), both of which support GovTrack's above-median estimate for a non-controversial infrastructure/agency-directive bill. No floor vote has occurred in either chamber as of September 2026, roughly 11 months after committee report — consistent with GovTrack's estimate reflecting real but incomplete momentum rather than near-certainty. p_committee is 1.0 since that step is complete; p_enact matches GovTrack's modeled figure given no material change in status since the report was filed."
  confidence: high
  text_source: full_text
  scored_at: "2026-09-09"
tags:
- NOAA
- weather forecasting
- wildfires
- government use
sources:
- label: Congress.gov
  url: https://www.congress.gov/bill/119th-congress/senate-bill/1378
- label: GovTrack.us
  url: https://www.govtrack.us/congress/bills/119/s1378
- label: CBO cost estimate
  url: https://www.cbo.gov/publication/61475
- label: Sen. Schatz press release
  url: https://www.schatz.senate.gov/news/press-releases/schatz-sheehy-introduce-bipartisan-legislation-to-use-ai-to-protect-communities-against-extreme-weather-wildfires
summary: Directs NOAA to build AI training datasets from federal weather data and integrate AI weather models into public forecasts and wildfire preparedness.
timeline:
- date: '2025-04-09'
  event: Introduced by Sen. Schatz with Sens. Sheehy, Luján, and Welch; referred to Senate Commerce, Science, and Transportation
- date: '2025-04-30'
  event: Committee marked up and ordered reported, with a Cruz amendment
- date: '2025-10-21'
  event: Written committee report filed (S.Rpt. 119-88)
- date: '2026-09-10'
  event: Verified — no floor vote scheduled in either chamber; House companion H.R. 2770 remains in committee
---

The bill directs NOAA to develop and curate comprehensive weather-forecasting training datasets from federal reanalysis and Earth-system data, in coordination with NASA, NSF, and outside technical experts, and to build and deploy AI weather models into public forecasts and wildfire preparedness. It authorizes NOAA to pursue public-private partnerships, requires biennial progress reports through 2035 and a one-year security assessment of foreign access to U.S. weather data, and directs NOAA to preserve funding for traditional physics-based forecasting alongside the new AI effort. The bill authorizes $105 million for FY2026 and $25 million annually for FY2027–2030. It cleared the Senate Commerce Committee with a bipartisan amendment in April 2025 and has a House companion, H.R. 2770.
