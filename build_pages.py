import json
import os

with open(os.path.join("assets", "gallery.json"), "r", encoding="utf-8") as f:
    gallery_data = json.load(f)

# Helper for common header
def get_header(current_page=""):
    pages = [
        ("index.html", "Inicio", "inicio"),
        ("historia.html", "Historia", "historia"),
        ("procesos.html", "Procesos", "procesos"),
        ("productos.html", "Productos", "productos"),
        ("clientes.html", "Clientes", "clientes"),
        ("contacto.html", "Contacto", "contacto")
    ]
    nav_links = []
    for url, title, slug in pages:
        active_cls = " active" if current_page == slug else ""
        nav_links.append(f'<a href="{url}" class="nav-link{active_cls}">{title}</a>')
        
    return f'''
  <!-- HEADER -->
  <header class="site-header">
    <div class="container header-container">
      <a href="index.html" class="brand-logo" title="Sacerdoti S.A. - Empresa Gráfica">
        <div class="brand-symbol">
          <img src="assets/logos/logochico.png" alt="Sacerdoti Gráfica" onerror="this.style.display='none'">
        </div>
        <div class="brand-text">
          <span class="brand-name">Sacerdoti</span>
          <span class="brand-tagline">Empresa Gráfica • Desde 1941</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Navegación principal">
        <div class="nav-list">
          {''.join(nav_links)}
        </div>
        <div class="header-actions">
          <a href="contacto.html" class="btn btn-accent btn-sm">Cotizar Proyecto</a>
        </div>
      </nav>

      <button class="mobile-menu-toggle" aria-label="Abrir menú de navegación" aria-expanded="false">
        <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
      </button>
    </div>
  </header>
'''

# Helper for common footer
def get_footer():
    return '''
  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="brand-logo" style="margin-bottom: 16px;">
            <div class="brand-symbol">
              <img src="assets/logos/logochico.png" alt="Sacerdoti">
            </div>
            <div class="brand-text">
              <span class="brand-name" style="color: #ffffff;">Sacerdoti</span>
              <span class="brand-tagline" style="color: #94a3b8;">Empresa Gráfica S.A.</span>
            </div>
          </div>
          <p>Más de 80 años de trayectoria y excelencia en producción gráfica in-house, especializada en packaging, estuchería farmacéutica y cosmética, publicidad y material POP.</p>
        </div>

        <div class="footer-col">
          <h5>Navegación</h5>
          <div class="footer-links">
            <a href="index.html">Inicio</a>
            <a href="historia.html">Historia y Trayectoria</a>
            <a href="procesos.html">Procesos de Producción</a>
            <a href="productos.html">Catálogo de Productos</a>
            <a href="clientes.html">Nuestros Clientes</a>
            <a href="contacto.html">Contacto y Cotizaciones</a>
          </div>
        </div>

        <div class="footer-col">
          <h5>Líneas de Producto</h5>
          <div class="footer-links">
            <a href="estuches.html">Estuches Productivos</a>
            <a href="estuchespromocionales.html">Estuches Promocionales</a>
            <a href="materialpop.html">Material POP & Exhibidores</a>
            <a href="promocion.html">Productos Promocionales</a>
            <a href="procesos.html">Sistemas de Seguridad</a>
          </div>
        </div>

        <div class="footer-col">
          <h5>Contacto Directo</h5>
          <div class="footer-links">
            <p style="color: #e2e8f0; font-size: 0.875rem; margin-bottom: 4px;">Mario Bravo 933 (C1175ABQ)</p>
            <p style="color: #94a3b8; font-size: 0.8125rem; margin-bottom: 12px;">CABA, Argentina</p>
            <p style="color: #e2e8f0; font-size: 0.875rem; margin-bottom: 4px;">Tel / Fax: (5411) 4865-3675 / 2794</p>
            <a href="mailto:sacerdoti@sacerdoti.com.ar" style="color: var(--color-accent-400);">sacerdoti@sacerdoti.com.ar</a>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p>© 1941 - 2026 Sacerdoti S.A. Todos los derechos reservados. Producción Gráfica Integral.</p>
        <div style="display: flex; gap: 16px;">
          <span class="badge badge-gold">ISO 9001:2008</span>
          <span class="badge badge-blue">Certificación RSE</span>
        </div>
      </div>
    </div>
  </footer>

  <!-- LIGHTBOX MODAL -->
  <div class="lightbox-modal" aria-hidden="true" role="dialog">
    <div class="lightbox-content">
      <button class="lightbox-close" aria-label="Cerrar modal">&times;</button>
      <button class="lightbox-nav-btn lightbox-prev" aria-label="Anterior">&#10094;</button>
      <button class="lightbox-nav-btn lightbox-next" aria-label="Siguiente">&#10095;</button>
      <div class="lightbox-img-wrapper">
        <img src="" alt="Muestra en alta resolución">
      </div>
      <div class="lightbox-caption">
        <h3></h3>
        <p></p>
      </div>
    </div>
  </div>

  <script src="js/app.js"></script>
'''

def render_html_page(title, current_page, content, desc="Empresa gráfica con más de 80 años de trayectoria especializada en packaging, estuchería masiva, publicidad y material POP."):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Sacerdoti - Empresa Gráfica</title>
  <meta name="description" content="{desc}">
  <link rel="stylesheet" href="css/main.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
</head>
<body>
{get_header(current_page)}
{content}
{get_footer()}
</body>
</html>
'''

print("Builder initialized...")
