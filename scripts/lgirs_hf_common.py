"""Committed-source and fixed-destination rules for terminology publication."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
SOURCE='Double-FW/LGIR-S-Agentic-Experience-Principles'
TARGET='GarethFW/LGIR-S_Agentic_Experience_Principles'
MANAGED=('README.md', 'LICENSE', 'NOTICE.md', 'criteria.jsonl', 'examples.jsonl', 'guidance.jsonl', 'routing_functions.jsonl', 'operation_examples.jsonl', 'framework.json', 'routing_map.json', 'source_register.json', 'provenance.json', 'record_schema.json', 'validation_report.json')
CONFIG='huggingface/export-config.json'

def digest(data):return hashlib.sha256(data).hexdigest()
def git(root,*args):return subprocess.check_output(['git','-C',str(root),*args])
def destination(value):
    if value!=TARGET:raise ValueError('HF_DATASET_ID must be '+TARGET+'.')
    return value

def committed(root,path):
    p=PurePosixPath(path)
    if p.is_absolute() or '..' in p.parts or any(x.startswith('.') for x in p.parts):raise ValueError('Invalid approved source path: '+path)
    info=git(root,'ls-tree','HEAD','--',path).decode().strip()
    if not info.startswith('100644 blob '):raise ValueError('Required source must be a committed regular file: '+path)
    sha=info.split()[2];data=git(root,'cat-file','blob',sha)
    if hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()!=sha:raise ValueError('Git source integrity failed: '+path)
    return data,{'path':path,'git_blob_sha':sha,'sha256':digest(data),'size_bytes':len(data)}

def read_sources(root=ROOT):
    raw,entry=committed(root,CONFIG);cfg=json.loads(raw)
    if cfg['source_repository']!=SOURCE:raise ValueError('Wrong source repository in export configuration.')
    destination(cfg['destination_dataset'])
    paths=cfg['source_files']
    if not isinstance(paths,list) or len(paths)!=len(set(paths)) or not all(isinstance(p,str) for p in paths):raise ValueError('Source allowlist must contain unique paths.')
    required={'data/framework.json','data/criteria.json','data/examples.json','data/sources.json','AGENTS.md','README.md','STATUS.md','LICENSE','NOTICE.md','docs/agentic-accessibility-function-routing-map.json','schemas/operation-record.schema.json'}
    if not required<=set(paths):raise ValueError('Required canonical sources and authority context must remain included.')
    texts={};manifest=[entry]
    for path in paths:
        data,e=committed(root,path);text=data.decode('utf-8')
        if any(x in text for x in ['chatgpt.com/library?','account_id=personal','file_id=libfile_']):raise ValueError('Personal source-access locator in public export: '+path)
        texts[path]=text;manifest.append(e)
        working=Path(root)/path
        if not working.is_file() or working.is_symlink() or working.read_bytes()!=data:raise ValueError('Working source differs from the committed snapshot: '+path)
    if digest(texts['LICENSE'].encode())!=cfg['approved_license_sha256']:raise ValueError('Licence bytes changed; review before publication.')
    return cfg,texts,manifest

def public_source():
    request=urllib.request.Request('https://api.github.com/repos/'+SOURCE,headers={'User-Agent':'Double-FW-terminology-dataset-sync'})
    with urllib.request.urlopen(request,timeout=30) as response:info=json.load(response)
    if info.get('full_name')!=SOURCE or info.get('private') is not False or info.get('visibility')!='public':raise ValueError('Publishing requires the approved public GitHub source.')
