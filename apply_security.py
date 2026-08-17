import os
import re
import base64
import json

# 1. Generate Cloudflare Pages / Netlify _headers file
headers_content = """/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://fonts.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; frame-src https://www.google.com https://maps.google.com;
"""

with open("_headers", "w", encoding="utf-8") as f:
    f.write(headers_content.strip())

# 2. Generate vercel.json
vercel_config = {
    "version": 2,
    "headers": [
        {
            "source": "/(.*)",
            "headers": [
                {"key": "X-Frame-Options", "value": "DENY"},
                {"key": "X-Content-Type-Options", "value": "nosniff"},
                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()"},
                {"key": "Strict-Transport-Security", "value": "max-age=31536000; includeSubDomains; preload"}
            ]
        }
    ]
}

with open("vercel.json", "w", encoding="utf-8") as f:
    json.dump(vercel_config, f, indent=2)

print("Created _headers and vercel.json successfully.")

# 3. Read and Minify CSS
with open("css/main.css", "r", encoding="utf-8") as f:
    css_content = f.read()

# Add Anti-Drag & Image Protection to CSS
css_security_rules = """
/* Media & Copy Protection */
img, .gallery-card, .lightbox-img-wrapper, .hero-slider-img-wrap, .product-category-img {
  -webkit-user-drag: none;
  -khtml-user-drag: none;
  -moz-user-drag: none;
  -o-user-drag: none;
  user-drag: none;
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
"""
css_full = css_content + "\n" + css_security_rules

# CSS Minifier
min_css = re.sub(r'/\*.*?\*/', '', css_full, flags=re.DOTALL)
min_css = re.sub(r'\s+', ' ', min_css)
min_css = re.sub(r'\s*([\{\}\:\;\,])\s*', r'\1', min_css)
min_css = min_css.strip()

with open("css/main.min.css", "w", encoding="utf-8") as f:
    f.write(min_css)

print(f"Minified CSS: {len(css_content)} bytes -> {len(min_css)} bytes.")

# 4. Enhance and Obfuscate/Minify JS
with open("js/app.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# Add Frame-Busting & Anti-Image Copy Protection to JS
js_security_code = """
// Anti-Clickjacking Frame-Buster
if (window.top !== window.self) {
  window.top.location = window.self.location;
}

// Anti-Image Extraction / Right Click on Media
document.addEventListener('contextmenu', function(e) {
  if (e.target.tagName === 'IMG' || e.target.closest('.gallery-card') || e.target.closest('.lightbox-img-wrapper') || e.target.closest('.hero-slider-img-wrap')) {
    e.preventDefault();
    return false;
  }
}, false);

document.addEventListener('dragstart', function(e) {
  if (e.target.tagName === 'IMG') {
    e.preventDefault();
    return false;
  }
}, false);
"""

js_enhanced = js_security_code + "\n" + js_content

# Basic JS Minifier
min_js = re.sub(r'/\*.*?\*/', '', js_enhanced, flags=re.DOTALL)
lines = []
for line in min_js.splitlines():
    line_clean = re.sub(r'//.*$', '', line).strip()
    if line_clean:
        lines.append(line_clean)
min_js = ' '.join(lines)
min_js = re.sub(r'\s*([\{\}\(\)\=\;\:\,\+\-\*\/\<\>\!])\s*', r'\1', min_js)

with open("js/app.min.js", "w", encoding="utf-8") as f:
    f.write(min_js)

print(f"Minified JS: {len(js_content)} bytes -> {len(min_js)} bytes.")
