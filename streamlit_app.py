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
            if not os.path.exists(dst) or os.path.getmtime(src) > os.path.getmtime(dst):
                shutil.copy2(src, dst)

    dirs_to_sync = ["css", "js", "icons"]
    for d in dirs_to_sync:
        src_dir = os.path.join(base_dir, d)
        dst_dir = os.path.join(static_dir, d)
        if os.path.exists(src_dir):
            if not os.path.exists(dst_dir):
                shutil.copytree(src_dir, dst_dir)
            else:
                # Comprobar si hay cambios
                for root, _, files in os.walk(src_dir):
                    rel_path = os.path.relpath(root, src_dir)
                    target_root = os.path.join(dst_dir, rel_path)
                    os.makedirs(target_root, exist_ok=True)
                    for file in files:
                        s_file = os.path.join(root, file)
                        d_file = os.path.join(target_root, file)
                        if not os.path.exists(d_file) or os.path.getmtime(s_file) > os.path.getmtime(d_file):
                            shutil.copy2(s_file, d_file)

sync_static_assets()

# Estilos para integración fluida sin bordes ni padding excesivo
st.markdown("""
<style>
    /* Ocultar elementos estándar de Streamlit para apariencia limpia */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Contenedor principal a pantalla completa */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    
    /* Barra superior informativa opcional */
    .pwa-topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #1e293b;
        color: #f8fafc;
        padding: 8px 16px;
        font-family: system-ui, -apple-system, sans-serif;
        font-size: 0.85rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .pwa-topbar a {
        color: #38bdf8;
        text-decoration: none;
        font-weight: 600;
        margin-left: 10px;
    }
    .pwa-topbar a:hover {
        text-decoration: underline;
    }

    /* Iframe adaptativo y fluido */
    iframe {
        border: none !important;
        width: 100% !important;
        min-height: calc(100vh - 40px) !important;
        display: block;
    }
</style>
""", unsafe_allow_html=True)

# Renderizar barra de utilidades superior
st.markdown("""
<div class="pwa-topbar">
    <div>
        <span>💰 <strong>FinanzFlow PWA</strong> | Admin: <code>admin</code> / Clave: <code>admin123</code></span>
    </div>
    <div>
        <a href="app/static/index.html" target="_blank" title="Abrir en pestaña independiente para pantalla completa">🚀 Abrir Modo Nativo Pantalla Completa ↗</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Incrustar la PWA mediante iframe con el path estático servido por Streamlit
components.iframe(src="app/static/index.html", height=950, scrolling=True)
