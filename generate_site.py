import json
import os

with open(os.path.join("assets", "gallery.json"), "r", encoding="utf-8") as f:
    gallery_data = json.load(f)

def get_logo_svg(is_dark=False):
    primary_color = "#38bdf8" if is_dark else "#0284c7"
    secondary_color = "#ffffff" if is_dark else "#0ea5e9"
    bg_color = "#0e2444" if is_dark else "#0a192f"
    
    return f'''
      <svg class="brand-logo-icon" viewBox="0 0 48 48" width="44" height="44" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="48" height="48" rx="11" fill="{bg_color}"/>
        <path d="M 33 13 L 19 13 C 14.5 13 11 16.5 11 21 C 11 25.5 14.5 29 19 29 L 29 29 C 33.5 29 37 32.5 37 37 C 37 41.5 33.5 45 29 45 L 14 45" stroke="#ffffff" stroke-width="4.2" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M 19 29 L 29 29 C 33.5 29 37 32.5 37 37 C 37 41.5 33.5 45 29 45 L 21 45" stroke="{secondary_color}" stroke-width="4.2" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="24" cy="21" r="2.8" fill="{primary_color}"/>
      </svg>
'''

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
        
    cotizar_active = ' style="box-shadow: 0 0 0 2px var(--color-accent-400);"' if current_page == 'cotizar' else ''
    
    return f'''
  <!-- HEADER -->
  <header class="site-header">
    <div class="container header-container">
      <a href="index.html" class="brand-logo-wrap" title="Sacerdoti S.A. - Empresa Gráfica">
        {get_logo_svg(is_dark=False)}
        <div class="brand-text-block">
          <span class="brand-title">SACERDOTI</span>
          <span class="brand-sub">Empresa Gráfica • Desde 1941</span>
        </div>
      </a>

      <nav class="main-nav" aria-label="Navegación principal">
        <div class="nav-list">
          {''.join(nav_links)}
        </div>
        <div class="header-actions">
          <a href="cotizar.html" class="btn btn-accent btn-sm"{cotizar_active}>Cotizar Proyecto</a>
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

def get_footer():
    return f'''
  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="brand-logo-wrap" style="margin-bottom: 16px;">
            {get_logo_svg(is_dark=True)}
            <div class="brand-text-block">
              <span class="brand-title">SACERDOTI</span>
              <span class="brand-sub">Empresa Gráfica S.A.</span>
            </div>
          </a>
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
            <a href="contacto.html">Contacto Institucional</a>
            <a href="cotizar.html" style="color: var(--color-accent-400); font-weight: 600;">Cotizador de Proyectos &rarr;</a>
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
            <p style="color: #94a3b8; font-size: 0.8125rem; margin-bottom: 12px;">Ciudad Autónoma de Buenos Aires, Argentina</p>
            <p style="color: #e2e8f0; font-size: 0.875rem; margin-bottom: 4px;">Tel / Fax: (5411) 4865-3675 / 4865-2794</p>
            <a href="mailto:sacerdoti@sacerdoti.com.ar" style="color: var(--color-accent-400);">sacerdoti@sacerdoti.com.ar</a>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p>© 1941 - 2026 Sacerdoti S.A. Todos los derechos reservados.</p>
        <div style="display: flex; gap: 14px; align-items: center;">
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

  <script src="js/app.min.js"></script>
'''

def render_page(title, current_page, content, desc="Empresa gráfica con más de 80 años de trayectoria especializada en packaging, estuchería masiva, publicidad y material POP."):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>{title} | Sacerdoti - Empresa Gráfica</title>
  <meta name="description" content="{desc}">
  <link rel="icon" type="image/svg+xml" href="assets/logos/logo.svg">
  <link rel="stylesheet" href="css/main.min.css">
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

def make_gallery_cards(items, category_label):
    cards = []
    for item in items:
        cards.append(f'''
      <div class="gallery-card" data-category="{item['category']}">
        <div class="gallery-img-wrap">
          <img src="{item['rel_path']}" data-full="{item['rel_path']}" alt="{item['title']}" loading="lazy" oncontextmenu="return false;">
          <div class="gallery-zoom-badge" title="Ampliar imagen">
            <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v6m3-3H7"/>
            </svg>
          </div>
        </div>
        <div class="gallery-card-body">
          <span class="gallery-card-tag">{category_label}</span>
          <h4 class="gallery-card-title">{item['title']}</h4>
        </div>
      </div>
''')
    return ''.join(cards)

# -------------------------------------------------------------
# 1. INDEX.HTML
# -------------------------------------------------------------
home_client_logos = []
for client in gallery_data["clientes"][:12]:
    home_client_logos.append(f'''
      <div class="client-logo-card" title="{client['title']}">
        <img src="{client['rel_path']}" alt="{client['title']}" loading="lazy" oncontextmenu="return false;">
      </div>
