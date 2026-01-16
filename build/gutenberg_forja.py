import os
import glob
import yaml
import argparse
import time
import sys
import datetime
import re
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# CONFIGURAÇÃO DE AMBIENTE
class Config:
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    INPUT_DIR = PROJECT_ROOT / "curriculo/01_SEMENTESV6"
    # OUTPUT_DIR ajustado para PRODUÇÃO
    OUTPUT_DIR = PROJECT_ROOT / "site/sementes" 
    TEMPLATES_DIR = PROJECT_ROOT / "site/templates"
    ASSETS_DIR = PROJECT_ROOT / "site/assets"
    REQUIRED_DIRS = [INPUT_DIR, TEMPLATES_DIR, ASSETS_DIR]

class ForgeLogger:
    """Central de Logs com Timestamps (Engenharia: Feedback Rápido)."""
    @staticmethod
    def log(msg, item=None, status="ℹ️"):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        item_str = f" [{item}]" if item else ""
        print(f"[{timestamp}] {status}  {msg}{item_str}", flush=True)

    @staticmethod
    def success(msg): ForgeLogger.log(msg, status="✅ ")
    
    @staticmethod
    def warn(msg): ForgeLogger.log(msg, status="⚠️ ")
    
    @staticmethod
    def error(msg): ForgeLogger.log(msg, status="💥")

