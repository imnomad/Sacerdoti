import os
import re
import html

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
    # Fix broken utf-8 / double-encoded sequences
    # Let's try latin1 -> utf-8 conversion if possible or explicit replace
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

for f in files:
    path = os.path.join('scraped_raw', f)
    if not os.path.exists(path):
        print(f"NOT FOUND: {path}")
        continue
    with open(path, 'rb') as fp:
        raw = fp.read()
    try:
        text = raw.decode('utf-8')
    except:
        text = raw.decode('latin-1')
    
    text = clean_mojibake(text)
    
    # Extract title
    title_m = re.search(r'<title>(.*?)</title>', text, re.IGNORECASE | re.DOTALL)
    title = title_m.group(1).strip() if title_m else 'No title'
    
    # Extract images
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', text, re.IGNORECASE)
    
    # Clean text content
    clean = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL|re.IGNORECASE)
    clean = re.sub(r'<style.*?</style>', '', clean, flags=re.DOTALL|re.IGNORECASE)
    # Remove hidden spam div if any
    clean = re.sub(r'<div style="position:absolute;top:-21101px;".*?</div>', '', clean, flags=re.DOTALL|re.IGNORECASE)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = html.unescape(clean)
    lines = [l.strip() for l in clean.splitlines() if l.strip()]
    
    print('=====================================================')
    print(f'FILE: {f}')
    print(f'TITLE: {title}')
    print(f'IMAGES ({len(imgs)}): {imgs}')
    print('--- CONTENT ---')
    print('\n'.join(lines))
    print('\n')
