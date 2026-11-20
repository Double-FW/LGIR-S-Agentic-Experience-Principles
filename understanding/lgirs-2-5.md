# Understanding LGIRS-2.5: Continuity, handover and resumption

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-2-5) · [Understanding index](README.md)

## Candidate criterion

After interruption, assistance or transfer, the service MUST preserve appropriate valid work and make current intent, completed effects, pending decisions and remaining limits available to the authorised successor.

**Local priority:** AA (provisional; not WCAG conformance).

## Intent and potential benefit

An interruption should not force people to reconstruct an invisible workflow from memory.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

Session expiry, human takeover, channel changes and operator handovers; persistence must respect retention and role permissions.

## Implementation approach

Provide a concise resumable task record and explicit handover acceptance; recheck authority before resuming side effects.

See [technique T10](../implementation/techniques.md#t10). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Expire a session after a partial update and resume through an authorised support channel with different permissions.
4. Observe: The successor can identify what actually happened and what remains, while restricted context is withheld and prior effects are not repeated.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

A resumed task repeats the payment because the only saved state was the conversational draft.

## Worked application

- [EX04: A long-running assistant works alongside a screen-reader user](../examples/ex04.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [DFW-COG: Double-FW/Cognitive-UX-Design / Cognitive Design Principles.md](https://github.com/Double-FW/Cognitive-UX-Design/blob/34d2e3cd2eb4a92409b198338f155fa42e0ba9ed/Cognitive%20Design%20Principles.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
- [DFW-ETH: Double-FW/Data_Ethics_and_Disability / README.md](https://github.com/Double-FW/Data_Ethics_and_Disability/blob/77163fa48b6df5839e1294ec02797abf67c73980/README.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
