# Understanding LGIRS-4.5: Supported portability and change assurance

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-4-5) · [Understanding index](README.md)

## Candidate criterion

Changes to model, provider, prompt, retrieval, tool contract or oversight design MUST be evaluated against the declared behavioural and access expectations before affected release, with versioned limitations and rollback or alternative plans.

**Local priority:** AA (provisional; not WCAG conformance).

## Intent and potential benefit

Decoupling reduces some dependencies but does not guarantee stable behaviour after a change.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

Material changes to the supported operating envelope; no claim covers arbitrary future models.

## Implementation approach

Maintain versioned task/failure/accessibility scenarios, compare action traces and human burden, and approve the actual supported combination.

See [technique T20](../implementation/techniques.md#t20). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Replace the model with one that emits valid schemas but interprets a permission boundary differently and changes notification frequency.
4. Observe: The regression and oversight checks identify the changed behaviour before affected release; syntax success alone does not qualify the change.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

A provider switch is approved solely because API requests parse and aggregate accuracy remains similar.

## Worked application

- [EX08: A provider change preserves syntax but changes behaviour](../examples/ex08.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [DFW-QA: Double-FW/QA_Accessibility_Testing / Testing_Approach.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/38602fc4ab48302649673d0524afc48d0a21a2a1/Testing_Approach.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
- [NIST-RMF: NIST AI Risk Management Framework resource](https://airc.nist.gov/airmf-resources/airmf/) — Voluntary risk-management reference; this repository is not a NIST certification or complete crosswalk.
