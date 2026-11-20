# Summary Mapping: Web WCAG vs. Agentic AI

Informative · Double-FW Editor's Draft 0.1.0

## Two connected questions

WCAG addresses access to web content and interaction. LGIR+S examines delegation to an agent, the evidence and permissions behind its work, the consequences of its actions, and the quality of collaboration. An agent interface needs both relevant accessibility requirements and agent-specific assurance.

The mapping below is an analogy for organising questions. It is not a standards crosswalk, a claim of equal requirements or a replacement for actual WCAG success criteria. POUR principles are broader than the brief questions in any summary table. In particular, perception is not limited to seeing and hearing, operation includes appropriate access methods, and understanding includes predictable behaviour and help with mistakes.

## Summary mapping

| Web WCAG principle | Core web-access question | LGIR+S principle | Additional agentic question | Example evidence |
| --- | --- | --- | --- | --- |
| Perceivable | Can people perceive the relevant information and interface through appropriate access routes? | Legible | Can people identify agent involvement, available context, boundaries, evidence and meaningful state? | Accessible attribution, effective-scope display, event-derived status and provenance |
| Operable | Can people operate the interface and navigation? | Governable | Can the authorised person direct, constrain and intervene in work, with truthful stopping and recovery limits? | Permission enforcement, actual intervention response, scoped approval and recovery evidence |
| Understandable | Can people understand the information and interface operation? | Interpretable | Can people understand intent, material decision factors, evidence and uncertainty sufficiently to decide and challenge? | Goal/plan previews, evidence-linked explanations and correction routes |
| Robust | Can content be interpreted reliably by user agents, including assistive technology? | Robust | Can data, execution and human oversight remain dependable under relevant failures and changes? | Context-integrity checks, failure reconciliation, tool contracts and versioned change evaluation |
| No additional official WCAG principle in this comparison | Accessibility and usability overlap; the four principles do not certify the whole experience | Satisfactory | Does collaboration achieve the person's intended purpose with appropriate quality, total effort, dignity and choice? | Correct/useful task outcomes, burden measures and people's accounts with coverage limitations |

Satisfactory is the overarching outcome principle. It is examined through every other principle; it is not a final rating that can average away a serious failure. The five LGIR+S principles and the additional S in Double-FW POURS do not amend WCAG.

## Why the additional lens is useful for agents

| Situation | An interface-level question | The explicit LGIR+S extension |
| --- | --- | --- |
| A payment tool times out | Is the error perceivable and understandable? | Did the action already commit, is retry safe, and who must reconcile it? |
| A person presses Stop | Is the control accessible and operable? | Did queued/sub-agent work actually cease, and what effects remain? |
| A report contains references | Can people navigate meaningful links? | Were sources actually retrieved, do qualifications survive synthesis, and what checking burden remains? |
| An agent changes a plan | Are the updated controls and instructions understandable? | Does the operative goal still match the person's intention, and does the change need new authority? |
| A model provider changes | Does the interface still work with the supported AT? | Are permission handling, decision behaviour, recovery and total human effort still acceptable? |

These are additional assurance questions, not properties that WCAG forbids or that experienced accessibility practitioners necessarily ignore. A full WCAG assessment also includes complete processes and more than a few interface checks. The examples compare a narrow interface-focused review with an explicit agentic task review; none establishes a WCAG pass.

## Three meanings of Robust

1. **WCAG Robust:** the source-owned accessibility principle, evaluated using the applicable requirements.
2. **Double-FW Agentic Robustness:** data/context integrity, execution dependability and effective human oversight across a declared operating envelope and changes.
3. **Robustness in another standard or law:** that source's actual definition and scope, which require their own inspection and applicability assessment.

Feeling Safe, from POURS, is a related emotional lens. It does not establish any of the three technical or legal findings. A reassuring agent can still act incorrectly; a technically controlled agent can still leave people feeling excluded.

## Claim boundary

LGIR+S is proposed as a more directly expressed set of questions for agentic work. There is no comparative study showing that it produces better outcomes than POUR, WCAG, human-centred design or other AI frameworks. The [research agenda](research-and-open-questions.md) specifies how that proposition could be investigated. Retain applicable WCAG evaluation while testing the added value.

References: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Understanding the principles](https://www.w3.org/WAI/WCAG22/Understanding/intro), [WAI on the overlap of accessibility, usability and inclusion](https://www.w3.org/WAI/fundamentals/accessibility-usability-inclusion/), and [the source register](references.md).
