# Implementation techniques

Informative approaches derived from the canonical candidate records. They are options to evaluate, not approved W3C techniques, production code or sufficient proof of conformance. Independently authored implementation chapters provide the wider architecture and human context.

[Understanding index](../understanding/README.md) · [Evaluation](../docs/evaluation-and-claims.md)


<a id="t01"></a>
## T01: Agent involvement and identity

**Supports:** [LGIRS-1.1](../understanding/lgirs-1-1.md)

**Possible implementation:** Use plain labels with programmatic equivalents; identify the accountable service; separate generated drafts from receipts based on actual tool responses.

**Failure to guard against:** An AI-written success message is styled as a completed transaction despite no successful tool response.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t02"></a>
## T02: Current scope, capabilities and context

**Supports:** [LGIRS-1.2](../understanding/lgirs-1-2.md)

**Possible implementation:** Derive the summary from effective permissions and active integrations, not a static marketing capability list; use progressive detail for scope and exclusions.

**Failure to guard against:** A permission badge still says full access after revocation and the agent invents unseen appointments.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t03"></a>
## T03: Meaningful task and execution status

**Supports:** [LGIRS-1.3](../understanding/lgirs-1-3.md)

**Possible implementation:** Map real event records to user language; distinguish waiting for a person from waiting for a tool; provide a retrievable history with version and time.

**Failure to guard against:** A timeout becomes Failed, safe to retry even though the remote operation may have committed.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t04"></a>
## T04: Output provenance and evidence access

**Supports:** [LGIRS-1.4](../understanding/lgirs-1-4.md)

**Possible implementation:** Attach source identity, revision and relevant dates to claims; offer protected provenance summaries when direct links would expose private data.

**Failure to guard against:** The system cites a plausible URL that was never retrieved or publishes a private participant record as evidence.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t05"></a>
## T05: Non-disruptive accessible feedback

**Supports:** [LGIRS-1.5](../understanding/lgirs-1-5.md)

**Possible implementation:** Use appropriate semantic status patterns, persistent summaries and preference-aware notification policies; reserve interruption for the justified priority.

**Failure to guard against:** Every token update is announced assertively and the person misses the only message requiring a decision.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t06"></a>
## T06: Bounded delegation and effective permissions

**Supports:** [LGIRS-2.1](../understanding/lgirs-2-1.md)

**Possible implementation:** Use least-privilege credentials, explicit budgets and scope checks before consequential calls; propagate limits to delegated actors.

**Failure to guard against:** The agent treats a paragraph in a retrieved document as permission to bypass the budget.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t07"></a>
## T07: Effective intervention and truthful stopping

**Supports:** [LGIRS-2.2](../understanding/lgirs-2-2.md)

**Possible implementation:** Propagate stop intent, prevent new side effects, handle late events and report actual status; identify work that cannot be cancelled.

**Failure to guard against:** The UI says Stopped while a queued sub-agent continues sending messages.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t08"></a>
## T08: Commitment boundaries and proportionate approval

**Supports:** [LGIRS-2.3](../understanding/lgirs-2-3.md)

**Possible implementation:** Bind approval to the action, recipient, amount, data and version; invalidate it after a material change; keep preparatory work separate from commitment.

**Failure to guard against:** An approval for a draft email is reused to send a revised message to additional recipients.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t09"></a>
## T09: Reversal, compensation and consequence disclosure

**Supports:** [LGIRS-2.4](../understanding/lgirs-2-4.md)

**Possible implementation:** Use version-aware checkpoints, transaction boundaries and authorised compensating actions; prevent recovery from overwriting another person's later valid work.

**Failure to guard against:** Undo restores an old database snapshot over unrelated recent work or claims a delivered email was unsent.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t10"></a>
## T10: Continuity, handover and resumption

**Supports:** [LGIRS-2.5](../understanding/lgirs-2-5.md)

**Possible implementation:** Provide a concise resumable task record and explicit handover acceptance; recheck authority before resuming side effects.

**Failure to guard against:** A resumed task repeats the payment because the only saved state was the conversational draft.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t11"></a>
## T11: Intent, plan and material-effect preview

**Supports:** [LGIRS-3.1](../understanding/lgirs-3-1.md)

**Possible implementation:** Maintain a concise task brief and update only material changes; show effects on people, records, costs and dependencies.

**Failure to guard against:** The agent silently changes Find options into Book the cheapest option and drops the access requirement.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t12"></a>
## T12: Useful explanations and inspectable outcomes

**Supports:** [LGIRS-3.2](../understanding/lgirs-3-2.md)

**Possible implementation:** Separate event-derived traces from generated summaries; explain key factors and source limits without requiring hidden internal chain-of-thought.

**Failure to guard against:** A persuasive rationale claims checks were performed when no corresponding events exist.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t13"></a>
## T13: Uncertainty and reliance calibration

**Supports:** [LGIRS-3.3](../understanding/lgirs-3-3.md)

**Possible implementation:** Use evidence-linked uncertainty categories and task-specific thresholds with an explicit evaluation basis; request only the missing decision needed for the affected work.

**Failure to guard against:** The model reports 97% confidence from its own unsupported estimate and silently resolves the conflict.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t14"></a>
## T14: Consistent policy, preferences and limits

**Supports:** [LGIRS-3.4](../understanding/lgirs-3-4.md)

**Possible implementation:** Resolve instruction authority outside untrusted retrieval, version preference records and show meaningful changes; do not infer sensitive preferences from behaviour.

