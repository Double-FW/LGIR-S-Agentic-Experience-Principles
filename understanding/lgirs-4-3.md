# Understanding LGIRS-4.3: Capability, Intent, State contracts

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-4-3) · [Understanding index](README.md)

## Candidate criterion

Tool and sub-agent integrations MUST provide versioned machine-readable capability contracts, intended effects and observed execution states, with validation and authorisation at the consuming boundary.

**Local priority:** A (provisional; not WCAG conformance).

## Intent and potential benefit

An agent needs a stable contract, while a schema alone cannot establish semantics or permission.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

Tool/API/sub-agent boundaries; open descriptions or documented adapters can supply the contract without requiring every vendor to implement one universal protocol.

## Implementation approach

Separate the operation schema, authorised task intent and execution record; validate requests and results; define adapter and version compatibility.

See [technique T18](../implementation/techniques.md#t18). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Return a schema-valid response that lacks the required business confirmation, then change the tool schema version.
4. Observe: The consuming system detects the missing confirmation and incompatible version rather than inventing success or treating the schema as authority.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

A JSON response containing accepted is rendered as funds transferred even though settlement is unconfirmed.

## Worked application

- [EX01: A booking agent times out after commitment](../examples/ex01.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [MCP-TOOLS: MCP tools, pinned 2025-06-18 edition](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) — Tool description/invocation reference; not a guarantee of safe behaviour or a universal UI.
- [OPENAPI: OpenAPI Specification 3.1.1](https://spec.openapis.org/oas/v3.1.1.html) — Pinned API description example, not latest-version advice or behavioural assurance.
