import os
import re
import urllib.parse
import urllib.request
from collections import deque

BASE_URL = "https://www.sacerdoti.com.ar/"
OUTPUT_DIR = os.path.join(os.getcwd(), "scraped_raw")

os.makedirs(OUTPUT_DIR, exist_ok=True)

visited_urls = set()
urls_to_visit = deque([BASE_URL])
downloaded_assets = set()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def clean_url(url):
    parsed = urllib.parse.urlparse(url)
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', '', ''))

def download_file(url, local_path):
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read()
            with open(local_path, "wb") as f:
                f.write(content)
            print(f"Downloaded: {url} -> {local_path} ({len(content)} bytes)")
            return content
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

html_pages = {}

while urls_to_visit:
    current_url = urls_to_visit.popleft()
    normalized_url = clean_url(current_url)
    if normalized_url in visited_urls:
        continue
    visited_urls.add(normalized_url)
    
    parsed = urllib.parse.urlparse(normalized_url)
    path = parsed.path
    if not path or path == "/" or path.endswith("/"):
        filename = "index.html"
        rel_path = "index.html"
    else:
        rel_path = path.lstrip("/")
        if not os.path.splitext(rel_path)[1]:
            rel_path += ".html"
            
    local_file = os.path.join(OUTPUT_DIR, rel_path.replace("/", os.sep))
    content_bytes = download_file(normalized_url, local_file)
    
    if content_bytes is None:
        continue
        
    # Check if html
    try:
        # Try decoding with utf-8 or latin1
        try:
            html_text = content_bytes.decode("utf-8")
        except UnicodeDecodeError:
            html_text = content_bytes.decode("latin-1")
            
        html_pages[normalized_url] = html_text
        
        # Find more links and assets
        # Find href and src
        found_links = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', html_text, re.IGNORECASE)
        for link in found_links:
            link = link.strip()
            if not link or link.startswith("#") or link.startswith("javascript:") or link.startswith("mailto:") or link.startswith("tel:"):
                continue
            abs_url = urllib.parse.urljoin(normalized_url, link)
            abs_parsed = urllib.parse.urlparse(abs_url)
            
            # If internal sacerdoti
            if "sacerdoti.com.ar" in abs_parsed.netloc:
                clean_abs = clean_url(abs_url)
                ext = os.path.splitext(abs_parsed.path)[1].lower()
                if ext in [".html", ".htm", ".php", ""] or abs_parsed.path.endswith("/"):
                    if clean_abs not in visited_urls and clean_abs not in urls_to_visit:
                        urls_to_visit.append(clean_abs)
                else:
                    if clean_abs not in downloaded_assets:
                        downloaded_assets.add(clean_abs)
                        asset_rel_path = abs_parsed.path.lstrip("/")
                        asset_local_file = os.path.join(OUTPUT_DIR, asset_rel_path.replace("/", os.sep))
                        download_file(clean_abs, asset_local_file)
    except Exception as e:
        print(f"Error parsing {normalized_url}: {e}")

print("\n--- Summary of Scraped Pages ---")
for u in html_pages.keys():
    print(f"Page: {u}")
