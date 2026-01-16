# LOG DELIBERAÇÃO: Bounded Contexts vs Advogado do Diabo
**Data:** 15/01/2026 15:01 | **Tema:** Como evitar viés de confirmação no sistema multi-agent

---

## TENSÃO IDENTIFICADA

**Problema:** Se definirmos bounded contexts rígidos, cada expert só fala do "seu quintal":
- Hormozi só opina em vendas
- CM só opina em pedagogia
- Lewis só opina em narrativa

**Risco:** Viés de confirmação — ninguém questiona ninguém. Echo chamber.

---

## PROPOSTA: Advogado do Diabo + Manifestação Aleatória

### Mecanismo 1: WILDCARD (Manifestação Aleatória)

```yaml
protocolo_wildcard:
  desc: "Em toda deliberação, 1 expert FORA do contexto pode se manifestar"
  gatilho: Automático aleatorio OU quando Orchestrator detecta consenso rapido demais
  exemplos:
    - {decisao: CPA licao, wildcard: Hormozi pergunta "Isso funciona em 5min?"}
    - {decisao: Oferta vendas, wildcard: CM pergunta "Isso respeita criança?"}
    - {decisao: Design visual, wildcard: Thiel pergunta "Isso é 10x ou incremental?"}
  beneficio: Forçar pensamento fora do contexto usual
```

### Mecanismo 2: ADVOCATUS DIABOLI (Expert Contrarian)

```yaml
advocatus_diaboli:
  desc: "Role temporário que QUALQUER expert pode assumir para questionar consenso"
  ativacao: Quando 3+ experts concordam rapidamente (possível groupthink)
  regras:
    - Deve buscar falhas na proposta aprovada
    - Não precisa acreditar no que diz — é role play
    - Objetivo é stress-test, não sabotagem
  candidatos_naturais:
    - {expert: peter_thiel, porque: "Contrarian thinker por natureza"}
    - {expert: ux_maes.priscila, porque: "A Prática corta enrolação"}
    - {expert: engenharia.qa, porque: "Shift-left testing"}
```

### Mecanismo 3: EXPERT EXTERNO (Voz de Fora)

```yaml
expert_externo:
  desc: "Persona temporária que representa perspectiva não coberta pelos 14"
  exemplos:
    - {persona: "Pai Cético", perspectiva: "Isso não é religioso demais? Funciona para agnósticos?"}
    - {persona: "Criança 8 anos", perspectiva: "Isso é chato? Vou querer brincar?"}
    - {persona: "Professor Escola", perspectiva: "Isso prepara para vestibular?"}
    - {persona: "Avó Tradicional", perspectiva: "Na minha época era diferente. Isso funciona?"}
  regra: Orchestrator pode invocar expert externo para testar robustez de decisão
```

---

## PROPOSTA CONSOLIDADA: Bounded Soft + Intrusion Protocol

```yaml
bounded_contexts:
  modo: SOFT  # Não rígido, permite intrusão
  
intrusion_protocol:
  wildcard:
    freq: 1 por deliberação
    tipo: Aleatorio ou on-demand
  advocatus_diaboli:
    gatilho: Consenso rápido (≤2 rodadas sem objeção)
    executor: Thiel ou QA ou Priscila
  expert_externo:
    quando: Decisões que afetam público não-tribal
    pool: [Pai Cético, Criança 8 anos, Professor Escola, Avó Tradicional]
    
principio: "Bounded contexts ORGANIZAM. Intrusion protocol QUESTIONA."
```

---

## PERGUNTAS PARA DECISÃO

1. **Frequência do Wildcard:** 1 por deliberação? Ou só quando consenso rápido?

2. **Quem é o Advocatus natural?** Thiel (contrarian), Priscila (prática), ou criar expert novo?

3. **Experts externos:** Pool fixo ou ad-hoc conforme tema?

4. **Risco de paralisia:** Muito questionamento trava decisão. Como balancear?

---

## VOZES DOS EXPERTS (Simulação)