''')

index_content = f'''
  <!-- HERO SECTION -->
  <section class="hero-section">
    <div class="container">
      <div class="hero-grid">
        <div class="hero-content">
          <div class="hero-cert-badges">
            <div class="cert-pill">
              <span class="cert-pill-icon"></span>
              <span>Producción In-House 100%</span>
            </div>
            <div class="cert-pill">
              <span class="cert-pill-icon" style="background-color: var(--color-accent-600);"></span>
              <span>Packaging & Material POP</span>
            </div>
          </div>

          <h1 class="hero-title">
            Soluciones integrales de <span>producción gráfica</span> y packaging de alta calidad.
          </h1>

          <p class="hero-description">
            Más de 80 años de trayectoria brindando servicios gráficos diferenciados. Especialistas en packaging para cosmética y farmacia, estuchería masiva, material POP y promociones con infraestructura propia.
          </p>

          <div class="hero-actions">
            <a href="productos.html" class="btn btn-primary btn-lg">Ver Catálogo de Productos</a>
            <a href="cotizar.html" class="btn btn-accent btn-lg">Cotizar Proyecto</a>
          </div>

          <div class="hero-metrics">
            <div class="metric-item">
              <span class="metric-number">+80</span>
              <span class="metric-label">Años de Trayectoria</span>
            </div>
            <div class="metric-item">
              <span class="metric-number">6+Barniz</span>
              <span class="metric-label">Impresión Simultánea</span>
            </div>
            <div class="metric-item">
              <span class="metric-number">100%</span>
              <span class="metric-label">Procesos Internos</span>
            </div>
            <div class="metric-item">
              <span class="metric-number">+25</span>
              <span class="metric-label">Sistemas de Seguridad</span>
            </div>
          </div>
        </div>

        <div class="hero-visual">
          <div class="hero-slider-card">
            <div class="hero-slider-img-wrap">
              <div class="hero-slide active">
                <img src="assets/images/slides/slide1.jpg" alt="Gráfica Sacerdoti" oncontextmenu="return false;">
                <div class="hero-slide-caption">
                  <h4>Gráfica Sacerdoti</h4>
                  <p>Queremos ser la primera alternativa a su necesidad.</p>
                </div>
              </div>
              <div class="hero-slide">
                <img src="assets/images/slides/slide2.jpg" alt="Gestión de Calidad" oncontextmenu="return false;">
                <div class="hero-slide-caption">
                  <h4>Gestión de Calidad</h4>
                  <p>Estándares que aseguran la máxima precisión técnica.</p>
                </div>
              </div>
              <div class="hero-slide">
                <img src="assets/images/slides/slide3.jpg" alt="Responsabilidad Empresaria" oncontextmenu="return false;">
                <div class="hero-slide-caption">
                  <h4>Compromiso Sustentable</h4>
                  <p>Responsabilidad Social y Empresaria en cada proceso.</p>
                </div>
              </div>
              <div class="hero-slide">
                <img src="assets/images/slides/slide4.jpg" alt="Producción In-House" oncontextmenu="return false;">
                <div class="hero-slide-caption">
                  <h4>Producción In-House</h4>
                  <p>Todos los procesos integrados bajo un mismo techo.</p>
                </div>
              </div>
              <div class="hero-slide">
                <img src="assets/images/slides/slide5.jpg" alt="Exámenes y Controles" oncontextmenu="return false;">
                <div class="hero-slide-caption">
                  <h4>Exámenes y Controles</h4>
                  <p>Rigurosos protocolos que rigen nuestra forma de trabajo.</p>
                </div>
              </div>
            </div>

            <div class="hero-slider-nav">
              <div class="slider-dots">
                <button class="slider-dot active" aria-label="Diapositiva 1"></button>
                <button class="slider-dot" aria-label="Diapositiva 2"></button>
                <button class="slider-dot" aria-label="Diapositiva 3"></button>
                <button class="slider-dot" aria-label="Diapositiva 4"></button>
                <button class="slider-dot" aria-label="Diapositiva 5"></button>
              </div>
              <div class="slider-arrows">
                <button class="slider-arrow-btn prev" aria-label="Diapositiva anterior">&#10094;</button>
                <button class="slider-arrow-btn next" aria-label="Diapositiva siguiente">&#10095;</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ¿QUIÉNES SOMOS? -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Nuestra Empresa</span>
        <h2 class="section-title">Solidez Gráfica e Innovación</h2>
        <p class="section-description">
          Somos una empresa gráfica con más de 80 años de trayectoria y experiencia en el mercado, caracterizada por brindar productos de alta calidad y especializada en trabajos masivos de Packaging, Estuchería, Publicidad y Promoción.
        </p>
      </div>

      <div class="grid-3">
        <div class="feature-card">
          <div class="feature-icon-box">
            <svg width="26" height="26" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>
            </svg>
          </div>
          <h3 class="feature-title">¿Por qué elegirnos?</h3>
          <p class="feature-desc">
            Contamos con una estructura que nos permite cubrir cada proceso con producción in-house. Brindamos confianza, respuesta inmediata, responsabilidad y originalidad en cada producto.
          </p>
        </div>

        <div class="feature-card">
          <div class="feature-icon-box">
            <svg width="26" height="26" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/>
            </svg>
          </div>
          <h3 class="feature-title">Nuestra Misión</h3>
          <p class="feature-desc">
            Queremos ser la primera alternativa a su necesidad. Brindar servicios gráficos diferenciados y de calidad, a través de una gestión integrada y responsable para establecer relaciones de confianza duraderas.
          </p>
        </div>

        <div class="feature-card">
          <div class="feature-icon-box">
            <svg width="26" height="26" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
            </svg>
          </div>
          <h3 class="feature-title">Nuestra Visión</h3>
          <p class="feature-desc">
            Trabajamos para ser la empresa gráfica líder a nivel nacional, reconocida por brindar soluciones a las necesidades y requerimientos de nuestros clientes mediante servicios y productos de excelencia.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- NUESTRAS 4 LÍNEAS DE PRODUCCIÓN -->
  <section class="section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Líneas de Especialización</span>
        <h2 class="section-title">Nuestras Soluciones de Packaging y POP</h2>
        <p class="section-description">
          Desarrollamos soluciones integrales para la industria farmacéutica, cosmética, consumo masivo y acciones de trade marketing.
        </p>
      </div>

      <div class="grid-4">
        <!-- 1. Estuches Productivos -->
        <div class="product-category-card">
          <div class="product-category-img">
            <img src="assets/images/estuches/vesalion.jpg" alt="Estuches Productivos" oncontextmenu="return false;">
          </div>
          <div class="product-category-body">
            <h3>Estuches Productivos</h3>
            <p>Packaging masivo para medicina, cosmética y alimentos. Impresión en 6 colores, hot stamping, lacas UV y sistemas de seguridad antifalsificación.</p>
            <a href="estuches.html" class="btn btn-sm btn-outline">Ver Catálogo &rarr;</a>
          </div>
        </div>

        <!-- 2. Estuches Promocionales -->
        <div class="product-category-card">
          <div class="product-category-img">
            <img src="assets/images/estuchespromocionales/gillettecaja.jpg" alt="Estuches Promocionales" oncontextmenu="return false;">
          </div>
          <div class="product-category-body">
            <h3>Estuches Promocionales</h3>
            <p>Packs de lanzamiento, cofres especiales y acciones de marketing directo con terminaciones de alto impacto para destacar en góndola.</p>
            <a href="estuchespromocionales.html" class="btn btn-sm btn-outline">Ver Catálogo &rarr;</a>
          </div>
        </div>

        <!-- 3. Material POP -->
        <div class="product-category-card">
          <div class="product-category-img">
            <img src="assets/images/materialpop/cuboissue.jpg" alt="Material POP" oncontextmenu="return false;">
          </div>
          <div class="product-category-body">
            <h3>Material POP & Displays</h3>
            <p>Colgantes 3D, exhibidores de mostrador, tótems, urnas y botaderos en cartulina montada, foamboard y PAI para punto de venta.</p>
            <a href="materialpop.html" class="btn btn-sm btn-outline">Ver Catálogo &rarr;</a>
          </div>
        </div>

        <!-- 4. Productos Promocionales -->
        <div class="product-category-card">
          <div class="product-category-img">
            <img src="assets/images/promocion/almanaquenestcafe.jpg" alt="Productos Promocionales" oncontextmenu="return false;">
          </div>
          <div class="product-category-body">
            <h3>Productos Promocionales</h3>
            <p>Raspaditas de seguridad antifraude para sorteos, juegos didácticos, almanaques, agendas institucionales y piezas de fidelización.</p>
            <a href="promocion.html" class="btn btn-sm btn-outline">Ver Catálogo &rarr;</a>
          </div>
        </div>
      </div>

      <div style="text-align: center; margin-top: 48px;">
        <a href="productos.html" class="btn btn-primary btn-lg">Explorar Todo el Catálogo &rarr;</a>
      </div>
    </div>
  </section>

  <!-- PRODUCCIÓN IN-HOUSE BANNER -->
  <section class="section section-dark">
    <div class="container">
      <div class="grid-2" style="align-items: center;">
        <div>
          <span class="section-tag">Infraestructura Integral</span>
          <h2 class="section-title">Producción In-House de Principio a Fin</h2>
          <p style="font-size: 1.05rem; color: #cbd5e1; line-height: 1.7; margin-bottom: 24px;">
            Desarrollamos departamentos interdisciplinados para llegar a la cobertura total de todas las áreas. Ofrecemos estándares asegurados sin tener que tercerizar procesos, optimizando tiempos y asegurando la fecha de entrega.
          </p>
          <ul style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 32px; color: #f1f5f9;">
            <li style="display: flex; align-items: center; gap: 10px;">
              <svg width="20" height="20" fill="none" stroke="var(--color-accent-400)" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
              <span><strong>Diseño y Preimpresión:</strong> Modelado estructural, CTP y pruebas de contrato.</span>
            </li>
            <li style="display: flex; align-items: center; gap: 10px;">
              <svg width="20" height="20" fill="none" stroke="var(--color-accent-400)" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
              <span><strong>Impresión Offset 6 Colores + Barniz:</strong> Túnel de secado UV y +25 sistemas de seguridad.</span>
            </li>
            <li style="display: flex; align-items: center; gap: 10px;">
              <svg width="20" height="20" fill="none" stroke="var(--color-accent-400)" viewBox="0 0 24 24" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
              <span><strong>Terminaciones y Logística:</strong> Stamping, laca sectorizada, troquelados y distribución federal.</span>
            </li>
          </ul>
          <a href="procesos.html" class="btn btn-accent btn-lg">Conocer Todos los Procesos &rarr;</a>
        </div>

        <div style="background-color: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); border-radius: var(--radius-xl); padding: 40px;">
          <h3 style="color: #ffffff; font-size: 1.4rem; margin-bottom: 16px;">Garantía de Calidad y Cumplimiento</h3>
          <p style="color: #cbd5e1; font-size: 0.9375rem; line-height: 1.65; margin-bottom: 24px;">
            Nuestros procesos productivos están auditados bajo normas de gestión de calidad y responsabilidad empresaria, garantizando trazabilidad y confidencialidad en tiradas críticas.
          </p>
          <div style="display: flex; gap: 14px;">
            <span class="badge badge-gold">ISO 9001:2008</span>
            <span class="badge badge-blue">Certificación RSE</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CLIENTES DESTACADOS -->
  <section class="section section-alt">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Marcas Líderes</span>
        <h2 class="section-title">Confían en Sacerdoti</h2>
        <p class="section-description">
          Acompañamos a laboratorios multinacionales, marcas de consumo masivo e instituciones bancarias de primer nivel.
        </p>
      </div>

      <div class="clients-grid">
        {''.join(home_client_logos)}
      </div>

      <div style="text-align: center; margin-top: 40px;">
        <a href="clientes.html" class="btn btn-outline">Ver Nómina Completa de Clientes &rarr;</a>
      </div>
    </div>
  </section>

  <!-- CTA COTIZADOR BANNER -->
  <section class="section">
    <div class="container">
      <div style="background: linear-gradient(135deg, var(--color-primary-900), var(--color-primary-850)); border-radius: var(--radius-xl); padding: 56px 48px; color: #ffffff; text-align: center; max-width: 960px; margin: 0 auto; box-shadow: var(--shadow-xl);">
        <h2 style="color: #ffffff; font-size: 2.2rem; margin-bottom: 16px;">¿Listo para iniciar su próximo proyecto gráfico?</h2>
        <p style="color: #cbd5e1; font-size: 1.1rem; max-width: 680px; margin: 0 auto 32px; line-height: 1.65;">
          Complete las especificaciones de su producto en nuestro cotizador técnico y reciba asesoramiento a medida.
        </p>
        <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
          <a href="cotizar.html" class="btn btn-accent btn-lg">Cotizar Proyecto Ahora</a>
          <a href="contacto.html" class="btn btn-outline-white btn-lg">Contacto Institucional</a>
        </div>
      </div>
    </div>
  </section>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(render_page("Inicio", "inicio", index_content))

