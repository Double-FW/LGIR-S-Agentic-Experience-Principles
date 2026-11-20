# Understanding LGIRS-4.4: Safe execution and partial-failure recovery

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-4-4) · [Understanding index](README.md)

## Candidate criterion

The service MUST preserve truthful state, constrain further effects and use evaluated recovery or escalation when execution fails or its outcome is uncertain; retries MUST account for duplicate and partial effects.

**Local priority:** A (provisional; not WCAG conformance).

## Intent and potential benefit

Distributed actions can commit even when the client sees a timeout.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

External writes, queued work, partial completion and concurrency; deterministic fallback must be evaluated for its scope.

## Implementation approach

Use durable operation identifiers, supported idempotency, commit checks and reconciliation; use transaction rollback only within actual transaction boundaries.

See [technique T19](../implementation/techniques.md#t19). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Commit the first half of a multi-system update, lose the response and replay a late result while another operator edits the second system.
4. Observe: The service reconciles effects without duplicate action or overwriting the other operator; unresolved state remains explicit.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

A timeout triggers blind retry, creating duplicate bookings and a falsely successful recovery message.

## Worked application

- [EX01: A booking agent times out after commitment](../examples/ex01.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [MCP-CANCEL: MCP cancellation, pinned 2025-06-18 edition](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/cancellation) — Pinned protocol example; cancellation is not guaranteed rollback; not asserted as latest edition.
- [DFW-QA: Double-FW/QA_Accessibility_Testing / Testing_Approach.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/38602fc4ab48302649673d0524afc48d0a21a2a1/Testing_Approach.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
