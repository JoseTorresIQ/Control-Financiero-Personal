# 💰 FinanzFlow — PWA de Control Financiero Personal Avanzado

**FinanzFlow** es una Aplicación Web Progresiva (**Progressive Web App - PWA**) de última generación, diseñada para la gestión integral, ágil e inteligente de finanzas personales, presupuestos, planificación de deudas y metas de ahorro.

Desarrollada bajo la filosofía **Offline-First**, garantiza que todos tus datos se procesen y almacenen **exclusivamente de forma local y privada** en tu dispositivo (LocalStorage e IndexedDB), sin depender de servidores externos ni suscripciones.

---

## 🚀 Nuevas Funcionalidades Implementadas

### 1. 👑 Sistema Multi-Usuario con Administrador General & Aislamiento Total de Datos
- **Pantalla de Inicio de Sesión (Login):** Interfaz moderna y segura para ingresar con credenciales individuales.
- **Administrador General Maestro (Master Admin):**
  - **Usuario por defecto:** `admin`
  - **Contraseña por defecto:** `admin123`
  - Posee un panel exclusivo para **gestionar usuarios** (`👑 Gestión de Usuarios`).
- **Creación y Administración de Usuarios Adicionales:**
  - El Administrador General puede crear nuevos usuarios con su propio nombre, nombre de usuario (`@usuario`), contraseña y rol (**Usuario Individual** o **Administrador**).
  - Puede cambiar contraseñas, editar perfiles y dar de baja usuarios.
- **Aislamiento Total de la Información (100% Privado e Individual):**
  - Cada usuario tiene su propio espacio de almacenamiento aislado (`finanzflow_u_<id>_*` y `IndexedDB`).
  - Ningún usuario común puede ver los ingresos, gastos, cuentas, metas, deudas o comprobantes de otro usuario.
  - Al iniciar sesión con un usuario, la aplicación se reconfigura por completo mostrando únicamente su información personal.
- **Seguridad Criptográfica Local:**
  - Contraseñas protegidas mediante algoritmos de hashing **SHA-256** con la API nativa `crypto.subtle`. Las contraseñas nunca se guardan en texto plano.

### 2. 👁️ Modo Privacidad Inmediato
- Botón en la cabecera para ocultar/desenfocar al instante todos los montos, balances y patrimonios (`filter: blur(8px)`).
- Ideal para consultar tus finanzas en espacios públicos, transporte o en la oficina sin miradas indiscretas.

### 3. 🔒 Bloqueo por PIN de Seguridad (4 Dígitos)
- Bloqueo de acceso local con teclado numérico integrado estilo cajero automático / smartphone.
- Si está activado, la aplicación solo se desbloquea tras introducir el PIN correcto.
- Se configura y desactiva fácilmente desde la sección de **Ajustes**.

### 4. 🧠 Salud Financiera: Regla 50 / 30 / 20
- Clasificación automática y visual de tus gastos del mes:
  - 🟢 **50% Necesidades Básicas:** Vivienda, supermercado, servicios fijos, salud y transporte.
  - 🔵 **30% Deseos & Estilo de Vida:** Entretenimiento, salidas, ropa, streaming y compras no esenciales.
  - 🟣 **20% Ahorro & Metas:** Fondos de emergencia, aportes a objetivos o inversiones.
- Barra tricolor segmentada con diagnóstico inteligente sobre si tus costos fijos están en un nivel saludable.

### 5. 💵 Soporte Bimoneda Consolidado (Soles S/. y Dólares USD $)
- Cuentas independientes en Soles o en Dólares americanos.
- Tipo de cambio configurable (por defecto `1 USD = 3.75 PEN`).
- En el Dashboard y en la sección de Cuentas verás el **Patrimonio Total Consolidado** en tu moneda principal y su equivalente exacto en la moneda secundaria.

### 6. 📅 Calendario de Vencimientos & Pagos Recurrentes
- Vista de calendario mensual interactiva con indicadores visuales por día:
  - 🔴 Vencimiento de servicios (Luz, Agua, Internet, Alquiler).
  - 🟠 Cuotas mínimas de tarjetas o préstamos.
  - 🟢 Sueldos o ingresos programados.
  - 🟣 Fechas límite de metas de ahorro.
- Panel de **Agenda del Día** y lista de **Próximos Vencimientos a 15 días** con botón directo para *"Registrar / Pagar"*.

