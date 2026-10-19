@echo off
title SUBIR FINANZFLOW A GITHUB
chcp 65001 > nul
cd /d "%~dp0"

echo ======================================================================
echo    FINANZFLOW - ASISTENTE PARA SUBIR A GITHUB Y DEPLOY STREAMLIT
echo ======================================================================
echo.
echo  Asegurate de haber creado un nuevo repositorio vacio en https://github.com/new
echo  (NO marques la casilla de agregar README, .gitignore o licencia, ya estan creados).
echo.
set /p REPO_URL="Pega aqui la URL de tu repositorio GitHub (ej: https://github.com/tu-usuario/finanzflow.git): "

if "%REPO_URL%"=="" (
    echo.
    echo  [!] No ingresaste ninguna URL. Operacion cancelada.
    pause
    exit /b
)

echo.
echo  Configurando origen remoto...
git remote remove origin 2>nul
git remote add origin %REPO_URL%

echo.
echo  Subiendo archivos a la rama 'main' de GitHub...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ======================================================================
    echo  [EXITO] Proyecto subido correctamente a GitHub!
    echo ======================================================================
    echo.
    echo  Proximos pasos para el Deploy en Streamlit Cloud:
    echo  1. Ve a: https://share.streamlit.io/
    echo  2. Inicia sesion con tu cuenta de GitHub.
    echo  3. Haz clic en "New app".
    echo  4. Selecciona tu repositorio y rama "main".
    echo  5. En "Main file path", escribe: streamlit_app.py
    echo  6. Haz clic en "Deploy!"
    echo.
) else (
    echo.
    echo  [!] Hubo un error al subir a GitHub.
    echo  Verifica que tengas permisos de escritura y que tus credenciales de GitHub esten activas.
)

pause
