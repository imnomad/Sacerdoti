import os
import shutil
import json

BASE_DIR = os.getcwd()
SCRAPED_DIR = os.path.join(BASE_DIR, "scraped_raw")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

os.makedirs(os.path.join(ASSETS_DIR, "images", "estuches"), exist_ok=True)
os.makedirs(os.path.join(ASSETS_DIR, "images", "estuchespromocionales"), exist_ok=True)
os.makedirs(os.path.join(ASSETS_DIR, "images", "materialpop"), exist_ok=True)
os.makedirs(os.path.join(ASSETS_DIR, "images", "promocion"), exist_ok=True)
os.makedirs(os.path.join(ASSETS_DIR, "images", "slides"), exist_ok=True)
os.makedirs(os.path.join(ASSETS_DIR, "images", "clientes"), exist_ok=True)
os.makedirs(os.path.join(ASSETS_DIR, "logos"), exist_ok=True)

# Copy logo
src_logo = os.path.join(SCRAPED_DIR, "imagenes", "logochico.png")
if os.path.exists(src_logo):
    shutil.copy2(src_logo, os.path.join(ASSETS_DIR, "logos", "logo.png"))
    shutil.copy2(src_logo, os.path.join(ASSETS_DIR, "logos", "logochico.png"))

# Copy slides
for i in range(1, 6):
    slide_src = os.path.join(SCRAPED_DIR, "images", f"slide{i}.jpg")
    if os.path.exists(slide_src):
        shutil.copy2(slide_src, os.path.join(ASSETS_DIR, "images", "slides", f"slide{i}.jpg"))

# Copy category images
categories = {
    "estuches": ("imagenes/estuches", "images/estuches"),
    "estuchespromocionales": ("imagenes/estuchespromocionales", "images/estuchespromocionales"),
    "materialpop": ("imagenes/materialpop", "images/materialpop"),
    "promocion": ("imagenes/promocion", "images/promocion"),
    "clientes": ("imagenes/clientes", "images/clientes")
}

gallery_data = {
    "estuches": [],
    "estuchespromocionales": [],
    "materialpop": [],
    "promocion": [],
    "clientes": []
}