# -------------------------------------------------------------
# 2. HISTORIA.HTML
# -------------------------------------------------------------
historia_content = f'''
  <section class="section" style="padding-top: calc(var(--header-height) + 48px);">
    <div class="container container-narrow">
      <div class="section-header text-left">
        <span class="section-tag">Trayectoria & Legado</span>
        <h1 class="section-title">Nuestra Historia</h1>
        <p class="section-description">
          Más de 80 años de evolución constante, maestros litógrafos italianos, ingeniería aplicada y tres generaciones dedicadas al arte gráfico.
        </p>
      </div>

      <div style="background-color: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-xl); padding: 48px; box-shadow: var(--shadow-md); margin-bottom: 48px;">
        <p style="font-size: 1.15rem; color: var(--color-text-main); line-height: 1.8; margin-bottom: 24px; font-weight: 500;">
          Una compañía originada en 1941, que nació con el objetivo de producir, diseñar y desarrollar productos de calidad que se adapten a las necesidades de nuestros clientes. La empresa se consolidó con un crecimiento sostenido, extendiendo la infraestructura, incorporando tecnologías de punta, diversificando los productos y ampliando el portfolio de clientes.
        </p>
        <p style="font-size: 1.05rem; color: var(--color-text-body); line-height: 1.75; margin-bottom: 24px;">
          La capacidad de brindar soluciones integrales, la excelencia en calidad y la innovación constante fueron las claves para convertir a Sacerdoti en una de las empresas gráficas líderes del mercado nacional.
        </p>

        <hr style="border: 0; border-top: 1px solid var(--color-border); margin: 36px 0;">

        <div style="display: flex; flex-direction: column; gap: 32px;">
          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary-900); margin-bottom: 12px;">1939 - 1941: Los Inicios del Dr. Eduardo Sacerdoti</h3>
            <p style="color: var(--color-text-body); line-height: 1.7;">
              El Dr. Eduardo Sacerdoti, abogado italiano, llegó a Buenos Aires en el año 1939 proveniente de Milán, Italia. En mayo de 1941 fundó Sacerdoti e instaló la empresa en la calle Córdoba y Talcahuano realizando impresión comercial tipográfica y edición de libros con el nombre de <em>Editorial Mireya</em>.
            </p>
          </div>

          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary-900); margin-bottom: 12px;">1947: La Escuela Litográfica Offset</h3>
            <p style="color: var(--color-text-body); line-height: 1.7;">
              1947 fue un año de grandes cambios: la empresa se trasladó a la calle <strong>Tucumán 3549</strong> y se convirtió en una gráfica litográfica offset. Con el aporte de técnicos italianos especializados en la materia marcaron un rumbo indiscutible en cuanto a calidad y arte en los impresos; sus nombres eran <strong>Tavazanni, Calzari y Fouquet</strong>.
            </p>
            <p style="color: var(--color-text-body); line-height: 1.7; margin-top: 10px;">
              Estos hombres aportaron dedicación, trabajo y conocimientos, haciendo escuela dentro de la empresa que permitió el perfeccionamiento continuo de jóvenes argentinos, contribuyendo a la consolidación de una compañía distinguida por su excelencia técnica.
            </p>
          </div>

          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary-900); margin-bottom: 12px;">1952 - 1978: Expansión e Ingeniería Industrial</h3>
            <p style="color: var(--color-text-body); line-height: 1.7;">
              <strong>Augusto Sacerdoti</strong>, hijo mayor de Eduardo y Doctor en Ciencias Económicas, se incorporó en 1952, demostrando un perfil creativo y de gran empuje comercial.
            </p>
            <p style="color: var(--color-text-body); line-height: 1.7; margin-top: 10px;">
              En 1967 llegó a la empresa <strong>Carlos Sacerdoti</strong>, ingeniero industrial, quien aportó las nuevas técnicas de organización industrial, expandiendo notablemente la actividad. A partir de ese momento, clientes de primera línea apreciaron la calidad en los impresos y la puntualidad en la entrega: un modo de trabajo que identifica a Sacerdoti hasta el día de hoy.
            </p>
            <p style="color: var(--color-text-body); line-height: 1.7; margin-top: 10px;">
              La llegada de <strong>Pablo Sacerdoti</strong>, también ingeniero industrial, en el año 1978, significó un valioso aporte de conocimientos y experiencias, especialmente en sistemas informáticos y control administrativo.
            </p>
          </div>

          <div>
            <h3 style="font-size: 1.35rem; color: var(--color-primary-900); margin-bottom: 12px;">Presente y Futuro</h3>
            <p style="color: var(--color-text-body); line-height: 1.7;">
              En la actualidad la empresa se enriquece con el aporte de directivos y profesionales especializados en las áreas de ingeniería, marketing y diseño. Junto con Carlos Sacerdoti, esta compañía continúa su amplia trayectoria con <strong>Ricardo, Flavio, Daniel y Juan Sacerdoti</strong>.
            </p>
          </div>
        </div>
      </div>

      <!-- 8 PILARES -->
      <div style="margin-bottom: 48px;">
        <h3 style="font-size: 1.5rem; color: var(--color-primary-900); margin-bottom: 20px; text-align: center;">Pilares Fundamentales de Nuestra Trayectoria</h3>
        <div class="pillars-grid" style="margin-top: 0;">
          <div class="pillar-card">
            <div class="pillar-number">1</div>
            <div class="pillar-content">
              <h4>Inmediatez</h4>
              <p>Respuesta ágil a presupuestos y consultas.</p>
            </div>
          </div>
          <div class="pillar-card">
            <div class="pillar-number">2</div>
            <div class="pillar-content">
              <h4>Diversidad</h4>
              <p>Desarrollo e ingeniería de productos.</p>
            </div>
          </div>
          <div class="pillar-card">
            <div class="pillar-number">3</div>
            <div class="pillar-content">
              <h4>Servicio</h4>
              <p>Acompañamiento personalizado.</p>
            </div>
          </div>
          <div class="pillar-card">
            <div class="pillar-number">4</div>
            <div class="pillar-content">
              <h4>Calidad</h4>
              <p>Estándares rigurosos en cada pliego.</p>
            </div>
          </div>
          <div class="pillar-card">
            <div class="pillar-number">5</div>
            <div class="pillar-content">
              <h4>Innovación</h4>
              <p>Tecnologías de vanguardia.</p>
            </div>
          </div>
          <div class="pillar-card">
            <div class="pillar-number">6</div>
            <div class="pillar-content">
              <h4>Control</h4>
              <p>Supervisión en cada etapa.</p>
            </div>
          </div>
          <div class="pillar-card">
            <div class="pillar-number">7</div>
            <div class="pillar-content">
              <h4>Comunicación</h4>
              <p>Reporte constante con el cliente.</p>
            </div>
          </div>
          <div class="pillar-card">
            <div class="pillar-number">8</div>
            <div class="pillar-content">
              <h4>Cumplimiento</h4>
              <p>Compromiso con los tiempos acordados.</p>
            </div>
          </div>
        </div>
      </div>

      <div style="text-align: center;">
        <a href="contacto.html" class="btn btn-primary btn-lg">Contactar a Nuestro Equipo Comercial</a>
      </div>
    </div>
  </section>
'''

