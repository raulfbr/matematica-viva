"""
🔨 LESSON BUILDER V2 (Multi-Cycle + Smart Build)
================================================
Gera páginas HTML para todos os ciclos do currículo.
Suporta: Sementes, Raízes.
Otimização: Smart Build (Rebuild apenas se modificado).
"""

import os
import yaml
from pathlib import Path
import re

# CONFIGURAÇÃO DE CICLOS (Map Universal)
CYCLES_CONFIG = [
    {
        'id': 'sementes',
        'input': Path("curriculo/01_SEMENTESV6"),
        'output': Path("site/sementes"),
        'name': 'Ciclo Sementes'
    },
    {
        'id': 'raizes',
        'input': Path("curriculo/02_RAIZES/01_RAIZES_I"), # Focando em Raízes I por enquanto
        'output': Path("site/raizes"),
        'name': 'Ciclo Raízes'
    }
]

# TEMPLATE PADRÃO
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITULO}} | Matemática Viva</title>
    <link rel="stylesheet" href="../style.css">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;700&family=Lora:ital,wght@0,400;0,600;1,400&family=Gloria+Hallelujah&display=swap" rel="stylesheet">
    <link rel="icon" href="../favicon.ico" type="image/x-icon">
</head>
<body class="{{CLIMA_CLASS}} cy-{{CYCLE_ID}}">
    <a href="../index.html" class="home-btn" title="Voltar ao Dashboard">🏡</a>

    <div class="lesson-container">
        
        <!-- Premium Hero Section -->
        <header class="lesson-hero">
            <div class="lesson-meta-tag">{{ID}} • {{TEMPO}} • {{CLIMA}}</div>
            <h1 class="hero-title">{{TITULO}}</h1>
            <p class="hero-quote">"{{IDEIA_VIVA}}"</p>
            <img src="{{GUARDIAO_IMG}}" alt="{{GUARDIAO}}" class="hero-guardian" title="Seu Guia: {{GUARDIAO}}">
        </header>

        <!-- Content Body -->
        <article class="lesson-body">
            {{CONTEUDO_HTML}}
        </article>

        <!-- Navigation Footer -->
        <nav class="lesson-nav">
            {{LINK_PREV}}
            {{LINK_NEXT}}
        </nav>
        
        <footer style="text-align: center; margin-top: 4rem; color: #A8A29E; font-size: 0.8rem;">
            Matemática Viva • {{CYCLE_NAME}}
        </footer>
    </div>
