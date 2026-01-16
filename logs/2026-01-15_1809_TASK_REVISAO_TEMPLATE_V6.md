# TASK: Template V6 — Revisão e Refinamento
**Data:** 15/01/2026 18:09 | **Status:** EM_ANDAMENTO

---

## VISÃO GERAL

### Objetivo
Revisar e refinar o Template V6 para máxima flexibilidade, integração com LORE, e preparo para produção IA.

### Tasks Identificadas

| # | Task | Prioridade | Status |
|---|------|------------|--------|
| 1 | **Revisão Template V6** — Flexibilidade e campos dinâmicos | P0 | 🔄 EM ANDAMENTO |
| 2 | **Mapeamento LORE** — Referências contextuais no template | P0 | ⏳ PENDENTE |
| 3 | **Decisão: Template por Ano ou Fase?** | P0 | ⏳ PENDENTE |
| 4 | **Integração curriculo_espiral.yaml** em PARA_FAMILIA | P1 | ⏳ PENDENTE |
| 5 | **Passos Concreto Dinâmicos** — Array aberto | P1 | ⏳ PENDENTE |
| 6 | **Validação Final Template V6.1** | P1 | ⏳ PENDENTE |

---

## TASK 1: REVISÃO TEMPLATE V6

### Questões Identificadas

#### Q1: Template por Ano ou Fase?
| Opção | Descrição | Prós | Contras |
|-------|-----------|------|---------|
| **Por Fase (Sementes, Raízes...)** | 1 template para todo o ciclo | Consistência, menos manutenção | Menos granular |
| **Por Ano** | 1 template por ano (K, 1º, 2º...) | Mais ajustado à idade | Mais templates para manter |
| **Híbrido** | Template base + regras por ano | Flexível | Mais complexo |

**Recomendação:** Por **FASE** (Sementes, Raízes, Lógica, Legado) com **variáveis de ano** nos metadados.

**Justificativa:**
- Sementes = K (1 ano)
- Raízes = 1º-5º ano (5 anos, mas estrutura similar)
- Lógica = 6º-8º ano (3 anos)
- Legado = 9º-12º ano (4 anos)

O template muda mais pela FASE (tom narrativo, CPA ratio) do que pelo ano específico.

---

#### Q2: Campos Estáticos vs Dinâmicos
| Campo Atual | Problema | Solução |
|-------------|----------|---------|
| `tipo: '[Senso Numérico|Operações...]'` | Hardcoded | → Ref `LORE/curriculo_espiral.yaml#conceitos` |
| `local: '[jardim_central|...]'` | Hardcoded | → Ref `LORE/locais.yaml` |
| `clima: '[ensolarado|...]'` | Hardcoded | → Ref `LORE/climas.yaml` |
| `guardiao_lider: '[celeste|...]'` | Hardcoded | → Ref `LORE/guardioes.yaml` |
| `virtude: '[curiosidade|...]'` | Hardcoded | → Ref (a definir) |

**Proposta:** Usar formato `$ref: LORE/arquivo.yaml#secao` para IA saber onde buscar.

---

#### Q3: Passos do Concreto
**Problema:** Template tem `passo: 1` e `passo: 2` fixos.
**Solução:** Array aberto com nota para IA.

```yaml
instrucoes_portador:
  # IA: Adicione quantos passos forem necessários (mínimo 2, máximo 6)
  - passo: 1
    acao: '[Descrição]'
    fala_sugerida: '[Fala]'
  # ... passos adicionais conforme necessário
```

---

### Q4: Integração LORE no Template

**11 arquivos LORE identificados:**

| Arquivo | Usado Quando | Seção Template |
|---------|--------------|----------------|
| `guardioes.yaml` | Escolher guardião | `metadados.guardiao_lider` |
| `locais.yaml` | Definir local | `ritual_abertura.local` |
| `climas.yaml` | Definir clima/tom | `ritual_abertura.clima` |
| `artefatos.yaml` | Objetos especiais | `para_portador.preparacao` |
| `evolucao_guardioes.yaml` | Tom por ciclo | `ritual_abertura.fala_guardiao.tom` |
| `viajante.yaml` | Título do viajante | `metadados` (Herdeiro em Sementes) |
| `padroes_narrativos.yaml` | Estrutura narrativa | `jornada.narrativa_principal` |
| `curriculo_espiral.yaml` | Conexão curricular | `para_familia.espiral` |
| `origem_guardioes.yaml` | Backstory guardião | Opcional, enriquece narrativa |
| `north_star.yaml` | Princípios gerais | `para_familia.principio_cm` |
| `index.yaml` | Índice do LORE | Meta-referência |

---

### Q5: curriculo_espiral.yaml em PARA_FAMILIA

**Como usar:**
```yaml
para_familia:
  espiral:
    conceito: 'Contagem'
    volta_atual: 'Sementes — Intuição numérica, correspondência 1-a-1'
    proxima_volta: 'Raízes — Operações com números maiores'
    nota: |
      Este conceito será revisitado em ciclos futuros com maior profundidade.
      Em Sementes, focamos no toque e no maravilhamento.
      Em Raízes, seu filho usará estes mesmos números para CONSTRUIR.
```

