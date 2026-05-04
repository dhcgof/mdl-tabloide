@echo off
chcp 65001 > nul
cls

echo.
echo ========================================================
echo 🔐 AUTO-SYNC GitHub API
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

REM Verificar se arquivo auto_sync_api.py existe
if not exist "auto_sync_api.py" (
    echo ❌ Arquivo 'auto_sync_api.py' não encontrado!
    echo.
    echo 💡 Copie o arquivo auto_sync_api.py para esta pasta
    pause
    exit /b 1
)

echo ✓ Script encontrado

echo.
echo 📦 Instalando dependências (primeira vez)...
pip install PyGithub watchdog -q

echo.
echo ========================================================
echo ✅ Iniciando sincronização automática com GitHub API!
echo ========================================================
echo.
echo 🔑 Primeira execução:
echo    Digite seu GitHub Personal Access Token
echo    Seu usuário GitHub
echo    Nome do repositório
echo.
echo 💡 Próximas execuções:
echo    Usa configuração salva em .github-sync.json
echo.

python auto_sync_api.py

pause
