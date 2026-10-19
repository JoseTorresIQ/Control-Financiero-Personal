@echo off
title FINANZFLOW - PWA CONTROL FINANCIERO PERSONAL
chcp 65001 > nul
cd /d "%~dp0"

echo ======================================================================
echo    FINANZFLOW - CONTROL FINANCIERO PERSONAL (PWA OFFLINE-FIRST)
echo ======================================================================
echo.
echo  Iniciando servidor local y abriendo en navegador...
echo.

python server.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo  [!] Ocurrio un error al ejecutar el servidor con python.
    echo  Abriendo directamente en navegador...
    start index.html
)

pause
