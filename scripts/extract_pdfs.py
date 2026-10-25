from pathlib import Path
import json
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    't1': 'Tema1DISM_Desarrollo_de_aplicaciones_multiplataforma.pdf',
    't21': 'Tema2-DISM-1.pdf',
    't22': 'Tema2-DISM-2.pdf',
    't31': 'Tema3-DISM-1.pdf',
    't32': 'Tema3-DISM-21.pdf',
}
out = ROOT / 'work' / 'sources'
out.mkdir(parents=True, exist_ok=True)
for key, filename in FILES.items():
    reader = PdfReader(Path('D:/Descargas2') / filename)
    pages = [{'page': i+1, 'text': p.extract_text() or ''} for i,p in enumerate(reader.pages)]
    (out / f'{key}.json').write_text(json.dumps(pages, ensure_ascii=False, indent=2), encoding='utf-8')
    (out / f'{key}.txt').write_text('\n\n'.join(f'=== PÁGINA PDF {p["page"]} ===\n{p["text"]}' for p in pages), encoding='utf-8')
    print(key, len(pages), 'pages', sum(len(p['text']) for p in pages), 'characters')
