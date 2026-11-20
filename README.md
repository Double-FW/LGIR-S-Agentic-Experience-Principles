LGIR+S: Agentic Experience Principles

Legible · Governable · Interpretable · Robust + Satisfactory

Double FW Ltd · Editor's Draft 0.1.0 · 20 November 2026 · MIT

LGIR+S connects dependable agentic systems with useful, accessible and respectful human experiences. Four enabling principles describe how an agent should be made visible, controllable, understandable and dependable. Satisfactory is the overarching experience principle: does the collaboration actually help people achieve their purpose with appropriate quality and total effort?

This is an independent Double-FW proposal. Its organisation follows the useful specification / understanding / implementation / evaluation pattern used in standards documentation. It is not a W3C publication, Recommendation, approved ACT rule set or certification scheme. There is no claim that LGIR+S has been shown experimentally to outperform POUR.

What the principles mean—and why agents need them

LGIR+S treats four enabling conditions as a route to an experience that is actually satisfactory. The principles apply to the whole agentic task: the person’s request, information and context, model, tools, permissions, execution, oversight and effects. They are useful to agents working alone, in a multi-agent workflow or inside a larger service because each can affect the others.

Principle

What it asks

Why the question matters for agents

Legible

Can the relevant people identify the agent’s role, effective scope, important context, evidence, current state and real outcome?

An agent can act across tools, retain context and continue asynchronously. People cannot supervise, verify or resume work if involvement, limits or state are hidden or confused with a prediction.

Governable

Can an authorised person set boundaries, direct work and intervene, with truthful information about stopping, approval, reversal and recovery?

Agent output can become an external effect. A visible “human in the loop” is not effective control if the person lacks authority, time or a control that takes effect before the consequence.

Interpretable

Can people understand the operative goal, material assumptions, evidence, constraints and uncertainty well enough to decide, correct or challenge?

A fluent explanation can be mistaken for evidence. Explanations need to connect to actual sources, decisions and observed results. This does not require disclosure of hidden chain-of-thought.

Robust

Do data, execution and human oversight remain dependable across relevant models, contexts, integrations, failures and changes?

Agents depend on changing models, retrieved context, tools and external services. A valid response or interface alone cannot show that permissions, partial effects, state and recovery remain sound when something changes or fails.

Satisfactory

Does the collaboration achieve the person’s intended outcome with appropriate quality, effort, pace, dignity and choice?

Delegation can shift checking, correction and recovery onto the person. Measure the complete task and affected people’s experience, not just an agent’s speed, output or success flag.

Satisfactory is an outcome lens across the other four, not a score that averages away an unauthorised action, exclusion or serious failure. “Satisfactory experience” is the principle; satisfaction ratings are one possible kind of evidence and are not proof of correctness or safety.

The Robust principle uses the owner-supplied definition in the Specification. Here it extends the robustness question to the agentic system, its data and its human-facing interfaces; it does not replace or redefine WCAG’s Robust principle. The detailed Robust criteria are proposed editorial work for review.

Why an agent should use LGIR+S

An agent can use LGIR+S as a common reasoning and review structure when it is asked to plan, design, implement, assess or explain agentic work. The principles help it:

look beyond the prompt or screen to the complete task, relevant actors, data, tools and consequences;

keep authority separate from capability, generated plans and retrieved instructions;

distinguish evidence from narrative, including proposed plans, tool observations, uncertain outcomes and confirmed effects;

consider failure and change, including interruption, partial completion, retries, handover and model or provider updates;

account for human work and experience, including accessibility, verification, correction and recovery;

produce reviewable recommendations that name the applicable criteria, evidence gaps, assumptions and decisions requiring an authorised person.

The framework is appropriate as a shared lens for agents, but not as a claim that every criterion applies identically to every system. Agents should assess the declared task, operating context, people affected and consequences. They should explain a justified “not applicable” decision, keep “not evaluated” distinct from a pass, and avoid turning proposed criteria or local A/AA labels into legal, organisational or product approval.

Use applicable WCAG requirements and other relevant security, privacy, safety and legal processes alongside LGIR+S. The framework complements them; it does not establish that an agent is compliant, safe, effective or superior to another approach.

Start with your task

Task

Read

Understand the project without technical knowledge

Start here

Read the five principles and candidate requirements

Specification

Compare web WCAG and agentic AI

Summary mapping and rationale

Investigate one criterion

Understanding index

Design data and context handling

Epistemic & Data Integrity

Design execution and recovery

Execution & Architectural Compatibility

Design human oversight and interaction

Human-Agent Legibility & Co-Agency

Evaluate useful outcomes and human effort

Satisfactory experience

Apply the framework to an actual project

Applications, worked examples, adoption runbook

Plan assessment and report limitations

Evaluation and claims, templates

Work with an AI assistant

AGENTS.md

What this edition contains

Five principles; 25 candidate criteria; an Understanding page for each criterion; implementation techniques; eight fictional worked applications; reusable assessment templates; machine-readable criterion/source records; and illustrative operation records with local integrity checks. The examples and proposed evaluation probes are not executed product evidence.

Use applicable accessibility requirements alongside LGIR+S. An agent control must still be accessible. LGIR+S adds explicit questions about delegation, permission, evidence, remote effects, intervention, model changes and the human work left behind. It does not replace WCAG, security engineering, applicable duties or participation by affected people.

Status and publication

Read Status, sources and known limitations. The framework is prepared for review and a bounded pilot; no operational agent, monitoring service, credential handling or Hugging Face sync is deployed by this repository.

Repository: Double-FW/LGIR-S-Agentic-Experience-Principles. This is an editor’s draft prepared for review and a bounded pilot, not a deployed product or validated conformance scheme.

Original material is copyright 2026 Double FW Ltd under LICENSE. External material retains its own terms; see NOTICE.
