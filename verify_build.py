import os
import re
import urllib.parse

html_files = [
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

errors = []
total_images_checked = 0
total_links_checked = 0

for hf in html_files:
    if not os.path.exists(hf):
        errors.append(f"Missing file: {hf}")
        continue
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check images
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    for src in img_srcs:
        total_images_checked += 1
        if src.startswith("http://") or src.startswith("https://"):
            continue
        clean_src = src.split("?")[0].split("#")[0]
        local_path = os.path.join(os.getcwd(), clean_src.replace("/", os.sep))
        if not os.path.exists(local_path):
            errors.append(f"[{hf}] Broken image src: {src} -> {local_path}")

    # Check internal links
    links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', content)
    for link in links:
        total_links_checked += 1
        if link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:") or link.startswith("tel:") or link.startswith("#"):
            continue
        clean_link = link.split("?")[0].split("#")[0]
        if clean_link:
            local_path = os.path.join(os.getcwd(), clean_link.replace("/", os.sep))
            if not os.path.exists(local_path):
                errors.append(f"[{hf}] Broken link: {link} -> {local_path}")

print("=== VERIFICATION RESULTS ===")
print(f"Total HTML files checked: {len(html_files)}")
print(f"Total images checked: {total_images_checked}")
print(f"Total links checked: {total_links_checked}")
if errors:
    print(f"Errors found ({len(errors)}):")
    for e in errors:
        print("  - " + e)
else:
    print("ALL IMAGES AND LINKS ARE 100% VALID AND EXIST ON DISK!")
