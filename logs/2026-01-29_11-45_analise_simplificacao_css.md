# Arquitetura de Refatoração de Interface: "Beleza Redentora"
**Data:** 29/01/2026 11:55
**Status:** Planejamento Robusto (Aprovado pelo Maestro)
**Referência:** `LORE/north_star.yaml` (Princípios: Impecabilidade, Beleza Redentora, Soberania Intelectual)

## 1. Objetivo Estratégico
Elevar o código-fonte ao mesmo nível de excelência da narrativa pedagógica. O código não deve ser apenas funcional; deve refletir a **Ordem** e a **Beleza** que ensinamos.
*"Se não é excelente, não é nosso."* (Princípio Fundamental #1)

## 2. Diagnóstico Arquitetural
O código atual, embora funcional, apresenta "ruídos" visuais (estilos inline) que ferem o princípio da **Impecabilidade** e dificultam a manutenção da **Identidade Tribal** (consistência visual).

### Pontos de Fricção Identificados:
1.  **Inconsistência Semântica:** Elementos de navegação e estrutura repetidos como "div soup" genérica.
2.  **Acoplamento Visual:** Regras de apresentação (rotação de cards, bordas) "chumbadas" no HTML, impedindo a evolução fluida da estética "Beatrix Potter".
3.  **Ruído Cognitivo no Código:** O excesso de `style="..."` distrai o "Pai Engenheiro" (usuário mantenedor) da essência narrativa do conteúdo.

---

## 3. Plano de Ação: "Clean Narrative UI"

### FASE A: Otimização da Navegação (Ordem)
*   **Problema:** Blocos de navegação repetitivos (`width: 33%`) poluem o início de cada lição.
*   **Solução:** Implementar Grid Semântico de Navegação.
*   **Componente:** `.lesson-nav-grid`
    *   `.nav-col.prev` (Alinhamento esquerdo, flex-start)
    *   `.nav-col.logo` (Centro, opacidade controlada)
    *   `.nav-col.next` (Alinhamento direito, flex-end)
*   **Meta:** Reduzir o bloco de navegação de 20 linhas para 5 linhas semânticas.

### FASE B: Estética Tátil (Beleza)
*   **Problema:** A estética "Beatrix Potter" (cards levemente rotacionados, sombras orgânicas) está hardcoded em cada `<img>`.
*   **Solução:** Abstração em Classes de "Toque Humano" (Organic Classes).
*   **Novas Classes CSS:**
    *   `.card-visual-asset`: Define borda branca grossa, sombra suave e radius.
    *   `.rotate-left`: `transform: rotate(-2deg)`
    *   `.rotate-right`: `transform: rotate(2deg)`
    *   `.hover-float`: `transition` e `transform` para dar "vida" ao passar o mouse.
*   **Impacto:** Permite ajustar a "fisicalidade" de todos os cards do site simultaneamente.

### FASE C: Tipografia e Listas (Clareza)
*   **Problema:** Listas de materiais e instruções com margens manuais.
*   **Solução:** Contexto Tipográfico Isolado.
*   **Seletores CSS:**
    *   `.materials-box ul`: Margens e bullets estilizados automaticamente.
    *   `.instruction-box ol`: Numeração clara e espaçada.
    *   `.tone-emoji`: Classe para emojis que não devem ser itálicos (ex: 🤫), removendo `<span style="font-style:normal">`.

### FASE D: Semântica e Acessibilidade (Profundidade)
*   **Melhoria:** Elevar o nível semântico do HTML.
*   **Ação:**
    *   Substituir `<div class="lesson-header-nav">` por `<nav class="lesson-header-nav" aria-label="Navegação da Lição">`.
    *   Substituir `<div class="materials-box">` por `<aside class="materials-box" aria-label="Lista de Materiais">`.
*   **Ganho:** Código autodocumentado e acessível.

### FASE E: Design System (Consistência)
*   **Diretriz:** Todas as novas classes DEVEM usar as variáveis CSS existentes (`--radius-sm`, `--shadow-soft`, `--g-melquior`, etc.).
*   **Proibido:** "Magic numbers" (ex: `border-radius: 12px` manual). Usar sempre `var(--radius-sm)`.

---

## 4. Definição de Tarefa Técnica (Prompt para Execução)

**Tarefa:** Refatoração "Clean Narrative" das Lições 000-002.

1.  **CSS (style.css):**
    *   Criar seção `/* === COMPONENTES DE NARRATIVA === */`.
    *   Implementar `.lesson-nav-grid` e filhas.
    *   Implementar `.card-visual-asset` usando **Design Tokens**.
    *   Implementar resets de lista para `.materials-box` e `.instruction-box`.
    *   Criar utilitário `.no-italic`.

2.  **HTML (MV-S-000, 001, 002):**
    *   **Varredura Impecável:** Substituir estilos inline novos componentes.
    *   **Upgrade Semântico:** Aplicar tags `<nav>` e `<aside>`.
    *   **Validação:** Garantir "Zero CSS Inline".

## 5. Critérios de Aceite (Definition of Done)
*   [ ] O arquivo HTML deve parecer um "texto limpo", quase literário.
*   [ ] Nenhuma regra de cor, borda ou sombra deve existir no HTML.
*   [ ] A navegação deve ser responsiva e idêntica em todas as lições.
*   [ ] O código deve respeitar a "Soberania Intelectual" do mantenedor (fácil de ler e evoluir).

---
*Assinado: Agente Especialista em UX/UI (Foco: Educação Clássica & Design System)*
