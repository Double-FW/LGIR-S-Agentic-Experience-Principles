"""Check document/data integrity and selected synthetic-record invariants only."""
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import unquote,urlsplit
import render_documents

ROOT=Path(__file__).resolve().parents[1]
OWNER_DEFINITION='Agentic systems, their underlying data, and their human-facing interfaces must be resilient, transparent, and interoperable enough to operate reliably across diverse models, shifting contexts, and human oversight mechanisms, both now and as capabilities evolve.'

def operation_errors(record,schema):
    errors=[]
    if not isinstance(record,dict):return ['Operation record must be an object']
    for key in schema['required']:
        if key not in record:errors.append('Missing operation field: '+key)
    for key in record:
        if key not in schema['properties']:errors.append('Unknown operation field: '+key)
    if errors:return errors
    for key,rule in schema['properties'].items():
        value=record[key]
        if rule.get('type')=='string' and (not isinstance(value,str) or not value.strip()):errors.append('Invalid string field: '+key)
        if rule.get('type')=='boolean' and not isinstance(value,bool):errors.append('Invalid boolean field: '+key)
        if rule.get('type')=='array' and (not isinstance(value,list) or any(not isinstance(x,str) or not x.strip() for x in value)):errors.append('Invalid array field: '+key)
        if 'enum' in rule and value not in rule['enum']:errors.append('Invalid enum field: '+key)
        if 'const' in rule and value is not rule['const']:errors.append('Invalid constant field: '+key)
    if errors:return errors
    if not record['limitations']:errors.append('Operation limitations are missing')
    state=record['execution_status'];effect=record['effect_status']
    if state=='outcome_unknown' and (effect!='unknown' or record['retry_policy']!='blocked_pending_reconciliation'):errors.append('Unknown outcome must retain unknown effect and the conservative blocked retry policy')
    if state=='completed' and (effect!='committed' or not record['evidence']):errors.append('Completed operation lacks committed effect/evidence')
    if state in ['failed_no_effect','stopped_before_commit'] and (effect!='none' or not record['evidence']):errors.append('No-effect claim lacks matching effect/evidence')
    if record['recovery_class'] in ['irreversible','unknown','not_applicable'] and record['can_undo']:errors.append('Undo contradicts recovery class')
    return errors

