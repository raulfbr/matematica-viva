# Planejamento: Restauração da Dashboard Completa do Reino
**Data:** 22/01/2026 - 14:15 | **Status:** Validado e Pronto
**Objetivo:** Restaurar a visibilidade de todos os ciclos (Brotos, Raízes, Legado), confirmar o Manual do Portador e garantir que lições de Raízes sejam compiladas.

## 1. Diagnóstico do Estado Atual

### A. O Manual do Portador (A Joia Fixa)
- **Status:** ✅ **EXISTE e SEGURO**.
- **Localização:** `site/manual-portador.html`.
- **Análise:** É um arquivo HTML robusto de 824 linhas. Não há evidência de um Markdown gerador para ele neste momento.
- **Estratégia de Preservação:**
    - O comando `gutebreg` (nossos scripts Python) opera gerando arquivos *específicos* (index.html e sementes/*.html). Ele **não** deleta a pasta `site/` inteira. Portanto, o manual está seguro.
    - **Ação Extra de Segurança:** Adicionarei um log no final do build: `Verificando integridade: Manual do Portador... OK`. Se ele sumir, o script grita.

### B. Os Ciclos Perdidos (Brotos, Raízes, Legado)
- **Status:** ⚠️ **LINKS MORTOS**.
- **Análise do Dashboard:** A sidebar aponta para `placeholders/*.html`, mas essas páginas são simples esqueletos ou não existem.
- **Estratégia Visual:**
    - Em vez de esconder os links ou levá-los para páginas vazias, vamos criar páginas "Em Breve" bonitas (`coming-soon.html`) para cada um, com a identidade visual do respectivo ciclo (Ex: Legado com ícones de ânforas, Raízes com árvores).

### C. A Lição de Raízes (O Guardião Esquecido)
- **Arquivo Alvo:** `curriculo/02_RAIZES/01_RAIZES_I/L001_IDENTIFICANDO_ESQUERDA_DIREITA.yaml`.
- **Status Atual do Build:** ❌ **IGNORADO**.
- **Causa:** O script `build_lessons.py` é "monocultura": só planta Sementes.
- **Ação Necessária:**
    - Transformar `build_lessons.py` em "policultura".
    - Ele irá iterar sobre uma lista de configurações:
      ```python
      MAPA_CICLOS = {
          '01_SEMENTESV6': {'out': 'site/sementes', 'tipo': 'Sementes'},
          '02_RAIZES':     {'out': 'site/raizes',   'tipo': 'Raízes'}
      }
      ```

---

## 2. Plano de Execução Detalhado

### Passo 1: O Mapeamento Universal (Crawler V2)
Atualizar `tools/build_lessons.py` para suportar múltiplos ciclos.

- **Nova Lógica:**
    - Loop principal itera sobre as chaves do `MAPA_CICLOS`.
    - Para cada ciclo, varre a pasta correspondente.
    - Ao gerar o HTML, injeta classes CSS específicas (ex: `.theme-raizes` vs `.theme-sementes`) se quisermos diferenciar visualmente no futuro.
    - **Importante:** A lição L001 de Raízes deve ser gerada em `site/raizes/` (pasta nova).

### Passo 2: O Dashboard Unificado
Atualizar `tools/build_dashboard.py` para exibir as novas seções.

- **Seção Raízes:**
    - Onde hoje existe `<section id="sementes">`, haverá também `<section id="raizes">`.
    - Esta seção só aparecerá se houver lições de Raízes geradas.
    - Os cards de Raízes terão uma cor de borda ou ícone distinto (Árvore `🌳` em vez de Semente `🌱`).

- **Placeholders Inteligentes:**
    - Criar um scriptzinho rápido `tools/build_placeholders.py` (ou função interna) que garante que `site/placeholders/brotos.html` exista e tenha um texto bonito "O Pomar está crescendo...". Isso elimina os erros 404 e melhora a UX.

### Passo 3: Segurança e Validação
- No final do script `build_dashboard.py`:
    - Check: `manual-portador.html` existe?
    - Check: `L001_IDENTIFICANDO_ESQUERDA_DIREITA.html` existe?
    - Check: `blog/*.html` existem?
    - Relatório final de "Saúde do Reino".

---

## 3. Checklist de Implementação (Revisão Incremental)

1.  [ ] **Refatorar `build_lessons.py`**:
    *   Implementar `MAPA_CICLOS`.
    *   Ajustar caminhos de saída dinâmicos.
2.  [ ] **Atualizar `build_dashboard.py`**:
    *   Ler lições de todas as pastas de saída.
    *   Agrupar lições por ciclo.
    *   Renderizar seções separadas no HTML principal.
3.  [ ] **Gerar Placeholders**:
    *   Criar páginas HTML estáticas simples para os links futuros (Brotos/Legado).
4.  [ ] **Validação Final**:
    *   Conferir Manual, Raízes L001 e Blog.

---

## 4. Simulação Mental e Análise Crítica (The "Antigravity" Simulation)

**Sua Pergunta:** "Isso vai quebrar outras coisas? Vai respeitar o planejamento anterior?"

Executei a simulação mental de compatibilidade.

### Compatibilidade com o Planejamento Anterior (Mobile + Blog)
- **Menu Mobile:** ✅ **Intacto**. O HTML/CSS do menu foi feito no `build_dashboard.py` (Main Template). O novo plano não toca nessa parte do código, apenas adiciona seções no "miolo" da página.
- **Blog Index:** ✅ **Intacto**. A função `get_blog_posts()` e sua injeção continuam funcionando exatamente igual.
- **Smart Build (Cache):** ⚠️ **Atenção Dedicada Necessária**.
    - Ao refatorar `build_lessons.py` para iterar por pastas, preciso garantir que a lógica `if html_date > yaml_date: continue` seja aplicada dentro do novo loop.
    - **Ação:** O código será copiado e adaptado, não removido. A otimização de tempo continuará valendo para Sementes e passará a valer para Raízes também.

### Conclusão: "Upgrade, não Restart"
Este plano é um "DLC" (Conteúdo Extra) para o sistema atual. Ele expande a capacidade do `build_lessons` sem remover as funcionalidades que acabamos de criar.
- **Vai melhorar:** Sim, pois o sistema deixa de ser "cego" para outras pastas.
- **Vai quebrar?** Não, pois a estrutura de saída (`site/sementes/*.html`) será mantida para o que já existe, evitando quebrar links antigos.
