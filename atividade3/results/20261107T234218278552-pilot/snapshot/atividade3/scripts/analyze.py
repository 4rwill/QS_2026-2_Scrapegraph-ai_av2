"""Join real human annotations with the automatic signal, preserving originals."""
import argparse
import csv
import html
import json
import shutil
from datetime import datetime
from pathlib import Path

from metrics import approved, decision
from experiment import read, save, write_csv

SCORES = ("correcao", "relevancia", "suporte", "falha_critica")


def annotations(path, expected):
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != len(expected) or {r["blind_id"] for r in rows} != set(expected):
        raise ValueError(f"{path}: missing, duplicate or unexpected blind ID")
    for row in rows:
        for key in SCORES:
            allowed = {"0", "1"} if key == "falha_critica" else {"0", "1", "2"}
            if row[key] not in allowed:
                raise ValueError(f"{path}: {row['blind_id']}: invalid or missing {key}")
        for key in ("avaliador", "data", "justificativa", "exposicao_previa"):
            if not row[key].strip():
                raise ValueError(f"{path}: {row['blind_id']}: fill {key}")
    return {r["blind_id"]: r for r in rows}


def combine(mapping, r1, r2, consensus):
    finals, matches, differences = {}, 0, []
    for item in mapping:
        key = item["blind_id"]
        chosen = r1[key]
        if key in r2:
            if r1[key]["avaliador"].strip().casefold() == r2[key]["avaliador"].strip().casefold():
                raise ValueError("R1 and R2 must be distinct people")
            matches += approved(r1[key]) == approved(r2[key])
            if any(r1[key][s] != r2[key][s] for s in SCORES):
                differences.append(key)
                if key not in consensus or not consensus[key].get("participantes", "").strip():
                    raise ValueError(f"{key}: disagreement needs a separate justified consensus")
                chosen = consensus[key]
        finals[key] = chosen
    if set(consensus) != set(differences):
        raise ValueError("Consensus rows must correspond exactly to score/flag disagreements")
    return finals, matches, differences


def analyze(folder):
    completion = read(folder / "completion.json")
    if not completion["final_experiment"] or completion["records"] != 12:
        raise ValueError("Pilot/incomplete run cannot produce final AV3 metrics")
    if not completion["conditions_comparable"]:
        raise ValueError("Conditions changed; investigate before a final comparison")
    mapping = read(folder / "private-mapping.json")
    rows = read(folder / "automatic.json")
    r1 = annotations(folder / "R1/annotations.csv", [m["blind_id"] for m in mapping])
    r2 = annotations(folder / "R2/annotations.csv", [m["blind_id"] for m in mapping if m["case_id"] in ("CT01", "CT05")])
    if len({r["avaliador"].strip().casefold() for r in r1.values()}) != 1 or len({r["avaliador"].strip().casefold() for r in r2.values()}) != 1:
        raise ValueError("Protocol expects one main evaluator and one second evaluator")
    differences = [k for k in r2 if any(r1[k][s] != r2[k][s] for s in SCORES)]
    consensus = annotations(folder / "consensus.csv", differences)
    finals, matches, differences = combine(mapping, r1, r2, consensus)
    table = []
    for row in sorted(rows, key=lambda r: (r["case_id"], r["version"])):
        item = next(m for m in mapping if (m["case_id"], m["version"]) == (row["case_id"], row["version"]))
        key = item["blind_id"]
        final = finals[key]
        table.append({**row, "blind_id": key, **{s: final[s] for s in SCORES},
            "human_approved": approved(final), "human_basis": "consenso" if key in consensus else "R1+R2" if key in r2 else "somente R1",
            "justificativa": final["justificativa"]})
    metrics = {"versions": {}, "automatic_human_agreement": {"numerator": sum(r["automatic_approved"] == r["human_approved"] for r in table), "denominator": 12},
        "r1_r2_agreement_before_consensus": {"numerator": matches, "denominator": 4},
        "score_disagreements": differences, "limitations": ["CT06 relacionado a CT01", "oito decisões somente R1", "uma execução por condição", "cegamento limitado; consultar exposicao_previa"]}
    for v in ("A", "B"):
        selected = [r for r in table if r["version"] == v]
        metrics["versions"][v] = dict(mean_f1=sum(r["f1"] for r in selected) / 6,
            human_approved=sum(r["human_approved"] for r in selected), denominator=6)
    metrics["decision"] = decision([r for r in table if r["version"] == "A"], [r for r in table if r["version"] == "B"])
    metrics["automatic_human_disagreements"] = [dict(case_id=r["case_id"], version=r["version"], output=r["output"], justification=r["justificativa"]) for r in table if r["automatic_approved"] != r["human_approved"]]
    out = folder / ("analysis-" + datetime.now().strftime("%Y%m%dT%H%M%S%f"))
    out.mkdir()
    save(out / "metrics.json", metrics)
    write_csv(out / "consolidated.csv", table, list(table[0]))
    for source in ("R1/annotations.csv", "R2/annotations.csv", "consensus.csv"):
        target = out / "annotations-snapshot" / source
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(folder / source, target)
    visual = ['<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>AV3 — resultados</title><style>body{font:16px Arial;max-width:1100px;margin:40px auto}table{border-collapse:collapse;width:100%}td,th{padding:12px;border-bottom:1px solid #ddd;text-align:left}meter{width:160px}</style><h1>AV3 — F1 lexical e decisão humana</h1><p>12 saídas; tau=0,5. Notas humanas: correção / relevância / suporte. CT06 é relacionado a CT01.</p><table><tr><th>Caso/versão</th><th>F1</th><th>Auto</th><th>Notas</th><th>Humano</th><th>Justificativa</th></tr>']
    for r in table:
        visual.append(f'<tr><td>{r["case_id"]}/{r["version"]}</td><td><meter min="0" max="1" value="{r["f1"]}"></meter> {r["f1"]:.3f}</td><td>{r["automatic_approved"]}</td><td>{r["correcao"]}/{r["relevancia"]}/{r["suporte"]}</td><td>{r["human_approved"]}</td><td>{html.escape(r["justificativa"])}</td></tr>')
    visual.append('</table><p>' + html.escape(metrics["decision"]) + '</p></html>')
    (out / "comparison.html").write_text("\n".join(visual), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("run", type=Path)
    args = parser.parse_args()
    try:
        analyze(args.run)
    except ValueError as e:
        parser.exit(2, str(e) + "\n")
