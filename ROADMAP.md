# ROADMAP — do YAML local ao RAG corporativo

Guia tático do portfólio. Cada fase traz: **o que o exame cobra**, **os desafios de engenharia**,
**o que entregar** e **como saber que terminou**.

**Legenda:** ✅ provado numa fonte oficial salva em `docs_oficiais/` (o caminho vem ao lado) ·
🔶 hipótese, ou fonte não oficial ainda não conferida · ❓ em aberto, precisa de teste no Azure.

Base: o relatório "Plano de Estudos AI-300" (documento pessoal, fora do repositório), conferido
contra o guia oficial do exame e a documentação do Microsoft Learn baixada em 2026-11-06.

---

## 0. O exame em uma tabela

Fonte: `docs_oficiais/00-exame-ai-300/study-guide-ai-300.md` (guia oficial, atualizado em 2026-10-15). ✅

| Domínio do exame | Peso | Fases deste repositório |
| :-- | :-- | :-- |
| Projetar e implementar infraestrutura de MLOps | 15–20% | 01, 02, 04 |
| Ciclo de vida e operação de modelos de ML | 25–30% | 01, 02 |
| Projetar e implementar infraestrutura de GenAIOps | 20–25% | 03, 04 |
| Garantia de qualidade e observabilidade de IA generativa | 10–15% | 03, 05 |
| Otimizar sistemas de IA generativa e desempenho dos modelos | 10–15% | 05 |

- Nota mínima de aprovação: 700. ✅
- Os pesos do relatório (que citava um site de simulados) **batem** com o guia oficial. ✅
- Somando os três domínios de IA generativa, dá **40% a 55%** da prova. ✅ (conta feita sobre os pesos acima)

---

## 1. Correções ao relatório de origem

Pontos em que as fontes oficiais divergem do relatório. Mantive a versão oficial.

| # | O relatório diz | A fonte oficial diz | Status |
| :-- | :-- | :-- | :-- |
| 1 | `managedNetworkKind` "habilita a rede virtual gerenciada". | `managedNetworkKind` só escolhe a **versão** da rede gerenciada (`V1` ou `V2`); a troca V1→V2 **não tem volta**. Quem isola o tráfego é `isolationMode`. (`04-bicep-rede-isolada/bicep-ref-workspaces.md`) | ✅ |
| 2 | O valor é `allow_only_approved_outbound`. | Esse é o nome no **YAML da CLI**. No **Bicep** o valor é `'AllowOnlyApprovedOutbound'`; as opções são `'AllowInternetOutbound'`, `'AllowOnlyApprovedOutbound'` e `'Disabled'`. (`avm-ml-workspace.main.bicep`, `how-to-managed-network.md`) | ✅ |
| 3 | O RRF aplica uma "penalidade estrita de ranker" e também cuida da ordenação semântica cruzada. | O RRF soma `1/(rank + k)` de cada lista. `k` é uma **constante** (a doc cita 60) e não tem relação com o `k` de vizinhos mais próximos da busca vetorial. O **semantic ranker roda depois** do RRF e devolve uma nota separada (`@search.rerankerScore`). (`05-rag-busca-hibrida/hybrid-search-ranking.md`) | ✅ |
| 4 | "Azure AI Foundry" com *hubs*. | O guia do exame fala em **Microsoft Foundry**. A documentação de *hubs* aparece como "classic". | ✅ nome · ❓ se o exame ainda cobra hubs |
| 5 | São seis repositórios em seis fases. | Este portfólio tem **cinco** pastas. O `azureml-examples` fica como material de consulta em todas as fases (ver seção 8). | decisão de projeto |

---

## 2. Fase 01 — `01-aml-cli-foundation` (gramática da CLI v2)

**Repositório-fonte:** `mslearn-aml-cli` · **Consulta:** `azureml-examples/cli/jobs`

**O que o exame cobra:** criar workspace, datastores, computes, data assets, environments e
componentes; rodar scripts de treino; ajustar hiperparâmetros automaticamente; montar pipelines de
treino; rastrear experimentos com MLflow; comparar jobs.

### Desafios de engenharia

1. **Escrever YAML validado pelo schema oficial.** A primeira linha de cada arquivo aponta para
   `https://azuremlschemas.azureedge.net/latest/<tipo>.schema.json`. Com essa linha, o VS Code
   passa a validar e autocompletar o arquivo. ✅ (`01-schemas-cli-v2/reference-yaml-job-pipeline.md`)
2. **Saber o que cabe num pipeline.** Hoje um pipeline só aceita *command jobs* e *sweep jobs* como
   etapas. ✅ (mesmo arquivo)
