import json
import os

with open(os.path.join("assets", "gallery.json"), "r", encoding="utf-8") as f:
    gallery_data = json.load(f)

# Save gallery data as a JS file so the SPA can load it instantly in the browser without network latency
with open(os.path.join("js", "gallery-data.js"), "w", encoding="utf-8") as f:
    f.write(f"window.SACERDOTI_GALLERY = {json.dumps(gallery_data, ensure_ascii=False, indent=2)};\n")

print("Created js/gallery-data.js successfully.")
