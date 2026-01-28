# Planejamento Impecável: Correção Definitiva do Sistema (Blog & Mobile)

**Data:** 2026-01-22
**Hora:** 14:05 (Atualizado)
**Status:** Planejamento Detalhado (Aguardando Aprovação)
**Assunto:** Solução para o desaparecimento do Index do Blog e implementação da Navegação Mobile.

## 1. O Diagnóstico Duplo

### A. O Mistério do Blog Desaparecido
Ao rodar o comando de build (`gutebreg` / `build_dashboard.py`), o arquivo `index.html` é regerado do zero.
- **Causa Raiz:** O script de build possui uma seção fixa (Hardcoded) que diz "Em Construção". Ele ignora completamente os artigos que existem na pasta `blog/`.
- **Consequência:** Toda vez que o site é reconstruído, a lista de blogs some.

### B. O Sumiço da Sidebar no Mobile
O usuário relatou que o menu lateral (Sidebar) some ao acessar pelo celular.
- **Causa Raiz:** Identifiquei no código CSS (gerado pelo `build_dashboard.py`) a seguinte regra explícita:
  ```css
  @media (max-width: 1024px) {
      .sidebar { display: none; } /* O Culpado */
  }
  ```
- **Consequência:** Em telas menores que 1024px (tablets e celulares), a navegação é totalmente removida, deixando o usuário "preso" na página sem poder navegar.

---

## 2. A Solução Impecável (O Plano)

Nosso objetivo é criar um sistema **Antifrágil**: quanto mais mexemos, melhor ele fica. Nada deve quebrar ao adicionar conteúdo novo.

### Frente 1: Automação Inteligente do Blog
Para nunca mais perder o index, vamos ensinar o `build_dashboard.py` a ler os blogs.

1.  **Varredura Automática:**
    - O script irá listar todos os arquivos `.md` e `.html` da pasta `blog/`.
    - Ele lerá o "Frontmatter" (metadados) para capturar: Título, Data, Resumo e Imagem de Capa (se houver).
    - **Ordenação:** Os posts serão ordenados automaticamente do mais recente para o mais antigo.

2.  **Injeção de Cards Dinâmicos:**
    - Em vez do texto "Em Construção", o script gerará HTML para cada post encontrado.
    - Se houver posts: Mostra a grade de cards bonitos (Estilo Glassmorphism).
    - Se *não* houver posts: Mostra a mensagem de espera (Fallback).

3.  **Resultado:** Você escreve o texto no Markdown, roda o build, e ele aparece magicamente na Home. Sem editar HTML manual.

### Frente 2: Navegação Mobile Premium
Para o celular, vamos implementar uma **Navegação Responsiva Híbrida**.

1.  **Menu "Hambúrguer" Elegante:**
    - Criar um botão flutuante ou fixo no topo (Header Mobile) que só aparece em telas pequenas.
    - Ícone: ☰ (Menu).

2.  **Sidebar como "Gaveta" (Drawer):**
    - Ao clicar no botão, a Sidebar (que estava escondida) deslizará suavemente da esquerda para a direita (animação slide-in).
    - Adicionar um fundo escurecido (overlay) atrás para focar na navegação.
    - Botão "X" para fechar.

3.  **Ajuste no CSS:**
    - Remover o `display: none` brutal.
    - Substituir por uma lógica de `transform: translateX(-100%)` (escondido fora da tela) e `transform: translateX(0)` (visível) controlada por um pequeno JavaScript injetado automaticamente.

### Frente 3: O "Gutebreg" Robusto (Orchestration)
Vamos garantir que o comando de build faça tudo de uma vez.

- O `build_dashboard.py` passará a importar e executar o `blog_builder.py` internamente.
- **Fluxo Único:**
  1. Limpa a pasta `site/`.
  2. Gera todos os artigos do Blog.
  3. Gera todas as Lições (Sementes).
  4. Constrói o `index.html` juntando tudo (Lições + Blog + Menu Mobile).
  5. Copia os assets.

---

## 3. Checklist de Execução

Ao receber seu "OK", executarei exatamente estes passos:

1.  **[CODE] Atualizar `tools/build_dashboard.py`**:
    - [ ] Adicionar função `get_blog_posts()`.
    - [ ] Adicionar lógica de Sidebar Mobile (CSS + JS simples).
    - [ ] Integrar chamada ao `blog_builder`.
2.  **[TESTE] Validação**:
    - [ ] Rodar o build.
    - [ ] Verificar se os blogs apareceram na Home.
    - [ ] Verificar (via simulação) se o menu aparece em resolução mobile.

## 4. Refinamentos Técnicos (Incrementos de Planejamento)

*Adicionado em 22/01/2026 às 14:08 - Detalhamento para execução impecável.*

### 4.1. Especificação da Navegação Mobile (Detalhe)
Para garantir que a solução não seja apenas funcional, mas **premium**:

