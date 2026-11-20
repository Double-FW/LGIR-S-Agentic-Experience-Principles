# LGIR+S Agentic Experience Principles

Double-FW Editor’s Draft 0.1.0 · 20 November 2026

## Abstract

LGIR+S sets out four enabling principles—Legible, Governable, Interpretable and Robust—and an overarching Satisfactory experience principle. It addresses the system, data and human–agent relationship across a complete delegated task. This independent proposal complements applicable interface accessibility requirements.

## Status and scope

Read [Status](STATUS.md). Candidate criteria are for review and a bounded local pilot, not a W3C Recommendation, externally mandated obligation or validated conformance scheme. The exact Agentic Robustness definition comes from the owner; the detailed criteria and explanations are editorial development.

## How to read requirements

Uppercase MUST, MUST NOT, SHOULD and MAY follow the conventions of [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174), within this local draft. Understanding pages, techniques, examples and evaluation probes are informative. Local tier A denotes proposed foundation priority; AA denotes proposed extended assurance priority. Neither is a WCAG level or an overall compliance claim. An actual duty or serious harm is not waived by a tier label.

Every criterion requires a declared task, people/roles, versions, operating envelope and evidence. A component check cannot establish complete-task success. Unsupported or unknown scope must be explicit. A justified Not applicable is different from Not evaluated.

[Mapping and rationale](docs/web-wcag-vs-agentic-ai.md) · [Evaluation method](docs/evaluation-and-claims.md) · [Understanding index](understanding/README.md)

## The five principles

## 1. Legible

Agent involvement, relevant capabilities, context boundaries, evidence and meaningful state are available in forms people can identify and use.

<a id="lgirs-1-1"></a>
### 1.1 Agent involvement and identity

**Reference:** LGIRS-1.1 · **Proposed local tier:** A · **Product result:** Not evaluated

The service MUST identify material agent involvement, the service responsible for it and whether a presented item is a proposal, generated output or confirmed system result through the supported accessible presentation.

[Understanding and application](understanding/lgirs-1-1.md)

<a id="lgirs-1-2"></a>
### 1.2 Current scope, capabilities and context

**Reference:** LGIRS-1.2 · **Proposed local tier:** A · **Product result:** Not evaluated

Before delegation and when a material boundary changes, the service MUST make the relevant accessible summary of available capabilities, effective permissions, significant context limits and delegation duration available to the authorised person.

[Understanding and application](understanding/lgirs-1-2.md)

<a id="lgirs-1-3"></a>
### 1.3 Meaningful task and execution status

**Reference:** LGIRS-1.3 · **Proposed local tier:** A · **Product result:** Not evaluated

The service MUST expose meaningful current task states, pending dependencies and actual completion or uncertainty without presenting predicted progress as an observed result.

[Understanding and application](understanding/lgirs-1-3.md)

<a id="lgirs-1-4"></a>
### 1.4 Output provenance and evidence access

**Reference:** LGIRS-1.4 · **Proposed local tier:** AA · **Product result:** Not evaluated

Material factual or action claims MUST have accessible provenance or an explicit evidence gap, with access to supporting detail appropriate to the person's role and the confidentiality of the source.

[Understanding and application](understanding/lgirs-1-4.md)

<a id="lgirs-1-5"></a>
### 1.5 Non-disruptive accessible feedback

**Reference:** LGIRS-1.5 · **Proposed local tier:** AA · **Product result:** Not evaluated

Status and intervention information MUST be available through the supported accessible routes with meaningful priority, persistence and user control, without requiring every channel to operate simultaneously.

[Understanding and application](understanding/lgirs-1-5.md)

## 2. Governable

Authorised people can direct, constrain and intervene in agentic work, with truthful limits on stopping, reversal and recovery.

<a id="lgirs-2-1"></a>
### 2.1 Bounded delegation and effective permissions

**Reference:** LGIRS-2.1 · **Proposed local tier:** A · **Product result:** Not evaluated

Agent actions MUST be constrained by effective authorised scope, resource limits and expiry, enforced at action boundaries independently of generated instructions.

[Understanding and application](understanding/lgirs-2-1.md)

<a id="lgirs-2-2"></a>
### 2.2 Effective intervention and truthful stopping

