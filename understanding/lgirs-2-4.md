# Understanding LGIRS-2.4: Reversal, compensation and consequence disclosure

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-2-4) · [Understanding index](README.md)

## Candidate criterion

For state-changing actions the service MUST identify what is reversible, compensatable or irreversible, provide the supported recovery route and disclose residual consequences and limits before commitment where relevant.

**Local priority:** AA (provisional; not WCAG conformance).

## Intent and potential benefit

An honest recovery model is more useful than an undo control that cannot deliver its promise.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

Writes and external effects, including multi-system operations; a documented absence of reversal does not remove the need for suitable pre-commit controls.

## Implementation approach

Use version-aware checkpoints, transaction boundaries and authorised compensating actions; prevent recovery from overwriting another person's later valid work.

See [technique T09](../implementation/techniques.md#t09). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Change a record, let another person update it, then request undo; also attempt to undo an already delivered message.
4. Observe: The later update is protected and the message is described as not retractable where applicable; compensation is not misrepresented as erasure.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

Undo restores an old database snapshot over unrelated recent work or claims a delivered email was unsent.

## Worked application

- [EX05: An email agent reaches an irreversible send boundary](../examples/ex05.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [DFW-QA: Double-FW/QA_Accessibility_Testing / Testing_Approach.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/38602fc4ab48302649673d0524afc48d0a21a2a1/Testing_Approach.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
- [MCP-CANCEL: MCP cancellation, pinned 2025-06-18 edition](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/cancellation) — Pinned protocol example; cancellation is not guaranteed rollback; not asserted as latest edition.
