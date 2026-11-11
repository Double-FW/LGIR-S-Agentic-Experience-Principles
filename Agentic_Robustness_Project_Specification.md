# Robustness for human agency

## Knowledge base project specification

Version: 1.0  
Date: 9 November 2026  
Status: Proposed framework for research, discussion and development  
Scope: Objectives, principles, approaches, methodologies and desired outcomes

## 1. Project purpose

Create an openly readable, evidence-informed knowledge base that extends the *ideas* behind WCAG robustness into a framework for agent-mediated accessibility. Its purpose is to help organisations make websites and apps reliably understandable, adaptable and usable through people's chosen technologies, including AI agents acting under their authority.

The project should connect three ambitions: dependable interpretation of content and interfaces; meaningful choice over output, interaction and control; and services that respond to user-declared needs without unnecessary disclosure or loss of trust.

**Central objective:** maximise a person's effective agency by making the information and capabilities needed for their chosen task reliably available to authorised intermediaries, within proportionate and understandable boundaries.

Universality is a direction of progress: widening participation across abilities, technologies, languages and circumstances. It is not a promise that one interface, AI model or preference profile will meet every need.

This is an independent conceptual framework. It does not amend WCAG, create new WCAG success criteria, establish a conformance scheme or imply endorsement by W3C.

## 2. Starting position and conceptual accuracy

### Established foundations

WCAG 2.2 Principle 4 concerns reliable interpretation by diverse user agents, including assistive technologies. Its compatibility guideline addresses present and future agents. Within WCAG 2.2, Name, Role, Value and Status Messages remain relevant; Parsing, formerly 4.1.1, has been removed. Robustness should not be reduced to syntactically valid markup. [S1]

The accessibility tree is a browser-derived representation related to, but distinct from, the DOM. Native semantics and ARIA contribute to what browsers expose through platform accessibility interfaces. It is neither a complete copy of the DOM nor a general business-service interface. Accurate semantics remain essential, but a usable tree alone does not guarantee successful task completion. [S2, S3]

WAI-Adapt explores authored semantics for adaptation. W3C cognitive accessibility guidance also supports personalisation and the use of extensions. These provide useful foundations without establishing a complete, universally deployed agent-to-service preference negotiation system. [S4, S5]

### Proposed extension

For this project, **agentic robustness** means the dependable preservation of meaning, available capabilities, user intent and authority as people access services through different modalities and authorised intermediaries.

This extends the project's interpretation of robustness from *reliable interpretation* towards *reliable participation*: understanding what a service offers, adapting its presentation, expressing intent, delegating permitted actions and establishing what actually happened.

Several of these ambitions also involve WCAG's Perceivable, Operable and Understandable principles. They are gathered here because interoperability connects them; they should not all be relabelled as existing Principle 4 requirements.

## 3. Objectives and boundaries

The knowledge base should enable organisations to:

1. Preserve trustworthy meaning across human interfaces, accessibility interfaces and authorised service interfaces.
2. Support chosen combinations of visual, auditory, textual, tactile and other available output.
3. Support different ways of expressing intent and controlling tasks, including direct, assisted and delegated interaction.
4. Respond to declared functional needs and preferences without requiring diagnostic profiles.
5. Permit useful delegation while protecting identity, confidentiality, other people and service integrity.
6. Maintain understandable service identity, commitments and accountability when an intermediary changes the presentation.
7. Learn from participation and exclusion, including who remains underserved.

Included: websites, web apps, conceptual application to native apps, browsers, assistive technologies, user-chosen agents, service-provider agents and authorised human supporters. Native apps use their platform semantics and accessibility interfaces rather than a DOM model.

Excluded: component specifications, design patterns, implementation code, API contracts, protocol selection, data schemas, QA scripts, security test cases, certification and claims of legal compliance. These may be future projects, but must not dilute this strategic knowledge base.

The first edition should remain technology-neutral. An agent may use browser interaction, accessibility interfaces or authorised service interfaces. No single access route, model supplier or protocol should define the framework.

## 4. Audiences and responsibilities