*   **Design da Sidebar (Drawer):**
    *   Não usar `display: none`. Usar `transform: translateX(-100%)` para performance (GPU acceleration).
    *   **Animação:** `transition: transform 0.3s cubic-bezier(0.4, 0.0, 0.2, 1);` (Movimento fluido natural).
    *   **Overlay (Fundo):** Criar um elemento `div.overlay` que escurece o fundo (`rgba(0,0,0,0.4)`) e aplica `backdrop-filter: blur(2px)` quando o menu abre.

*   **Botão Trigger (Hambúrguer):**
    *   Posição: `fixed` no canto superior esquerdo (ou dentro do Header, se houver).
    *   Z-Index: Alto (51) para ficar acima de tudo.
    *   Aparência: Botão circular branco com sombra suave (`box-shadow`), consistente com o design "Toca Boca".

*   **Comportamento de Fechamento:**
    *   Ao clicar em *qualquer* link dentro da sidebar, ela deve fechar automaticamente (UX essencial para SPAs/âncoras).
    *   Ao clicar no Overlay, ela fecha.

### 4.2. Especificação da Engine de Blog (Detalhe)
Para o `build_dashboard.py` se tornar um orquestrador robusto:

*   **Tratamento de Erros (Defensive Programming):**
    *   Se um arquivo `.md` estiver mal formatado (ex: frontmatter inválido), o script **não** deve quebrar o site inteiro.
    *   **Fallback:** O artigo problemático será ignorado ou listado com título "Título Indisponível" e um aviso no log, permitindo que o resto do site funcione.

*   **Metadata Extraction:**
    *   Priorizar campos padrão: `title`, `nav_title`, `date`, `description`.
    *   Normalizar datas para garantir a ordem cronológica correta (Mais novo -> Mais antigo).

*   **Consistência Visual:**
    *   Os Cards do Blog usarão a **mesma** estrutura CSS dos Cards das Lições (`.card`), mas com uma classe modificadora (ex: `.card-blog`) se necessário para diferenciar sutilmente (ex: ícone de lápis em vez de guardião).

## 5. Simulação Mental e Análise de Risco (The "Antigravity" Simulation)

*Adicionado em 22/01/2026 às 14:10 - Revisão de Robustez e Otimização.*

Atendendo ao seu pedido, executei uma simulação mental completa do novo sistema operando em cenários reais e de estresse.

### 5.1. Simulação do Cenário de Erro (Debug)
**Cenário:** Você cria um blog post novo, mas esquece de fechar as aspas no título do YAML, ou usa um caractere inválido.
- **Antes (Sem tratamento):** O script `yaml.safe_load` lançaria uma *Exception*, o build pararia no meio, e o site ficaria incompleto (sem index).
- **Agora (Com o Novo Plano):**
    - O script entra no bloco `try/except` ao ler o arquivo.
    - Captura o erro específico (`yaml.scanner.ScannerError`).
    - **Ação do Sistema:**
        1.  Ignora apenas aquele arquivo "tóxico".
        2.  Imprime no terminal: `⚠️ [BLOG] Erro ao processar 'meu_post_errado.md': YAML Inválido na linha 3`.
        3.  Continua e gera o site com os outros 10 artigos saudáveis.
    - **Resultado:** O site nunca sai do ar por erro de conteúdo. O terminal te conta exatamente onde arrumar.

### 5.2. Simulação do Menu Mobile
**Cenário:** Usuário abre o site num iPhone (Safari) e clica no menu.
- **Risco:** O CSS `sidebar` sobrepor o conteúdo mas o fundo ficar clicável, confundindo o usuário.
- **Solução Implementada:** O elemento `overlay` (fundo escuro) não serve só para beleza; ele bloqueia toques no conteúdo abaixo.
- **Risco:** O menu ficar "preso" aberto se o JS falhar.
- **Mitigação:** Adicionar um CSS fallback onde, se o JS quebrar, o menu ainda pode ser acessado via âncora ou permanece visível levemente. (Mas o JS proposto é tão simples — 5 linhas — que a falha é improvável).

### 5.3. A Questão da Performance (1.200 Lições)
**Sua Pergunta:** "Faz sentido reconstruir tudo de novo toda vez?"
**Resposta:** Não. Hoje, com 20 lições, leva < 2 segundos. Com 1.200 lições, levará ~40-60 segundos. Isso mata a criatividade ("Feedback Loop" lento).

**A Solução de Otimização (Smart Build):**
Incluirei no script `build_lessons.py` uma verificação de **timestamp** (data de modificação):
1.  Antes de processar `licao_01.yaml`, o script verifica se existe `licao_01.html`.
2.  **A Pergunta de Ouro:** "O arquivo YAML é mais novo que o HTML?"
    - **Sim:** Reconstruir (Mudou algo).
    - **Não:** Pular (Cache).
3.  **Resultado da Simulação:** Com 1.200 lições, se você mudar apenas 1 vírgula em 1 lição, o build levará **0.5 segundos** (verificando datas rapidamente e processando apenas 1 arquivo), em vez de 1 minuto.

---
**Status Final do Plano:**
Pronto para execução. O código será escrito já com a "Smart Build" (build incremental) e o tratamento de erros robusto.