### 7. 🧾 Fotos de Comprobantes & Recibos con IndexedDB
- Adjunta fotos de tickets de compra, boletas o facturas directamente desde la cámara o galería al registrar una transacción.
- Almacenamiento eficiente de imágenes mediante **IndexedDB**, superando el límite tradicional de 5 MB de LocalStorage.
- Visor modal interactivo para consultar el comprobante en cualquier momento mediante el icono `🧾`.

### 8. 🧮 Herramientas Financieras & Simulador de Deudas
- **Simulador de Liquidación de Deudas:**
  - Registra tus tarjetas o préstamos con su saldo, pago mínimo y tasa de interés (TEA %).
  - Compara en tiempo real dos estrategias comprobadas:
    - 🔥 **Método Avalancha (Mayor Tasa Primero):** Minimiza matemáticamente los intereses pagados.
    - ❄️ **Método Bola de Nieve (Menor Saldo Primero):** Maximiza victorias psicológicas eliminando cuentas rápido.
  - Calcula los meses exactos hasta quedar libre de deudas y el dinero ahorrado en intereses.
- **Calculadora de Interés Compuesto:**
  - Proyecta el crecimiento de tu dinero a 1, 3, 5, 10 o 20 años con aportes mensuales y rendimiento anual estimado.

### 9. 📱 Experiencia Móvil Mobile-First & PWA Nativa Mejorada
- **Barra de Navegación Inferior Ergonómica:** Barra fija con soporte para áreas seguras de pantalla (`env(safe-area-inset-bottom)` en iPhone y Android), con accesos rápidos a **Inicio**, **Movs**, **Presupuesto**, **Metas** y **Más**.
- **Menú Drawer Deslizable ("Más"):** Panel tipo *Bottom Sheet* nativo que despliega con fluidez todas las secciones secundarias: Calendario & Pagos, Cuentas & Bancos, Deudas & Calculadoras, Usuarios (Admin), Ajustes, y atajos rápidos para cambiar tema, modo privacidad o cerrar sesión.
- **Formularios y Modales Adaptativos:** En smartphones, los diálogos se abren desde la parte inferior como hojas deslizables con botones de acción a tamaño completo para el pulgar.
- **Prevención de Zoom Forzado en iOS Safari:** Tipografía mínima de 16px en campos de formulario que evita el molesto auto-zoom de Safari al escribir.
- **Cabecera Móvil Limpia y Botón Flotante (+):** En pantallas pequeñas se oculta el botón de texto superior dejando un Floating Action Button (FAB) flotante sobre la barra de navegación, liberando espacio para el balance y gráficos.

---

## 📲 Cómo Instalar la PWA en tus Dispositivos

### En Windows / macOS (Google Chrome / Microsoft Edge):
1. Al abrir la app en `http://localhost:8000`, haz clic en el botón **"📲 Instalar App"** en la cabecera o en el icono de instalación de la barra de direcciones.
2. Se instalará como una aplicación nativa con ventana independiente sin barra de navegador.

### En Android / iOS:
- **Android (Chrome):** Toca el menú de tres puntos (⋮) y selecciona **"Instalar aplicación"** o **"Agregar a pantalla principal"**.
- **iPhone / iPad (Safari):** Presiona el botón **Compartir** y elige **"Agregar a pantalla de inicio"**.

---

## 💻 Instrucciones de Ejecución

