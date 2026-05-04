#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdf2image
from pdf2image import convert_from_path
import os

pdf_path = "/sessions/gallant-magical-clarke/mnt/uploads/MDL TABLOIDE MENSAL  (32).pdf"
output_dir = "/sessions/gallant-magical-clarke/mnt/outputs/imagens_pdf"

# Criar diretório se não existir
os.makedirs(output_dir, exist_ok=True)

try:
    # Converter PDF para imagens
    print("Convertendo PDF para imagens...")
    images = convert_from_path(pdf_path, dpi=150)

    # Salvar cada página como imagem
    for i, image in enumerate(images, 1):
        image_path = os.path.join(output_dir, f"pagina_{i}.jpg")
        image.save(image_path, 'JPEG')
        print(f"✓ Página {i} salva: {image_path}")

    print(f"\n✓ Total de {len(images)} imagens extraídas com sucesso!")

except Exception as e:
    print(f"Erro: {e}")
    print("Instalando dependências necessárias...")
    os.system("pip install pdf2image Pillow poppler-utils --break-system-packages")
