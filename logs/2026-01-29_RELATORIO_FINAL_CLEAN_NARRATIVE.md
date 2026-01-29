# Relatório Mestre: Arquitetura "Clean Narrative" (North Star)
**Data:** 29/01/2026
**Autor:** Antigravity (Google DeepMind)
**Contexto:** Refatoração Visual e Semântica do Módulo Sementes (Lições 000-002)
**Status:** ✅ Concluído & Impecável

---

## 1. Visão Geral
Este relatório documenta a transformação arquitetural realizada na interface do projeto "Matemática Viva". O objetivo foi **eliminar a dívida técnica** acumulada (estilos inline, HTML não-semântico) e estabelecer um novo padrão visual **"Impecável"**, alinhado aos princípios de design de alto padrão (Premium Design).

A partir de agora, o código não apenas "funciona", mas é legível, escalável e fácil de manter.

---

## 2. A Nova Arquitetura "Clean Narrative"

### 2.1. Centralização e Tokens Visuais (`style.css`)
Abandonamos a prática de definir estilos visuais complexos diretamente nas tags HTML. Criamos "Tokens Visuais" (classes CSS) que encapsulam decisões de design.

**O que mudou no CSS:**
Adicionamos uma seção dedicada **"PHASE 6: COMPONENTES DE NARRATIVA"** no final do arquivo `site/sementes/style.css`.

#### Componentes Principais:
1.  **`.card-visual-asset` (O Card Mestre)**
    *   **Função:** Padronizar todas as imagens de Guardiões e Locais.
    *   **Propriedades Fixas:**
        *   `border: 4px solid white;` (Borda de "polaroid" ou carta física).
        *   `box-shadow: 0 4px 6px rgba(0,0,0,0.1);` (Sombra suave para profundidade).
        *   `border-radius: var(--radius-sm);` (Cantos arredondados consistentes).
    *   **Benefício:** Se quisermos mudar a borda de TODOS os cards para dourado, alteramos apenas 1 linha no CSS, em vez de centenas de arquivos.

2.  **Modificadores de Rotação (`.rotate-*`)**
    *   Para evitar a rigidez de um site corporativo, usamos rotações sutis para dar a sensação de "itens espalhados sobre uma mesa".
    *   `.rotate-left`: Inclina -2 graus.
    *   `.rotate-right`: Inclina +2 graus.
    *   `.hover-float`: **Micro-interação** que, ao passar o mouse, "levanta" o card (sombra aumenta) e o endireita (rotação 0), convidando ao clique/toque.

3.  **Grid de Navegação (`.lesson-nav-grid`)**
    *   Substituímos alinhamentos manuais (`float`, `text-align`) por **CSS Grid**.
    *   Garante que o botão "Anterior" fique na esquerda, o Logo no centro, e "Próxima" na direita, perfeitamente alinhados verticalmente.

---

## 3. Comparativo Técnico: Antes vs. Depois

Para ilustrar o impacto da limpeza, veja a comparação direta de código:

### Exemplo 1: Imagens dos Guardiões

❌ **Antes (Legacy Code):**
*Difícil de ler, repetitivo, propenso a erros visuais.*
```html
<div style="text-align:center; margin-top:2rem;">
    <p class="local-label">Visualizar</p>
    <img src="../assets/cards/guardioes/celeste-raposa.png"
         style="width:120px; border-radius:12px; box-shadow:0 4px 6px rgba(0,0,0,0.1); transform: rotate(-2deg); border: 4px solid white;"
         onError="..." alt="Card celeste">
</div>
```

✅ **Depois (Clean Narrative):**
*Semântico, limpo e conectado ao Design System.*
```html
<div style="text-align:center; margin-top:2rem;">
    <p class="local-label">Visualizar</p>
    <img src="../assets/cards/guardioes/celeste-raposa.png"
         class="card-visual-asset rotate-left hover-float"
         onError="..." alt="Card celeste">
</div>
```

### Exemplo 2: Cabeçalho de Navegação

❌ **Antes:**
*Divs genéricas com estilos inline de largura.*
```html
<div class="lesson-header-nav">
    <div style="width: 33%;">...</div>
    <div style="width: 33%; text-align: center;">...</div>
    <div style="width: 33%; text-align: right;">...</div>
</div>
```

✅ **Depois:**
*Tag HTML5 `<nav>` e controle total via CSS Class.*
```html
<nav class="lesson-nav-grid" aria-label="Navegação da Lição">
    <div class="nav-col prev">...</div>
    <div class="nav-col logo">...</div>
    <div class="nav-col next">...</div>
</nav>
```

---

## 4. Arquivos Impactados
A refatoração foi aplicada cirurgicamente nos seguintes arquivos:

1.  **CSS Global:**
    *   `site/sementes/style.css` (Adição das classes da Phase 6).
2.  **Lições (HTML):**
    *   `site/sementes/MV-S-000_O_PORTAL_DO_REINO.html`
    *   `site/sementes/MV-S-001_A_TRINDADE_NA_PALMA.html`
    *   `site/sementes/MV-S-002_AS_PEDRAS_DA_FORTALEZA.html`

## 5. Guia para o Futuro (Mantendo a Impecabilidade)

Ao criar novas lições (ex: `MV-S-003`), siga estas regras de ouro:

1.  **Nunca use `style="..."` em imagens importantes.** Use sempre `.card-visual-asset`.
2.  **Use `<nav>` e `<aside>`.** Estrutura semântica ajuda leitores de tela e organização do código.
3.  **Mantenha o padrão de listas.** Use as listas limpas dentro de `.materials-box` (sem margens manuais).
4.  **Copie o Padrão.** Use o arquivo `MV-S-001.html` como "template dourado" para copiar e colar estruturas.

---
*Relatório finalizado em 29/01/2026. Todas as tarefas da Phase 6 foram concluídas com sucesso.*
