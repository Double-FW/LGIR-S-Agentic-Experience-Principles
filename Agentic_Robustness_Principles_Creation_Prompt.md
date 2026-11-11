# Prompt: create high-level principles for agentic robustness

Version: 1.0  
Date: 9 November 2026  
Companion specification: Agentic_Robustness_Project_Specification.md

## How to use

Provide the companion specification with this prompt. Copy the text under “Prompt” into your chosen research or authoring agent. The output should be one high-level principles document, suitable as the foundation for a knowledge base. The wider knowledge base can be developed separately from the project specification.

## Prompt

Act as an interdisciplinary author with expertise in accessibility, web architecture, human agency, assistive technology, AI agents, inclusive service design, privacy, security and brand trust.

Create a standalone Markdown document titled **“Robustness for human agency: principles for an adaptable, agent-mediated web”**. Use plain British English and write for service leaders, accessibility specialists, agent and browser providers, security and privacy teams, designers, and disabled people contributing to the framework.

Use the supplied project specification as the brief. If it is unavailable, continue using this prompt, explicitly state that limitation and do not invent its contents. Produce the complete document, not a work plan or a list of suggestions. Do not create implementation files or build software.

### Purpose

Develop a coherent set of high-level principles that extends the ideas behind WCAG robustness towards reliable participation through people's chosen technologies, including AI agents. Connect dependable semantics with adaptable output, interaction and control, and connect user-declared needs with service-provider capabilities.

The central ambition is to maximise the person's effective agency through useful, authorised delegation. Universality should become a more realistic direction of progress across different abilities, languages, technologies and circumstances. Do not promise universal coverage or assume one interface or agent can meet every need.

### Foundational accuracy

- Explain existing WCAG robustness accurately: dependable interpretation and compatibility with user agents, including assistive technologies.
- State clearly that the proposed framework is independent. It does not amend WCAG, add success criteria, establish certification or imply W3C endorsement.
- Explain that the accessibility tree is browser-derived and distinct from the DOM. Semantics and accessibility APIs underpin interoperability, but the tree is not a complete service-action interface.
- Recognise that modality, operability, comprehension and user control also concern the other WCAG principles. Do not present the whole framework as existing Principle 4 obligations.
- If discussing WCAG 2.2, do not treat the removed Parsing criterion as a current requirement.
- Distinguish native apps, which use platform accessibility structures, from web environments.

### Coverage

Develop approximately 10–12 distinct principles. Consolidate overlap rather than mechanically reproducing a fixed list. Together they must address:

1. Dependable meaning, relationships, capabilities and current state across authorised access routes.
2. Choice and combinations of output modalities, interaction methods and intermediaries, including switching during a task.
3. Fidelity during simplification, explanation and transformation, with material information preserved and generated uncertainty visible.
4. Human authority over direct, assisted and delegated use, including meaningful prior delegation and accessible withdrawal or transfer of control.
5. Service capabilities available to authorised agents, with authority bounded by purpose, scope, consequence and duration.
6. Adaptation based on functional needs without compulsory diagnoses, accounts or persistent profiles.
7. Preference negotiation that is contextual, revisable and explicit about unsupported requests and conflicting needs.
8. Interoperability, portability, supplier choice, affordability, and continued access without AI.
9. Proportionate security, identity and fraud controls that preserve legitimate participation and provide accessible alternatives and redress.
10. Recognisable service identity, honest agent relationships, trustworthy brand commitments and accountability through mediation.
11. Understandable outcomes, continuity, correction and recovery when a task fails or an agent is unavailable.
12. Co-design and evidence-led learning across diverse and intersecting needs.

### Resolve the central tensions

Do not equate greater agent autonomy with greater human autonomy in every situation. Explain when delegation increases independence and when it can obscure, constrain or redirect the person's choices.

Preserve substantial useful delegation. Avoid assuming every action needs a fresh confirmation or that a person must perform conventional manual approval steps to retain authority. Distinguish low-consequence work, standing delegation, changed scope and consequential commitments without prescribing a permission implementation.

