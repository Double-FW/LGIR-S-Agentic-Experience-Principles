# Evaluation, evidence and claims

Informative assessment method · No validated LGIR+S conformance scheme is defined

## Establish the assessment boundary

Record the purpose and decision; service/journey; affected people and roles; channels and supported access modes; model/prompt/retrieval/tool versions; operating environment; actual authorisation; data classes; relevant external requirements; and period. State exclusions and their consequences. A result for one assistant is not an organisation-wide maturity result.

Select relevant candidate criteria with reasons. Give each a documented evaluation route. Use automation for reliable observable properties, manual/AT inspection for interaction, appropriate specialists for security/data/sector questions, and participation for actual experience. A source prompt, expected result or synthetic fixture is not an executed test.

## Use distinct result states

| State | Meaning |
| --- | --- |
| Not evaluated | The needed evaluation has not been performed |
| Met in evaluated scope | Evidence supports the selected criterion within its declared scope and limits |
| Not met | Evidence shows an unmet criterion in the evaluated scope |
| Inconclusive | Evaluation occurred but evidence is insufficient or conflicting |
| Not applicable | A reasoned applicability decision is recorded, with its scope and reviewer |

All 25 criterion records in this repository initially have product_evaluation_status: not_evaluated. They describe the proposal, not a product assessment. Store actual sensitive evidence in controlled organisational systems, with appropriate references in a public report.

## Evaluate the complete task and its boundaries

Begin with the intended goal and constraints. Examine start, delegation, ordinary work, material decisions, external effects, handovers, completion and remedy. Include interrupted and partial paths. Relevant stress cases include stale or conflicting evidence, hostile retrieval, permission revocation, unfamiliar benign inputs, timeout after commit, late replies, duplicates, concurrent edits, model change and unavailable oversight.

For each probe, record setup, actual inputs, expected observations, actual events, human observations, environment and limitations. Predefine relevant response tolerances and safe test conditions. Use a sandbox or simulation for consequential failures; do not cause real harm to demonstrate an incident. If a simulated path has not been checked in the real integration, say so.

Repeat trials where generation varies and retain distributions and negative cases. A single successful response is not a reliability estimate. Do not invent a universal sample size or confidence threshold. Set the study and statistical method for the decision, including uncertainty and coverage.

## Preserve different evidence roles

Keep interface access, source integrity, tool/action correctness, authority, fairness/appropriate treatment and human experience visible as separate findings. One observation can support several scoped questions, but it does not make their meanings equivalent. High satisfaction must not erase an access barrier or an unauthorised effect. A technically successful action must not erase unmet intent or dignity.

Do not produce an overall percentage accessible, an LGIR Level AA certificate or a maturity score from the provisional tiers. An adopting organisation can define a transparent pilot profile, but must name it as its local decision and disclose deviations. Unmet actual legal or contractual duties require their own response; this draft cannot waive them.

## Report and improve

Use the [assessment record](../templates/assessment-record.md). Report scope, methods, evidence dates, results, serious failures, untested areas, uncertainty, owners and review triggers. Distinguish a proposed mitigation from an implemented and retested correction. Record the actual person authorised to release or accept residual consequences; a generated approval line has no such authority.

An accurate statement might be: “We evaluated criteria LGIRS-1.3 and LGIRS-4.4 in the defined booking sandbox on the stated versions. The tested late-response cases reconciled without duplicate booking; live provider recovery and additional AT combinations remain untested.” It should not become “LGIR+S compliant and safe across all models.”

Local repository checks are described in [validation](../VALIDATION.md). They do not perform this product assessment or independently validate the framework.