| Audience | Intended use and responsibility |
| --- | --- |
| Disabled people and representative communities | Shape priorities, challenge assumptions and describe acceptable outcomes and burdens. |
| Service and product leaders | Make participation, service continuity and accountability explicit objectives. |
| Accessibility and inclusive design specialists | Connect established accessibility foundations with emerging forms of mediation. |
| Browser, assistive technology and agent providers | Preserve meaning, act within authority and communicate limitations. |
| Security, privacy and governance teams | Enable legitimate use through proportionate boundaries and accountable decisions. |
| Brand and customer experience teams | Preserve recognition, promises, trust and redress across presentations and channels. |
| Researchers and standards contributors | Identify evidence gaps and distinguish proposals from established requirements. |

Service providers remain responsible for the services they offer. Agent providers remain responsible for their mediation. A user should not become the default investigator or liability holder when the two disagree.

## 5. Working definitions

| Term | Meaning within this project |
| --- | --- |
| Human agency | A person's practical ability to understand choices, express intent and influence outcomes. |
| AI agent | Software capable of interpreting a goal and taking steps towards it; capabilities and autonomy vary. |
| Authorised intermediary | A technology or person permitted to assist within a defined scope. Technical access alone does not establish permission. |
| Output modality | The way information reaches a person, such as text, speech, images or braille. |
| Interaction modality | The way a person expresses intent, such as typing, speech, touch, switches or assisted communication. |
| Control | Authority over navigation, changes, submissions, commitments and stopping or recovering a task. |
| Functional need | An access requirement, such as more processing time, without needing an explanation of its medical cause. |
| Responsive accessibility | A service's ability to accommodate declared or locally applied needs and preferences as circumstances change, while preserving essential meaning and access. This is broader than responsive visual layout. |
| Preference negotiation | A bounded exchange about requested accommodations, available capabilities and unresolved differences; not an exchange of a complete personal profile. |
| Fidelity | Preservation of material facts, choices, relationships, warnings, commitments and outcomes through mediation. |

## 6. Candidate principle domains

These are proposed starting points for the knowledge base, not established standards. The accompanying prompt should refine them, resolve overlaps and produce a coherent public principles document.

### P01. Dependable shared meaning

Provide a coherent account of content, relationships, actions and current state across supported access routes. Agents should not have to infer essential meaning from appearance alone. Where representations disagree, make the conflict discoverable and recoverable. Desired outcome: people can depend on the same material service meaning through different technologies.

### P02. Choice of modality and mediation

Support access through different combinations of presentation and interaction, including simultaneous modalities. Let people choose familiar tools and change their approach during a task. Desired outcome: the interface becomes adaptable to the person rather than requiring the person to fit one mode of use.

### P03. Fidelity through transformation

Adapt explanation and presentation while preserving material information, genuine choices and service commitments. Distinguish source information from generated interpretation and disclose consequential uncertainty. Desired outcome: easier access without silent distortion or invented certainty.

### P04. Human authority over delegation

Let people choose whether, when and how much to delegate, including sustained delegation within agreed boundaries. Support stopping, narrowing, withdrawing or transferring control without an avoidable loss of work. Desired outcome: greater independence, including for people who cannot repeatedly perform conventional approval interactions.

### P05. Useful capabilities with bounded authority

Make legitimate task capabilities available to authorised agents, with permissions proportionate to purpose, scope, consequence and duration. Permission to read does not imply permission to change or commit. Desired outcome: substantial useful autonomy without unnecessary exposure or uncontrolled action.

### P06. Adaptation without compulsory disclosure

Accommodate functional requests wherever feasible without requiring disability labels, inferred diagnoses or permanent accounts. Prefer local application of preferences when provider disclosure is unnecessary. Desired outcome: access with dignity and less exposure of sensitive circumstances.

### P07. Negotiated, contextual accessibility

Recognise that preferences change and may conflict. Services should communicate what they can accommodate, and people should control priorities or use prior instructions they have chosen. Desired outcome: an understandable agreement, or a clear explanation and alternative when accommodation is unavailable.

### P08. Open interoperability and continuity

Support replaceable intermediaries, portable preferences where the user wants them, and continuity across access routes. Preserve an accessible route for people who decline AI, cannot afford it or lose access to it. Desired outcome: participation without dependence on one supplier or additional paid technology.

### P09. Proportionate security that preserves participation

