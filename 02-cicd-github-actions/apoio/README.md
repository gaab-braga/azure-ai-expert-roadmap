# Apoio — Módulo 02

Arquivos **nossos**, que complementam os labs oficiais sem alterá-los.

## Pré-requisitos

- Assinatura do Azure com alerta de orçamento, e uma conta no GitHub.
- Labs 01 a 05: Azure Cloud Shell (Bash).
- Labs 06 e 07: um repositório **seu**, criado a partir do template (botão **Use this template**
  na página do `mslearn-mlops` no GitHub), como os labs mandam. ✅ É nele que você edita workflows:
  nunca na cópia de referência deste módulo.

## Usar no Cloud Shell a mesma versão do lab que está aqui

Logo depois do `git clone` que o lab manda fazer:

```bash
cd mslearn-mlops && git checkout 87482bc76b9ffa665e6ce6b76746d31e7a164b01 && cd ..
```

## Recriar o ambiente

Cada lab já começa rodando o script oficial `infra/setup.sh`. ✅ Recriar é só rodar de novo:

```bash
cd mslearn-mlops/infra && ./setup.sh
```

Atenção: o script sorteia a **região** e um **sufixo** no nome, então cada execução cria um grupo
novo (`rg-ai300-l<sufixo>`). ✅ Para listar os que existem:

```bash
az group list --query "[?starts_with(name,'rg-ai300')].name" -o tsv
```

## Apagar tudo

1. Apague cada grupo `rg-ai300-*` (inclusive os de dev, prod e registry do lab 05):

    ```bash
    bash ../../scripts/apagar-ambiente.sh <nome-do-grupo>
    ```

2. Apague o service principal criado no lab 06. Descubra o `appId` com
   `az ad sp list --display-name "<nome-que-você-deu>" --query "[].appId" -o tsv` e depois rode
   `az ad sp delete --id <appId>`.
3. Apague o repositório de teste criado a partir do template, como o lab 06 orienta.