### Charlotte Mason
> "Aprecio a ideia. Criança é pessoa — devemos sempre perguntar 'A criança aprovaria?' Adicionar 'Criança 8 anos' como expert externo é excelente."

### Peter Thiel
> "Sou naturalmente contrarian. Posso ser Advocatus, mas cuidado: contrarian real não é teatral. Melhor que o protocolo force QUALQUER expert a questionar do que delegar para 'o cara do não'."

### Alex Hormozi
> "Speed matters. Se cada decisão tem 3 mecanismos de questionamento, velocidade morre. Sugestão: Intrusion só para decisões irreversíveis. Quick wins seguem sem burocracia."

### CS Lewis
> "Verdade emerge do debate. Mas debate falso é pior que consenso real. O Advocatus deve realmente questionar, não fingir. Teatralidade é condescendência."

### Engenharia (Eric Evans)
> "Bounded contexts existem para CLAREZA, não para SILÊNCIO. O intrusion protocol é elegante — mantém separação mas permite cross-pollination. Implementar como soft boundary, não hard."

---

## SÍNTESE PROPOSTA

```yaml
# Adicionar ao orchestrator.yaml

anti_vies:
  principio: "Bounded contexts ORGANIZAM. Intrusion protocol DESAFIA."
  
  bounded_soft:
    desc: "Experts têm domínios primários mas podem opinar fora"
    primarios:
      pedagogia: [charlotte_mason, susan_macaulay, jerome_bruner, lev_vygotsky]
      narrativa: [cs_lewis, jrr_tolkien, beatrix_potter, makoto_fujimura]
      negocios: [seth_godin, alex_hormozi, peter_thiel]
      ux: [ux_maes, design]
      tecnico: [engenharia]
    regra: "Expert DEVE opinar no primário. PODE opinar fora com justificativa."
  
  intrusion:
    wildcard:
      desc: "1 expert fora do contexto se manifesta"
      freq: decisoes_irreversiveis
      seleção: aleatorio ou on_demand
    advocatus:
      gatilho: consenso_rapido ≤2 rodadas
      executor: rotativo (não fixo para evitar role)
    externo:
      pool: [Pai Cético, Criança 8 Anos, Professor Escola, Avó Tradicional]
      quando: decisao_afeta_nao_tribal
  
  protecao_velocidade:
    quick_decisions: "Sem intrusion. CM decide direto."
    medium_decisions: "Wildcard opcional."
    strategic_decisions: "Full protocol (wildcard + advocatus + externo)."
```

---

## DECISÃO PENDENTE

O que você acha desta estrutura? Pontos a discutir:

1. ✅ ou ❌ **Bounded Soft** (domínio primário mas pode sair)?
2. ✅ ou ❌ **Wildcard** como manifestação aleatória?
3. ✅ ou ❌ **Advocatus Diaboli** para consenso rápido?
4. ✅ ou ❌ **Experts Externos** (Pai Cético, Criança 8 anos)?
5. ✅ ou ❌ **Proteção de velocidade** (quick decisions sem burocracia)?

---

## REVISÃO CRÍTICA (15:05) — Questionando a Síntese

### Objeção do Maestro (Raul)
> "A síntese está complexa demais. Bounded Soft + Wildcard + Advocatus + Externo + Proteção Velocidade = 5 mecanismos. O viés aparece justamente nas decisões 'simples' que ninguém questiona. Quero algo mais direto: **SEMPRE alguém de fora, independente da complexidade.**"

### Contra-argumento Analisado

O Maestro tem razão. Vamos examinar onde o viés realmente aparece:

| Tipo Decisão | Risco de Viés | Proposta Anterior | Problema |
|--------------|---------------|-------------------|----------|
| Quick | **ALTO** | Sem intrusion | Exatamente onde viés passa despercebido |
| Medium | Médio | Wildcard opcional | "Opcional" vira "nunca" na prática |
| Strategic | Baixo | Full protocol | Excesso burocrático |

