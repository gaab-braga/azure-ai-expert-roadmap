# Apoio — Módulo 05

Arquivos **nossos**, que complementam o repositório oficial sem alterá-lo.

## Pré-requisitos

Azure Developer CLI (azd), Python, Node.js e Git, conforme a seção de pré-requisitos do
[README oficial](../azure-search-openai-demo/README.md). Depois:

```bash
azd auth login
```

## Onde fazer o deploy

**Nunca** dentro de `azure-search-openai-demo/`, porque o guia de custo mínimo manda editar o
`azure.yaml` ✅, e isso alteraria a cópia de referência. Crie uma pasta vazia **fora** deste
repositório e inicialize por lá, como o README oficial ensina ✅:

```bash
azd init -t azure-search-openai-demo
```

## Escolher o plano antes do `azd up`

| Objetivo | O que fazer |
| :-- | :-- |
| Só conhecer a aplicação, gastando o mínimo | Siga o [deploy_lowcost.md](../azure-search-openai-demo/docs/deploy_lowcost.md) na pasta de trabalho. Fica **sem** semantic ranker |
| Fazer o projeto (comparar com e sem semantic ranker) | Mantenha o AI Search num plano pago (Basic ou maior), faça a comparação de uma vez e apague tudo |

Depois:

```bash
azd up
```

## Recriar o ambiente

Na pasta de trabalho, `azd up` de novo. Ele provisiona a infraestrutura e indexa os arquivos da pasta
`data/`. ✅

## Apagar tudo

Na pasta de trabalho:

```bash
azd down --purge
```
