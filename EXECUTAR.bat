@echo off
chcp 65001 > nul
echo.
echo ==========================================
echo 🎯 GERADOR DE ANÚNCIOS - MDL Móveis do Lar
echo ==========================================
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
echo.

REM Verificar se o PDF existe
if not exist "MDL TABLOIDE MENSAL*.pdf" (
    echo ❌ Arquivo PDF não encontrado!
    echo.
    echo 💡 Por favor:
    echo    1. Copie o arquivo: MDL TABLOIDE MENSAL (32).pdf
    echo    2. Coloque na mesma pasta deste script
    echo    3. Execute este arquivo novamente
    pause
    exit /b 1
)

echo ✓ Arquivo PDF encontrado
echo.
echo 📦 Instalando/Verificando bibliotecas necessárias...
echo.

pip install pdf2image Pillow python-docx pdfplumber -q

if %errorlevel% neq 0 (
    echo ❌ Erro na instalação de bibliotecas
    pause
    exit /b 1
)

echo ✓ Bibliotecas prontas
echo.
echo ⏳ Processando PDF (pode levar alguns minutos)...
echo.

python gerar_anuncios.py

if %errorlevel% equ 0 (
    echo.
    echo ✅ SUCESSO! Arquivo criado: Anuncios_com_Imagens.docx
    echo.
    echo 💡 Próximos passos:
    echo    1. O arquivo está em: %cd%\Anuncios_com_Imagens.docx
    echo    2. Abra com Microsoft Word
    echo    3. Edite e customize conforme necessário
    echo.
) else (
    echo.
    echo ❌ Erro durante processamento
    echo    Verifique se Poppler está instalado:
    echo    https://github.com/oschwartz10612/poppler-windows/releases/
    echo.
)

pause
