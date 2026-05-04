# 🔑 Guia de Configuração - GitHub API Auto-Sync

Sincronize seus arquivos com GitHub usando **GitHub API** (sem necessidade do Git CLI!)

---

## 📋 Requisitos Mínimos

- ✅ Python 3.6+
- ✅ GitHub Personal Access Token
- ✅ Acesso à internet
- ✅ Repositório no GitHub (já criado)

---

## 🔐 Passo 1: Gerar GitHub Personal Access Token

### **No GitHub.com:**

1. Clique na **foto de perfil** (canto superior direito)
2. Vá para **Settings**
3. Na barra lateral esquerda, clique em **Developer settings**
4. Clique em **Personal access tokens**
5. Clique em **Tokens (classic)** (ou **Generate new token**)
6. Clique em **Generate new token (classic)**

### **Configure o Token:**

| Campo | Valor |
|-------|-------|
| **Token name** | `mdl-tabloide-sync` |
| **Expiration** | 90 days (ou conforme sua preferência) |

### **Permissões Necessárias (marque):**

```
☑ repo (full control)
  ☑ repo:status
  ☑ repo_deployment
  ☑ public_repo
  ☑ repo:invite
  ☑ security_events

☑ workflow (if using GitHub Actions)
```

### **Gerar Token:**

7. Role até o final
8. Clique em **Generate token**
9. **COPIE O TOKEN IMEDIATAMENTE** (você só verá uma vez!)
   - Aparece assim: `ghp_1A2B3C4D5E6F7G8H9I0J...`

⚠️ **IMPORTANTE:** Guarde o token em um local seguro (não compartilhe!)

---

## 🚀 Passo 2: Preparar Arquivos

### **Estrutura de Pastas:**

```
seu-repositorio/
├── auto_sync_api.py        ← Copie aqui
├── index.html
├── VISUALIZADOR_TABLOIDE.html
├── EXTRATOR_PRODUTOS.html
└── (outros arquivos do projeto)
```

### **Copiar Arquivo:**

1. Copie o arquivo `auto_sync_api.py` para a **raiz** do seu repositório local
2. Certifique-se que você está na pasta do repositório:
   ```bash
   cd caminho/para/seu-repositorio
   ```

---

## 🔧 Passo 3: Instalar Dependência (primeira vez)

Execute **uma única vez** para instalar a biblioteca PyGithub:

**Windows:**
```bash
pip install PyGithub watchdog
```

**Mac/Linux:**
```bash
pip3 install PyGithub watchdog
```

✓ Pronto! Agora está tudo configurado.

---

## ▶️ Passo 4: Executar Script

### **Windows:**

**Opção A - Duplo clique (mais fácil):**
1. Crie um arquivo `INICIAR_SYNC.bat` na mesma pasta:
   ```batch
   @echo off
   python auto_sync_api.py
   pause
   ```
2. Duplo clique no arquivo `.bat`

**Opção B - Linha de comando:**
```bash
python auto_sync_api.py
```

### **Mac/Linux:**

```bash
python3 auto_sync_api.py
```

---

## 🔐 Passo 5: Primeira Execução (Configuração Interativa)

Quando rodar pela primeira vez, o script pedirá informações:

```
🚀 AUTO-SYNC COM GITHUB API
============================================================

🔐 Autenticando com GitHub API...
```

**Digite quando solicitado:**

```
GitHub Personal Access Token: [COLE_SEU_TOKEN_AQUI]
Seu usuário GitHub: [seu-usuario-github]
Nome do repositório: [mdl-tabloide]
```

**Exemplo completo:**
```
GitHub Personal Access Token: ghp_1A2B3C4D5E6F7G8H9I0J...
Seu usuário GitHub: diego-github
Nome do repositório: mdl-tabloide
```

✓ **Configuração salva** em `.github-sync.json`

---

## 👀 Passo 6: Monitoramento (Deixar Rodando)

Após a configuração inicial, você verá:

```
============================================================
👀 Monitorando mudanças...
============================================================

📌 Funcionamento:
  • Detecta mudanças em tempo real
  • Aguarda 5 segundos para agrupar mudanças
  • Sincroniza via GitHub API
  • Suporta criar, atualizar e deletar arquivos

💡 Para parar: Pressione Ctrl+C
============================================================
```

**Agora:**
- Edite qualquer arquivo no seu repositório
- O script detectará automaticamente
- Criará/atualizará o arquivo no GitHub via API
- GitHub Pages atualizará em 1-2 minutos

### **Exemplo de Output:**

```
📝 Modificado: index.html
📝 Modificado: style.css

🔄 Sincronizando: index.html (update)
📝 Autenticado como: diego-github
✓ Repositório: diego-github/mdl-tabloide
✓ Atualizado: index.html

🔄 Sincronizando: style.css (update)
✓ Atualizado: style.css
```

---

## 📁 Arquivo de Configuração

Após primeira execução, um arquivo `.github-sync.json` é criado:

```json
{
  "token": "ghp_1A2B3C4D5E6F7G8H9I0J...",
  "owner": "seu-usuario",
  "repo": "mdl-tabloide"
}
```

⚠️ **ATENÇÃO:** 
- Não compartilhe este arquivo (contém seu token!)
- Adicione ao `.gitignore`:
  ```
  .github-sync.json
  ```

---

## 🛑 Parar o Script

Pressione: **`Ctrl + C`**

```
^C

⏹️  Parando sincronização...
✓ Auto-sync desativado
```

---

## 📊 O que o Script Faz

### **Monitora:**
✅ Mudanças em **arquivos locais**
✅ Criação de **novos arquivos**
✅ **Exclusão de arquivos**

### **Ignora Automaticamente:**
❌ `.git/` - Pasta do Git
❌ `__pycache__/` - Cache Python
❌ `node_modules/` - Dependências npm
❌ `.venv/`, `venv/` - Ambientes virtuais
❌ Arquivos `.pyc`, `.tmp`, `.log`, etc.

### **Aguarda 5 segundos:**
Para agrupar múltiplas mudanças em uma sincronização

### **Sincroniza via GitHub API:**
Sem necessidade do Git CLI!

---

## 🚀 Fluxo Completo

```
┌─────────────────────────────────┐
│ Você edita um arquivo local     │
│ (ex: index.html)                │
└─────────────┬───────────────────┘
              ↓
    ┌──────────────────────┐
    │ Script detecta       │
    │ (em tempo real)      │
    └──────┬───────────────┘
           ↓
    ┌──────────────────────────┐
    │ Aguarda 5 segundos       │
    │ (para agrupar mudanças)  │
    └──────┬──────────────────┘
           ↓
    ┌──────────────────────────────────────┐
    │ Sincroniza via GitHub API            │
    │ - Autentica com token               │
    │ - Lê arquivo local                  │
    │ - Cria/atualiza no GitHub           │
    │ - Log de operação                   │
    └──────┬───────────────────────────────┘
           ↓
    ┌──────────────────────────────────────┐
    │ GitHub Pages atualiza               │
    │ (1-2 minutos)                       │
    └──────────────────────────────────────┘
    
         ✅ Arquivo sincronizado!
```

---

## 🔍 Verificar Status

### **Logs em Tempo Real:**

O script mostra tudo que está fazendo:
- Autenticação
- Detecção de mudanças
- Operações de sincronização
- Erros (se houver)

### **Arquivo de Configuração:**

```bash
# Ver configuração salva
cat .github-sync.json

# (Não edite manualmente - é gerado automaticamente)
```

### **No GitHub:**

1. Acesse seu repositório: https://github.com/seu-usuario/mdl-tabloide
2. Verifique se os arquivos foram atualizados
3. Histórico de commits mostra "Auto-update" com timestamp

---

## 🆘 Troubleshooting

### **"Erro de autenticação"**

