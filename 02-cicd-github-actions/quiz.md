# Quiz — Módulo 02 (ciclo de vida e CI/CD)

Questões escritas para este curso a partir da documentação oficial (a fonte está em cada gabarito).
As **questões oficiais** do Learn estão linkadas na etapa 4 do [README](README.md). Responda sem consultar.

---

**02-Q1.** No workflow do GitHub Actions que faz login no Azure por OIDC, qual permissão o job precisa ter?

<details><summary>Gabarito</summary>

`permissions: id-token: write`. Ela permite ao job pedir o token OIDC ao GitHub.
Fonte: [connect-from-azure-openid-connect.md](leituras/connect-from-azure-openid-connect.md).
</details>

---

**02-Q2.** Com OIDC, o `azure/login` recebe `AZURE_CLIENT_ID`, `AZURE_TENANT_ID` e
`AZURE_SUBSCRIPTION_ID`. Algum deles é senha? Onde fica a confiança?

<details><summary>Gabarito</summary>

**Nenhum é senha.** São identificadores. A confiança está na **credencial de identidade federada**,
configurada num app do Entra ID ou numa managed identity atribuída pelo usuário, que aceita tokens
emitidos pelo GitHub para o **seu** repositório. Compare com o lab 06, que guarda um segredo JSON
(`AZURE_CREDENTIALS`).
Fonte: [connect-from-azure-openid-connect.md](leituras/connect-from-azure-openid-connect.md); lab [06](mslearn-mlops/docs/06-automate-model-training.md).
</details>

---

**02-Q3.** O que faz a flag `--all-traffic` em `az ml online-deployment create`?

<details><summary>Gabarito</summary>

Manda **100% do tráfego** do endpoint para o deployment recém-criado.
Fonte: [how-to-safely-rollout-online-endpoints.md](leituras/how-to-safely-rollout-online-endpoints.md).
</details>

---

**02-Q4.** Você quer validar o deployment `green` com tráfego real **sem afetar** os clientes. Que
recurso usa, e quais são os limites dele?

<details><summary>Gabarito</summary>

**Espelhamento de tráfego** (*mirror traffic*, também chamado de *shadowing*): uma cópia de parte do
tráfego vai para o `green`. Limites:
- no máximo **50%** do tráfego;
- só **um** deployment por endpoint recebe o espelho;
- não funciona em endpoints Kubernetes;
- exige CLI `ml` 2.4.0 ou mais nova.

Fonte: [how-to-safely-rollout-online-endpoints.md](leituras/how-to-safely-rollout-online-endpoints.md), "Test the deployment with mirrored traffic".
</details>

---

**02-Q5.** Qual é o **primeiro** passo para monitorar um modelo em produção no Azure ML? E se o modelo
estiver num endpoint em lote (batch)?

<details><summary>Gabarito</summary>

**Coletar os dados de inferência de produção.** Em endpoint online, isso se faz com a coleta de dados
do Azure ML. Em endpoint batch, ou fora do Azure ML, **a coleta é responsabilidade sua**.
Fonte: [concept-model-monitoring.md](leituras/concept-model-monitoring.md).
</details>

---

**02-Q6.** Cite os sinais de monitoramento embutidos para dados tabulares.

<details><summary>Gabarito</summary>

Data drift, prediction drift, data quality, feature attribution drift e model performance.
Fonte: [concept-model-monitoring.md](leituras/concept-model-monitoring.md).
</details>

---

**02-Q7.** No lab 07, como o treino em produção é disparado?

<details><summary>Gabarito</summary>

Por um **comentário** `/train-prod` no PR: o workflow `train-prod.yml` usa o gatilho `issue_comment`
e roda no *environment* `prod` do GitHub.
Fonte: `mslearn-mlops/.github/workflows/train-prod.yml`.
</details>

---

## Revisão intercalada (pós-teste)

Refaça, de memória, as questões **01-Q1**, **01-Q4** e **01-Q5** do [quiz do módulo 01](../01-aml-cli-foundation/quiz.md).
