# ⚡ Guia Rápida - Sincronização Automática

Escolha a opção que melhor se adequa ao seu caso.

---

## 🎯 Qual Método Escolher?

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  VOCÊ QUER O MÁXIMO DE CONTROLE?                               │
│  ✓ Ver cada mudança em tempo real                              │
│  ✓ Deixar rodando enquanto trabalha                            │
│  ✓ Sem dependência do Git CLI                                  │
│                                                                 │
│         👉 USE: auto_sync_api.py (GitHub API)                  │
│                                                                 │
│─────────────────────────────────────────────────────────────────│
│                                                                 │
│  VOCÊ TRABALHA COM GIT E PREFERE SIMPLIFICAR?                  │
│  ✓ Quer usar git commands automaticamente                       │
│  ✓ Deixar rodando enquanto trabalha                            │
│  ✓ Tem Git CLI instalado                                       │
│                                                                 │
│         👉 USE: auto_push.py (Git CLI)                         │
│                                                                 │
│─────────────────────────────────────────────────────────────────│
│                                                                 │
│  VOCÊ QUER ZERO SCRIPTS LOCAIS?                                │
│  ✓ Deploy automático apenas quando faz git push               │
│  ✓ Sem script rodando continuamente                            │
│  ✓ Funciona em múltiplos computadores                          │
│                                                                 │
│         👉 USE: deploy.yml (GitHub Actions)                    │
│                                                                 │
│─────────────────────────────────────────────────────────────────│
│                                                                 │
│  VOCÊ QUER MÁXIMA AUTOMAÇÃO?                                   │
│  ✓ Script local (auto_sync_api.py) +                           │
│  ✓ GitHub Actions em backup                                    │
│                                                                 │
│         👉 USE: AMBAS as soluções                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 Arquivos Criados

### **Para GitHub API (Recomendado ⭐)**

| Arquivo | Tipo | O que faz | Windows | Mac/Linux |
|---------|------|----------|---------|-----------|
| `auto_sync_api.py` | Python | Sincroniza via API | ✓ | ✓ |
| `AUTO_SYNC_API.bat` | Batch | Lançador | ✓ | ✗ |
| `API_GITHUB_SETUP_GUIA.md` | Guia | Setup completo | ✓ | ✓ |

**Requisitos:**
- Python 3.6+
- PyGithub library
- Watchdog library
- GitHub Personal Access Token

**Tempo de Setup:** 5 minutos

---

### **Para Git CLI**

| Arquivo | Tipo | O que faz | Windows | Mac/Linux |
|---------|------|----------|---------|-----------|
| `auto_push.py` | Python | Auto-commit + push | ✓ | ✓ |
| `AUTO_PUSH.bat` | Batch | Lançador | ✓ | ✗ |
| `AUTO_UPLOAD_GUIA.md` | Guia | Setup + troubleshooting | ✓ | ✓ |

**Requisitos:**
- Python 3.6+
- Git CLI instalado
- Watchdog library
- Git configurado (`user.name`, `user.email`)

**Tempo de Setup:** 3 minutos

---

### **Para GitHub Actions**

| Arquivo | Tipo | Localização | O que faz |
|---------|------|-------------|----------|
| `deploy.yml` | YAML | `.github/workflows/` | Deploy automático ao fazer push |
| `AUTO_UPLOAD_GUIA.md` | Guia | Raiz do repo | Instruções de setup |

**Requisitos:**
- Nenhum! GitHub Actions é nativo

**Tempo de Setup:** 2 minutos

---

### **Documentação do Projeto**

| Arquivo | Descrição |
|---------|-----------|
| `README.md` | Documentação completa do projeto |
| `GITHUB_PAGES_GUIA.md` | Como fazer upload inicial do site |
| `index.html` | Página inicial com links para todas ferramentas |
| `VISUALIZADOR_TABLOIDE.html` | Visualizador PDF no navegador |
| `EXTRATOR_PRODUTOS.html` | Extrator interativo de produtos |
| `extrair_produtos_individuais.py` | Extrator automático em batch |
| `EXTRATOR_PRODUTOS.bat` | Lançador do extrator |

---

## 🚀 Setup Rápido - GitHub API (Recomendado)

### **5 Passos Simples:**

**1️⃣ Gerar Token no GitHub:**
- GitHub Settings → Developer settings → Personal access tokens
- Marque: `repo` e `workflow`
- Copie o token

