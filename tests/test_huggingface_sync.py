import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from export_huggingface import build
from publish_huggingface import publish
from lgirs_hf_common import MANAGED,SOURCE,TARGET
from huggingface_hub.errors import EntryNotFoundError

class FakeHub:
    def __init__(self,root):self.files={'.gitattributes':b'preserve me','unrelated.md':b'preserve me too'};self.parent='destination-parent';self.commits=[];self.root=root;self.reject_concurrent=False
    def repo_info(self,**kwargs):return SimpleNamespace(sha=self.parent)
    def download(self,filename,**kwargs):
        if filename not in self.files:raise EntryNotFoundError('Missing test file')
        path=self.root/'old'/filename;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(self.files[filename]);return str(path)
    def create_commit(self,**kwargs):
        if self.reject_concurrent or kwargs['parent_commit']!=self.parent:raise RuntimeError('Concurrent destination change')
        self.commits.append(kwargs)
        for op in kwargs['operations']:self.files[op.path_in_repo]=op.path_or_fileobj
        self.parent='next-destination-parent'

class LGIRSExport(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.work=Path(self.tmp.name);self.root=self.work/'source';self.output=self.work/'export'
        subprocess.run(['git','clone','--quiet','--no-hardlinks',str(ROOT),str(self.root)],check=True)
    def tearDown(self):self.tmp.cleanup()
    def rows(self,name):return [json.loads(l) for l in (self.output/name).read_text().splitlines()]
    def preview(self):return build(self.root,self.output)
    def publish(self,hub,**kw):return publish(self.output,'test-token-not-a-real-credential',source_root=self.root,api=hub,download=hub.download,check_public=lambda:None,**kw)
    def commit(self):
        subprocess.run(['git','-C',str(self.root),'-c','user.name=Test','-c','user.email=test@example.invalid','add','-A'],check=True)
        subprocess.run(['git','-C',str(self.root),'-c','user.name=Test','-c','user.email=test@example.invalid','commit','-qm','Fixture change'],check=True)
    def test_all_criteria_keep_full_record_and_status(self):
        counts=self.preview();original=json.loads((self.root/'data/criteria.json').read_text())['criteria']
        self.assertEqual(original,[json.loads(r['record_json']) for r in self.rows('criteria.jsonl')]);self.assertEqual(25,counts['criteria'])
        for r in self.rows('criteria.jsonl'):
            self.assertEqual('not_evaluated',r['product_evaluation_status']);self.assertIn('agent_instructions_as_source_data',json.loads(r['framework_context_json']))
    def test_examples_are_fictional_and_operation_examples_synthetic(self):
        counts=self.preview();self.assertEqual(8,counts['examples']);self.assertEqual(4,counts['operation_examples'])
        for r in self.rows('examples.jsonl'):self.assertTrue(r['fictional']);self.assertEqual('not_evaluated',r['evaluation_status'])
        for r in self.rows('operation_examples.jsonl'):self.assertTrue(r['synthetic']);self.assertIn('properties',json.loads(r['operation_schema_json']))
    def test_routing_preserves_all_function_fields_and_global_context(self):
        self.preview();original=json.loads((self.root/'docs/agentic-accessibility-function-routing-map.json').read_text())
        rows=self.rows('routing_functions.jsonl');self.assertEqual(29,len(rows));self.assertEqual(original['function_map'],[json.loads(r['record_json']) for r in rows])
        for r in rows:
            ctx=json.loads(r['routing_context_json']);self.assertEqual(original['global_guardrails'],ctx['global_guardrails']);self.assertEqual(original['maintenance_notes'],ctx['maintenance_notes'])
        self.assertEqual(original,json.loads((self.output/'routing_map.json').read_text()))
    def test_documents_are_exact_and_generated_views_excluded(self):
        self.preview()
        for r in self.rows('guidance.jsonl'):self.assertEqual((self.root/r['source_path']).read_text(),r['text']);self.assertFalse(r['source_path'].startswith('understanding/'))
    def test_unresolved_routing_criterion_stops_export(self):
        p=self.root/'docs/agentic-accessibility-function-routing-map.json';v=json.loads(p.read_text());v['function_map'][0]['relevant_lgirs_criteria'].append('LGIRS-99.99');p.write_text(json.dumps(v));self.commit()
        with self.assertRaisesRegex(ValueError,'routing criterion'):self.preview()
    def test_unresolved_routing_repository_stops_export(self):
        p=self.root/'docs/agentic-accessibility-function-routing-map.json';v=json.loads(p.read_text());v['function_map'][0]['primary_repo_ids'].append('private-unknown');p.write_text(json.dumps(v));self.commit()
        with self.assertRaisesRegex(ValueError,'routing repository'):self.preview()
    def test_same_revision_is_deterministic(self):
        self.preview();other=self.work/'second';build(self.root,other)
        for n in MANAGED:self.assertEqual((self.output/n).read_bytes(),(other/n).read_bytes())
    def test_dirty_canonical_source_stops_export(self):
        p=self.root/'data/criteria.json';p.write_text(p.read_text()+'\n')
        with self.assertRaisesRegex(ValueError,'Working source differs'):self.preview()
    def test_missing_committed_required_source_stops_export(self):
        (self.root/'data/criteria.json').unlink();self.commit()
        with self.assertRaisesRegex(ValueError,'committed regular file'):self.preview()
    def test_changed_licence_stops_export(self):
        p=self.root/'LICENSE';p.write_text(p.read_text()+'\nChanged licence.\n');self.commit()
        with self.assertRaisesRegex(ValueError,'Licence bytes changed'):self.preview()
    def test_wrong_destination_stops_before_publish(self):
        self.preview();hub=FakeHub(self.work)
        with self.assertRaisesRegex(ValueError,'HF_DATASET_ID'):self.publish(hub,dataset_id='GarethFW/wrong')
        self.assertEqual([],hub.commits)
    def test_modified_export_cannot_publish_even_if_report_is_present(self):
        self.preview();p=self.output/'criteria.jsonl';p.write_text(p.read_text()+'\n');hub=FakeHub(self.work)
        with self.assertRaisesRegex(ValueError,'Export bytes differ'):self.publish(hub)
        self.assertEqual([],hub.commits)
    def test_first_publish_is_atomic_and_preserves_other_files(self):
        self.preview();hub=FakeHub(self.work);self.publish(hub)
        self.assertEqual(1,len(hub.commits));self.assertEqual('destination-parent',hub.commits[0]['parent_commit'])
        self.assertEqual(set(MANAGED),{o.path_in_repo for o in hub.commits[0]['operations']});self.assertEqual(b'preserve me',hub.files['.gitattributes'])
    def test_repeat_publish_does_not_clear_historical_report_with_extra_commit(self):
        self.preview();hub=FakeHub(self.work);self.publish(hub);result=self.publish(hub)
        self.assertIn('No changes',result);self.assertEqual(1,len(hub.commits))
    def test_foreign_destination_provenance_is_not_overwritten(self):
        self.preview();hub=FakeHub(self.work);hub.files['provenance.json']=b'{"source_repository":"another/source"}'
        with self.assertRaisesRegex(ValueError,'different source'):self.publish(hub)
        self.assertEqual([],hub.commits)
    def test_concurrent_destination_change_is_not_blindly_retried(self):
        self.preview();hub=FakeHub(self.work);hub.reject_concurrent=True
        with self.assertRaisesRegex(RuntimeError,'Concurrent'):self.publish(hub)
        self.assertEqual([],hub.commits)
    def test_private_source_failure_prevents_destination_write(self):
        self.preview();hub=FakeHub(self.work)
        def private():raise ValueError('Source is private')
        with self.assertRaisesRegex(ValueError,'private'):publish(self.output,'test-token',source_root=self.root,api=hub,download=hub.download,check_public=private)
        self.assertEqual([],hub.commits)
    def test_whitespace_token_is_rejected_without_echoing_it(self):
        self.preview();token=' accidental-sensitive-token\n'
        with self.assertRaises(ValueError) as raised:publish(self.output,token,source_root=self.root,check_public=lambda:None)
        self.assertNotIn(token.strip(),str(raised.exception))

if __name__=='__main__':unittest.main()
