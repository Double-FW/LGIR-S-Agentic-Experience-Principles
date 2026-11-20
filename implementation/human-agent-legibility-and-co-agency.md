# Human-Agent Legibility & Co-Agency

Informative implementation guidance · principles 1–3, with LGIRS-4.4 and principle 5

Co-agency means a workable division of activity and control between people and agents. Its quality depends on what people can know, decide and do in time, not on the presence of a nominal Human in the loop label.

## Identify the people and their actual rights

The person requesting work, the operator, the accountable decision-maker and the person affected by an outcome can be different people. Define their information, intervention and remedy routes separately. A customer may have a right to question a result without permission to inspect another customer's record or operate a privileged administrative tool.

Document who may delegate, approve a commitment, change a limit, stop a workflow and accept a residual risk. A generated role map does not appoint anyone. Check that the proposed person has capacity, access and enough time to act; an alert arriving after an irreversible consequence is not meaningful oversight of that consequence.

## Make the important state available

Provide an accessible task summary with the current goal, material constraints, progress, dependencies, actual effects and next decision. Let the person inspect more detail without requiring them to read an event log continuously. Distinguish agent-generated suggestions, observed tool results and human decisions.

Use plain status language such as “Waiting for the provider to confirm; the booking outcome is not yet known.” Do not translate internal network errors into false certainty. If progress is an estimate, label it and avoid a fabricated percentage. Make consequential information persistent or retrievable, with relevant timestamps and scope.

## Design notification priority and control

| Event | Possible treatment | Check |
| --- | --- | --- |
| Routine internal step | Group into progress summary or optional detail | Does it distract from the person's primary task? |
| Waiting on a dependency | Persistent status with what happens next | Can the person choose other work or intervene? |
| Required human decision | Clear, actionable notice with retrievable context | Can the person perceive it and understand the actual choice? |
| Failure or uncertain effect | Appropriate priority with recovery/status route | Does the message match actual execution evidence? |
| Completion | Outcome and remaining limits | Is success verified rather than merely predicted? |

Support relevant visual, non-visual and other platform access routes with user-controlled preferences. Equivalent information does not mean simultaneous compulsory speech, sound, vibration and visual alerts. Avoid focus theft, repeated assertive live-region output and token-by-token announcements that hide the one important event. Inspect the actual AT/device combination and repeated exposure, not only an isolated property check.

## Explain decisions usefully

An explanation should identify the interpreted goal, relevant evidence, material constraints, main decision factors, uncertainty and actual outcome. It should enable correction or challenge. A generated rationale must not claim that checks or approvals occurred without corresponding evidence.

This does not require revealing hidden internal chain-of-thought. Keep private prompts, credentials, confidential source data and security-sensitive detail protected. Provide role-appropriate summaries or controlled access to evidence. An audit trail should record actual events; an explanation can summarise those events without becoming their replacement.

## Make control workable

Provide accessible pause/cancel and handover routes suited to the service. Explain which operations can still stop, which effects may already exist and what recovery remains. Preserve valid work appropriately, including when the person changes pace, access mode or assistance preference. Recheck permissions on resumption rather than inheriting an expired authority.

Preview material commitments in a concise form: what will change, whom it affects, important costs/data and what can be reversed. Use existing authorisation for work it actually covers. Ask for clarification only when it materially affects the relevant action; continue independent authorised activity. Excessive confirmation can make people habituate to prompts and can defeat the intended benefit of delegation.

## Learn from people's experience

Investigate whether the person can stay oriented, choose support, recognise uncertainty and recover without unnecessary memory or attention demands. Include people who abandon or cannot enter the current route. Do not infer diagnosis, incapacity or preferred autonomy level from clicks, speed or device settings.

Satisfaction and trust reports are useful alongside observed outcomes. Neither proves correctness, security or appropriate authority. See [EX04](../examples/ex04.md), [EX07](../examples/ex07.md) and [Satisfactory experience](satisfactory-experience-and-research.md). Supporting context includes Cognitive UX, Data Ethics and W3C status-message guidance in [references](../docs/references.md).
