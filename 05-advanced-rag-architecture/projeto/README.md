# Projeto do zero — Módulo 05

> **Status:** ⏳ não iniciado

## Enunciado

Responda com números: **qual configuração de busca dá as melhores respostas para o seu conjunto de
documentos?** Use um corpus **seu**, de documentos públicos (por exemplo, as leituras oficiais deste
curso), e não os PDFs de exemplo do demo.

## Requisitos

- [ ] Corpus próprio (10 a 30 documentos públicos) indexado
- [ ] Conjunto de 20 a 30 perguntas com resposta esperada (*ground truth*). Inclua perguntas com
      **termos exatos** (siglas, nomes de propriedades) e perguntas **conceituais**
- [ ] A mesma avaliação rodada em 4 configurações:
      1. só texto (`retrieval_mode: text`)
      2. só vetor (`vectors`)
      3. híbrida (`hybrid`)
      4. híbrida + `semantic_ranker: true`
- [ ] Métricas: Groundedness, Relevance, latência e tokens
- [ ] Tabela de resultados + **conclusão**: qual configuração usar e qual o custo dela
- [ ] Um experimento extra à sua escolha: `top` (3 × 5 × 10), tamanho de chunk ou `minimum_reranker_score`
- [ ] Opcional: repetir uma configuração com rede privada (`deploy_private.md`)

## Rubrica

| Critério | 0 | 1 | 2 |
| :-- | :-- | :-- | :-- |
| Dados | Corpus de exemplo | Corpus próprio sem perguntas de termo exato | Corpus próprio + perguntas dos dois tipos |
| Experimento | 1 configuração | 2 ou 3 configurações | As 4 configurações + 1 extra |
| Métricas | Impressão subjetiva | Só qualidade | Qualidade + latência + tokens |
| Conclusão | Ausente | "A híbrida é melhor" sem números | Decisão justificada com a tabela e o custo |
| Explicação | Ausente | Descrição dos passos | "Como funciona" que alguém de negócio entende |

**Aprovado:** nenhum critério com 0 e pelo menos 8 pontos de 10.

## Resultados

| Configuração | Groundedness | Relevance | Latência (s) | Tokens/resposta |
| :-- | :-- | :-- | :-- | :-- |
| texto | | | | |
| vetor | | | | |
| híbrida | | | | |
| híbrida + semantic | | | | |

## Como funciona

*(Etapa 8.)*

## Evidências

*(Links para [../evidencias/](../evidencias/).)*
