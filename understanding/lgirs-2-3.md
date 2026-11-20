# Understanding LGIRS-2.3: Commitment boundaries and proportionate approval

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-2-3) · [Understanding index](README.md)

## Candidate criterion

Before an action exceeds existing authorisation or crosses a declared high-impact or irreversible boundary, the service MUST provide an accessible preview of material effects and obtain the required actual decision.

**Local priority:** A (provisional; not WCAG conformance).

## Intent and potential benefit

People need control at consequential boundaries without approving every harmless step repeatedly.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

Actions requiring additional authority by the declared local policy, contract or applicable duty; existing clear authority can cover lower-impact work.

## Implementation approach

Bind approval to the action, recipient, amount, data and version; invalidate it after a material change; keep preparatory work separate from commitment.

See [technique T08](../implementation/techniques.md#t08). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Approve one recipient and amount, then change the recipient or amount before execution while also running an independent read-only task.
4. Observe: The changed action does not inherit the old approval; the independent authorised task is not needlessly blocked.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

An approval for a draft email is reused to send a revised message to additional recipients.

## Worked application

- [EX05: An email agent reaches an irreversible send boundary](../examples/ex05.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [DFW-SYN: Double-FW/Synchronistic-Design-Formal-Operating-Model / README.md](https://github.com/Double-FW/Synchronistic-Design-Formal-Operating-Model/blob/8d3caf35eedc71c423f32c77947e3eb862066f61/README.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
- [DFW-QA: Double-FW/QA_Accessibility_Testing / Testing_Approach.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/38602fc4ab48302649673d0524afc48d0a21a2a1/Testing_Approach.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
