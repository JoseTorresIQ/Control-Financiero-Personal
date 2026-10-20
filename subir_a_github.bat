@echo off
title SUBIR FINANZFLOW A GITHUB - SINCRONIZACIÓN TOTAL
chcp 65001 > nul
cd /d "%~dp0"

echo ======================================================================
echo    FINANZFLOW - SUBIR TODOS LOS ARCHIVOS A GITHUB
echo ======================================================================
echo.

:: 1. Verificar o configurar el repositorio remoto
echo [1/3] Verificando repositorio remoto de GitHub...
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

:: 2. Agregar TODOS los archivos al control de versiones (nuevos, modificados y eliminados)
echo.
echo [2/3] Preparando todos los archivos del proyecto (git add -A)...
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

:: 3. Subir a GitHub
echo.
echo [3/3] Subiendo todos los archivos a GitHub (rama main)...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ======================================================================
    echo  [EXITO] ¡Todos los archivos fueron subidos correctamente a GitHub!
    echo ======================================================================
    echo.
    echo  - Repositorio: %CURRENT_REMOTE%
    echo  - Rama: main
    echo  - Servidor PWA centralizado en: server.py
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
