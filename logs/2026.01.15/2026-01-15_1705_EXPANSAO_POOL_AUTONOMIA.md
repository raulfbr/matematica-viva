# EXPANSÃO POOL EXTERNOS + AUTONOMIA ORCHESTRATOR
**Data:** 15/01/2026 17:05 | **Tipo:** Implementação

---

## EXPANSÃO DO POOL EXTERNO

### Novos Experts Externos Criados

#### 1. Pai Montessoriano (sugerido por Jerome Bruner)
- **Arquivo:** `experts/externos/pai_montessoriano.yaml`
- **Título:** O Defensor do Método Alternativo
- **Foco:** Questiona CPA vs métodos alternativos (Montessori, Waldorf)
- **Pergunta típica:** "Por que CPA e não materiais Montessori?"
- **Prioridade:** 25

#### 2. Mãe Veterana (sugerido por Seth Godin)
- **Arquivo:** `experts/externos/mae_veterana.yaml`
- **Título:** A Prova Social Viva
- **Foco:** Valida promessas com experiência de 3+ anos
- **Pergunta típica:** "Isso é realista para uma mãe no primeiro mês?"
- **Prioridade:** 26

### Métricas do Pool

| Antes | Depois |
|-------|--------|
| 10 externos | 12 externos |
| 24 experts total | 26 experts total |

---

## MODO DELIBERACAO_AUTONOMA

### Conceito
Loop automático que alterna entre experts internos e externos, com logging em tempo real, sem intervenção do Maestro até conclusão ou impasse.

### Configuração

```yaml
DELIBERACAO_AUTONOMA:
  autonomo: true
  max_rodadas: 5
  condicao_parada: "Consenso 80%+ OU max_rodadas"
  escalar_para_maestro: "Impasse após max_rodadas"
```

### Fases do Loop

```
┌─────────────────────────────────────────────────────┐
│                    INICIALIZAÇÃO                     │
│  - Recebe tema                                       │
│  - Cria log com timestamp                           │
│  - Seleciona experts relevantes                     │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│                  RODADA INTERNA                      │
│  - Posições iniciais dos internos                   │
│  - Réplicas                                         │
│  - Síntese parcial por CM                          │
│  - Registra em log                                  │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│                 CONSULTA EXTERNA                     │
│  - Seleciona 2-3 externos (algoritmo P)            │
│  - Externos avaliam síntese                         │
│  - Fazem perguntas desafiadoras                    │
│  - Registra em log                                  │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│                RODADA DE RESPOSTA                    │
│  - Internos respondem externos                      │
│  - Tréplica se necessário                          │
│  - CM avalia mudança                               │
│  - Registra em log                                  │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│                  DECISÃO LOOP                        │
│  Consenso?                                          │
│  ├── SIM → Fechamento                              │
│  └── NÃO                                            │
│       ├── rodadas < max → Volta p/ Rodada Interna  │
│       └── rodadas >= max → Escala p/ Maestro       │
└─────────────────────────────────────────────────────┘
```

### Comando

```
/deliberar-autonomo [tema]
```

### Exemplo de Log Gerado

```
logs/2026-01-15T1705_DELIBERACAO_AUTONOMA_Incluir_Pictórico_Sementes.md
```

---

## ORCHESTRATOR v1.4

### Incrementos

| Métrica | v1.3 | v1.4 | Delta |
|---------|------|------|-------|
| Linhas | 277 | 367 | +90 |
| Externos | 10 | 12 | +2 |
| Modos | 5 | 6 | +1 |
| Comandos | 8 | 9 | +1 |
| Total experts | 24 | 26 | +2 |

### Novos Recursos

1. **Modo DELIBERACAO_AUTONOMA** — Loop com logging
2. **Comando /deliberar-autonomo** — Ativa loop
3. **Pai Montessoriano** — Questionador de método
4. **Mãe Veterana** — Prova social

---

## ARQUIVOS MODIFICADOS

| Arquivo | Ação |
|---------|------|
| `orchestrator.yaml` | v1.3 → v1.4 (+90 linhas) |
| `_pool.yaml` | +2 externos, métricas |
| `pai_montessoriano.yaml` | NOVO |
| `mae_veterana.yaml` | NOVO |

---

**IMPLEMENTAÇÃO CONCLUÍDA: 15/01/2026 17:10**
