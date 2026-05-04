@echo off
chcp 65001 > nul
cls

echo.
echo ========================================================
echo 🎯 EXTRATOR DE PRODUTOS INDIVIDUAIS - MDL Móveis do Lar
echo ========================================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado no PATH
    echo.
    echo 💡 Solução:
    echo    1. Instale Python de https://www.python.org/downloads/
    echo    2. MARQUE "Add Python to PATH" durante instalação
    echo    3. Reinicie este script
    pause
    exit /b 1
)

echo ✓ Python encontrado

REM Verificar se o PDF existe
if not exist "MDL TABLOIDE MENSAL*.pdf" (
    echo ❌ Arquivo PDF não encontrado!
    echo.
    echo 💡 Por favor:
    echo    1. Baixe: MDL TABLOIDE MENSAL (32).pdf
    echo    2. Coloque na mesma pasta deste script
    echo    3. Execute este arquivo novamente
    pause
    exit /b 1
)

echo ✓ Arquivo PDF encontrado
echo.
echo 📦 Instalando/Verificando bibliotecas...
pip install pdf2image Pillow -q

echo.
echo ⏳ Extraindo produtos (pode levar 2-5 minutos)...
echo.

python extrair_produtos_individuais.py

if %errorlevel% equ 0 (
    echo.
    echo ✅ SUCESSO!
    echo.
    echo 📁 Pasta criada: produtos_individuais
    echo 🖼️  31 imagens de produtos extraídas
    echo.
    echo 💡 Próximos passos:
    echo    1. Abra a pasta "produtos_individuais"
    echo    2. Verifique as imagens PRODUTO_01.jpg até PRODUTO_31.jpg
    echo    3. Use as imagens em anúncios, redes sociais, etc.
    echo.
) else (
    echo.
    echo ❌ Erro durante extração
    echo.
)

pause
