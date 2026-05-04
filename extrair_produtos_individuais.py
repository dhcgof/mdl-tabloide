#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para extrair imagens individuais de cada produto do tabloide MDL
Divide automaticamente as páginas em uma grade e recorta cada produto
"""

import os
import sys
from pathlib import Path

try:
    from pdf2image import convert_from_path
    from PIL import Image
    import math
except ImportError:
    print("📦 Instalando dependências...")
    os.system("pip install pdf2image Pillow --break-system-packages -q")
    from pdf2image import convert_from_path
    from PIL import Image
    import math

def extrair_produtos(pdf_path, linhas=4, colunas=4, output_dir="produtos_individuais"):
    """
    Extrai imagens individuais de produtos em grid

    Args:
        pdf_path: Caminho do PDF
        linhas: Número de linhas no grid
        colunas: Número de colunas no grid
        output_dir: Diretório de saída
    """

    print("\n" + "="*60)
    print("🎯 EXTRATOR DE PRODUTOS INDIVIDUAIS - MDL")
    print("="*60)

    # Validar PDF
    if not os.path.exists(pdf_path):
        print(f"❌ PDF não encontrado: {pdf_path}")
        return False

    # Criar diretório de saída
    Path(output_dir).mkdir(exist_ok=True)

    try:
        print(f"\n📄 Processando: {os.path.basename(pdf_path)}")

        # Converter PDF para imagens
        print(f"🔄 Convertendo para imagens (DPI: 150)...")
        images = convert_from_path(pdf_path, dpi=150)
        print(f"✓ {len(images)} página(s) carregada(s)\n")

        product_number = 1

        # Processar cada página
        for page_num, image in enumerate(images, 1):
            print(f"📖 Página {page_num}/{len(images)}")

            width, height = image.size

            # Calcular dimensões de cada célula
            cell_width = width // colunas
            cell_height = height // linhas

            print(f"   Grid: {linhas}x{colunas} (célula: {cell_width}x{cell_height}px)")

            # Recortar cada célula
            for row in range(linhas):
                for col in range(colunas):
                    # Coordenadas da célula
                    left = col * cell_width
                    top = row * cell_height
                    right = left + cell_width
                    bottom = top + cell_height

                    # Recortar produto
                    crop_box = (left, top, right, bottom)
                    product_image = image.crop(crop_box)

                    # Remover bordas brancas (opcional)
                    # Esta parte reduz o tamanho se houver muito espaço branco
                    try:
                        # Encontrar bbox sem branco
                        product_image = product_image.convert('RGB')
                        bbox = product_image.getbbox()
                        if bbox:
                            # Adicionar pequena margem
                            margin = 10
                            bbox = (
                                max(0, bbox[0] - margin),
                                max(0, bbox[1] - margin),
                                min(product_image.width, bbox[2] + margin),
                                min(product_image.height, bbox[3] + margin)
                            )
                            product_image = product_image.crop(bbox)
                    except:
                        pass

                    # Redimensionar para tamanho consistente (500x500)
                    product_image = product_image.resize((500, 500), Image.Resampling.LANCZOS)

                    # Salvar produto
                    filename = f"PRODUTO_{product_number:02d}.jpg"
                    filepath = os.path.join(output_dir, filename)
                    product_image.save(filepath, 'JPEG', quality=95)

                    print(f"   ✓ Produto {product_number:2d} salvo: {filename}")

                    product_number += 1

        print(f"\n" + "="*60)
        print(f"✅ SUCESSO!")
        print(f"📁 {product_number - 1} imagens extraídas")
        print(f"📍 Localização: {os.path.abspath(output_dir)}")
        print(f"📊 Tamanho: {sum(os.path.getsize(os.path.join(output_dir, f)) for f in os.listdir(output_dir)) / (1024*1024):.2f} MB")
        print("="*60)

        return True

    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Função principal"""

    # Procurar PDF na pasta atual
    pdf_files = list(Path('.').glob('*.pdf'))

    if not pdf_files:
        print("❌ Nenhum PDF encontrado na pasta atual")
        print("💡 Coloque o arquivo MDL TABLOIDE MENSAL (32).pdf aqui e execute novamente")
        return False

    pdf_path = str(pdf_files[0])

    # Configurações padrão (ajustar conforme necessário)
    print("\n⚙️  CONFIGURAÇÃO")
    print("-" * 60)
    print("Grid padrão: 4 linhas × 4 colunas = 16 produtos por página")
    print("Altere conforme o layout real do seu tabloide")
    print("-" * 60)

    linhas = 4
    colunas = 4

    # Se forem 2 páginas com 16 produtos cada, teremos 32 (precisamos apenas de 31)
    # O último será descartado

    # Executar extração
    sucesso = extrair_produtos(
        pdf_path=pdf_path,
        linhas=linhas,
        colunas=colunas,
        output_dir="produtos_individuais"
    )

    if sucesso:
        print("\n💡 Próximos passos:")
        print("   1. Verifique as imagens na pasta 'produtos_individuais'")
        print("   2. Se o layout for diferente, edite LINHAS e COLUNAS no script")
        print("   3. Imagens podem ser usadas em anúncios, redes sociais, etc.")

    return sucesso

if __name__ == "__main__":
    sucesso = main()
    sys.exit(0 if sucesso else 1)