```
❌ Erro de autenticação: Bad credentials (401)
```

**Solução:**
1. Verifique se o token está correto
2. Gere um novo token se expirou
3. Delete `.github-sync.json` e execute novamente
4. Teste a conexão:
   ```bash
   # Teste o token no PowerShell/Terminal:
   curl -H "Authorization: token SEU_TOKEN" https://api.github.com/user
   ```

### **"Repositório não encontrado"**

```
❌ Erro de autenticação: Repository not found (404)
```

**Solução:**
1. Verifique username e repo name (case-sensitive)
2. Certifique-se que o repositório existe no GitHub
3. Verifique permissões do token (precisa de `repo`)
4. Execute novamente e verifique os valores

### **"Arquivo não encontrado no repo"**

```
⚠️  Arquivo não encontrado no repo: novo-arquivo.txt
```

**Solução:**
Normal na primeira execução - arquivo será criado no próximo sync
Aguarde 5 segundos e o arquivo será criado

### **Script não detecta mudanças**

**Solução:**
1. Certifique-se que **salvou** o arquivo (Ctrl+S)
2. Não apenas editou, mas salvou
3. Aguarde 5 segundos
4. Verifique a conexão de internet
5. Reinicie o script

### **Tokens aparecendo nos logs**

**Segurança:**
O token é mascarado nos logs de sucesso, mas:
- Não coloque o token em commits
- Mantenha `.github-sync.json` privado
- Adicione ao `.gitignore`:
  ```
  .github-sync.json
  ```

---

## ⚡ Dicas Profissionais

### **1. Múltiplos Computadores**

Se trabalhar em mais de um PC:

```bash
# Antes de começar em outro PC:
git pull origin main

# Isso sincroniza as mudanças
```

### **2. Parar o Script Temporariamente**

Pressione `Ctrl+C` quando precisar editar sem sincronizar

### **3. Monitorar Sem Deixar Aberto**

Use GitHub Actions em paralelo (veja `deploy.yml`)

### **4. Renovar Token**

Se o token expirou:
1. Gere novo no GitHub Settings
2. Delete `.github-sync.json`
3. Execute novamente com novo token

### **5. Verificar Logs Detalhados**

Redirecione para arquivo:

**Windows:**
```bash
python auto_sync_api.py > sync.log 2>&1
```

**Mac/Linux:**
```bash
python3 auto_sync_api.py | tee sync.log
```

---

## 🎯 Checklist de Sucesso

- ✅ GitHub Personal Access Token gerado
- ✅ `auto_sync_api.py` copiado para repositório
- ✅ PyGithub e watchdog instalados
- ✅ Script executado e configurado
- ✅ `.github-sync.json` criado
- ✅ Script rodando e monitorando
- ✅ Teste: edite um arquivo e veja sincronizar

**Se todos os itens estão marcados: você está pronto! 🎉**

---

## 📞 Próximas Etapas

### **1. Deixe o Script Rodando**
- Mantenha em um terminal aberto enquanto trabalha
- Pode minimizar a janela

### **2. GitHub Pages Atualiza Automaticamente**
- Seu site https://seu-usuario.github.io/mdl-tabloide/ atualiza em 1-2 minutos

### **3. Opcional: GitHub Actions**
- Se quiser redundância, configure também `deploy.yml`
- Veja `AUTO_UPLOAD_GUIA.md` para mais detalhes

### **4. Coloque em Produção**
- Quando estiver confiante, mantenha o script rodando em background
- Use task scheduler (Windows) ou cron (Mac/Linux) para iniciar automaticamente

---

## 🔗 Recursos Adicionais

- **GitHub API Docs**: https://docs.github.com/en/rest
- **PyGithub Documentation**: https://pygithub.readthedocs.io/
- **GitHub Personal Access Tokens**: https://github.com/settings/tokens

---

**Desenvolvido com ❤️ para MDL - Móveis do Lar**

Auto-sincronização ativada! 🚀
