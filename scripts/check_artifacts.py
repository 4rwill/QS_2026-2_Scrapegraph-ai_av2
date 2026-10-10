"""Check frozen fixtures, planned categories and preservation of source clones."""
import csv
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'data/manifest.json').read_text())
for name,entry in manifest.items():
    assert hashlib.sha256((ROOT/entry['file']).read_bytes()).hexdigest()==entry['sha256'],name
rows=list(csv.DictReader((ROOT/'tests/cases.csv').open(encoding='utf-8')))
assert len({r['id'] for r in rows})==10
assert Counter(r['categoria'] for r in rows)=={'funcional':3,'contexto':2,'metamórfico':2,'adversarial':2,'saída':1}
for repo in ['Scrapegraph-ai','QS_2026-2_Scrapegraph-ai']:
    if (ROOT/repo/'.git').exists():
        assert not subprocess.check_output(['git','-C',str(ROOT/repo),'status','--porcelain'],text=True),repo
for file in ['docs/status.md','docs/repositories.md','docs/manual-checklist.md','docs/report.md','docs/threats.csv','prompts/P1-direct.md','prompts/P2-structured.md','prompts/P3-few-shot.md']:
    assert (ROOT/file).is_file(),file
print('PASS: fixture hashes; 10 planned cases and categories; present source clones clean; required evaluation artifacts')
