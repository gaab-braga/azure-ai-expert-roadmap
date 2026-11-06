# Quiz — Módulo 04 (IaC e rede isolada)

Questões escritas para este curso a partir da documentação oficial (a fonte está em cada gabarito).
Responda sem consultar.

---

**04-Q1.** No módulo Bicep oficial (AVM) do workspace de ML, qual é o valor padrão de
`publicNetworkAccess`?

<details><summary>Gabarito</summary>

`'Disabled'`. Quem usa o módulo sem mudar nada já começa sem acesso público.
Fonte: [avm-ml-workspace.main.bicep](leituras/avm-ml-workspace.main.bicep), parâmetro `publicNetworkAccess`.
</details>

---

**04-Q2.** Quais são os valores de `managedNetwork.isolationMode` no Bicep? E como o modo "só saída
aprovada" se escreve no YAML da CLI?

<details><summary>Gabarito</summary>

No Bicep: `'AllowInternetOutbound'`, `'AllowOnlyApprovedOutbound'` e `'Disabled'`. No YAML da CLI:
`allow_only_approved_outbound`. É o mesmo modo com outra grafia.
Fonte: [avm-ml-workspace.main.bicep](leituras/avm-ml-workspace.main.bicep); [how-to-managed-network.md](leituras/how-to-managed-network.md).
</details>

---

**04-Q3.** Para que serve `managedNetworkKind`? Dá para desfazer a mudança?

<details><summary>Gabarito</summary>

Escolhe a **versão** da rede gerenciada, `V1` ou `V2`, sendo que a V2 dá controle de acesso mais
granular. A troca de V1 para V2 **não tem volta**. Não é essa propriedade que isola o tráfego: quem
isola é o `isolationMode`.
Fonte: [bicep-ref-workspaces.md](leituras/bicep-ref-workspaces.md).
</details>

---

**04-Q4.** Quais são os 3 tipos de regra de saída da rede gerenciada, e quais deles só valem no modo
`allow_only_approved_outbound`?

<details><summary>Gabarito</summary>

`service_tag`, `fqdn` e `private_endpoint`. As de **service tag** e **FQDN** só valem em
`allow_only_approved_outbound`.
Fonte: [how-to-managed-network.md](leituras/how-to-managed-network.md).
</details>

---

**04-Q5.** Você liberou o PyPI com uma regra **FQDN**. Que custo novo aparece na fatura?

<details><summary>Gabarito</summary>

**Azure Firewall**: as regras FQDN são implementadas com ele.
Fonte: [how-to-managed-network.md](leituras/how-to-managed-network.md).
</details>

---

**04-Q6.** Você criou o workspace com rede gerenciada e a rede ainda não existe. Por quê? Quanto
tempo pode levar?

<details><summary>Gabarito</summary>

A criação da rede é **adiada** até surgir a primeira compute, ou até você mandar provisioná-la
manualmente. Com a criação automática, a primeira compute pode levar cerca de **30 minutos**, porque
a rede é criada junto.
Fonte: [how-to-managed-network.md](leituras/how-to-managed-network.md).
</details>

---

**04-Q7.** Que zonas de DNS privado o private endpoint de um workspace do Azure ML usa?

<details><summary>Gabarito</summary>

`privatelink.api.azureml.ms` e `privatelink.notebooks.azure.net`.
Fonte: [how-to-configure-private-link.md](leituras/how-to-configure-private-link.md).
</details>

---

**04-Q8.** O Key Vault do workspace está com acesso público desligado. Que opção precisa ficar
ligada nele?

<details><summary>Gabarito</summary>

**Allow trusted Microsoft services to bypass this firewall** (permitir que serviços confiáveis da
Microsoft passem pelo firewall).
Fonte: [how-to-managed-network.md](leituras/how-to-managed-network.md).
</details>

---

## Revisão intercalada (pós-teste)

Refaça, de memória: **02-Q2** ([módulo 02](../02-cicd-github-actions/quiz.md)), **03-Q1**
([módulo 03](../03-genaiops-ai-foundry/quiz.md)) e **01-Q6** ([módulo 01](../01-aml-cli-foundation/quiz.md)).