**Reference:** LGIRS-2.2 · **Proposed local tier:** A · **Product result:** Not evaluated

The authorised person MUST have an accessible intervention route with declared response limits; the system MUST distinguish an intervention request from confirmed cessation and reconcile work already in flight.

[Understanding and application](understanding/lgirs-2-2.md)

<a id="lgirs-2-3"></a>
### 2.3 Commitment boundaries and proportionate approval

**Reference:** LGIRS-2.3 · **Proposed local tier:** A · **Product result:** Not evaluated

Before an action exceeds existing authorisation or crosses a declared high-impact or irreversible boundary, the service MUST provide an accessible preview of material effects and obtain the required actual decision.

[Understanding and application](understanding/lgirs-2-3.md)

<a id="lgirs-2-4"></a>
### 2.4 Reversal, compensation and consequence disclosure

**Reference:** LGIRS-2.4 · **Proposed local tier:** AA · **Product result:** Not evaluated

For state-changing actions the service MUST identify what is reversible, compensatable or irreversible, provide the supported recovery route and disclose residual consequences and limits before commitment where relevant.

[Understanding and application](understanding/lgirs-2-4.md)

<a id="lgirs-2-5"></a>
### 2.5 Continuity, handover and resumption

**Reference:** LGIRS-2.5 · **Proposed local tier:** AA · **Product result:** Not evaluated

After interruption, assistance or transfer, the service MUST preserve appropriate valid work and make current intent, completed effects, pending decisions and remaining limits available to the authorised successor.

[Understanding and application](understanding/lgirs-2-5.md)

## 3. Interpretable

People can understand operative intent, material evidence, constraints and uncertainty sufficiently to make relevant decisions and challenge outcomes.

<a id="lgirs-3-1"></a>
### 3.1 Intent, plan and material-effect preview

**Reference:** LGIRS-3.1 · **Proposed local tier:** A · **Product result:** Not evaluated

The service MUST make its operative interpretation of the person's goal, relevant assumptions and material planned effects inspectable in plain language before the affected commitments.

[Understanding and application](understanding/lgirs-3-1.md)

<a id="lgirs-3-2"></a>
### 3.2 Useful explanations and inspectable outcomes

**Reference:** LGIRS-3.2 · **Proposed local tier:** A · **Product result:** Not evaluated

For consequential recommendations and actions the service MUST provide an understandable account of relevant evidence, material constraints, decision factors and observed outcomes, with uncertainty and missing evidence explicit.

[Understanding and application](understanding/lgirs-3-2.md)

<a id="lgirs-3-3"></a>
### 3.3 Uncertainty and reliance calibration

**Reference:** LGIRS-3.3 · **Proposed local tier:** AA · **Product result:** Not evaluated

Material uncertainty from sources, retrieval, model behaviour and action outcomes MUST be distinguished and communicated in a form appropriate to the decision; numerical confidence MUST NOT be presented as calibrated without relevant evaluation.

[Understanding and application](understanding/lgirs-3-3.md)

<a id="lgirs-3-4"></a>
### 3.4 Consistent policy, preferences and limits

**Reference:** LGIRS-3.4 · **Proposed local tier:** AA · **Product result:** Not evaluated

The service MUST apply the declared versioned rules and relevant authorised preferences consistently and explain material conflicts, expiry or changes that affect the task.

[Understanding and application](understanding/lgirs-3-4.md)

<a id="lgirs-3-5"></a>
### 3.5 Challenge, correction and accessible remedy

**Reference:** LGIRS-3.5 · **Proposed local tier:** AA · **Product result:** Not evaluated

People affected by consequential outcomes MUST have an accessible route to question material information, submit corrections and reach the responsible human or service with a traceable response.

[Understanding and application](understanding/lgirs-3-5.md)

## 4. Robust

Agentic systems, their underlying data, and their human-facing interfaces must be resilient, transparent, and interoperable enough to operate reliably across diverse models, shifting contexts, and human oversight mechanisms, both now and as capabilities evolve.

<a id="lgirs-4-1"></a>
### 4.1 Epistemic traceability and context integrity

**Reference:** LGIRS-4.1 · **Proposed local tier:** A · **Product result:** Not evaluated

