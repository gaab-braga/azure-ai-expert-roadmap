# Ajustes feitos nos labs do módulo 01

Cópias dos 4 YAMLs do `mslearn-aml-cli` (commit `191e880`) **com as edições que fiz ao fazer os
labs**. O original continua intacto em [../../mslearn-aml-cli/](../../mslearn-aml-cli/). Os arquivos
são da Microsoft (licença MIT); só as linhas abaixo são minhas.

| Arquivo | Original | Meu ajuste | Por quê |
| :-- | :-- | :-- | :-- |
| `Labs/02/basic-job/basic-job.yml` | `compute: azureml:<your-compute-instance-name>` | `azureml:testdev-vm` | O lab deixa o nome da compute para o aluno preencher |
| `Labs/02/input-data-job/data-job.yml` | idem | `azureml:testdev-vm` | idem |
| `Labs/03/mlflow-job/mlflow-job.yml` | idem | `azureml:testdev-vm` | idem |
| `Labs/02/sweep-job/sweep-job.yml` | `compute: azureml:aml-cluster`; `max_total_trials: 6`; `max_concurrent_trials: 3`; `timeout: 3600` | `azureml:testdev-vm`; `2`; `1`; `7200` | 🔶 Provavelmente cota ou custo: rodar na compute instance, que já existia, com menos trials. Confirme e anote o motivo real |

## Como reaplicar

Para reaplicar no clone que o lab manda fazer no Cloud Shell (no mesmo commit), copie o arquivo
`ajustes.patch` para lá e rode:

```bash
cd mslearn-aml-cli && git apply ajustes.patch
```

## Lição para o projeto do zero

O original do sweep usa **cluster** com 3 trials em paralelo. Na compute instance só cabe 1 por vez,
por isso o ajuste. No projeto do módulo 01 o sweep deve rodar num cluster
(`az ml compute create --type AmlCompute`). Esse é um dos requisitos.
