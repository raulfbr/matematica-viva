# REVISÃO LIÇÕES SEMENTES — QA Quíntupla Multi-Expert
**Data:** 15/01/2026 17:26 | **Modo:** REVISAO | **Escopo:** curriculo/01_SEMENTES
**Total Lições:** 17 arquivos | **Status:** EM_ANDAMENTO

---

## CONVOCATÓRIA

### Experts Revisores
| Check | Expert | Critério |
|-------|--------|----------|
| CM Check | Charlotte Mason | 20 Princípios OK? |
| CPA Check | Jerome Bruner | Ordem C→P→A? |
| Tempo Check | Charlotte Mason | ≤ 20min? |
| Guardião Check | JRR Tolkien | Frases canônicas OK? |
| Template Check | Engenharia | Seções obrigatórias? |

### Arquivos a Revisar
```
000_INICIO_FORJA.yaml       (26.1 KB)
000_O_PORTAL.yaml           (6.2 KB)
001_TRINDADE_PALMA.yaml     (20.2 KB) ← Lição referência
002_AS_PEDRAS_DA_FORTALEZA  (6.1 KB)
003_A_ESTRELA_DO_REINO      (6.0 KB)
004_O_RITMO_DO_CRIADOR      (6.2 KB)
005_PALAVRAS_DE_POSICAO     (5.9 KB)
006_PRATICA_DE_NUMEROS      (5.9 KB)
007_NUMEROS_6_E_7           (5.9 KB)
008_O_PAR_PERFEITO          (5.8 KB)
009_O_CELEIRO_DE_NOE        (5.9 KB)
010_A_FILA_DA_PROVIDENCIA   (5.9 KB)
011_A_PLENITUDE_DAS_MAOS    (6.1 KB)
012_O_SEGREDO_DO_FEIXE      (6.1 KB)
013_O_RIO_QUE_SE_UNE        (6.1 KB)
014_O_CELEIRO_QUE_CRESCE    (5.8 KB)
015_A_ESCADA_DE_LUZ         (5.9 KB)
```

---

## LIÇÃO REFERÊNCIA: L001_TRINDADE_PALMA

### Análise Estrutural

| Seção | Presente | Linhas |
|-------|----------|--------|
| metadados | ✅ | 9-19 |
| ideia_viva | ✅ | 21-28 |
| atmosfera | ✅ | 30-42 |
| linkage | ✅ | 44-54 |
| preparacao | ✅ | 56-71 |
| para_o_portador | ✅ | 73-106 |
| ritual_abertura | ✅ | 108-135 |
| jornada | ✅ | 137-306 |
| narracao | ✅ | 308-326 |
| ritual_fechamento | ✅ | 328-356 |
| catedra_pais | ✅ | 358-389 |
| sugestoes | ✅ | 391-430 |
| diario_portador | ✅ | 432-444 |
| auditoria_qa | ✅ | 446-498 |
| lore_extraido | ✅ | 504-518 |

### QA Quíntupla — L001

#### 1. CM Check (Charlotte Mason)
| Critério | Status | Evidência |
|----------|--------|-----------|
| Criança como pessoa? | ✅ | "Herdeiro" tratado com dignidade |
| Ideia Viva presente? | ✅ | "Três sementes de carvalho... promessas do Rei" |
| Narração incluída? | ✅ | Seção narracao L308-326 |
| Lição ≤ 20 min? | ✅ | "15-20 min" em preparacao |
| Hábito Atenção? | ✅ | Ritual de abertura com transição |
| 20 Princípios? | ✅ | P1, P9, P10, P18 evidentes |

**Posição CM:** ✅ APROVADA
> "Esta lição exemplifica o que significa tratar a criança como pessoa. O ritual, a narrativa, o tempo curto — tudo alinha com meus princípios."

#### 2. CPA Check (Jerome Bruner)
| Critério | Status | Evidência |
|----------|--------|-----------|
| Concreto ≥ 60%? | ✅ | "80%+ da lição (NORTE ABSOLUTO)" L246 |
| Pictórico apropriado? | ✅ | "vetado: true" em Sementes L261 |
| Abstrato mínimo? | ✅ | "≤20% reconhecimento visual" |
| Progressão C→P→A? | ✅ | Tocou → Traçou no ar → Nome |
| Enativo presente? | ✅ | "Traçar no ar = ENATIVO" L251 |

**Posição Bruner:** ✅ APROVADA
> "Progressão CPA impecável. O veto ao pictórico em Sementes é correto — 'Things before Signs'. O enativo (traçar no ar, pular) é bem aplicado."

#### 3. Tempo Check (Charlotte Mason)
| Critério | Status | Evidência |
|----------|--------|-----------|
| Tempo declarado | ✅ | "15-20 min" |
| Seções enxutas? | ✅ | Sem padding desnecessário |
| Extensão opcional? | ✅ | "Só continue se os olhos pedirem" L291 |

**Posição CM (Tempo):** ✅ APROVADA
> "Lição curta como deve ser. A extensão é opcional — sábio."

#### 4. Guardião Check (JRR Tolkien)
| Critério | Status | Evidência |
|----------|--------|-----------|
| Celeste apresentada? | ✅ | Guardião líder |
| Frase canônica? | ✅ | "Quer ver o que eu encontrei?" L511-512 |
| Tom consistente? | ✅ | Curiosa, animada |
| Local do LORE? | ✅ | "clareira_das_perguntas" |
| Clima correto? | ✅ | "ensolarado" |

**Posição Tolkien:** ✅ APROVADA
> "Consistência interna impecável. Celeste é a Raposa Curiosa — seu tom animado COMBINA. O local (Clareira das Perguntas) é apropriado para o tema de descoberta."

#### 5. Template Check (Engenharia)
| Critério | Status | Evidência |
|----------|--------|-----------|
| Todas seções? | ✅ | 15 seções presentes |
| YAML válido? | ✅ | Parseável |
| IDs corretos? | ✅ | MV-S-001 |
| Linkage L000→L002? | ✅ | elo_anterior/proximo_passo |
| auditoria_qa presente? | ✅ | L446-498 |

**Posição Engenharia:** ✅ APROVADA
> "Template 100% completo. Estrutura YAML impecável. Linkage funcional."

---

## RESUMO L001

| Check | Resultado |
|-------|-----------|
| CM Check | ✅ APROVADA |
| CPA Check | ✅ APROVADA |
| Tempo Check | ✅ APROVADA |
| Guardião Check | ✅ APROVADA |
| Template Check | ✅ APROVADA |

**Status L001:** ✅ **QA QUÍNTUPLA APROVADA**

---

## VERIFICAÇÃO RÁPIDA DEMAIS LIÇÕES

### Checklist por Tamanho

| Lição | Tamanho | Comparado L001 | Análise |
|-------|---------|----------------|---------|
| 000_INICIO_FORJA | 26.1 KB | +29% | ⚠️ MAIOR — verificar |
| 000_O_PORTAL | 6.2 KB | -69% | ⚠️ MENOR — verificar |
| 001_TRINDADE_PALMA | 20.2 KB | REFERÊNCIA | ✅ |
| 002-015 | ~6.0 KB | -70% | ⚠️ MUITO MENORES |

### Alerta de Padrão

> **ATENÇÃO:** L002-L015 têm ~6 KB cada, enquanto L001 tem 20.2 KB.
> 
> Possíveis razões:
> 1. L001 é "lição modelo" mais detalhada
> 2. L002-L015 podem estar incompletas
> 3. Estrutura diferente por design

---

## VERIFICAÇÃO L002 (Amostra)

### Análise Rápida

