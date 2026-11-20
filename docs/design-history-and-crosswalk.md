# Design history and editorial crosswalk

Gareth Ford Williams supplied the Agentic Robustness definition and proposed Legible, Governable, Interpretable and Robust as an agentic counterpart to POUR. The exact robustness definition is retained in the specification. The owner subsequently requested the dedicated LGIR+S contents, including the Satisfactory experience principle, examples and implementation guidance.

This edition develops those ideas into 25 candidate criteria. The original eight detailed robustness provisions and twelve LGIR provisions were overlapping views. They are not twenty independent obligations or unchanged copies of this new criterion set. The relationships below are editorial traceability suggestions, not equivalence or verified coverage claims.

## Original detailed robustness provisions

| Supplied provision | Candidate criteria developing the idea |
| --- | --- |
| Provenance & Grounding | LGIRS-1.4, 3.2–3.3, 4.1 |
| Distribution & Edge-Case Resilience | LGIRS-3.3, 4.2 |
| Capability, Intent, State | LGIRS-1.2–1.3, 4.3 |
| Deterministic Guardrails & Graceful Degradation | LGIRS-2.1–2.2, 2.4, 4.4 |
| Cross-Model Portability | LGIRS-4.5 |
| Ambient State & Reasoning Transparency | LGIRS-1.3–1.5, 3.2 |
| Reversible Agency & Intervention Hooks | LGIRS-2.2–2.5 |
| Adaptive Calibration | LGIRS-2.3, 3.3, 5.3 |

## Original LGIR provisions

| Supplied provision | Candidate criteria developing the idea |
| --- | --- |
| Agentic Attribution & Provenance | LGIRS-1.1, 1.4 |
| Scope & Capability Signaling | LGIRS-1.2, 2.1 |
| Ambient Status & Multi-Modal Feedback | LGIRS-1.3, 1.5 |
| Interruptibility & Kill-Switches | LGIRS-2.2 |
| Granular Permission & Blast-Radius Control | LGIRS-2.1, 2.3 |
| Reversible Agency & Checkpoints | LGIRS-2.4–2.5 |
| Intent Preview & Plan Inspection | LGIRS-2.3, 3.1 |
| Calibrated Confidence & Uncertainty Signaling | LGIRS-3.3 |
| Predictable Policy & Behavioral Consistency | LGIRS-3.4 |
| Epistemic & Data Integrity | LGIRS-4.1–4.2 |
| Execution & Architectural Compatibility | LGIRS-4.3–4.5 |
| Human-Agent Co-Agency Resilience | LGIRS-1.5, 2.2, 2.5, 3.5, 4.4 |

## Satisfactory and editorial refinements

The Satisfactory definition was proposed in the conversation and included following the owner's request to develop LGIR+S. It addresses correct/useful outcomes, total human burden, choice, dignity/comparable opportunity and experience evidence in LGIRS-5.1–5.5. It does not change the four official WCAG principles.

Implementation wording qualifies promises that cannot be universal: metadata can be incomplete; confidence needs a defined meaning; cancelling a request is not proof of stopping an effect; rollback is bounded; common schemas do not guarantee semantic portability; useful transparency does not require hidden internal reasoning or disclosure of private data. Tier assignments remain provisional.

WCAG 4.1.1 appears only as historical background: it was removed from WCAG 2.2. The cited 4.1.2/4.1.3 analogies do not impose tool contracts, transaction recovery or reasoning logs as WCAG requirements.

## Identifiers and changes

LGIRS-1.1 through LGIRS-5.5 belong to this repository's candidate criterion namespace. They do not replace identifiers in WCAG, earlier local proposal catalogues, Cognitive UX or QA sources. Preserve source IDs in their own context. Any later split, retirement or meaning change needs a versioned migration note; do not reuse a retired ID for a different requirement.
