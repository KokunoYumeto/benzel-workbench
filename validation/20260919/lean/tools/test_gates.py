#!/usr/bin/env python3
"""Regression checks for the handoff's reporting and axiom-policy gate."""
from __future__ import annotations
import json,sys,unittest
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from lean_check import strip_comments,audit_axioms,static_checks
from check_generated_data import Parser
class GateTests(unittest.TestCase):
 def test_nested_comments(self):
  self.assertEqual(strip_comments('theorem x /- outer /- inner -/ sorry -/ : True := by trivial').split(),
    ['theorem','x',':','True',':=','by','trivial'])
 def test_complete_allowed_report(self):
  got=audit_axioms("'Benzel.x' depends on axioms: [propext, Classical.choice, Quot.sound]\n",['Benzel.x'])
  self.assertEqual(len(got['Benzel.x']),3)
 def test_no_axioms_report(self):
  self.assertEqual(audit_axioms("'Benzel.x' does not depend on any axioms\n",['Benzel.x']),{'Benzel.x':[]})
 def test_reject_proof_escape(self):
  with self.assertRaises(ValueError):audit_axioms("'Benzel.x' depends on axioms: [sorryAx]\n",['Benzel.x'])
 def test_reject_missing_target(self):
  with self.assertRaises(ValueError):audit_axioms("'Benzel.x' does not depend on any axioms\n",['Benzel.x','Benzel.y'])
 def test_reject_duplicate(self):
  with self.assertRaises(ValueError):audit_axioms("'Benzel.x' does not depend on any axioms\n"*2,['Benzel.x'])
 def test_reject_extra_target(self):
  with self.assertRaises(ValueError):audit_axioms("'Benzel.x' does not depend on any axioms\n'Benzel.y' does not depend on any axioms\n",['Benzel.x'])
 def test_original_literal(self):
  self.assertEqual(Parser('⟨.vertical, ⟨0, 3, 1, (-2)⟩, ⟨(-1), 0, 1, 0⟩⟩').all(),('V',(0,3,1,-2),(-1,0,1,0)))
 def test_reject_bad_literal(self):
  with self.assertRaises(ValueError):Parser('⟨.left, 0, 0⟩').all()
 def test_task_graph(self):
  tasks=json.loads((ROOT/'TASKS.json').read_text())['tasks'];ids={t['id']for t in tasks};seen=set()
  self.assertEqual(len(ids),len(tasks))
  for t in tasks:
   self.assertTrue(set(t['depends_on'])<=seen)
   self.assertEqual(t['status'],'OPEN');seen.add(t['id'])
 def test_current_scaffold_state(self):
  s=json.loads((ROOT/'STATUS.json').read_text())
  self.assertEqual(s['new_kernel_checked_declarations'],0)
  self.assertFalse((ROOT/'formal/Benzel/Final.lean').exists())
 def test_specification_lock(self):
  self.assertEqual(static_checks()['status'],'PASS')
if __name__=='__main__':unittest.main(verbosity=2)
