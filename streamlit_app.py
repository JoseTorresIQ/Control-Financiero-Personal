# streamlit_app.py - FinanzFlow PWA en Streamlit Cloud
import os
import shutil
import streamlit as st
import streamlit.components.v1 as components

# Configuración de página Streamlit
st.set_page_config(
    page_title="FinanzFlow | Control Financiero Personal PWA",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Sincronización automática de archivos estáticos (Root -> static/)
def sync_static_assets():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, "static")
    os.makedirs(static_dir, exist_ok=True)

    files_to_sync = ["index.html", "manifest.json", "sw.js"]
    for f in files_to_sync:
        src = os.path.join(base_dir, f)
        dst = os.path.join(static_dir, f)
        if os.path.exists(src):
            if (
                not os.path.exists(dst)
                or os.path.getmtime(src) != os.path.getmtime(dst)
                or os.path.getsize(src) != os.path.getsize(dst)
            ):
                shutil.copy2(src, dst)

    dirs_to_sync = ["css", "js", "icons"]
    for d in dirs_to_sync:
        src_dir = os.path.join(base_dir, d)
        dst_dir = os.path.join(static_dir, d)
        if os.path.exists(src_dir):
            if not os.path.exists(dst_dir):
                shutil.copytree(src_dir, dst_dir)
            else:
                for root, _, files in os.walk(src_dir):
                    rel_path = os.path.relpath(root, src_dir)
                    target_root = os.path.join(dst_dir, rel_path)
                    os.makedirs(target_root, exist_ok=True)
                    for file in files:
                        s_file = os.path.join(root, file)
                        d_file = os.path.join(target_root, file)
                        if (
                            not os.path.exists(d_file)
                            or os.path.getmtime(s_file) != os.path.getmtime(d_file)
                            or os.path.getsize(s_file) != os.path.getsize(d_file)
                        ):
                            shutil.copy2(s_file, d_file)

sync_static_assets()

# Estilos para integración fluida sin bordes ni padding excesivo (Mobile-First)
st.markdown("""
<style>
    /* Ocultar elementos estándar de Streamlit para apariencia de app nativa */
    #MainMenu {visibility: hidden; display: none !important;}
    footer {visibility: hidden; display: none !important;}
    header {visibility: hidden; display: none !important;}
    [data-testid="stDecoration"] {display: none !important;}
    [data-testid="stStatusWidget"] {display: none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    
    /* Contenedor principal a pantalla completa */
    .stApp {
        background-color: #090d16 !important;
    }
    .main {
        padding: 0 !important;
        margin: 0 !important;
    }
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    
    /* Barra superior informativa adaptable a celulares */
    .pwa-topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #0f172a;
        color: #f8fafc;
        padding: 10px 16px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-size: 0.85rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        gap: 10px;
    }
    .pwa-topbar .brand-info {
        display: flex;
        align-items: center;
        gap: 8px;
        flex-wrap: wrap;
    }
    .pwa-topbar code {
        background: rgba(255, 255, 255, 0.1);
        padding: 2px 6px;
        border-radius: 4px;
        color: #38bdf8;
        font-size: 0.8rem;
    }
    .pwa-topbar a.fullscreen-btn {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(16, 185, 129, 0.15);
        color: #10b981;
        border: 1px solid rgba(16, 185, 129, 0.35);
        padding: 6px 14px;
        border-radius: 9999px;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.8rem;
        transition: all 0.2s ease;
        white-space: nowrap;
    }
    .pwa-topbar a.fullscreen-btn:hover {
        background: rgba(16, 185, 129, 0.25);
        border-color: #10b981;
        transform: translateY(-1px);
    }

    /* Iframe adaptativo y fluido para móviles y desktop */
    iframe {
        border: none !important;
        width: 100% !important;
        min-height: calc(100vh - 48px) !important;
        min-height: calc(100dvh - 48px) !important;
        height: 100% !important;
        display: block;
    }

    /* Ajustes para celulares en Streamlit */
    @media (max-width: 640px) {
        .pwa-topbar {
            flex-direction: column;
            align-items: stretch;
            padding: 8px 12px;
            gap: 6px;
            text-align: center;
        }
        .pwa-topbar .brand-info {
            justify-content: center;
            font-size: 0.78rem;
        }
        .pwa-topbar a.fullscreen-btn {
            justify-content: center;
            width: 100%;
            padding: 6px 12px;
        }
        iframe {
            min-height: calc(100vh - 78px) !important;
            min-height: calc(100dvh - 78px) !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Renderizar barra de utilidades superior adaptable
st.markdown("""
<div class="pwa-topbar">
    <div class="brand-info">
        <span>💰 <strong>FinanzFlow PWA</strong> | Admin: <code>admin</code> / Clave: <code>admin123</code></span>
    </div>
    <div>
        <a href="app/static/index.html" target="_blank" class="fullscreen-btn" title="Abrir en pestaña independiente para experiencia nativa a pantalla completa e instalación">
            📲 Modo Pantalla Completa PWA ↗
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# Incrustar la PWA mediante iframe con el path estático servido por Streamlit
if hasattr(st, "iframe"):
    st.iframe(src="app/static/index.html", height=950, width="stretch")
else:
    components.iframe(src="app/static/index.html", height=950, scrolling=True)

