# PLANEJAMENTO REFINADO: Navegação & Objetivos (Engenharia V4)

**Data:** 16/01/2026 16:35
**Base:** `engenharia.yaml` (Clean Code & SSOT)
**Fonte da Verdade:** `curriculo/_SISTEMA/CURRICULOS_MESTRE/000_K_SEMENTES_CURRICULO_MESTRE.md`

---

## 1. O Diagnóstico Engenharia (Code Quality Review)

**Problema:** A navegação quebrada e a falta de objetivos no HTML violam o princípio **"Qualidade Não Negociável"**. O pai fica perdido na sequência e no propósito.

**Solução Arquitetural:**
Não vamos apenas "remendar". Vamos aplicar **Single Responsibility Principle (SRP)**:
1.  **NavigationService:** Uma classe dedicada apenas a calcular `prev` e `next` com base na ordem dos arquivos. O Driver apenas consome isso.
2.  **Enriquecimento de Metadados:** O Objetivo Matemático (TGTB) deve ser um dado de primeira classe no YAML da lição (`objetivo_pedagogico`), garantindo **SSOT** no nível do artefato.

---

## 2. A Fonte da Verdade (TGTB)

Verificamos o arquivo mestre e extraímos os mapeamentos exatos:

| Lição | Ref TGTB (Fonte: 000_K_SEMENTES_CURRICULO_MESTRE.md) | Objetivo para o Pai (Discreto) |
|:---|:---|:---|
| **L000** | *Litúrgica / Intro* | *Foco: Atmosfera & Boas-Vindas* |
| **L001** | *Numbers 1 to 3* | *Matemática: Números de 1 a 3* |
| **L002** | *Ten Frames* | *Matemática: Quadros de Dez* |

---

## 3. Roteiro de Execução Técnica (Refinado)

Adicionamos a **Fase 0** para garantir que novas lições já nasçam corretas.

### Fase 0: Padronização do Schema (Template V6)
Antes de tudo, o `_TEMPLATE_V6.yaml` precisa ser a referência oficial.
*   **Ação:** Atualizar `curriculo/01_SEMENTESV6/_TEMPLATE_V6.yaml`.
*   **Mudança:** Adicionar campo explícito sob `metadados`:
    ```yaml
    metadados:
      # ...
      objetivo_pedagogico: '[Discreto: O foco matemático da lição]'  <-- NOVO
      tgtb_ref: '[000-LXX - Tópico Original]'
    ```

### Fase A: Atualização de Conteúdo (YAMLs Existentes)
Atualizar L000, L001 e L002 para incluir este novo campo, copiando os dados da tabela TGTB acima.

### Fase B: Inteligência de Navegação (Python)
Refatorar `build/fases/sementes.py`:
*   Ler todas as lições em memória.
*   Ordenar por ID.
*   Calcular `prev` e `next` (vizinhos).
*   Injetar esses dados no contexto do Jinja2.

### Fase C: Refinamento dos Templates (Jinja2)
1.  **`licao.j2`**:
    *   **Header:** Exibir `< Navegação >` e `Objetivo: ...`.
    *   **Footer:** Usar link dinâmico para a Próxima Lição.
2.  **`index.j2`**:
    *   Exibir `objetivo_pedagogico` como uma etiqueta discreta no card.

---

## 4. Detalhamento da UX (Experience)

Como solicitado: **"Discreto e Navegável"**.

*   **Header da Lição:**
    *   *Visual:* Linha fina acima do título. Esquerda: "← Anterior". Direita: "Próxima →". Centro: Ícone do Ciclo.
    *   *Subtítulo:* Abaixo do Título Poético ("A Trindade..."), em cinza: *Foco Matemático: Números de 1 a 3*.

*   **Index Card:**
    *   Mantém a limpeza. Adiciona apenas uma linha de rodapé no card com ícone de etiqueta: `🏷️ Números 1-3`.

---

**Plano Aprovado e Refinado.**
Pronto para execução em etapas: (1) Template, (2) Conteúdo, (3) Código, (4) Template HTML.
