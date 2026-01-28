"""
🔨 DASHBOARD BUILDER V3 (Orchestrator Aligned)
==============================================
Gera um index.html com estética MatViva Premium.
Alinhamento: North Star (Qualidade Impecável) + Orchestrator (Distinção Papéis).
"""

import os
import yaml
from pathlib import Path
from datetime import datetime
import shutil

# CONFIGURAÇÃO
INPUT_DIR_SEMENTES = Path("curriculo/01_SEMENTESV6")
INPUT_DIR_RAIZES = Path("curriculo/02_RAIZES/01_RAIZES_I")
OUTPUT_DIR = Path("site")
OUTPUT_HTML = OUTPUT_DIR / "index.html"

# ASSETS MAP (Centralizado)
ASSETS = {
    'css': OUTPUT_DIR / "style.css",
    'cards': OUTPUT_DIR / "assets/cards",
    'js': "" # Inline
}

# CORES & ESTILO (Palette North Star - Potter/Morris/TocaBoca)
STYLE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;700&family=Lora:ital,wght@0,400;0,600;1,400&family=Gloria+Hallelujah&display=swap');

:root {
    --primary: #B8860B; /* Ouro Antigo */
    --secondary: #1F2937; /* Cinza Escuro */
    --bg-page: #FDF8F3; /* Papel Antigo */
    --bg-card: #FFFFFF;
    --font-heading: 'Lora', serif;
    --font-body: 'Outfit', sans-serif;
}

/* Reset & Base */
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: var(--bg-page); color: var(--secondary); font-family: var(--font-body); line-height: 1.6; }
a { text-decoration: none; color: inherit; transition: all 0.2s; }

/* Layout Grid */
.main-wrapper { display: flex; min-height: 100vh; }
.sidebar {
    width: 280px; background: white; border-right: 1px solid #E5E7EB;
    padding: 2rem; position: fixed; height: 100vh; overflow-y: auto; z-index: 50;
}
.main-content { margin-left: 280px; padding: 3rem 4rem; width: 100%; max-width: 1400px; }

