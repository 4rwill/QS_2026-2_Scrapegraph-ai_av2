"""Synthetic controls of the evaluator; not experimental/model results."""
import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from metrics import lexical_f1, approved, decision
from experiment import BASE, case_hash, review_gate, read, validate_inputs
from analyze import annotations, combine


def human(c=2, r=2, s=2, critical=0, name="R1 pessoa"):
    return dict(correcao=str(c), relevancia=str(r), suporte=str(s), falha_critica=str(critical), avaliador=name)


class PipelineTests(unittest.TestCase):
    def test_multiset_and_empty(self):
        result = lexical_f1("a a b", "a b b")
        self.assertAlmostEqual(result["f1"], 2 / 3)
        self.assertEqual(lexical_f1("", "referência")["f1"], 0)
        self.assertEqual(lexical_f1("x", "y")["f1"], 0)

    def test_normalization(self):
        self.assertEqual(lexical_f1("CAFÉ", "cafe\u0301")["f1"], 1)

    def test_empty_reference_rejected(self):
        with self.assertRaises(ValueError):
            lexical_f1("resposta", "...")

    def test_lexical_is_not_fact_check(self):
        self.assertGreaterEqual(lexical_f1("Produto Aurora custa 999 reais", "Produto Aurora custa 10 reais")["f1"], .5)

    def test_strict_human_approval(self):
        self.assertTrue(approved(human()))
        self.assertFalse(approved(human(s=1)))
        self.assertFalse(approved(human(critical=1)))

    def test_decision_regression_and_critical(self):
        a, b = [human()] * 6, [human()] * 6
        self.assertIn("manter A", decision(a, b))
        self.assertIn("regressão", decision(a, [human(s=1)] + b[1:]))
        self.assertIn("falha crítica", decision(a, [human(critical=1)] + b[1:]))
        self.assertIn("próxima etapa", decision([human(s=1)] + a[1:], b))

    def test_real_inputs_and_reference_gate(self):
        cases = read(BASE / "data/cases.json")
        validate_inputs(cases)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "reviews.csv"
            fields = ["case_id", "reference_sha256", "revisor", "data", "status", "justificativa"]
            rows = [dict(zip(fields, [c["id"], case_hash(c), "Pessoa fictícia de teste", "2026-11-07", "aprovado", "Controle sintético"])) for c in cases]
            def write():
                with path.open("w", encoding="utf-8", newline="") as f:
                    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
            write(); review_gate(cases, path)
            rows[0]["status"] = "pendente"; write()
            with self.assertRaises(ValueError): review_gate(cases, path)
            rows[0]["status"] = "aprovado"; rows[0]["reference_sha256"] = "stale"; write()
            with self.assertRaises(ValueError): review_gate(cases, path)

    def test_no_consensus_overwrite(self):
        mapping = [dict(blind_id="S01")]
        r1, r2 = {"S01": human()}, {"S01": human(s=1, name="R2 pessoa")}
        with self.assertRaises(ValueError): combine(mapping, r1, r2, {})
        consensus = {"S01": {**human(s=1), "participantes": "R1 e R2"}}
        finals, matches, differences = combine(mapping, r1, r2, consensus)
        self.assertEqual(matches, 0)
        self.assertEqual(differences, ["S01"])
        self.assertEqual(r1["S01"]["suporte"], "2")
        self.assertEqual(finals["S01"]["suporte"], "1")

    def test_blank_annotations_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "notes.csv"
            path.write_text("blind_id,correcao,relevancia,suporte,falha_critica\nS01,,,,\n", encoding="utf-8")
            with self.assertRaises(ValueError): annotations(path, ["S01"])


if __name__ == "__main__":
    unittest.main()
