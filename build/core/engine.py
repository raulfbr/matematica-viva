import os
import yaml
import time
import re
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from .logger import ForgeLogger
from .assets import AssetManager

class GutenbergEngine:
    """
    Motor de Renderização Base (Core).
    Princípios: Robustez (Impecável), Atomicidade, Feedback Claro.
    """
    def __init__(self, config, dry_run=False):
        self.config = config
        self.dry_run = dry_run
        self.asset_manager = AssetManager(config.ASSETS_DIR)
        self.assets_index = {}
        self.lessons_index = []
        self.warnings = []
        self.errors = []
        self.env = None 
        
        ForgeLogger.log(f"Iniciando Engine (Mode: {'DRY RUN' if dry_run else 'LIVE BUILD'})", status="🔥")

    def ensure_directories(self):
        """Phase 1: Pre-Flight Check."""
        ForgeLogger.log("Verificando integridade de diretórios...")
        
        # Check Inputs
        required = [self.config.INPUT_DIR, self.config.TEMPLATES_DIR, self.config.ASSETS_DIR]
        for d in required:
            if not d.exists():
                self.errors.append(f"CRITICAL: Diretório obrigatório não encontrado: {d}")
                ForgeLogger.error(f"Diretório ausente: {d}")
                return False
        
        # Check/Create Output
        if not self.config.OUTPUT_DIR.exists():
            if self.dry_run:
                ForgeLogger.log(f"Dry Run: Criaria diretório {self.config.OUTPUT_DIR}")
            else:
                try:
                    os.makedirs(self.config.OUTPUT_DIR, exist_ok=True)
                    ForgeLogger.log(f"Criada pasta de saída: {self.config.OUTPUT_DIR.name}", status="📂")
                except Exception as e:
                    self.errors.append(f"CRITICAL: Falha ao criar output dir: {e}")
                    return False
        
        ForgeLogger.success("Diretórios verificados.")
        return True

    def setup_jinja(self):
        """Phase 2: Jinja2 Setup & Filters."""
        ForgeLogger.log("Inicializando Motor Jinja2...")
        try:
            self.env = Environment(loader=FileSystemLoader(self.config.TEMPLATES_DIR))
            
            # Carregar Dicionário de Toms (SSOT)
            try:
                toms_path = self.config.PROJECT_ROOT / "LORE" / "toms_de_voz.yaml"
                if toms_path.exists():
                    with open(toms_path, 'r', encoding='utf-8') as f:
                        toms_data = yaml.safe_load(f)
                    self.env.globals['toms'] = toms_data
                    ForgeLogger.log(f"🎭 Dicionário de Toms carregado: {len(toms_data.get('tons', {}))} tons.", status="🎭")
                else:
                    ForgeLogger.log("⚠️ LORE/toms_de_voz.yaml não encontrado.", status="⚠️")
                    self.env.globals['toms'] = {}
            except Exception as e:
                ForgeLogger.log(f"❌ Erro ao carregar Toms: {e}", status="❌")
                self.env.globals['toms'] = {}

            # Filtro: Smart Typography (Impecabilidade)
            def smart_typography(text):
                if not isinstance(text, str): return text
                text = text.replace('"', '”').replace("'", "’") 
                text = re.sub(r' - ', ' — ', text)
                return text

            self.env.filters['typogrify'] = smart_typography
            ForgeLogger.success("Engine Jinja2 Pronta.")
        except Exception as e:
            self.errors.append(f"CRITICAL: Falha ao iniciar Jinja2: {e}")
            return False

    def scan_yamls(self):
        """Phase 1: YAML Integrity Scan."""
        ForgeLogger.log("Escaneando Lições YAML...")
        
        yaml_files = list(self.config.INPUT_DIR.glob("*.yaml"))
        
        if not yaml_files:
            self.warnings.append("Nenhum arquivo YAML encontrado.")
            return

        ForgeLogger.log(f"Iniciando Scan de {len(yaml_files)} arquivos...")

        processed_count = 0
        for fpath in yaml_files:
            if fpath.name.startswith("_") or "TEMPLATE" in fpath.name.upper():
                ForgeLogger.log(f"Ignorando {fpath.name} (Meta-arquivo)", status="⏭️ ")
                continue
                
            loop_start = time.time()
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                
                # Validation Hook
                if not self.validate_lesson(fpath, data):
                    continue
                
                meta = data['licao'].get('metadados', {})
                self.lessons_index.append({
                    'file': fpath.name,
                    'id': meta.get('id'),
                    'titulo': meta.get('titulo'),
                    'data': data
                })
                
                elapsed = time.time() - loop_start
                ForgeLogger.success(f"{meta.get('id')} ({meta.get('titulo')}) OK ({elapsed:.2f}s).")
                processed_count += 1
                
            except Exception as e:
                self.errors.append(f"{fpath.name}: Erro leitura - {str(e)}")
                ForgeLogger.error(f"Falha ao ler {fpath.name}: {e}")

        ForgeLogger.success(f"Scan concluído. {processed_count} lições válidas.")

    def validate_lesson(self, fpath, data):
        """Hook para validação específica por fase."""
        if not data or 'licao' not in data:
            self.warnings.append(f"{fpath.name}: Schema inválido")
            return False
            
        meta = data['licao'].get('metadados', {})
        if not meta.get('id'):
            self.warnings.append(f"{fpath.name}: Metadados sem ID")
            return False
            
        return True

    def render_all(self):
        """Phase 2: Render Loop."""
        if self.dry_run:
            ForgeLogger.log("Modo Dry Run: Pulando gravação.", status="🛑")
            return

        ForgeLogger.log(f"Iniciando Renderização de {len(self.lessons_index)} lições...")
        
        try:
           template = self.env.get_template(self.config.TEMPLATE_NAME)
        except Exception as e:
           self.errors.append(f"Template {self.config.TEMPLATE_NAME} não encontrado: {e}")
           return

        for lesson in self.lessons_index:
            lid = lesson['id']
            try:
                html_content = template.render(licao=lesson['data']['licao'])
                
                clean_title = str(lesson['titulo']).replace(' ', '_').upper()
                clean_title = "".join([c for c in clean_title if c.isalnum() or c in ('_', '-')])
                filename = f"{lid}_{clean_title}.html"
                
                output_path = self.config.OUTPUT_DIR / filename
                
                # Atomic Write
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
        
        if not self.ensure_directories(): return
        self.setup_jinja()
        if self.errors: return

        self.assets_index = self.asset_manager.index_assets()
        self.scan_yamls()
        
        if not self.dry_run:
            self.render_all()

        elapsed = time.time() - start_time
        ForgeLogger.log(f"Fim de Ciclo em {elapsed:.2f}s", status="🏁")
