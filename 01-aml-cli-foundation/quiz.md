# Quiz — Módulo 01 (CLI v2)

Questões escritas para este curso a partir da documentação oficial (a fonte está em cada gabarito).
Responda **sem consultar**. Só depois abra o gabarito.

**Usar em:** pré-teste (etapa 2), pós-teste (etapa 6) e revisões de +1, +7 e +30 dias.

---

**01-Q1.** Num *pipeline job* da CLI v2, quais tipos de job podem ser usados como passos (`jobs:`)?

a) Qualquer tipo de job · b) Só *command jobs* · c) *Command jobs* e *sweep jobs* · d) *Command jobs*, *sweep jobs* e *AutoML jobs*

<details><summary>Gabarito</summary>

**c)** A referência diz que hoje só *command jobs* e *sweep jobs* rodam dentro de um pipeline.
Fonte: [reference-yaml-job-pipeline.md](leituras/reference-yaml-job-pipeline.md), campo `jobs`.
</details>

---

**01-Q2.** Num sweep, o script de treino registra a métrica como `val_accuracy`, e o YAML usa
`primary_metric: accuracy`. O que acontece?

<details><summary>Gabarito</summary>

O sweep não acha a métrica: o nome em `primary_metric` precisa ser **exatamente** igual ao nome
registrado pelo script. Sem ela, a parada antecipada também não funciona, porque usa essa métrica.
Fonte: [how-to-tune-hyperparameters.md](leituras/how-to-tune-hyperparameters.md), seção do objetivo.
</details>

---

**01-Q3.** Você vai ajustar 3 hiperparâmetros com amostragem **bayesiana**. Quais distribuições
você pode usar e qual é o número mínimo de execuções recomendado?

<details><summary>Gabarito</summary>

Só `choice`, `uniform` e `quniform`. A doc recomenda pelo menos **20 × o número de hiperparâmetros**,
ou seja, 60 execuções.
Fonte: [how-to-tune-hyperparameters.md](leituras/how-to-tune-hyperparameters.md), "Bayesian sampling".
</details>

---

**01-Q4.** Cite as três políticas de parada antecipada do Azure ML e diga o que a **Bandit** faz.

<details><summary>Gabarito</summary>

**Bandit**, **Median stopping** e **Truncation selection**. A Bandit encerra um job quando a métrica
principal dele fica fora da folga permitida (`slack_factor`, que é uma razão, ou `slack_amount`, que é
um valor absoluto) em relação ao melhor job, checando a cada `evaluation_interval`.
Fonte: [how-to-tune-hyperparameters.md](leituras/how-to-tune-hyperparameters.md), "Specify early termination policy".
</details>

---

**01-Q5.** Seu script usa MLflow e roda como job no Azure ML. Você precisa configurar o *tracking
URI* dentro do script?

<details><summary>Gabarito</summary>

**Não.** Jobs que usam MLflow e rodam no Azure ML registram tudo no workspace automaticamente. O
tracking URI só precisa ser configurado ao rastrear de **fora** do Azure ML (por exemplo, no seu
notebook local).
Fonte: [how-to-use-mlflow-cli-runs.md](leituras/how-to-use-mlflow-cli-runs.md).
</details>

---

**01-Q6.** Para que serve a linha `$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json`
no topo de um YAML? E qual o cuidado com o `latest`?

<details><summary>Gabarito</summary>

Ela faz o VS Code (extensão do Azure ML) **validar e autocompletar** o arquivo. O schema `latest` só
tem garantia de funcionar com a versão **mais recente** da extensão `ml` da CLI; versões antigas têm
schemas próprios.
Fonte: [reference-yaml-job-pipeline.md](leituras/reference-yaml-job-pipeline.md), introdução e campo `$schema`.
</details>

---

**01-Q7.** O que faz `az configure --defaults group=<rg> workspace=<ws>` e por que o lab usa esse comando?

<details><summary>Gabarito</summary>

Define o grupo de recursos e o workspace **padrão** da CLI. Assim os comandos `az ml ...` seguintes
não precisam repetir `--resource-group` e `--workspace-name`.
Fonte: lab [01-create-workspace.md](mslearn-aml-cli/Instructions/Labs/01-create-workspace.md).
</details>
