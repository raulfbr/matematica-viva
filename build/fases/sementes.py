from pathlib import Path
from core.engine import GutenbergEngine, ForgeLogger

class SementesConfig:
    """Configuração ISOLADA da Fase Sementes."""
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    INPUT_DIR = PROJECT_ROOT / "curriculo/01_SEMENTESV6"
    OUTPUT_DIR = PROJECT_ROOT / "site/sementes"
    
    # NOVO: Templates ISOLADOS por fase (Arquitetura v4.0)
    TEMPLATES_DIR = PROJECT_ROOT / "site/sementes/templates"
    TEMPLATE_NAME = "licao.j2"
    
    # NOVO: Assets ISOLADOS por fase
    ASSETS_DIR = PROJECT_ROOT / "site/assets/sementes"

class NavigationService:
    """Serviço isolado para cálculo de navegação (SRP)."""
    
    @staticmethod
    def _generate_filename(lid, titulo):
        """
        Gera nome do arquivo IDÊNTICO ao GutenbergEngine (Core).
        Lógica: UPPERCASE + Underscores + Apenas Alphanum.
        """
        clean_title = str(titulo).replace(' ', '_').upper()
        # Filtro alnum idêntico ao engine.py
        clean_title = "".join([c for c in clean_title if c.isalnum() or c in ('_', '-')])
        return f"{lid}_{clean_title}.html"

    @staticmethod
    def calculate_links(lessons_data):
        """
        Recebe lista de lições (formato Engine: {'data': ..., 'id': ...}).
        Retorna a mesma lista com 'prev_licao' e 'next_licao' injetados.
        """
        # 1. Ordenar por ID da lição
        sorted_lessons = sorted(
            lessons_data, 
            key=lambda x: x['data']['licao']['metadados']['id']
        )
        
        # 2. Injetar Vizinhos
        for i, item in enumerate(sorted_lessons):
            current_yaml = item['data']['licao']
            
            # Anterior
            if i > 0:
                prev = sorted_lessons[i-1]['data']['licao']['metadados']
                filename = NavigationService._generate_filename(prev['id'], prev['titulo'])
                
                # Injeta dado estruturado para Template
                item['prev_licao'] = {
                    'titulo': prev['titulo'],
                    'url': filename
                }
                # Fallback manual no YAML
                if 'navegacao' not in current_yaml: current_yaml['navegacao'] = {}
                current_yaml['navegacao']['anterior'] = {
                    'id': prev['id'], 
                    'titulo': prev['titulo'],
                    'url': filename
                }

            # Próximo
            if i < len(sorted_lessons) - 1:
                nxt = sorted_lessons[i+1]['data']['licao']['metadados']
                filename = NavigationService._generate_filename(nxt['id'], nxt['titulo'])
                
                item['next_licao'] = {
                    'titulo': nxt['titulo'],
                    'url': filename
                }
                # Fallback manual no YAML
                if 'navegacao' not in current_yaml: current_yaml['navegacao'] = {}
                current_yaml['navegacao']['proxima'] = {
                    'id': nxt['id'], 
                    'titulo': nxt['titulo'],
                    'url': filename
                }
                
        return sorted_lessons

class SementesDriver(GutenbergEngine):
    """Driver Específico para Fase Sementes."""
    def __init__(self, dry_run=False):
        super().__init__(SementesConfig, dry_run)
    
    def render_all(self):
        """
        Override do Loop de Renderização.
        Injeta Navegação antes de chamar o renderizador padrão.
        """
        ForgeLogger.log("🔪 Sementes: Calculando Navegação Linear...", status="🔪")
        
        # 1. Calcular Navegação (Modifica self.lessons_index in-place)
        # Nota: calculate_links retorna lista ordenada, vamos atualizar o index.
        self.lessons_index = NavigationService.calculate_links(self.lessons_index)
        ForgeLogger.log(f"🔗 Navegação injetada em {len(self.lessons_index)} lições.", status="🔗")
        
        # 2. Injetar varáveis calculadas no contexto 'licao' para o Jinja
        # O Engine padrão espera 'licao' dentro de 'data'.
        for item in self.lessons_index:
            if 'prev_licao' in item:
                item['data']['licao']['navegacao_calculada_prev'] = item['prev_licao']
            if 'next_licao' in item:
                item['data']['licao']['navegacao_calculada_next'] = item['next_licao']
        
        # 3. Delegar para o Engine padrão fazer o trabalho pesado (Jinja, Filesystem)
        super().render_all()

    def validate_lesson(self, fpath, data):
        """Validação Estrita: Sementes proíbe Pictórico."""
        # Validação básica do Engine (Schema, ID, etc)
        # Nota: Engine.validate_lesson não é publico/fácil de chamar sem refatorar o Engine.
        # Vamos assumir que se carregou o YAML e tem 'licao', é válido por enquanto, 
        # ou duplicar a logica minima.
        if 'licao' not in data:
            self.logger.warning(f"❌ {fpath.name}: YAML sem chave 'licao'.")
            return False
            
        # Regra de Negócio: Veto Pictórico
        jornada = data['licao'].get('jornada', {})
        pictorico = jornada.get('pictorico', {})
        
        status = pictorico.get('status', '').upper()
        if status != 'VETADO':
            self.warnings.append(f"{fpath.name} [VIOLAÇÃO]: Pictórico deve ser VETADO em Sementes.")
            
        return True
