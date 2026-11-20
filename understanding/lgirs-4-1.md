# Understanding LGIRS-4.1: Epistemic traceability and context integrity

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-4-1) · [Understanding index](README.md)

## Candidate criterion

Material training-data collection, retrieval and runtime-context dependencies MUST have provenance at the granularity actually available, relevant dates, transformations and declared evidence gaps; these qualifications MUST survive retrieval and export.

**Local priority:** A (provisional; not WCAG conformance).

## Intent and potential benefit

Reliable reasoning depends on the context that accompanies information, not merely the presence of text.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

Data pipelines and material knowledge dependencies; incomplete historical training lineage must be disclosed rather than invented.

## Implementation approach

Use versioned source records, claim-to-source relationships and trust classifications; distinguish publication, access, review and expiry dates.

See [technique T16](../implementation/techniques.md#t16). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Retrieve a section whose source is an unverified historical draft, then export and re-import it into a new context.
4. Observe: Its identity, date and unverified status remain attached; it is not promoted to current authoritative guidance.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

A fresh export date replaces the original legal review date and the model treats the old draft as current law.

## Worked application

- [EX03: A research assistant creates a fast but expensive-to-check report](../examples/ex03.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [DFW-QA: Double-FW/QA_Accessibility_Testing / Testing_Approach.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/38602fc4ab48302649673d0524afc48d0a21a2a1/Testing_Approach.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
- [DFW-ETH: Double-FW/Data_Ethics_and_Disability / README.md](https://github.com/Double-FW/Data_Ethics_and_Disability/blob/77163fa48b6df5839e1294ec02797abf67c73980/README.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
