# Quiz — Módulo 05 (RAG avançado)

Questões escritas para este curso a partir da documentação e do código oficiais (a fonte está em cada
gabarito). Responda sem consultar.

---

**05-Q1.** Como o RRF calcula a nota de um documento? O `k` dessa fórmula é o mesmo `k` da busca vetorial?

<details><summary>Gabarito</summary>

Soma `1/(rank + k)` de cada lista em que o documento aparece, sendo `k` uma **constante** (a doc cita
60). **Não** é o mesmo `k`: o da busca vetorial é o número de vizinhos mais próximos.
Fonte: [hybrid-search-ranking.md](leituras/hybrid-search-ranking.md).
</details>

---

**05-Q2.** O semantic ranker roda antes ou depois do RRF? Onde fica a nota dele?

<details><summary>Gabarito</summary>

**Depois.** Ele reordena o resultado já fundido pelo RRF e devolve uma nota separada,
`@search.rerankerScore`, que vai de 0 a 4.
Fonte: [hybrid-search-ranking.md](leituras/hybrid-search-ranking.md); [semantic-search-overview.md](leituras/semantic-search-overview.md).
</details>

---

**05-Q3.** O semantic ranker consegue encontrar um documento relevante que **não** veio na busca inicial?

<details><summary>Gabarito</summary>

**Não.** Ele só reordena o conjunto que já existe, os **50 primeiros** resultados. Não refaz a
consulta no índice inteiro. Por isso a busca inicial precisa ser boa.
Fonte: [semantic-search-overview.md](leituras/semantic-search-overview.md).
</details>

---

**05-Q4.** Numa consulta híbrida, você dá peso `0.5` à consulta vetorial. O que acontece? E qual é o peso padrão?

<details><summary>Gabarito</summary>

A nota vetorial **pesa menos** na fusão do RRF. O padrão é `1.0`, ou seja, sem peso extra.
Fonte: [hybrid-search-ranking.md](leituras/hybrid-search-ranking.md).
</details>

---

**05-Q5.** No `azure-search-openai-demo`, a requisição chega sem `retrieval_mode` e sem `semantic_ranker`.
Que busca roda?

<details><summary>Gabarito</summary>

Busca **híbrida** (texto e vetor), porque a ausência de `retrieval_mode` liga as duas, e **sem**
semantic ranker, porque ele fica desligado quando não é pedido. O `top` padrão é 5.
Fonte: [chatreadretrieveread.py](azure-search-openai-demo/app/backend/approaches/chatreadretrieveread.py), linhas 311 a 316.
</details>

---

**05-Q6.** Para economizar, você muda o AI Search para o plano gratuito. O que você perde?

<details><summary>Gabarito</summary>

O **semantic ranker** e o suporte a **managed identity**. Além disso, só é permitido **1** serviço
gratuito por assinatura.
Fonte: [deploy_lowcost.md](azure-search-openai-demo/docs/deploy_lowcost.md).
</details>

---

**05-Q7.** Por que a busca híbrida costuma ser melhor que a só vetorial para documentos técnicos?

<details><summary>Gabarito</summary>

A parte de **texto** (palavra-chave) acerta termos exatos, como códigos, siglas e nomes de produto, que
a busca vetorial pode "aproximar" errado. A parte **vetorial** acha o mesmo sentido escrito com outras
palavras. A híbrida junta as duas listas com o RRF.
Fonte: [hybrid-search-overview.md](leituras/hybrid-search-overview.md).
</details>

---

## Revisão intercalada (pós-teste)

Refaça, de memória: **03-Q2**, **03-Q3** ([módulo 03](../03-genaiops-ai-foundry/quiz.md)) e **04-Q4**
([módulo 04](../04-enterprise-iac-bicep/quiz.md)).