**Valor para famílias:** 
- Pai entende que o conceito volta
- Cria expectativa para próximos ciclos
- Justifica o "simples" de Sementes

---

## PERGUNTAS PARA O MAESTRO

1. **Template por Fase (Sementes, Raízes...) está OK?** Ou prefere por ano?

2. **Referências LORE:** Posso usar formato `$ref: LORE/arquivo.yaml` para IA?

3. **curriculo_espiral em PARA_FAMILIA:** A proposta de mostrar "volta atual" e "próxima volta" faz sentido?

4. **Virtudes:** Temos 7 virtudes hardcoded. Devem ir para um arquivo LORE?

---

## PRÓXIMOS PASSOS (Após Respostas)

- [ ] Atualizar Template V6 → V6.1 com referências LORE
- [ ] Abrir passos do concreto
- [ ] Adicionar seção espiral em PARA_FAMILIA
- [ ] Validar com experts
- [ ] Testar com L001

---

## RESPOSTAS DO MAESTRO (15/01/2026 18:15)

### Pergunta 1: Template por Fase
**Resposta:** ✅ Sim, por FASE.
**Adicional:** Deixar nota no template: "Sementes é base para Raízes, Raízes 1 evolui para Raízes 2..."

### Pergunta 2: Referências LORE
**Resposta:** Usar `engenharia.yaml` para decidir. Usar `LORE/index.yaml` se estiver impecável.
**Requisito:** GARANTIR que clima use clima, guardião use guardião, etc.

### Pergunta 3: Espiral em PARA_FAMILIA
**Resposta:** A ideia de evolução é do CPA/BRUNER. Referência está em `triade.yaml`.

### Pergunta 4: Virtudes
**Resposta:** "Me explique melhor"

---

## DECISÕES TÉCNICAS (Baseadas em Engenharia.yaml)

### Decisão 1: Referências LORE no Template

**Princípio SSOT (Eric Evans):**
> "Cada dado existe UM lugar apenas. Link don't duplicate."

**Abordagem aprovada:**
- NÃO listar valores hardcoded no template
- Usar comentário `# ref: LORE/arquivo.yaml` para indicar fonte
- IA consulta o arquivo referenciado para valores válidos

**Exemplo:**
```yaml
# BLOCO 5: RITUAL DE ABERTURA
ritual_abertura:
  local: # ref: LORE/locais.yaml — IA escolhe de 5 opções
  clima: # ref: LORE/climas.yaml — IA escolhe de 8 opções
  ...
```

### Decisão 2: Estrutura de Navegação (LORE/index.yaml)

O `index.yaml` já tem seção `navegacao.criar_licao`:
```yaml
navegacao:
  criar_licao:
    sempre: [guardioes.yaml, locais.yaml, padroes_narrativos.yaml]
    por_ciclo:
      sementes: [evolucao_guardioes.yaml#sementes, viajante.yaml#herdeiro]
```

**Template pode referenciar:** `# ref: LORE/index.yaml#navegacao.criar_licao.sempre`

### Decisão 3: CPA via triade.yaml

O `triade.yaml` já define CPA por ciclo:
```yaml
ciclos:
  sementes:
    cpa: {concreto: "80-100% (NORTE ABSOLUTO)", pictorico: VETADO, abstrato: "≤20%"}
```

**Template deve referenciar:** `# ref: .bmad/expansion-packs/matematica-viva/triade.yaml#ciclos.sementes.cpa`

---

## EXPLICAÇÃO: VIRTUDES

**Contexto:**
No template atual, temos:
```yaml
virtude: '[curiosidade|persistencia|atencao|paciencia|sabedoria|coragem|gratidao]'
```

**O que são:**
Cada lição tem uma VIRTUDE associada (alinhada com Charlotte Mason — formação de caráter).
- Lição com Celeste → curiosidade
- Lição com Bernardo → persistência
- Lição com Noé → paciência
- etc.

**Pergunta era:**
Devemos criar `LORE/virtudes.yaml` como SSOT dessas 7 virtudes?

**Recomendação:**
As virtudes já estão implícitas nos guardiões. Cada guardião TEM uma virtude principal.
Ver `LORE/guardioes.yaml` — provavelmente já tem essa informação.

Se não tiver, podemos:
1. Adicionar `virtude_principal` em `guardioes.yaml` (recomendado — coesão semântica)
2. OU criar arquivo separado `virtudes.yaml`

**Decisão:** Verificar `guardioes.yaml` antes de criar novo arquivo.

---

## PRÓXIMOS PASSOS

- [x] Respostas do Maestro recebidas
- [x] Decisões técnicas baseadas em engenharia.yaml
- [ ] Verificar `guardioes.yaml` para virtudes
- [ ] Atualizar Template V6 → V6.1 com referências LORE
- [ ] Abrir passos do concreto (array dinâmico)
- [ ] Adicionar seção espiral em PARA_FAMILIA (ref triade.yaml)
- [ ] Adicionar nota de evolução "Sementes → Raízes"
- [ ] Criar Template V6.1 final

---

**Status:** CONTINUA