# Pretty titles mapping
title_map = {
    # Estuches
    "merthiolateiodo.jpg": "Merthiolate Yodo",
    "oralsone.jpg": "Oralsone",
    "hexadefital.jpg": "Hexadefital",
    "findol_plus.jpg": "Findol Plus",
    "vesalion.jpg": "Vesalion",
    "pharmaton.jpg": "Pharmaton",
    "fotocrem.jpg": "Fotocrem",
    "periodent.jpg": "Periodent",
    "dibactil.jpg": "Dibactil",
    "perlutal.jpg": "Perlutal",
    "vimax.jpg": "Vimax",
    "bisolvon.jpg": "Bisolvon",
    "andrelatour.jpg": "André Latour Cosmética",
    "rowefer.jpg": "Rowefer",
    "centella.jpg": "Centella Queen",
    "estuchebucaltac.jpg": "Bucaltac Estuche",
    "cremadental.jpg": "Crema Dental Especial",
    "metglucon850.jpg": "Metglucon 850",
    "gonadotrofina.jpg": "Gonadotrofina Coriónica",
    "dineumobron.jpg": "Dineumobrón",
    # Estuches promocionales
    "cajaeucerin1.jpg": "Eucerin Pack Promocional",
    "cajaeucerin2.jpg": "Eucerin Cofre de Tratamiento",
    "cajapromobbva.jpg": "BBVA Francés Estuche Promocional",
    "cajapromovillavicencio.jpg": "Villavicencio Pack Lanzamiento",
    "dovemencare.jpg": "Dove Men+Care Pack Especial",
    "estuchepromosedal1.jpg": "Sedal Estuche Edición Especial",
    "estuchepromosedal2.jpg": "Sedal Cofre Promocional",
    "gillettecaja.jpg": "Gillette Pack Promocional",
    "knorrdispenser.jpg": "Knorr Dispenser Promocional",
    "packpromodanica.jpg": "Dánica Pack Promoción",
    # Material POP
    "colgante3dcepita.jpg": "Cepita Colgante 3D",
    "colgantecocacola.jpg": "Coca-Cola Colgante Punto de Venta",
    "colgantecocacola2.jpg": "Coca-Cola Colgante Promocional 2",
    "colgantecocacola3.jpg": "Coca-Cola Colgante 3",
    "colgantecocacola4.jpg": "Coca-Cola Colgante 4",
    "cuboissue.jpg": "Issue Cubo Exhibidor",
    "cuboneutrogena.jpg": "Neutrogena Cubo Promocional",
    "exhibidorcepita.jpg": "Cepita Exhibidor de Mostrador",
    "dispenserclubsocial.jpg": "Club Social Dispenser",
    "displayheineken.jpg": "Heineken Display de Barra",
    "displayroc.jpg": "RoC Display Cosmético",
    "pancartacepita.jpg": "Cepita Pancarta / Cartel",
    "totemheineken.jpg": "Heineken Tótem de Pie",
    "displaylucky.jpg": "Lucky Strike Display de Marca",
    "urnacocalight.jpg": "Coca-Cola Light Urna Promocional",
    "urnacocalight2.jpg": "Coca-Cola Light Urna para Sorteos",
    # Promoción
    "agendamasisa.jpg": "Masisa Agenda Institucional",
    "almanaquenarnia2.jpg": "Disney Las Crónicas de Narnia Almanaque",
    "almanaquenestcafe.jpg": "Nescafé Almanaque de Pared",
    "cuadernoclap2.jpg": "Cuaderno Clap Diseño 2",
    "cuadernoclap.jpg": "Cuaderno Clap Diseño 1",
    "historieta.jpg": "Historieta Promocional Ilustrada",
    "manitosbotellacocacola.jpg": "Coca-Cola Manitos On-Pack",
    "manitoscocacolamundial.jpg": "Coca-Cola Manitos Copa del Mundo",
    "raspaditamusimundo.jpg": "Musimundo Raspadita con Sistema de Seguridad",
    "rompecabezas.jpg": "Rompecabezas Promocional",
    "rompecabezas4.jpg": "Rompecabezas Juegos Didácticos",
    # Clientes
    "roemmers.gif": "Laboratorios Roemmers",
    "gramon.jpeg": "Gramon Millet",
    "argentia2.jpeg": "Laboratorios Argentia",
    "temis.jpg": "Temis Lostaló",
    "investi.jpg": "Investi Farma",
    "Beiersdorf.png": "Beiersdorf (Nivea / Eucerin)",
    "andromaco.jpg": "Laboratorios Andrómaco",
    "grimberg.jpg": "Grimberg Dentales",
    "glaxosmithkline.jpg": "GlaxoSmithKline (GSK)",
    "molinos.gif": "Molinos Río de la Plata",
    "macro.jpg": "Banco Macro",
    "disney.jpeg": "The Walt Disney Company",
    "unilever.jpg": "Unilever",
    "esso.gif": "Esso / Mobil",
    "Masisa.jpg": "Masisa",
    "gador.jpg": "Laboratorios Gador",
    "j&j.jpg": "Johnson & Johnson",
    "coca.jpg": "The Coca-Cola Company",
    "logo-galicia.gif": "Banco Galicia",
    "santanderrio.jpg": "Banco Santander Río",
    "colgate.jpg": "Colgate-Palmolive",
    "hsbc.gif": "HSBC Bank",
    "arcor.jpg": "Grupo Arcor",
    "arcosdorados.gif": "Arcos Dorados (McDonald's)",
    "fargo.jpg": "Fargo",
    "bimbo.jpg": "Grupo Bimbo",
    "goodyear.jpg": "Goodyear",
    "nidera.jpg": "Nidera",
    "ua.jpg": "Under Armour",
    "pierre.jpg": "Pierre Fabre",
    "sunstar.jpg": "Sunstar GUM"
}

for cat, (src_rel, dest_rel) in categories.items():
    src_dir = os.path.join(SCRAPED_DIR, src_rel.replace("/", os.sep))
    dest_dir = os.path.join(ASSETS_DIR, dest_rel.replace("/", os.sep))
    if os.path.exists(src_dir):
        for f in os.listdir(src_dir):
            src_file = os.path.join(src_dir, f)
            if os.path.isfile(src_file) and not f.endswith(".html"):
                dest_file = os.path.join(dest_dir, f)
                shutil.copy2(src_file, dest_file)
                title = title_map.get(f, f.rsplit(".", 1)[0].replace("_", " ").title())
                gallery_data[cat].append({
                    "file": f,
                    "rel_path": f"assets/{dest_rel}/{f}",
                    "title": title,
                    "category": cat
                })

with open(os.path.join(ASSETS_DIR, "gallery.json"), "w", encoding="utf-8") as out:
    json.dump(gallery_data, out, indent=2, ensure_ascii=False)

print("Assets organized successfully. Total items indexed:")
for k, v in gallery_data.items():
    print(f"  {k}: {len(v)} items")
