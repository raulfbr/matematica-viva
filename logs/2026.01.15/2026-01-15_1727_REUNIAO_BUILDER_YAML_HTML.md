# REUNIÃO DELIBERATIVA: Builder YAML → HTML
**Data:** 15/01/2026 17:27 | **Modo:** REUNIAO_TODOS | **Tema:** Estruturar Builder de Lições
**Status:** EM_ANDAMENTO

---

## CONVOCATÓRIA

### Contexto
O Maestro solicitou planejamento completo para criar um **builder que transforma YAML em HTML premium**.

### Referências Analisadas
| Tipo | Arquivo | Linhas/KB |
|------|---------|-----------|
| YAML Source | `curriculo/01_SEMENTES/001_TRINDADE_PALMA.yaml` | 519 linhas (20.2 KB) |
| HTML Target | `site/TESTE/001_VER_C_PRIME.html` | 465 linhas (20.2 KB) |

### Observação do Maestro
> "Somente L001 tem muitas linhas, L002 para frente são menores (incompletas)"

---

## FASE 1: ANÁLISE TÉCNICA (Engenharia)

### Estrutura YAML (Source)
```yaml
licao:
  metadados:       # id, titulo, fase, guardiao, tgtb_ref
  ideia_viva:      # frase, conceito, intencao_cm
  atmosfera:       # clima, local, virtude, artefato
  linkage:         # elo_anterior, proximo_passo
  preparacao:      # tempo, materiais
  para_o_portador: # dica_coracao, protocolo, audio_script, nota_graca
  ritual_abertura: # instrucao, transicao, fala_portador
  jornada:
    abertura_sensorial:
    narrativa_principal:
      cena_1...cena_N:
    concreto:
    pictorico:     # pode ser vetado
    abstrato:
    extensao:
  narracao:        # pergunta_principal, perguntas_coracao
  ritual_fechamento:
  catedra_pais:
  sugestoes:
  diario_portador:
  auditoria_qa:
lore_extraido:
```

### Estrutura HTML (Target)
```html
<html>
  <head> <!-- Meta, CSS, Fonts -->
  <body class="clima-{clima}">
    <lesson-container>
      <header class="lesson-hero"> <!-- titulo, quote, guardiao -->
      <article class="lesson-body">
        <!-- CARDS: -->
        <div class="scene-card"> Preparação </div>
        <div class="scene-card"> Ritual Abertura </div>
        <h2> A Jornada </h2>
        <div class="scene-card"> Cena 1 </div>
        ...
        <h2> O Concreto </h2>
        <div class="scene-card"> Concreto </div>
        <div class="scene-card"> Narração </div>
        <div class="scene-card"> Fechamento </div>
      </article>
      <nav class="lesson-nav"> <!-- anterior/próxima -->
      <footer>
    </lesson-container>
  </body>
</html>
```

### Componentes HTML Identificados

| Componente | Classe CSS | Uso |
|------------|------------|-----|
| Hero | `.lesson-hero` | Título, quote, guardião |
| Card | `.scene-card` | Container de cada seção |
| Persona Block | `.script-persona-block` | Fala de guardião/portador |
| Instruction Box | `.instruction-box` | Instruções ao portador |
| Section Header | `<h2>` inline style | Divisor de fases |
| Navigation | `.lesson-nav` | Links anterior/próxima |

### Mapeamento YAML → HTML

| YAML Section | HTML Output |
|--------------|-------------|
| `metadados` | Hero + meta-tag |
| `ideia_viva.frase` | Hero quote |
| `atmosfera.clima` | body class |
| `para_o_portador` | Card "Preparação" |
| `ritual_abertura` | Card "Ritual de Abertura" |
| `jornada.cena_N` | Cards individuais por cena |
| `jornada.concreto` | Card "Atividade Concreta" |
| `narracao` | Card "Narramos Juntos" |
| `ritual_fechamento` | Card "Ritual de Fechamento" |
| `linkage` | Navigation footer |

---

## FASE 2: POSIÇÕES DOS EXPERTS

### Charlotte Mason (Pedagógica)
> "O builder deve preservar a ATMOSFERA. Não é só converter texto — é manter o encanto.
> 
> **Requisitos:**
> 1. Hero com quote inspiradora (ideia_viva)
> 2. Clima visual (classe CSS por atmosfera)
> 3. Cards que fluem como história, não lista
> 4. Persona blocks com avatar do guardião
> 
> **Crítico:** A transição para o Reino deve ser SENTIDA no HTML."

### Jerome Bruner (CPA)
> "O HTML deve refletir a progressão C→P→A.
> 
> **Requisitos:**
> 1. Seção Concreto deve ser DESTACADA (Norte Absoluto)
> 2. Pictórico pode estar ausente (vetado em Sementes)
> 3. Abstrato deve ser sutil, não dominante
> 4. Indicadores visuais de fase (ícones, cores)"