/* Sidebar */
.brand { font-family: var(--font-heading); font-size: 1.5rem; font-weight: 600; color: var(--primary); margin-bottom: 3rem; display: flex; align-items: center; gap: 0.5rem; }
.nav-section { text-transform: uppercase; letter-spacing: 0.05em; color: #9CA3AF; font-size: 0.75rem; font-weight: 700; margin: 2rem 0 0.5rem; }
.nav-link { display: flex; align-items: center; gap: 0.75rem; padding: 0.75rem; border-radius: 8px; font-weight: 500; color: #4B5563; }
.nav-link:hover { background: #FEF3C7; color: #92400E; }
.nav-link.active { background: #FFFBEB; color: #B45309; border-left: 3px solid #F59E0B; }
.nav-link small { margin-left: auto; font-size: 0.7rem; color: #D1D5DB; }

/* Header */
header { margin-bottom: 4rem; }
.role-badge { background: #E0E7FF; color: #3730A3; font-size: 0.75rem; padding: 0.25rem 0.5rem; border-radius: 4px; display: inline-block; margin-bottom: 0.5rem; font-weight: 600; }
h1 { font-family: var(--font-heading); font-size: 3rem; font-weight: 400; color: #111827; letter-spacing: -0.02em; }
.subtitle { color: #6B7280; font-size: 1.1rem; margin-top: 0.5rem; }

/* Stats Row */
.stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; margin-bottom: 4rem; }
.stat-card { background: white; padding: 1.5rem; border-radius: 12px; border: 1px solid #E5E7EB; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
.stat-val { font-size: 2rem; font-weight: 700; color: #111827; font-family: var(--font-heading); }
.stat-label { font-size: 0.85rem; color: #6B7280; font-weight: 500; }

/* Sections */
.section-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 2rem; border-bottom: 1px solid #E5E7EB; padding-bottom: 1rem; }
.section-title { font-family: var(--font-heading); font-size: 1.75rem; color: #111827; display: flex; align-items: center; gap: 0.5rem; }
.section-meta { font-size: 0.9rem; color: #9CA3AF; }

/* Grid Cards */
.grid-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; }
.card {
    background: white; border-radius: 16px; overflow: hidden;
    border: 1px solid #F3F4F6; transition: all 0.3s ease; position: relative;
    display: flex; flex-direction: column; height: 100%;
}
.card:hover { transform: translateY(-4px); box-shadow: 0 12px 24px -10px rgba(0,0,0,0.1); border-color: #FCD34D; }

/* Card Variants (Guardians) */
.card.celeste { border-top: 4px solid #F97316; } /* Raposa Laranja */
.card.bernardo { border-top: 4px solid #8B5CF6; } /* Urso Roxo/Forte */
.card.noe { border-top: 4px solid #10B981; }      /* Coruja Verde/Sabedoria */
.card.iris { border-top: 4px solid #EC4899; }     /* Pássaro Rosa/Beleza */
.card.melquior { border-top: 4px solid #F59E0B; } /* Leão Dourado/Rei */
.card.raizes { border-top: 4px solid #4B5563; border-style: dashed; } /* Raízes (Diferente) */

.card-body { padding: 1.5rem; flex-grow: 1; display: flex; flex-direction: column; }
.card-meta { display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem; }
.card-id { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.05em; color: #9CA3AF; text-transform: uppercase; background: #F3F4F6; padding: 2px 6px; border-radius: 4px; }
.card-title { font-family: var(--font-heading); font-size: 1.25rem; margin-bottom: 0.5rem; color: #1F2937; line-height: 1.3; }
.card-desc { font-size: 0.95rem; color: #6B7280; font-style: italic; margin-bottom: 1rem; }
.guardian-icon-img { width: 40px; height: 40px; border-radius: 50%; border: 2px solid #FEF3C7; padding: 2px; background: white; }

.card-footer { padding: 1rem 1.5rem; border-top: 1px solid #F3F4F6; background: #FAFAFA; display: flex; justify-content: flex-end; }
.btn-arr { font-size: 0.85rem; font-weight: 600; color: #4B5563; display: flex; align-items: center; gap: 0.25rem; }
.btn-arr span { transition: transform 0.2s; }
.btn-arr:hover span { transform: translateX(3px); }
.btn-arr:hover { color: #B45309; }

/* Empty States */
.blog-empty { text-align: center; padding: 4rem; background: #F9FAFB; border-radius: 12px; border: 2px dashed #E5E7EB; opacity: 0.7; }
.blog-empty h3 { color: #374151; margin-bottom: 0.5rem; font-weight: 600; }
.blog-empty p { color: #6B7280; font-size: 0.9rem; max-width: 400px; margin: 0 auto; }

/* MOBILE NAVIGATION REFINED (Drawer Style) */
.mobile-toggle { display: none; }
.overlay { 
    position: fixed; top: 0; left: 0; right: 0; bottom: 0; 
    background: rgba(0,0,0,0.4); backdrop-filter: blur(2px); 
    z-index: 40; opacity: 0; pointer-events: none; transition: opacity 0.3s;
}
.overlay.active { opacity: 1; pointer-events: all; }

@media (max-width: 1024px) {
    .sidebar { 
        display: block; /* Restored */
        transform: translateX(-100%); 
        transition: transform 0.3s cubic-bezier(0.4, 0.0, 0.2, 1);
        width: 80%; max-width: 300px;
    }
    .sidebar.active { transform: translateX(0); box-shadow: 5px 0 30px rgba(0,0,0,0.15); }

    .main-content { margin-left: 0; padding: 2rem; padding-top: 6rem; }
    
    .mobile-toggle { 
        display: flex; position: fixed; top: 1.5rem; left: 1.5rem; 
        width: 3.5rem; height: 3.5rem; border-radius: 50%; 
        background: white; align-items: center; justify-content: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08); z-index: 60;
        font-size: 1.5rem; border: none; color: var(--primary);
        cursor: pointer; transition: transform 0.2s;
    }
    .mobile-toggle:active { transform: scale(0.95); }
}

/* LESSON PAGE SPECIFIC (Premium Visuals) */
.lesson-container { max-width: 800px; margin: 0 auto; background: white; padding: 4rem; box-shadow: 0 4px 25px rgba(0,0,0,0.03); border-radius: 16px; position: relative; }
.home-btn { position: fixed; top: 2rem; left: 2rem; font-size: 1.5rem; text-decoration: none; opacity: 0.6; transition: opacity 0.2s; z-index: 10; filter: grayscale(1); }
.home-btn:hover { opacity: 1; filter: grayscale(0); transform: scale(1.1); }
.lesson-hero { text-align: center; margin-bottom: 4rem; position: relative; }
.lesson-meta-tag { font-size: 0.8rem; letter-spacing: 0.1em; color: #9CA3AF; text-transform: uppercase; margin-bottom: 1rem; font-weight: 700; }
.hero-title { font-family: var(--font-heading); font-size: 3.5rem; color: #1F2937; line-height: 1.1; margin-bottom: 1rem; }
.hero-quote { font-family: var(--font-heading); font-style: italic; color: #6B7280; font-size: 1.2rem; margin-bottom: 2rem; }
.hero-guardian { width: 120px; height: 120px; border-radius: 50%; border: 4px solid #FEF3C7; padding: 4px; background: white; margin-top: 1rem; box-shadow: 0 10px 30px -5px rgba(0,0,0,0.1); }
/* Typography for Lesson Body */
.lesson-body p { margin-bottom: 1.5rem; font-size: 1.1rem; color: #4B5563; }
.lesson-body h2 { font-family: var(--font-heading); font-size: 1.8rem; color: #B45309; margin-top: 3rem; margin-bottom: 1.5rem; border-bottom: 1px solid #FFE4E6; padding-bottom: 0.5rem; }
.lesson-body h3 { font-size: 1.4rem; color: #1F2937; margin-top: 2rem; margin-bottom: 1rem; }
.lesson-body ul { list-style: none; margin-bottom: 2rem; padding-left: 0; }
.lesson-body li { padding: 0.75rem 0; border-bottom: 1px dashed #E5E7EB; color: #4B5563; display: flex; gap: 0.75rem; }
.lesson-body li::before { content: "•"; color: #F59E0B; font-weight: bold; }
/* Rich Objects */
.script-persona-block { background: #FDF2F8; border-left: 4px solid #EC4899; padding: 1.5rem; margin: 2rem 0; border-radius: 0 12px 12px 0; display: flex; gap: 1rem; align-items: flex-start; }
.script-avatar { width: 48px; height: 48px; border-radius: 50%; border: 2px solid white; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
.script-content { flex: 1; }
.script-name { font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #BE185D; margin-bottom: 0.25rem; display: block; }
.script-text { font-family: var(--font-heading); font-style: italic; font-size: 1.1rem; color: #831843; line-height: 1.5; margin: 0; }

.instruction-box { background: #EFF6FF; border: 1px solid #DBEAFE; border-radius: 12px; padding: 1.25rem; margin: 2rem 0; display: flex; gap: 1rem; color: #1E40AF; }
.instruction-icon { font-size: 1.5rem; }

/* Navigation Footer */
.lesson-nav { display: flex; justify-content: space-between; margin-top: 6rem; padding-top: 2rem; border-top: 1px solid #E5E7EB; }
.nav-btn { display: flex; flex-direction: column; text-decoration: none; padding: 1rem 2rem; border-radius: 8px; transition: all 0.2s; max-width: 45%; }
.nav-btn:hover { background: #F3F4F6; }
.nav-btn.disabled { opacity: 0; pointer-events: none; }
.nav-btn .nav-label { font-size: 0.75rem; text-transform: uppercase; color: #9CA3AF; font-weight: 700; margin-bottom: 0.25rem; }
.nav-btn .nav-title { font-family: var(--font-heading); font-size: 1.1rem; color: #1F2937; font-weight: 600; }
.nav-btn.prev { text-align: left; }
.nav-btn.next { text-align: right; }

@media (max-width: 768px) {
    .lesson-container { padding: 2rem 1.5rem; margin: 1rem; }
    .hero-title { font-size: 2.5rem; }
    .lesson-nav { flex-direction: column; gap: 1rem; }
    .nav-btn { max-width: 100%; text-align: center !important; background: #F9FAFB; }
}
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matemática Viva | Orchestrator Dashboard</title>
    <style>{{STYLE_CSS}}</style>
    <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>
    <!-- Mobile Elements -->
    <button class="mobile-toggle" onclick="toggleMenu()">☰</button>
    <div class="overlay" onclick="toggleMenu()"></div>

    <nav class="sidebar" id="sidebar">
        <div class="brand">
            <img src="assets/cards/guardioes/melquior-leao.png" alt="Logo" style="width: 32px; height: 32px;"> Matemática Viva
        </div>
        
        <div class="nav-section">Reino Contado</div>
        <a href="#sementes" class="nav-link"><span>🌱</span> Ciclo Sementes</a>
        <a href="#raizes" class="nav-link"><span>🌳</span> Ciclo Raízes</a>
        
        <div class="nav-section">Acervo Público</div>
        <a href="#blog" class="nav-link"><span>📝</span> Artigos & Ensaios</a>
        <a href="manual-portador.html" class="nav-link"><span>🔥</span> Manual do Portador</a>
        <a href="placeholders/biblioteca.html" class="nav-link"><span>📚</span> Biblioteca Pedagogia</a>
        
        <div class="nav-section">Sistema (Orchestrator)</div>
        <a href="placeholders/config.html" class="nav-link"><span>⚙️</span> Configurações</a>
    </nav>

    <main class="main-content">
        <header>
            <div class="role-badge">Admin: Maestro Raul</div>
            <h1>Visão Geral do Reino</h1>
            <p class="subtitle">O progresso da Matemática Viva, monitorado pelo Orchestrator. Aqui a "Qualidade Não é Negociável" se torna visível.</p>
        </header>

        <!-- ESTATÍSTICAS REMOVIDAS POR DESIGN REVIEW (Foco na Narrativa) -->
        <!--
        <section class="stats">
            <div class="stat-card">
                <div class="stat-val">{{TOTAL_SEMENTES}}</div>
                <div class="stat-label">Lições Sementes</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">{{TOTAL_RAIZES}}</div>
                <div class="stat-label">Lições Raízes</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">100%</div>
                <div class="stat-label">Conformidade North Star</div>
            </div>
        </section>
        -->

        <!-- SEMENTES -->
        <section id="sementes" class="mb-16">
            <div class="section-header">
                <div class="section-title"><span>🌱</span> Ciclo Sementes</div>
                <div class="section-meta">Estação 1: A Fundação • Build: {{DATA}}</div>
            </div>
            <div class="grid-cards">
                {{CARDS_SEMENTES}}
            </div>
        </section>

        <!-- RAIZES (Condicional via CSS ou não renderizado se vazio) -->
        <section id="raizes" style="margin-top: 6rem; display: {{DISPLAY_RAIZES}};">
            <div class="section-header">
                <div class="section-title"><span>🌳</span> Ciclo Raízes</div>
                <div class="section-meta">Estação 2: O Aprofundamento</div>
            </div>
            <div class="grid-cards">
                {{CARDS_RAIZES}}
            </div>
        </section>

        <!-- BLOG -->
        <section id="blog" style="margin-top: 6rem;">
            <div class="section-header">
                <div class="section-title"><span>📝</span> Blog & Ensaios</div>
                <div class="section-meta">Base de Conhecimento</div>
            </div>
            
            <div class="grid-cards">
                {{CARDS_BLOG}}
            </div>
            
            <div class="blog-empty" style="display: {{BLOG_EMPTY_DISPLAY}};">
                <h3>O sistema de blog está sendo forjado.</h3>
                <p>Nenhum artigo encontrado em blog/*.md</p>
            </div>
        </section>
        
        <footer style="margin-top: 6rem; border-top: 1px solid #E5E7EB; padding-top: 2rem; color: #9CA3AF; font-size: 0.875rem; display: flex; justify-content: space-between;">
            <div>&copy; 2026 Matemática Viva. Built by Orchestrator.</div>
            <div>Versão 2.1.0 (Narrative Focus)</div>
        </footer>
    </main>
</body>
</html>
<script>
    function toggleMenu() {
        document.getElementById('sidebar').classList.toggle('active');
        document.querySelector('.overlay').classList.toggle('active');
    }
    
    // Fechar ao clicar em link (UX)
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            if(window.innerWidth <= 1024) toggleMenu();
        });
    });
</script>
"""

def get_guardian_data(name):
    name = str(name).lower()
    if 'celeste' in name: return 'assets/cards/guardioes/celeste-raposa.png'
    if 'bernardo' in name: return 'assets/cards/guardioes/bernardo-urso.png'
    if 'noé' in name or 'noe' in name: return 'assets/cards/guardioes/noe-coruja.png'
    if 'íris' in name or 'iris' in name: return 'assets/cards/guardioes/iris-passarinho.png'
    return 'assets/cards/guardioes/melquior-leao.png'
    
def build_lesson_card(file_path, cycle_folder='sementes'):
    """Lê um YAML de lição e retorna o HTML do Card."""
    try:
        content = file_path.read_text(encoding='utf-8')
        data = {}
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 2: data = yaml.safe_load(parts[1])
        else:
            data = yaml.safe_load(content)
        
        # 1. Navegação Robusta por Metadados
        meta = data.get('licao', {}).get('metadados', {}) if 'licao' in data else data
        
        # 2. Busca Profunda de Ideia Viva
        ideia = ""
        licao_body = data.get('licao', {})
        if 'ideia_viva' in licao_body:
             ideia = licao_body['ideia_viva'].get('frase', '')
        if not ideia and 'para_portador' in licao_body:
            ideia = licao_body['para_portador'].get('ideia_viva', {}).get('frase', '')
        if not ideia: 
             ideia = data.get('ideia_viva', {}).get('frase', "A aventura começa aqui.")
        
        # 3. Identidade Visual
        titulo = meta.get('titulo', 'Sem Título')
        guardiao = meta.get('guardiao_lider', 'Melquior')
        
        # IDs e Tags
        raw_id = meta.get('id', 'L000') # Ex: L001
        # Formata para "Lição 001" (Remove chars não numéricos se quiser, mas raw é seguro)
        display_id = f"Lição {raw_id.replace('L', '')}" if raw_id.startswith('L') else raw_id
        
        tema_tag = meta.get('tipo', 'Geral') # Ex: Geometria / Espaço
        
        img_path = get_guardian_data(guardiao)
        link = f"{cycle_folder}/{file_path.stem}.html"
        
        # CSS Class
        css_class = 'melquior'
        if 'celeste' in guardiao.lower(): css_class = 'celeste'
        elif 'bernardo' in guardiao.lower(): css_class = 'bernardo'
        elif 'noe' in guardiao.lower() or 'noé' in guardiao.lower(): css_class = 'noe'
        elif 'iris' in guardiao.lower() or 'íris' in guardiao.lower(): css_class = 'iris'
        if cycle_folder == 'raizes': css_class = 'raizes'
        
        return f"""
        <article class="card {css_class}">
            <div class="card-body">
                <div class="card-meta">
                    <span class="card-id">{display_id}</span>
                    <img src="{img_path}" class="guardian-icon-img" alt="{guardiao}" title="{guardiao}">
                </div>
                <h3 class="card-title">{titulo}</h3>
                <p class="card-desc">“{ideia}”</p>
                
                <div class="card-objective" style="margin-top: 0.5rem; font-size: 0.8rem; color: #6B7280; border-top: 1px solid #F3F4F6; padding-top: 0.5rem; display: flex; align-items: center; gap: 0.25rem;">
                    <span>🏷️</span> <em>{tema_tag}</em>
                </div>
            </div>
            <div class="card-footer">
                <a href="{link}" class="btn-arr">Abrir Lição <span>→</span></a>
            </div>
        </article>
        """
    except Exception as e:
        print(f"❌ Erro em {file_path.name}: {e}")
        return ""
        
def build_blog_card(file_path):
    """Gera o HTML Card para um post de blog."""
    try:
        content = file_path.read_text(encoding='utf-8')
        # Frontmatter Parsing
        meta = {}
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 2:
                meta = yaml.safe_load(parts[1])
        
        if not meta: return ""
        
        titulo = meta.get('titulo', file_path.stem)
        data = meta.get('data', '')
        resumo = meta.get('resumo', 'Clique para ler este ensaio completo.')
        autor = meta.get('autor', 'Forja Viva')
        link = f"blog/{file_path.stem}.html"
        
        # Design Visual (Distinto das lições: Ícone de Lápis/Pen)
        return f"""
        <article class="card card-blog">
            <div class="card-body">
                <div class="card-meta">
                    <span class="card-id" style="background:#E0E7FF; color:#3730A3;">ARTIGO</span>
                    <span style="font-size: 2rem;">✍️</span> 
                </div>
                <h3 class="card-title">{titulo}</h3>
                <p class="card-desc" style="font-size: 0.95rem;">{resumo}</p>
                <div style="font-size: 0.8rem; color: #9CA3AF; margin-top: auto;">
                    {data} • {autor}
                </div>
            </div>
            <div class="card-footer">
                <a href="{link}" class="btn-arr" style="background: #4F46E5;">Ler Artigo <span>→</span></a>
            </div>
        </article>
        """
    except Exception as e:
        print(f"⚠️ [BLOG] Erro ao ler {file_path.name}: {e}")
        return ""

def get_blog_posts():
    """Varre a pasta blog e retorna os cards HTML ordenados."""
    blog_dir = Path("blog")
    if not blog_dir.exists(): return []
    
    posts = []
    files = sorted(list(blog_dir.glob("*.md")), reverse=True) # Mais recentes primeiro (por nome/data)
    
    for f in files:
        card = build_blog_card(f)
        if card: posts.append(card)
        
    return posts

def ensure_placeholders():
    """Garante a existência de páginas placeholder para links do menu."""
    ph_dir = OUTPUT_DIR / "placeholders"
    ph_dir.mkdir(parents=True, exist_ok=True)
    
    files = ['brotos.html', 'raizes.html', 'biblioteca.html', 'config.html', 'logica.html', 'legado.html']
    
    template_ph = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Em Breve | Matemática Viva</title>
    <link rel="stylesheet" href="../style.css">
    <style>
        body { display: flex; align-items: center; justify-content: center; height: 100vh; text-align: center; }
        .container { max-width: 500px; padding: 2rem; background: white; border-radius: 16px; box-shadow: 0 10px 40px -10px rgba(0,0,0,0.1); }
        h1 { color: #B8860B; font-family: 'Lora', serif; margin-bottom: 1rem; }
        p { color: #6B7280; margin-bottom: 2rem; }
        .btn { display: inline-block; padding: 0.75rem 1.5rem; background: #1F2937; color: white; border-radius: 8px; text-decoration: none; }
    </style>
</head>
<body>
    <div class="container">
        <div style="font-size: 4rem;">🚧</div>
        <h1>Em Construção</h1>
        <p>Esta seção do Reino Contado ainda está sendo plantada.</p>
        <a href="../index.html" class="btn">Voltar ao Mapa</a>
    </div>
</body>
</html>"""

    for f in files:
        path = ph_dir / f
        if not path.exists():
            path.write_text(template_ph, encoding='utf-8')
            print(f"   🚧 Placeholder criado: {f}")

def main():
    print("🥁 Orchestrator: Refinando Dashboard V3 (Multi-Ciclo)...")
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 0. ASSETS SYNC
    CARDS_SRC = Path("docs/cards/web")
    CARDS_DEST = OUTPUT_DIR / "assets/cards"
    
    if CARDS_SRC.exists():
        print(f"   ↳ Sincronizando Assets...")
        try:
            shutil.copytree(CARDS_SRC, CARDS_DEST, dirs_exist_ok=True)
        except Exception as e:
            print(f"   ⚠️ Aviso ao copiar assets: {e}")
    
    # 1. PLACEHOLDERS
    ensure_placeholders()

    # 2. BUILD DAS LIÇÕES (Via Script Externo)
    print("   ↳ Disparando Build de Lições...")
    import build_lessons
    build_lessons.main()

    # 3. BUILD DO BLOG
    print("   ↳ Disparando Build de Blog...")
    try:
        import blog_builder
        blog_builder.main()
    except ImportError:
        print("   ⚠️ Blog Builder não encontrado.")
    
    # 4. GERAR DASHBOARD (INDEX)
    (OUTPUT_DIR / "style.css").write_text(STYLE_CSS, encoding='utf-8')
    
    # Cards Sementes
    cards_sementes = []
    if INPUT_DIR_SEMENTES.exists():
        files = sorted(list(INPUT_DIR_SEMENTES.glob("*.yaml")))
        for f in files:
            c = build_lesson_card(f, 'sementes')
            if c: cards_sementes.append(c)

    # Cards Raízes
    cards_raizes = []
    if INPUT_DIR_RAIZES.exists():
        files = sorted(list(INPUT_DIR_RAIZES.glob("*.yaml")))
        for f in files:
            c = build_lesson_card(f, 'raizes')
            if c: cards_raizes.append(c)
    
    # Cards Blog
    blog_cards = get_blog_posts()
    
    # Template Replacement
    html = HTML_TEMPLATE.replace("{{STYLE_CSS}}", STYLE_CSS) # Inject CSS directly
    html = html.replace("{{CARDS_SEMENTES}}", "\n".join(cards_sementes))
    html = html.replace("{{TOTAL_SEMENTES}}", str(len(cards_sementes)))
    
    html = html.replace("{{CARDS_RAIZES}}", "\n".join(cards_raizes))
    html = html.replace("{{TOTAL_RAIZES}}", str(len(cards_raizes)))
    html = html.replace("{{DISPLAY_RAIZES}}", "grid" if cards_raizes else "none")
    
    html = html.replace("{{CARDS_BLOG}}", "\n".join(blog_cards))
    html = html.replace("{{BLOG_EMPTY_DISPLAY}}", "none" if blog_cards else "block")
    
    html = html.replace("{{DATA}}", datetime.now().strftime("%d/%m/%Y %H:%M"))
    
    OUTPUT_HTML.write_text(html, encoding='utf-8')
    print(f"✨ Dashboard Impecável gerado em: {OUTPUT_HTML}")
    
    # 5. Validação Final (Safety Check)
    manual_path = OUTPUT_DIR / "manual-portador.html"
    if manual_path.exists():
        print("   ✅ Validação: Manual do Portador está seguro.")
    else:
        print("   ❌ ALERTA: Manual do Portador desapareceu!")

if __name__ == "__main__":
    main()
