# AUDITORIA: L001 vs L002 vs Template — Qual é o Modelo Correto?
**Data:** 15/01/2026 17:37 | **Tipo:** Auditoria Técnica

---

## COMPARAÇÃO ESTRUTURAL

### Root Level

| Aspecto | Template V5.1 | L001 | L002 |
|---------|---------------|------|------|
| Wrapper `licao:` | ✅ `licao:` L19 | ✅ `licao:` L7 | ❌ Flat |
| Metadados loc | `licao.metadados` | `licao.metadados` | Root level |

**Veredito:** L001 ✅ | L002 ❌

---

### Seção `metadados`

| Campo | Template | L001 | L002 |
|-------|----------|------|------|
| id | `MV-S-XXX` | ✅ `MV-S-001` | ✅ `MV-S-002` |
| titulo | ✅ | ✅ | ✅ |
| fase | ✅ | ✅ | ✅ |
| trimestre | ✅ | ✅ | ✅ |
| guardiao_lider | ✅ | ✅ | ✅ |
| guardiao_secundario | ✅ | ✅ | ✅ |
| tgtb_ref | ✅ | ✅ | ✅ |
| status | ✅ | ✅ | ✅ |
| **tipo** | ❌ não tem | ✅ "Senso Numérico" | ❌ |
| **versao** | ❌ não tem | ✅ "5.0" | ❌ |
| **guardioes_apresentados** | ❌ não tem | ✅ [Celeste, Melquior] | ❌ |

**Veredito:** L001 tem MAIS campos que o template (extras úteis)

---

### Seção `ideia_viva`

| Campo | Template | L001 | L002 |
|-------|----------|------|------|
| frase | ✅ | ✅ | ✅ |
| conceito | ✅ `conceito` | ⚠️ `conceito_matematico` | ✅ `conceito` |
| intencao_cm | ✅ | ✅ | ✅ |

**Veredito:** L002 segue template! L001 usa nome diferente (`conceito_matematico`)

---

### Seção `atmosfera`

| Campo | Template | L001 | L002 |
|-------|----------|------|------|
| clima | ✅ | ✅ | ✅ |
| clima_desc | ✅ `clima_desc` | ⚠️ `clima_descricao` | ✅ `clima_desc` |
| local | ✅ | ✅ | ✅ |
| local_desc | ✅ `local_desc` | ⚠️ `local_descricao` | ✅ `local_desc` |
| virtude | ✅ | ✅ | ✅ |
| artefato | ✅ | ✅ | ✅ |

**Veredito:** L002 segue template! L001 usa `_descricao` em vez de `_desc`

---

### Seção `linkage`

| Campo | Template | L001 | L002 |
|-------|----------|------|------|
| elo_anterior | ✅ inline | ⚠️ nested | ✅ inline |
| proximo | ✅ `proximo` | ⚠️ `proximo_passo` | ✅ `proximo` |

**Veredito:** L002 segue template! L001 usa nomes diferentes

---

### Seção `para_o_portador`

| Campo | Template | L001 | L002 |
|-------|----------|------|------|
| dica_coracao | ✅ | ✅ | ✅ |
| protocolo_impecabilidade | ✅ | ✅ | ❌ ausente |
| audio_script | ✅ | ✅ | ❌ ausente |
| filho_descobre | ✅ | ⚠️ `o_que_seu_filho_vai_descobrir` | ✅ |
| nota_graca | ✅ | ✅ | ✅ |
| conforto_emocional | ✅ | ✅ | ✅ |

**Veredito:** MISTO — L001 tem mais campos mas nomes diferentes

---

### Seção `jornada.concreto`

| Campo | Template | L001 | L002 |
|-------|----------|------|------|
| desc | ✅ | ✅ | ✅ |
| card_objeto | ✅ | ✅ | ✅ |
| instrucoes_portador | ✅ array | ✅ array | ⚠️ `passos` |
| tempo_minimo | ✅ | ✅ | ⚠️ `tempo` |
| adaptacao_bernardo | ✅ | ✅ | ✅ |

**Veredito:** L001 segue template! L002 usa `passos` em vez de `instrucoes_portador`

---

## RESUMO COMPARATIVO

### Conformidade com Template V5.1

| Seção | L001 | L002 | Melhor |
|-------|------|------|--------|
| Root wrapper | ✅ | ❌ | **L001** |
| metadados | ✅+ extras | ✅ | **L001** |
| ideia_viva | ⚠️ nome diff | ✅ | **L002** |
| atmosfera | ⚠️ nome diff | ✅ | **L002** |
| linkage | ⚠️ nome diff | ✅ | **L002** |
| para_o_portador | ✅+ extras | ⚠️ falta campos | **L001** |
| concreto | ✅ | ⚠️ passos | **L001** |

### Contagem Final

| Critério | L001 | L002 |
|----------|------|------|
| Segue nomes do template | 4/7 | 5/7 |
| Tem wrapper correto | ✅ | ❌ |
| Tem campos extras úteis | ✅ muitos | ❌ |
| É mais completo | ✅ 519 linhas | ❌ 117 linhas |

---

## DIAGNÓSTICO FINAL

### L001 (A Trindade na Palma)
**Prós:**
- Wrapper `licao:` correto
- Muito mais detalhado e completo
- Campos extras úteis (versão, tipo, guardioes_apresentados)
- Concreto usa `instrucoes_portador` corretamente

**Contras:**
- Alguns nomes de campos diferentes do template:
  - `conceito_matematico` vs `conceito`
  - `clima_descricao` vs `clima_desc`
  - `proximo_passo` vs `proximo`
  - `o_que_seu_filho_vai_descobrir` vs `filho_descobre`

### L002 (As Pedras da Fortaleza)
**Prós:**
- Nomes de campos SEGUEM o template
- Mais enxuto (YAML Lean)

**Contras:**
- SEM wrapper `licao:` (estrutura flat)
- Falta campos importantes (protocolo_impecabilidade, audio_script)
- Usa `passos` em vez de `instrucoes_portador`

---

## RECOMENDAÇÃO

### NENHUMA das duas é perfeita!

**Modelo ideal seria:**
1. Wrapper `licao:` de L001
2. Nomes de campos do Template/L002
3. Completude de L001
4. Concisão onde apropriado

### Ação Recomendada

**Criar um "Golden Template" atualizado** que combina o melhor:

1. **Atualizar template** para incluir campos extras úteis de L001:
   - `tipo`, `versao`, `guardioes_apresentados`
   
2. **Padronizar nomenclatura** (o template é o SSOT):
   - `conceito` não `conceito_matematico`
   - `clima_desc` não `clima_descricao`
   - `proximo` não `proximo_passo`
   
3. **Migrar ambos** para o formato padronizado

---

## MATRIZ DE DECISÃO

| Opção | Esforço | Risco | Benefício |
|-------|---------|-------|-----------|
| A: Usar L001 como modelo e adaptar nomes | 2h | Médio | Alto |
| B: Usar L002 como modelo e adicionar wrapper + campos | 3h | Alto | Médio |
| C: Atualizar template e migrar todos | 4h | Baixo | **Máximo** |

**Recomendação: Opção C** — Atualizar template PRIMEIRO, depois migrar.

---

**AGUARDA:** Decisão do Maestro

**Pergunta:** Qual abordagem prefere?