with open("historia.html", "w", encoding="utf-8") as f:
    f.write(render_page("Historia", "historia", historia_content, "Historia de Gráfica Sacerdoti desde su fundación en 1941 por el Dr. Eduardo Sacerdoti."))

# -------------------------------------------------------------
# 3. PROCESOS.HTML
# -------------------------------------------------------------
procesos_content = f'''
  <section class="section" style="padding-top: calc(var(--header-height) + 48px);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Estructura Productiva In-House</span>
        <h1 class="section-title">Nuestros Procesos de Producción</h1>
        <p class="section-description">
          Para la producción gráfica, desarrollamos departamentos interdisciplinados para llegar a la cobertura total de todas las áreas. De esta manera podemos ofrecerle un producto con estándares asegurados y la posibilidad de que usted utilice nuestros servicios para el desarrollo del suyo propio sin tener que tercerizar por áreas; optimizando tiempo y anticipando la entrega.
        </p>
      </div>

      <div style="display: flex; flex-direction: column; gap: 32px; max-width: 1000px; margin: 0 auto;">
        
        <!-- Depto 1: Diseño -->
        <div class="feature-card" style="border-left: 4px solid var(--color-accent-600);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
            <h3 style="font-size: 1.5rem; color: var(--color-primary-900);">Departamento de Diseño</h3>
            <span class="badge badge-blue">Área 01</span>
          </div>
          <p style="color: var(--color-text-body); margin-bottom: 16px;">Desarrollo conceptual, maquetación volumétrica y piezas gráficas listas para producción industrial.</p>
          <ul style="display: flex; flex-direction: column; gap: 10px; color: var(--color-text-body);">
            <li style="display: flex; gap: 10px;"><span>•</span><span><strong>Creación de originales:</strong> Desarrollo y modelado estructural de packaging.</span></li>
            <li style="display: flex; gap: 10px;"><span>•</span><span><strong>Fotografía digital:</strong> Captura en estudio con iluminación calibrada.</span></li>
            <li style="display: flex; gap: 10px;"><span>•</span><span><strong>Retoque digital:</strong> Preparación cromática y optimización para artes gráficas.</span></li>
          </ul>
        </div>

        <!-- Depto 2: Preimpresión -->
        <div class="feature-card" style="border-left: 4px solid var(--color-accent-600);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
            <h3 style="font-size: 1.5rem; color: var(--color-primary-900);">Departamento de Preimpresión</h3>
            <span class="badge badge-blue">Área 02</span>
          </div>
          <p style="color: var(--color-text-body); margin-bottom: 16px;">Control riguroso de archivos digitales y preparación de matrices para garantizar cero errores en pliego.</p>
          <ul style="display: flex; flex-direction: column; gap: 10px; color: var(--color-text-body);">
            <li style="display: flex; gap: 10px;"><span>•</span><span><strong>Preparación de originales:</strong> CTP (Computer to Plate) de alta resolución y pruebas de contrato.</span></li>
            <li style="display: flex; gap: 10px;"><span>•</span><span><strong>Control de originales según el proceso del producto:</strong> Verificación de normativas farmacéuticas, códigos farmacopea y perfiles de color.</span></li>
          </ul>
        </div>

        <!-- Depto 3: Impresión -->
        <div class="feature-card" style="border-left: 4px solid var(--color-accent-600);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
            <h3 style="font-size: 1.5rem; color: var(--color-primary-900);">Departamento de Impresión</h3>
            <span class="badge badge-blue">Área 03</span>
          </div>
          <p style="color: var(--color-text-body); margin-bottom: 16px;">Capacidad instalada para cubrir grandes volúmenes con tiempos de respuesta récord y la máxima fidelidad.</p>
          <ul style="display: flex; flex-direction: column; gap: 10px; color: var(--color-text-body);">
            <li style="display: flex; gap: 10px;"><span>•</span><span><strong>Impresión en 6 colores + barniz simultáneo y túnel de secado:</strong> Acabados perfectos en una sola pasada.</span></li>
            <li style="display: flex; gap: 10px;"><span>•</span><span><strong>Impresión con más de 25 sistemas de seguridad:</strong> Tintas reactivas, reactivos a UV, numeraciones de seguridad, hologramas y tintas invisibles.</span></li>
            <li style="display: flex; gap: 10px;"><span>•</span><span><strong>Efectos especiales:</strong> Barnices irisados, tintas aromáticas, metalizadas y de alto impacto.</span></li>
          </ul>
        </div>

        <!-- Depto 4: Terminaciones -->
        <div class="feature-card" style="border-left: 4px solid var(--color-accent-600);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
            <h3 style="font-size: 1.5rem; color: var(--color-primary-900);">Departamento de Terminaciones</h3>
            <span class="badge badge-blue">Área 04</span>
          </div>
          <p style="color: var(--color-text-body); margin-bottom: 16px;">La línea de post-impresión más completa del mercado para terminaciones mecánicas y artesanales.</p>
          <ul style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; color: var(--color-text-body);">
            <li style="display: flex; gap: 8px;"><span>•</span><span>Laca UV total y sectorizada</span></li>
            <li style="display: flex; gap: 8px;"><span>•</span><span>Hot Stamping oro, plata y colores</span></li>
            <li style="display: flex; gap: 8px;"><span>•</span><span>Troquelado / Relieve seco / Braille</span></li>
            <li style="display: flex; gap: 8px;"><span>•</span><span>Corte recto / Corte a molde</span></li>
            <li style="display: flex; gap: 8px;"><span>•</span><span>Doblado / Pegado lineal y fondo auto</span></li>
            <li style="display: flex; gap: 8px;"><span>•</span><span>Alzado, perforado, anillado, acaballado, puntillado</span></li>
            <li style="display: flex; gap: 8px;"><span>•</span><span>Impresión de bases de datos variable</span></li>
            <li style="display: flex; gap: 8px;"><span>•</span><span>Embolsado y termo sellado</span></li>
            <li style="display: flex; gap: 8px;"><span>•</span><span>Terminaciones manuales de alta precisión</span></li>
          </ul>
        </div>

        <!-- Depto 5: Embalaje y Expedición -->
        <div class="feature-card" style="border-left: 4px solid var(--color-accent-600);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
            <h3 style="font-size: 1.5rem; color: var(--color-primary-900);">Departamento de Embalaje y Expedición</h3>
            <span class="badge badge-blue">Área 05</span>
          </div>
          <p style="color: var(--color-text-body); margin-bottom: 16px;">Acondicionamiento y transporte bajo estándares de protección para recepción impecable.</p>
          <ul style="display: flex; flex-direction: column; gap: 10px; color: var(--color-text-body);">
            <li style="display: flex; gap: 10px;"><span>•</span><span><strong>Embalaje según producto y medio de transporte:</strong> Paletizado, encajonado e impermeabilizado.</span></li>
            <li style="display: flex; gap: 10px;"><span>•</span><span><strong>Embalajes especiales:</strong> Protecciones a medida para displays y piezas delicadas.</span></li>
            <li style="display: flex; gap: 10px;"><span>•</span><span><strong>Logística en Argentina y el resto del mundo:</strong> Despachos locales y de exportación.</span></li>
            <li style="display: flex; gap: 10px;"><span>•</span><span><strong>Ajuste de tiempos de entrega:</strong> Sincronización acordada a la necesidad operativa de cada cliente.</span></li>
          </ul>
        </div>

      </div>

      <div style="text-align: center; margin-top: 56px;">
        <a href="cotizar.html" class="btn btn-accent btn-lg">Cotizar Proyecto de Producción &rarr;</a>
      </div>
    </div>
  </section>
'''

