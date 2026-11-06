# Apoio — Módulo 03

Arquivos **nossos**, que complementam os labs oficiais sem alterá-los.

## Pré-requisitos

O lab 00 lista o que instalar na sua máquina: VS Code, Python 3.9+, Git, Azure CLI e Azure Developer
CLI (azd). ✅ Depois:

```bash
az login
```

```bash
azd auth login
```

## Onde fazer os labs

O lab 01 manda criar um repositório **seu** a partir do template (**Use this template**). ✅ Clone
esse repositório **fora** desta pasta (por exemplo, numa pasta `labs-trabalho/` ao lado do
`azure-ai-expert-roadmap`). A cópia em `mslearn-genaiops/` fica só para leitura.

Para o seu repositório ficar na mesma versão da referência, confira o commit do template com
`git log -1`. O commit fixado está no [repos-oficiais.lock.json](../../repos-oficiais.lock.json). 🔶 Um
repositório criado por template começa com histórico novo, então a comparação é pelo conteúdo, não
pelo número do commit.

## Recriar o ambiente

Na pasta do seu repositório de trabalho:

```bash
azd up
```

Se você apagou tudo com `azd down`, rodar o `azd up` de novo recria os recursos a partir do Bicep da
pasta `infra/`. ✅ Antes do lab 04, o lab manda instalar a extensão `azure.ai.agents` do azd e
conferir a cota do modelo.

## Apagar tudo

1. Na pasta do repositório de trabalho (o lab 04 usa a mesma forma):

    ```bash
    azd down --purge --force
    ```

    O `--purge` apaga de vez os recursos que o Azure guarda numa "lixeira" por um tempo, e com isso
    libera os nomes e a cota.

2. Apague o service principal ou app do lab 04 com `az ad sp delete --id <appId>`.
3. Apague o repositório de teste no GitHub, se não for mais usar.
