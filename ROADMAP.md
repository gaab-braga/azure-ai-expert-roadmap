# ROADMAP — visão geral do curso

O passo a passo de cada módulo está na **página do módulo**. Este arquivo guarda o que vale para o
curso inteiro: o mapa do exame, as correções feitas ao relatório de origem, a avaliação de fontes e
a ordem dos módulos.

**Legenda:** ✅ provado em fonte oficial · 🔶 hipótese · ❓ em aberto

---

## 1. O exame e os módulos

Fonte: guia oficial do exame, em [00-preparacao/leituras/study-guide-ai-300.md](00-preparacao/leituras/study-guide-ai-300.md)
([online](https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-300)),
atualizado em 2026-10-15. ✅

| Domínio do exame | Peso | Módulos |
| :-- | :-- | :-- |
| Projetar e implementar infraestrutura de MLOps | 15–20% | 01, 02, 04 |
| Ciclo de vida e operação de modelos de ML | 25–30% | 01, 02 |
| Projetar e implementar infraestrutura de GenAIOps | 20–25% | 03, 04 |
| Garantia de qualidade e observabilidade de IA generativa | 10–15% | 03, 05 |
| Otimizar sistemas de IA generativa e desempenho dos modelos | 10–15% | 03 (fine-tuning), 05 (RAG) |

- Nota mínima de aprovação: 700. ✅
- Os três domínios de IA generativa somam de **40% a 55%** da prova (conta feita sobre os pesos acima).
- O curso oficial **AI-300T00** tem 2 trilhas e 14 módulos no Learn, todos com questões de verificação.
  Elas estão linkadas nos módulos 02 e 03 deste curso. ✅ (catálogo do Learn)

## 2. Os módulos

| Módulo | Repositório oficial (referência intacta) | Projeto do zero |
| :-- | :-- | :-- |
| [00 Preparação](00-preparacao/README.md) | — | Conta, orçamento, ferramentas, simulado inicial |
| [01 CLI v2](01-aml-cli-foundation/README.md) | `mslearn-aml-cli` | Fluxo completo só com YAML/CLI, com outro dataset |
| [02 CI/CD](02-cicd-github-actions/README.md) | `mslearn-mlops` | Esteira com OIDC, blue/green e drift |
| [03 GenAIOps](03-genaiops-ai-foundry/README.md) | `mslearn-genaiops` | Agente próprio com portão de avaliação no PR |
| [04 IaC/Bicep](04-enterprise-iac-bicep/README.md) | `mlops-v2` | Workspace em Bicep sem acesso público, com teste negativo |
| [05 RAG](05-advanced-rag-architecture/README.md) | `azure-search-openai-demo` | Comparação de 4 configurações de busca com números |

O `azureml-examples` fica em `referencias/` e serve de consulta nos módulos 01, 02 e 04.

**Ordem:** um módulo de cada vez, de 00 a 05. O próximo só abre quando o projeto do atual passar na
rubrica (ver [COMO-ESTUDAR.md](COMO-ESTUDAR.md)).

## 3. Correções ao relatório de origem

Pontos em que as fontes oficiais divergem do relatório "Plano de Estudos AI-300". Vale a versão oficial.

| # | O relatório diz | A fonte oficial diz | Fonte |
| :-- | :-- | :-- | :-- |
| 1 | `managedNetworkKind` habilita a rede gerenciada | Só escolhe a versão (`V1` ou `V2`), e a troca V1→V2 não tem volta. Quem isola é o `isolationMode` ✅ | módulo 04, `bicep-ref-workspaces.md` |
| 2 | O valor é `allow_only_approved_outbound` | Essa é a grafia do YAML da CLI. No Bicep é `'AllowOnlyApprovedOutbound'` ✅ | módulo 04 |
| 3 | O RRF aplica uma "penalidade estrita" e faz a ordenação semântica | O RRF soma `1/(rank+k)`, com `k` constante (cerca de 60). O semantic ranker roda **depois** e tem nota própria ✅ | módulo 05 |
| 4 | "Azure AI Foundry" com *hubs* | O guia do exame fala em **Microsoft Foundry**; a documentação de hubs aparece como "classic" ✅ | guia do exame |
| 5 | Seis repositórios em seis fases | Cinco módulos + `azureml-examples` como referência | decisão de projeto |
| 6 | O `mlops-v2` é o caminho do Bicep | O guia com GitHub Actions usa **Terraform** (`tf-gha-deploy-infra.yml`). Ele roda o cluster padrão em `STANDARD_D16S_V3` (até 64 vCPUs de cota), mas o SKU é configurável ✅ | módulo 04, `deployguide_gha.md` |

## 4. Avaliação de fontes externas

### msfthub.com/certs/azure/ai-300 — descartada como material de estudo; serve só como índice de links

Lida em 2026-11-06. É um agregador comunitário com cerca de 300–400 palavras:

- não tem código;
- não tem simulado próprio;
- não traz casos de borda;
- não cita OIDC nem RRF;
- não mostra os pesos dos domínios do exame.

Tudo o que tem valor nela aponta para o Microsoft Learn, que já está integrado aos módulos, junto com
as questões oficiais.

## 5. Em aberto

- ❓ O exame ainda cobra *hubs* do Foundry (classic) ou só o modelo novo de projetos?
- ❓ Qual o papel RBAC mínimo para a identidade do GitHub? (Projeto do módulo 02.)