**Insight:** O viés é mais perigoso em decisões rápidas porque ninguém para para questionar. "É óbvio" é a frase mais perigosa em sistema multi-agent.

---

## PROPOSTA SIMPLIFICADA v2: "Always One Outside"

### Princípio Único
> **Em TODA deliberação, por mais simples que seja, SEMPRE há 1 voz de fora do contexto primário.**

### Implementação Mínima

```yaml
anti_vies:
  principio: "Always One Outside — Toda decisão tem 1 voz não-óbvia"
  
  mecanismo_unico:
    nome: OUTSIDE_VOICE
    regra: "Antes de fechar qualquer decisão, 1 expert de FORA do contexto primário deve se manifestar"
    seleção: Aleatorio se não especificado
    manifesta: "Mesmo que concorde, deve EXPLICAR por que concorda de sua perspectiva"
    
  exemplos:
    - {decisao: "Ordem CPA lição", contexto: pedagogia, outside: seth_godin, pergunta: "Isso engaja ou entedia?"}
    - {decisao: "Tom narrativa", contexto: narrativa, outside: ux_maes.priscila, pergunta: "Mãe 7h manhã entende?"}
    - {decisao: "Cor botão", contexto: design, outside: jerome_bruner, pergunta: "Apoia progressão C→P→A?"}
    - {decisao: "Preço oferta", contexto: negocios, outside: cs_lewis, pergunta: "Linguagem é nobre?"}
    
  anti_echo_chamber:
    regra: "Outside voice NÃO pode ser do mesmo conselho que decidiu"
    rotação: "Não pode ser o mesmo outside 2x seguidas"
```

### Por Que Funciona

1. **Simplicidade:** 1 mecanismo, não 5
2. **Sempre ativo:** Não depende de "gravidade" da decisão
3. **Baixo custo:** 1 pergunta, não tribunal completo
4. **Anti-viés real:** Força perspectiva diferente mesmo em "casos óbvios"

---

## VOZES DOS EXPERTS — Round 2

### Charlotte Mason (questionando a si mesma)
> "Se eu decidir sozinha que lição está boa, quem me questiona? Preciso de outside voice também. Talvez Hormozi pergunte 'Mãe vai conseguir aplicar?' — isso me força a pensar praticidade, não só filosofia."

### Peter Thiel (aprovando)
> "Simples é melhor. Contrarian por default, não por exception. Um outside voice sempre presente é mais honesto do que 'advocatus teatral' só quando parece importante."

### Alex Hormozi (preocupação válida)
> "Concordo com simplificação. Mas precisa ser RÁPIDO. 1 pergunta, não 10. Se outside voice vira interrogatório, mata velocidade. Sugestão: outside faz 1 PERGUNTA, não discurso."

### Engenharia (implementação)
> "Implementável. Sugestão técnica: outside_voice como campo obrigatório no output de toda deliberação. Se vazio, Orchestrator recusa fechar decisão."

---

## QUESTÕES RESTANTES PARA DISCUSSÃO

### 1. Pool do Outside Voice
**Opção A:** Qualquer expert de fora do contexto
**Opção B:** Pool específico de "questionadores naturais" (Thiel, Priscila, QA)
**Opção C:** Incluir experts externos (Pai Cético, Criança 8 anos)

**Sua preferência?**

### 2. Formato da Manifestação
**Opção A:** 1 pergunta apenas (rápido)
**Opção B:** 1 pergunta + 1 observação (médio)
**Opção C:** Posição completa (lento mas profundo)

**Sua preferência?**

### 3. E se Outside Voice Concordar?
**Opção A:** Deve explicar POR QUE concorda (força reflexão)
**Opção B:** Pode só dizer "Aprovo" (rápido)
**Opção C:** Se concordar, puxar OUTRO outside (até ter discordância)

**Sua preferência?**

### 4. Experts Externos (Pai Cético, Criança 8 anos)
**Opção A:** Incluir no pool de outside
**Opção B:** Só para decisões que afetam público geral
**Opção C:** Criar como experts permanentes (não ad-hoc)

