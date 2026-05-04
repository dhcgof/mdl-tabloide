# 🚀 Guia de Auto-Upload Automático

Configurar seu repositório para fazer upload automático quando você alterar arquivos.

---

## 🎯 2 Formas de Automatizar

### **OPÇÃO 1: Script Local (Mais Controle)** ⭐ Recomendado
Monitora mudanças NO SEU COMPUTADOR e faz push automático.

### **OPÇÃO 2: GitHub Actions (Sem Script)**
Faz deploy automático do GitHub Pages quando há mudanças.

---

## ✅ OPÇÃO 1: Script Local (Auto-Push)

### **Passo 1: Copiar Arquivo**

1. Coloque o arquivo `auto_push.py` na raiz do seu repositório
2. Certifique-se que está no repositório local (pasta do git)

### **Passo 2: Instalar Dependência**

```bash
pip install watchdog
```

### **Passo 3: Executar Script**

**Windows:**
```bash
# Duplo clique em: AUTO_PUSH.bat
# OU execute no CMD/PowerShell:
python auto_push.py
```

**Mac/Linux:**
```bash
python3 auto_push.py
```

### **Como Funciona**

```
Você edita um arquivo
         ↓
Script detecta mudança (em tempo real)
         ↓
Aguarda 5 segundos
         ↓
Faz: git add .
Faz: git commit -m "🔄 Auto-upload: 2024-01-15 14:30:45"
Faz: git push origin main
         ↓
GitHub Pages atualiza em 1-2 minutos
```

### **O que Monitora**

✅ **Rastreia:**
- `.html` - Páginas web
- `.py` - Scripts Python
- `.bat` - Scripts Windows
- `.md` - Documentação
- Qualquer arquivo modificado

❌ **Ignora:**
- `.git/` - Pasta do Git
- `__pycache__/` - Cache Python
- `node_modules/` - Dependências npm
- Arquivos temporários

### **Parar o Script**

Pressione: `Ctrl + C`

---

## ⚙️ OPÇÃO 2: GitHub Actions (Deploy Automático)

**GitHub Actions** é um CI/CD integrado no GitHub que faz deploy automático sem script local.

### **Passo 1: Criar Pasta de Workflows**

No seu repositório local:
```
mkdir -p .github/workflows
```

### **Passo 2: Copiar Arquivo de Deploy**

Coloque o arquivo `deploy.yml` em: `.github/workflows/deploy.yml`

Estrutura final:
```
seu-repositorio/
├── .github/
│   └── workflows/
│       └── deploy.yml          ← Copie aqui!
├── index.html
├── EXTRATOR_PRODUTOS.html
└── README.md
```

### **Passo 3: Fazer Commit e Push**

```bash
git add .github/workflows/deploy.yml
git commit -m "Adicionar GitHub Actions deploy"
git push origin main
```

### **Passo 4: Ativar Pages (se não estiver)**

1. Acesse: https://github.com/seu-usuario/mdl-tabloide
2. Settings → Pages
3. Branch: `main` → `/` (root)
4. Save

### **Como Funciona**

```
Você faz: git push origin main
         ↓
GitHub Actions dispara automaticamente
         ↓
Faz build dos arquivos
         ↓
Deploy para GitHub Pages
         ↓
Página atualiza em 1-2 minutos
```

### **Monitorar Deploy**

1. Acesse seu repositório no GitHub
2. Clique em **Actions** (aba no topo)
3. Veja o status do deploy

---

## 🎯 Qual Escolher?

### **Escolha OPÇÃO 1 (Script Local) se:**
- ✅ Quer controle total
- ✅ Trabalha sempre no mesmo PC
- ✅ Quer ver commits automáticos em tempo real
- ✅ Prefere não usar GitHub Actions

### **Escolha OPÇÃO 2 (GitHub Actions) se:**
- ✅ Quer sem script local
- ✅ Trabalha em múltiplos PCs
- ✅ Quer deploy automático apenas
- ✅ Prefere configuração mínima

### **Escolha AMBAS se:**
- ✅ Quer máxima automação
- ✅ Script local + GitHub Actions redundância

---

## 🔒 Segurança & Credenciais

### **Para GitHub Actions (sem configuração necessária)**
- GitHub Actions usa token automático
- Sem necessidade de credentials
- Tudo funciona out-of-the-box

### **Para Script Local**
GitHub va pedir credenciais na primeira execução:

