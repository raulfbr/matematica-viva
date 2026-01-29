# Revisão e Planejamento: Migração CSS (Regressões e Ajustes)
**Data:** 29/01/2026 11:30
**Assunto:** Análise das regressões identificadas na migração das Lições 000, 001, 002 e plano de correção incremental.

## 1. Identificação dos Problemas (Gap Analysis)

### A. Navegação Superior Ausente
*   **Problema:** A navegação "Anterior / Próximo" (com o ícone Sementes no meio) foi removida das lições migradas, mas o usuário deseja mantê-la.
*   **Referência (Backup/MV-S-003):** Elemento `<div class="lesson-header-nav">` presente nas linhas 98-118 do arquivo não migrado.
*   **Ação Necessária:** Reintegrar este bloco HTML no topo das lições e garantir que a classe `.lesson-header-nav` exista no `style.css` (atualmente ela não existe, foi removida ou nunca criada).

### B. "Portador da Tocha" Desalinhado
*   **Problema:** O ícone (🔥) e o texto "Portador da Tocha" não estão na mesma linha (flexbox behavior).
*   **Diagnóstico:** A classe `.script-persona-block` tem `display: block` (linha 597 do style.css) para permitir "word wrap", mas isso quebrou a estrutura da linha do cabeçalho do portador. A classe `.portador-block` precisa de um tratamento específico para realinhar o ícone com o título.
*   **Ação Necessária:** Ajustar o CSS de `.portador-block .script-header` para `display: flex; align-items: center;`.

### C. Labels "Visualizar" e "Mostrar Card" Desalinhados
*   **Problema:** Textos auxiliares que deveriam estar centralizados estão alinhados à esquerda ou sem formatação.
*   **Ação Necessária:** Criar/Reforçar classes utilitárias `.text-center` ou garantir que `.local-label` tenha `text-align: center` e seja aplicado corretamente aos elementos `p` que antecedem imagens.

### D. Estilos de Título Perdidos (".scene-header")
*   **Problema:** Os títulos como "🎬 Ritual de Abertura" perderam o peso (bold), tamanho e ícone destacado.
*   **Diagnóstico:** A classe `.scene-header` no `style.css` (não localizada na última visualização ou incompleta) precisa corresponder ao estilo visual do inline original: `font-size: 1.35rem; display: flex; align-items: center; font-weight: 600;`.
*   **Ação Necessária:** Restaurar/Adicionar a regra completa `.scene-header` no `style.css`.

### E. Estilo de Card "Before" (Gradiente) Perdido
*   **Problema:** A barra colorida no topo dos cards (`.scene-card::before`) desapareceu.
*   **Diagnóstico:** O pseudo-elemento `::before` estava definido inline. Ele precisa ser portado para o CSS principal.
*   **Ação Necessária:** Adicionar `.scene-card::before` com o gradiente correto no `style.css`.

### F. Espaçamento Superior (Casinha "Apertada")
*   **Problema:** O botão "Home" (Casinha) está sobrepondo ou ficando muito próximo do início do texto/header.
*   **Sugestão do Usuário:** Adicionar "dois dedos" de espaço (aprox. 3rem - 4rem) no topo para empurrar o conteúdo para baixo.
*   **Ação Necessária:** Ajustar `padding-top` de `.lesson-container` (especialmente no Mobile) para garantir que o conteúdo não colida com o botão flutuante/absoluto.

### G. Restauração Visual dos Cards (Blocos Separados)
*   **Problema:** O visual de "blocos" independentes (fundo branco, sombra, bordas arredondadas) foi perdido ou achatado, parecendo tudo um texto corrido.
*   **Diagnóstico:** CONFIRMADO: A classe `.scene-card` NÃO existe no escopo global do `style.css`. Ela precisa ser definida com `background: #FFFFFF`, `border-radius: 12px`, `box-shadow`, etc., antes das media queries.
*   **Ação Necessária:** Criar a regra `.scene-card` no início do `style.css` (Seção de Componentes) e ajustar a media query mobile para não remover *todas* as bordas/margens se o usuário quiser separação.

### H. Padronização Inteligente de Labels (Visualizar / Mostrar Card)
*   **Problema:** Nem todos estão centralizados porque muitos usam estilos inline antigos (`<p style="...">`) que não possuem `text-align: center`, em vez da classe `.local-label`.
*   **Ação Necessária:** Substituir padrões de string inline por `<p class="local-label">` nos arquivos HTML (000, 001, 002). Isso garantirá que todos herdem a centralização do CSS.

---

## 2. Plano de Execução Incremental

Para não perder contexto e fazer com segurança:

### Fase 1: CSS "Cirúrgico" (Correção Visual Global)
Faremos alterações APENAS no `style.css` para consertar o que já está quebrado visualmente, sem mexer no HTML ainda.
1.  **Restaurar `.lesson-header-nav`**: Criar as classes necessárias para a navegação superior.
2.  **Fix `.scene-card` & `.scene-header`**: Adicionar o gradiente `::before` e restaurar a tipografia do cabeçalho.
3.  **Fix `.portador-block`**: Corrigir o alinhamento flex do cabeçalho.
4.  **Fix `.local-label`**: Garantir centralização.
5.  **Fix Spacing**: Aumentar `padding-top` do container.

### Fase 2: HTML "Reconstrução" (Inserção de Componentes)
Iterar arquivo por arquivo (000, 001, 002) para:
1.  Re-inserir o bloco de HTML da navegação superior (recuperado do backup/modelo 003).
2.  Verificar se as classes de label ("Visualizar") estão aplicadas corretamente.

---

## 3. Próximos Passos Sugeridos
1.  Aprovar este plano.
2.  Executar a **Fase 1** (CSS).
3.  Validar visualmente (se possível).
4.  Executar a **Fase 2** (HTML) passo a passo (000, depois 001, etc.).

Aguardando sua confirmação para iniciar a Fase 1.