**Sua preferência?**

---

## PRÓXIMO PASSO

Responda as 4 questões acima e implemento no `orchestrator.yaml` a versão final simplificada.

Ou se quiser explorar mais algum ponto, continue a discussão aqui.

---

## DECISÕES DO MAESTRO (15:28)

### Respostas às 4 Questões

| # | Pergunta | Decisão | Justificativa Maestro |
|---|----------|---------|----------------------|
| 1 | Pool Outside Voice | **Qualquer um + Externos** | "Se for sempre o mesmo, serão sempre os mesmos questionamentos" |
| 2 | Formato Manifestação | **Completo** | "A ideia é quebrar o viés MESMO" |
| 3 | Se Concordar | **Deve explicar POR QUE** | Força reflexão genuína |
| 4 | Experts Externos | **Pool Dinâmico Proporcional** | Algoritmo que cria novos conforme necessidade |

---

## ALGORITMO: Pool Dinâmico Proporcional

### Conceito
> "Quanto menor o pool de externos, maior a chance de criar um novo. Quanto maior, menor a chance — mas SEMPRE existe chance de criar."

### Fórmula Proposta

```yaml
pool_dinamico:
  descricao: "Probabilidade inversamente proporcional ao tamanho do pool"
  
  formula:
    # P = probabilidade de criar novo externo
    # N = número atual de externos no pool
    # K = constante de decaimento (sugestão: 0.5)
    
    P = 1 / (1 + K * N)
    
  exemplos:
    - {N: 0, P: "100%", explicacao: "Pool vazio → SEMPRE cria"}
    - {N: 1, P: "67%", explicacao: "1 externo → 2/3 chance criar"}
    - {N: 2, P: "50%", explicacao: "2 externos → 1/2 chance criar"}
    - {N: 3, P: "40%", explicacao: "3 externos → 2/5 chance criar"}
    - {N: 5, P: "29%", explicacao: "5 externos → ~1/3 chance criar"}
    - {N: 10, P: "17%", explicacao: "10 externos → ~1/6 chance criar"}
    - {N: ∞, P: "→0%", explicacao: "Nunca zero, sempre alguma chance"}

  comportamento:
    - "Decai LENTAMENTE (não linear)"
    - "NUNCA chega a zero"
    - "Garante diversidade inicial"
    - "Permite renovação perpétua"
```

### Visualização do Decaimento

```
Chance de Criar Novo (%)
100 |█
 80 |██
 67 |███    ← Pool com 1
 50 |████   ← Pool com 2
 40 |█████  ← Pool com 3
 29 |██████ ← Pool com 5
 17 |██████████ ← Pool com 10
    +---------------------------
      0  1  2  3  5  10   N (externos)
```

---

## QUESTÕES PARA REFINAR O ALGORITMO

### 1. Constante K (Velocidade de Decaimento)

**Opção A:** K = 0.3 (decai LENTO)
- 5 externos ainda dá 50% chance
- Favorece MUITA diversidade

**Opção B:** K = 0.5 (decai MÉDIO) ← Sugestão
- 5 externos dá ~30% chance
- Balanceado

**Opção C:** K = 1.0 (decai RÁPIDO)
- 5 externos dá ~17% chance
- Estabiliza pool mais rápido

**Sua preferência?**

---

### 2. Quando Criar vs Quando Selecionar do Pool?

O algoritmo roda ANTES de escolher outside voice:

```yaml
fluxo_outside_voice:
  1_calcular_P: "P = 1 / (1 + K * N)"
  2_sortear: "random() < P ?"
  3_se_sim: "CRIAR novo expert externo ad-hoc"
  4_se_nao: "SELECIONAR aleatório do pool existente (internos + externos)"
  5_manifestar: "Outside voice faz posição COMPLETA"
```

**Isso faz sentido?**

---

### 3. Como Criar Expert Externo Ad-Hoc?

