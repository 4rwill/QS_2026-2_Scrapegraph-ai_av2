"""Compute reviewed citation metrics, never treating missing data as zero."""
import csv
import json
import hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'docs/audit.csv').open(encoding='utf-8')))
reviewed=[r for r in rows if r['revisor'].strip() and r['veredito'] in ['sustentada','parcialmente sustentada','não sustentada'] and r['fonte_valida'] in ['true','false']]
def ratio(n,d): return {'numerator':n,'denominator':d,'ratio':n/d if d else None}
metrics={'claims_reviewed':len(reviewed),'citation_coverage':ratio(sum(r['fonte_valida']=='true' for r in reviewed),len(reviewed)),'citation_precision':ratio(sum(r['veredito']=='sustentada' for r in reviewed if r['fonte'].strip()),sum(bool(r['fonte'].strip()) for r in reviewed)),'partial':sum(r['veredito']=='parcialmente sustentada' for r in reviewed),'unreviewed':len(rows)-len(reviewed),'limitation':'reviewed sample only; rows must reference real response files'}
confirmation_path=ROOT/'results/evidence/human-review-2026-10-15.json'
if confirmation_path.exists():
    confirmation=json.loads(confirmation_path.read_text(encoding='utf-8'))
    unchanged=hashlib.sha256((ROOT/'docs/audit.csv').read_text(encoding='utf-8').encode('utf-8')).hexdigest()==confirmation['audit_csv_sha256']
    metrics['human_confirmation']={'confirmed':unchanged and confirmation['audit']['human_confirmed'],'date':confirmation['confirmation_date'],'source':confirmation['source'],'individual_signatures':confirmation['individual_signatures'],'audit_csv_unchanged':unchanged,'record':str(confirmation_path.relative_to(ROOT))}
print(json.dumps(metrics,ensure_ascii=False,indent=2))
