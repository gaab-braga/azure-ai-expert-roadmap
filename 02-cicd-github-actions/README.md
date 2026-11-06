# Módulo 02 — Ciclo de vida de ML e CI/CD com GitHub Actions

> Esta página é o módulo inteiro. Siga as etapas de 1 a 9, nesta ordem, sem pular.
> Como estudar: [COMO-ESTUDAR.md](../COMO-ESTUDAR.md) · Seu progresso: [PROGRESSO.md](../PROGRESSO.md)

**Legenda:** ✅ provado em fonte oficial · 🔶 hipótese · ❓ em aberto

---

## 1. Visão geral

**Objetivo:** levar o modelo do experimento à produção sem comandos manuais. O GitHub treina,
registra, implanta com troca gradual de tráfego e monitora o drift, entrando no Azure **sem senha
guardada** (OIDC).

**Repositório oficial:** `mslearn-mlops`, em [mslearn-mlops/](mslearn-mlops/), com uma
[versão navegável](https://microsoftlearning.github.io/mslearn-mlops/). É o conjunto de labs do
**curso oficial AI-300T00** (os scripts usam o prefixo `ai300`). ✅ Esse repositório **não declara
licença**, por isso fica só na sua máquina e nunca é republicado. ✅

**Trilha oficial do Learn:** [Operationalize machine learning models (MLOps)](https://learn.microsoft.com/training/paths/build-first-machine-operations-workflow/),
com 7 módulos, todos com questões de verificação. ✅

**Habilidades do exame cobertas:**
- MLOps infrastructure: GitHub integration with secure access · resource provisioning with GitHub Actions · source control with Git
- ML model lifecycle: MLflow tracking · AutoML · hyperparameter tuning · training pipelines · register MLflow model
- Deploy (real-time endpoints) · progressive rollout and rollback · data drift · retraining triggers

**Tempo:** labs de 45 min cada (01 a 06) e 60 min (07), segundo os próprios labs ✅. A trilha do
Learn soma 349 min ✅ (catálogo do Learn).

**Custo — atenção:**
- O `setup.sh` do lab cria compute instance e cluster `aml-cluster` (DS11_V2, até 2 nós). ✅
- O endpoint do lab 07 (`Standard_D2as_v4`) cobra enquanto existir. ✅
- O lab 05 pode criar **3 grupos de recursos** (dev, prod e registry). ✅

---

## 2. Pré-teste

Responda o [quiz.md](quiz.md) **sem consultar** e anote a nota no [PROGRESSO.md](../PROGRESSO.md).

---

## 3. Preparar o ambiente

```bash
python scripts/preparar_modulos.py 02
```

Depois siga o [apoio/README.md](apoio/README.md): Cloud Shell na mesma versão do lab, como recriar o
ambiente e o repositório-template do GitHub (labs 06 e 07).

---

## 4. Estudar (Learn → lab → questões oficiais)

Para cada linha, nesta ordem: **teoria** no Learn → **lab** → anote no [diario.md](diario.md) o
"o que observar" → **questões oficiais** (knowledge check) do Learn, respondidas de memória.

| # | Teoria (Learn) | Lab oficial | O que observar | Questões oficiais |
| :-- | :-- | :-- | :-- | :-- |
| 00 | [Get started with ML in Azure](https://learn.microsoft.com/training/modules/design-machine-learning-model-training-solution/) | [Estudo de caso Proseware](mslearn-mlops/docs/00-case-study.md) | O problema de negócio que guia todos os labs | [knowledge check](https://learn.microsoft.com/training/modules/design-machine-learning-model-training-solution/6-knowledge-check) |
| 01 | [Experiment with Azure ML](https://learn.microsoft.com/training/modules/experiment-azure-machine-learning/) | [Achar o melhor modelo](mslearn-mlops/docs/01-experiment-evaluate-models.md) | AutoML × tracking manual com MLflow | [knowledge check](https://learn.microsoft.com/training/modules/experiment-azure-machine-learning/9-knowledge-check) |
| 02 | [Run training scripts and track with MLflow](https://learn.microsoft.com/training/modules/run-training-scripts-track-models-mlflow/) | [Otimizar o treino](mslearn-mlops/docs/02-optimize-model-training.md) | Notebook → script com funções → command job | [knowledge check](https://learn.microsoft.com/training/modules/run-training-scripts-track-models-mlflow/8-knowledge-check) |
| 03 | [Hyperparameter tuning](https://learn.microsoft.com/training/modules/perform-hyperparameter-tuning-azure-machine-learning-pipelines/) | [Sweep job](mslearn-mlops/docs/03-hyperparameter-tuning.md) | Compare com o sweep em YAML do módulo 01: aqui é pelo SDK | [knowledge check](https://learn.microsoft.com/training/modules/perform-hyperparameter-tuning-azure-machine-learning-pipelines/7-knowledge-check) |
| 04 | [Run pipelines](https://learn.microsoft.com/training/modules/run-pipelines-azure-machine-learning/) | [Pipelines](mslearn-mlops/docs/04-run-pipelines.md) | Mesma ideia do módulo 01, outra interface | [knowledge check](https://learn.microsoft.com/training/modules/run-pipelines-azure-machine-learning/6-knowledge-check) |
| 05 | — (sem módulo correspondente na trilha) | [Planejar a solução MLOps](mslearn-mlops/docs/05-plan-and-prepare.md) | Por que dev, prod e um **registry** compartilhado | — |
| 06 | [Automate training with GitHub Actions](https://learn.microsoft.com/training/modules/trigger-azure-machine-learn-jobs-github-actions/) | [Treino automatizado](mslearn-mlops/docs/06-automate-model-training.md) | O lab usa **service principal com segredo** (`AZURE_CREDENTIALS`) e papel **Contributor** ✅. No projeto você troca por OIDC | [knowledge check](https://learn.microsoft.com/training/modules/trigger-azure-machine-learn-jobs-github-actions/6-knowledge-check) |
| 07 | [Deploy and monitor a model](https://learn.microsoft.com/training/modules/deploy-model-github-actions/) | [Deploy e monitoramento](mslearn-mlops/docs/07-deploy-monitor.md) | Gatilho por comentário `/train-prod` (`issue_comment`) ✅; GitHub *environments* dev/prod; coleta de dados → monitor de drift | [knowledge check](https://learn.microsoft.com/training/modules/deploy-model-github-actions/6-knowledge-check) |

Os módulos 01 a 04 retomam assuntos do módulo 01 deste curso, agora pelo SDK e por notebooks. Essa
repetição é intencional (intercalação): aproveite para comparar as duas formas.

---

## 5. Ler (aprofundar)

| Leitura | Por quê |
| :-- | :-- |
| [connect-from-azure-openid-connect.md](leituras/connect-from-azure-openid-connect.md) · [oficial](https://learn.microsoft.com/azure/developer/github/connect-from-azure-openid-connect) | Login OIDC: a base do projeto |
| [how-to-github-actions-machine-learning.md](leituras/how-to-github-actions-machine-learning.md) · [oficial](https://learn.microsoft.com/azure/machine-learning/how-to-github-actions-machine-learning?view=azureml-api-2) | GitHub Actions com Azure ML |
| [how-to-safely-rollout-online-endpoints.md](leituras/how-to-safely-rollout-online-endpoints.md) · [oficial](https://learn.microsoft.com/azure/machine-learning/how-to-safely-rollout-online-endpoints?view=azureml-api-2) | Blue/green, divisão de tráfego e espelhamento |
| [concept-model-monitoring.md](leituras/concept-model-monitoring.md) · [oficial](https://learn.microsoft.com/azure/machine-learning/concept-model-monitoring?view=azureml-api-2) | Sinais de monitoramento e alertas |
| `referencias/azureml-examples/cli/endpoints/online/managed/sample/` (`blue-deployment.yml`, `green-deployment.yml`) e `cli/deploy-safe-rollout-online-endpoints.sh` | Rollout seguro completo pela CLI |
| `referencias/azureml-examples/cli/endpoints/batch/deploy-models/heart-classifier-mlflow/` | Endpoint em lote (batch), que o exame também cobra |
---

## 6. Pós-teste

Refaça o [quiz.md](quiz.md) **e** a revisão intercalada que está no fim dele. Anote as notas no
[PROGRESSO.md](../PROGRESSO.md).

---

## 7. Projeto do zero

Enunciado, requisitos e rubrica: [projeto/README.md](projeto/README.md). Comece sem abrir os labs e
registre cada consulta no [diario.md](diario.md).

---

## 8. Explicar

Escreva a seção "Como funciona" do [projeto/README.md](projeto/README.md). Inclua um diagrama em texto
do fluxo: push → treino → registro → deploy → tráfego → monitor.

---

## 9. Fechar o módulo

- [ ] Apague os grupos de recursos, o service principal ou app do Entra e o repositório-template de
      teste (veja [apoio/README.md](apoio/README.md#apagar-tudo))
- [ ] Evidências em [evidencias/](evidencias/)
- [ ] Projeto aprovado na rubrica e nenhum 🔶 pendente neste módulo
- [ ] Commit e push · [PROGRESSO.md](../PROGRESSO.md) com as datas de revisão
