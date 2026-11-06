# Quiz — Módulo 03 (GenAIOps)

Questões escritas para este curso a partir da documentação oficial (a fonte está em cada gabarito).
As **questões oficiais** do Learn estão linkadas na etapa 4 do [README](README.md). Responda sem consultar.

---

**03-Q1.** Qual é a escala do avaliador **Groundedness** e qual é o limite padrão de aprovação?

<details><summary>Gabarito</summary>

A escala vai de **1 a 5** e o limite padrão é **3**: nota igual ou acima de 3 é `pass`.
Fonte: [rag-evaluators.md](leituras/rag-evaluators.md).
</details>

---

**03-Q2.** Groundedness e Response Completeness medem coisas diferentes. Qual mede **precisão**, qual
mede **cobertura**, e qual exige resposta de referência (*ground truth*)?

<details><summary>Gabarito</summary>

- **Groundedness** mede **precisão**: a resposta não traz nada que não esteja no contexto.
- **Response Completeness** mede **cobertura** (*recall*): a resposta não deixa de fora o que
  importa. É ela que exige *ground truth*.

Fonte: [rag-evaluators.md](leituras/rag-evaluators.md).
</details>

---

**03-Q3.** Quais campos você deve passar ao Groundedness para ter o melhor resultado?

<details><summary>Gabarito</summary>

`response` e `context`. O `query` é opcional, mas melhora a precisão da nota, então o ideal é passar
os três.
Fonte: [rag-evaluators.md](leituras/rag-evaluators.md), "Using RAG evaluators".
</details>

---

**03-Q4.** O que o **Groundedness Pro** devolve e que serviço ele usa?

<details><summary>Gabarito</summary>

Devolve **verdadeiro ou falso** (não uma nota de 1 a 5) e usa o **Azure AI Content Safety**. Está em
preview.
Fonte: [rag-evaluators.md](leituras/rag-evaluators.md).
</details>

---

**03-Q5.** Como se liga o tracing do lado do servidor (*server-side*) num projeto Foundry? Precisa
mudar o código?

<details><summary>Gabarito</summary>

Basta **conectar um recurso do Application Insights ao projeto**: o Foundry liga o tracing
automaticamente, **sem mudança de código**. Os traces seguem as convenções semânticas do
**OpenTelemetry**.
Fonte: [trace-agent-setup.md](leituras/trace-agent-setup.md).
</details>

---

**03-Q6.** O tracing está ligado, mas você não consegue consultar a telemetria. Que papel RBAC falta?

<details><summary>Gabarito</summary>

**Log Analytics Reader** no recurso do Application Insights conectado.
Fonte: [trace-agent-setup.md](leituras/trace-agent-setup.md), pré-requisitos.
</details>

---

**03-Q7.** No painel de monitoramento de agentes, o uso de tokens subiu muito. O que a documentação
diz que isso pode indicar?

<details><summary>Gabarito</summary>

Prompts ou respostas **verbosos demais**, que podem ser otimizados (compare com o lab 03, que mede a
economia de tokens de um prompt mais conciso).
Fonte: [how-to-monitor-agents-dashboard.md](leituras/how-to-monitor-agents-dashboard.md).
</details>

---

## Revisão intercalada (pós-teste)

Refaça, de memória: **02-Q1**, **02-Q4** ([módulo 02](../02-cicd-github-actions/quiz.md)) e **01-Q2**
([módulo 01](../01-aml-cli-foundation/quiz.md)).
