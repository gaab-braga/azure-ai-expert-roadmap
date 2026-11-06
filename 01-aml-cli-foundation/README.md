# Módulo 01 — Fundação na CLI v2 do Azure Machine Learning

> Esta página é o módulo inteiro. Siga as etapas de 1 a 9, nesta ordem, sem pular.
> Como estudar: [COMO-ESTUDAR.md](../COMO-ESTUDAR.md) · Seu progresso: [PROGRESSO.md](../PROGRESSO.md)

**Legenda:** ✅ provado em fonte oficial · 🔶 hipótese · ❓ em aberto

---

## 1. Visão geral

**Objetivo:** escrever e enviar pelo terminal os quatro tipos de trabalho mais cobrados (job de
comando, sweep, pipeline com componentes e endpoint online), usando YAML validado pelo schema
oficial e rastreio com MLflow.

**Repositório oficial:** `mslearn-aml-cli` (licença MIT), em [mslearn-aml-cli/](mslearn-aml-cli/).
É uma **cópia só para leitura**: o lab roda num clone próprio no Cloud Shell (etapa 3).

**Habilidades do exame cobertas** (guia oficial, domínios "MLOps infrastructure" e "ML model lifecycle"):
- Create and manage a workspace, compute targets, data assets, environments, components
- Run model training scripts · Automate hyperparameter tuning · Implement training pipelines
- Configure experiment tracking with MLflow
- Deploy models as real-time endpoints with managed inference options

**Tempo:** o lab informa só a criação da compute instance ("2 to 5 minutes"). ✅ O resto depende do seu ritmo.

**Custo — atenção:**
- A compute instance (`STANDARD_DS11_V2`) cobra enquanto estiver ligada. Os labs mandam pará-la
  (`az ml compute stop`). ✅
- O endpoint do lab 05 (`Standard_F4s_v2`) cobra enquanto existir. Apague-o no fim do lab. ✅
- O workspace cobra um pouco de armazenamento mesmo parado. ✅ No fim do módulo, apague o grupo de
  recursos inteiro (etapa 9).

**Aviso:** a trilha do Learn deste repositório saiu do catálogo, e ele **não faz parte** do curso
oficial AI-300T00. ✅ Ele continua aqui porque ensina a gramática YAML/CLI que os outros módulos
pressupõem. Como não há questões oficiais para ele, o quiz é próprio (etapas 2 e 6).

---

## 2. Pré-teste

Responda o [quiz.md](quiz.md) **sem consultar nada** e anote a nota no [PROGRESSO.md](../PROGRESSO.md).
Errar agora é o esperado: o pré-teste mostra o que você ainda não sabe e prepara a memória para a
resposta certa.

---

## 3. Preparar o ambiente

1. Baixe a cópia de referência (só na primeira vez):

    ```bash
    python scripts/preparar_modulos.py 01
    ```

2. Siga o [apoio/README.md](apoio/README.md): pré-requisitos, como abrir o Cloud Shell na mesma versão
   do lab e como **recriar o ambiente** se você tiver apagado os recursos entre uma sessão e outra.

---

## 4. Estudar (labs oficiais)

Para cada lab: leia a teoria indicada → faça o lab → anote no [diario.md](diario.md) os pontos de
"o que observar" → feche o lab e responda de memória à pergunta de checagem.

