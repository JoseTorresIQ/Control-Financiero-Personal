@echo off
title SUBIR FINANZFLOW A GITHUB - SINCRONIZACIÓN TOTAL
chcp 65001 > nul
cd /d "%~dp0"

echo ======================================================================
echo    FINANZFLOW - SUBIR TODOS LOS ARCHIVOS A GITHUB & STREAMLIT CLOUD
echo ======================================================================
echo.

:: 1. Sincronizar activos estáticos para Streamlit Cloud
echo [1/4] Sincronizando todos los archivos estáticos hacia static/...
python -c "import streamlit_app; streamlit_app.sync_static_assets()" 2>nul
if %ERRORLEVEL% EQU 0 (
    echo   [OK] Archivos estáticos sincronizados correctamente.
) else (
    echo   [!] Nota: Continuando sincronización directa con git...
)

:: 2. Verificar o configurar el repositorio remoto
echo.
echo [2/4] Verificando repositorio remoto de GitHub...
git remote get-url origin >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo   No hay repositorio remoto configurado.
    set /p REPO_URL="  Ingresa la URL de tu repositorio GitHub (ej: https://github.com/usuario/repo.git): "
    if "%REPO_URL%"=="" (
        echo   [!] Operacion cancelada: No se proporciono URL.
        pause
        exit /b 1
    )
    git remote add origin %REPO_URL%
)

for /f "tokens=*" %%u in ('git remote get-url origin 2^>nul') do set CURRENT_REMOTE=%%u
echo   Destino remoto: %CURRENT_REMOTE%

:: 3. Agregar TODOS los archivos al control de versiones (nuevos, modificados y eliminados)
echo.
echo [3/4] Preparando todos los archivos del proyecto (git add -A)...
git add -A

:: Verificar si hay cambios pendientes de commit
git diff --cached --quiet
if %ERRORLEVEL% NEQ 0 (
    echo   Archivos detectados con cambios listos para subir:
    git status --short
    echo.
    set /p COMMIT_MSG="  Mensaje del commit (Presiona ENTER para usar mensaje automatico): "
    if "%COMMIT_MSG%"=="" (
        set COMMIT_MSG=Actualizacion de FinanzFlow PWA - %DATE% %TIME%
    )
    git commit -m "%COMMIT_MSG%"
    echo   [OK] Cambios confirmados localmente.
) else (
    echo   No hay modificaciones locales nuevas por confirmar. Verificando sincronizacion...
)

:: 4. Subir a GitHub
echo.
echo [4/4] Subiendo todos los archivos a GitHub (rama main)...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ======================================================================
    echo  [EXITO] ¡Todos los archivos fueron subidos correctamente a GitHub!
    echo ======================================================================
    echo.
    echo  - Repositorio: %CURRENT_REMOTE%
    echo  - Rama: main
    echo  - Streamlit Cloud detectara los cambios y actualizara tu app automaticamente.
    echo.
) else (
    echo.
    echo ======================================================================
    echo  [!] Error al subir a GitHub.
    echo ======================================================================
    echo  Verifica que tu conexion a internet este activa y que tus credenciales
    echo  de GitHub esten autenticadas en tu equipo.
    echo.
)

pause
