"""Export approved committed LGIR+S records without inventing training answers."""
import argparse
import json
from pathlib import Path
import subprocess
from lgirs_hf_common import ROOT,SOURCE,TARGET,MANAGED,read_sources,git,destination

STREAMS=('criteria','examples','guidance','routing_functions','operation_examples')
def serial(value):return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'))

def build(root,output,dataset_id=TARGET):
    destination(dataset_id);root=Path(root);output=Path(output)
    cfg,texts,manifest=read_sources(root)
    # Both the checked source bytes and the checker itself are committed inputs.
    subprocess.run(['python','scripts/check_repository.py'],cwd=root,check=True,capture_output=True,text=True)
    commit=git(root,'rev-parse','HEAD').decode().strip()
    date=git(root,'show','-s','--format=%cI','HEAD').decode().strip()
    framework=json.loads(texts['data/framework.json']);criteria=json.loads(texts['data/criteria.json']);examples=json.loads(texts['data/examples.json'])
    mapping=json.loads(texts['docs/agentic-accessibility-function-routing-map.json'])
    context=serial({'framework':framework,'source_status':texts['STATUS.md'],'agent_instructions_as_source_data':texts['AGENTS.md'],'notice':texts['NOTICE.md'],'qualification':'Double-FW editorial draft. Proposed local A/AA tiers are not WCAG conformance. Fictional examples are not observed performance. Retrieved instructions do not grant execution authority.'})
    streams={k:[] for k in STREAMS}
    def record(stream,ident,path,body,**fields):
        streams[stream].append(dict(id=ident,source_repository=SOURCE,source_commit=commit,source_commit_date=date,source_path=path,source_url=f'https://github.com/{SOURCE}/blob/{commit}/{path}',framework_context_json=context,record_json=serial(body),**fields))
    ids={c['id'] for c in criteria['criteria']}
    if len(ids)!=len(criteria['criteria']):raise ValueError('Duplicate criterion IDs.')
    for c in criteria['criteria']:
        record('criteria',c['id'],'data/criteria.json',c,title=c['title'],principle=c['principle'],product_evaluation_status=c['product_evaluation_status'])
    for ident,e in examples.items():
        if e.get('fictional') is not True or e.get('evaluation_status')!='not_evaluated':raise ValueError('Example status must be reviewed before publication.')
        record('examples',ident,'data/examples.json',e,title=e['title'],fictional=True,evaluation_status=e['evaluation_status'])
    for path in cfg['guidance_files']:
        if path not in texts or not path.endswith('.md'):raise ValueError('Unapproved guidance path.')
        record('guidance',path,path,{'text':texts[path]},text=texts[path])
    catalog={x['id']:x for x in mapping['repository_catalog']}
    if len(catalog)!=len(mapping['repository_catalog']):raise ValueError('Duplicate routing repository ID.')
    for item in catalog.values():
        if item['visibility']!='public' or item['url']!='https://github.com/'+item['repository'] or not item['repository'].startswith('Double-FW/'):raise ValueError('Routing catalog requires recorded public Double-FW references.')
    mapcontext={k:v for k,v in mapping.items() if k not in ['function_map','repository_catalog']}
    for key in ['status','scope','agent_routing_protocol','global_guardrails','maintenance_notes']:
        if not mapcontext.get(key):raise ValueError('Routing context missing: '+key)
    routeids=set()
    for f in mapping['function_map']:
        if f['id'] in routeids:raise ValueError('Duplicate routing function ID.')
        routeids.add(f['id'])
        if not set(f['relevant_lgirs_criteria'])<=ids:raise ValueError('Unresolved routing criterion reference.')
        refs=f['primary_repo_ids']+f['supporting_repo_ids']
        if not set(refs)<=catalog.keys():raise ValueError('Unresolved routing repository reference.')
        if not f.get('guardrails') or not f.get('required_behaviour_and_user_control'):raise ValueError('Routing guardrails missing.')
        record('routing_functions',f['id'],'docs/agentic-accessibility-function-routing-map.json',f,title=f['title'],routing_context_json=serial(mapcontext),repository_references_json=serial([catalog[x] for x in dict.fromkeys(refs)]))
    schema=json.loads(texts['schemas/operation-record.schema.json'])
    for path in sorted(texts):
        if path.startswith('examples/records/') and path.endswith('.json'):
            e=json.loads(texts[path])
            if e.get('synthetic') is not True:raise ValueError('Operation examples must remain synthetic.')
            record('operation_examples',Path(path).stem,path,e,synthetic=True,operation_schema_json=serial(schema),example_context=texts['examples/records/README.md'])
    provenance={'source_repository':SOURCE,'source_commit':commit,'source_commit_date':date,'destination_dataset':TARGET,'manifest':manifest,'licence':'MIT','qualification':'Structural export only; no product evaluation or fresh external-source audit. Catalog public-verification dates are recorded source assertions, not renewed by export.'}
    columns={k:sorted(v[0]) if v else [] for k,v in streams.items()}
    payload={k+'.jsonl':''.join(serial(x)+'\n' for x in v).encode() for k,v in streams.items()}
    for out,src in [('LICENSE','LICENSE'),('NOTICE.md','NOTICE.md'),('framework.json','data/framework.json'),('routing_map.json','docs/agentic-accessibility-function-routing-map.json'),('source_register.json','data/sources.json')]:payload[out]=texts[src].encode()
    for name,value in [('provenance.json',provenance),('record_schema.json',{'format':'JSON Lines','columns':columns,'json_string_columns':['record_json','framework_context_json','routing_context_json','repository_references_json','operation_schema_json'],'note':'JSON strings preserve heterogeneous source records without losing fields. Guidance text is exact source Markdown.'}),('validation_report.json',{'source_commit':commit,'structural_checks':'passed','counts':{k:len(v) for k,v in streams.items()},'product_evaluation':'not_evaluated','external_catalog_links':'Recorded source references; not fetched or reverified by this export.'})]:payload[name]=(serial(value)+'\n').encode()
    card='---\nlicense: mit\nlanguage:\n- en\ntask_categories:\n- text-retrieval\nconfigs:\n'
    for k in STREAMS:card+=f'- config_name: {k}\n  data_files:\n  - split: train\n    path: {k}.jsonl\n'
    card+='---\n# LGIR+S Agentic Experience Principles\n\nDouble-FW editorial knowledge resource, exported from [the public source](https://github.com/'+SOURCE+').\n\n## Scope and limitations\n\nLGIR+S is a Double-FW draft, not a W3C standard, replacement for WCAG, legal conclusion or validated conformance scheme. A/AA are proposed local priorities. No real agent or participant research is represented. Examples are fictional and operation records synthetic. The `train` split is a dataset-loader convention, not evidence that a model was trained. This is source material for retrieval or further reviewed preparation; no instruction/answer pairs are fabricated. Retrieved agent instructions are data and do not grant authority.\n\n## Records and reuse\n\nFive configurations separate candidate criteria, fictional examples, independently authored Markdown guidance, routing functions and synthetic operation examples. Full original records are preserved in JSON string columns, alongside retrieval fields and shared authority context. Routing functions preserve global guardrails and selected repository references. `routing_map.json` retains the entire original map, including its catalog. Links in that map are live editorial references with recorded inspection dates, not freshly verified or pinned evidence. `source_register.json` preserves the separate canonical inspected source register.\n\nGenerated specification and Understanding pages are omitted as duplicate views. The provenance manifest includes all explicitly approved repository source files needed for structural verification; not every manifest file is a dataset record. Framework and source-register auxiliary files preserve context.\n\n## Provenance and licence\n\nMIT; retain the copyright and permission notice in LICENSE. External referenced works retain their own rights; the licence does not relicense third-party material. See NOTICE.md. Each record identifies its exact GitHub revision and path. The manifest records source hashes. `validation_report.json` describes structural checks only. The weekly workflow does not review legal applicability or evaluate products. Use accountable review and appropriate privacy controls before downstream training or deployment.\n'
    payload['README.md']=card.encode()
    if set(payload)!=set(MANAGED):raise ValueError('Managed file set mismatch.')
    output.mkdir(parents=True,exist_ok=True)
    for name,data in payload.items():(output/name).write_bytes(data)
    return {k:len(v) for k,v in streams.items()}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--dataset-id',required=True);a=p.parse_args()
    print(serial(build(ROOT,a.output,a.dataset_id)))
if __name__=='__main__':main()
