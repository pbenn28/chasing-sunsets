# AI Legislation Tracker — Scoring Rubric

This document is the authoritative rubric for scoring bills tracked at `/legislation`. It exists so that scoring is a defensible, repeatable application of explicit criteria rather than editorial "vibes." Research agents scoring a bill should read this document in full before scoring, apply each ladder literally, and write a short rationale citing the specific provision(s) that justify the chosen value.

**These scores are meant to be final.** Once written, they are not revisited or hand-tuned — so apply the rubric carefully, and when a bill sits between two rungs, pick the closer one and say so in the rationale rather than defaulting to a round number.

## Sign convention (locked)

**Positive = safety / restriction. Negative = deregulation / acceleration.** This applies to every signed axis (A, B, C, D, F). Do not flip it, and do not reuse any pre-existing `safety_accel` value from the old scoring system — that field used the opposite convention and must be treated as meaningless for this rubric.

## The axis set

There are five **signed** axes, one **unsigned** axis, and a set of derived **impact components**. Three of the signed axes feed the headline safety composite at full or partial weight, one (D) is excluded from the composite by default (but still recorded and shown).

### Guardrail: every axis measures effect on AI governance, not domain-general mechanisms (read this before scoring A, B, or C)

**Axes A, B, and C score a bill's effect on AI governance specifically — not the presence of a mechanism that happens to use the same words as the rubric.** "Incident reporting," "savings clause," and "standing information flow" are generic legal and legislative-drafting terms that show up constantly in bills that have nothing to do with AI safety regulation. A bill can contain a mechanism that is, in isolation, a textbook example of a rung's literal wording — mandatory reporting, a preemption carve-out, a new federal database — and still deserve close to a 0 on that axis, because the mechanism's *object* is something other than AI governance (CSAM detection, tax administration, financial fraud, whatever the bill is actually about).

The test: **does this mechanism observe, constrain, or govern AI development or deployment, or does it just happen to appear in a bill that also mentions AI?** Ask who or what the obligation actually runs against and what it actually tracks. "AI-generated CSAM" reported to NCMEC's CyberTipline is CSAM enforcement that incidentally covers one AI-produced category, not AI-safety incident reporting — the CyberTipline doesn't observe model behavior, doesn't feed into any AI oversight function, and would exist in identical form if AI didn't exist. A savings clause preserving state authority over child-exploitation law says nothing about states' authority to regulate frontier model development. A reporting mandate aimed at platforms that host third-party content binds distributors, not the developers axis A is about.

**Rule: a domain-general mechanism that superficially matches a rung's wording caps at ±1 on that axis, regardless of how well-drafted, well-enforced, or textually on-point it looks.** This is a hard ceiling, not a starting point — don't score it at ±1 by default; score whatever the actual (usually smaller, often 0) AI-governance effect is, then apply the cap only to prevent an inflated read from exceeding it. If there's a genuine, if narrow or contingent, AI-specific channel buried in an otherwise domain-general mechanism (e.g. whether an AI developer could itself qualify as a covered entity under a platform-liability bill), that can justify landing at the ±1 ceiling with the contingency spelled out in the rationale — but don't let an unsettled interpretive question silently harden into a bigger number just because the rest of the bill is well-documented.

This failure mode reads as thorough scoring because everything else about it can be correct — the right section cited, the right dollar figure, real full-text verification — while the number itself answers the wrong question. It is the single most likely place for a high-confidence, full-text-sourced score to still be wrong, because good research quality has nothing to do with whether the axis was scoped correctly in the first place.

### Guardrail: frontier/systemic risk vs. near-term consumer harm (read this before scoring A, B, or C)

**Axes A, B, and C feed the safety composite `S` because, together, they're meant to track one specific fight: the pace and stringency of frontier/systemic AI development, and states' authority to regulate it.** Axis E (consumer/near-term harm) exists as a separate, unsigned, impact-only axis — deliberately excluded from `S` — precisely to hold everything else: deepfakes, NCII, companion-bot manipulation, algorithmic discrimination, election integrity, child and senior protection. A bill can impose a real, enforced, well-drafted conduct mandate on "AI developers" or "covered entities" and still belong almost entirely on axis E, because the mandate's *subject* is a narrow demographic or sectoral harm rather than frontier or systemic AI risk.