### JRR Tolkien (Consistência)
> "Cada guardião deve ter identidade visual consistente.
> 
> **Requisitos:**
> 1. Avatar correto por guardião (celeste-raposa.png)
> 2. Cor de borda por guardião (Celeste = green)
> 3. Tom de fala entre parênteses (Animada, Misteriosa)
> 4. Local e clima devem mapear para classes CSS"

### Beatrix Potter (Visual)
> "O HTML deve ser BONITO, não funcional.
> 
> **Requisitos:**
> 1. Cards com sombra suave (prime shadow)
> 2. Fio dourado (gold accent no topo do card)
> 3. Tipografia elegante (Outfit + Lora)
> 4. Mobile-first (768px max-width)"

### Alex Hormozi (Eficiência)
> "Um builder que leva horas é inútil.
> 
> **Requisitos:**
> 1. Processar 1 YAML em < 1 segundo
> 2. Batch processing de todas as lições
> 3. Hot reload para desenvolvimento
> 4. Error reporting claro"

### Seth Godin (Tribal)
> "O HTML é a primeira impressão da tribo.
> 
> **Requisitos:**
> 1. Branding consistente (Matemática Viva)
> 2. Footer com identidade
> 3. Meta tags para SEO
> 4. Compartilhável (OG tags)"

### Engenharia (Técnica)
> "Precisamos de arquitetura limpa.
> 
> **Requisitos:**
> 1. Python como linguagem (já existe build_lessons.py?)
> 2. Jinja2 ou similar para templates
> 3. CSS em arquivo separado (style.css)
> 4. Assets em diretório organizado
> 5. CLI com opções (--watch, --single, --all)"

### Design
> "O CSS do referência é bom, mas inline styles são ruins.
> 
> **Requisitos:**
> 1. Extrair inline styles para style.css
> 2. Variáveis CSS (--color-gold, --font-heading)
> 3. Dark mode opcional
> 4. Print-friendly"

### Peter Thiel (10x)
> "O builder deve ser tão bom que é difícil de copiar.
> 
> **Requisitos:**
> 1. Não só converter — VALIDAR durante build
> 2. QA automática (seções obrigatórias)
> 3. Relatório de problemas
> 4. Linkage verification (arquivos existem?)"

---

## FASE 3: CONSULTA EXTERNA

### Externos Selecionados

#### Mãe Veterana
> "Eu não me importo com código. Quero ver a lição no celular.
> 
> **Pergunta:** O builder vai gerar HTML que funciona no Safari do iPhone?"

#### Pai Tech
> "Cadê o deploy automático? Vercel? GitHub Pages?
> 
> **Pergunta:** O builder integra com CI/CD?"

#### Criança 8 Anos
> "Vai ter desenhos bonitos? As cores que eu gosto?
> 
> **Pergunta:** (tradução) As imagens dos guardiões vão aparecer corretamente?"

---

## FASE 4: SÍNTESE (Charlotte Mason)

### Arquitetura Proposta

```
┌─────────────────────────────────────────────────────────────┐
│                     BUILD PIPELINE                           │
│                                                              │
│  curriculo/01_SEMENTES/*.yaml                               │
│           ↓                                                  │
│  ┌─────────────────┐   ┌──────────────────┐                 │
│  │   YAML Parser   │ → │   QA Validation  │                 │
│  └─────────────────┘   └──────────────────┘                 │
│           ↓                     ↓                           │
│  ┌─────────────────┐   ┌──────────────────┐                 │
│  │ Template Engine │ ← │  Error Report    │                 │
│  │    (Jinja2)     │   └──────────────────┘                 │
│  └─────────────────┘                                        │
│           ↓                                                  │
│  ┌─────────────────┐                                        │
│  │   HTML Output   │ → site/sementes/001_TRINDADE.html     │
│  └─────────────────┘                                        │
│           ↓                                                  │
│  ┌─────────────────┐                                        │
│  │  Assets Copy    │ → assets/cards/guardioes/              │
│  └─────────────────┘                                        │
└─────────────────────────────────────────────────────────────┘
```

### Estrutura de Diretórios

```
Project001-MatematicaVivaV4/
├── .bmad/
│   └── builder/
│       ├── build_lessons.py      # CLI principal
│       ├── templates/
│       │   ├── base.html         # Template base
│       │   ├── lesson.html       # Template de lição
│       │   └── components/
│       │       ├── hero.html
│       │       ├── card.html
│       │       ├── persona.html
│       │       └── nav.html
│       ├── validators/
│       │   ├── qa_cm.py          # Validação CM
│       │   ├── qa_cpa.py         # Validação CPA
│       │   └── qa_template.py    # Validação estrutura
│       └── config.yaml           # Configuração do builder
├── curriculo/
│   └── 01_SEMENTES/
│       └── *.yaml                # Source files
├── site/
│   └── sementes/
│       └── *.html                # Output files
└── assets/
    ├── cards/
    ├── style.css
    └── favicon.ico
```

