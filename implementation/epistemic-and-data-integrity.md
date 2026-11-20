# Epistemic & Data Integrity

Informative implementation guidance · LGIRS-1.4, LGIRS-3.2–3.3 and LGIRS-4.1–4.2

Epistemic integrity concerns the relationship between available evidence and the claims or actions derived from it. Data integrity also concerns whether information and its context survive collection, transformation, retrieval and use without undetected corruption. A clean file can contain a false claim; a trustworthy source can be retrieved for the wrong question.

## 1. Record what is known about the source

Maintain a source record with an identifier, origin, version or immutable revision where available, publication/access/review dates with their distinct meanings, relevant scope, transformations, rights/access restrictions and verification status. Link material claims to their actual supporting records. The [source-record template](../templates/source-record.md) explains the human version.

For historical training collections, item-level attribution may be unavailable. Record the granularity actually known, such as collection-level lineage, documented filtering and unresolved provenance. Do not invent source URLs, pretend complete training traceability or treat the absence of an exact citation as proof a statement is false. The resulting limitation affects the permitted reliance and evaluation plan.

For runtime retrieval, record which source version supplied the context and what transformations were applied. Preserve qualifications at the retrieval unit: an isolated paragraph must not lose the fact that it came from a draft, fictional example, outdated legal interpretation or unverified source. A fresh embedding or export date does not renew the source's underlying review.

## 2. Keep different judgements separate

| Judgement | Question | Typical mistake |
| --- | --- | --- |
| Source reliability | What supports reliance on this source for this question? | Treating popularity or a public URL as verification |
| Currency | Is the relevant information suitable for this decision date? | Substituting retrieval date for substantive review |
| Retrieval relevance | Does this passage address the actual question and scope? | Treating similarity rank as factual authority |
| Model uncertainty | What is known about the reliability of the generated interpretation? | Presenting a self-reported confidence number as calibrated probability |
| Action risk | What can happen if the conclusion or execution is wrong? | Using the same threshold for harmless drafting and consequential action |

Use Unknown where evidence is absent. Define thresholds for the actual task with an evaluation basis; do not add a universal 80% or 95% rule merely because a template has a confidence field. Explanations should say what is missing and what would resolve it.

## 3. Establish trust boundaries

Separate authorised instructions from retrieved and tool-supplied content. Source material can contain commands, misleading metadata or hostile text. Treat it as data unless a legitimate authority relationship has been established. Do not let a source document expand permissions, change recipients or create tool authority.

Input cleaning and filtering can help, but prompt-injection resistance requires more than sanitisation. Combine limited credentials, action-boundary checks, safe data handling, structured outputs where appropriate and tests that inspect actual attempted effects. A model's verbal refusal is not proof that a tool call was blocked.

Include indirect injection in documents and tool results, conflicting versions, missing qualifications, unfamiliar but benign phrasing and multilingual/context changes relevant to the service. Record attack assumptions and exclusions. A defence can fail outside its tested cases, so preserve operational detection and response routes.

## 4. Validate transformations and outputs

Check that material meaning, source relationships and uncertainty survive summarisation, format conversion and export. Evaluate omitted qualifications and unsupported causal claims, not just checksum or schema success. A summary that changes “proposed” to “approved” is wrong even if its JSON is valid.

Where useful, maintain a controlled evidence set with known conflicts and expected uncertainty states. Compare outputs against actual source passages and have the appropriate expert or affected person examine the questions automation cannot resolve. Synthetic fixtures support repeatable checks but do not substitute for real task or participant evidence.

## 5. Operational workflow

1. Identify the task, intended reliance and affected people.
2. Select sources and record known provenance and gaps.
3. Apply trust and permission boundaries before retrieval can influence actions.
4. Retrieve source context and qualifications together.
5. Validate material claims, transformations and unknowns for the intended use.
6. Stop, qualify or obtain the decision needed for the affected action; continue independent authorised work where useful.
7. Record the source versions and limitations with the delivered result.
8. Review after source changes, observed errors, model/retrieval changes or new misuse evidence.

The [research-assistant example](../examples/ex03.md) and [hostile-document example](../examples/ex02.md) show the approach. Relevant references are DFW-QA, DFW-ETH and OWASP-PI in [references](../docs/references.md). No source register or defensive pattern proves factual truth or immunity to every attack.
