# Log de Planejamento: Unificação Visual (CSS)
**Data:** 28/01/2026 - 20:07
**Contexto:** O projeto possui cerca de 25 lições. Atualmente, estilos críticos (layout, cards, fontes) estão duplicados dentro de cada arquivo HTML (`<style>`), causando inconsistências (ex: padding mobile) e dificuldade de manutenção.

## 1. A Estratégia: Centralizar é Simplificar
Você perguntou se existe um jeito mais simples.
*   **Manter como está (Inline):** É o caminho "fácil" agora, mas "infernal" depois. Teríamos que abrir 25 arquivos toda vez que quiséssemos ajustar uma margem.
*   **Centralizar (Style.css):** É o caminho "trabalhoso" por 1 hora, mas "eterno" depois. Ajustou no `style.css`, as 25 lições obedecem instantaneamente.

**Veredito:** Centralizar não é complicar. É **profissionalizar** para escalar.

## 2. O Que Vamos Unificar?
Analisei os arquivos `MV-S-000`, `001` e `002`. Estes são os candidatos para migração imediata:

### A. Estrutural (Layout)
*   `.lesson-container`: Padding e largura máxima.
*   `@media (mobile)`: Regras de responsividade críticas.

### B. Componentes Visuais
*   `.scene-card`: O cartão branco com sombra.
*   `.instruction-box` / `.materials-box`: Caixas coloridas de aviso.
*   `.bruner-box`, `.cm-box`, `.tgtb-box`: Caixas pedagógicas (já estão parcialmente no CSS, mas precisam de revisão).

### C. Personagens (Guardiões)
*   `.script-persona-block`: O bloco de fala.
*   `.script-avatar`: A bolinha da imagem.
*   `.portador-block`: **Atenção:** Precisa de regra especial (Flexbox) para manter ícone ao lado.

### D. Navegação
*   `.lesson-nav`: Botões de Anterior/Próximo.
*   `.lesson-header-nav`: O menu superior interno.

## 3. O Plano Tático (Task Robusta)
Para não "se perder" e não quebrar nada, faremos em **Círculos Concêntricos**:

3.  **Círculo 1 (Segurança): Backups**
    *   Criar cópia de segurança de `MV-S-000`, `001`, `002` (ex: `MV-S-000.bak`).
    *   Garantia de rollback imediato se algo der errado.

4.  **Círculo 2 (CSS Mestre em Camadas)**
    *   **Camada 1 (Tipografia):** Mover fontes e cores.
    *   **Camada 2 (Layout):** Mover containers principais.
    *   **Camada 3 (Componentes):** Unificar Cards, Caixas e Avatares.
    *   **Camada 4 (Mobile):** Aplicar a "Regra de Ouro" (padding 0.75rem).
    *   **Camada 5 (Correção):** Arrumar o Flexbox do Portador.

2.  **Círculo 2: O Piloto (Lição 000)**
    *   Remover `<style>` da Lição 000.
    *   Validar se quebrou algo.

3.  **Círculo 3: A Expansão (Lição 001 e 002)**
    *   Remover `<style>` das outras lições já criadas.
    *   Verificar se o layout se manteve.

4.  **Círculo 4: O Legado**
    *   Para as outras 22 lições futuras, o template já estará limpo, sem o bloco `<style>` problemático.

## 4. Detalhes Táticos (O Como)

### 4.1. Backup (Segurança Primeiro)
Antes de tocar em qualquer código:
*   `copy MV-S-000_O_PORTAL_DO_REINO.html MV-S-000_O_PORTAL_DO_REINO.html.bak`
*   `copy MV-S-001_A_TRINDADE_NA_PALMA.html MV-S-001_A_TRINDADE_NA_PALMA.html.bak`
*   `copy MV-S-002_AS_PEDRAS_DA_FORTALEZA.html MV-S-002_AS_PEDRAS_DA_FORTALEZA.html.bak`

### 4.2. O Novo CSS (Snippets Críticos - Responsivo)
Estes são os códigos exatos que entrarão no `style.css` para garantir fluidez total:

**A. Sistema de Breakpoints (Tríade):**
```css
/* 1. DESKTOP (Padrão > 1024px) */
/* Espaçoso, focado em leitura imersiva */
.lesson-container {
    max-width: 900px;
    padding: 4rem 2rem;
    margin: 0 auto;
}

/* 2. TABLET (768px - 1024px) */
/* Adaptação para telas médias, sem perder o ar "premium" */
@media (max-width: 1024px) {
    .main-content {
        padding: 2rem; /* Reduz de 4rem para 2rem */
    }
    
    .lesson-container {
        padding: 2rem 1rem;
    }
    
    .scene-card, .instruction-box {
        padding: 1.5rem; /* Intermediário */
    }
}

/* 3. MOBILE (< 768px) */
/* Edge-to-Edge, aproveitamento máximo */
@media (max-width: 768px) {
    .main-content {
        padding: 1rem 0.5rem;
    }

    .lesson-container {
        padding: 1rem 0; /* Zero lateral no container */
    }

    /* Otimização de Espaço */
    .script-persona-block,
    .instruction-box,
    .lesson-hero,
    .card-body,
    .scene-card {
        padding: 0.75rem !important; /* Mínimo absoluto (12px) */
    }
}
```

**B. Correção do Portador (Flexbox):**
```css
/* Correção do Ícone ao lado do Texto */
.portador-block .script-content {
    display: flex;
    flex-direction: column; /* Mobile first */
}

@media (min-width: 768px) {
    .portador-block .script-content {
        flex-direction: row;
        align-items: flex-start;
        gap: 1rem;
    }
    
    .portador-icon {
        font-size: 2rem;
        line-height: 1;
    }
}
```

