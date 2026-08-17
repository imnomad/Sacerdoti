import os
import re
import html
import json

files = [
    'index.html',
    'historia.html',
    'procesos.html',
    'productos.html',
    'estuches.html',
    'estuchespromocionales.html',
    'materialpop.html',
    'promocion.html',
    'clientes.html',
    'contacto.html'
]

def clean_mojibake(text):
    fixes = [
        ('aó±os', 'años'),
        ('ó±', 'ñ'),
        ('Estucheró\xada', 'Estuchería'),
        ('Estucheró­a', 'Estuchería'),
        ('travós', 'través'),
        ('ló\xader', 'líder'),
        ('ló­der', 'líder'),
        ('ó\xad', 'í'),
        ('ó­', 'í'),
        ('ó\xba', 'ú'),
        ('óº', 'ú'),
        ('ó\xa9', 'é'),
        ('ó©', 'é'),
        ('ó\xa1', 'á'),
        ('ó¡', 'á'),
        ('ó\xb3', 'ó'),
        ('ó³', 'ó'),
        ('ó\xb1', 'ñ'),
        ('ó±', 'ñ'),
        ('ó\xbf', '¿'),
        ('ó¿', '¿'),
        ('Ã¡', 'á'),
        ('Ã©', 'é'),
        ('Ã\xad', 'í'),
        ('Ã³', 'ó'),
        ('Ãº', 'ú'),
        ('Ã±', 'ñ'),
        ('Ã‘', 'Ñ'),
        ('â€“', '–'),
        ('â€”', '—'),
        ('â€œ', '“'),
        ('â€\x9d', '”'),
        ('â€˜', '‘'),
        ('â€™', '’'),
        ('&oacute;', 'ó'),
        ('&iacute;', 'í'),
        ('&eacute;', 'é'),
        ('&aacute;', 'á'),
        ('&uacute;', 'ú'),
        ('&ntilde;', 'ñ'),
        ('&iquest;', '¿'),
        ('&Ntilde;', 'Ñ')
    ]
    for old, new in fixes:
        text = text.replace(old, new)
    return text

extracted = {}

for f in files:
    path = os.path.join('scraped_raw', f)
    if not os.path.exists(path):
        continue
    with open(path, 'rb') as fp:
        raw = fp.read()
    try:
        text = raw.decode('utf-8')
    except:
        text = raw.decode('latin-1')
        
    text = clean_mojibake(text)
    
    title_m = re.search(r'<title>(.*?)</title>', text, re.IGNORECASE | re.DOTALL)
    title = title_m.group(1).strip() if title_m else ''
    
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', text, re.IGNORECASE)
    
    clean = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL|re.IGNORECASE)
    clean = re.sub(r'<style.*?</style>', '', clean, flags=re.DOTALL|re.IGNORECASE)
    clean = re.sub(r'<div style="position:absolute;top:-21101px;".*?</div>', '', clean, flags=re.DOTALL|re.IGNORECASE)
    
    extracted[f] = {
        "title": title,
        "images": imgs,
        "raw_html": text
    }

with open("site_data.json", "w", encoding="utf-8") as out:
    json.dump(extracted, out, indent=2, ensure_ascii=False)

print("Saved site_data.json successfully")
