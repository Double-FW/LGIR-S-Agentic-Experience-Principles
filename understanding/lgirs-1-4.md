# Understanding LGIRS-1.4: Output provenance and evidence access

Informative · Editor’s Draft 0.1.0 · No product result established

[Specification](../SPECIFICATION.md#lgirs-1-4) · [Understanding index](README.md)

## Candidate criterion

Material factual or action claims MUST have accessible provenance or an explicit evidence gap, with access to supporting detail appropriate to the person's role and the confidentiality of the source.

**Local priority:** AA (provisional; not WCAG conformance).

## Intent and potential benefit

Useful source context enables checking without requiring disclosure of protected material.

This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.

## Applicability

Factual summaries, advice, transformed content and action claims; creative content must be labelled appropriately rather than supplied with invented citations.

## Implementation approach

Attach source identity, revision and relevant dates to claims; offer protected provenance summaries when direct links would expose private data.

See [technique T04](../implementation/techniques.md#t04). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.

## Evaluation probe — not yet run

1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.
2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.
3. Ask for a cited summary containing one expired public source and one restricted internal source.
4. Observe: The source date and restriction remain visible, unauthorised contents remain protected and the unsupported claim is labelled or withheld.
5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.

## Failure example

The system cites a plausible URL that was never retrieved or publishes a private participant record as evidence.

## Worked application

- [EX03: A research assistant creates a fast but expensive-to-check report](../examples/ex03.md)

## Evidence and limits

Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.

## Supporting references

- [DFW-ETH: Double-FW/Data_Ethics_and_Disability / README.md](https://github.com/Double-FW/Data_Ethics_and_Disability/blob/77163fa48b6df5839e1294ec02797abf67c73980/README.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
- [DFW-POURS: Double-FW/POUR-for-Branding-Systems-and-CX / POURS_Access_Experience_and_Brand_Promise.md](https://github.com/Double-FW/POUR-for-Branding-Systems-and-CX/blob/0410091af93053783ff8594f4404be1bf721f407/POURS_Access_Experience_and_Brand_Promise.md) — Public practitioner guidance; preserve original draft/adoption status. Not independently validated or a substitute for applicable primary requirements.
