# 📚 Guia Completo - GitHub Pages

## O que é GitHub Pages?

GitHub Pages é um serviço **gratuito** que hospeda sites estáticos diretamente do GitHub. Perfeito para nossas ferramentas web!

**Sua página ficará em:** `https://seu-usuario.github.io/mdl-tabloide/`

---

## ✅ Pré-requisitos

1. **Conta GitHub** (gratuita em https://github.com)
2. **Git instalado** (https://git-scm.com/downloads)
3. Os arquivos prontos:
   - `index.html` (página inicial)
   - `EXTRATOR_PRODUTOS.html` (extrator interativo)
   - `VISUALIZADOR_TABLOIDE.html` (visualizador)
   - `extrair_produtos_individuais.py` (script Python)
   - `EXTRAIR_PRODUTOS.bat` (script Windows)
   - `README.md` (documentação)

---

## 🚀 Passo-a-Passo para GitHub Pages

### **PASSO 1: Criar Repositório no GitHub**

1. Acesse https://github.com/new
2. Preencha:
   - **Repository name:** `mdl-tabloide`
   - **Description:** "Ferramentas para extrair imagens de produtos do tabloide MDL"
   - **Public** (não privado - necessário para Pages grátis)
   - Não marque "Initialize with README" (faremos depois)
3. Clique **"Create repository"**

---

### **PASSO 2: Preparar Arquivos Localmente**

```bash
# 1. Criar pasta do projeto
mkdir mdl-tabloide
cd mdl-tabloide

# 2. Copiar todos os arquivos HTML, Python e Batch para esta pasta
# Arquivos necessários:
# - index.html
# - EXTRATOR_PRODUTOS.html
# - VISUALIZADOR_TABLOIDE.html
# - extrair_produtos_individuais.py
# - EXTRAIR_PRODUTOS.bat
# - README.md (vamos criar)
```

---

### **PASSO 3: Inicializar Git**

```bash
# Na pasta mdl-tabloide, execute:

git init
git add .
git commit -m "Commit inicial: Ferramentas MDL Tabloide"
git branch -M main
git remote add origin https://github.com/seu-usuario/mdl-tabloide.git
git push -u origin main
```

**Substitua `seu-usuario` pelo seu usuário do GitHub!**

---

### **PASSO 4: Ativar GitHub Pages**

1. Acesse seu repositório: `https://github.com/seu-usuario/mdl-tabloide`
2. Clique em **"Settings"** (⚙️ no topo)
3. Na esquerda, clique em **"Pages"**
4. Em **"Source"**:
   - Branch: `main`
   - Folder: `/ (root)`
5. Clique **"Save"**

**Aguarde 1-2 minutos...**

Sua página estará em: `https://seu-usuario.github.io/mdl-tabloide/`

---

## 📝 Criar um Bom README.md

Crie um arquivo `README.md` na raiz do repositório:

```markdown
# 🎯 MDL Tabloide - Extrator de Produtos

Ferramentas para extrair e visualizar imagens de produtos do tabloide MDL - Móveis do Lar.

## 🌐 Acesse Online

👉 **[mdl-tabloide.github.io](https://seu-usuario.github.io/mdl-tabloide/)**

## 🎯 Ferramentas Disponíveis

### 1. Extrator Automático ⚡
- Extrai todos os 31 produtos em um clique
- Divide em grid, recorta e redimensiona
- **Arquivo:** `extrair_produtos_individuais.py`
- **Tempo:** 2-5 minutos

### 2. Extrator Interativo 🎨
- Interface visual no navegador
- Selecione cada produto manualmente
- **Arquivo:** `EXTRATOR_PRODUTOS.html`
- **Tempo:** Controlado por você

### 3. Visualizador 👁️
- Apenas visualize o PDF
- Baixe as páginas como imagens
- **Arquivo:** `VISUALIZADOR_TABLOIDE.html`

## ⚙️ Requisitos

### Para ferramentas web (no navegador):
- ✓ Navegador moderno (Chrome, Firefox, Edge, Safari)
- ✓ Nada para instalar!

### Para script Python:
- ✓ Python 3.7+
- ✓ Bibliotecas: `pdf2image`, `Pillow`
- ✓ Poppler (Windows)

## 📥 Como Usar

### Online (Recomendado):
1. Acesse a página no link acima
2. Use qualquer uma das ferramentas web
3. Pronto! Sem instalações

### Localmente (Python):
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/mdl-tabloide.git
   cd mdl-tabloide
   ```

2. Instale dependências:
   ```bash
   pip install pdf2image Pillow
   ```

3. Execute:
   ```bash
   python extrair_produtos_individuais.py
   ```

## 📊 Recursos

- ✅ 31 produtos extraídos automaticamente
- ✅ Imagens em alta qualidade (500x500px)
- ✅ Remoção automática de espaço branco
- ✅ Nomes de arquivo organizados
- ✅ Interface intuitiva

## 🏪 MDL - Móveis do Lar

Ferramentas desenvolvidas para otimizar a extração de imagens de produtos.

---

**Versão 1.0** | Desenvolvido com ❤️
```

---

## 🔄 Atualizações Futuras

Se precisar fazer mudanças:

```bash
# 1. Edite os arquivos localmente
# 2. Commit e push

git add .
git commit -m "Descrição das mudanças"
git push origin main

# A página atualiza automaticamente em 1-2 minutos!
```

---

## ✅ Checklist Final

- [ ] Conta GitHub criada
- [ ] Git instalado no PC
- [ ] Repositório criado em GitHub
- [ ] Arquivos salvos na pasta local
- [ ] `git init`, `git add`, `git commit` executados
- [ ] `git push` executado para enviar
- [ ] GitHub Pages ativado nas Settings
- [ ] Página acessível em `https://seu-usuario.github.io/mdl-tabloide/`

---

## 🆘 Troubleshooting

### "Página não carrega"
- Aguarde 2-3 minutos após ativar Pages
- Verifique se o repositório é **Public**
- Confirme que a branch é `main`

### "Botões não funcionam"
- Certifique-se que a URL está correta
- Limpe cache do navegador (Ctrl+Shift+Del)
- Tente em outro navegador

### "Erro ao fazer push"
- Verifique credenciais do GitHub
- Use token ao invés de senha (configurar no GitHub)
- Tente: `git config --global user.email "seu-email@github.com"`

---

## 🎉 Pronto!

Sua plataforma de ferramentas está no ar! 

Compartilhe a URL: `https://seu-usuario.github.io/mdl-tabloide/`

---

**Dúvidas?** Consulte a documentação oficial: https://docs.github.com/pt/pages
