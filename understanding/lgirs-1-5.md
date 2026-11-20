# Understanding LGIRS-1.5: Non-disruptive accessible feedback

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-1-5) · [Understanding index](README.md)

## Candidate criterion

Status and intervention information MUST be available through the supported accessible routes with meaningful priority, persistence and user control, without requiring every channel to operate simultaneously.

**Local priority:** AA (provisional; not WCAG conformance).

## Intent and potential benefit

More notifications can reduce awareness by obscuring the important event.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

Human-facing status, alerts and consequential messages across the declared platforms and assistive-technology combinations.

## Implementation approach

Use appropriate semantic status patterns, persistent summaries and preference-aware notification policies; reserve interruption for the justified priority.

See [technique T05](../implementation/techniques.md#t05). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Run a long task with frequent internal events while a screen-reader user edits unrelated text, then introduce an actionable failure.
4. Observe: Routine events do not steal focus or create an announcement backlog; the consequential failure is perceivable, retrievable and actionable.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

Every token update is announced assertively and the person misses the only message requiring a decision.

## Worked application

- [EX04: A long-running assistant works alongside a screen-reader user](../examples/ex04.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [WCAG-STATUS: Understanding Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html) — Scoped informative explanation; not a specification for full agent observability.
- [DFW-COG: Double-FW/Cognitive-UX-Design / Cognitive Design Principles.md](https://github.com/Double-FW/Cognitive-UX-Design/blob/34d2e3cd2eb4a92409b198338f155fa42e0ba9ed/Cognitive%20Design%20Principles.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