The test, applied independently to each of A/B/C: **is this mechanism about frontier-scale training, catastrophic/CBRN risk, loss-of-control, or systemic AI oversight capacity — or is it about protecting a specific population or narrow harm domain (children, seniors, workers, voters, discrimination) from AI already in ordinary deployment?** A chatbot bill's parental-control mandate, age-verification duty, or FTC incident-reporting requirement about *child-safety* incidents can textually match axis A's "+2 mandated process" rung or axis C's "+3 standing information flow" rung — but if nothing in it reaches frontier-model training, deployment-scale risk, or systemic AI oversight, it isn't what those rungs are describing. Score it near the floor on A (rarely above +0.5–+1, even for a real enforced mandate) and near the floor on C (rarely above +0.5–+1, even for a real standing reporting regime) — then let axis E carry the bill's actual severity, which is exactly what E is for.

**This applies to axis B too, not just A and C.** A savings clause that guarantees states may pass *more protective chatbot-safety law*, or *more protective senior-protection law*, says nothing about states' authority to regulate frontier AI development — it's scoped to the bill's own narrow topic. Don't score it at the "+3 affirmative guarantee with teeth" rung just because the clause is textually unconditional; cap it near "+1 ordinary savings clause" unless the preservation language is genuinely general (i.e. it preserves state authority over AI regulation broadly, not just this bill's own subject). The same logic runs in both directions: a narrow-domain liability shield or immunity provision shouldn't be scored as a deep negative on A either, for the same reason.

This is a sharper version of the AI-governance-scoping guardrail above, not a restatement of it — a mechanism can be genuinely, unambiguously AI-specific (a chatbot-only conduct standard is not a domain-general mechanism the way CyberTipline reporting is) and *still* belong on E rather than A/B/C, because AI-specificity and frontier/systemic relevance are different questions. Getting the first right and missing the second produces a scoring pattern that looks careful — real section citations, real enforcement mechanisms, real savings-clause text — while still landing a narrow child-safety or anti-discrimination bill at a higher `S` than a literal AI data-center moratorium. That mismatch is the signal something went wrong, not a legitimate result: a bill has to actually move the frontier-safety-vs-acceleration needle to score high on the composite that measures it.

### Guardrail: conduct standards vs. input chokepoints (read this before scoring A or F)

**Axis A scores only conduct standards imposed on developers** — obligations that regulate the *act* of training or deploying a model (disclosure, audits, incident reporting, a training moratorium, a cap on training-run FLOP). If a bill instead constrains development by restricting an *input* — compute hardware, electricity, siting, water, land — that provision belongs on **axis F** (domestic compute/energy chokepoints) or **axis D** (foreign/export-control chokepoints), never on axis A, even if the practical effect is similarly restrictive.

This distinction is easy to blur because both a training moratorium and a data-center moratorium can look like "+5, nothing gets built" — but they are different levers with different political coalitions and different failure modes, and conflating them was a real scoring error in an earlier pass of this rubric. The test: **does the obligation name the model-training/deployment activity itself, or does it name a physical input to that activity?** A statutory cap on training-run FLOP is **A +5** (it regulates the act of training). A cap on megawatts a facility may draw, or a moratorium on new data-center construction, is **F +5** (it regulates an input), even though a bill that caps compute hardware capacity tightly enough can have a similar chilling effect to a training moratorium. Score bills with both kinds of provisions on both axes independently — don't pick one.

---

### A. Frontier developer stringency (−5 … +5) · core

What obligation, if any, does the bill place on developers of frontier/advanced AI systems, and how strong is it?

**Apply the guardrail above before scoring this axis: only conduct standards on developers belong here.** A cap on training-run FLOP is A (it regulates training itself). A cap on data-center megawatts, a compute-hardware import limit, or a moratorium on new AI facility construction is **not** A — score that on axis F (or D if it's an export/foreign-access control) instead.

| Score | Criteria |
|---|---|
| +5 | Prohibition or license-to-exist: training moratorium, statutory FLOP/compute-scale cap on training runs, pre-approval required to train |
| +4 | Government intervention authority over deployed systems — shutdown, revocation, mandated recall |
| +3 | Pre-deployment gating by an outside party: licensed verifiers, mandatory audit/certification before release |
| +2 | Mandated process with enforcement: incident reporting, required risk framework, whistleblower protection, eval access |
| +1 | Disclosure only — publish a framework, model cards, training-data provenance, no substantive standard |
| +0.5 | Procurement and government-use conditions. Binds the buyer, not the builder |
| 0 | Studies, task forces, definitions |
| −0.5 | Capacity and money with no obligations attached (e.g. compute subsidies, grant programs) |
| −1 | Codifies voluntary/light-touch practice in lieu of mandates |
| −2 | Marginal relief: time-limited waivers, sandbox exemptions, small-developer carve-outs |
| −3 | Substantive liability limitation — immunity or damages caps for model outputs |
| −4 | Repeal or nullification of existing binding federal obligations |
| −5 | Blanket immunity plus repeal. Reserve this for the most extreme case |

**Why compute subsidies score −0.5, not on axis C:** axis A is about obligations placed on developers. Giving developers money or compute with no strings attached is not itself restrictive or governance-building — if anything it accelerates capability, so it's mildly negative here. It is deliberately *not* scored on axis C (see below) — capacity to build is not capacity to govern.

---

### B. Preemption posture (−5 … +3) · core

Does the bill preserve, narrow, or eliminate states' ability to regulate AI independently?

| Score | Criteria |
|---|---|
| +3 | Affirmative statutory guarantee that states may exceed the federal standard, with a savings clause that has teeth |
| +2 | Repeals or defunds existing preemption (e.g. voids a prior executive order's preemptive effect, bars funds for enforcing it) |
| +1 | Ordinary savings clause bolted onto a substantive bill |
| 0 | Silent on preemption |
| −1 | Conflict preemption only (states barred only where they directly conflict with federal law) |
| −2 | Field preemption in one narrow domain |
| −3 | Time-limited broad moratorium on state AI regulation |
| −4 | Permanent broad field preemption |
| −5 | Broad preemption **plus** displacement of state tort and common-law claims, or federal funds conditioned on state non-regulation |

**Why the −4/−5 gap is the largest intentional discontinuity in this rubric:** ordinary field preemption (−4) still leaves tort and common-law claims as a backstop — an injured party can still sue. Stripping that too (−5) removes the *only* enforcement mechanism that doesn't depend on a federal agency choosing to act. That is a qualitatively different, much more severe outcome than "just" blocking new state statutes, so it must not be treated as one more step on a smooth ladder. When scoring, check specifically for tort/common-law displacement language or funding conditions before assigning −5 — don't assign it just because a moratorium sounds sweeping.

**Preemption does not need to be explicit — the implicit-preemption floor.** Under ordinary conflict-preemption doctrine, a comprehensive federal regulatory scheme can preempt conflicting state law *by implication*, even with zero preemption language in the bill text. Scoring such a bill B = 0 ("silent") is wrong — silence is not neutral when the scheme itself does the preempting. The rule: **any bill that scores A ≥ +2 (frontier developer stringency), establishes a federal regulatory scheme, and contains no express savings clause floors at B = −1**, even if no one ever wrote the word "preemption."

- **"Establishes a federal regulatory scheme"** means an ongoing, structured federal regulatory regime — licensing, mandatory audits, a standing incident-reporting requirement, a certification/verification process. It does *not* mean a one-off study, a narrow disclosure requirement, or a purely definitional provision.
- **"Express savings clause"** means the bill text affirmatively states that it does not preempt or limit state authority to regulate in the same space (e.g. "Nothing in this Act shall be construed to preempt any State law..."). Absence of any preemption *language at all* is not a savings clause — it's exactly the silence this rule is meant to catch.
- This is a **floor, not a fixed value**: if a bill's actual text supports a more negative (more preemptive) score than −1, use that instead — the floor only raises an under-scored B up to −1, it never lowers an already-correctly-scored one.
- Apply this check to every bill scoring A ≥ +2. Because it depends on the presence or absence of specific text (a savings clause), it requires reading the bill's actual text, not just its summary — see the `text_source` rule below.

---

### C. Governance capacity (−3 … +5) · core, low weight

Does the bill build or strip the government's own capacity to observe, evaluate, and enforce — as distinct from the capacity to build AI systems?

| Score | Criteria |
|---|---|
| +5 | New agency or major statutory authority, appropriated and enforceable |
| +4 | Authorizes and funds a dedicated evaluation body (e.g. national testbeds, a security-institute authorization) |
| +3 | Standing information flows: mandatory incident reporting into a government database |
| +2 | Enforcement staffing or new authority for an existing regulator; whistleblower channels |
| +1 | Studies, GAO reviews, advisory committees with real reporting deadlines |
| 0 | None |
| −1 | Cuts or lets lapse existing capacity |
| −2 | Strips authority from a regulator; sunsets an evaluation body |
| −3 | Affirmatively bars an agency from collecting information or acting in the domain |

**Why this axis exists separately from A, and why it's low-weight by default:** compute subsidies and R&D money (axis A, −0.5) build capacity to *build* AI. This axis is only about capacity to *govern* it — a testbed, an incident database, an inspector general. Conflating the two would make "give the government AI money" look identical to "give the government AI oversight," which are politically and substantively different. It is weighted at 0.4 by default (vs. axis A's implicit weight of 1.0) because governance-capacity bills are usually a precondition for future stringency rather than stringency themselves — real but secondary to axis A and B.

---

### D. External / geopolitical (−3 … +5) · reported, excluded by default

Does the bill touch export controls, chip/compute access, or other geopolitical-competition levers?

| Score | Criteria |
|---|---|
| +5 | Hard controls with enforcement: location verification, KYC-on-compute, criminal penalties for diversion |
| +4 | New export restrictions on advanced chips or model weights |
| +3 | BIS enforcement resourcing, mandatory export reporting |
| +1 to +2 | Assessments, allied coordination |
| 0 | None |
| −1 to −3 | Loosens controls, carve-outs, licenses to restricted destinations |

**Why this axis is tracked but excluded from the composite by default (`w_D = 0.0`):** unlike axes A-C, this axis does not load cleanly onto the safety/acceleration spectrum. There is a coherent "race to stay ahead, so control chip diffusion" case for tightening controls, and an equally coherent "controls just accelerate foreign indigenization, so loosen them" case — both arguments are made by people who'd otherwise agree on frontier-safety policy. Folding this into the same composite as A-C would conflate two different debates. Record the score and rationale, but leave it out of `S` unless a reader explicitly opts in via the UI toggle.

---

### F. Capability buildout constraint (−5 … +5) · core

Domestic compute/energy chokepoints: data centers, permitting, interconnection, siting, water and power allocation, ratepayer protection. **Apply the guardrail above:** this axis is for provisions that constrain (or accelerate) AI capability by acting on a physical *input* to building/running compute — not on developer conduct. If a bill instead imposes a conduct standard on developers themselves, that belongs on axis A.

| Score | Criteria |
|---|---|
| +5 | National moratorium or hard cap on new AI compute capacity (e.g. a federal AI data-center moratorium) |
| +4 | Binding cap or quota in a major jurisdiction; federal veto over large-facility siting |
| +3 | Mandatory approval gates with discretionary denial; siting restrictions with real bite |
| +2 | Cost-shifting that materially raises the marginal cost of capacity — full cost allocation to developers, dedicated tariffs |
| +1 | Energy/water disclosure and reporting; local consent requirements |
| 0 | Neutral, or study only |
| −1 | Streamlined reporting; modest siting facilitation |
| −2 | Expedited permitting; interconnection queue priority |
| −3 | Categorical exclusions from environmental review; preemption of local siting authority |
| −4 | Direct subsidy or federal land/power allocation at scale |
| −5 | Federal buildout program with preemptive siting authority |

**Why this axis is now signed and part of the composite (unlike the old unsigned "buildout and energy" axis it replaces):** a data-center moratorium and a permitting-reform bill are not politically neutral relative to each other — one constrains AI capability by restricting a physical input, the other accelerates it by removing a physical bottleneck. That is directly analogous to what axes A-C already measure for developer conduct, just applied to the input side instead. Folding this into `S` at substantial weight (`w_F = 0.75` by default) means a bill that caps data-center buildout hard enough reads as safety/restriction-leaning even if it never touches a developer's conduct directly, and a bill that fast-tracks buildout reads as acceleration-leaning — which is the correct read of what these bills actually do.

---

### E. Consumer / near-term harm stringency (0 … 5) · impact only, unsigned

Deepfakes, non-consensual intimate imagery (NCII), companion-bot regulation, algorithmic discrimination, election integrity — harms that fall on distributors, deployers, and individuals rather than frontier developers.

| Score | Criteria |
|---|---|
| 5 | Broad private right of action across sectors |
| 3 | Criminal liability for specific AI-enabled conduct |
| 1 | End-user labeling requirement only |
| 0 | No consumer/near-term harm content |

Use intermediate values (e.g. 2, 4) when a bill's provisions sit between two rungs. **This axis never enters the safety composite** — it measures a different kind of stringency (harm to individuals/consumers) that isn't comparable to frontier-developer stringency on the same scale, and mixing them would make a state deepfake-labeling bill look like a frontier-safety bill. It is now the *only* impact-only, unsigned axis — its predecessor axis F has been promoted to a signed, composite-feeding axis (above).

---

## Composite 1: Safety score `S`

Every axis feeds the composite through its own weight — axis A gets full weight by default (making it "the base" in practice, not by special-casing it in the formula), B and C are partial adjustments, D defaults to zero, F is a substantial partial weight. **Do not average the axes** — averaging shrinks every bill toward zero and destroys the spread that makes the scatter plot informative.

```
S = clamp(w_A·A + w_B·B + w_C·C + w_D·D + w_F·F, −5, +5)

defaults:  w_A = 1.0   w_B = 0.6   w_C = 0.3   w_D = 0.0   w_F = 0.75
```

`S` is **not stored per bill** — only the raw axis values (A, B, C, D, F) are stored. `S` is computed at render time (server-side for the initial sort/display, and live in the browser via reader-facing sliders for every weight — `w_A`, `w_B`, `w_C`, `w_D`, `w_F`), so changing the weights never requires re-scoring a single bill. `w_B` remains the primary "SPR hook" (see the worked example below), but every weight is a slider — a reader can zero out axis A entirely, or raise `w_D` above zero to fold in export-control posture, and watch bills move in real time.

**Worked example (FRONTIER Act, illustrative):** with `A=+3` (pre-deployment gating via licensed independent verifiers), `B=−3` (three-year moratorium on state AI regulation), `C=+3` (funds a dedicated evaluation body), at default weights:

```
S = 3 + 0.6(−3) + 0.4(3) = 3 − 1.8 + 1.2 = +2.4
```

Note this does *not* land near zero — a bill can impose real stringency on developers while also being a major deregulatory event on preemption, and the composite reflects both rather than netting them to "moderate." The crossover point — the `w_B` at which this bill's `S` hits exactly 0 — is `w_B ≈ 1.4`, i.e. only if a reader believes the state-moratorium cost is more than 1.4× as significant as each point of direct federal stringency does this bill read as net-deregulatory. That crossover is exactly what the `w_B` slider in the UI lets a reader explore for themselves — don't tune the default weights to make any particular bill land at a "expected" number; let bills fall where the stated weights put them.

---

## Composite 2: Impact score

Four components, each normalized to 0–1, combined linearly. This measures magnitude of change, not direction — a maximally deregulatory bill and a maximally restrictive bill can have the same Impact score.

```
Impact = 10 × (0.35·R + 0.30·Depth + 0.20·E_f + 0.15·P)
```

(Range 0–10.)

### R — Reach (0–1)

Share of the target universe actually covered by the bill, **normalized within the bill's own tag class** (e.g. "frontier developer" bills vs. "consumer-facing" bills), not globally. Comparing headcount across classes directly would rank every consumer-facing state bill above every frontier bill just because more people are consumers than frontier labs — that's not a meaningful comparison of reach.

Jurisdiction weight table (kept here even though every currently-tracked bill is federal, so this needs no rework when state bills are added):

| Jurisdiction | Developer-facing bill | Consumer-facing bill |
|---|---|---|
| Federal | 1.0 | 1.0 |
| California | 0.85 | 0.12 |
| New York / Texas | 0.5 | 0.07 |
| Other large state | 0.3 | 0.03 |

**Why California gets two very different weights:** nearly all frontier labs are headquartered or incorporated such that a California developer-facing law reaches almost the entire frontier industry — that's a near-federal event. A California consumer-facing law (e.g. chatbot disclosure) only reaches Californians — about 12% of the country. Same state, two very different effective reach numbers depending on who the bill binds.

For a federal bill, `R` = 1.0 × the fraction of the target class actually covered once you account for thresholds, revenue floors, or sector carve-outs written into the bill (e.g. a bill that only covers developers spending >$100M on compute still gets `R` close to 1.0 if that threshold captures essentially the entire frontier industry, as intended).

### Depth (0–1)

```
Depth = max(|A|, |B|, |C|, |F|, E) / 5
```

This is `impact_components.D` in the stored record — **not the same thing as `axes.D`** (external/geopolitical). The shared letter is coincidental notation carried over from the original rubric; when writing rationale, always spell this one out as "Depth" to avoid confusion. It captures how far any single axis pushes from neutral, on a 0–1 scale comparable to the other impact components. `F` was added to this formula when axis F was promoted to a signed, composite-feeding axis — `D` (external/geopolitical) remains excluded from Depth because it, like the safety composite, is excluded from the default-weighted set by design; only axes that get a nonzero default weight in `S` (A implicitly, B, C, F) plus E (impact-only but same 0–5 magnitude scale) feed Depth.

### E_f — Enforceability (0–1)

| Score | Criteria |
|---|---|
| 1.0 | Private right of action |
| 0.8 | Agency rulemaking + civil penalties |
| 0.6 | AG enforcement only |
| 0.4 | Obligation with no stated penalty |
| 0.2 | Voluntary |
| 0 | Study only |

### P — Precedent (0–1)

| Score | Criteria |
|---|---|
| 1.0 | Creates a permanent institution or a preemption ceiling |
| 0.8 | First-in-nation framework likely to be copied |
| 0.6 | Joins an established multi-state template |
| 0.4 | Sector-specific and self-contained |
| 0.2 | Sunsets |

**Note on naming collision:** this `P` (Precedent, an impact component, 0–1 scale) is unrelated to `p_enact` (probability of enactment, see below). Both happen to be called "P"/"p" in the source material — keep them straight in rationale text.

---

## Likelihood

Two probabilities, not one 1–5 "vibes" number:

- `p_committee` (0–1): probability the bill advances out of committee.
- `p_enact` (0–1): probability the bill is ultimately enacted into law.
- `basis` (string): a short label for the methodology used (e.g. `"base_rate_adjusted"`, `"govtrack_corroborated"`).

Where available, anchor these to GovTrack.us's own modeled "prognosis" for the specific bill (many bill pages publish one) and note that anchor explicitly in the rationale — even if your own estimate differs from GovTrack's, say so and explain why. Where no external model is available, use historical base rates for bills at a comparable stage (e.g. share of House bills that clear committee at all in a given Congress) adjusted for the specific bill's cosponsor count, bipartisan pairing, committee chair alignment, and any recent news-cycle attention.

## Sort key: Expected Impact

```
ExpectedImpact = Impact × p_enact
```

This is the tracker's default sort — it surfaces bills that are both consequential *and* likely to actually happen, rather than either extreme alone (a huge bill with near-zero odds, or a trivial bill that's a lock to pass).

## Scatter plot design

- x-axis: `S` (−5 to +5, "Deregulation ⟵ ⟶ Safety/Restriction")
- y-axis: `p_enact` (0 to 1, "Probability of enactment")
- point size: `Impact` (0–10)
- point color: diverges through white at `S = 0` (warm/orange toward −5, cool/blue toward +5)

Under this design, a bill like the FRONTIER Act — large, high-probability, and near-neutral on `S` once state preemption is weighed against federal stringency — reads visually as "large, high-probability, ambiguous," which is an accurate description rather than an artifact of averaging.

**Only bills with `text_source: full_text` are plotted.** A bill scored from a summary can be plotted anywhere on the chart with a confident-looking dot, but the reader has no way to tell that its position rests on incomplete information — so it doesn't get a dot until someone has actually confirmed it against the bill's real text. The bill still appears in the list below the chart either way.

## Record schema

Stored per bill, replacing the old `scores:`/`rationale:` block:

```yaml
scoring:
  axes:
    A: 3.0
    B: -3.0
    C: 3.0
    D: 0.0
    F: 0.0
  unsigned:
    E_consumer: 0.0
  impact_components:
    R: 0.95
    D: 0.60        # Depth — unrelated to axes.D
    E_f: 0.80
    P: 1.00
  likelihood:
    p_committee: 0.55
    p_enact: 0.18
    basis: "base_rate_adjusted"
  rationale:
    A: "..."
    B: "..."
    C: "..."
    D: "..."
    F: "..."
    E_consumer: "..."
    R: "..."
    Depth: "..."
    E_f: "..."
    P: "..."
    likelihood: "..."
  confidence: medium   # high | medium | low
  text_source: summary   # full_text | summary | press_release | unknown
  scored_at: "2026-08-01"
```

Every scored number requires its own rationale string. `S`, `Impact`, and `ExpectedImpact` are never stored — they are always computed from the raw fields above, so that changing `w_B`/`w_C`/`w_D`/`w_F` (e.g. via the reader-facing weight slider) never requires touching this file.

### `text_source` — what was actually read, and why it gates the public scatter

`text_source` records what the scoring pass actually consulted, honestly:

- `full_text` — the bill's actual introduced text (fetched from congress.gov or an equivalent official source) was read for this scoring pass.
- `summary` — scoring relied on the tracker's own curated summary/body text (or a sponsor press release quoted in it), not the bill's official text.
- `press_release` — scoring relied primarily on a sponsor or news press release.
- `unknown` — provenance wasn't tracked (legacy data only; never write this for new scoring).

**The rule: anything not `full_text` gets `confidence: low`, and is excluded from the public scatter chart (it still appears in the bill list).** This exists because of a real failure mode: a bill's curated summary can simply omit a provision — most commonly a preemption clause — that's present in the actual introduced text, and an agent scoring only from the summary has no way to know it's missing something. Congress.gov publishes the full introduced text for every bill; there is no excuse for guessing when it's one fetch away. This rule is enforced in code (`app/routes.py`), not just convention — setting `confidence: high` with `text_source: summary` will still be treated as low-confidence and dropped from the scatter.

**When to fetch full text:** always for axis B (preemption) when a savings clause or preemption language would plausibly be dispositive and isn't clearly resolved by the bill's existing summary — the summary was very likely written by an earlier pass that itself worked from a press release or abstract, not the statute. Fetch it proactively for any "major" bill (A ≥ +2, advanced past introduction, or otherwise high-priority) even if you don't yet suspect an error — the point of this rule is to stop discovering these gaps one at a time after the fact.

## Instructions for research agents

1. Read the bill's existing markdown body and front matter first — it already contains real, previously-researched prose about what the bill does. This tells you what to look for, but it is a summary, not the statute — it can and does omit provisions, most commonly preemption/savings-clause language, that only show up in the actual bill text.
2. Score every signed axis (A, B, C, D, F), the one unsigned axis (E), all four impact components (R, Depth, E_f, P), and both likelihood probabilities (p_committee, p_enact). Before scoring A, B, or C, apply the AI-governance-scoping guardrail (above): confirm the mechanism you're about to score actually observes, constrains, or governs AI, not just a domain-general mechanism that happens to appear in an AI-tagged bill — cap at ±1 if it's the latter. Apply the conduct-vs-input-chokepoint guardrail before scoring A and F — if you find yourself putting a compute-hardware, energy, siting, or water provision on A, it belongs on F (or D if it's an export/foreign-access control) instead. Apply the implicit-preemption floor (above) whenever A ≥ +2.
3. **Fetch the bill's actual introduced text from congress.gov whenever axis B is uncertain, and always for a "major" bill** (A ≥ +2, past introduction, or otherwise high-priority) — do not infer "no preemption language" from its absence in the tracker's own summary; confirm it against the real text. Set `text_source: full_text` once you've done this. If you score B from the existing summary/body text alone without confirming against the official text, set `text_source: summary` and `confidence: low` — do not mark a summary-sourced score as high or medium confidence.
4. Do supplemental live web research to firm up `likelihood` — check the bill's current status on congress.gov and, if available, GovTrack.us's prognosis page — since that's the most time-sensitive, fact-dependent part of the score. Spend more research effort here for bills that are further along (further from `introduced`, closer to `signed`).
5. Write a rationale for every single scored field — cite the specific provision or fact that justifies the number. When a bill sits between two rungs on a ladder, say so and explain which way you rounded. When the implicit-preemption floor applies, say so explicitly in the B rationale.
6. Set `confidence` to reflect how well-corroborated the estimate is, but note the hard override in the `text_source` section above: `text_source` other than `full_text` always forces `confidence: low`, regardless of how well-corroborated anything else about the score is.
7. Set `scored_at` to the date you performed the scoring.
8. Edit the bill's `.md` file to replace the entire old `scores:` and `rationale:` top-level keys with the new `scoring:` block above (including `text_source`). Remove the old keys completely — do not leave them alongside the new block. Do not modify any other field or the markdown body.
