# 🎯 MDL Tabloide - Extrator de Produtos

![Badge](https://img.shields.io/badge/Status-Ativo-green) ![Badge](https://img.shields.io/badge/Versão-1.0-blue) ![Badge](https://img.shields.io/badge/Licença-MIT-orange)

Ferramentas poderosas e gratuitas para extrair e visualizar imagens de produtos do tabloide MDL - Móveis do Lar.

## 🌐 Acesse Online

**[👉 https://seu-usuario.github.io/mdl-tabloide/]()**

Abra no navegador e comece a usar AGORA - sem instalações necessárias!

---

## 📦 O que tem aqui?

### 1. **Extrator Automático** ⚡⚡⚡
Extrai todos os 31 produtos de uma vez!

- ✅ Divide o PDF em grid automaticamente
- ✅ Recorta cada produto
- ✅ Remove espaço branco
- ✅ Redimensiona para 500x500px
- ✅ Salva como: PRODUTO_01.jpg até PRODUTO_31.jpg
- ⏱️ Tempo: 2-5 minutos
- 📁 Arquivo: `extrair_produtos_individuais.py`

**Uso:**
```bash
python extrair_produtos_individuais.py
```

### 2. **Extrator Interativo** 🎨
Interface visual para controle total!

- ✅ Carregue o PDF no navegador
- ✅ Veja lista de todos os 31 produtos
- ✅ Selecione cada produto visualmente
- ✅ Desenhe retângulo de seleção
- ✅ Salve com nome personalizado
- ⏱️ Tempo: Controlado por você
- 📁 Arquivo: `EXTRATOR_PRODUTOS.html`

**Uso:**
1. Abra `EXTRATOR_PRODUTOS.html` no navegador
2. Clique "📂 Carregar PDF"
3. Selecione e recorte cada produto

### 3. **Visualizador** 👁️
Apenas visualize e baixe as páginas

- ✅ Carregue qualquer PDF
- ✅ Navegue entre páginas
- ✅ Baixe imagens em alta qualidade
- ✅ Interface limpa e simples
- 📁 Arquivo: `VISUALIZADOR_TABLOIDE.html`

---

## 🚀 Quick Start

### **Opção 1: Online (Recomendado)** - 30 segundos
```
1. Acesse: https://seu-usuario.github.io/mdl-tabloide/
2. Clique em qualquer ferramenta
3. Comece a usar!
```

### **Opção 2: Localmente (Python)** - 5 minutos
```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/mdl-tabloide.git
cd mdl-tabloide

# 2. Instale dependências
pip install pdf2image Pillow

# 3. Execute
python extrair_produtos_individuais.py
```

### **Opção 3: Windows (Um clique)** - 5 minutos
```
1. Coloque o PDF na pasta do repositório
2. Duplo clique em: EXTRAIR_PRODUTOS.bat
3. Pronto! Pasta "produtos_individuais/" criada
```

---

## ✅ Requisitos

### Para Ferramentas Web:
- ✅ Navegador moderno (Chrome, Firefox, Edge, Safari)
- ✅ Nada para instalar!

### Para Script Python:
- ✅ Python 3.7 ou superior
- ✅ Bibliotecas:
  ```bash
  pip install pdf2image Pillow
  ```
- ✅ Poppler instalado (Windows) - opcional
  - Se não tiver: https://github.com/oschwartz10612/poppler-windows/releases/

---

## 📊 Comparação de Ferramentas

| Ferramenta | Velocidade | Automação | Qualidade | Facilidade |
|-----------|-----------|-----------|-----------|-----------|
| **Extrator Automático** | ⚡⚡⚡ | ⚙️⚙️⚙️ | ⭐⭐⭐ | ✓✓✓ |
| **Extrator Interativo** | ⚡⚡ | ⚙️⚙️ | ⭐⭐⭐⭐ | ✓✓ |
| **Visualizador** | ⚡⚡⚡ | ⚙️ | ⭐⭐ | ✓✓✓ |

---

## 📁 Estrutura do Repositório

```
mdl-tabloide/
├── index.html                          # Página inicial (hub de acesso)
├── EXTRATOR_PRODUTOS.html              # Ferramenta interativa
├── VISUALIZADOR_TABLOIDE.html          # Visualizador de PDF
├── extrair_produtos_individuais.py     # Script Python automático
├── EXTRAIR_PRODUTOS.bat                # Batch script (Windows)
├── GITHUB_PAGES_GUIA.md                # Guia de setup
└── README.md                           # Este arquivo
```

---

## 🎯 Casos de Uso

### Para Marketing:
- 📱 Compartilhe imagens individuais em redes sociais
- 💌 Use em campanhas de email marketing
- 🎨 Crie anúncios personalizados

### Para Catálogos:
- 📄 Crie brochuras com as imagens
- 🌐 Atualize seu site com novas imagens
- 📦 Organize produtos em categorias

### Para Operações:
- 🏪 Imprima para vitrine da loja
- 📸 Qualidade consistente em todas as imagens
- 💾 Organize em biblioteca de produtos

---

## 🔧 Desenvolvimento

### Modificar Grid (automático):
Edite `extrair_produtos_individuais.py`:
```python
linhas = 4      # Número de linhas (padrão: 4)
colunas = 4     # Número de colunas (padrão: 4)
```

### Ajustar Qualidade:
```python
# Altere no script:
convert_from_path(pdf_path, dpi=150)  # Padrão: 150
# dpi=100 (menor, mais rápido)
# dpi=200 (melhor qualidade)
# dpi=300 (máxima qualidade)
```

---

## 🆘 Troubleshooting

### "Ferramentas web não funcionam"
- Abra navegador moderno (Chrome, Firefox, Edge)
- Limpe cache: Ctrl+Shift+Del
- Tente em incógnito (Ctrl+Shift+N)

### "Python não encontrado"
- Instale de: https://www.python.org/downloads/
- Marque "Add Python to PATH"
- Reinicie o CMD/PowerShell

### "Erro ao extrair produtos"
- Certifique-se que o PDF está na pasta correta
- Verifique se é um PDF válido
- Tente aumentar DPI (150 → 200)

### "Poppler não encontrado"
- Baixe: https://github.com/oschwartz10612/poppler-windows/releases/
- Extraia em: `C:\Program Files\poppler`
- Reinicie o computador

---

## 📈 Resultados Esperados

**Automático:**
- 31 imagens em 2-5 minutos
- Formato: PNG/JPEG (alta qualidade)
- Tamanho: ~500KB-2MB por imagem
- Resolução: 500x500px

**Interativo:**
- 31 imagens personalizadas
- Tempo variável (depende da sua velocidade)
- Qualidade máxima
- Nomes customizados

---

## 💾 Output Files

Após executar, você terá:

```
produtos_individuais/
├── PRODUTO_01.jpg
├── PRODUTO_02.jpg
├── PRODUTO_03.jpg
...
└── PRODUTO_31.jpg
```

Todas prontas para usar em:
- 🌐 Website
- 📱 Instagram/Facebook
- 📧 Email marketing
- 📄 Catálogos impressos
- 🎨 Materiais de marketing

---

## 🤝 Contribuições

Encontrou um bug? Tem uma sugestão?

1. Abra uma [Issue](https://github.com/seu-usuario/mdl-tabloide/issues)
2. Descreva o problema em detalhes
3. Anexe screenshots se possível

---

## 📜 Licença

Este projeto está sob licença **MIT** - veja [LICENSE](LICENSE) para detalhes.

---

## 👤 Autor

**MDL - Móveis do Lar**
- 🏪 Especializada em móveis de qualidade
- 📍 Seu bairro
- 📱 Contato: sua-loja@email.com

---

## 🙏 Agradecimentos

Desenvolvido com ❤️ usando:
- [PDF.js](https://mozilla.github.io/pdf.js/) - Visualização de PDFs
- [Python](https://www.python.org/) - Processamento de imagens
- [GitHub Pages](https://pages.github.com/) - Hospedagem

---

## 📞 Suporte

- 📖 [Guia GitHub Pages](./GITHUB_PAGES_GUIA.md)
- 🐛 [Reportar Bug](https://github.com/seu-usuario/mdl-tabloide/issues)
- 💬 [Discussões](https://github.com/seu-usuario/mdl-tabloide/discussions)

---

**Última atualização:** 2026-05-04  
**Versão:** 1.0  
**Status:** ✅ Pronto para produção