**Failure to guard against:** One sub-agent follows an expired policy while another treats a remembered preference as permission to disclose data.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t15"></a>
## T15: Challenge, correction and accessible remedy

**Supports:** [LGIRS-3.5](../understanding/lgirs-3-5.md)

**Possible implementation:** Link the outcome to case context and a service owner; distinguish proposed corrections from verified changes and avoid requiring repeated sensitive disclosure.

**Failure to guard against:** The only appeal is Ask the same bot again, and the bot repeatedly declares its own answer correct.

**Context and limits:** Read the [implementation chapter](human-agent-legibility-and-co-agency.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t16"></a>
## T16: Epistemic traceability and context integrity

**Supports:** [LGIRS-4.1](../understanding/lgirs-4-1.md)

**Possible implementation:** Use versioned source records, claim-to-source relationships and trust classifications; distinguish publication, access, review and expiry dates.

**Failure to guard against:** A fresh export date replaces the original legal review date and the model treats the old draft as current law.

**Context and limits:** Read the [implementation chapter](epistemic-and-data-integrity.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t17"></a>
## T17: Adversarial and distribution-shift resilience

**Supports:** [LGIRS-4.2](../understanding/lgirs-4-2.md)

**Possible implementation:** Separate trusted instructions from data, constrain tool authority and evaluate attack paths and benign edge cases; input sanitisation is one defence, not a complete solution.

**Failure to guard against:** The system rejects harmless unfamiliar phrasing but obeys a hidden instruction in an external document.

**Context and limits:** Read the [implementation chapter](epistemic-and-data-integrity.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t18"></a>
## T18: Capability, Intent, State contracts

**Supports:** [LGIRS-4.3](../understanding/lgirs-4-3.md)

**Possible implementation:** Separate the operation schema, authorised task intent and execution record; validate requests and results; define adapter and version compatibility.

**Failure to guard against:** A JSON response containing accepted is rendered as funds transferred even though settlement is unconfirmed.

**Context and limits:** Read the [implementation chapter](execution-and-architectural-compatibility.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t19"></a>
## T19: Safe execution and partial-failure recovery

**Supports:** [LGIRS-4.4](../understanding/lgirs-4-4.md)

**Possible implementation:** Use durable operation identifiers, supported idempotency, commit checks and reconciliation; use transaction rollback only within actual transaction boundaries.

**Failure to guard against:** A timeout triggers blind retry, creating duplicate bookings and a falsely successful recovery message.

**Context and limits:** Read the [implementation chapter](execution-and-architectural-compatibility.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t20"></a>
## T20: Supported portability and change assurance

**Supports:** [LGIRS-4.5](../understanding/lgirs-4-5.md)

**Possible implementation:** Maintain versioned task/failure/accessibility scenarios, compare action traces and human burden, and approve the actual supported combination.

**Failure to guard against:** A provider switch is approved solely because API requests parse and aggregate accuracy remains similar.

**Context and limits:** Read the [implementation chapter](execution-and-architectural-compatibility.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t21"></a>
## T21: Correct and useful intended outcomes

**Supports:** [LGIRS-5.1](../understanding/lgirs-5-1.md)

**Possible implementation:** Define goal-specific correctness and usefulness measures before the trial; examine adverse effects and relevant independent checks.

**Failure to guard against:** The dashboard declares success because a booking ID exists, ignoring the person's access requirement.

**Context and limits:** Read the [implementation chapter](satisfactory-experience-and-research.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t22"></a>
## T22: Total human burden and appropriate pace

**Supports:** [LGIRS-5.2](../understanding/lgirs-5-2.md)

**Possible implementation:** Record active and elapsed time separately, include assistance and correction, and compare appropriate accessible alternatives under comparable task conditions.

**Failure to guard against:** A 30-second generation is advertised as a 90% saving while ignoring an hour of review.

**Context and limits:** Read the [implementation chapter](satisfactory-experience-and-research.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t23"></a>
## T23: Choice, preferences and assistance

**Supports:** [LGIRS-5.3](../understanding/lgirs-5-3.md)

**Possible implementation:** Offer adjustable notification/detail, save-and-return and supported human routes; avoid diagnosis-based defaults and coercive agent-only channels.

**Failure to guard against:** The only accessible alternative is a slower paid channel available for fewer hours.

**Context and limits:** Read the [implementation chapter](satisfactory-experience-and-research.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t24"></a>
## T24: Dignity and comparable opportunity

**Supports:** [LGIRS-5.4](../understanding/lgirs-5-4.md)

**Possible implementation:** Combine task evidence with voluntary accounts and exposure-aware analysis; keep group definitions and sample limits explicit without inferring diagnoses.

**Failure to guard against:** A positive average rating hides that the assisted route requires humiliating disclosure.

**Context and limits:** Read the [implementation chapter](satisfactory-experience-and-research.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.

<a id="t25"></a>
## T25: Experience evidence and continuous improvement

**Supports:** [LGIRS-5.5](../understanding/lgirs-5-5.md)

**Possible implementation:** Ask short purposeful questions, use consent and data minimisation, analyse non-response and route exclusion, and track correction/retest ownership.

**Failure to guard against:** Only successful users can answer the survey, and the resulting score is described as satisfaction for every customer.

**Context and limits:** Read the [implementation chapter](satisfactory-experience-and-research.md) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.