with open("procesos.html", "w", encoding="utf-8") as f:
    f.write(render_page("Procesos", "procesos", procesos_content, "Departamentos y procesos de producción gráfica in-house en Sacerdoti: Diseño, Preimpresión, Impresión 6 Colores, Terminaciones y Expedición."))

# -------------------------------------------------------------
# 4. PRODUCTOS.HTML
# -------------------------------------------------------------
all_products_gallery = []
all_products_gallery.append(make_gallery_cards(gallery_data["estuches"], "Estuches Productivos"))
all_products_gallery.append(make_gallery_cards(gallery_data["estuchespromocionales"], "Estuches Promocionales"))
all_products_gallery.append(make_gallery_cards(gallery_data["materialpop"], "Material POP"))
all_products_gallery.append(make_gallery_cards(gallery_data["promocion"], "Productos Promocionales"))

productos_content = f'''
  <section class="section" style="padding-top: calc(var(--header-height) + 48px);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Catálogo Integral</span>
        <h1 class="section-title">Catálogo de Productos</h1>
        <p class="section-description">
          Explore nuestras líneas de estuchería productiva, packs promocionales, elementos para punto de venta y acciones de marketing masivo.
        </p>
      </div>

      <!-- FILTRO DE GALERÍA -->
      <div class="filter-nav">
        <button class="filter-btn active" data-filter="all">Todos ({len(gallery_data["estuches"]) + len(gallery_data["estuchespromocionales"]) + len(gallery_data["materialpop"]) + len(gallery_data["promocion"])})</button>
        <button class="filter-btn" data-filter="estuches">Estuches Productivos ({len(gallery_data["estuches"])})</button>
        <button class="filter-btn" data-filter="estuchespromocionales">Estuches Promocionales ({len(gallery_data["estuchespromocionales"])})</button>
        <button class="filter-btn" data-filter="materialpop">Material POP ({len(gallery_data["materialpop"])})</button>
        <button class="filter-btn" data-filter="promocion">Promocionales ({len(gallery_data["promocion"])})</button>
      </div>

      <div class="gallery-grid">
        {''.join(all_products_gallery)}
      </div>

      <div style="text-align: center; margin-top: 56px;">
        <a href="cotizar.html" class="btn btn-accent btn-lg">Cotizar Proyecto a Medida &rarr;</a>
      </div>
    </div>
  </section>
'''

with open("productos.html", "w", encoding="utf-8") as f:
    f.write(render_page("Productos", "productos", productos_content, "Catálogo completo de packaging, estuchería productiva, estuches promocionales, material POP y promociones de Sacerdoti."))

# -------------------------------------------------------------
# 5. ESTUCHES.HTML
# -------------------------------------------------------------
estuches_content = f'''
  <section class="section" style="padding-top: calc(var(--header-height) + 48px);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Packaging Farmacéutico & Cosmético</span>
        <h1 class="section-title">Estuches Productivos</h1>
        <p class="section-description">
          Brindamos una cobertura total en diseño, desarrollo, producción e impresión. Hot stamping, lacas y barnices sectorizados, perfumado, perlado, UV, metalizado, pegados, troquelados, hologramas, aplicación de sistemas de seguridad antifalsificación. Todo trabajo está realizado bajo un riguroso sistema de seguridad para evitar contaminación de productos y todos los procesos pasan por control de calidad. Nuestra amplia experiencia en la realización de estuches para cosmética, productos medicinales y alimenticios nos brinda un conocimiento real de tiempos de entrega y costos.
        </p>
      </div>

      <div class="gallery-grid">
        {make_gallery_cards(gallery_data["estuches"], "Estuche Productivo")}
      </div>

      <div style="text-align: center; margin-top: 56px;">
        <a href="cotizar.html" class="btn btn-accent btn-lg">Cotizar Estuches Productivos</a>
      </div>
    </div>
  </section>
'''
with open("estuches.html", "w", encoding="utf-8") as f:
    f.write(render_page("Estuches Productivos", "productos", estuches_content, "Estuches productivos medicinales, cosméticos y alimenticios con sistemas de seguridad de Gráfica Sacerdoti."))

