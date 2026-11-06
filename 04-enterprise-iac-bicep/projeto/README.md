# Projeto do zero — Módulo 04

> **Status:** ⏳ não iniciado

## Enunciado

Escreva o **seu** Bicep para um workspace de ML corporativo, sem o acelerador e usando o módulo
oficial AVM como base. Ele deve subir do zero por pipeline, sem acesso público e com saída de rede
controlada.

## Requisitos

- [ ] `main.bicep` usando o módulo AVM `machine-learning-services/workspace`
- [ ] `publicNetworkAccess: 'Disabled'` declarado de forma **explícita**, mesmo sendo o padrão
- [ ] `managedNetwork.isolationMode: 'AllowOnlyApprovedOutbound'` + uma regra de saída para o PyPI.
      Explique no README o custo dessa escolha (FQDN usa Azure Firewall)
- [ ] Private endpoint do workspace + zonas `privatelink.api.azureml.ms` e `privatelink.notebooks.azure.net`
- [ ] Nomes globais únicos (por exemplo, com `uniqueString(resourceGroup().id)`). 🔶 As regras de nome
      da Storage Account ainda não estão nas leituras: confirme na doc antes de usar
- [ ] `dev.bicepparam` e `prod.bicepparam`, sem nenhum ID real versionado
- [ ] Workflow: `az deployment group what-if` no PR e `az deployment group create` depois da
      aprovação, com login por OIDC (reaproveite o do módulo 02)
- [ ] **Teste negativo:** acessar o workspace pela internet pública **tem que falhar**. Guarde a
      evidência

## Rubrica

| Critério | 0 | 1 | 2 |
| :-- | :-- | :-- | :-- |
| IaC | Portal ou script solto | Bicep sem parâmetros por ambiente | AVM + bicepparam dev/prod |
| Rede | Acesso público | Private endpoint sem DNS | PE + DNS + saída controlada |
| Pipeline | Deploy manual | Só deploy | what-if no PR + deploy aprovado |
| Prova | Nenhuma | "Funciona" sem teste negativo | Teste negativo com evidência |
| Explicação | Ausente | Lista de recursos | Desenho do tráfego + custo das escolhas |

**Aprovado:** nenhum critério com 0 e pelo menos 8 pontos de 10.

## Como funciona

*(Etapa 8.)*

## Evidências

*(Links para [../evidencias/](../evidencias/).)*
