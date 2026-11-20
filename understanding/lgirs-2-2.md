# Understanding LGIRS-2.2: Effective intervention and truthful stopping

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-2-2) · [Understanding index](README.md)

## Candidate criterion

The authorised person MUST have an accessible intervention route with declared response limits; the system MUST distinguish an intervention request from confirmed cessation and reconcile work already in flight.

**Local priority:** A (provisional; not WCAG conformance).

## Intent and potential benefit

A visible stop control is insufficient when execution continues invisibly.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

Active loops, queued work, sub-agents and outstanding remote operations; the safe intervention method depends on the service.

## Implementation approach

Propagate stop intent, prevent new side effects, handle late events and report actual status; identify work that cannot be cancelled.

See [technique T07](../implementation/techniques.md#t07). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Request cancellation after a remote action is accepted but before the client receives its response.
4. Observe: No new actions are scheduled; already committed effects are disclosed and reconciliation remains possible without claiming universal undo.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

The UI says Stopped while a queued sub-agent continues sending messages.

## Worked application

- [EX01: A booking agent times out after commitment](../examples/ex01.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [MCP-CANCEL: MCP cancellation, pinned 2025-06-18 edition](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/cancellation) — Pinned protocol example; cancellation is not guaranteed rollback; not asserted as latest edition.
- [DFW-QA: Double-FW/QA_Accessibility_Testing / Testing_Approach.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/38602fc4ab48302649673d0524afc48d0a21a2a1/Testing_Approach.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