```bash
# Digite seu GitHub username ou token
username: seu-usuario
password: seu-token-pessoal
```

**Como criar token:**
1. GitHub → Settings (canto superior direito)
2. Developer settings → Personal access tokens
3. Generate new token (classic)
4. Marque: `repo` e `workflow`
5. Copie o token e use como "password"

---

## 🆘 Troubleshooting

### **Script não detecta mudanças**
```
Solução:
1. Salve arquivo com Ctrl+S (não apenas edite)
2. Aguarde 5 segundos
3. Verifique conexão de internet
4. Reinicie o script
```

### **"Git não configurado"**
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@github.com"
```

### **"Repositório não encontrado"**
```bash
# Certifique-se que está na pasta certa:
cd seu-repositorio
git status  # Deve mostrar "On branch main"
```

### **Push falha com erro de autenticação**
```
1. Gere um Personal Access Token no GitHub
2. Use o token como "password"
3. Ou: git config --global credential.helper store
```

### **GitHub Actions falha**
```
1. Verifique a aba "Actions" no GitHub
2. Clique no workflow que falhou
3. Veja o log de erro completo
4. Verifique se Pages está ativado
```

---

## 📊 Fluxo Completo

```
┌─────────────────────────────────────────┐
│  Você edita um arquivo                 │
│  (index.html, EXTRATOR_PRODUTOS.html)  │
└──────────────┬──────────────────────────┘
               ↓
        ┌──────────────┐
        │ Salva (Ctrl+S)
        └──────┬───────┘
               ↓
    ┌──────────────────────────┐
    │ Script monitora (se ativo)│
    └──────────┬───────────────┘
               ↓
    ┌──────────────────────────────────────┐
    │ Auto-Push para GitHub (5s delay)    │
    │ - git add .                        │
    │ - git commit                       │
    │ - git push                         │
    └──────────┬───────────────────────────┘
               ↓
    ┌──────────────────────────────────────┐
    │ GitHub Actions dispara (se configurado)
    │ - Build & Deploy automático        │
    │ - GitHub Pages atualiza            │
    └──────────┬───────────────────────────┘
               ↓
    ┌──────────────────────────────────────┐
    │ Seu site atualiza!                 │
    │ https://seu-usuario.github.io/...   │
    └──────────────────────────────────────┘
    
         ⏱️ Total: 1-2 minutos
```

---

## 💾 Arquivos Necessários

Para **OPÇÃO 1** (Script Local):
```
✅ auto_push.py          (fornecido)
✅ AUTO_PUSH.bat         (fornecido)
✅ watchdog (library)    (instalar com pip)
```

Para **OPÇÃO 2** (GitHub Actions):
```
✅ .github/workflows/deploy.yml  (fornecido)
```

---

## 🎉 Pronto!

Agora seu repositório está configurado para:
- ✅ Auto-upload quando você edita
- ✅ Deploy automático para GitHub Pages
- ✅ Página sempre atualizada

**Resultado:** Você edita → GitHub atualiza automaticamente!

---

## 📞 Dicas Profissionais

### **1. Usar em múltiplos PCs**
```bash
# Antes de começar a editar em outro PC:
git pull origin main

# Isso baixa as mudanças mais recentes
```

### **2. Monitorar Status**
```bash
# Ver status de mudanças não commitadas:
git status

# Ver histórico de commits:
git log --oneline
```

### **3. Desfazer Último Commit**
```bash
# Se cometeu um erro:
git reset --soft HEAD~1
git reset HEAD .  # desfazer git add
```

### **4. Limpar Histórico (avançado)**
```bash
# Se quiser resetar para um commit anterior:
git reset --hard <commit-hash>
git push -f origin main  # ⚠️ Force push (cuidado!)
```

---

## ✨ Resultado Final

```
📱 Seu Computador            🌐 GitHub.com           📄 GitHub Pages
  ┌─────────────────┐        ┌──────────────┐       ┌──────────────┐
  │ Edita arquivo   │───────→│ Repositório  │──────→│ Website ao   │
  │ (automático)    │        │ (automático) │       │ vivo         │
  └─────────────────┘        └──────────────┘       └──────────────┘
        ↓                           ↓                      ↓
   Auto-push                   Auto-deploy         Sempre atualizado
   (5s delay)              (GitHub Actions)         (1-2 min)
```

---

**Desenvolvido com ❤️ para MDL - Móveis do Lar**