Material training-data collection, retrieval and runtime-context dependencies MUST have provenance at the granularity actually available, relevant dates, transformations and declared evidence gaps; these qualifications MUST survive retrieval and export.

[Understanding and application](understanding/lgirs-4-1.md)

<a id="lgirs-4-2"></a>
### 4.2 Adversarial and distribution-shift resilience

**Reference:** LGIRS-4.2 · **Proposed local tier:** AA · **Product result:** Not evaluated

The declared operating envelope MUST be evaluated with representative ambiguous, unfamiliar and adversarial inputs, and failures MUST lead to bounded behaviour and truthful uncertainty rather than unauthorised action or fabricated certainty.

[Understanding and application](understanding/lgirs-4-2.md)

<a id="lgirs-4-3"></a>
### 4.3 Capability, Intent, State contracts

**Reference:** LGIRS-4.3 · **Proposed local tier:** A · **Product result:** Not evaluated

Tool and sub-agent integrations MUST provide versioned machine-readable capability contracts, intended effects and observed execution states, with validation and authorisation at the consuming boundary.

[Understanding and application](understanding/lgirs-4-3.md)

<a id="lgirs-4-4"></a>
### 4.4 Safe execution and partial-failure recovery

**Reference:** LGIRS-4.4 · **Proposed local tier:** A · **Product result:** Not evaluated

The service MUST preserve truthful state, constrain further effects and use evaluated recovery or escalation when execution fails or its outcome is uncertain; retries MUST account for duplicate and partial effects.

[Understanding and application](understanding/lgirs-4-4.md)

<a id="lgirs-4-5"></a>
### 4.5 Supported portability and change assurance

**Reference:** LGIRS-4.5 · **Proposed local tier:** AA · **Product result:** Not evaluated

Changes to model, provider, prompt, retrieval, tool contract or oversight design MUST be evaluated against the declared behavioural and access expectations before affected release, with versioned limitations and rollback or alternative plans.

[Understanding and application](understanding/lgirs-4-5.md)

## 5. Satisfactory

Agentic experiences must help people achieve their intended outcomes with appropriate quality, time and effort, while respecting their dignity, identity, preferences and control. Success must account for the work transferred to the human, including checking, correcting, supervising and recovering.

<a id="lgirs-5-1"></a>
### 5.1 Correct and useful intended outcomes

**Reference:** LGIRS-5.1 · **Proposed local tier:** A · **Product result:** Not evaluated

Evaluation MUST establish whether the person's intended outcome is achieved correctly and usefully within the declared scope, distinguishing generated output, administrative completion and actual benefit.

[Understanding and application](understanding/lgirs-5-1.md)

<a id="lgirs-5-2"></a>
### 5.2 Total human burden and appropriate pace

**Reference:** LGIRS-5.2 · **Proposed local tier:** AA · **Product result:** Not evaluated

Evaluation MUST include the person's total relevant effort and time across delegation, waiting, supervision, verification, correction and recovery, with the comparison and uncertainty stated.

[Understanding and application](understanding/lgirs-5-2.md)

<a id="lgirs-5-3"></a>
### 5.3 Choice, preferences and assistance

**Reference:** LGIRS-5.3 · **Proposed local tier:** A · **Product result:** Not evaluated

The experience MUST support relevant choices of pace, presentation, assistance and delegation within real service constraints, with workable alternatives and explicit limits.

[Understanding and application](understanding/lgirs-5-3.md)

<a id="lgirs-5-4"></a>
### 5.4 Dignity and comparable opportunity

**Reference:** LGIRS-5.4 · **Proposed local tier:** A · **Product result:** Not evaluated

Evaluation MUST examine material differences in dignity, privacy, control, service quality and opportunity across relevant access routes and affected groups; favourable averages MUST NOT erase a serious excluded outcome.

[Understanding and application](understanding/lgirs-5-4.md)

<a id="lgirs-5-5"></a>
### 5.5 Experience evidence and continuous improvement

**Reference:** LGIRS-5.5 · **Proposed local tier:** AA · **Product result:** Not evaluated

The service evaluation MUST collect proportionate accessible evidence about whether the experience met people's needs and reasons, connect findings to owned improvement work and preserve contrary evidence and study limitations.

[Understanding and application](understanding/lgirs-5-5.md)