3. **Montar o `search_space` de um sweep.** O schema aceita as distribuições `choice`, `randint`,
   `uniform`, `quniform`, `loguniform`, `normal`, `qnormal` e `lognormal`, e as estratégias de
   amostragem `random`, `grid` e `bayesian`. ✅ (`01-schemas-cli-v2/sweepJob.schema.json`)
4. **Ligar saída de um passo à entrada do próximo** (`${{parent.jobs.<passo>.outputs.<saida>}}`). 🔶 sintaxe a conferir no schema/exemplos
5. **MLflow sem código extra:** `mlflow.autolog()` no script e métricas aparecendo no estúdio. 🔶

### Entregáveis

- [ ] `command-job.yml` treinando um modelo simples, com métricas no MLflow
- [ ] `sweep-job.yml` com pelo menos 2 hiperparâmetros e política de parada antecipada
- [ ] `pipeline-job.yml` com 2+ etapas (preparar dados → treinar → registrar)
- [ ] `README.md` da fase com o comando exato para rodar cada um

**Pronto quando:** os três jobs rodam com `az ml job create --file ... --stream` sem erro de schema
e o modelo aparece registrado no workspace.

---

## 3. Fase 02 — `02-cicd-github-actions` (o GitHub roda por você)

**Repositório-fonte:** `mslearn-mlops`

**O que o exame cobra:** integrar o GitHub ao Azure ML com acesso seguro; automatizar recursos com
workflows; registrar e versionar modelos MLflow; implantar endpoints online/batch; fazer rollout
progressivo e rollback; detectar *data drift* e disparar retreino.

### Desafios de engenharia

1. **Login sem senha (OIDC).** ✅ (`02-cicd-oidc/connect-from-azure-openid-connect.md`)
   - Criar uma *federated identity credential* num app do Entra ID **ou** numa managed identity
     atribuída pelo usuário, confiando no seu repositório do GitHub.
   - No workflow, liberar a emissão do token: `permissions: id-token: write`.
   - Passar ao `azure/login` três secrets: `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`,
     `AZURE_SUBSCRIPTION_ID`. Nenhum deles é senha; a segurança está na federação.
2. **Menor privilégio no RBAC.** Qual papel a identidade do GitHub precisa no grupo de recursos?
   O relatório sugere *Contributor*; a doc baixada não confirma. 🔶 Testar com um papel mais
   restrito e registrar o resultado.
3. **Promoção de modelo só via repositório:** registrar → implantar em endpoint → teste de fumaça →
   trocar o tráfego aos poucos (ex.: 10% → 100%) → rollback se falhar. 🔶 desenho a validar
4. **Gatilho de retreino** quando o monitor de drift passar do limite. ❓

### Entregáveis

- [ ] Workflow `train.yml` que roda o pipeline da fase 01 a cada `push` na `main`
- [ ] Workflow `deploy.yml` com aprovação manual (GitHub *environments*) antes de produção
- [ ] Endpoint online com **dois deployments** (blue/green) e divisão de tráfego
- [ ] Documento curto: "quais secrets existem, para que servem e qual papel RBAC cada um tem"

**Pronto quando:** um `push` treina, registra e implanta sem nenhum comando manual, e nenhum
segredo aparece no código.

---

## 4. Fase 03 — `03-genaiops-ai-foundry` (do modelo clássico ao LLM)

**Repositório-fonte:** `mslearn-genaiops` (o clone local já tem `docs/04-automated-evaluation.md`)

**O que o exame cobra:** criar recursos e projetos no Foundry; managed identity e RBAC; implantar
modelos (serverless ou compute gerenciado, PTU para alto volume); versionar prompts no Git;
criar datasets de teste; métricas de qualidade e de segurança; avaliação automatizada; monitorar
latência, custo de tokens e traces.

### Desafios de engenharia

1. **Entender Groundedness de verdade.** ✅ (`03-avaliacao-groundedness/rag-evaluators.md`)
   - Nota de **1 a 5**; limite padrão de aprovação = **3**; saída `pass`/`fail`.
   - Entradas: `response` e `context` (recomendado); `query` é opcional, mas melhora a nota.
   - Groundedness mede **precisão** (não inventar). Para medir **cobertura** (não esquecer nada),
     o par é *Response Completeness*, que exige uma resposta de referência (ground truth).
   - *Groundedness Pro* (preview) usa o Azure AI Content Safety e devolve só verdadeiro/falso.
2. **Prompt como código:** prompts em arquivo versionado, com variantes comparadas pela mesma
   avaliação. 🔶