| # | Lab oficial | Teoria antes do lab | O que observar | Checagem de memória |
| :-- | :-- | :-- | :-- | :-- |
| 01 | [Criar workspace e assets](mslearn-aml-cli/Instructions/Labs/01-create-workspace.md) | — | `az configure --defaults` evita repetir grupo e workspace; o environment é Docker + Conda | Quais 2 arquivos definem um environment? |
| 02 | [Job Python básico](mslearn-aml-cli/Instructions/Labs/02-run-python-job.md) | [commandJob.schema.json](leituras/commandJob.schema.json) (campos `command`, `inputs`, `compute`) | Como um input de dados vira `${{inputs.x}}` no comando | Que campo liga o job a uma compute? |
| 03 | [Sweep de hiperparâmetros](mslearn-aml-cli/Instructions/Labs/03-run-sweep-job.md) | [how-to-tune-hyperparameters.md](leituras/how-to-tune-hyperparameters.md) | Os arquivos estão em `Allfiles/Labs/02/sweep-job` (a numeração das pastas está deslocada) ✅; o YAML usa o cluster `azureml:aml-cluster`, com 3 trials em paralelo ✅; os labs 02 e 04 deixam o nome da compute para você preencher. Veja os [ajustes que eu fiz](apoio/ajustes-dos-labs/README.md) | Por que um sweep roda melhor em cluster? |
| 04 | [MLflow nos jobs](mslearn-aml-cli/Instructions/Labs/04-use-mlflow-jobs.md) | [how-to-use-mlflow-cli-runs.md](leituras/how-to-use-mlflow-cli-runs.md) | Diferença entre `autolog()` e log manual | Precisa configurar tracking URI dentro de um job? |
| 05 | [Endpoint online gerenciado](mslearn-aml-cli/Instructions/Labs/05-deploy-managed-endpoint.md) | — | Endpoint ≠ deployment: um endpoint pode ter vários deployments | Qual comando apaga o endpoint ao final? |
| 06 | [Pipeline com componentes](mslearn-aml-cli/Instructions/Labs/06-create-pipeline.md) | [reference-yaml-job-pipeline.md](leituras/reference-yaml-job-pipeline.md) | Componente registrado × job; como a saída de um passo vira entrada do próximo | Que tipos de job podem ser passos de um pipeline? |

---

## 5. Ler (aprofundar)

| Leitura | Por quê |
| :-- | :-- |
| [reference-yaml-job-pipeline.md](leituras/reference-yaml-job-pipeline.md) · [oficial](https://learn.microsoft.com/azure/machine-learning/reference-yaml-job-pipeline?view=azureml-api-2) | Todos os campos de um pipeline job |
| [how-to-tune-hyperparameters.md](leituras/how-to-tune-hyperparameters.md) · [oficial](https://learn.microsoft.com/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2) | Amostragem, distribuições e políticas de parada antecipada |
| [how-to-use-mlflow-cli-runs.md](leituras/how-to-use-mlflow-cli-runs.md) · [oficial](https://learn.microsoft.com/azure/machine-learning/how-to-use-mlflow-cli-runs?view=azureml-api-2) | Experimentos, runs e autolog |
| [pipelineJob](leituras/pipelineJob.schema.json) · [commandJob](leituras/commandJob.schema.json) · [sweepJob](leituras/sweepJob.schema.json) (JSON schemas) | Para consultar o nome exato de um campo |
| `referencias/azureml-examples/cli/jobs/basics/` (`hello-mlflow.yml`, `hello-sweep.yml`) | Exemplos mínimos e corretos |
| `referencias/azureml-examples/cli/jobs/pipelines-with-components/basics/` | Pipelines do mais simples ao mais completo |

Para ter a pasta `referencias/`, rode `python scripts/preparar_modulos.py ref`.

---

## 6. Pós-teste

Refaça o [quiz.md](quiz.md) sem consultar, anote a nota nova no [PROGRESSO.md](../PROGRESSO.md) e
compare com a do pré-teste. Releia a fonte de cada questão que errou.

---

## 7. Projeto do zero

Enunciado, requisitos e rubrica: [projeto/README.md](projeto/README.md).

**Regra:** comece sem abrir os labs. Quando precisar consultar algo, consulte, mas registre no
[diario.md](diario.md) **o que** foi e **por quê**. Esse registro mostra o que ainda não está firme.

---

## 8. Explicar

Escreva a seção "Como funciona" do [projeto/README.md](projeto/README.md) como se ensinasse um colega
que nunca usou o Azure ML. Se travar em algum ponto, é ali que está a lacuna: volte à leitura.

---

## 9. Fechar o módulo

- [ ] Apague o grupo de recursos (veja [apoio/README.md](apoio/README.md#apagar-tudo))
- [ ] Prints e saídas salvos em [evidencias/](evidencias/)
- [ ] Projeto aprovado na rubrica e nenhum 🔶 pendente neste módulo
- [ ] Commit e push
- [ ] [PROGRESSO.md](../PROGRESSO.md) atualizado, com as datas de revisão (+1, +7 e +30 dias) marcadas
