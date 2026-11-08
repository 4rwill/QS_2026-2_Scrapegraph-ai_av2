"""Bounded AV3 execution; final run requires recorded human reference review."""
import argparse
import csv
import hashlib
import importlib.util
import json
import random
import shutil
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

from metrics import lexical_f1

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parent
AV2 = ROOT / "atividade2"


def now():
    return datetime.now(timezone(timedelta(hours=-3))).isoformat()


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as f:
        json.dump(value, f, ensure_ascii=False, indent=2)


def write_csv(path, rows, fields):
    with path.open("x", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def case_hash(case):
    return hashlib.sha256(json.dumps(case, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def review_gate(cases, path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 6 or {r["case_id"] for r in rows} != {c["id"] for c in cases}:
        raise ValueError("Reference review must contain each of the six cases once")
    for case in cases:
        row = next(r for r in rows if r["case_id"] == case["id"])
        if (row["status"] != "aprovado" or row["reference_sha256"] != case_hash(case)
                or not all(row[k].strip() for k in ("revisor", "data", "justificativa"))):
            raise ValueError(f"{case['id']}: human reference review pending or stale")


def av2_module():
    spec = importlib.util.spec_from_file_location("av2_worker", AV2 / "scripts/evaluate.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def environment():
    result = av2_module().preflight()
    result["repository_commit"] = subprocess.check_output(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip()
    result["system_commit"] = subprocess.check_output(
        ["git", "-C", str(ROOT / "Scrapegraph-ai"), "rev-parse", "HEAD"], text=True).strip()
    return result


def compatible(env, config):
    models = env.get("tags", {}).get("models", [])
    return (env["ready"] and env["system_commit"] == config["expected_system_commit"]
            and any(m.get("name") == "llama3.2:latest" and
                    m.get("digest") == config["expected_model_digest"] for m in models))


def validate_inputs(cases):
    if [c["id"] for c in cases] != [f"CT{i:02d}" for i in range(1, 7)]:
        raise ValueError("Expected CT01..CT06 in order")
    for case in cases:
        lexical_f1(None, case["reference"])
        source = BASE / "data" / (case["source"] + ".html")
        if not source.is_file():
            raise ValueError(f"Missing source: {source}")
        source_hash = hashlib.sha256(source.read_text(encoding="utf-8").encode()).hexdigest()
        if source_hash != case["source_sha256"]:
            raise ValueError(f"{case['id']}: source changed; update and review the reference again")


def snapshot(folder):
    files = [AV2 / "scripts/evaluate.py", AV2 / "tests/schema.json"]
    for pattern in ("data/*", "versions/*/*", "scripts/*.py", "tests/*.py", "docs/*.md", "config.json"):
        files.extend(BASE.glob(pattern))
    hashes = {}
    for source in sorted(set(files)):
        if source.is_file():
            rel = source.relative_to(ROOT)
            target = folder / "snapshot" / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            hashes[rel.as_posix()] = hashlib.sha256(source.read_bytes()).hexdigest()
    save(folder / "snapshot-hashes.json", hashes)
    return hashes


def packets(folder, rows, cases):
    shuffled = rows[:]
    random.SystemRandom().shuffle(shuffled)
    mapping = [{"blind_id": f"S{i:02d}", "case_id": r["case_id"], "version": r["version"],
                "output": r["output"]} for i, r in enumerate(shuffled, 1)]
    save(folder / "private-mapping.json", mapping)
    fields = ["blind_id", "avaliador", "data", "correcao", "relevancia", "suporte", "falha_critica", "justificativa", "exposicao_previa"]
    for role in ("R1", "R2"):
        directory = folder / role
        directory.mkdir()
        selected = [m for m in mapping if role == "R1" or m["case_id"] in ("CT01", "CT05")]
        write_csv(directory / "annotations.csv", [{k: m["blind_id"] if k == "blind_id" else "" for k in fields} for m in selected], fields)
        text = [f"# Pacote {role}\n\nAvaliar individualmente antes de conversar. Não consultar private-mapping.json, automatic.csv ou o pacote do outro avaliador.\n\nPreencher annotations.csv; notas 0/1/2, falha crítica 0/1. Seguir a rubrica anexada. Notas humanas não devem ser preenchidas por IA.\n"]
        for m in selected:
            case = next(c for c in cases if c["id"] == m["case_id"])
            response = read(folder / m["output"])
            failed = ("environment_or_runtime_error" in response or "graph_error" in response or "answer" not in response
                      or (folder / Path(m["output"]).parent / "timeout.json").exists())
            answer = "[FALHA DE EXECUÇÃO: SEM SAÍDA UTILIZÁVEL]" if failed else json.dumps(response["answer"], ensure_ascii=False, indent=2)
            source = (folder / "snapshot/atividade3/data" / (case["source"] + ".html")).read_text(encoding="utf-8")
            text.append(f"\n## {m['blind_id']} — {case['id']}\n\nPergunta: {case['question']}\n\nFonte: {case['source']}\n```html\n{source}\n```\nReferência (consultar estado da revisão humana no plano do lote):\n```json\n{json.dumps(case['reference'], ensure_ascii=False, indent=2)}\n```\nResposta observada:\n```text\n{answer}\n```\n")
        (directory / "packet.md").write_text("\n".join(text), encoding="utf-8")
        # The detailed protocol reveals the intervention; provide only the rubric.
        protocol = (BASE / "docs/protocol.md").read_text(encoding="utf-8")
        rubric = protocol.split("## Rubrica humana e falha crítica\n", 1)[1].split("## Regra de decisão", 1)[0]
        (directory / "rubric.md").write_text("# Rubrica\n" + rubric, encoding="utf-8")
    consensus_fields = fields + ["participantes"]
    write_csv(folder / "consensus.csv", [], consensus_fields)


def run(mode):
    config, cases = read(BASE / "config.json"), read(BASE / "data/cases.json")
    validate_inputs(cases)
    references_reviewed = False
    try:
        review_gate(cases, BASE / "data/reference-review.csv")
        references_reviewed = True
    except ValueError:
        if mode == "final":
            raise
    if mode == "final":
        review_gate(cases, BASE / "data/reference-review.csv")
    env = environment()
    stamp = datetime.now().strftime("%Y%m%dT%H%M%S%f")
    if not compatible(env, config):
        path = BASE / "results" / f"{stamp}-blocked.json"
        save(path, env)
        raise ValueError(f"Environment unavailable or differs from plan; evidence: {path}")
    folder = BASE / "results" / f"{stamp}-{mode}"
    folder.mkdir()
    save(folder / "environment-before.json", env)
    hashes = snapshot(folder)
    jobs = [(c, v) for i, c in enumerate(cases) for v in (("A", "B") if i % 2 == 0 else ("B", "A"))]
    if mode == "pilot":
        jobs = jobs[:1]
    save(folder / "plan.json", dict(mode=mode, created_at=now(), tau=config["tau"],
        jobs=[dict(case_id=c["id"], version=v) for c, v in jobs], references_human_reviewed=references_reviewed,
        methodological_deviation="Referências sem revisão humana prévia; lote completo provisório, pendente de validação acadêmica." if mode == "provisional" and not references_reviewed else None))
    for version in ("A", "B"):
        manifest = read(BASE / f"versions/{version}/manifest.json")
        manifest.update(mode=mode, created_at=now(), state="execução planejada; consultar completion.json",
                        environment=env, configuration=config, snapshot_hashes=hashes,
                        results=[f"{v}-{c['id']}/response.json" for c, v in jobs if v == version])
        save(folder / f"manifest-{version}.json", manifest)
    rows = []
    all_configs_match = True
    for case, version in jobs:
        path = folder / f"{version}-{case['id']}"
        frozen = folder / "snapshot/atividade3"
        context = (frozen / "data" / (case["source"] + ".html")).read_text(encoding="utf-8")
        prompt = (frozen / f"versions/{version}/prompt.md").read_text(encoding="utf-8")
        prompt += f"\nPergunta: {case['question']}\nFonte identificada como: {case['source']}"
        request = dict(case_id=case["id"], version=version, prompt=prompt, context=context,
                       time=now(), source=case["source"], mode=mode)
        save(path / "request.json", request)
        try:
            proc = subprocess.run([sys.executable, str(folder / "snapshot/atividade2/scripts/evaluate.py"), "worker", "--job", str(path / "request.json")],
                capture_output=True, encoding="utf-8", errors="replace", timeout=config["timeout_seconds"])
            (path / "process.log").write_text(proc.stdout + "\n" + proc.stderr, encoding="utf-8")
            if not (path / "response.json").exists():
                save(path / "response.json", dict(environment_or_runtime_error=f"worker exit {proc.returncode}"))
        except subprocess.TimeoutExpired as exc:
            def decoded(value):
                return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else value or ""
            (path / "process.log").write_text(decoded(exc.stdout) + "\n" + decoded(exc.stderr), encoding="utf-8")
            # Preserve any partial response from the worker instead of replacing it.
            save(path / "timeout.json", dict(error="timeout", seconds=config["timeout_seconds"], retry=False))
            if not (path / "response.json").exists():
                save(path / "response.json", dict(environment_or_runtime_error="timeout; no automatic retry"))
        response = read(path / "response.json")
        failed = ("answer" not in response or "graph_error" in response or
                  "environment_or_runtime_error" in response or (path / "timeout.json").exists())
        checks = lexical_f1(None if failed else response["answer"], case["reference"])
        config_ok = response.get("config") == config["config"] if not failed else True
        all_configs_match = all_configs_match and config_ok
        row = dict(case_id=case["id"], version=version, **checks, automatic_approved=checks["f1"] >= config["tau"],
                   runtime_status="falha" if failed else "resposta", config_matches=config_ok,
                   output=f"{version}-{case['id']}/response.json")
        rows.append(row)
        save(path / "automatic.json", row)
        print(json.dumps({"case": case["id"], "version": version, "runtime_status": row["runtime_status"]}), flush=True)
    after = environment()
    save(folder / "environment-after.json", after)
    stable = compatible(after, config) and after.get("version") == env.get("version") and all_configs_match
    save(folder / "completion.json", dict(time=now(), mode=mode, records=len(rows),
        successful_responses=sum(r["runtime_status"] == "resposta" for r in rows),
        conditions_comparable=stable, final_experiment=mode == "final", references_human_reviewed=references_reviewed,
        human_evaluation="pendente"))
    write_csv(folder / "automatic.csv", rows, list(rows[0]))
    save(folder / "automatic.json", rows)
    if mode != "pilot":
        packets(folder, rows, cases)
    print(json.dumps({"run": str(folder.relative_to(ROOT)), "comparable": stable, "records": len(rows)}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["check", "pilot", "provisional", "final"])
    args = parser.parse_args()
    try:
        if args.command == "check":
            cases = read(BASE / "data/cases.json")
            validate_inputs(cases)
            record = dict(time=now(), environment=environment(), cases=6)
            record["environment_matches"] = compatible(record["environment"], read(BASE / "config.json"))
            try:
                review_gate(cases, BASE / "data/reference-review.csv")
                record["references_human_reviewed"] = True
            except ValueError as e:
                record["references_human_reviewed"] = False
                record["blocking_reason"] = str(e)
            path = BASE / "results" / (datetime.now().strftime("%Y%m%dT%H%M%S%f") + "-check.json")
            save(path, record)
            print(json.dumps(record, ensure_ascii=True, indent=2))
        else:
            run(args.command)
    except ValueError as e:
        parser.exit(2, str(e) + "\n")
