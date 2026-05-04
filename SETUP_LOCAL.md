# 🚀 Guia de Setup Local - Anúncios com Imagens

Como o ambiente online tem limitações, você pode executar o script localmente na sua máquina Windows para gerar os anúncios com imagens embutidas automaticamente.

## 📋 Pré-requisitos

1. **Python 3.7+** instalado (baixar em https://www.python.org/downloads/)
   - ✅ Marcar "Add Python to PATH" durante a instalação
2. **Poppler** instalado (necessário para converter PDF em imagens)

## 🔧 Instalação Passo a Passo

### Passo 1: Instalar Python (se não tiver)
```
https://www.python.org/downloads/
Baixar Python 3.10 ou superior
```

### Passo 2: Instalar Poppler no Windows
```
1. Baixar: https://github.com/oschwartz10612/poppler-windows/releases/
2. Download: Release-xxxx_xx_xx.zip (versão mais recente)
3. Extrair em: C:\Program Files\poppler
4. Copiar o caminho: C:\Program Files\poppler\Library\bin
```

### Passo 3: Adicionar Poppler ao PATH (Windows)
```
1. Tecla Windows + R
2. Digite: sysdm.cpl
3. Aba "Variáveis de Ambiente"
4. Clique "Variáveis de Ambiente"
5. Adicionar novo PATH:
   C:\Program Files\poppler\Library\bin
6. OK em tudo
7. Reiniciar computador
```

### Passo 4: Instalar Bibliotecas Python
```
Abrir PowerShell ou CMD e executar:

pip install pdf2image
pip install pillow
pip install python-docx
pip install pdfplumber
```

## 📂 Organização de Arquivos

```
Sua Pasta de Trabalho/
├── MDL TABLOIDE MENSAL (32).pdf
├── gerar_anuncios.py
└── (resultado será criado aqui)
```

## ▶️ Executar o Script

```
1. Copie o arquivo PDF para a mesma pasta do script
2. Abra PowerShell/CMD nessa pasta
3. Execute:
   python gerar_anuncios.py
4. Aguarde alguns minutos (dependendo do tamanho do PDF)
5. Arquivo criado: Anuncios_com_Imagens.docx
```

## 💡 Dicas Importantes

- **Primeira execução**: Pode levar 2-5 minutos
- **Qualidade de imagens**: Aumentar DPI em `convert_from_path(pdf_path, dpi=150)` (máx: 300)
- **Memória**: Feche outros programas se tiver PC lento
- **Problemas**: Verifique se Python está no PATH digitando `python --version` no CMD

## 📧 Precisa de Ajuda?

Se encontrar erros:
1. Copie a mensagem de erro completa
2. Verifique se Poppler está em: C:\Program Files\poppler\Library\bin
3. Execute novamente após reiniciar o computador

---

**Próximos passos após gerar o arquivo:**
- Abra o .docx no Word
- Edite conforme necessário
- Exporte para PDF se desejar compartilhar
- Use em impressoras ou e-mail marketing
