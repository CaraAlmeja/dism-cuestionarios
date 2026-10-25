"""Aplica el helper de cuestionarios a cada bloque y produce una fuente final única."""
from pathlib import Path
import importlib.util
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
HELPER=Path.home()/'.codex/skills/cuestionarios/scripts/quiz.py'
sys.path.insert(0,str(ROOT/'scripts'))
import author_bank
author_bank.save()
spec=importlib.util.spec_from_file_location('quiz_helper',HELPER)
helper=importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
draft=json.loads((ROOT/'content/draft.json').read_text(encoding='utf-8'))
draft_audit=helper.audit(draft)
assert not draft_audit['errors'],draft_audit
final={**draft,'questions':[],'version':1}
reports={}
for i,block in enumerate(draft['blocks']):
    doc={**draft,'title':f"DISM · {block['code']} · {block['title']}",
         'expected_questions':20,'questions':[q for q in draft['questions'] if q['block']==block['id']]}
    folder=ROOT/'work'/'prepare'
    folder.mkdir(parents=True,exist_ok=True)
    raw=folder/f"{block['id']}-draft.json"
    ready=folder/f"{block['id']}-final.json"
    raw.write_text(json.dumps(doc,ensure_ascii=False),encoding='utf-8')
    if ready.is_file(): ready.unlink()
    # prepare usa semillas independientes, sin ciclos ni cuotas por bloques de cuatro.
    subprocess.run([sys.executable,'-X','utf8',str(HELPER),'prepare',str(raw),str(ready),'--seed',str(817+i*197)],check=True,capture_output=True)
    prepared=json.loads(ready.read_text(encoding='utf-8'))
    report=helper.audit(prepared)
    assert not report['errors'],report
    reports[block['id']]=report
    final['questions'].extend(prepared['questions'])
    output=ROOT/'public'/'exports'/block['id']
    output.mkdir(parents=True,exist_ok=True)
    # El helper no sobrescribe: se eliminan solo sus tres salidas conocidas.
    for name in ['cuestionario.md','solucionario.md','informe-automatico.json']:
        target=output/name
        if target.is_file(): target.unlink()
    subprocess.run([sys.executable,'-X','utf8',str(HELPER),'render',str(ready),str(output)],check=True,capture_output=True)
    for name in ['cuestionario.md','solucionario.md']:
        target=output/name
        target.write_text(target.read_text(encoding='utf-8').rstrip()+'\n',encoding='utf-8')
report=helper.audit(final)
assert not report['errors'],report
(ROOT/'public/data').mkdir(parents=True,exist_ok=True)
(ROOT/'public/data/questions.json').write_text(json.dumps(final,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'content/audit.json').write_text(json.dumps({'bank':report,'blocks':reports},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
