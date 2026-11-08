"""Consolidate an explicitly AI-authored rubric; human measures stay unavailable."""
import argparse
import csv
import json
from datetime import datetime
from pathlib import Path
from metrics import approved, lexical_f1
from experiment import read, save, write_csv


def consolidate(folder):
    completion = read(folder / 'completion.json')
    if completion['records'] != 12 or not completion['conditions_comparable']:
        raise ValueError('Expected complete comparable 12-output batch')
    automatic = read(folder / 'automatic.json')
    with (folder / 'ai-assessment.csv').open(encoding='utf-8-sig', newline='') as f:
        notes = list(csv.DictReader(f))
    keys = {(r['case_id'], r['version']) for r in automatic}
    if len(notes) != 12 or {(r['case_id'], r['version']) for r in notes} != keys:
        raise ValueError('Expected exactly one explicitly AI-authored note per output')
    rows = []
    for a in sorted(automatic, key=lambda r: (r['case_id'], r['version'])):
        note = next(r for r in notes if (r['case_id'], r['version']) == (a['case_id'], a['version']))
        if note['evaluation_origin'] != 'IA — Codex' or not note['justificativa'].strip():
            raise ValueError('Origin and justification required')
        for field in ('correcao', 'relevancia', 'suporte'):
            if note[field] not in ('0','1','2'): raise ValueError('Invalid score')
        if note['falha_critica'] not in ('0','1'): raise ValueError('Invalid flag')
        rows.append({**a, **note, 'ai_rubric_approved': approved(note), 'human_approved': None})
    metrics = dict(assessment_origin='IA — Codex', batch_mode=completion['mode'], responses=12,
        human_annotations_completed=0, human_approval=None, automatic_human_agreement=None,
        r1_r2_agreement_before_consensus=None, experimental_decision='pendente de avaliação humana e resolução da revisão prévia das referências',
        versions={}, automatic_ai_agreement=dict(numerator=sum(r['automatic_approved'] == r['ai_rubric_approved'] for r in rows),denominator=12),
        automatic_ai_disagreements=[dict(case_id=r['case_id'],version=r['version'],f1=r['f1'],justificativa=r['justificativa']) for r in rows if r['automatic_approved'] != r['ai_rubric_approved']])
    for version in ('A','B'):
        selected=[r for r in rows if r['version']==version]
        metrics['versions'][version]=dict(mean_f1=sum(r['f1'] for r in selected)/6, denominator=6,
            automatic_approved=sum(r['automatic_approved'] for r in selected),ai_rubric_approved=sum(r['ai_rubric_approved'] for r in selected),
            ai_critical_flags=sum(int(r['falha_critica']) for r in selected),human_approved=None)
    out=folder/('ai-analysis-'+datetime.now().strftime('%Y%m%dT%H%M%S%f'));out.mkdir()
    save(out/'metrics.json',metrics)
    write_csv(out/'consolidated.csv',rows,list(rows[0]))
    save(out/'consolidated.json',rows)
    print(out)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('run',type=Path);args=p.parse_args()
    consolidate(args.run)