Assess the behaviour, authority and potential harm involved rather than treating all automation as equivalent. Provide accessible routes through identity and fraud controls, with review and redress for mistaken restrictions. Desired outcome: protection that enables legitimate participation and does not make disability disclosure the price of access.

### P10. Trustworthy identity and accountable brand experience

Keep the service provider recognisable through mediation, along with the origin of information, applicable promises and responsibility for decisions. Surface material agent conflicts of interest. Desired outcome: people know whom they are dealing with, what to expect and where to seek help.

### P11. Recoverable and understandable outcomes

Make the status and consequences of delegated work intelligible in the person's chosen form. Do not present intention or attempted execution as confirmed success. Preserve practical routes to correction, cancellation, assistance or redress. Desired outcome: confidence grounded in what actually happened.

### P12. Universality through shared learning

Develop the framework with people with diverse, intersecting and changing needs. Record disagreements, limitations and excluded groups. Desired outcome: progressively broader participation supported by evidence, without claims of universal success.

## 7. Conceptual approach

Organise the knowledge around five connected relationships. These are analytical lenses, not a required software architecture.

| Relationship | Strategic question |
| --- | --- |
| Service meaning and accessible representation | Can people and their tools obtain dependable meaning and current state? |
| Representation and chosen modalities | Can presentation and interaction change without loss of material information? |
| User intent and delegated capability | Can the agent do what the person authorised, within the actual service permissions? |
| Personal preferences and provider capabilities | Can needs be met with the least necessary disclosure and an understandable resolution of conflicts? |
| Actions and accountable outcomes | Can the person establish what happened, retain control and obtain correction or redress? |

Service-side adaptation and user-side augmentation should be complementary. Agent assistance should not excuse inaccessible source services. Provider-managed agents should not displace the person's chosen intermediary merely to preserve a preferred customer journey.

## 8. Balancing access, authority and security

The governing ambition is **maximum useful delegation within the person's authorised purpose**, with proportionate protection. More agent autonomy is valuable when it increases the person's effective control; autonomy that obscures consequences, redirects choices or creates dependence can reduce it.

OWASP identifies prompt injection, tool abuse, data leakage and excessive autonomy as agent risks. Its guidance supports scoped permissions and controls around consequential actions. These are security foundations for this project's synthesis, not evidence that instructions alone can make an agent safe. [S9]

| Tension | Proposed decision approach |
| --- | --- |
| Repeated confirmation versus meaningful control | Use understandable prior delegation for suitable recurring actions; seek renewed authority when scope or material consequences change. Offer accessible ways to grant, inspect and withdraw authority. |
| Automation versus abuse prevention | Justify restrictions by the actual risk; provide proportionate alternatives and an accessible way to challenge mistaken blocking. |
| Personalisation versus privacy | Separate a requested accommodation from its cause. Share only what the provider needs for the stated task; do not reuse preferences for unrelated profiling. |
| Reading versus acting | Treat content, offers and embedded instructions as information to assess, not authority to change permissions or goals. |
| Rich context versus confidentiality | Limit what crosses service, agent and organisational boundaries; protect information about other people as well as the user. |
| Seamless experience versus consequential commitment | Preserve fluid low-consequence work while making material commitments understandable and consistent with the chosen delegation. |
| Brand consistency versus adaptive presentation | Preserve identity, trust, expectations, value and commitments while permitting changes to appearance, language and interaction. |

Restrictions should have a stated purpose, a proportionate scope, an accessible alternative where feasible and a route for review. This is not an instruction to bypass authentication or obtain information beyond a person's entitlements. Reading public material, reading authenticated records, changing data and making commitments require distinct consideration.

## 9. Preference negotiation methodology

Describe an iterative relationship rather than inventing a universal profile or protocol:

1. The person chooses an accommodation or authorises their intermediary to apply an existing preference.
2. The intermediary considers whether the accommodation can be applied locally.
3. If provider participation is needed, share the minimum functional request with permission and an understood purpose.
4. The provider indicates its capability, constraints and available alternatives.
5. The person or their authorised intermediary resolves trade-offs using the person's priorities.
6. The service makes the resulting arrangement understandable and revisable.
7. Changes, expiry and withdrawal do not silently reinstate inaccessible conditions or discard progress.