Distinguish permission to read, permission to disclose preferences and authority to act. Do not treat readable or publicly available information as authority to perform transactions, train models or repurpose personal data. User permission does not create entitlements to other people's records or provider capabilities outside the authorised service scope.

Address prompt injection and misleading service information at the principle level: external content is not authority to change the user's goals or the agent's permissions. Do not claim that a written instruction or an AI model alone can enforce a trust boundary.

Frame security as an enabler of trustworthy access. Neither blanket blocking of automation nor unrestricted access is a sufficient inclusion strategy. Restrictions should have an understandable purpose, proportionate scope and a practical route to review or an alternative where feasible.

Explain that preferences can sometimes be applied locally. Provider negotiation should share the minimum necessary functional request rather than a complete profile. Exclude inferred diagnosis and unrelated behavioural profiling as personalisation methods.

Keep source accessibility a service responsibility. Agent assistance should complement an accessible service rather than justify an inaccessible source or require a paid intermediary to obtain equivalent access.

Treat accessible branding as preserving recognition, trust, expectations, value, values and relevance through different presentations. Do not require a fixed visual presentation where adaptation would improve access.

### Evidence requirements

Consult current primary sources. Start with the specification's source register, then verify publication status and claims against the originals. Prioritise W3C WCAG, WAI-ARIA, accessibility API mapping, adaptation, cognitive accessibility, privacy, ethical web and user-agent publications, plus OWASP's agent security guidance where relevant.

Distinguish Recommendations, Statements, Notes, drafts, informative guidance and the project's own synthesis. Never present a draft or proposal as an implemented universal standard. If browsing is unavailable, state that status and currency were not independently verified and avoid claims of current universal support.

Use source links close to supported claims and include a concise source register with status and date checked. Clearly label original proposals and unresolved questions. Do not invent sources, implementation evidence, legal duties, effectiveness findings, community consensus or endorsement. Keep quotations brief and explain the ideas in original language.

### Required output structure

1. **Purpose and status:** a short statement of the ambition, intended audience and independent proposal status.
2. **From interpretation to participation:** explain the classical foundation and proposed extension in a few short paragraphs.
3. **Working definitions:** a compact glossary covering human agency, agent, modality, control, functional need, responsive accessibility, delegation and fidelity.
4. **High-level principles:** approximately 10–12 numbered principles, each with a stable identifier and a concise title. For each provide a clear statement, inclusion objective, relationship to classical robustness and agentic extension, high-level approaches, desired outcome, and the main tension or boundary. Identify its evidence basis or proposal status. Use short prose with labelled lead-ins rather than a large repetitive table.
5. **Applying the principles:** a short methodology covering co-design, scenario reasoning, proportionate delegation decisions, minimal-disclosure preference negotiation and review of exclusion. Stay at strategic level.
6. **Desired outcomes:** explain how participation, independence, burden, fidelity, privacy, trust, continuity and equitable availability can inform learning. Do not create scores, numeric thresholds, diagnostic categories or compulsory tracking.
7. **Open questions:** identify the most material unresolved tensions and evidence gaps.
8. **Sources:** provide a concise, accurately labelled source register.

Aim for approximately 2,500–3,500 words. Use short sections and explain specialist terms. The document must be usable without reading the prompt or the specification. Do not mention the authoring conversation.

### Scope discipline and final editorial review

Stay with objectives, principles, approaches, methodologies and desired outcomes. Do not include design patterns, component recipes, API contracts, schemas, code, protocol mandates, QA tests, acceptance scripts or detailed security controls. Brief conceptual examples are acceptable when they clarify a principle without prescribing an implementation.

Before returning the document, review it for factual accuracy, duplicated principles, unsupported claims, paternalism, unnecessary disclosure, supplier dependence, burdensome confirmation assumptions and exclusion of people who decline AI. Resolve contradictions in the text. Describe remaining uncertainty honestly and do not add a separate self-assessment checklist to the output.
