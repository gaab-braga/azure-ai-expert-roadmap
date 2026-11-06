# Módulo 04 — Infraestrutura corporativa em Bicep (rede isolada)

> Esta página é o módulo inteiro. Siga as etapas de 1 a 9, nesta ordem, sem pular.
> Como estudar: [COMO-ESTUDAR.md](../COMO-ESTUDAR.md) · Seu progresso: [PROGRESSO.md](../PROGRESSO.md)

**Legenda:** ✅ provado em fonte oficial · 🔶 hipótese · ❓ em aberto

---

## 1. Visão geral

**Objetivo:** subir o workspace inteiro **por código**, sem acesso público, com saída de rede só para
destinos aprovados, e entender como uma empresa separa experimentação (*inner loop*) de produção
(*outer loop*).

**Repositório oficial:** `mlops-v2` (licença MIT), em [mlops-v2/](mlops-v2/). É o acelerador
corporativo da Microsoft. O clone traz **documentação e o script de bootstrap**, não o código de
infraestrutura: esse vem de outros dois repositórios (`mlops-templates` e `mlops-project-template`),
que o guia manda copiar para a sua organização no GitHub. ✅

**Questões oficiais:** o curso AI-300T00 não tem um módulo do Learn só de IaC, então o quiz deste
módulo é próprio. ✅ (catálogo do Learn)

**Habilidades do exame cobertas:**
- Deploy Machine Learning workspaces and resources by using Bicep and Azure CLI
- Restrict network access to Machine Learning workspaces
- Implement network security and private networking configurations (Foundry)
- Automate resource provisioning by using GitHub Actions workflows

**Tempo e custo — atenção:**
- O cluster padrão do acelerador usa `STANDARD_D16S_V3` e pode precisar de até **64 vCPUs** de cota
  "Standard DSv3 Family". ✅ O SKU é configurável (`aml_compute_sku`) ✅: numa conta de estudo, troque
  por um menor antes de rodar.
- A rede virtual gerenciada só é criada quando surge a **primeira compute**, e isso pode levar cerca
  de **30 minutos**. ✅
- Regras de saída por **FQDN** usam **Azure Firewall**, que tem custo próprio. ✅
- Destruir o ambiente do acelerador leva de 9 a 12 minutos. ✅

---

## 2. Pré-teste

Responda o [quiz.md](quiz.md) **sem consultar** e anote a nota no [PROGRESSO.md](../PROGRESSO.md).

---

## 3. Preparar o ambiente

```bash
python scripts/preparar_modulos.py 04
```

Depois siga o [apoio/README.md](apoio/README.md): Bicep CLI, como conferir a cota de vCPU e se vale
rodar o acelerador completo.

---

## 4. Estudar (documentação oficial do acelerador + leituras)

| # | Estudar | O que observar | Checagem de memória |
| :-- | :-- | :-- | :-- |
| 1 | [Arquitetura](mlops-v2/documentation/architecture/README.md) e [ML clássico](mlops-v2/documentation/architecture/classical.md) | Os blocos da arquitetura, principalmente o 3 (*inner loop*) e o 5 (*outer loop*) ✅ | Quem faz o quê em cada loop? |
| 2 | [Estrutura dos repositórios](mlops-v2/documentation/structure/README.md) | O modelo de 3 repositórios e as opções do `sparse_checkout.sh` (bicep/terraform, github/azure devops, classical/cv/nlp) | Por que separar templates do projeto? |
| 3 | [Guia de deploy com GitHub Actions](mlops-v2/documentation/deployguides/deployguide_gha.md) | Arquivos `config-infra-dev.yml` e `config-infra-prod.yml`; a opção de private endpoints; o workflow que destrói tudo | O que muda entre dev e prod? |
| 4 | [bicep-ref-workspaces.md](leituras/bicep-ref-workspaces.md) | As propriedades `publicNetworkAccess`, `managedNetwork.isolationMode` e `managedNetworkKind` | Qual propriedade isola o tráfego de saída? |
| 5 | [avm-ml-workspace.main.bicep](leituras/avm-ml-workspace.main.bicep) | O valor padrão de `publicNetworkAccess` e as regras de saída (`outboundRules`) | Qual é o padrão do módulo AVM? |
| 6 | [how-to-managed-network.md](leituras/how-to-managed-network.md) | Os 3 modos de isolamento e os 3 tipos de regra de saída | Que tipo de regra gera custo extra? |
| 7 | [how-to-configure-private-link.md](leituras/how-to-configure-private-link.md) | Private endpoint + zonas de DNS privado | Que zonas de DNS o workspace usa? |

**Executar o acelerador é opcional.** Ele cria bastante coisa e depende de cota. Se a sua cota
permitir, siga o guia na sua organização do GitHub, com o SKU reduzido.

---

## 5. Ler (aprofundar)

| Leitura | Por quê |
| :-- | :-- |
| [bicep-ref-workspaces.md](leituras/bicep-ref-workspaces.md) · [oficial](https://learn.microsoft.com/azure/templates/microsoft.machinelearningservices/workspaces) | Todas as propriedades do recurso workspace |
| [how-to-managed-network.md](leituras/how-to-managed-network.md) · [oficial](https://learn.microsoft.com/azure/machine-learning/how-to-managed-network?view=azureml-api-2) | Rede virtual gerenciada |
| [how-to-configure-private-link.md](leituras/how-to-configure-private-link.md) · [oficial](https://learn.microsoft.com/azure/machine-learning/how-to-configure-private-link?view=azureml-api-2) | Private endpoint do workspace |
| [avm-ml-workspace.README.md](leituras/avm-ml-workspace.README.md) · [oficial](https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/machine-learning-services/workspace) | Exemplos prontos do módulo AVM |
| `referencias/azureml-examples/cli/endpoints/online/managed/vnet/` | Endpoint online numa rede isolada |

---

## 6. Pós-teste

Refaça o [quiz.md](quiz.md) e a revisão intercalada que está no fim dele. Anote as notas no
[PROGRESSO.md](../PROGRESSO.md).

---

## 7. Projeto do zero

Enunciado, requisitos e rubrica: [projeto/README.md](projeto/README.md). Comece sem abrir as leituras
e registre cada consulta no [diario.md](diario.md).

---

## 8. Explicar

Escreva a seção "Como funciona" do [projeto/README.md](projeto/README.md) com um desenho, em texto, de
por onde o tráfego passa: o seu PC, o GitHub, o workspace, o storage, o Key Vault e a internet.

---

## 9. Fechar o módulo

- [ ] Apague os grupos de recursos (veja [apoio/README.md](apoio/README.md#apagar-tudo))
- [ ] Evidências em [evidencias/](evidencias/), incluindo o **teste negativo**
- [ ] Projeto aprovado na rubrica e nenhum 🔶 pendente neste módulo
- [ ] Commit e push · [PROGRESSO.md](../PROGRESSO.md) com as datas de revisão
