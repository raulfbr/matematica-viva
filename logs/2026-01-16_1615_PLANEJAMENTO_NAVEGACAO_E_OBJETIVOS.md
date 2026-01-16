# PLANEJAMENTO DETALHADO: Navegação Fluida & Objetivos Matemáticos

**Data:** 16/01/2026 16:15
**Objetivo:** Refinar a UX das Lições e do Index, corrigindo a navegação e trazendo clareza pedagógica (o que se aprende) sem perder a magia narrativa.
**Status:** 🚧 Planejamento (NÃO EXECUTAR)

---

## 1. O Problema da Navegação (Links Quebrados)

**Diagnóstico:**
Atualmente, o `forge.py` renderiza cada lição isoladamente (`render_lesson`). Ele não sabe quem é o "vizinho". Por isso, os links "Anterior" e "Próximo" no template estão mortos ou manuais.

**Solução Técnica (O Elo da Corrente):**
Precisamos de um **Passo de Pré-Processamento** no `SementesDriver`:
1.  **Scan:** Ler todas as lições válidas (L000, L001, L002...).
2.  **Sort:** Ordenar por ID (000, 001, 002).
3.  **Linkage:** Para cada lição na lista, injetar:
    *   `prev_licao`: {titulo: "...", url: "..."}
    *   `next_licao`: {titulo: "...", url: "..."}
4.  **Render:** Só então renderizar o HTML.

**Impacto Visual:**
*   **Topo da Lição:** Adicionar uma barra de navegação discreta (Setas) acima do título.
*   **Rodapé:** Manter os cards grandes de navegação, mas agora *funcionando*.

---

## 2. O Objetivo Matemático (TGTB -> Matemática Viva)

**O Desafio:**
O currículo é narrativo ("Trindade na Palma"), mas os pais precisam saber que isso ensina "Contagem até 3" ou "Geometria Básica".

**A Fonte (TGTB):**
Os arquivos brutos estão em `curriculo/_SISTEMA/_REFERENCIAS_TGTB_BRUTO`.

**A Estratégia de Dados:**
Não vamos parsear TXT bruto em tempo de build (frágil). Vamos trazer essa informação para o **YAML da Lição** (Single Source of Truth).
*   Novo Campo em `metadados`:
    ```yaml
    metadados:
      titulo: "A Trindade na Palma"
      objetivo_pedagogico: "Contagem 1-3 e Reconhecimento Visual" # Traduzido discretamente
      tgtb_ref: "Lesson 1: Numbers 1-3" # Referência oculta se precisar
    ```

**Exibição Discreta:**
1.  **No Index (Card):**
    *   Abaixo do Título Narrativo ("A Trindade..."), uma etiqueta pequena e elegante: *Foco: Contagem 1-3*.
    *   Isso ajuda o pai a escanear o progresso acadêmico.
2.  **Na Lição (Header):**
    *   Abaixo do título principal, um subtítulo em itálico ou uma "Tag" visual: *Aprendizado: Quantidade e Símbolo*.

---

## 3. Roteiro de Implementação (Passo a Passo)

### Fase A: Atualização dos Dados (Conteúdo)
Editar `L000`, `L001`, `L002` em `curriculo/01_SEMENTESV6/` para incluir o campo `objetivo_pedagogico`.

### Fase B: Inteligência de Navegação (Python)
Atualizar `build/fases/sementes.py`:
*   Criar lógica `calculate_navigation(lessons_list)`.
*   Passar `prev` e `next` para o template.

### Fase C: Refinamento dos Templates (Jinja2)
1.  **`licao.j2`**:
    *   Inserir Menu de Navegação no Topo (Flexbox: Esquerda <-> Direita).
    *   Inserir `metadados.objetivo_pedagogico` no Header.
    *   Corrigir Rodapé para usar as variáveis `prev/next` dinâmicas.
2.  **`index.j2`**:
    *   Adicionar o `objetivo_pedagogico` no Card da lição.

---

## 4. Resultado Esperado (Simulação)

*   **Usuário no Index:** Vê "A Trindade na Palma" e logo abaixo, pequeno: *"Matemática: Números 1 a 3"*. Sente segurança acadêmica.
*   **Usuário na Lição L001:**
    *   Lê a lição.
    *   No topo, vê "< L000" e "L002 >".
    *   Ao terminar, clica no card gigante "Próxima Aventura: As Pedras da Fortaleza".
    *   **O fluxo não para.**

**Aguardando autorização para executar.**
