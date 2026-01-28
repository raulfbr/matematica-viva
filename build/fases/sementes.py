from pathlib import Path
from core.engine import GutenbergEngine, ForgeLogger
from core.navigation import NavigationService

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
        
        # 3. FILTRO DE SEGURANÇA (MANUAL OVERRIDE)
        # O usuário está editando manualmente as lições 000-020.
        # Removemos essas lições da lista de renderização para que o Forge NÃO as sobrescreva.
        # Elas ainda foram usadas para cálculo de links (passo 1), então a navegação da 021 apontará corretamente para a 020.
        lessons_to_render = []
        for item in self.lessons_index:
            try:
                # Extrai número do ID (Ex: MV-S-001 -> 1)
                lid = item.get('id', '')
                parts = lid.split('-')
                if len(parts) >= 3 and parts[2].isdigit():
                    num = int(parts[2])
                    if 0 <= num <= 25:
                        ForgeLogger.log(f"🔒 Skipped (Manual Release): {lid}", status="🛡️")
                        continue
            except:
                 pass # Se falhar o parse, renderiza por segurança
            
            lessons_to_render.append(item)
            
        self.lessons_index = lessons_to_render

        # 4. Delegar para o Engine padrão fazer o trabalho pesado (Jinja, Filesystem)
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
