import os

redirect_map = {
    "historia.html": "index.html#historia",
    "procesos.html": "index.html#procesos",
    "productos.html": "index.html#productos",
    "estuches.html": "index.html#productos/estuches",
    "estuchespromocionales.html": "index.html#productos/estuchespromocionales",
    "materialpop.html": "index.html#productos/materialpop",
    "promocion.html": "index.html#productos/promocion",
    "clientes.html": "index.html#clientes",
    "contacto.html": "index.html#contacto",
    "cotizar.html": "index.html#cotizar"
}

for filename, target in redirect_map.items():
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url={target}">
  <title>Redireccionando... | Sacerdoti S.A.</title>
  <script>window.location.replace("{target}");</script>
</head>
<body style="font-family: sans-serif; text-align: center; padding: 40px; background: #0a192f; color: #fff;">
  <p>Cargando Sacerdoti S.A...</p>
  <p><a href="{target}" style="color: #38bdf8;">Haga clic aquí si no es redirigido automáticamente.</a></p>
</body>
</html>"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

print("Created fallback redirect files for all subroutes successfully.")
