# Understanding LGIRS-5.1: Correct and useful intended outcomes

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-5-1) · [Understanding index](README.md)

## Candidate criterion

Evaluation MUST establish whether the person's intended outcome is achieved correctly and usefully within the declared scope, distinguishing generated output, administrative completion and actual benefit.

**Local priority:** A (provisional; not WCAG conformance).

## Intent and potential benefit

A successful tool call or fluent answer can still leave the person's goal unmet.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

Complete delegated tasks including dependencies and final confirmation; the goal and quality criteria must be agreed for the context.

## Implementation approach

Define goal-specific correctness and usefulness measures before the trial; examine adverse effects and relevant independent checks.

See [technique T21](../implementation/techniques.md#t21). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Complete a travel booking with a lower price but an inaccessible transfer that violates the stated requirement.
4. Observe: The assessment records the goal as unmet even though payment and API calls succeeded; the access constraint remains visible.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

The dashboard declares success because a booking ID exists, ignoring the person's access requirement.

## Worked application

- [EX06: A travel agent optimises price but misses the actual goal](../examples/ex06.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [DFW-POURS: Double-FW/POUR-for-Branding-Systems-and-CX / POURS_Access_Experience_and_Brand_Promise.md](https://github.com/Double-FW/POUR-for-Branding-Systems-and-CX/blob/0410091af93053783ff8594f4404be1bf721f407/POURS_Access_Experience_and_Brand_Promise.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
- [DFW-QA: Double-FW/QA_Accessibility_Testing / Testing_Approach.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/38602fc4ab48302649673d0524afc48d0a21a2a1/Testing_Approach.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
