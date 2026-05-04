#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Auto-Sync com GitHub API
Sincroniza arquivos automaticamente usando GitHub API
Sem necessidade do Git CLI
"""

import os
import sys
import time
import json
import base64
import logging
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

try:
    from github import Github
    from github import InputFileContent
except ImportError:
    print("📦 Instalando PyGithub...")
    os.system("pip install PyGithub watchdog -q")
    from github import Github
    from github import InputFileContent

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class GitHubAutoSync:
    """Sincronizador automático via GitHub API"""

    def __init__(self, token, repo_name, owner):
        """
        Inicializar sincronizador

        Args:
            token: GitHub Personal Access Token
            repo_name: Nome do repositório (ex: mdl-tabloide)
            owner: Dono do repositório (seu usuário)
        """
        self.token = token
        self.repo_name = repo_name
        self.owner = owner
        self.github = None
        self.repo = None
        self.last_sync = {}
        self.ignored_dirs = ['.git', '__pycache__', 'node_modules', '.venv', 'venv']
        self.ignored_extensions = ['.pyc', '.pyo', '.tmp', '.swp', '.log']

    def autenticar(self):
        """Autenticar com GitHub API"""
        try:
            logger.info("🔐 Autenticando com GitHub API...")
            self.github = Github(self.token)

            # Testar token
            user = self.github.get_user()
            logger.info(f"✓ Autenticado como: {user.login}")

            # Obter repositório
            self.repo = self.github.get_user(self.owner).get_repo(self.repo_name)
            logger.info(f"✓ Repositório: {self.owner}/{self.repo_name}")

            return True
        except Exception as e:
            logger.error(f"❌ Erro de autenticação: {e}")
            return False

    def should_ignore(self, filepath):
        """Verificar se arquivo deve ser ignorado"""
        path_str = str(filepath).replace('\\', '/')

        # Ignorar diretórios
        for ignored in self.ignored_dirs:
            if f"/{ignored}/" in path_str or path_str.startswith(ignored):
                return True

        # Ignorar extensões
        for ext in self.ignored_extensions:
            if path_str.endswith(ext):
                return True

        # Ignorar arquivos de configuração do sistema
        if path_str.endswith(('.DS_Store', 'Thumbs.db')):
            return True

        return False

    def ler_arquivo(self, filepath):
        """Ler conteúdo do arquivo"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            # Arquivo binário
            with open(filepath, 'rb') as f:
                return base64.b64encode(f.read()).decode('utf-8')

    def obter_caminho_relativo(self, filepath):
        """Obter caminho relativo do arquivo"""
        return str(Path(filepath)).replace('\\', '/')

    def fazer_sync(self, filepath, action='update'):
        """
        Sincronizar arquivo com GitHub API

        Args:
            filepath: Caminho do arquivo
            action: 'create', 'update' ou 'delete'
        """
        if self.should_ignore(filepath):
            return False

        try:
            filepath = Path(filepath)
            rel_path = self.obter_caminho_relativo(filepath)

            logger.info(f"🔄 Sincronizando: {rel_path} ({action})")

            if action == 'delete':
                # Deletar arquivo
                try:
                    file_obj = self.repo.get_contents(rel_path)
                    self.repo.delete_file(
                        path=rel_path,
                        message=f"🗑️  Auto-delete: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                        sha=file_obj.sha,
                        branch='main'
                    )
                    logger.info(f"✓ Deletado: {rel_path}")
                except Exception as e:
                    logger.warning(f"⚠️  Arquivo não encontrado no repo: {rel_path}")
                    return False

            else:
                # Criar ou atualizar arquivo
                content = self.ler_arquivo(filepath)

                try:
                    # Tentar obter arquivo existente
                    file_obj = self.repo.get_contents(rel_path)
                    sha = file_obj.sha

                    # Atualizar
                    self.repo.update_file(
                        path=rel_path,
                        message=f"📝 Auto-update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                        content=content,
                        sha=sha,
                        branch='main'
                    )
                    logger.info(f"✓ Atualizado: {rel_path}")

                except:
                    # Criar novo arquivo
                    self.repo.create_file(
                        path=rel_path,
                        message=f"✨ Auto-create: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                        content=content,
                        branch='main'
                    )
                    logger.info(f"✓ Criado: {rel_path}")

            # Registrar sincronização
            self.last_sync[rel_path] = datetime.now()
            return True

        except Exception as e:
            logger.error(f"❌ Erro ao sincronizar {filepath}: {e}")
            return False

    def sincronizar_todos(self):
        """Sincronizar todos os arquivos locais"""
        logger.info("\n" + "="*60)
        logger.info("🔄 SINCRONIZAÇÃO COMPLETA")
        logger.info("="*60)

        count = 0
        for filepath in Path('.').rglob('*'):
            if filepath.is_file() and not self.should_ignore(filepath):
                if self.fazer_sync(filepath, 'update'):
                    count += 1

        logger.info(f"\n✓ {count} arquivo(s) sincronizado(s)")
        logger.info("="*60 + "\n")

