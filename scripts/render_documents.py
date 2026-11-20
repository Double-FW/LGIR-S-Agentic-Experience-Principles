"""Render the specification, Understanding pages and examples from canonical data."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def write(path,text):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n')

def render():
    framework=json.loads((ROOT/'data/framework.json').read_text())
    criteria=json.loads((ROOT/'data/criteria.json').read_text())['criteria']
    sources={s['id']:s for s in json.loads((ROOT/'data/sources.json').read_text())}
    examples=json.loads((ROOT/'data/examples.json').read_text())
    paths={c['id']:f"understanding/{c['id'].lower().replace('.','-')}.md" for c in criteria}
    spec=['# LGIR+S Agentic Experience Principles','','Double-FW Editor’s Draft 0.1.0 · 20 November 2026','','## Abstract','','LGIR+S sets out four enabling principles—Legible, Governable, Interpretable and Robust—and an overarching Satisfactory experience principle. It addresses the system, data and human–agent relationship across a complete delegated task. This independent proposal complements applicable interface accessibility requirements.','','## Status and scope','','Read [Status](STATUS.md). Candidate criteria are for review and a bounded local pilot, not a W3C Recommendation, externally mandated obligation or validated conformance scheme. The exact Agentic Robustness definition comes from the owner; the detailed criteria and explanations are editorial development.','','## How to read requirements','','Uppercase MUST, MUST NOT, SHOULD and MAY follow the conventions of [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174), within this local draft. Understanding pages, techniques, examples and evaluation probes are informative. Local tier A denotes proposed foundation priority; AA denotes proposed extended assurance priority. Neither is a WCAG level or an overall compliance claim. An actual duty or serious harm is not waived by a tier label.','','Every criterion requires a declared task, people/roles, versions, operating envelope and evidence. A component check cannot establish complete-task success. Unsupported or unknown scope must be explicit. A justified Not applicable is different from Not evaluated.','','[Mapping and rationale](docs/web-wcag-vs-agentic-ai.md) · [Evaluation method](docs/evaluation-and-claims.md) · [Understanding index](understanding/README.md)','','## The five principles','']
    index=['# Understanding LGIR+S','','Informative explanation of candidate criteria. No product evaluation is recorded. Read [the specification](../SPECIFICATION.md) and [status](../STATUS.md) first.','','| Criterion | Topic | Proposed local tier |','| --- | --- | --- |']
    for p in framework['principles']:
        spec.extend([f"## {p['number']}. {p['name']}",'',p['definition'],''])
        for c in [x for x in criteria if x['principle']==p['name']]:
            slug=c['id'].lower().replace('.','-')
            spec.extend([f'<a id="{slug}"></a>',f"### {c['number']} {c['title']}",'',f"**Reference:** {c['id']} · **Proposed local tier:** {c['proposed_local_tier']} · **Product result:** Not evaluated",'',c['requirement'],'',f"[Understanding and application]({paths[c['id']]})",''])
            index.append(f"| [{c['id']}]({slug}.md) | {c['title']} | {c['proposed_local_tier']} |")
            lines=[f"# Understanding {c['id']}: {c['title']}",'','Informative · Editor’s Draft 0.1.0 · No product result established','','[Specification](../SPECIFICATION.md#'+slug+') · [Understanding index](README.md)','','## Candidate criterion','',c['requirement'],'',f"**Local priority:** {c['proposed_local_tier']} (provisional; not WCAG conformance).",'','## Intent and potential benefit','',c['intent'],'','This is a rationale to investigate, not a measured effectiveness claim. Confirm its relevance with the affected people and the actual service.','','## Applicability','',c['applicability'],'','## Implementation approach','',c['implementation_approach'],'',f"See [technique {c['technique_id']}](../implementation/techniques.md#{c['technique_id'].lower()}). The approach is informative; document and evaluate an alternative if it achieves the scoped outcome.",'','## Evaluation probe — not yet run','','1. Identify the task, roles, authorised scope, product/model/tool versions and expected evidence. Agree any service-specific timing and safety limits before testing.','2. Prepare controlled, synthetic or appropriately authorised test conditions; do not cause real irreversible effects merely to test a failure route.',f"3. {c['evaluation_probe']}",f"4. Observe: {c['expected_observation']}",'5. Capture actual events, accessible presentation and human observations separately. Record missing coverage and contrary evidence. Assign the criterion result using the evaluation method; do not infer effectiveness from this written probe.','','## Failure example','',c['failure_example'],'','## Worked application','']
            for eid in c['example_ids']:lines.append(f"- [{eid}: {examples[eid]['title']}](../examples/{eid.lower()}.md)")
            lines.extend(['','## Evidence and limits','','Retain the requirement ID, exact evaluated scope, method, observed outcome, source/version context, reviewer and unresolved gaps. A generated expected result is not an observation. Machine checks, human inspection, specialist evaluation and participant research have different roles. Passing this probe alone does not establish conformance with WCAG or reliability for all contexts.','','## Supporting references',''])
            for sid in c['source_ids']:lines.append(f"- [{sid}: {sources[sid]['title']}]({sources[sid]['url']}) — {sources[sid]['scope']}")
            write(paths[c['id']],'\n'.join(lines))
    write('SPECIFICATION.md','\n'.join(spec));write('understanding/README.md','\n'.join(index))
    exindex=['# Worked examples and applications','','All examples are fictional design cases. Benefits are reasoned hypotheses, not observed performance, participant testimony or proof that LGIR+S outperforms WCAG. A narrow interface review is not the whole of POUR, WCAG or inclusive design.','','| Example | Application |','| --- | --- |']
    for eid,e in examples.items():
        exindex.append(f"| [{eid}]({eid.lower()}.md) | {e['title']} |")
        lines=[f"# {eid}: {e['title']}",'','Fictional illustrative case · No product trial performed','','[Examples index](README.md) · [Summary mapping](../docs/web-wcag-vs-agentic-ai.md)','','## Situation','',e['situation'],'','## What a narrow interface-focused POUR review might examine','',e['pour_review'],'','These observations would not establish a full WCAG result; actual applicable criteria and complete processes still need evaluation.','','## Agentic issue that remains','',e['remaining_problem'],'','## Applying LGIR+S','']
        for name,body in e['application'].items():lines.append(f'- **{name}:** {body}')
        lines.extend(['','## Why this adds a better-targeted agentic question','',e['why_additional'],'','The proposed advantage is specificity for this agentic issue, not demonstrated general superiority or a reason to remove accessibility requirements.','','## Evaluate the proposal',''])
        for item in e['evaluation']:lines.append('- '+item)
        linked=[c for c in criteria if eid in c['example_ids']]
        lines.extend(['','## Linked criteria',''])
        for c in linked:lines.append(f"- [{c['id']}: {c['title']}](../{paths[c['id']]})")
        lines.extend(['','## Limits','',e['limits'],'','**Assessment status:** Not evaluated. No numerical effect, real approval or participant finding is asserted.'])
        write(f'examples/{eid.lower()}.md','\n'.join(lines))
    write('examples/README.md','\n'.join(exindex))
    techniques=['# Implementation techniques','','Informative approaches derived from the canonical candidate records. They are options to evaluate, not approved W3C techniques, production code or sufficient proof of conformance. Independently authored implementation chapters provide the wider architecture and human context.','','[Understanding index](../understanding/README.md) · [Evaluation](../docs/evaluation-and-claims.md)','','']
    for c in criteria:
        chapter='human-agent-legibility-and-co-agency.md' if c['principle'] in ['Legible','Governable','Interpretable'] else ('satisfactory-experience-and-research.md' if c['principle']=='Satisfactory' else ('epistemic-and-data-integrity.md' if c['number'] in ['4.1','4.2'] else 'execution-and-architectural-compatibility.md'))
        techniques.extend([f'<a id="{c["technique_id"].lower()}"></a>',f"## {c['technique_id']}: {c['title']}",'',f"**Supports:** [{c['id']}](../{paths[c['id']]})",'','**Possible implementation:** '+c['implementation_approach'],'','**Failure to guard against:** '+c['failure_example'],'',f'**Context and limits:** Read the [implementation chapter]({chapter}) and assess the actual declared scope. A technique can support several outcomes and still fail when configured or composed differently.',''])
    write('implementation/techniques.md','\n'.join(techniques))
    return {'criteria':len(criteria),'examples':len(examples)}

if __name__=='__main__':print(json.dumps(render()))
