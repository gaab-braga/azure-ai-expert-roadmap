# Módulo 05 — Arquitetura RAG avançada

> Esta página é o módulo inteiro. Siga as etapas de 1 a 9, nesta ordem, sem pular.
> Como estudar: [COMO-ESTUDAR.md](../COMO-ESTUDAR.md) · Seu progresso: [PROGRESSO.md](../PROGRESSO.md)

**Legenda:** ✅ provado em fonte oficial · 🔶 hipótese · ❓ em aberto

---

## 1. Visão geral

**Objetivo:** entender por dentro uma aplicação RAG de produção (busca híbrida, RRF, semantic ranker
e avaliação) e provar **com números** qual configuração de busca responde melhor.

**Repositório oficial:** `azure-search-openai-demo` (licença MIT), em
[azure-search-openai-demo/](azure-search-openai-demo/). É uma aplicação completa (backend em Python
com Quart, frontend em React e infraestrutura em Bicep), publicada com `azd up`. ✅

**Questões oficiais:** o curso AI-300T00 não tem um módulo do Learn só de RAG, então o quiz deste
módulo é próprio. A avaliação de RAG aparece no módulo 03. ✅

**Habilidades do exame cobertas** (domínio "Optimize generative AI systems"):
- Tune similarity thresholds, chunk sizes and retrieval strategies
- Implement and optimize hybrid search (semantic + keyword)
- Evaluate RAG with relevance metrics and A/B testing

**Custo — atenção:**
- O próprio README avisa que os recursos começam a cobrar **logo após** o deploy, principalmente o AI
  Search. ✅
- O guia de custo mínimo ([deploy_lowcost.md](azure-search-openai-demo/docs/deploy_lowcost.md))
  permite usar o AI Search **gratuito**, mas esse plano **não tem semantic ranker**, só permite 1
  serviço gratuito por assinatura e não suporta managed identity. ✅
- Consequência: para comparar com e sem semantic ranker, você precisa de um plano pago (Basic ou
  maior). Faça a comparação de uma vez e apague tudo em seguida.

---

## 2. Pré-teste

Responda o [quiz.md](quiz.md) **sem consultar** e anote a nota no [PROGRESSO.md](../PROGRESSO.md).

---

## 3. Preparar o ambiente

```bash
python scripts/preparar_modulos.py 05
```

Depois siga o [apoio/README.md](apoio/README.md). O deploy é feito numa pasta de trabalho criada com
`azd init`, e **não** na cópia de referência.

---

## 4. Estudar (ler o código na ordem do fluxo de uma pergunta)

| # | Estudar | O que observar | Checagem de memória |
| :-- | :-- | :-- | :-- |
| 1 | [README](azure-search-openai-demo/README.md) e [arquitetura](azure-search-openai-demo/docs/architecture.md) | Os componentes e o caminho de uma pergunta | Quais serviços do Azure participam? |
| 2 | [chatreadretrieveread.py](azure-search-openai-demo/app/backend/approaches/chatreadretrieveread.py), por volta da linha 311 | O `retrieval_mode` decide entre texto, vetor ou os dois; sem esse parâmetro, roda **híbrido** ✅. O `semantic_ranker` fica **desligado** se a requisição não o pedir ✅. O `top` padrão é 5 ✅ | O que acontece se a requisição não mandar `retrieval_mode`? |
| 3 | [approach.py](azure-search-openai-demo/app/backend/approaches/approach.py) (método de busca) | Onde `top`, `use_text_search`, `use_vector_search` e os limites mínimos de nota viram a chamada ao AI Search | Para que servem `minimum_search_score` e `minimum_reranker_score`? |
| 4 | Prompts em `app/backend/approaches/prompts/` | A etapa 1 **reescreve a pergunta** usando o histórico, antes de buscar | Por que reescrever a pergunta antes da busca? |
| 5 | [evaluation.md](azure-search-openai-demo/docs/evaluation.md) e `evals/evaluate_config.json` | Métricas `gpt_groundedness`, `gpt_relevance`, `latency` e `citations_matched` ✅ | Que métricas o projeto já mede? |
| 6 | [deploy_lowcost.md](azure-search-openai-demo/docs/deploy_lowcost.md) e [deploy_private.md](azure-search-openai-demo/docs/deploy_private.md) | Os planos gratuitos e o que se perde com eles; a versão com rede privada | O que o plano gratuito do Search não tem? |
| 7 | **Deploy de verdade**, seguindo o [apoio](apoio/README.md) | Faça perguntas e mude as "Developer settings" na interface | O que muda na resposta ao trocar o modo de busca? |

---

## 5. Ler (aprofundar)

| Leitura | Por quê |
| :-- | :-- |
| [hybrid-search-overview.md](leituras/hybrid-search-overview.md) · [oficial](https://learn.microsoft.com/azure/search/hybrid-search-overview) | O que é busca híbrida |
| [hybrid-search-ranking.md](leituras/hybrid-search-ranking.md) · [oficial](https://learn.microsoft.com/azure/search/hybrid-search-ranking) | Como o RRF junta as listas |
| [semantic-search-overview.md](leituras/semantic-search-overview.md) · [oficial](https://learn.microsoft.com/azure/search/semantic-search-overview) | O que o semantic ranker faz, e o que não faz |

**Conta para fixar o RRF:** cada documento ganha `1/(posição + 60)` em cada lista em que aparece. Um
documento em 1º lugar só na busca de texto soma `1/61 ≈ 0,0164`. Um documento em 2º lugar nas duas
listas soma `2 × 1/62 ≈ 0,0323` e fica **na frente**. O RRF premia quem aparece bem nas duas buscas.

---

## 6. Pós-teste

Refaça o [quiz.md](quiz.md) e a revisão intercalada que está no fim dele. Anote as notas no
[PROGRESSO.md](../PROGRESSO.md).

---

## 7. Projeto do zero

Enunciado, requisitos e rubrica: [projeto/README.md](projeto/README.md). Registre cada consulta no
[diario.md](diario.md).

---

## 8. Explicar

Escreva a seção "Como funciona" do [projeto/README.md](projeto/README.md) explicando a sua tabela de
resultados para alguém de negócio: qual configuração usar e por quê.

---

## 9. Fechar o módulo

- [ ] `azd down --purge` na pasta de trabalho (veja [apoio/README.md](apoio/README.md#apagar-tudo))
- [ ] Evidências em [evidencias/](evidencias/)
- [ ] Projeto aprovado na rubrica e nenhum 🔶 pendente neste módulo
- [ ] Commit e push · [PROGRESSO.md](../PROGRESSO.md) com as datas de revisão
- [ ] Fim do curso: veja a seção "Fechamento" do [COMO-ESTUDAR.md](../COMO-ESTUDAR.md#fechamento-do-curso)
