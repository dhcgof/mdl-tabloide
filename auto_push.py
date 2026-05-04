#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para Auto-Upload de Arquivos no GitHub
Monitora mudanças nos arquivos e faz push automático
"""

import os
import sys
import time
import subprocess
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class GitAutoUploadHandler(FileSystemEventHandler):
    """Handler para detectar mudanças de arquivos e fazer push automático"""

    def __init__(self, ignored_dirs=None):
        self.ignored_dirs = ignored_dirs or ['.git', '__pycache__', '.pytest_cache', 'node_modules']
        self.last_push_time = 0
        self.push_delay = 5  # Aguardar 5 segundos antes de fazer push

    def should_ignore(self, path):
        """Verificar se o arquivo deve ser ignorado"""
        path_str = str(path).replace('\\', '/')

        # Ignorar certos diretórios
        for ignored in self.ignored_dirs:
            if f"/{ignored}/" in path_str or path_str.startswith(ignored):
                return True

        # Ignorar arquivos temporários
        if path.endswith(('.pyc', '.pyo', '.tmp', '.swp', '.swo')):
            return True

        return False

    def on_modified(self, event):
        """Chamado quando um arquivo é modificado"""
        if event.is_directory or self.should_ignore(event.src_path):
            return

        print(f"📝 Arquivo modificado: {Path(event.src_path).name}")
        self.schedule_push()

    def on_created(self, event):
        """Chamado quando um arquivo é criado"""
        if event.is_directory or self.should_ignore(event.src_path):
            return

        print(f"✨ Arquivo novo: {Path(event.src_path).name}")
        self.schedule_push()

    def on_deleted(self, event):
        """Chamado quando um arquivo é deletado"""
        if event.is_directory or self.should_ignore(event.src_path):
            return

        print(f"🗑️  Arquivo deletado: {Path(event.src_path).name}")
        self.schedule_push()

    def schedule_push(self):
        """Agendar push (com delay para evitar múltiplos pushes)"""
        current_time = time.time()

        # Se menos de 5 segundos desde o último push, ignorar
        if current_time - self.last_push_time < self.push_delay:
            return

        self.last_push_time = current_time

        # Aguardar um pouco e fazer push
        time.sleep(self.push_delay)
        self.push_to_github()

    def push_to_github(self):
        """Fazer push automático para GitHub"""
        try:
            # Verificar se há mudanças
            result = subprocess.run(
                ['git', 'status', '--short'],
                capture_output=True,
                text=True,
                timeout=10
            )

            if not result.stdout.strip():
                # Nenhuma mudança para commitar
                return

            print("\n" + "="*60)
            print("🚀 Auto-Upload Detectado!")
            print("="*60)

            # Mostrar mudanças
            print("📝 Arquivos alterados:")
            for line in result.stdout.strip().split('\n'):
                if line:
                    status = line[:2]
                    filename = line[3:]
                    status_emoji = {
                        'M ': '📝 Modificado',
                        'A ': '✨ Novo',
                        'D ': '🗑️  Deletado',
                        '??': '❓ Não rastreado'
                    }.get(status, status)
                    print(f"  {status_emoji}: {filename}")

            # Fazer git add de todos os arquivos
            print("\n⏳ Adicionando arquivos...")
            subprocess.run(['git', 'add', '.'], timeout=10, check=True)
            print("✓ Arquivos adicionados")

            # Criar mensagem de commit automática
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            commit_msg = f"🔄 Auto-upload: {timestamp}"

            # Fazer commit
            print("💾 Fazendo commit...")
            subprocess.run(
                ['git', 'commit', '-m', commit_msg],
                timeout=10,
                check=True
            )
            print(f"✓ Commit: {commit_msg}")

            # Fazer push
            print("📤 Fazendo push para GitHub...")
            subprocess.run(['git', 'push', 'origin', 'main'], timeout=30, check=True)
            print("✓ Push concluído!")

            print("\n✅ GitHub Pages será atualizado em 1-2 minutos")
            print("="*60 + "\n")

        except subprocess.TimeoutExpired:
            print("❌ Erro: Operação demorou muito. Tente novamente.")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Erro: {e}")
            print("Dica: Verifique credenciais do GitHub ou conexão de internet")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

def check_git_configured():
    """Verificar se Git está configurado"""
    try:
        subprocess.run(
            ['git', 'config', 'user.email'],
            capture_output=True,
            timeout=5,
            check=True
        )
        return True
    except:
        return False

def main():
    """Função principal"""
    print("\n" + "="*60)
    print("🚀 AUTO-UPLOAD GITHUB - MDL Tabloide")
    print("="*60)

    # Verificar Git
    if not check_git_configured():
        print("\n⚠️  Git não configurado!")
        print("\nExecute estes comandos uma vez:")
        print("  git config --global user.name 'Seu Nome'")
        print("  git config --global user.email 'seu-email@gmail.com'")
        return False

    # Verificar se está em repositório Git
    if not Path('.git').exists():
        print("\n❌ Erro: Não estou em um repositório Git")
        print("\nExecute primeiro:")
        print("  git clone https://github.com/seu-usuario/mdl-tabloide.git")
        print("  cd mdl-tabloide")
        return False

    print("✓ Git configurado")
    print("✓ Repositório encontrado")

    # Configurar observer
    event_handler = GitAutoUploadHandler(
        ignored_dirs=['.git', '__pycache__', 'node_modules', '.venv', 'venv']
    )

    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)

    print("\n" + "="*60)
    print("👀 Monitorando mudanças de arquivos...")
    print("="*60)
    print("\n📌 O que acontece agora:")
    print("  1. Qualquer mudança em arquivos será detectada")
    print("  2. Auto-commit será criado com timestamp")
    print("  3. Auto-push para GitHub")
    print("  4. GitHub Pages atualiza em 1-2 minutos")
    print("\n💡 Dicas:")
    print("  • Deixe este script rodando enquanto trabalha")
    print("  • Pressione Ctrl+C para parar")
    print("  • Verifique sua conexão de internet")
    print("  • Use git pull antes de fazer mudanças se trabalhar em 2+ PCs")
    print("\n" + "="*60 + "\n")

    try:
        observer.start()

        # Manter script rodando
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\n⏹️  Parando monitoramento...")
        observer.stop()
        print("✓ Auto-upload desativado")
        observer.join()

    return True

if __name__ == "__main__":
    try:
        sucesso = main()
        sys.exit(0 if sucesso else 1)
    except Exception as e:
        print(f"\n❌ Erro fatal: {e}")
        sys.exit(1)