# -------------------------------------------------------------
# 6. ESTUCHESPROMOCIONALES.HTML
# -------------------------------------------------------------
estuchespromocionales_content = f'''
  <section class="section" style="padding-top: calc(var(--header-height) + 48px);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Packs de Lanzamiento & Marketing Directo</span>
        <h1 class="section-title">Estuches Promocionales</h1>
        <p class="section-description">
          Desarrollamos packs promocionales con inclusión de productos. Cajas para presentación de los mismos o lanzamientos, acciones de marketing directo, con desarrollos y diseños propios o del cliente. Contamos con una amplia experiencia en este tipo de productos para punto de venta o envío al hogar. Relieves, stamping, laca UV total o sectorizada. Adaptamos los productos a las necesidades del cliente.
        </p>
      </div>

      <div class="gallery-grid">
        {make_gallery_cards(gallery_data["estuchespromocionales"], "Estuche Promocional")}
      </div>

      <div style="text-align: center; margin-top: 56px;">
        <a href="cotizar.html" class="btn btn-accent btn-lg">Cotizar Packs Promocionales</a>
      </div>
    </div>
  </section>
'''
with open("estuchespromocionales.html", "w", encoding="utf-8") as f:
    f.write(render_page("Estuches Promocionales", "productos", estuchespromocionales_content, "Estuches promocionales, cofres y packs de lanzamiento de Gráfica Sacerdoti."))

# -------------------------------------------------------------
# 7. MATERIALPOP.HTML
# -------------------------------------------------------------
materialpop_content = f'''
  <section class="section" style="padding-top: calc(var(--header-height) + 48px);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Punto de Venta & Trade Marketing</span>
        <h1 class="section-title">Material POP y Exhibidores</h1>
        <p class="section-description">
          Ofrecemos una amplia variedad de elementos para punto de venta. Colgantes, collarines, estuches, cajas, stoppers, pancartas, tótems, mini-tótems, cubos, botaderos, displays, evas, gigantografías, banners, guirnaldas, elementos para productos on-pack, afiches, posters. Productos desarrollados en cartulina, cartulina montada / foamboard, cartón montado / forrado, PAI. Producción masiva para el interior y exterior.
        </p>
      </div>

      <div class="gallery-grid">
        {make_gallery_cards(gallery_data["materialpop"], "Material POP")}
      </div>

      <div style="text-align: center; margin-top: 56px;">
        <a href="cotizar.html" class="btn btn-accent btn-lg">Cotizar Material POP & Displays</a>
      </div>
    </div>
  </section>
'''
with open("materialpop.html", "w", encoding="utf-8") as f:
    f.write(render_page("Material POP", "productos", materialpop_content, "Material POP, colgantes 3D, tótems, exhibidores de punto de venta y displays de Gráfica Sacerdoti."))

# -------------------------------------------------------------
# 8. PROMOCION.HTML
# -------------------------------------------------------------
promocion_content = f'''
  <section class="section" style="padding-top: calc(var(--header-height) + 48px);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Campañas Masivas & Fidelización</span>
        <h1 class="section-title">Productos Promocionales</h1>
        <p class="section-description">
          Desarrollo de elementos promocionales: Raspaditas con sistemas de seguridad antifalsificación, cajas, juegos didácticos, almanaques, catálogos, autoliquidables, desarrollos personalizados, postales, naipes, figuritas, imanes, carpetas de presentación, entradas y tickets numerados.
        </p>
      </div>

      <div class="gallery-grid">
        {make_gallery_cards(gallery_data["promocion"], "Promocional")}
      </div>

      <div style="text-align: center; margin-top: 56px;">
        <a href="cotizar.html" class="btn btn-accent btn-lg">Cotizar Acciones Promocionales</a>
      </div>
    </div>
  </section>
'''
with open("promocion.html", "w", encoding="utf-8") as f:
    f.write(render_page("Productos Promocionales", "productos", promocion_content, "Productos promocionales, raspaditas de seguridad, agendas, juegos y merchandising de Gráfica Sacerdoti."))

# -------------------------------------------------------------
# 9. CLIENTES.HTML
# -------------------------------------------------------------
all_client_logos_html = []
for client in gallery_data["clientes"]:
    all_client_logos_html.append(f'''
      <div class="client-logo-card" title="{client['title']}">
        <img src="{client['rel_path']}" alt="{client['title']}" loading="lazy" oncontextmenu="return false;">
      </div>
''')

clientes_content = f'''
  <section class="section" style="padding-top: calc(var(--header-height) + 48px);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Confianza Comprobada</span>
        <h1 class="section-title">Nuestros Clientes</h1>
        <p class="section-description">
          Trabajamos junto a las empresas más exigentes de la industria farmacéutica, consumo masivo, entidades bancarias y entretenimiento, brindando calidad constante y puntualidad en cada entrega.
        </p>
      </div>

      <div class="clients-grid">
        {''.join(all_client_logos_html)}
      </div>

      <div style="background-color: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-xl); padding: 48px; margin-top: 56px; text-align: center; box-shadow: var(--shadow-sm);">
        <h3 style="font-size: 1.5rem; color: var(--color-primary-900); margin-bottom: 12px;">Súmese a las empresas líderes</h3>
        <p style="color: var(--color-text-muted); max-width: 600px; margin: 0 auto 24px; font-size: 1rem;">
          Descubra por qué los principales laboratorios y corporaciones multinacionales eligen a Gráfica Sacerdoti para sus proyectos más críticos.
        </p>
        <a href="cotizar.html" class="btn btn-accent btn-lg">Solicitar Presupuesto de Producción</a>
      </div>
    </div>
  </section>
'''
with open("clientes.html", "w", encoding="utf-8") as f:
    f.write(render_page("Clientes", "clientes", clientes_content, "Principales clientes y marcas que confían en Gráfica Sacerdoti S.A."))