Quando o algoritmo decide CRIAR, de onde vem a persona?

**Opção A:** Pool Semente Fixo
```yaml
pool_semente:
  - Pai Cético
  - Mãe Secular
  - Criança 8 anos
  - Professor Escola Tradicional
  - Avó Tradicional
  - Pai Tech/Gamer
  - Mãe Workaholic
  - Adolescente Entediado
```
→ Sorteia deste pool, depois adiciona ao pool principal

**Opção B:** Geração Contextual
→ Orchestrator analisa a DECISÃO e gera persona relevante
→ Ex: Decisão sobre preço? Gera "Pai Classe C Preocupado com Valor"

**Opção C:** Híbrido
→ 70% pool semente, 30% geração contextual

**Sua preferência?**

---

### 4. Separação: Internos vs Externos no Pool?

**Opção A:** Pool Único
→ Todos (14 experts + externos criados) competem igual
→ Problema: Externos podem dominar com o tempo

**Opção B:** Pools Separados com Proporção
```yaml
selecao:
  chance_interno: 60%  # Sempre maioria interna
  chance_externo: 40%  # Externos trazem frescor
```

**Opção C:** Proporcional ao Tamanho
```yaml
selecao:
  # Se 14 internos e 3 externos:
  chance_interno: 14/17 = 82%
  chance_externo: 3/17 = 18%
```

**Sua preferência?**

---

## VOZES DOS EXPERTS — Round 3 (Algoritmo)

### Peter Thiel
> "Gosto do decaimento assintótico. Nunca zero = sempre possibilidade de surpresa. Isso é anti-frágil."

### Alex Hormozi
> "Complexidade mata execução. O algoritmo é elegante MAS precisa ser automático. Se exigir decisão humana cada vez, morre. Implementar hardcoded no Orchestrator."

### Charlotte Mason
> "Pool semente com 'Criança 8 anos' é essencial. Ela é o CLIENTE REAL. Não pode ser raro — deve ter peso maior ou garantia mínima de aparecer."

### Engenharia (Eric Evans)
> "Tecnicamente viável. Sugestão: persistir pool em YAML. Externos criados vão para `experts/externos/`. Tratados como experts reais, não ad-hoc descartáveis."

---

## DECISÕES PENDENTES

Responda as 4 questões acima para eu consolidar a proposta final:

1. **Constante K:** A (lento), B (médio), ou C (rápido)?
2. **Fluxo:** O algoritmo proposto faz sentido?
3. **Criação Externa:** A (pool semente), B (contextual), ou C (híbrido)?
4. **Separação Pools:** A (único), B (proporção fixa), ou C (proporcional tamanho)?

---

## PARECER DA ENGENHARIA (15:55)

> **Referência:** `engenharia.yaml` — Eric Evans (DDD), BMAD Framework, Clean Code, QA

### Decisões Maestro Recebidas
- K = 0.5 (médio) ✅
- Fluxo: confirmar com Engenharia
- Criação Externa: decisão Engenharia
- Separação Pools: decisão Engenharia

---

### ANÁLISE: Princípios Aplicados

#### Eric Evans (DDD) — Bounded Contexts + SSOT

| Princípio | Aplicação ao Anti-Viés |
|-----------|------------------------|
| **SSOT** | Externos criados DEVEM ir para `experts/externos/` como YAML persistente. NÃO são ad-hoc descartáveis. Senão violamos SSOT. |
| **Bounded Contexts** | Externos são contexto separado dos 14 internos. Fronteira clara: internos=domínio, externos=perspectiva-fora. |
| **Context Mapping** | Documentar como externo é selecionado e como interage com decisão. Logs explícitos. |

**Decisão DDD:** 
- ✅ Externos como YAML persistente em `experts/externos/`
- ✅ Pools separados (bounded contexts)
- ✅ Proporção deve ser documentada (context mapping)

---

#### BMAD Framework — Agent as Code + Federated Knowledge

