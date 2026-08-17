import json
import re
import html

with open('site_data.json', encoding='utf-8') as f:
    data = json.load(f)

output_lines = []

for page, info in data.items():
    raw = info['raw_html']
    output_lines.append(f"\n{'='*60}\nPAGE: {page}\nTITLE: {info.get('title')}\n{'='*60}")
    
    clean = re.sub(r'<script.*?</script>', '', raw, flags=re.DOTALL|re.IGNORECASE)
    clean = re.sub(r'<style.*?</style>', '', clean, flags=re.DOTALL|re.IGNORECASE)
    clean = re.sub(r'<div style="position:absolute;top:-21101px;".*?</div>', '', clean, flags=re.DOTALL|re.IGNORECASE)
    
    # Extract links
    links = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', clean, re.DOTALL | re.IGNORECASE)
    output_lines.append("LINKS:")
    for href, text in links:
        t = re.sub(r'<[^>]+>', '', text).strip()
        t = re.sub(r'\s+', ' ', t)
        if t or href:
            output_lines.append(f"  - [{t}] -> {href}")
            
    # Extract images
    imgs = re.findall(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*>', clean, re.DOTALL | re.IGNORECASE)
    output_lines.append("IMAGES:")
    for img in imgs:
        output_lines.append(f"  - {img}")
        
    # Extract plain text
    clean_text = re.sub(r'<[^>]+>', '\n', clean)
    clean_text = html.unescape(clean_text)
    clean_text = clean_text.replace('\u200b', '')
    lines = [re.sub(r'\s+', ' ', l).strip() for l in clean_text.splitlines() if l.strip()]
    output_lines.append("\nEXTRACTED TEXT LINES:")
    for l in lines:
        output_lines.append(f"  {l}")

with open("pages_summary.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(output_lines))

print("pages_summary.txt written successfully")
