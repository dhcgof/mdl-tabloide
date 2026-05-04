@echo off
chcp 65001 > nul
cls

echo.
echo ========================================================
echo 🚀 AUTO-UPLOAD - Monitor de Mudanças GitHub
echo ========================================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python não encontrado
    echo.
    echo 💡 Solução:
    echo    1. Instale Python: https://www.python.org/downloads/
    echo    2. Marque "Add Python to PATH"
    echo    3. Reinicie este script
    pause
    exit /b 1
)

echo ✓ Python encontrado

REM Verificar se está em repositório Git
if not exist ".git" (
    echo ❌ Não está em um repositório Git!
    echo.
    echo 💡 Execute primeiro:
    echo    git clone https://github.com/seu-usuario/mdl-tabloide.git
    echo    cd mdl-tabloide
    pause
    exit /b 1
)

echo ✓ Repositório Git encontrado
echo.

REM Verificar Git config
git config user.email >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Git não configurado!
    echo.
    echo Digite seu nome:
    set /p username=Nome:
    git config --global user.name "%username%"

    echo.
    echo Digite seu email GitHub:
    set /p email=Email:
    git config --global user.email "%email%"

    echo.
    echo ✓ Git configurado
)

echo.
echo 📦 Instalando dependências...
pip install watchdog -q

echo.
echo ========================================================
echo ✅ Iniciando monitoramento automático!
echo ========================================================
echo.

python auto_push.py

pause
