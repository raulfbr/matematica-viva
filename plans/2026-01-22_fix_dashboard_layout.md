# Planejamento: Correção Crítica do Layout da Dashboard
**Data:** 22/01/2026 - 14:47 | **Status:** Revisado e Pronto

## 1. O Problema
O layout do `index.html` quebrou.
**Causa:** Durante a última atualização, a variável `STYLE_CSS` em `build_dashboard.py` foi corrompida. O arquivo ficou com **duas definições** de CSS mescladas incorretamente, gerando sintaxe inválida.

## 2. A Solução (Estratégia Segura)
Vamos substituir **todo o bloco de definição do CSS** em `tools/build_dashboard.py` por um bloco limpo e correto.

### O Bloco CSS Correto (V3.1)
Deve incluir:
- Reset Global (`* { margin: 0... }`)
- Variáveis CSS (`:root`)
- Layout (`.sidebar`, `.main-content`)
- Componentes (`.card`, `.btn-arr`, `.stat-card`)
- **Fix Crítico:** Classes específicas de variante (ex: `.card.raizes`)
- Mobile Media Queries (`@media (max-width: 1024px)`)

### Simulação Mental ("Dry Run")
1.  **Ação:** Selecionar linhas ~28 até ~236 do `build_dashboard.py`.
2.  **Substituição:** Inserir o novo CSS consolidado.
3.  **Resultado Esperado:** O script Python volta a ser válido. O CSS gerado no `index.html` será limpo.
4.  **Risco:** Se errarmos as linhas de início/fim, podemos apagar o `def main():`.
    - **Mitigação:** Usarei `target_content` (conteúdo exato) no `replace_file_content` para garantir que só estou substituindo o que quero, ou usarei números de linha com margem de segurança após ler o arquivo novamente. **Vou ler o arquivo com números de linha antes de aplicar.**

## 3. Plano de Execução (Passo a Passo)

1.  **Leitura de Precisão:**
    - Ler `tools/build_dashboard.py` linhas 20-300 para identificar EXATAMENTE onde começa e termina a bagunça.
2.  **Correção Cirúrgica:**
    - Substituir o bloco `STYLE_CSS = """ ... """` inteiro.
3.  **Teste de Build:**
    - Rodar o script.
    - Verificar se o erro de sintaxe sumiu e se o HTML gerado abre corretamente.

**Autorizado para Execução.**