| Princípio | Aplicação |
|-----------|-----------|
| **Agent as Code** | Externo criado = arquivo YAML em `experts/externos/nome.yaml`. Versionado Git. Tratado como expert real. |
| **Federated Knowledge** | Pool de externos = arquivo SSOT `experts/externos/_pool.yaml` com lista de todos criados. |
| **YAML Lean** | Externos seguem mesmo formato lean dos internos. Sem separadores visuais. |

**Decisão BMAD:**
- ✅ Cada externo = 1 arquivo YAML autônomo
- ✅ `_pool.yaml` = índice centralizado
- ✅ Formato idêntico aos internos (compatibilidade)

---

#### Clean Code — DRY + Single Responsibility

| Princípio | Aplicação |
|-----------|-----------|
| **DRY** | Algoritmo de seleção em UM lugar: `orchestrator.yaml` seção `anti_vies`. |
| **Funções Fazem UMA Coisa** | `selecionar_outside()` só seleciona. `criar_externo()` só cria. Separação clara. |
| **Código para Humanos** | Fórmula P = 1/(1+K*N) documentada com exemplos práticos. |

---

#### QA — Shift-Left + Verificação

| Princípio | Aplicação |
|-----------|-----------|
| **Shift-Left** | Antes de invocar outside, verificar se pool está em estado válido. |
| **AI Eficiência YAML** | External pool legível direto por IA sem parser customizado. |

---

### DECISÕES FINAIS ENGENHARIA

#### Questão 2: Fluxo — ✅ APROVADO com Ajuste

Fluxo original está correto, mas adicionar passo de persistência:

```yaml
fluxo_outside_voice:
  1_calcular_P: "P = 1 / (1 + 0.5 * N)"
  2_sortear: "random() < P ?"
  3a_se_sim_criar: 
    - "CRIAR novo expert externo"
    - "PERSISTIR em experts/externos/{nome}.yaml"  # DDD: não descartável
    - "ATUALIZAR experts/externos/_pool.yaml"  # BMAD: federated knowledge
  3b_se_nao_selecionar: "SELECIONAR aleatório do pool existente"
  4_manifestar: "Outside voice faz posição COMPLETA"
  5_logar: "Registrar decisão em log deliberação"  # QA: transparência
```

---

#### Questão 3: Criação Externa — **OPÇÃO C (Híbrido)** com Proporção 60/40

**Justificativa DDD:**
- Pool Semente (60%) = Bounded Context conhecido, personas validadas
- Geração Contextual (40%) = Flexibilidade para casos não cobertos

**Pool Semente Inicial (10 personas validadas):**

```yaml
pool_semente:
  personas:
    - {id: pai_cetico, nome: Pai Cético, perspectiva: "Isso não é religioso demais?", foco: [secular, universal]}
    - {id: mae_secular, nome: Mãe Secular, perspectiva: "Funciona sem cosmovisão específica?", foco: [neutro, prático]}
    - {id: crianca_8_anos, nome: Criança 8 Anos, perspectiva: "Isso é chato ou divertido?", foco: [engajamento, clareza]}
    - {id: professor_tradicional, nome: Professor Escola, perspectiva: "Prepara para vestibular?", foco: [resultados, métrica]}
    - {id: avo_tradicional, nome: Avó Tradicional, perspectiva: "Na minha época era diferente...", foco: [tradição, segurança]}
    - {id: pai_tech, nome: Pai Tech/Gamer, perspectiva: "Cadê a gamificação?", foco: [tecnologia, dopamina]}
    - {id: mae_workaholic, nome: Mãe Workaholic, perspectiva: "Tenho só 5min. Funciona?", foco: [tempo, eficiência]}
    - {id: adolescente_entediado, nome: Adolescente Entediado, perspectiva: "Isso é coisa de criancinha?", foco: [coolness, relevância]}
    - {id: pai_classe_c, nome: Pai Classe C, perspectiva: "Vale o investimento?", foco: [valor, custo-benefício]}
    - {id: mae_ansiosa, nome: Mãe Ansiosa, perspectiva: "E se meu filho ficar para trás?", foco: [comparação, validação]}
```

