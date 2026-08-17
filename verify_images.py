import os
import re
import urllib.parse
import urllib.request

images_found = set()

# Scan all html files in scraped_raw
for root, dirs, files in os.walk("scraped_raw"):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="latin-1", errors="ignore") as f:
                content = f.read()
            # find all jpg, png, gif, jpeg references
            matches = re.findall(r'["\']([^"\']+\.(?:jpg|jpeg|png|gif|webp|svg))(?:\?[^"\']*)?["\']', content, re.IGNORECASE)
            for m in matches:
                images_found.add(m)
            # also check hrefs pointing to images
            href_matches = re.findall(r'href=["\']([^"\']+)["\']', content, re.IGNORECASE)
            for h in href_matches:
                if any(h.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg']) or '/imagenes/' in h:
                    images_found.add(h)

print(f"Total image URLs found in HTML files: {len(images_found)}")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

missing = []
downloaded = []

for img_url in sorted(images_found):
    # check local path
    parsed = urllib.parse.urlparse(img_url)
    path = parsed.path.lstrip("/")
    local_path = os.path.join("scraped_raw", path.replace("/", os.sep))
    
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        downloaded.append((img_url, local_path, os.path.getsize(local_path)))
    else:
        # Try to download if absolute or relative
        full_url = urllib.parse.urljoin("https://www.sacerdoti.com.ar/", img_url)
        print(f"Attempting download for missing: {full_url}")
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        try:
            req = urllib.request.Request(full_url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
                with open(local_path, "wb") as f:
                    f.write(data)
                print(f"Successfully downloaded: {local_path} ({len(data)} bytes)")
                downloaded.append((img_url, local_path, len(data)))
        except Exception as e:
            print(f"Failed to fetch {full_url}: {e}")
            missing.append((img_url, str(e)))

print("\n--- Summary ---")
print(f"Downloaded / Existing images: {len(downloaded)}")
print(f"Missing images: {len(missing)}")
for m in missing:
    print(f"  Missing: {m}")
