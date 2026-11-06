# azure-ai-expert-roadmap

Portfólio prático de **MLOps e GenAIOps no Azure**, construído fase a fase rumo à certificação
**AI-300 — Operationalizing Machine Learning and Generative AI Solutions**.

A ideia: cada pasta é um degrau. Começa com um arquivo YAML enviado pelo terminal e termina com
uma arquitetura de RAG corporativa sobre rede privada. Quem lê o repositório deve conseguir ver
**o que foi construído, como rodar e qual problema de engenharia cada etapa resolve**.

> **Status (2026-11-06):** só a estrutura existe. Nenhuma fase tem código ainda. O plano está
> em [ROADMAP.md](ROADMAP.md).

---

## Glossário rápido

| Termo | O que é, em uma linha |
| :-- | :-- |
| **MLOps** | Práticas para levar um modelo de ML do notebook para produção de forma repetível (versionar, testar, implantar, monitorar). |
| **GenAIOps** | O mesmo, mas para aplicações com LLMs: versionar prompts, avaliar respostas, rastrear custo de tokens. |
| **Azure ML CLI v2** | Comando `az ml ...` que cria recursos e jobs a partir de arquivos YAML. |
| **Job / Pipeline** | Job = uma execução (ex.: treinar). Pipeline = vários jobs encadeados. |
| **CI/CD** | Integração/Entrega contínua: o GitHub executa os passos sozinho a cada `push`. |
| **OIDC** | Forma de o GitHub Actions entrar no Azure **sem guardar senha**: o Azure confia num token temporário emitido pelo GitHub. |
| **IaC / Bicep** | Infraestrutura como código: a nuvem é descrita num arquivo (`.bicep`) em vez de cliques no portal. |
| **Private Endpoint** | Um "IP interno" para o serviço: ele deixa de ser acessível pela internet pública. |
| **RAG** | O LLM responde com base em documentos buscados na hora, não só no que "decorou". |
| **Groundedness** | Nota (1 a 5) de quanto a resposta se apoia **só** no contexto fornecido. Mede alucinação. |

---

## Stack

| Camada | Ferramenta |
| :-- | :-- |
| Treino e ciclo de vida de ML | Azure Machine Learning (CLI v2, MLflow) |
| IA generativa | Microsoft Foundry (projetos, avaliação, rastreamento) |
| Automação | GitHub Actions com login OIDC |
| Infraestrutura | Bicep + Azure CLI (módulo oficial AVM de workspace) |
| Busca para RAG | Azure AI Search (busca híbrida + RRF + semantic ranker) |
| Linguagem | Python, YAML, Bicep |

## Estrutura

```text
azure-ai-expert-roadmap/
├── 01-aml-cli-foundation/        Fase 1 — jobs, sweep e pipelines via YAML
├── 02-cicd-github-actions/       Fase 2 — os mesmos jobs disparados pelo GitHub (OIDC)
├── 03-genaiops-ai-foundry/       Fase 3 — prompts, deploy de modelos e avaliação no Foundry
├── 04-enterprise-iac-bicep/      Fase 4 — workspace em Bicep, sem acesso público, rede gerenciada
├── 05-advanced-rag-architecture/ Fase 5 — RAG com busca híbrida, RRF e reranking
├── docs_oficiais/                Referências brutas baixadas da Microsoft (ver FONTES.md)
├── scripts/                      atualizar_docs_oficiais.py — baixa de novo as referências
├── README.md                     Este arquivo
└── ROADMAP.md                    Plano tático: desafios de cada fase e mapa do exame
```

O repositório `azureml-examples` não tem pasta própria: ele é a "enciclopédia" consultada em todas
as fases (ver ROADMAP).

## Pré-requisitos

- Assinatura do Azure com permissão para criar grupos de recursos.
- Azure CLI e a extensão de ML:

```bash
az extension add --name ml
```

- Git e uma conta no GitHub (fase 2 em diante).
- Python 3.10+.

## Fluxos básicos no terminal

Entrar no Azure e definir padrões (troque os nomes pelos seus — **nunca** commite IDs reais):

```bash
az login
```

```bash
az configure --defaults group=<grupo-de-recursos> workspace=<workspace-ml>
```

Enviar um job descrito em YAML (fase 1):

```bash
az ml job create --file 01-aml-cli-foundation/<job>.yml --stream
```

Validar um Bicep antes de implantar (fase 4):

```bash
az deployment group what-if --resource-group <grupo-de-recursos> --template-file 04-enterprise-iac-bicep/main.bicep
```

> Os arquivos `<job>.yml` e `main.bicep` ainda não existem; serão criados nas fases.

## Regras do repositório

- **Nenhum segredo ou ID real em arquivo versionado.** Assinatura, tenant e client ID ficam em
  *GitHub Secrets* ou em arquivos locais listados no `.gitignore` (ex.: `config.json`).
- Toda afirmação técnica nos documentos vem com a fonte. Legenda usada:
  ✅ provado (está numa fonte oficial em `docs_oficiais/`) · 🔶 hipótese · ❓ em aberto.
- `docs_oficiais/` é cópia bruta: não se edita; se a Microsoft atualizar, baixa-se de novo.
