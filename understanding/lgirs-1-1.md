# Understanding LGIRS-1.1: Agent involvement and identity

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-1-1) · [Understanding index](README.md)

## Candidate criterion

The service MUST identify material agent involvement, the service responsible for it and whether a presented item is a proposal, generated output or confirmed system result through the supported accessible presentation.

**Local priority:** A (provisional; not WCAG conformance).

## Intent and potential benefit

People need to know who or what is acting before deciding how to rely on it.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

Human-facing agent outputs and actions; a machine-only component must supply the information needed by its consuming interface.

## Implementation approach

Use plain labels with programmatic equivalents; identify the accountable service; separate generated drafts from receipts based on actual tool responses.

See [technique T01](../implementation/techniques.md#t01). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Show a generated booking suggestion next to a confirmed reservation using keyboard and a screen reader, then remove visual colour cues.
4. Observe: The two states remain distinguishable and the confirmed item refers to actual execution evidence; a draft cannot appear as a receipt.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

An AI-written success message is styled as a completed transaction despite no successful tool response.

## Worked application

- [EX01: A booking agent times out after commitment](../examples/ex01.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [WCAG22: Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/) — External normative standard; LGIR+S does not amend its requirements.
- [DFW-COG: Double-FW/Cognitive-UX-Design / Cognitive Design Principles.md](https://github.com/Double-FW/Cognitive-UX-Design/blob/34d2e3cd2eb4a92409b198338f155fa42e0ba9ed/Cognitive%20Design%20Principles.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