# -------------------------------------------------------------
# 10. COTIZAR.HTML (NUEVA PÁGINA EXCLUSIVA DE COTIZACIÓN TÉCNICA)
# -------------------------------------------------------------
cotizar_content = f'''
  <section class="section" style="padding-top: calc(var(--header-height) + 48px);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Presupuesto y Asesoramiento Técnico</span>
        <h1 class="section-title">Cotizador de Producción Gráfica</h1>
        <p class="section-description">
          Complete las especificaciones técnicas de su trabajo para que nuestro equipo de ingeniería y ventas prepare una propuesta a medida con tiempos y costos optimizados.
        </p>
      </div>

      <div class="contact-grid">
        <!-- FORMULARIO TÉCNICO DE COTIZACIÓN -->
        <div class="contact-form-card">
          <h3 style="font-size: 1.4rem; color: var(--color-primary-900); margin-bottom: 8px;">Especificaciones del Proyecto</h3>
          <p style="color: var(--color-text-muted); font-size: 0.9rem; margin-bottom: 24px;">Complete los datos técnicos para una cotización exacta de pliego y terminaciones.</p>

          <div id="formSuccessMsg" class="form-success-message">
            ¡Muchas gracias! Su solicitud de cotización ha sido recibida por nuestro equipo técnico. Nos pondremos en contacto a la brevedad con la propuesta formal.
          </div>

          <form id="contactForm">
            <!-- 1. DATOS DE CONTACTO -->
            <div style="margin-bottom: 24px; padding-bottom: 20px; border-bottom: 1px solid var(--color-border);">
              <h4 style="font-size: 1.05rem; color: var(--color-primary-900); margin-bottom: 16px;">1. Datos de Contacto y Empresa</h4>
              <div class="form-row">
                <div class="form-group">
                  <label class="form-label" for="nombre">Nombre y Apellido *</label>
                  <input type="text" id="nombre" name="nombre" class="form-control" placeholder="Ej. Martín Rodríguez" required>
                </div>
                <div class="form-group">
                  <label class="form-label" for="empresa">Empresa / Laboratorio *</label>
                  <input type="text" id="empresa" name="empresa" class="form-control" placeholder="Ej. Laboratorios ABC" required>
                </div>
              </div>
              <div class="form-row">
                <div class="form-group">
                  <label class="form-label" for="email">E-mail Corporativo *</label>
                  <input type="email" id="email" name="email" class="form-control" placeholder="nombre@empresa.com" required>
                </div>
                <div class="form-group">
                  <label class="form-label" for="telefono">Teléfono / WhatsApp *</label>
                  <input type="tel" id="telefono" name="telefono" class="form-control" placeholder="Ej. (011) 15-4444-5555" required>
                </div>
              </div>
            </div>

            <!-- 2. PRODUCTO Y CANTIDADES -->
            <div style="margin-bottom: 24px; padding-bottom: 20px; border-bottom: 1px solid var(--color-border);">
              <h4 style="font-size: 1.05rem; color: var(--color-primary-900); margin-bottom: 16px;">2. Tipo de Producto y Tirada Estimada</h4>
              <div class="form-row">
                <div class="form-group">
                  <label class="form-label" for="tipo_producto">Tipo de Producto *</label>
                  <select id="tipo_producto" name="tipo_producto" class="form-control" required>
                    <option value="estuches_medicinales">Estuches Medicinales (Farmacopea)</option>
                    <option value="estuches_cosmetica">Estuches para Cosmética y Perfumería</option>
                    <option value="estuches_alimentos">Packaging para Alimentos y Consumo</option>
                    <option value="packs_promocionales">Packs de Lanzamiento & Cofres Promocionales</option>
                    <option value="material_pop">Material POP & Displays para Punto de Venta</option>
                    <option value="raspaditas_seguridad">Raspaditas de Seguridad Antifraude</option>
                    <option value="piezas_promocionales">Agendas, Almanaques y Merchandising</option>
                    <option value="otro">Otro Desarrollo a Medida</option>
                  </select>
                </div>
                <div class="form-group">
                  <label class="form-label" for="tirada">Cantidad de Unidades Estimada *</label>
                  <select id="tirada" name="tirada" class="form-control" required>
                    <option value="1k_5k">1.000 a 5.000 unidades</option>
                    <option value="5k_20k">5.000 a 20.000 unidades</option>
                    <option value="20k_50k">20.000 a 50.000 unidades</option>
                    <option value="50k_100k">50.000 a 100.000 unidades</option>
                    <option value="mas_100k">+100.000 unidades (Gran Escala)</option>
                    <option value="consultar">A definir / Asesoramiento</option>
                  </select>
                </div>
              </div>

              <div class="form-group">
                <label class="form-label" for="sustrato">Sustrato / Material Preferido</label>
                <select id="sustrato" name="sustrato" class="form-control">
                  <option value="cartulina_triplex">Cartulina Triplex / Encapada</option>
                  <option value="carton_montado">Cartón Montado / Foamboard</option>
                  <option value="microcorrugado">Cartón Microcorrugado Montado</option>
                  <option value="pai_plastico">Plásticos PAI / PVC</option>
                  <option value="recomendar">Recomendar según el producto</option>
                </select>
              </div>
            </div>

            <!-- 3. TERMINACIONES ESPECIALES -->
            <div style="margin-bottom: 24px; padding-bottom: 20px; border-bottom: 1px solid var(--color-border);">
              <h4 style="font-size: 1.05rem; color: var(--color-primary-900); margin-bottom: 12px;">3. Terminaciones Especiales y Seguridad</h4>
              <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 10px;">
                <label style="display: flex; align-items: center; gap: 8px; font-size: 0.875rem; cursor: pointer;">
                  <input type="checkbox" name="terminacion" value="laca_uv"> Laca UV Sectorizada / Total
                </label>
                <label style="display: flex; align-items: center; gap: 8px; font-size: 0.875rem; cursor: pointer;">
                  <input type="checkbox" name="terminacion" value="hot_stamping"> Hot Stamping (Oro / Plata)
                </label>
                <label style="display: flex; align-items: center; gap: 8px; font-size: 0.875rem; cursor: pointer;">
                  <input type="checkbox" name="terminacion" value="relieve_braille"> Relieve Seco / Braille
                </label>
                <label style="display: flex; align-items: center; gap: 8px; font-size: 0.875rem; cursor: pointer;">
                  <input type="checkbox" name="terminacion" value="seguridad_tintas"> Tintas UV / Reactivas
                </label>
                <label style="display: flex; align-items: center; gap: 8px; font-size: 0.875rem; cursor: pointer;">
                  <input type="checkbox" name="terminacion" value="pegado_auto"> Fondo Automático
                </label>
                <label style="display: flex; align-items: center; gap: 8px; font-size: 0.875rem; cursor: pointer;">
                  <input type="checkbox" name="terminacion" value="raspadita"> Zona de Raspadita
                </label>
              </div>
            </div>

            <!-- 4. DETALLES ADICIONALES -->
            <div class="form-group">
              <label class="form-label" for="mensaje">Medidas aproximadas y detalles técnicos *</label>
              <textarea id="mensaje" name="mensaje" class="form-control" placeholder="Indique medidas (Base x Alto x Profundidad), colores de pliego, plazos de entrega requeridos u otras observaciones..." required></textarea>
            </div>

            <button type="submit" class="btn btn-accent btn-lg" style="width: 100%;">Solicitar Presupuesto Técnico</button>
          </form>
        </div>

        <!-- PANEL LATERAL DE VALOR AGREGADO -->
        <div>
          <div class="contact-info-card" style="margin-bottom: 24px;">
            <h3>Ventajas de Producir con Sacerdoti</h3>
            <p style="margin-bottom: 20px;">Garantizamos los más altos estándares de la industria gráfica argentina.</p>

            <ul style="display: flex; flex-direction: column; gap: 14px; color: #f1f5f9; font-size: 0.9rem;">
              <li style="display: flex; gap: 10px; align-items: flex-start;">
                <svg width="20" height="20" fill="none" stroke="var(--color-accent-400)" viewBox="0 0 24 24" stroke-width="2" style="flex-shrink: 0; margin-top: 2px;"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                <span><strong>Producción 100% In-House:</strong> Cero tercerizaciones, asegurando plazos y confidencialidad.</span>
              </li>
              <li style="display: flex; gap: 10px; align-items: flex-start;">
                <svg width="20" height="20" fill="none" stroke="var(--color-accent-400)" viewBox="0 0 24 24" stroke-width="2" style="flex-shrink: 0; margin-top: 2px;"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                <span><strong>Asesoramiento Estructural:</strong> Diseño y desarrollo de maquetas previas para validación.</span>
              </li>
              <li style="display: flex; gap: 10px; align-items: flex-start;">
                <svg width="20" height="20" fill="none" stroke="var(--color-accent-400)" viewBox="0 0 24 24" stroke-width="2" style="flex-shrink: 0; margin-top: 2px;"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                <span><strong>Calidad Certificada:</strong> Protocolos ISO 9001:2008 y estricto control de farmacopea.</span>
              </li>
              <li style="display: flex; gap: 10px; align-items: flex-start;">
                <svg width="20" height="20" fill="none" stroke="var(--color-accent-400)" viewBox="0 0 24 24" stroke-width="2" style="flex-shrink: 0; margin-top: 2px;"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
                <span><strong>Logística Integral:</strong> Embalaje especializado y despacho a todo el país y exterior.</span>
              </li>
            </ul>
          </div>

          <div style="background-color: #ffffff; border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 24px; text-align: center;">
            <h4 style="font-size: 1.1rem; color: var(--color-primary-900); margin-bottom: 8px;">¿Necesita asesoramiento telefónico directo?</h4>
            <p style="color: var(--color-text-muted); font-size: 0.875rem; margin-bottom: 16px;">Comuníquese con nuestra oficina técnica comercial:</p>
            <p style="font-family: var(--font-display); font-size: 1.25rem; font-weight: 700; color: var(--color-primary-900); margin-bottom: 12px;">(011) 4865-3675</p>
            <a href="contacto.html" class="btn btn-outline btn-sm">Ver Datos Institucionales</a>
          </div>
        </div>
      </div>
    </div>
  </section>
'''
with open("cotizar.html", "w", encoding="utf-8") as f:
    f.write(render_page("Cotizar Proyecto", "cotizar", cotizar_content, "Cotizador y solicitud de presupuestos técnicos para packaging, estuches, material POP y promocionales en Gráfica Sacerdoti."))

