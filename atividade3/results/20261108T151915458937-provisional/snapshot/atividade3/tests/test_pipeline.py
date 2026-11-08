"""Synthetic controls of the evaluator; not experimental/model results."""
import csv
import json
import sys
import unittest
import uuid
from contextlib import contextmanager
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from metrics import lexical_f1, approved, decision
from experiment import BASE, case_hash, review_gate, read, validate_inputs, packets, save, write_csv
from analyze import annotations, combine, analyze
import shutil


@contextmanager
def workspace_temp():
    # Windows sandbox can deny access to tempfile's private (0700) directories.
    parent = (BASE / "tests").resolve()
    path = parent / ("test-tmp-" + uuid.uuid4().hex)
    path.mkdir()
    try:
        yield path
    finally:
        if path.resolve().parent != parent:
            raise ValueError("Unsafe test cleanup path")
        shutil.rmtree(path)


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
        with workspace_temp() as tmp:
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
        with workspace_temp() as tmp:
            path = Path(tmp) / "notes.csv"
            path.write_text("blind_id,correcao,relevancia,suporte,falha_critica\nS01,,,,\n", encoding="utf-8")
            with self.assertRaises(ValueError): annotations(path, ["S01"])

    def test_synthetic_end_to_end_packets_and_analysis(self):
        # All identities and ratings here are synthetic controls, kept temporary.
        with workspace_temp() as path:
            cases = read(BASE / "data/cases.json")
            rows = []
            for case in cases:
                source = path / "snapshot/atividade3/data" / (case["source"] + ".html")
                source.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(BASE / "data" / source.name, source)
                for version in ("A", "B"):
                    output = f"{version}-{case['id']}/response.json"
                    save(path / output, {"answer": case["reference"]})
                    rows.append(dict(case_id=case["id"], version=version, f1=1.0,
                                     automatic_approved=True, output=output))
            packets(path, rows, cases)
            save(path / "completion.json", dict(final_experiment=True, records=12, conditions_comparable=True))
            save(path / "automatic.json", rows)
            for role, count in (("R1", 12), ("R2", 4)):
                file = path / role / "annotations.csv"
                with file.open(encoding="utf-8", newline="") as f:
                    values = list(csv.DictReader(f))
                self.assertEqual(len(values), count)
                for row in values:
                    row.update(human(name="Controle sintético " + role), data="2026-11-07", justificativa="Controle sintético, não avaliação humana", exposicao_previa="controle automatizado")
                file.unlink()
                write_csv(file, values, list(values[0]))
                packet = (path / role / "packet.md").read_text(encoding="utf-8")
                self.assertNotIn('"f1"', packet)
                self.assertNotIn('version', packet)
            analyze(path)
            result = read(next(path.glob("analysis-*/metrics.json")))
            self.assertEqual(result["automatic_human_agreement"], {"numerator": 12, "denominator": 12})
            self.assertEqual(result["r1_r2_agreement_before_consensus"], {"numerator": 4, "denominator": 4})
            self.assertIn("manter A", result["decision"])


if __name__ == "__main__":
    unittest.main()
