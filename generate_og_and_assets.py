import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs(os.path.join("assets", "images", "acabados"), exist_ok=True)

# 1. GENERATE OPEN GRAPH BANNER (1200 x 630 px)
w, h = 1200, 630
img = Image.new("RGB", (w, h), color="#0a192f")
draw = ImageDraw.Draw(img)

# Background gradient / decorative rectangles
for i in range(h):
    r = int(10 + (i / h) * 4)
    g = int(25 + (i / h) * 11)
    b = int(47 + (i / h) * 21)
    draw.line([(0, i), (w, i)], fill=(r, g, b))

# Decorative geometric circuit/lines representing printing plates
draw.rectangle([60, 60, w - 60, h - 60], outline="#1e3a5f", width=2)
draw.rectangle([70, 70, w - 70, h - 70], outline="#132c4a", width=1)

# Draw Brand Icon Box
box_x, box_y = 120, 140
box_size = 110
draw.rounded_rectangle([box_x, box_y, box_x + box_size, box_y + box_size], radius=24, fill="#0e2444", outline="#38bdf8", width=3)

# Stylized "S" on box
draw.line([(box_x + 75, box_y + 32), (box_x + 42, box_y + 32)], fill="#ffffff", width=8)
draw.arc([(box_x + 24, box_y + 32), (box_x + 60, box_y + 68)], 90, 270, fill="#ffffff", width=8)
draw.line([(box_x + 42, box_y + 55), (box_x + 68, box_y + 55)], fill="#ffffff", width=8)
draw.arc([(box_x + 50, box_y + 55), (box_x + 86, box_y + 91)], 270, 90, fill="#0ea5e9", width=8)
draw.line([(box_x + 68, box_y + 91), (box_x + 35, box_y + 91)], fill="#0ea5e9", width=8)
draw.ellipse([(box_x + 55 - 6, box_y + 44 - 6), (box_x + 55 + 6, box_y + 44 + 6)], fill="#38bdf8")

# Typography
try:
    font_brand = ImageFont.truetype("arial.ttf", 64)
    font_sub = ImageFont.truetype("arial.ttf", 22)
    font_h1 = ImageFont.truetype("arial.ttf", 44)
    font_desc = ImageFont.truetype("arial.ttf", 24)
    font_badge = ImageFont.truetype("arial.ttf", 18)
except:
    font_brand = font_sub = font_h1 = font_desc = font_badge = ImageFont.load_default()

draw.text((box_x + box_size + 30, box_y + 14), "SACERDOTI", fill="#ffffff", font=font_brand)
draw.text((box_x + box_size + 34, box_y + 86), "EMPRESA GRÁFICA • DESDE 1941", fill="#38bdf8", font=font_sub)

# Headline
draw.text((120, 290), "Soluciones Integrales de Packaging,", fill="#ffffff", font=font_h1)
draw.text((120, 345), "Estuchería y Material POP", fill="#38bdf8", font=font_h1)

# Description
draw.text((120, 420), "Más de 80 años de excelencia industrial en impresión offset 6 colores,", fill="#cbd5e1", font=font_desc)
draw.text((120, 455), "sistemas de seguridad farmacopea y producción 100% in-house.", fill="#cbd5e1", font=font_desc)

# Badges at bottom
def draw_badge(x, y, text, bg, border, text_col):
    bw = len(text) * 11 + 32
    draw.rounded_rectangle([x, y, x + bw, y + 38], radius=19, fill=bg, outline=border, width=2)
    draw.text((x + 16, y + 9), text, fill=text_col, font=font_badge)
    return x + bw + 18

bx = 120
bx = draw_badge(bx, 515, "ISO 9001:2008 CERTIFIED", "#1e3a5f", "#38bdf8", "#38bdf8")
bx = draw_badge(bx, 515, "PRODUCCIÓN IN-HOUSE", "#163354", "#0ea5e9", "#ffffff")
bx = draw_badge(bx, 515, "+80 AÑOS DE TRAYECTORIA", "#3b2a14", "#f59e0b", "#f59e0b")

img.save(os.path.join("assets", "images", "og-preview.png"), "PNG", quality=95)
print("Created assets/images/og-preview.png successfully.")

# 2. GENERATE FINISHES SHOWCASE ILLUSTRATIVE CARDS
finishes = [
    ("hotstamping.jpg", "HOT STAMPING", "Metalizado térmico oro, plata y holográfico de alta gama para destacar en góndola.", "#d97706", "#fef3c7"),
    ("lacauv.jpg", "LACA UV SECTORIZADA", "Contraste óptico brillo y mate de alto impacto con relieve y secado UV instantáneo.", "#0284c7", "#e0f2fe"),
    ("relievebraille.jpg", "RELIEVE SECO & BRAILLE", "Relieve tridimensional al tacto y tipografía Braille bajo estricta normativa de farmacopea.", "#059669", "#d1fae5"),
    ("seguridaduv.jpg", "SISTEMAS DE SEGURIDAD UV", "Tintas reactivas invisibles, microtextos y hologramas antifalsificación para laboratorios.", "#7c3aed", "#ede9fe"),
    ("raspaditas.jpg", "RASPADITAS SCRATCH-OFF", "Cobertura opaca de seguridad antifraude con códigos variables para promociones masivas.", "#ea580c", "#ffedd5")
]

for filename, title, desc, accent, bg_pill in finishes:
    fw, fh = 600, 400
    fimg = Image.new("RGB", (fw, fh), color="#0a192f")
    fdraw = ImageDraw.Draw(fimg)
    
    # Background texture gradient
    for y in range(fh):
        r = int(10 + (y / fh) * 6)
        g = int(24 + (y / fh) * 12)
        b = int(44 + (y / fh) * 20)
        fdraw.line([(0, y), (fw, y)], fill=(r, g, b))
        
    # Decorative card frame
    fdraw.rectangle([20, 20, fw - 20, fh - 20], outline="#1e3a5f", width=1)
    
    # Glow circle
    fdraw.ellipse([fw - 180, -40, fw + 80, 220], fill="#0e2a4f")
    fdraw.ellipse([fw - 150, -10, fw + 50, 190], outline=accent, width=2)
    
    # Tag
    fdraw.rounded_rectangle([40, 45, 40 + len(title)*9 + 20, 75], radius=15, fill="#0e2444", outline=accent, width=2)
    fdraw.text((50, 52), title, fill=accent, font=font_badge)
    
    # Title
    fdraw.text((40, 110), title.title(), fill="#ffffff", font=font_h1)
    
    # Separator
    fdraw.line([(40, 175), (140, 175)], fill=accent, width=4)
    
    # Description lines
    words = desc.split(" ")
    line1 = " ".join(words[:len(words)//2 + 1])
    line2 = " ".join(words[len(words)//2 + 1:])
    fdraw.text((40, 210), line1, fill="#cbd5e1", font=font_desc)
    fdraw.text((40, 245), line2, fill="#cbd5e1", font=font_desc)
    
    # Technical badge
    fdraw.rounded_rectangle([40, 310, 260, 350], radius=8, fill="#0e2444", outline="#1e3a5f", width=1)
    fdraw.text((55, 322), "ESTÁNDAR SACERDOTI IN-HOUSE", fill="#38bdf8", font=font_badge)
    
    fimg.save(os.path.join("assets", "images", "acabados", filename), "JPEG", quality=92)

print("Created all finishes showcase cards successfully.")