# -------------------------------------------------------------
# 11. CONTACTO.HTML (DEDICADA A CONTACTO INSTITUCIONAL Y PLANTA)
# -------------------------------------------------------------
contacto_content = f'''
  <section class="section" style="padding-top: calc(var(--header-height) + 48px);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Atención Institucional y Planta</span>
        <h1 class="section-title">Contacto</h1>
        <p class="section-description">
          Comuníquese con nuestras oficinas centrales y planta gráfica para consultas administrativas, proveedores o coordinación de visitas técnicas.
        </p>
      </div>

      <div class="contact-grid">
        <div class="contact-info-card">
          <div>
            <h3>Sacerdoti S.A.</h3>
            <p>Empresa Gráfica de Vanguardia en Buenos Aires, Argentina.</p>

            <div class="contact-details-list">
              <div class="contact-detail-item">
                <div class="contact-icon-wrap">
                  <svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                  </svg>
                </div>
                <div class="contact-detail-content">
                  <h5>Dirección Oficial y Planta</h5>
                  <p>Mario Bravo 933 (C1175ABQ)<br>Ciudad Autónoma de Buenos Aires, Argentina</p>
                </div>
              </div>

              <div class="contact-detail-item">
                <div class="contact-icon-wrap">
                  <svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                  </svg>
                </div>
                <div class="contact-detail-content">
                  <h5>Teléfono / Fax</h5>
                  <p><a href="tel:+541148653675">(5411) 4865-3675</a> / <a href="tel:+541148652794">4865-2794</a></p>
                </div>
              </div>

              <div class="contact-detail-item">
                <div class="contact-icon-wrap">
                  <svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                  </svg>
                </div>
                <div class="contact-detail-content">
                  <h5>Correo Institucional</h5>
                  <p><a href="mailto:sacerdoti@sacerdoti.com.ar">sacerdoti@sacerdoti.com.ar</a></p>
                </div>
              </div>
            </div>
          </div>

          <div style="padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.15);">
            <p style="font-size: 0.8125rem; color: #94a3b8; margin-bottom: 0;">Horario de Atención: Lunes a Viernes de 8:00 a 18:00 hs.</p>
          </div>
        </div>

        <div class="contact-form-card">
          <h3>Mensaje Institucional o Consulta General</h3>
          <p>Para consultas administrativas o institucionales, complete los datos a continuación:</p>

          <div id="formSuccessMsg" class="form-success-message">
            ¡Muchas gracias por contactarnos! Su mensaje ha sido enviado correctamente. Le responderemos a la brevedad.
          </div>

          <form id="contactForm">
            <div class="form-row">
              <div class="form-group">
                <label class="form-label" for="nombre">Nombre y Apellido *</label>
                <input type="text" id="nombre" name="nombre" class="form-control" placeholder="Ej. Carlos Martínez" required>
              </div>
              <div class="form-group">
                <label class="form-label" for="empresa">Empresa / Institución</label>
                <input type="text" id="empresa" name="empresa" class="form-control" placeholder="Ej. Empresa / Agencia">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label class="form-label" for="email">E-mail de Contacto *</label>
                <input type="email" id="email" name="email" class="form-control" placeholder="nombre@correo.com" required>
              </div>
              <div class="form-group">
                <label class="form-label" for="telefono">Teléfono</label>
                <input type="tel" id="telefono" name="telefono" class="form-control" placeholder="Ej. (011) 15-4444-5555">
              </div>
            </div>

            <div class="form-group">
              <label class="form-label" for="motivo">Motivo de Contacto</label>
              <select id="motivo" name="motivo" class="form-control">
                <option value="consulta_general">Consulta General / Información</option>
                <option value="proveedores">Proveedores e Insumos</option>
                <option value="recursos_humanos">Recursos Humanos / Postulaciones</option>
                <option value="administracion">Administración y Finanzas</option>
              </select>
            </div>

            <div class="form-group">
              <label class="form-label" for="mensaje">Mensaje *</label>
              <textarea id="mensaje" name="mensaje" class="form-control" placeholder="Escriba aquí su consulta..." required></textarea>
            </div>

            <button type="submit" class="btn btn-primary btn-lg" style="width: 100%;">Enviar Mensaje Institucional</button>

            <div style="margin-top: 16px; text-align: center;">
              <span style="font-size: 0.875rem; color: var(--color-text-muted);">¿Desea solicitar un presupuesto de producción? <a href="cotizar.html" style="color: var(--color-accent-600); font-weight: 600;">Ir al Cotizador Técnico &rarr;</a></span>
            </div>
          </form>
        </div>
      </div>

      <div class="map-card">
        <iframe 
          title="Ubicación Sacerdoti S.A."
          src="https://maps.google.com/maps?q=Mario%20Bravo%20933,%20Buenos%20Aires,%20Argentina&t=&z=15&ie=UTF8&iwloc=&output=embed" 
          loading="lazy">
        </iframe>
      </div>
    </div>
  </section>
'''
with open("contacto.html", "w", encoding="utf-8") as f:
    f.write(render_page("Contacto", "contacto", contacto_content, "Contacto directo, datos institucionales y ubicación de Gráfica Sacerdoti en Buenos Aires, Argentina."))

print("Site successfully rebuilt with dedicated Cotizador page (cotizar.html)!")