3. **Avaliação no CI:** rodar a avaliação no GitHub Actions e **reprovar o PR** se Groundedness ou
   Relevance caírem abaixo do limite. 🔶 (há um lab oficial com esse tema, listado no msfthub — conteúdo não lido)
4. **Custo:** registrar tokens por requisição e comparar modelos por custo × qualidade. ❓

### Entregáveis

- [ ] Projeto Foundry criado por script (não pelo portal)
- [ ] Pasta `prompts/` com 2 variantes e um dataset de teste em JSONL (dados fictícios)
- [ ] Script de avaliação com Groundedness, Relevance e uma métrica de segurança
- [ ] Workflow que roda a avaliação e falha abaixo do limite

**Pronto quando:** mudar o prompt dispara a avaliação e o resultado decide se o PR passa.

---

## 5. Fase 04 — `04-enterprise-iac-bicep` (a fortaleza)

**Repositório-fonte:** `mlops-v2` · **Módulo oficial:** AVM `machine-learning-services/workspace`

**O que o exame cobra:** implantar workspaces e recursos com Bicep e Azure CLI; restringir o acesso
de rede ao workspace; segurança de rede e rede privada também no Foundry.

### Desafios de engenharia

1. **Desligar o acesso público.** `publicNetworkAccess: 'Disabled'`. No módulo AVM esse já é o
   **valor padrão**. ✅ (`04-bicep-rede-isolada/avm-ml-workspace.main.bicep`)
2. **Escolher o modo de saída da rede gerenciada** (`managedNetwork.isolationMode`). ✅
   - `AllowInternetOutbound`: os computes saem para a internet livremente.
   - `AllowOnlyApprovedOutbound`: só saem para destinos liberados (regras de FQDN, service tags,
     private endpoints). É o modo corporativo, e o `pip install` quebra até você liberar o PyPI.
   - Algumas regras de saída **só existem** em `AllowOnlyApprovedOutbound`. ✅ (comentários do módulo AVM)
3. **Isolar o tráfego com Private Endpoints + DNS privado.** Workspace, Storage, Key Vault e ACR
   ganham IP interno, e uma zona `privatelink.*` resolve o nome para esse IP. 🔶 lista exata de
   zonas a extrair de `how-to-managed-network.md`
4. **Nomes globais únicos.** Storage Account aceita 3–24 caracteres, só minúsculas e números.
   Padrão: `'st${uniqueString(resourceGroup().id)}'`. 🔶 regra conhecida, mas ainda sem fonte em `docs_oficiais/`
5. **Storage padrão do workspace:** não usar conta com namespace hierárquico (Data Lake Gen2) nem
   Premium. 🔶 fonte não oficial (open-exam-prep)
6. **Inner Loop × Outer Loop.** Inner = o cientista experimenta no workspace de dev. Outer = a
   esteira de MLOps empacota, valida e implanta. ✅ (`mlops-v2/documentation/architecture/classical.md`, clone local)
7. **`what-if` antes de tudo:** nunca implantar sem ver o diff da infraestrutura.

### Entregáveis

- [ ] `main.bicep` usando o módulo AVM, com `publicNetworkAccess: 'Disabled'`
- [ ] `isolationMode: 'AllowOnlyApprovedOutbound'` + regra de saída para o PyPI
- [ ] `dev.bicepparam` e `prod.bicepparam` (ambientes separados, sem IDs reais versionados)
- [ ] Workflow que roda `what-if` no PR e `deployment create` após aprovação
- [ ] Teste negativo: acessar o workspace por rede pública **deve falhar** (print da evidência)

**Pronto quando:** a infraestrutura inteira sobe de um grupo de recursos vazio só com o pipeline, e o
teste negativo prova que o acesso público está fechado.

---

## 6. Fase 05 — `05-advanced-rag-architecture` (RAG nível produção)

**Repositório-fonte:** `azure-search-openai-demo` (ainda não clonado aqui)

**O que o exame cobra:** ajustar limites de similaridade, tamanho dos chunks e estratégia de busca;
escolher e ajustar modelos de embedding; busca híbrida (semântica + palavra-chave); avaliar o RAG
com métricas de relevância e testes A/B; fine-tuning e dados sintéticos.

### Desafios de engenharia

1. **Busca híbrida.** Uma consulta de texto (BM25) e uma vetorial rodam em paralelo. A de texto acha
   códigos e termos exatos; a vetorial acha o mesmo sentido com outras palavras. ✅
   (`05-rag-busca-hibrida/hybrid-search-overview.md`)