### Funcionalidades do Builder

| Feature | Prioridade | Descrição |
|---------|------------|-----------|
| YAML → HTML | P0 | Conversão básica |
| QA Validation | P0 | Verifica seções obrigatórias |
| Linkage Check | P0 | Verifica anterior/próxima existem |
| Guardião Avatar | P0 | Mapeia guardião → imagem |
| Clima CSS | P0 | Classe body por clima |
| Mobile-first | P0 | CSS responsivo |
| Batch Mode | P1 | Processar todas lições |
| Watch Mode | P1 | Hot reload |
| Error Report | P1 | Log de problemas |
| SEO Tags | P2 | Meta, OG |
| Print CSS | P3 | Versão impressão |

### Comandos CLI

```bash
# Construir uma lição
python build_lessons.py --single 001_TRINDADE_PALMA.yaml

# Construir todas as lições
python build_lessons.py --all

# Modo watch (dev)
python build_lessons.py --watch

# Com validação estrita
python build_lessons.py --all --strict

# Gerar relatório QA
python build_lessons.py --qa-report
```

---

## FASE 5: DECISÃO FINAL

### DELIBERAÇÃO APROVADA

| Item | Decisão |
|------|---------|
| Linguagem | Python 3.x |
| Template Engine | Jinja2 |
| Estrutura | Modular (builder, templates, validators) |
| Output | site/sementes/*.html |
| Validação | QA durante build |
| Prioridade | P0 features primeiro |

### BIG TASK — Checklist de Implementação

#### Fase 1: Infraestrutura (2h)
- [ ] Criar diretório `.bmad/builder/`
- [ ] Criar `build_lessons.py` (CLI skeleton)
- [ ] Criar `config.yaml` com paths
- [ ] Setup Jinja2 environment

#### Fase 2: Templates (3h)
- [ ] Criar `templates/base.html` (head, body structure)
- [ ] Criar `templates/lesson.html` (extends base)
- [ ] Criar `templates/components/hero.html`
- [ ] Criar `templates/components/card.html`
- [ ] Criar `templates/components/persona.html`
- [ ] Criar `templates/components/instruction.html`
- [ ] Criar `templates/components/nav.html`

#### Fase 3: Parser YAML (2h)
- [ ] Função `parse_lesson(yaml_path)` → dict
- [ ] Mapear seções YAML para contexto Jinja
- [ ] Handler para seções ausentes (lições incompletas)
- [ ] Extração de guardiões e avatares

#### Fase 4: Renderização (2h)
- [ ] Função `render_lesson(context)` → HTML
- [ ] Mapear clima → classe CSS
- [ ] Renderizar cenas dinamicamente
- [ ] Linkage navigation

#### Fase 5: Validação QA (2h)
- [ ] Criar `validators/qa_template.py`
- [ ] Verificar seções obrigatórias
- [ ] Verificar linkage (arquivos existem)
- [ ] Verificar guardiões (imagens existem)
- [ ] Relatório de erros

#### Fase 6: CLI e Batch (1h)
- [ ] Argparse para --single, --all, --watch
- [ ] Processar múltiplos arquivos
- [ ] Logging de progresso
- [ ] Exit codes corretos

#### Fase 7: CSS e Assets (1h)
- [ ] Consolidar CSS em `style.css`
- [ ] Variáveis CSS
- [ ] Verificar assets existem
- [ ] Copiar assets se necessário

#### Fase 8: Teste e Validação (2h)
- [ ] Build L001 e comparar com referência
- [ ] Build L002-L015 (lições incompletas)
- [ ] Verificar mobile
- [ ] Verificar links funcionam

### Estimativa Total
**~15 horas de desenvolvimento**

### Próximo Passo Imediato
```
Criar `.bmad/builder/` e iniciar build_lessons.py
```

---

## VOTAÇÃO FINAL

| Expert | Voto |
|--------|------|
| Charlotte Mason | ✅ APROVA |
| Jerome Bruner | ✅ APROVA |
| JRR Tolkien | ✅ APROVA |
| Beatrix Potter | ✅ APROVA |
| Alex Hormozi | ✅ APROVA (com ressalva: foco P0) |
| Seth Godin | ✅ APROVA |
| Engenharia | ✅ APROVA |
| Design | ✅ APROVA |
| Peter Thiel | ✅ APROVA |
| Mãe Veterana | ✅ APROVA (quer ver no celular) |
| Pai Tech | ✅ APROVA (quer CI/CD depois) |
| Criança 8 Anos | ✅ APROVA (quer desenhos bonitos) |

**CONSENSO: 100%**

---

**REUNIÃO CONCLUÍDA: 15/01/2026 17:35**
**DECISÃO:** Implementar builder conforme BIG TASK acima.
**AGUARDA:** Aprovação do Maestro para iniciar execução.
