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

## 📁 Estructura del Proyecto

```text
20261019 - PWA CONTROL FINANCIERO PERSONAL/
├── css/
│   └── styles.css               # Diseño Glassmorphism, Login, PIN, Calendario y Calculadoras
├── js/
│   ├── app.js                   # Controlador maestro, routing y widget 50/30/20
│   ├── auth.js                  # Autenticación, Hashing SHA-256, Gestión de Usuarios y Roles
│   ├── storage.js               # Persistencia LocalStorage + IndexedDB aislada por usuario
│   ├── security.js              # Bloqueo por PIN de 4 dígitos y Modo Privacidad (👁️)
│   ├── calendar.js              # Calendario mensual, agenda y vencimientos a 15 días
│   ├── calculators.js           # Simulador Avalancha vs Bola de Nieve e Interés Compuesto
│   ├── charts.js                # Motor de gráficos nativo Canvas (Offline-First)
│   ├── transactions.js          # Transacciones, bimoneda, filtros y subida de comprobantes
│   ├── budgets.js               # Presupuestos por categoría y alertas de consumo
│   └── goals.js                 # Metas de ahorro con aportes directos
├── icons/
│   ├── icon.svg                 # Ícono vectorial escalable
│   ├── icon-192.png             # Ícono estándar 192x192
│   ├── icon-512.png             # Ícono estándar 512x512
│   ├── icon-maskable-192.png    # Ícono adaptable Android
│   ├── icon-maskable-512.png    # Ícono adaptable Android
│   └── favicon-64.png           # Favicon para navegadores
├── index.html                   # Single Page Application (SPA) con Login y vistas integradas
├── manifest.json                # Especificación PWA Web App Manifest
├── sw.js                        # Service Worker v1.3.0 (Offline-First)
├── server.py                    # Servidor local con apertura automática
├── ejecutar_pwa_finanzas.bat    # Lanzador por lotes
└── README.md                    # Documentación completa
```