Haz doble clic en cualquiera de los lanzadores:
- [`ejecutar_pwa_finanzas.bat`](file:///c:/Users/ADMIN/OneDrive/PYTHON/ejecutar_pwa_finanzas.bat) (en la raíz de `PYTHON`)
- [`ejecutar_pwa_finanzas.bat`](file:///c:/Users/ADMIN/OneDrive/PYTHON/20261019%20-%20PWA%20CONTROL%20FINANCIERO%20PERSONAL/ejecutar_pwa_finanzas.bat) (dentro de la carpeta del proyecto)

O por terminal:
```powershell
cd "c:\Users\ADMIN\OneDrive\PYTHON\20261019 - PWA CONTROL FINANCIERO PERSONAL"
python server.py
```

---

## 🚀 Servidor Centralizado (`server.py`) & Acceso Móvil por Wi-Fi

El servidor [`server.py`](file:///c:/Users/ADMIN/OneDrive/PYTHON/20261019%20-%20PWA%20CONTROL%20FINANCIERO%20PERSONAL/server.py) opera **100% con la Biblioteca Estándar de Python** (sin necesidad de instalar dependencias externas como Streamlit o Flask).

- **Acceso Local (PC):** `http://localhost:8000/index.html`
- **Acceso desde Celular o Tablet (Misma Wi-Fi):** `http://<IP_LOCAL>:8000/index.html`
  - El servidor detecta automáticamente tu IP local en la red Wi-Fi (ej. `http://192.168.1.15:8000/index.html`).
  - Solo necesitas abrir esa dirección en el navegador de tu celular y presionar **"Instalar aplicación"** o **"Agregar a pantalla principal"** para tener FinanzFlow como app nativa.
- **Soporte PWA Completo:** Configurado con cabeceras MIME explícitas para Service Worker (`sw.js`) y Web App Manifest (`manifest.json`), permitiendo funcionamiento offline total.
- **Puerto configurable:** Puedes cambiar el puerto mediante variable de entorno `PORT` o pasando el puerto como argumento: `python server.py 8080`.

---

## ☁️ Cómo Subir y Actualizar el Proyecto en GitHub

Todo el repositorio está configurado para sincronizarse y respaldarse en **GitHub** con 1 solo clic:

### Opción A (Automática mediante script):
1. Haz doble clic en [`subir_a_github.bat`](file:///c:/Users/ADMIN/OneDrive/PYTHON/20261019%20-%20PWA%20CONTROL%20FINANCIERO%20PERSONAL/subir_a_github.bat) (o desde la raíz de Python: [`subir_pwa_finanzas_github.bat`](file:///c:/Users/ADMIN/OneDrive/PYTHON/subir_pwa_finanzas_github.bat)).
2. El script ejecuta:
   - `git add -A` para agregar todos los archivos (nuevos, modificados o eliminados).
   - `git commit` con mensaje automático o personalizado.
   - `git push -u origin main` para subir todo al repositorio de GitHub.

### Opción B (Manual por consola):
```bash
cd "c:\Users\ADMIN\OneDrive\PYTHON\20261019 - PWA CONTROL FINANCIERO PERSONAL"
git add -A
git commit -m "Actualizacion de FinanzFlow PWA"
git push origin main
```

---

## 📁 Estructura Limpia del Proyecto

```text
20261019 - PWA CONTROL FINANCIERO PERSONAL/
├── css/
│   └── styles.css               # Diseño Glassmorphism, Responsive Móvil, Drawer y Modales
├── js/
│   ├── app.js                   # Controlador maestro, routing y Drawer sheet móvil
│   ├── auth.js                  # Autenticación, Hashing SHA-256, Gestión de Usuarios y Roles
│   ├── storage.js               # Persistencia LocalStorage + IndexedDB aislada por usuario
│   ├── security.js              # Bloqueo por PIN de 4 dígitos y Modo Privacidad (👁️)
│   ├── calendar.js              # Calendario mensual, agenda y vencimientos a 15 días
│   ├── calculators.js           # Simulador Avalancha vs Bola de Nieve e Interés Compuesto
│   ├── charts.js                # Motor de gráficos nativo Canvas (Offline-First)
│   ├── transactions.js          # Transacciones, bimoneda, filtros y comprobantes fotográficos
│   ├── budgets.js               # Presupuestos por categoría y alertas de consumo
│   └── goals.js                 # Metas de ahorro con aportes directos
├── icons/
│   ├── icon.svg                 # Ícono vectorial escalable
│   ├── icon-192.png             # Ícono estándar 192x192
│   ├── icon-512.png             # Ícono estándar 512x512
│   ├── icon-maskable-192.png    # Ícono adaptable Android
│   ├── icon-maskable-512.png    # Ícono adaptable Android
│   └── favicon-64.png           # Favicon para navegadores
├── index.html                   # Single Page Application (SPA) con Login, Drawer y vistas PWA
├── manifest.json                # Especificación PWA Web App Manifest
├── sw.js                        # Service Worker v1.4.0 (Offline-First y caché inteligente)
├── server.py                    # Servidor centralizado local y red Wi-Fi para móviles
├── ejecutar_pwa_finanzas.bat    # Lanzador directo en Windows
├── subir_a_github.bat           # Automatizador de subida y commit total a GitHub
├── requirements.txt             # Indicador de dependencias estándar (0 paquetes externos)
└── README.md                    # Documentación completa
```