class FileChangeHandler(FileSystemEventHandler):
    """Handler para mudanças de arquivos"""

    def __init__(self, syncer):
        self.syncer = syncer
        self.pending_changes = {}
        self.sync_delay = 5

    def on_modified(self, event):
        if not event.is_directory and not self.syncer.should_ignore(event.src_path):
            logger.info(f"📝 Modificado: {Path(event.src_path).name}")
            self.schedule_sync(event.src_path, 'update')

    def on_created(self, event):
        if not event.is_directory and not self.syncer.should_ignore(event.src_path):
            logger.info(f"✨ Novo: {Path(event.src_path).name}")
            self.schedule_sync(event.src_path, 'create')

    def on_deleted(self, event):
        if not event.is_directory and not self.syncer.should_ignore(event.src_path):
            logger.info(f"🗑️  Deletado: {Path(event.src_path).name}")
            self.schedule_sync(event.src_path, 'delete')

    def schedule_sync(self, filepath, action):
        """Agendar sincronização com delay"""
        self.pending_changes[filepath] = (action, time.time())
        self.process_pending()

    def process_pending(self):
        """Processar mudanças pendentes"""
        current_time = time.time()
        to_remove = []

        for filepath, (action, scheduled_time) in self.pending_changes.items():
            if current_time - scheduled_time >= self.sync_delay:
                self.syncer.fazer_sync(filepath, action)
                to_remove.append(filepath)

        for filepath in to_remove:
            del self.pending_changes[filepath]

def carregar_config():
    """Carregar configuração do arquivo"""
    config_file = Path('.github-sync.json')

    if config_file.exists():
        with open(config_file, 'r') as f:
            return json.load(f)

    return None

def salvar_config(token, owner, repo):
    """Salvar configuração"""
    config = {
        'token': token,
        'owner': owner,
        'repo': repo
    }

    with open('.github-sync.json', 'w') as f:
        json.dump(config, f, indent=2)

    logger.info("✓ Configuração salva em .github-sync.json")

def main():
    """Função principal"""
    logger.info("\n" + "="*60)
    logger.info("🚀 AUTO-SYNC COM GITHUB API")
    logger.info("="*60)

    # Carregar ou solicitar configuração
    config = carregar_config()

    if not config:
        logger.info("\n📝 Configuração inicial necessária")
        print("\n Digite suas credenciais GitHub:")

        token = input("GitHub Personal Access Token: ").strip()
        owner = input("Seu usuário GitHub: ").strip()
        repo = input("Nome do repositório: ").strip()

        if not all([token, owner, repo]):
            logger.error("❌ Dados incompletos!")
            return False

        salvar_config(token, owner, repo)
    else:
        token = config.get('token')
        owner = config.get('owner')
        repo = config.get('repo')

    # Criar sincronizador
    syncer = GitHubAutoSync(token, repo, owner)

    # Autenticar
    if not syncer.autenticar():
        return False

    # Sincronizar todos os arquivos inicialmente
    syncer.sincronizar_todos()

    # Configurar monitor
    handler = FileChangeHandler(syncer)
    observer = Observer()
    observer.schedule(handler, path='.', recursive=True)

    logger.info("\n" + "="*60)
    logger.info("👀 Monitorando mudanças...")
    logger.info("="*60)
    logger.info("\n📌 Funcionamento:")
    logger.info("  • Detecta mudanças em tempo real")
    logger.info("  • Aguarda 5 segundos para agrupar mudanças")
    logger.info("  • Sincroniza via GitHub API")
    logger.info("  • Suporta criar, atualizar e deletar arquivos")
    logger.info("\n💡 Para parar: Pressione Ctrl+C")
    logger.info("="*60 + "\n")

    try:
        observer.start()

        # Processar mudanças periodicamente
        while True:
            handler.process_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        logger.info("\n\n⏹️  Parando sincronização...")
        observer.stop()
        logger.info("✓ Auto-sync desativado")
        observer.join()

    return True

if __name__ == "__main__":
    try:
        sucesso = main()
        sys.exit(0 if sucesso else 1)
    except Exception as e:
        logger.error(f"❌ Erro fatal: {e}")
        sys.exit(1)