### 4.3. Protocolo de Validação
Para considerar uma fase "Concluída", verificar:
1.  [ ] **Desktop:** O layout "Book View" (centralizado) se mantém?
2.  [ ] **Mobile:** As margens laterais vermelhas sumiram?
3.  [ ] **Card Portador:** O ícone de fogo/tocha está alinhado corretamente?
4.  [ ] **Navegação:** Os botões Anterior/Próximo funcionam e estão estilizados?

## 5. Plano de Rollback (Se der ruim)
Se após remover os estilos o layout quebrar:
1.  Restaurar o arquivo `.bak` imediatamente.
2.  Revisar o `style.css` procurando por erros de sintaxe ou especificidade.
3.  Não avançar para a próxima lição até resolver.

## 6. Próximos Passos
Aprovar este plano e iniciar pelo **Círculo 1 (Backups)**.

---

### 🔄 Log de Atualizações do Planejamento

#### [20:12] Refinamento: Mentalidade Responsiva (Não apenas Mobile)
**Discussão:** O usuário pontuou corretamente que não devemos pensar binário (Desktop vs Mobile), mas sim **Responsivo**. O layout deve se adaptar fluidamente.

**Ajuste na Estratégia:**
1.  **Tablet (768px - 1024px):** Hoje é uma "terra de ninguém". Vamos garantir que o padding seja intermediário (ex: `1.5rem`), não caindo direto de `4rem` para `0.75rem`.
2.  **Fluidez:** Em vez de apenas "esmagar" margens, vamos usar % ou `clamp()` onde possível futuramente. Por agora, definiremos **3 Breakpoints Claros** no CSS Unificado:
    *   **Desktop (> 1024px):** Espaçoso (`padding: 4rem`, `max-width: 900px`). Foco em leitura confortável (linha de 75 caracteres).
    *   **Tablet (768px - 1024px):** Híbrido (`padding: 2rem`).
    *   **Mobile (< 768px):** Imersivo (`padding: 0.75rem`). Foco em aproveitamento de tela.

### 🔄 Log de Atualizações do Planejamento

#### [20:17] Pesquisa: Unidades de Espaçamento (Rem vs % vs Clamp)
**Pergunta do Usuário:** "Não seria melhor usar Porcentagem (%)?"

**Veredito Técnico (Pesquisa):**
1.  **Porcentagem (%):** É útil para *largura* (grids), mas perigosa para *padding vertical* (pois 5% de padding-top é calculado sobre a LARGURA do pai, não a altura, gerando resultados estranhos).
2.  **REM (Recomendado pela Acessibilidade):** É a medida mais robusta para texto. Garante que se o usuário der "Zoom" no navegador, o espaçamento cresce junto.
3.  **Clamp() (O "Futuro"):** A técnica mais moderna é `padding: clamp(1rem, 5vw, 4rem)`. Ela escala fluidamente entre um mínimo e um máximo.

**Decisão para o Projeto:**
Manteremos os **Breakpoints Fixos (Tri-State)** com `rem` por agora por ser:
a) Mais previsível para manter.
b) "À prova de falhas" (simples de debugar).
c) Já resolve o problema do "vermelho" imediatamente.

*Futuramente, podemos refatorar para `clamp()` se quisermos uma fluidez matemática perfeita.*

## 7. Estratégia de Versionamento (Git)
Para fazer o commit "do jeito certo" (limpo e organizado), faremos em duas etapas:

1.  **Commit 1 (Planejamento):** Salvar APENAS a documentação e os planos.
    *   `logs/`
    *   `docs/`
    *   Mensagem: `docs: Strategic plan for CSS migration and Responsive Breakpoints`
    
2.  **Commit 2 (Snapshot):** Salvar o estado atual do código (Lições e CSS) como um "Ponto de Restauração" seguro antes da refatoração.
    *   `site/`
    *   Mensagem: `chore: Snapshot of code state before Modular CSS Refactor`

**Motivo:** Se precisarmos reverter o código, não perdemos o planejamento.

---

### 🔄 Log de Atualizações (Continuação)

#### [21:30] Bug Report: A "Casinha" Invasora
**Problema:** O ícone de Home (`.home-btn`) está com `position: fixed`, o que faz ele sobrepor o texto ou criar margens estranhas ("comendo coluna").
**Observação:** O menu "Hambúrguer" mobile não está visível/ativo atualmente, então a Casinha é a única navegação.
**Solução Referenciada:**
1.  **Desktop:** Manter `fixed`, mas aumentar o `padding-left` do container da lição para que o texto nunca encoste nela.
2.  **Mobile:** Transformar em `position: absolute` relativo ao topo da lição (não fixed), ou garantir que ele fique num canto que não tape o título.
3.  **Evitar Colisão:** Se ativarmos o hamburger no futuro, decidiremos quem fica. Por enquanto, **salvar a Casinha** de atrapalhar a leitura.

#### [21:36] Inconsistência Estrutural (Lição 00)
**Problema:** A `MV-S-000` usa um HTML de navegação (`.lesson-header-nav`) diferente do padrão das outras lições (`.lesson-nav` no rodapé).
**Ação Necessária:** Não basta apenas migrar o CSS. Será necessário **padronizar o HTML** da Lição 00, inserindo o bloco de rodapé padrão para garantir consistência visual e funcional com o restante do curso.

---
**Status Final (28/01):** Planejamento concluído e revisado. Repositório salvo e sincronizado. Pronto para execução imediata na próxima sessão.