class GutenbergForge:
    """
    Motor de Renderização da Forja Gutenberg.
    Princípios: Robustez (Impecável), Atomicidade, Feedback Claro.
    """
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.assets_index = {}
        self.lessons_index = []
        self.warnings = []
        self.errors = []
        self.env = None # Jinja Environment
        
        print("-" * 60)
        ForgeLogger.log(f"Iniciando Forja Gutenberg V2.3 (Mode: {'DRY RUN' if dry_run else 'LIVE BUILD'})", status="🔥")
        print("-" * 60)

    def ensure_directories(self):
        """Phase 1: Pre-Flight Check."""
        ForgeLogger.log("Verificando integridade de diretórios...")
        
        # Check Inputs
        for d in Config.REQUIRED_DIRS:
            if not d.exists():
                self.errors.append(f"CRITICAL: Diretório obrigatório não encontrado: {d}")
                ForgeLogger.error(f"Diretório ausente: {d}")
                return False
        
        # Check/Create Output
        # Em modo Real ou Teste, queremos que a pasta exista
        if not Config.OUTPUT_DIR.exists():
            if self.dry_run:
                ForgeLogger.log(f"Dry Run: Criaria diretório {Config.OUTPUT_DIR}")
            else:
                try:
                    os.makedirs(Config.OUTPUT_DIR, exist_ok=True)
                    ForgeLogger.log(f"Criada pasta de saída: {Config.OUTPUT_DIR.name}", status="📂")
                except Exception as e:
                    self.errors.append(f"CRITICAL: Falha ao criar output dir: {e}")
                    return False
        
        ForgeLogger.success("Diretórios verificados.")
        return True

    def setup_jinja(self):
        """Phase 2: Jinja2 Setup & Filters."""
        ForgeLogger.log("Inicializando Motor Jinja2...")
        try:
            self.env = Environment(loader=FileSystemLoader(Config.TEMPLATES_DIR))
            
            # Filtro: Smart Typography (Impecabilidade)
            def smart_typography(text):
                if not isinstance(text, str): return text
                # Aspas curvas
                text = text.replace('"', '”').replace("'", "’") 
                # Travessão de diálogo ( - )
                text = re.sub(r' - ', ' — ', text)
                return text

            self.env.filters['typogrify'] = smart_typography
            ForgeLogger.success("Engine Jinja2 Pronta.")
        except Exception as e:
            self.errors.append(f"CRITICAL: Falha ao iniciar Jinja2: {e}")
            return False

    def index_assets(self):
        """Phase 1: Asset Inventory (Single-Pass V2.2)."""
        ForgeLogger.log("Indexando Assets Visuais (Single-Pass)...")
        start = time.time()
        
        valid_extensions = {'.png', '.jpg', '.jpeg', '.svg', '.webp'}
        found_count = 0
        
        if not Config.ASSETS_DIR.exists():
             self.errors.append(f"CRITICAL: Assets dir not found: {Config.ASSETS_DIR}")
             return

        # V2.2: Single-Pass Scan (Otimizado para OneDrive)
        for asset_path in Config.ASSETS_DIR.rglob('*'):
            if asset_path.is_file() and asset_path.suffix.lower() in valid_extensions:
                try:
                    rel_path = asset_path.relative_to(Config.ASSETS_DIR)
                    key = str(rel_path).replace('\\', '/')
                    self.assets_index[key] = asset_path
                    found_count += 1
                except ValueError:
                    continue
        
        elapsed = time.time() - start
        ForgeLogger.success(f"Indexados {found_count} assets ({elapsed:.3f}s).")

    def scan_yamls(self):
        """Phase 1: YAML Integrity Scan."""
        ForgeLogger.log("Escaneando Lições YAML...")
        
        if not Config.INPUT_DIR.exists():
             self.errors.append(f"CRITICAL: Input dir not found: {Config.INPUT_DIR}")
             return

        yaml_files = list(Config.INPUT_DIR.glob("*.yaml"))
        
        if not yaml_files:
            self.warnings.append("Nenhum arquivo YAML encontrado.")
            return

        ForgeLogger.log(f"Iniciando Scan de {len(yaml_files)} arquivos...")

        processed_count = 0
        for fpath in yaml_files:
            # FILTRO DE TEMPLATES
            if fpath.name.startswith("_") or "TEMPLATE" in fpath.name.upper():
                ForgeLogger.log(f"Ignorando {fpath.name} (Meta-arquivo)", status="⏭️ ")
                continue
                
            loop_start = time.time()
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                
                # Validation
                if not data or 'licao' not in data:
                    self.warnings.append(f"{fpath.name}: Schema inválido")
                    continue
                
                meta = data['licao'].get('metadados', {})
                lid = meta.get('id')
                titulo = meta.get('titulo')
                
                if not lid:
                    self.warnings.append(f"{fpath.name}: Metadados sem ID")
                    continue
                    
                self.lessons_index.append({
                    'file': fpath.name,
                    'id': lid,
                    'titulo': titulo,
                    'data': data
                })
                
                # Telemetria Heartbeat
                elapsed = time.time() - loop_start
                ForgeLogger.success(f"{lid} ({titulo}) OK ({elapsed:.2f}s).")
                processed_count += 1
                
                if elapsed > 2.0:
                    ForgeLogger.warn(f"⚠️ SLOW WARNING: {lid} demorou {elapsed:.2f}s")

            except Exception as e:
                self.errors.append(f"{fpath.name}: Erro leitura - {str(e)}")
                ForgeLogger.error(f"Falha ao ler {fpath.name}: {e}")

        ForgeLogger.success(f"Scan concluído. {processed_count} lições válidas.")

    def render_all(self):
        """Phase 2: Render Loop."""
        if self.dry_run:
            ForgeLogger.log("Modo Dry Run: Pulando etapa de renderização (Arquivos não gravados).", status="🛑")
            return

        ForgeLogger.log(f"Iniciando Renderização de {len(self.lessons_index)} lições...")
        
        template_name = "licao.j2"
        try:
           template = self.env.get_template(template_name)
        except Exception as e:
           self.errors.append(f"Template {template_name} não encontrado: {e}")
           return

        for lesson in self.lessons_index:
            lid = lesson['id']
            try:
                # 1. Render String
                html_content = template.render(licao=lesson['data']['licao'])
                
                # 2. Determine Filename (Clean URL)
                clean_title = str(lesson['titulo']).replace(' ', '_').upper()
                clean_title = "".join([c for c in clean_title if c.isalnum() or c in ('_', '-')])
                filename = f"{lid}_{clean_title}.html"
                
                output_path = Config.OUTPUT_DIR / filename
                
                # 3. Atomic Write
                tmp_path = output_path.with_suffix('.tmp')
                with open(tmp_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                
                if os.path.exists(output_path):
                    os.remove(output_path)
                os.rename(tmp_path, output_path)
                
                ForgeLogger.log(f"Renderizada: {filename}", status="🔨")
                
            except Exception as e:
                self.errors.append(f"Erro ao renderizar {lid}: {e}")
                ForgeLogger.error(f"Falha em {lid}: {e}")

    def run(self):
        """Main Pipeline Execution."""
        start_time = time.time()
        
        # 1. Setup
        if not self.ensure_directories():
            self._print_report(start_time, success=False)
            return
            
        self.setup_jinja()
        if self.errors: # Abort if jinja failed
             self._print_report(start_time, success=False)
             return

        # 2. Inventory
        self.index_assets()
        self.scan_yamls()
        
        # 3. Validation Reports (Dry Run logic)
        if self.dry_run:
            self._validate_integrity_dry_run()
        else:
            # Phase 2: Live Render
            self.render_all()

        self._print_report(start_time, success=True)

    def _validate_integrity_dry_run(self):
        """Dry Run Logic."""
        ForgeLogger.log("Executando validação lógica (Dry Run)...")
        # Simula render check
        if not self.env: return
        try:
            self.env.get_template("licao.j2")
            ForgeLogger.success("Template licao.j2 validado.")
        except Exception as e:
             ForgeLogger.error(f"Template licao.j2 inválido: {e}")
                
    def _print_report(self, start_time, success):
        print("-" * 60)
        
        if self.errors:
            ForgeLogger.log("ERROS CRÍTICOS ENCONTRADOS:", status="💥")
            for e in self.errors:
                print(f"   - {e}")
            print("-" * 60)
            sys.exit(1)

        if self.warnings:
            ForgeLogger.log("AVISOS GERADOS:", status="⚠️ ")
            for w in self.warnings:
                print(f"   - {w}")
            print("-" * 60)
            
        elapsed = time.time() - start_time
        ForgeLogger.log(f"Forja Finalizada em {elapsed:.2f}s", status="🏁")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Forja Gutenberg: YAML to HTML Pipeline")
    parser.add_argument("--dry-run", action="store_true", help="Executa verificação sem gravacao em disco")
    args = parser.parse_args()
    
    forge = GutenbergForge(dry_run=args.dry_run)
    forge.run()