Separate permission to use a preference locally, permission to disclose it, and authority to act on a service. One does not imply the others. Treat disability inference from behaviour as outside the intended approach. A person may need different arrangements for different tasks or times of day; persistent adaptation should remain optional.

This is a project proposal informed by adaptation and privacy work [S4, S5, S6]. It is not a claim that present browsers and services already support this exchange consistently.

## 10. Trust and accessible brand objectives

Extend the assessment of brand experience beyond visual consistency. A mediated experience should help everyone identify the organisation and service, build trust, set understandable expectations, create value, communicate the organisation's values and remain relevant to the person.

The knowledge base should explore how those objectives survive alternative presentation and delegated interaction. A generated summary should not obscure who is making an offer, an agent should not silently change commercial terms, and a personalised presentation should not imply a different service commitment.

Trust should rest on observable fidelity, honest limitations, privacy, reliable outcomes and effective redress. Brand presentation or reassuring language alone cannot establish it. W3C's ethical and user-agent publications provide context for user interests and intermediary responsibilities [S7, S8]; the brand framing here is the project's own proposal.

## 11. Knowledge base structure and editorial model

The project should produce a small, connected set of documents:

| Proposed document | Purpose |
| --- | --- |
| Overview and scope | Explain the purpose, audience, boundaries and independent status. |
| High-level principles | Present the central public framework, with rationale, approaches and desired outcomes. |
| Conceptual model and glossary | Distinguish meaning, modalities, preferences, authority and outcomes. |
| Methodologies | Explain co-design, preference negotiation and proportionate decisions at a strategic level. |
| Trust, security and privacy | Address tensions, accountability and legitimate restrictions without implementation recipes. |
| Outcome framework | Describe participation, autonomy, burden, trust and continuity. |
| Evidence and open questions | Maintain source status, project synthesis, uncertainties and research priorities. |

Each principle should carry a stable identifier, concise statement, rationale, classic robustness connection, agentic extension, high-level approaches, desired outcome, tensions and evidence status. This is an editorial convention, not a technical schema.

Distinguish throughout: established requirements; informative guidance; emerging drafts; project proposals; and unresolved hypotheses. Record source title, publisher, URL, publication status, date checked, relevance and limitations. Summarise sources in original language, link to originals and avoid copying technical specifications into the knowledge base.

Write in plain British English with descriptive headings, short sections, explained terminology and tables only where they aid comparison. Content should stand alone while supporting retrieval by people and knowledge tools. Explicit boundaries should survive extraction: a retrieved proposal must not appear to be a W3C requirement.

## 12. Development methodology

**Foundation review:** establish the terminology and evidence base, including standards status and the limits of current support. Compare the proposed ambitions with all four WCAG principles and identify genuine extensions.

**Participatory development:** involve people with sensory, physical, cognitive and communication access needs, including intersecting needs and people who decline AI. Include assistive technology, agent, service, privacy, security and brand perspectives. Provide accessible participation and compensate contributors where practicable.

**Scenario reasoning:** explore journeys across changing modalities and levels of delegation. Include beneficial uses, unsupported needs, inconsistent representations, malicious content, agent failure and lost connectivity. Use these to challenge the principles, not to generate component specifications or QA scripts.

**Trade-off review:** ask who gains control, who bears effort, what data moves, what harm remains and what alternatives exist. Record contested decisions and uncertainty rather than claiming consensus prematurely.

**Editorial synthesis:** consolidate overlapping principles; map each to an identifiable inclusion objective and evidence category; distinguish aspiration from current capability.

**Publication and revision:** publish the principles as a versioned proposal, invite accessible feedback and review after significant standards, technology or evidence changes. Assign editorial and review responsibilities when the project team is formed; do not invent named owners.

## 13. Desired outcomes and evidence

Evaluate usefulness through research and service evidence rather than a robustness score or claimed conformance percentage.

| Outcome | Evidence to seek at programme level |
| --- | --- |
| Broader participation | More people can complete meaningful tasks across chosen technologies and combinations of needs. |
| Greater independence | People can choose and revise delegation while reducing unwanted dependence on others. |
| Less cognitive and physical burden | Fewer repeated explanations, unnecessary interactions and demands to remember preferences or task state. |
| Faithful access | Material meaning and service commitments remain understandable through mediation. |
| Privacy and dignity | Accommodation requires less unnecessary disclosure and supports people who decline persistent profiling. |
| Trust and accountability | People can identify the provider, understand outcomes and obtain correction or redress. |
| Continuity and choice | Tasks remain viable when agents, modalities, suppliers or connectivity change. |
| Equitable availability | Benefits extend to people using older, low-cost or non-AI technologies. |

