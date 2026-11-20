# Understanding LGIRS-1.3: Meaningful task and execution status

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-1-3) · [Understanding index](README.md)

## Candidate criterion

The service MUST expose meaningful current task states, pending dependencies and actual completion or uncertainty without presenting predicted progress as an observed result.

**Local priority:** A (provisional; not WCAG conformance).

## Intent and potential benefit

People need to decide whether to wait, intervene or continue other work.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

Long-running tasks and operations whose remote outcome may be delayed or unknown.

## Implementation approach

Map real event records to user language; distinguish waiting for a person from waiting for a tool; provide a retrievable history with version and time.

See [technique T03](../implementation/techniques.md#t03). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Delay a tool acknowledgement, then deliver a completion event after a cancellation request.
4. Observe: The interface first reports the unknown or pending outcome and later reconciles it; it does not announce stopped or completed merely from a request.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

A timeout becomes Failed, safe to retry even though the remote operation may have committed.

## Worked application

- [EX01: A booking agent times out after commitment](../examples/ex01.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [WCAG-STATUS: Understanding Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) — Scoped informative explanation; not a specification for full agent observability.
- [MCP-CANCEL: MCP cancellation, pinned 2025-06-18 edition](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/cancellation) — Pinned protocol example; cancellation is not guaranteed rollback; not asserted as latest edition.
