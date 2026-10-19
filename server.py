#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FinanzFlow PWA - Servidor Local Offline-First
Sirve la Progressive Web App con los tipos MIME correctos para Service Workers y Web App Manifest.
Abre automáticamente el navegador predeterminado en localhost.
"""

import sys
import os
import socket
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

class PWAHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Manejador HTTP con soporte explícito para Service Worker y Manifest PWA."""

    extensions_map = SimpleHTTPRequestHandler.extensions_map.copy()
    extensions_map.update({
        '.webmanifest': 'application/manifest+json',
        '.json': 'application/json',
        '.js': 'application/javascript; charset=utf-8',
        '.mjs': 'application/javascript; charset=utf-8',
        '.css': 'text/css; charset=utf-8',
        '.html': 'text/html; charset=utf-8',
        '.svg': 'image/svg+xml',
        '.png': 'image/png',
        '.ico': 'image/x-icon'
    })

    def end_headers(self):
        # Cabeceras para Service Worker y Caché adecuada en desarrollo local
        self.send_header('Service-Worker-Allowed', '/')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def find_available_port(start_port=8000, max_attempts=50):
    for port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return start_port

def run_server():
    # Asegurar que el directorio de trabajo sea la raíz de este proyecto
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    port = find_available_port(8000)
    server_address = ('127.0.0.1', port)
    url = f"http://localhost:{port}/index.html"

    print("=" * 70)
    print("     FINANZFLOW - PWA CONTROL FINANCIERO PERSONAL")
    print("=" * 70)
    print(f"[*] Directorio raíz: {base_dir}")
    print(f"[*] Servidor iniciado en: {url}")
    print("[*] Service Worker y Offline Caching listos.")
    print("[*] Presiona Ctrl+C en cualquier momento para detener el servidor.")
    print("=" * 70)

    # Abrir navegador automáticamente
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"[!] No se pudo abrir el navegador automáticamente: {e}")

    httpd = HTTPServer(server_address, PWAHTTPRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Servidor detenido por el usuario.")
        httpd.server_close()
        sys.exit(0)

if __name__ == '__main__':
    run_server()
