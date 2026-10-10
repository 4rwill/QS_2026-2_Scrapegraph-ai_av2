"""Compute reviewed citation metrics, never treating missing data as zero."""
import csv
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'docs/audit.csv').open(encoding='utf-8')))
reviewed=[r for r in rows if r['revisor'].strip() and r['veredito'] in ['sustentada','parcialmente sustentada','não sustentada'] and r['fonte_valida'] in ['true','false']]
def ratio(n,d): return {'numerator':n,'denominator':d,'ratio':n/d if d else None}
metrics={'claims_reviewed':len(reviewed),'citation_coverage':ratio(sum(r['fonte_valida']=='true' for r in reviewed),len(reviewed)),'citation_precision':ratio(sum(r['veredito']=='sustentada' for r in reviewed if r['fonte'].strip()),sum(bool(r['fonte'].strip()) for r in reviewed)),'partial':sum(r['veredito']=='parcialmente sustentada' for r in reviewed),'unreviewed':len(rows)-len(reviewed),'limitation':'reviewed sample only; rows must reference real response files'}
print(json.dumps(metrics,ensure_ascii=False,indent=2))
