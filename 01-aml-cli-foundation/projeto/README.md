# Projeto do zero — Módulo 01

> **Status:** ⏳ não iniciado

## Enunciado

Monte, **só com YAML e CLI** (sem notebooks e sem portal), um fluxo completo de treino e deploy
para um dataset **público e diferente do lab** (o lab usa diabetes). Sugestões: `breast_cancer` ou
`wine` do scikit-learn, ou um CSV do UCI. Dado de empresa, nunca.

## Requisitos

- [ ] `environment.yml` + `conda.yml` próprios
- [ ] `data.yml` registrando o dataset como data asset
- [ ] `command-job.yml` treinando um modelo, com `mlflow.autolog()` no script
- [ ] `sweep-job.yml` com pelo menos 2 hiperparâmetros, amostragem escolhida e justificada,
      política de parada antecipada e `primary_metric` igual à métrica registrada, rodando num
      **cluster** (`az ml compute create --type AmlCompute`)
- [ ] `pipeline-job.yml` com pelo menos 2 componentes próprios (preparar dados → treinar)
- [ ] Modelo registrado e publicado num endpoint online gerenciado, com uma chamada de teste
- [ ] Todo YAML com a linha `$schema` no topo
- [ ] `comandos.md` com a sequência exata de comandos para reproduzir tudo, do zero

## Rubrica

| Critério | 0 — não atende | 1 — parcial | 2 — atende |
| :-- | :-- | :-- | :-- |
| Reprodutibilidade | Faltam passos | Roda com ajustes manuais | Roda do zero só seguindo o `comandos.md` |
| Sweep | Não roda | Roda, mas a métrica não bate ou não há parada antecipada | Métrica certa, parada antecipada e escolha justificada |
| Pipeline | Ausente | 1 passo ou passos sem ligação | 2+ componentes com saída → entrada |
| Deploy | Ausente | Endpoint criado sem teste | Endpoint testado e apagado depois, com evidência |
| Explicação | Ausente | Lista de comandos | "Como funciona" que um colega entende |

**Aprovado:** nenhum critério com 0 e pelo menos 8 pontos de 10.

## Como funciona

*(Etapa 8: explique aqui, com suas palavras, o que cada arquivo faz e como eles se ligam.)*

## Evidências

*(Links para os arquivos em [../evidencias/](../evidencias/).)*