def check(root=ROOT):
    errors=[]
    def fail(message):errors.append(message)
    try:
        framework=json.loads((root/'data/framework.json').read_text())
        criteria=json.loads((root/'data/criteria.json').read_text())['criteria']
        examples=json.loads((root/'data/examples.json').read_text())
        sources=json.loads((root/'data/sources.json').read_text())
        schema=json.loads((root/'schemas/operation-record.schema.json').read_text())
    except (OSError,ValueError,KeyError,TypeError) as exc:return ['Unreadable canonical data: '+str(exc)]
    if framework.get('robust_definition')!=OWNER_DEFINITION:fail('Owner definition changed without an explicit preservation-check update')
    principles=framework.get('principles',[])
    if [p.get('name') for p in principles]!=['Legible','Governable','Interpretable','Robust','Satisfactory']:fail('Five principle names/order differ from LGIR+S')
    if len(principles)>3 and principles[3].get('definition')!=framework.get('robust_definition'):fail('Robust principle differs from retained definition')
    expected_ids={f'LGIRS-{p}.{c}' for p in range(1,6) for c in range(1,6)}
    ids=[c.get('id') for c in criteria]
    if set(ids)!=expected_ids or len(ids)!=25:fail('Expected 25 distinct stable criterion IDs')
    source_ids=[s.get('id') for s in sources]
    if len(set(source_ids))!=len(source_ids):fail('Duplicate source ID')
    for s in sources:
        if not s.get('url','').startswith('https://') or not s.get('scope'):fail('Incomplete source URL/scope')
        if s.get('source_type')=='double_fw_public_guidance':
            if s.get('public') is not True or not re.fullmatch('[a-f0-9]{40}',s.get('commit','')):fail('Double-FW source is not recorded as public/pinned')
            prefix=f"https://github.com/{s.get('repository')}/blob/{s.get('commit')}/"
            if not s['url'].startswith(prefix):fail('Double-FW source URL does not use its pinned revision')
    if set(examples)!={f'EX{i:02d}' for i in range(1,9)}:fail('Expected eight worked cases')
    for eid,e in examples.items():
        if e.get('fictional') is not True or e.get('evaluation_status')!='not_evaluated':fail(eid+': fictional case falsely promoted to product evidence')
        if set(e.get('application',{}))!={'Legible','Governable','Interpretable','Robust','Satisfactory'}:fail(eid+': missing principle application')
    techniques=[]
    required=['title','principle','requirement','intent','applicability','implementation_approach','evaluation_probe','expected_observation','failure_example','authority','tier_status']
    for c in criteria:
        cid=c.get('id','MISSING')
        for field in required:
            if not isinstance(c.get(field),str) or not c[field].strip():fail(cid+': missing '+field)
        if c.get('proposed_local_tier') not in ['A','AA']:fail(cid+': invalid local priority')
        if c.get('tier_status')!='provisional_local_priority_not_wcag_or_agentic_conformance':fail(cid+': priority falsely promoted to conformance')
        if c.get('product_evaluation_status')!='not_evaluated' or c.get('independently_validated') is not False:fail(cid+': unexecuted criterion falsely promoted to evaluated/validated')
        if any(sid not in source_ids for sid in c.get('source_ids',[])):fail(cid+': dangling source reference')
        if not c.get('example_ids') or any(eid not in examples for eid in c['example_ids']):fail(cid+': dangling/missing example reference')
        if not re.fullmatch('T[0-9]{2}',c.get('technique_id','')):fail(cid+': invalid technique ID')
        techniques.append(c.get('technique_id'))
    if len(set(techniques))!=25:fail('Expected a distinct technique reference for each criterion')
    for p in (root/'examples/records').glob('*.json'):
        try:record=json.loads(p.read_text())
        except ValueError as exc:fail(str(p.name)+': '+str(exc));continue
        for e in operation_errors(record,schema):fail(p.name+': '+e)
    if errors:return errors
    # Re-render in an isolated temporary directory; do not overwrite working views.
    with tempfile.TemporaryDirectory() as temp:
        temp=Path(temp);shutil.copytree(root/'data',temp/'data')
        old=render_documents.ROOT
        try:render_documents.ROOT=temp;render_documents.render()
        finally:render_documents.ROOT=old
        expected_paths=set()
        for p in temp.rglob('*.md'):
            rel=p.relative_to(temp);expected_paths.add(str(rel));actual=root/rel
            if not actual.is_file() or actual.read_bytes()!=p.read_bytes():fail('Stale generated view: '+str(rel))
        for folder in ['understanding']:
            actual={str(p.relative_to(root)) for p in (root/folder).glob('*.md')}
            expected={p for p in expected_paths if p.startswith(folder+'/')}
            if actual!=expected:fail('Unexpected generated file set: '+folder)
    # Local Markdown links and fragments, outside literal fenced examples.
    for p in root.rglob('*.md'):
        text=p.read_text();fence=False
        if '\ufffd' in text:fail('Replacement character in '+str(p.relative_to(root)))
        for line in text.splitlines():
            if line.lstrip().startswith(('```','~~~')):fence=not fence;continue
            if fence:continue
            for raw in re.findall(r'\]\(([^)]+)\)',line):
                link=raw.strip().strip('<>');u=urlsplit(link)
                if u.scheme or u.netloc:continue
                target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
                if not target.is_relative_to(root.resolve()) or not target.is_file():fail(str(p.relative_to(root))+': missing local target '+link);continue
                if u.fragment and target.suffix=='.md':
                    body=target.read_text();anchors=set(re.findall(r'<a id="([^"]+)"',body))
                    for h in re.findall(r'^#{1,6}\s+(.+)$',body,re.M):anchors.add(re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-'))
                    if unquote(u.fragment) not in anchors:fail(str(p.relative_to(root))+': missing fragment '+link)
    return errors

if __name__=='__main__':
    errors=check()
    if errors:print('\n'.join(errors));raise SystemExit(1)
    print(json.dumps({'status':'passed','candidate_criteria':25,'fictional_cases':8,'operation_examples':4,'scope':'record/reference integrity, generated-view consistency, local navigation and selected synthetic invariants','product_evaluation_performed':False,'live_external_link_audit':False}))