2. **Como o RRF junta as listas.** ✅ (`05-rag-busca-hibrida/hybrid-search-ranking.md`)
   - Cada documento ganha `1/(rank + k)` em cada lista onde aparece, e as parcelas são somadas.
   - `k` é uma constante (a doc cita 60). Não confundir com o `k` de vizinhos da busca vetorial.
   - Peso por consulta vetorial: padrão `1.0`; `0.5` reduz a influência, `2.0` aumenta.
   - Exemplo: um documento em 1º lugar no BM25 e ausente no vetor recebe `1/61 ≈ 0,0164`. Um em 2º
     lugar nas duas listas recebe `2 × 1/62 ≈ 0,0323` e fica **acima**. O RRF premia consenso.
3. **Semantic ranker depois do RRF.** Ele reordena o topo e devolve `@search.rerankerScore`,
   separado de `@search.score`. ✅
4. **Fluxo ChatReadRetrieveRead:** (1) o LLM reescreve a pergunta usando o histórico, (2) roda a
   busca híbrida, (3) o LLM responde só com o contexto recuperado. ❓ arquivo e nomes a conferir no
   repositório atual
5. **Chunking:** chunk pequeno perde contexto; chunk grande gasta tokens e dilui a atenção do modelo.
   Medir, não chutar. 🔶
6. **RAG ou fine-tuning?** Fine-tuning muda o *comportamento* do modelo; RAG muda o *conhecimento*
   disponível. Fine-tuning custa treino, hospedagem e retreino. 🔶 confirmar com a doc oficial

### Entregáveis

- [ ] Índice no AI Search com campo vetorial + campos de texto + configuração semântica
- [ ] Notebook/script comparando busca **só texto × só vetor × híbrida × híbrida + semantic**
- [ ] Mesmo dataset de perguntas avaliado com Groundedness/Relevance em cada configuração
- [ ] Tabela de resultados (qualidade × latência × tokens) com a conclusão

**Pronto quando:** a tabela mostra, com números, qual configuração vence e por quê.

---

## 7. Avaliação de fontes externas

### msfthub.com/certs/azure/ai-300 — **Veredito: descartar como material de estudo, manter só como índice de links**

Lido em 2026-11-06 (página principal + página de labs + guia genérico de preparação).

| Critério | O que existe lá |
| :-- | :-- |
| Código (YAML, Bicep, Python) | **Nenhum.** |
| Simulados | **Nenhum próprio.** Linka a avaliação prática oficial (o próprio site diz que é mais fácil que a prova) e um site de terceiros. |
| Casos de borda / troubleshooting | **Nenhum.** Só títulos de labs. |
| OIDC, RRF, busca híbrida | Não aparecem. |
| Pesos dos domínios | Não mostra; remete ao guia oficial. |
| Autoria | Site comunitário ("Microsoft Certification Hub"), sem data de atualização visível. |

**Por quê:** é um agregador de cerca de 300–400 palavras. Tudo que tem valor nele é link para o
Microsoft Learn, que já está em `docs_oficiais/`. O único ganho real é a **página de labs**: uma lista
de ~50 exercícios do Learn e 12 labs do GitHub (`mslearn-mlops`, `mslearn-genaiops`), útil como
checklist. Exemplos de títulos: "Create a secure workspace with a managed virtual network",
"Automate AI evaluations with Microsoft Foundry and GitHub Actions". Usar como checklist, nunca como
fonte de verdade.

---

## 8. `azureml-examples` — a enciclopédia (todas as fases)

Não vira pasta. Consulte quando a fase pedir algo fora do básico:

- Fase 01: `cli/jobs/` (sweep, pipelines com componentes, MLflow com runs aninhados)
- Fase 01–02: treino distribuído (PyTorch, DeepSpeed), que o exame cobra em "Manage distributed training"
- Fase 02: `cli/endpoints/` (online, batch, divisão de tráfego)

🔶 Caminhos de pasta citados de memória/relatório; conferir no repositório antes de usar.

---

## 9. Ordem de execução e próximos passos

1. Fase 01 inteira antes de abrir a 02: sem YAML fluente, o CI só automatiza erro.
2. Fases 02 e 03 podem andar em paralelo depois da 01.
3. Fase 04 depois da 02 (reaproveita o login OIDC).
4. Fase 05 por último (reaproveita a avaliação da 03 e a rede da 04).

Em aberto (❓) para resolver ao longo do caminho:

- O exame ainda cobra *hubs* do Foundry (classic) ou só o modelo novo de projetos?
- Papel RBAC mínimo para a identidade do GitHub em cada fase.
- Nome atual do arquivo da estratégia ChatReadRetrieveRead no `azure-search-openai-demo`.
