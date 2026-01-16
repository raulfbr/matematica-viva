# ANÁLISE: Padronização YAMLs vs Builder
**Data:** 15/01/2026 17:35 | **Tipo:** Análise Técnica

---

## DESCOBERTAS

### L001 vs L002 — Comparação

| Aspecto | L001_TRINDADE_PALMA | L002_PEDRAS_FORTALEZA |
|---------|---------------------|------------------------|
| Linhas | 519 | 117 |
| Estrutura raiz | `licao:` wrapper | Flat (sem wrapper) |
| metadados | Nested em `licao.metadados` | Flat no root |
| para_o_portador | 6 campos detalhados | 4 campos |
| ritual_abertura | Campos separados | Campos separados |
| concreto | `instrucoes_portador` array | `passos` array |
| auditoria_qa | Checks booleanos detalhados | Arrays boolean simplificados |

### Template vs Realidade

| Aspecto | Template (licao-template.yaml) | L001 | L002 |
|---------|--------------------------------|------|------|
| Root wrapper | `licao:` | ✅ Tem | ❌ Não tem |
| id format | `MV-S-XXX` | ✅ | ✅ (mas no root) |
| concreto.instrucoes | Array de objetos | ✅ | ❌ (usa `passos`) |
| Linhas esperadas | ~145 template | 519 (3.5x) | 117 (0.8x) |

### Problema Principal

> **L002-L015 seguem estrutura DIFERENTE de L001 e do template!**

- L001: Segue template V5 fielmente (com wrapper `licao:`)
- L002+: Estrutura flat, campos com nomes diferentes

---

## DIAGNÓSTICO

### O que está "errado" nas L002+?

1. **Sem wrapper `licao:`** — acesso direto aos campos
2. **Campos com nomes diferentes:**
   - Template: `instrucoes_portador` → L002: `passos`
   - Template: `perguntas_do_coracao` → L002: `perguntas_coracao`
3. **Menos detalhes:** 
   - L001 tem `audio_script`, `protocolo_impecabilidade` — L002 não
4. **Estrutura flat vs nested:**
   - L001: `licao.metadados.id` 
   - L002: `id` (root)

### O que está CERTO?

- Conteúdo pedagógico parece bom
- Seções principais presentes
- QA checkboxes existem

---

## OPÇÕES

### Opção A: Padronizar YAMLs PRIMEIRO
**Esforço:** ~4-6 horas
**Resultado:** 17 YAMLs todos iguais a L001

**Prós:**
- Builder mais simples (um formato só)
- Template canônico respeitado
- Consistência total

**Contras:**
- Delay no builder
- L002-L015 precisam ser expandidas manualmente

### Opção B: Builder FLEXÍVEL que aceita ambos formatos
**Esforço:** +2 horas no builder
**Resultado:** Builder funciona com L001 E L002+

**Prós:**
- Builder pronto mais rápido
- Não perde trabalho já feito
- Gradualmente padroniza

**Contras:**
- Código mais complexo
- Dois formatos em produção

### Opção C: HÍBRIDO (RECOMENDADO)
**Esforço:** ~3 horas padronização + 2 horas builder

1. **Criar script de migração** que converte L002-L015 para formato L001
2. **Builder assume formato único** (L001/template)
3. **Executar migração** antes de build

---

## RECOMENDAÇÃO (Engenharia + CM)

### Opção C — HÍBRIDO

**Justificativa:**
- L002-L015 têm conteúdo bom, só estrutura diferente
- Script de migração pode ser automatizado
- Builder fica simples e robusto
- Template V5 se torna SSOT

### Plano de Ação Atualizado

```
FASE 0: Migração YAML (3h)
├── Criar migrate_yaml.py
├── Mapear: flat → nested
├── Mapear: passos → instrucoes_portador
├── Expandir campos faltantes com placeholders
└── Executar em L002-L015

FASE 1-8: Builder (como planejado)
```

### Script de Migração — Lógica

```python
def migrate_lesson(old_yaml, template):
    """
    Converte YAML flat (L002+) para formato nested (L001).
    """
    new = {'licao': {}}
    
    # Metadados (flat → nested)
    new['licao']['metadados'] = {
        'id': old_yaml.get('id'),
        'titulo': old_yaml.get('titulo'),
        'fase': old_yaml.get('fase'),
        # ...
    }
    
    # Concreto (passos → instrucoes_portador)
    if 'jornada' in old_yaml and 'concreto' in old_yaml['jornada']:
        if 'passos' in old_yaml['jornada']['concreto']:
            old_yaml['jornada']['concreto']['instrucoes_portador'] = \
                convert_passos(old_yaml['jornada']['concreto']['passos'])
    
    # ...
    return new
```

---

## VOTAÇÃO EXPERTS

| Expert | Voto | Razão |
|--------|------|-------|
| Engenharia | C (Híbrido) | "Um formato = menos bugs" |
| Charlotte Mason | C | "Ordem antes da ação" |
| Hormozi | B ou C | "Faça rápido, mas faça certo" |
| Tolkien | C | "Consistência é lei" |

**Consenso: Opção C (Híbrido)**

---

## PRÓXIMOS PASSOS

1. [ ] Criar `migrate_yaml.py` (~1h)
2. [ ] Testar com L002 (~30min)
3. [ ] Executar em L003-L015 (~30min)
4. [ ] Validar YAMLs migrados (~30min)
5. [ ] Iniciar builder com formato único

---

**AGUARDA:** Aprovação do Maestro

**Pergunta:** Quer que eu inicie pela migração dos YAMLs (Opção C)?