</body>
</html>
"""

def simple_markdown_to_html(md_text):
    """Conversor ultra-simples de MD para HTML para manter integridade."""
    if not md_text: return ""
    html = str(md_text)
    
    # Headers
    html = re.sub(r'^### (.*$)', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*$)', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    
    # Bold/Italic
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Lists (Simples)
    lines = html.split('\n')
    new_lines = []
    in_list = False
    
    for line in lines:
        if line.strip().startswith('- '):
            if not in_list:
                new_lines.append('<ul>')
                in_list = True
                
            # Check for bold within list item
            content = line.strip()[2:]
            content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)
            new_lines.append(f'<li>{content}</li>')
        else:
            if in_list:
                new_lines.append('</ul>')
                in_list = False
            if line.strip():
                if not line.startswith('<h') and not line.startswith('<ul') and not line.startswith('<li'):
                     new_lines.append(f'<p>{line}</p>')
                else:
                    new_lines.append(line)
    
    if in_list: new_lines.append('</ul>')
    return "\n".join(new_lines)

def load_lessons_from_dir(input_dir):
    """Lê lições de um diretório específico."""
    lessons = []
    if not input_dir.exists(): 
        # Tenta verificar se tem subpastas (Recursivo simples)
        # Se não existir, retorna vazio
        return []

    # Procura recursive em subpastas também, ou apenas no root?
    # Para Raízes, está em 01_RAIZES_I... vamos varrer recurisvamente
    files = sorted(list(input_dir.rglob("*.yaml")))
    
    for f in files:
        try:
            content = f.read_text(encoding='utf-8')
            data = {}
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 2: data = yaml.safe_load(parts[1])
            else:
                data = yaml.safe_load(content)
            
            # Normalização de Chaves
            meta = data.get('licao', {}).get('metadados', {}) if 'licao' in data else data
            ideia = data.get('licao', {}).get('ideia_viva', {}).get('frase', '') if 'licao' in data else data.get('ideia_viva', {}).get('frase', '')
            corpo = data.get('licao', {}) if 'licao' in data else data
            
            content_dict = {k:v for k,v in corpo.items() if k not in ['metadados', 'ideia_viva']}
            
            lid = meta.get('id', 'MV-X-XXX')
            # Extract number for sorting
            sort_num = 999
            numbers = re.findall(r'\d+', lid)
            if numbers: sort_num = int(numbers[0])

            lessons.append({
                'file_stem': f.stem,
                'file_path': f,
                'id': lid,
                'sort_id': sort_num,
                'titulo': meta.get('titulo', 'Sem Título'),
                'ideia': ideia,
                'guardiao': meta.get('guardiao_lider', 'Melquior'),
                'tempo': meta.get('tempo_estimado', '20 min'),
                'clima': meta.get('clima', 'Ensolarado'),
                'raw_content': content_dict
            })
        except Exception as e:
            print(f"⚠️ Erro ao carregar {f.name}: {e}")
            
    return sorted(lessons, key=lambda x: x['sort_id'])

def get_guardian_data(name):
    name = str(name).lower()
    if 'celeste' in name: return '../assets/cards/guardioes/celeste-raposa.png'
    if 'bernardo' in name: return '../assets/cards/guardioes/bernardo-urso.png'
    if 'noé' in name or 'noe' in name: return '../assets/cards/guardioes/noe-coruja.png'
    if 'íris' in name or 'iris' in name: return '../assets/cards/guardioes/iris-passarinho.png'
    return '../assets/cards/guardioes/melquior-leao.png'

def render_rich_content(key, value):
    """Renderiza blocos ricos (Personas, Dicas)."""
    key_lower = str(key).lower()
    
    # 1. Rich Persona Block
    if 'fala' in key_lower or 'guardiao' in key_lower or 'portador' in key_lower:
        nome_guardiao = str(key).replace('fala_', '').replace('_', ' ').strip().title()
        if 'Portador' in nome_guardiao:
            avatar_img = "../assets/cards/guardioes/melquior-leao.png" # Default/User avatar
        else:
            avatar_img = get_guardian_data(nome_guardiao)
            
        script_text = value
        if isinstance(value, dict):
             script_text = value.get('script', '') or value.get('fala', '') or str(value)

        return f'''
        <div class="script-persona-block">
            <img src="{avatar_img}" class="script-avatar" alt="{nome_guardiao}">
            <div class="script-content">
                <div class="script-header">
                    <span class="script-name">{nome_guardiao}</span>
                </div>
                <p class="script-text">"{script_text}"</p>
            </div>
        </div>
        '''

    # 2. Instruction Box
    elif 'instrucao' in key_lower or 'dica' in key_lower:
        instruction_text = value
        if isinstance(value, dict):
            instruction_text = value.get('script', '') or value.get('instrucao', '') or str(value)
            
        return f'''
        <div class="instruction-box">
            <span class="instruction-icon">💡</span>
            <div>{instruction_text}</div>
        </div>
        '''
    return None

def render_recursive(data, level=2):
    """Recursividade para aninhamento infinito."""
    html_parts = []
    
    if isinstance(data, dict):
        for k, v in data.items():
            key_clean = k.replace('_', ' ').title()
            
            rich_html = render_rich_content(k, v)
            if rich_html:
                html_parts.append(rich_html)
                continue
                
            if isinstance(v, dict):
                header_tag = f"h{min(level+1, 6)}"
                html_parts.append(f"<{header_tag}>{key_clean}</{header_tag}>")
                html_parts.append("<div class='nested-section'>")
                html_parts.append(render_recursive(v, level+1))
                html_parts.append("</div>")
            elif isinstance(v, list):
                # Detecta se é uma lista complexa (cenas, passos) ou simples (strings)
                is_complex = any(isinstance(i, dict) for i in v)
                
                if is_complex:
                    # Sem Header Genérico para não poluir
                    for item in v:
                        if isinstance(item, dict):
                             html_parts.append("<div class='list-item-block' style='margin-bottom: 1.5rem; border-bottom: 1px dashed #E5E7EB; padding-bottom: 1rem;'>")
                             
                             # Promove Título (se houver)
                             if 'titulo' in item:
                                 html_parts.append(f"<h4 style='color: #92400E; margin-bottom: 0.5rem; font-size: 1.1rem;'>{item['titulo']}</h4>")
                             
                             # Renderiza resto
                             remaining = {k:val for k,val in item.items() if k != 'titulo'}
                             html_parts.append(render_recursive(remaining, level+1))
                             html_parts.append("</div>")
                        else:
                             html_parts.append(f"<p>{item}</p>")
                else:
                    # Lista Simples (Bullets)
                    html_parts.append(f"<p><strong>{key_clean}:</strong></p><ul>")
                    for item in v: 
                        html_parts.append(f"<li>{item}</li>")
                    html_parts.append("</ul>")
            else:
                if 'descricao' in k.lower() or 'narrativa' in k.lower() or 'script' in k.lower():
                     html_parts.append(simple_markdown_to_html(str(v)))
                else:
                     html_parts.append(f"<p><strong>{key_clean}:</strong> {v}</p>")
                     
    return "\n".join(html_parts)

def format_content(content_dict):
    """Engine de transformação YAML -> HTML."""
    if not content_dict: return ""
    html_parts = []
    
    # Ordem Lógica (Sementes) - Padrão, mas flexível
    order = [
         'preparacao_do_portador', 'para_o_portador', 
         'ritual_abertura', 
         'jornada', 
         'atividade_concreta', 'concreto', 
         'atividade_pictorica', 'pictorico',
         'atividade_abstrata', 'abstrato',
         'narramos_juntos', 'narracao', 
         'ritual_fechamento'
    ]
    
    labels = {
        'preparacao_do_portador': '👨‍👩‍👧 Preparação do Portador',
        'para_o_portador': '👨‍👩‍👧 Preparação do Portador',
        'ritual_abertura': '🎬 Ritual de Abertura',
        'jornada': '🗺️ A Jornada',
        'atividade_concreta': '🧱 Atividade Concreta',
        'concreto': '🧱 Atividade Concreta',
        'atividade_pictorica': '🎨 Atividade Pictórica',
        'pictorico': '🎨 Atividade Pictórica',
        'atividade_abstrata': '🔢 Atividade Abstrata',
        'abstrato': '🔢 Atividade Abstrata',
        'narramos_juntos': '🗣️ Narramos Juntos',
        'narracao': '🗣️ Narramos Juntos',
        'ritual_fechamento': '🏁 Ritual de Fechamento'
    }

    # 1. Render Known Sections in Order
    for key in order:
        if key in content_dict and content_dict[key]:
            section = content_dict[key]
            html_parts.append(f"<h2>{labels.get(key, key.title())}</h2>")
            html_parts.append(render_recursive(section, level=2))

    # 2. Render Remaining Sections (Raízes pode ter items novos)
    for key, value in content_dict.items():
        if key not in order and isinstance(value, (dict, list, str)):
             # Ignore simple metadata
             if key in ['id', 'titulo', 'metadados']: continue
             html_parts.append(f"<h2>{key.replace('_', ' ').title()}</h2>")
             html_parts.append(render_recursive(value, level=2))
             
    return "\n".join(html_parts)

def main():
    print("🚀 Iniciando Lesson Builder V2 (Multi-Ciclo)...")
    
    for cycle in CYCLES_CONFIG:
        print(f"👉 Processando Ciclo: {cycle['name']}")
        
        cycle['output'].mkdir(parents=True, exist_ok=True)
        lessons = load_lessons_from_dir(cycle['input'])
        
        print(f"   📦 Encontradas: {len(lessons)} lições.")
        
        for i, lesson in enumerate(lessons):
            prev_lesson = lessons[i-1] if i > 0 else None
            next_lesson = lessons[i+1] if i < len(lessons)-1 else None
            
            guardiao_img = get_guardian_data(lesson.get('guardiao', 'Melquior'))
            
            # HTML Injection
            html = HTML_TEMPLATE
            html = html.replace('{{TITULO}}', str(lesson.get('titulo', '')))
            html = html.replace('{{ID}}', str(lesson.get('id', '')))
            html = html.replace('{{IDEIA_VIVA}}', str(lesson.get('ideia', '')))
            html = html.replace('{{GUARDIAO}}', str(lesson.get('guardiao', '')))
            html = html.replace('{{GUARDIAO_IMG}}', guardiao_img)
            html = html.replace('{{TEMPO}}', str(lesson.get('tempo', '')))
            html = html.replace('{{CLIMA}}', str(lesson.get('clima', '')))
            html = html.replace('{{CLIMA_CLASS}}', f"clima-{str(lesson.get('clima', '')).lower()}")
            html = html.replace('{{CYCLE_ID}}', cycle['id'])
            html = html.replace('{{CYCLE_NAME}}', cycle['name'])
            
            content_html = format_content(lesson['raw_content'])
            html = html.replace('{{CONTEUDO_HTML}}', content_html)
            
            # Nav Links
            if prev_lesson:
                link_prev = f'<a href="{prev_lesson["file_stem"]}.html" class="nav-btn prev"><span class="nav-label">← Anterior</span><span class="nav-title">{prev_lesson["titulo"]}</span></a>'
            else:
                link_prev = '<div class="nav-btn prev disabled"></div>'
            if next_lesson:
                link_next = f'<a href="{next_lesson["file_stem"]}.html" class="nav-btn next"><span class="nav-label">Próxima →</span><span class="nav-title">{next_lesson["titulo"]}</span></a>'
            else:
                link_next = '<div class="nav-btn next disabled"></div>'
                
            html = html.replace('{{LINK_PREV}}', link_prev)
            html = html.replace('{{LINK_NEXT}}', link_next)
            
            # File Write with SMART BUILD
            out_file = cycle['output'] / f"{lesson['file_stem']}.html"
            
            # PROTEÇÃO DA LIÇÃO 000 (Manual)
            is_lesson_000 = "000_PORTAL" in out_file.name
            if is_lesson_000 and out_file.exists():
                # print(f"  🔒 Skipped (Manual Lock): {out_file.name}")
                continue

            if out_file.exists():
                src_mtime = lesson.get('file_path').stat().st_mtime
                dst_mtime = out_file.stat().st_mtime
                if dst_mtime > src_mtime:
                    # Cache Hit
                    continue 

            out_file.write_text(html, encoding='utf-8')
            print(f"   ✅ Gerada ({cycle['id']}): {out_file.name}")

    print("✨ Build de Lições Concluído!")

if __name__ == "__main__":
    main()
