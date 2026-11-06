# Apoio — Módulo 04

Arquivos **nossos**, que complementam a documentação oficial sem alterá-la.

## Pré-requisitos

- Azure CLI com Bicep:

    ```bash
    az bicep install
    ```

- Extensão **Bicep** no VS Code, que valida e autocompleta os arquivos `.bicep`.
- Para o seu projeto, um repositório **seu** no GitHub (pode ser este portfólio).

## Conferir a cota antes de rodar o acelerador

O cluster padrão do `mlops-v2` usa `STANDARD_D16S_V3` e pode precisar de até 64 vCPUs da família
DSv3. ✅ Para ver a sua cota numa região:

```bash
az vm list-usage --location eastus --query "[?contains(name.value,'DSv3')].{familia:name.localValue, uso:currentValue, limite:limit}" -o table
```

🔶 O comando é padrão da Azure CLI, mas não foi testado nesta assinatura. Se o limite for baixo,
troque o `aml_compute_sku` nos arquivos `config-infra-*.yml` por um SKU menor, como o próprio guia
permite. ✅

## Onde fazer o acelerador (opcional)

O guia manda fazer *fork* do `mlops-templates`, gerar um repositório a partir do
`mlops-project-template` e rodar o `sparse_checkout.sh` para criar o **seu** projeto. ✅ Tudo isso
acontece na sua organização do GitHub. A cópia em `mlops-v2/` fica só para leitura.

## Recriar o ambiente

- **Acelerador:** rode de novo o workflow de infraestrutura do repositório gerado.
- **Seu projeto:** `az deployment group create` com o seu `main.bicep`. Esse é justamente o valor da
  IaC: recriar é um comando.

## Apagar tudo

- **Acelerador:** o guia tem um workflow de destruição, um para cada branch ✅. Leva de 9 a 12 minutos:

    ```bash
    gh workflow run tf-gha-deploy-infra.yml --ref dev -f action=destroy
    ```

    ```bash
    gh workflow run tf-gha-deploy-infra.yml --ref main -f action=destroy
    ```

    Repare no prefixo `tf-`: o caminho do guia com GitHub Actions usa **Terraform**. Já o seu
    projeto usa **Bicep**. Comparar os dois é um bom exercício.
- **Seu projeto:** `bash ../../scripts/apagar-ambiente.sh <grupo>`.
