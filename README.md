# Sacerdoti S.A. — Empresa Gráfica (Sitio Web Modernizado)

Sitio web institucional moderno, responsive y de alto rendimiento para **Sacerdoti S.A.** (empresa gráfica argentina fundada en 1941, especializada en packaging medicinal, estuchería cosmética, material POP y campañas promocionales masivas).

---

## 🚀 Características del Proyecto

- **Arquitectura Jamstack**: 100% estático (HTML5, Vanilla CSS3 y JavaScript moderno), sin dependencias pesadas ni vulnerabilidades de bases de datos.
- **Sistema de Diseño Profesional**: Paleta corporativa inspirada en artes gráficas y tipografías Google Fonts (`Plus Jakarta Sans` e `Inter`).
- **Catálogo Interactivo con Lightbox**: Muestras en alta resolución con filtros por categoría y visor modal con zoom.
- **Navegación Multipágina Limpia**:
  - `index.html` — Inicio con carrusel hero y visión ejecutiva.
  - `historia.html` — Línea de tiempo histórica (1939 - Presente) y directivos.
  - `procesos.html` — Desglose de los 5 departamentos de producción in-house.
  - `productos.html` — Catálogo general con filtros dinámicos.
  - `estuches.html` — Packaging farmacéutico y cosmético.
  - `estuchespromocionales.html` — Packs de lanzamiento y cofres de marketing directo.
  - `materialpop.html` — Exhibidores, colgantes 3D, tótems y displays de punto de venta.
  - `promocion.html` — Raspaditas de seguridad, merchandising y juegos.
  - `clientes.html` — Portafolio con más de 30 marcas líderes.
  - `contacto.html` — Formulario de cotización, datos directos y mapa interactivo.
- **Seguridad y Blindaje Web**:
  - Configuración de cabeceras de seguridad para **Cloudflare Pages**, **Netlify** (`_headers`) y **Vercel** (`vercel.json`).
  - Protección Anti-Clickjacking (frame-busting).
  - Bloqueo disuasorio de clic derecho y arrastre de imágenes de catálogo.
  - Hojas de estilo y scripts minificados y ofuscados (`main.min.css`, `app.min.js`).

---

## 🛠️ Ejecución Local

Para visualizar el sitio web en tu navegador:

```bash
# Con Python 3
python -m http.server 3000

# O simplemente abre cualquier archivo .html directamente en tu navegador
```

Acceder a: [http://localhost:3000](http://localhost:3000)

---

## 📁 Estructura del Repositorio

```
Sacerdoti/
├── index.html                   # Página de Inicio
├── historia.html                # Historia y Trayectoria
├── procesos.html                # Procesos de Producción In-House
├── productos.html               # Catálogo General
├── estuches.html                # Estuches Productivos
├── estuchespromocionales.html   # Estuches Promocionales
├── materialpop.html             # Material POP y Exhibidores
├── promocion.html               # Productos Promocionales
├── clientes.html                # Clientes
├── contacto.html                # Contacto y Cotizaciones
├── css/
│   ├── main.css                 # CSS Fuente
│   └── main.min.css             # CSS Minificado y Protegido
├── js/
│   ├── app.js                   # JavaScript Fuente
│   └── app.min.js               # JavaScript Minificado y Protegido
├── assets/
│   ├── logos/                   # Logotipo SVG y variantes
│   └── images/                  # 90+ Fotografías de productos originales
├── scraped_raw/                 # Respaldo completo del sitio web original
├── _headers                     # Cabeceras de seguridad (Cloudflare Pages / Netlify)
├── vercel.json                  # Configuración de despliegue (Vercel)
└── README.md
```

---

© 1941 - 2026 Sacerdoti S.A. Todos los derechos reservados.