**Geração Contextual (40%):**
```yaml
geracao_contextual:
  gatilho: "Quando pool semente não cobre perspectiva necessária"
  prompt_template: |
    Decisão: {decisao}
    Contexto: {contexto}
    Gere persona externa que questione de ângulo não coberto pelos existentes.
    Formato: {nome, perspectiva, foco[]}
  persistir: true  # Sempre salvar em experts/externos/
```

---

#### Questão 4: Separação Pools — **OPÇÃO C (Proporcional ao Tamanho)**

**Justificativa Clean Code (DRY):**
Uma fórmula elegante que escala automaticamente:

```yaml
selecao_pool:
  formula: "chance_externo = N_externos / (N_internos + N_externos)"
  
  exemplos:
    - {internos: 14, externos: 0, chance_externo: "0%", nota: "Sem externos → 100% interno"}
    - {internos: 14, externos: 3, chance_externo: "18%", nota: "3 externos → ~1/5 externo"}
    - {internos: 14, externos: 7, chance_externo: "33%", nota: "7 externos → 1/3 externo"}
    - {internos: 14, externos: 14, chance_externo: "50%", nota: "Equilíbrio 50/50"}
  
  cap: 
    max_externo: 50%  # Nunca mais de 50% externos (internos sempre maioria)
    
  ajuste_crianca_8_anos:
    boost: "+10%"
    justificativa: "CM: Ela é o CLIENTE REAL. Garantia mínima de aparecer."
```

---

### ARQUITETURA PROPOSTA

```
.bmad/experts/
├── pedagogia/
│   └── pedagogia.yaml
├── narrativa/
│   └── narrativa.yaml
├── negocios/
│   └── negocios.yaml
├── [...]
└── externos/              # NOVO: Bounded Context Externos
    ├── _pool.yaml         # Índice SSOT de todos externos
    ├── pai_cetico.yaml    # Persona persistente
    ├── crianca_8_anos.yaml
    └── [criados dinamicamente]
```

---

### RESUMO DECISÕES ENGENHARIA

| Questão | Decisão | Princípio |
|---------|---------|-----------|
| **K** | 0.5 (médio) | Maestro |
| **Fluxo** | ✅ Aprovado + Persistência | DDD SSOT |
| **Criação** | Híbrido 60/40 | Bounded Contexts |
| **Pools** | Proporcional + cap 50% + boost Criança | Clean Code DRY |

---

## PRÓXIMO PASSO

Criar implementation_plan.md detalhado com todas as mudanças necessárias:

1. Criar diretório `experts/externos/`
2. Criar `_pool.yaml` com pool semente
3. Criar 10 arquivos YAML de personas
4. Atualizar `orchestrator.yaml` com seção `anti_vies`
5. Documentar algoritmo completo

Aguardando confirmação para gerar plano detalhado.

---

## ✅ STATUS: IMPLEMENTADO (15:58)

### Arquivos Criados

| Arquivo | Status |
|---------|--------|
| `experts/externos/_pool.yaml` | ✅ Criado (índice SSOT) |
| `experts/externos/pai_cetico.yaml` | ✅ Criado |
| `experts/externos/mae_secular.yaml` | ✅ Criado |
| `experts/externos/crianca_8_anos.yaml` | ✅ Criado (com boost +10%) |
| `experts/externos/professor_tradicional.yaml` | ✅ Criado |
| `experts/externos/avo_tradicional.yaml` | ✅ Criado |
| `experts/externos/pai_tech.yaml` | ✅ Criado |
| `experts/externos/mae_workaholic.yaml` | ✅ Criado |
| `experts/externos/adolescente_entediado.yaml` | ✅ Criado |
| `experts/externos/pai_classe_c.yaml` | ✅ Criado |
| `experts/externos/mae_ansiosa.yaml` | ✅ Criado |

### Orchestrator Atualizado

