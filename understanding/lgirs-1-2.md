# Understanding LGIRS-1.2: Current scope, capabilities and context

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-1-2) · [Understanding index](README.md)

## Candidate criterion

Before delegation and when a material boundary changes, the service MUST make the relevant accessible summary of available capabilities, effective permissions, significant context limits and delegation duration available to the authorised person.

**Local priority:** A (provisional; not WCAG conformance).

## Intent and potential benefit

A person cannot make an informed delegation from a fictional picture of what the agent can access.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

Delegation and material changes in tools, data access, accounts or autonomy; not unrestricted disclosure of other users' data.

## Implementation approach

Derive the summary from effective permissions and active integrations, not a static marketing capability list; use progressive detail for scope and exclusions.

See [technique T02](../implementation/techniques.md#t02). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Revoke calendar write access during a task and introduce a second account whose records are inaccessible.
4. Observe: The scope display and execution gate reflect the revocation; unavailable account contents are not implied to be known.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

A permission badge still says full access after revocation and the agent invents unseen appointments.

## Worked application

- [EX02: A procurement agent reads a hostile supplier document](../examples/ex02.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [DFW-SYN: Double-FW/Synchronistic-Design-Formal-Operating-Model / README.md](https://github.com/Double-FW/Synchronistic-Design-Formal-Operating-Model/blob/8d3caf35eedc71c423f32c77947e3eb862066f61/README.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
- [MCP-TOOLS: MCP tools, pinned 2025-06-18 edition](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) — Tool description/invocation reference; not a guarantee of safe behaviour or a universal UI.