Seek evidence of benefits and harms, including those caused by security or confirmation burdens. Compare experiences across contexts without requiring diagnostic classification. Do not turn evaluation into behavioural diagnosis, surveillance or compulsory tracking. Agree future indicators and evidence collection with affected communities; numeric thresholds are outside this specification.

## 14. Deliverables and acceptance expectations

The initial commissioned work should produce the seven connected knowledge documents described above, with the principles document as the primary output. This specification and its accompanying generation prompt initiate that work; they do not claim the entire knowledge base is already complete.

The first edition is ready for public review when:

- The relationship with existing WCAG is accurate and the proposed extension is explicit.
- The principles cover output, interaction, control, preference negotiation, trust and continuity.
- Substantial authorised delegation is supported without assuming unrestricted access.
- Privacy, security and user control are integrated into inclusion objectives.
- AI refusal, affordability and non-AI access are addressed.
- Native app applicability is explained without assuming every platform has a DOM.
- Source status and uncertainty are visible, and no consensus or effectiveness is fabricated.
- The text remains strategic and contains no patterns, code, schemas or QA tests.

## 15. Questions the project should keep open

- Which service capabilities genuinely require explicit provider cooperation, and which should users be able to adapt locally?
- How can people with limited capacity for repeated interaction retain effective authority without restrictive assumptions about their autonomy?
- How should contradictory information between an interface, an accessibility representation and a service interface be resolved?
- How can preference portability avoid creating a new identifier or fingerprint?
- When should an agent recommend a different modality, and how can that avoid overriding the person's choice?
- What evidence distinguishes useful personalisation from a new burden or an inferior service?
- How should accountability work when a provider, browser and agent each contributed to an unsuccessful outcome?

## 16. Source register

Sources checked on 9 November 2026. Status descriptions apply at that date; linked living documents may change. The framework, candidate principles and methodologies are original project synthesis informed by these sources.

| ID | Source and checked status | Relevance and limit |
| --- | --- | --- |
| S1 | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/), Recommendation, 12 December 2024 | Existing accessibility baseline; does not define this proposed agentic framework. |
| S2 | [W3C WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/), Recommendation, 6 June 2023 | Roles, states, properties and accessibility-tree relationship; not a business-action or permission protocol. |
| S3 | [W3C Core Accessibility API Mappings 1.2](https://www.w3.org/TR/core-aam-1.2/), Candidate Recommendation Draft, 5 November 2026 | Browser-to-accessibility API mappings; work in progress, not a final Recommendation. |
| S4 | [W3C WAI-Adapt Overview](https://www.w3.org/WAI/adapt/), explanatory overview | Adaptation foundations; linked work has differing maturity and does not establish universal implementation. |
| S5 | [W3C Cognitive Accessibility Objective: Support Adaptation and Personalization](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o8-personalization/), supplemental guidance from a Working Group Note | Supports user customisation and extensions; not required for WCAG conformance. |
| S6 | [W3C Privacy Principles](https://www.w3.org/TR/privacy-principles/), Statement, 15 May 2025 | Privacy foundations; not a jurisdiction-specific compliance determination. |
| S7 | [W3C Ethical Web Principles](https://www.w3.org/TR/ethical-web-principles/), Statement, 12 December 2024; non-normative principles | User benefit, inclusion and control; not a technical conformance standard. |
| S8 | [W3C User Agents](https://www.w3.org/TR/user-agents/), Group Note, 22 October 2026 | Intermediary duties to users; a Group Note is not a W3C Recommendation or W3C-endorsed standard. |
| S9 | [OWASP AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html), maintained security guidance | Agent threats and permission boundaries; not proof of security or a guarantee of accessibility. |
| S10 | [W3C Ethical Principles for Web Machine Learning](https://www.w3.org/TR/webmachinelearning-ethics/), Group Draft Note, 8 January 2024 | Context for autonomy, oversight and responsible ML; exploratory guidance, not a final endorsed standard. |