**2️⃣ Copiar Arquivo:**
- Coloque `auto_sync_api.py` na raiz do repositório

**3️⃣ Instalar (primeira vez):**
```bash
pip install PyGithub watchdog
```

**4️⃣ Executar:**
**Windows:** Duplo clique em `AUTO_SYNC_API.bat`
**Mac/Linux:** `python3 auto_sync_api.py`

**5️⃣ Configurar (primeira execução):**
- Cola seu token GitHub
- Digite seu usuário
- Digite nome do repositório

✅ **Pronto! Começar a sincronizar**

---

## 📊 Comparação Rápida

```
                 GitHub API  │  Git CLI  │  Actions
─────────────────────────────┼───────────┼──────────
Sem Git CLI           ✓      │     ✗     │    ✓
Monitoração tempo real ✓     │     ✓     │    ✗
Setup (minutos)       5      │     3     │    2
Python necessário     ✓      │     ✓     │    ✗
Script rodando        ✓      │     ✓     │    ✗
Múltiplos PCs         ✗      │     ✗     │    ✓
Máxima automação      ✓      │     ✓     │    ✓
Recomendado           ⭐     │           │
─────────────────────────────┴───────────┴──────────
```

---

## 🔑 Lembre-se

### **GitHub API (Escolhido por você)**

✅ **Vantagens:**
- Não precisa Git CLI
- Mais robusto e confiável
- Controle total via API
- Funciona em qualquer sistema

⚠️ **Precisa de:**
- GitHub Personal Access Token
- PyGithub + Watchdog

---

## 📖 Documentação Detalhada

Para instruções **passo a passo** com exemplos e troubleshooting:

- **GitHub API:** `API_GITHUB_SETUP_GUIA.md`
- **Git CLI:** `AUTO_UPLOAD_GUIA.md`
- **Projeto Completo:** `README.md`
- **GitHub Pages:** `GITHUB_PAGES_GUIA.md`

---

## 🎯 Fluxo de Trabalho

```
1. SETUP INICIAL (5 minutos)
   ├─ Gerar token GitHub
   ├─ Copiar auto_sync_api.py
   ├─ Instalar dependências
   └─ Executar e configurar

2. USAR DIARIAMENTE (automático!)
   ├─ Editar arquivos localmente
   ├─ Script detecta mudanças
   ├─ Sincroniza via API
   └─ GitHub Pages atualiza (1-2 min)

3. DEIXAR RODANDO
   ├─ Mantenha o script ativo
   ├─ Minimize se quiser
   ├─ Ou use task scheduler
   └─ Sincronização 100% automática
```

---

## ✅ Checklist Inicial

- [ ] Li `API_GITHUB_SETUP_GUIA.md`
- [ ] Gerei GitHub Personal Access Token
- [ ] Copiei `auto_sync_api.py` para repositório
- [ ] Instalei `pip install PyGithub watchdog`
- [ ] Executei `AUTO_SYNC_API.bat` (ou script Python)
- [ ] Colei token quando solicitado
- [ ] Script está rodando e monitorando
- [ ] Testei: editei um arquivo e viu sincronizar
- [ ] Acessei GitHub e vi arquivo atualizado
- [ ] Seu site em GitHub Pages atualizou

---

## 🆘 Problemas?

| Problema | Solução |
|----------|---------|
| "Python não encontrado" | Instale Python e marque "Add to PATH" |
| "Bad credentials" | Token expirado? Gere novo |
| "Repository not found" | Verifique username/repo (case-sensitive) |
| "Arquivo não sincroniza" | Você salvou (Ctrl+S)? Aguarde 5 sec |
| "Erro de conexão" | Verifique internet e firewall |

**Detalhes completos:** Ver `API_GITHUB_SETUP_GUIA.md` seção Troubleshooting

---

## 🎉 Resultado Final

```
📝 Você edita arquivo local
    ↓
⚡ Script detecta (automático!)
    ↓
🔄 Sincroniza via GitHub API
    ↓
☁️  GitHub repositório atualiza
    ↓
🌐 GitHub Pages atualiza (1-2 min)
    ↓
✅ Seu site está atualizado!

(Tudo automático - você só trabalha!)
```

---

**Desenvolvido com ❤️ para MDL - Móveis do Lar**

Sua sincronização está pronta! 🚀
