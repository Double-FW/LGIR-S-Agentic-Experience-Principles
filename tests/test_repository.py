import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from check_repository import check,operation_errors

class RepositoryIntegrity(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)/'repo'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('__pycache__','.git'))
    def tearDown(self):self.temp.cleanup()
    def change(self,path,fn):
        p=self.root/path;d=json.loads(p.read_text());fn(d);p.write_text(json.dumps(d))
    def test_valid_package(self):self.assertEqual([],check(self.root))
    def test_missing_satisfactory_is_detected(self):
        self.change('data/framework.json',lambda d:d['principles'].pop())
        self.assertTrue(any('Five principle' in e for e in check(self.root)))
    def test_empty_principle_list_reports_an_error(self):
        self.change('data/framework.json',lambda d:d.update(principles=[]))
        self.assertTrue(any('Five principle' in e for e in check(self.root)))
    def test_owner_definition_cannot_drift(self):
        self.change('data/framework.json',lambda d:d.update(robust_definition='A different definition'))
        self.assertTrue(any('Owner definition changed' in e for e in check(self.root)))
    def test_dangling_source_is_detected(self):
        self.change('data/criteria.json',lambda d:d['criteria'][0].update(source_ids=['NONEXISTENT']))
        self.assertTrue(any('dangling source' in e for e in check(self.root)))
    def test_false_evaluation_is_detected(self):
        self.change('data/criteria.json',lambda d:d['criteria'][0].update(product_evaluation_status='passed'))
        self.assertTrue(any('falsely promoted' in e for e in check(self.root)))
    def test_local_tiers_cannot_become_wcag_conformance(self):
        self.change('data/criteria.json',lambda d:d['criteria'][0].update(tier_status='WCAG Level A compliant'))
        self.assertTrue(any('priority falsely promoted' in e for e in check(self.root)))
    def test_case_cannot_become_real_evidence(self):
        self.change('data/examples.json',lambda d:d['EX01'].update(fictional=False))
        self.assertTrue(any('fictional case falsely promoted' in e for e in check(self.root)))
    def test_stale_understanding_view_is_detected(self):
        p=self.root/'understanding/lgirs-1-1.md';p.write_text(p.read_text()+'\nChanged only here.\n')
        self.assertTrue(any('Stale generated' in e for e in check(self.root)))
    def test_broken_local_link_is_detected(self):
        p=self.root/'README.md';p.write_text(p.read_text()+'\n[Missing](missing.md)\n')
        self.assertTrue(any('missing local target' in e for e in check(self.root)))
    def test_unknown_outcome_cannot_claim_safe_retry(self):
        self.change('examples/records/timeout-unknown.json',lambda d:d.update(retry_policy='allowed_with_verified_idempotency'))
        self.assertTrue(any('Unknown outcome' in e for e in check(self.root)))
    def test_irreversible_effect_cannot_claim_undo(self):
        self.change('examples/records/irreversible-send.json',lambda d:d.update(can_undo=True))
        self.assertTrue(any('Undo contradicts' in e for e in check(self.root)))
    def test_completion_requires_effect_evidence(self):
        self.change('examples/records/reconciled-completion.json',lambda d:d.update(evidence=[]))
        self.assertTrue(any('Completed operation lacks' in e for e in check(self.root)))

if __name__=='__main__':unittest.main()