- ✅ Seção `anti_vies` adicionada ao `orchestrator.yaml`
- ✅ Algoritmo K=0.5 documentado
- ✅ Fluxo completo especificado
- ✅ Boost Criança 8 Anos (+10%) configurado

### Verificação

- ✅ 11 arquivos YAML criados em `experts/externos/`
- ✅ `_pool.yaml` válido (yamllint passed)
- ✅ Bounded Context correto (externos separados de internos)

---

## MÉTRICAS FINAIS DA DELIBERAÇÃO

| Métrica | Valor |
|---------|-------|
| Duração deliberação | ~40 min (15:01 → 15:58) |
| Decisões tomadas | 8 |
| Versões refinadas | 2 (v1 complexa → v2 simplificada) |
| Arquivos criados | 11 |
| Arquivos modificados | 1 (orchestrator.yaml) |
| Experts consultados | 4 (CM, Thiel, Hormozi, Engenharia) |
| Princípios aplicados | 4 (DDD SSOT, BMAD AaC, Clean Code DRY, CM Princípio 1) |

---

**LOG ENCERRADO: 15/01/2026 15:58**

---

## 🔍 REVISÃO DE IMPECABILIDADE (16:09)

### Diagnóstico Inicial
- Arquivos externos tinham apenas ~16 linhas
- Experts internos (ex: `charlotte_mason.yaml`) têm ~130 linhas
- **Gap identificado:** Externos muito básicos, sem `veto`, `audit_q`, `alinhamento_north_star`

### Expansão Realizada

| Arquivo | Antes | Depois | Expansão |
|---------|-------|--------|----------|
| `crianca_8_anos.yaml` | 16 | 92 | **6x** |
| `pai_cetico.yaml` | 16 | 92 | **6x** |
| `mae_secular.yaml` | 16 | 93 | **6x** |
| `professor_tradicional.yaml` | 16 | 93 | **6x** |
| `avo_tradicional.yaml` | 16 | 96 | **6x** |
| `pai_tech.yaml` | 16 | 98 | **6x** |
| `mae_workaholic.yaml` | 16 | 97 | **6x** |
| `adolescente_entediado.yaml` | 16 | 100 | **6x** |
| `pai_classe_c.yaml` | 16 | 98 | **6x** |
| `mae_ansiosa.yaml` | 16 | 104 | **6.5x** |
| `_pool.yaml` | 37 | 119 | **3x** |

### Estrutura Adicionada a Cada Persona

Cada arquivo agora inclui:

```yaml
# Seções obrigatórias adicionadas:
- perfil:              # Contexto, background, preocupações
- audit_q:             # 6 perguntas de auditoria específicas
- veto:                # Poder de veto com prioridade e gatilhos
- alinhamento_north_star:  # Conexão com princípios do projeto
- citacoes:            # Frases características
- nota_importante:     # Tensões saudáveis e respostas
- referencias:         # Fontes e observações
```

### Hierarquia de Prioridades

| pri | Persona | Foco |
|-----|---------|------|
| 15 | Criança 8 Anos | Cliente real (+boost 10%) |
| 16 | Pai Cético | Secular/Universal |
| 17 | Mãe Secular | Evidência/Ciência |
| 18 | Professor Tradicional | Resultados/Métricas |
| 19 | Avó Tradicional | Tradição/Simplicidade |
| 20 | Pai Tech | Gamificação/UX |
| 21 | Mãe Workaholic | Tempo/Eficiência |
| 22 | Adolescente Entediado | Coolness/Relevância |
| 23 | Pai Classe C | Valor/Acessibilidade |
| 24 | Mãe Ansiosa | Validação/Segurança |

### Validação
- ✅ 11 arquivos YAML válidos
- ✅ Estrutura consistente com experts internos
- ✅ Cada persona tem 92-104 linhas
- ✅ Índice `_pool.yaml` atualizado com 119 linhas

---

**REVISÃO DE IMPECABILIDADE CONCLUÍDA: 15/01/2026 16:09**


