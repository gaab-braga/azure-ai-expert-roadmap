# docs_oficiais — índice das fontes

Cópias **brutas** de referências oficiais, baixadas em **2026-11-06**. Não edite à mão; para
atualizar, rode:

```bash
python scripts/atualizar_docs_oficiais.py
```

O log da última execução fica em `_log_mcp.json`.

## Como foram obtidas

- **MCP do Microsoft Learn** (`https://learn.microsoft.com/api/mcp`), chamado por HTTP/JSON-RPC.
  O conector desse MCP não estava instalado no Claude Code; o servidor é público, então o script
  conversa direto com ele. Ferramentas usadas: `microsoft_docs_search` (arquivos `busca_*.json`:
  até 10 trechos por consulta) e `microsoft_docs_fetch` (arquivos `.md`: a página inteira).
- **Download direto** para o que o MCP não serve: JSON schemas, módulo Bicep e guia do exame.

## Arquivos

| Pasta | Arquivo | O que é | Origem |
| :-- | :-- | :-- | :-- |
| `00-exame-ai-300` | `study-guide-ai-300.md` | Guia oficial do exame: domínios, pesos, habilidades | learn.microsoft.com (download direto) |
| `01-schemas-cli-v2` | `pipelineJob.schema.json` | JSON schema dos pipeline jobs | azuremlschemas.azureedge.net/latest |
| | `commandJob.schema.json` | JSON schema dos command jobs | idem |
| | `sweepJob.schema.json` | JSON schema dos sweep jobs (distribuições do `search_space`) | idem |
| | `reference-yaml-job-pipeline.md` | Referência YAML do pipeline job | MCP fetch |
| | `busca_pipeline_job_yaml.json` | Busca no Learn | MCP search |
| `02-cicd-oidc` | `connect-from-azure-openid-connect.md` | Login OIDC do GitHub Actions no Azure | MCP fetch |
| | `how-to-github-actions-machine-learning.md` | GitHub Actions com Azure ML | MCP fetch |
| | `busca_github_actions_oidc.json` | Busca no Learn | MCP search |
| `03-avaliacao-groundedness` | `rag-evaluators.md` | Avaliadores de RAG do Foundry (Groundedness, Relevance…) | MCP fetch |
| | `busca_groundedness.json` | Busca no Learn | MCP search |
| `04-bicep-rede-isolada` | `bicep-ref-workspaces.md` | Referência Bicep/ARM de `Microsoft.MachineLearningServices/workspaces` | MCP fetch |
| | `how-to-managed-network.md` | Rede virtual gerenciada do Azure ML | MCP fetch |
| | `avm-ml-workspace.main.bicep` | Módulo oficial AVM do workspace (padrão `publicNetworkAccess = 'Disabled'`) | github.com/Azure/bicep-registry-modules |
| | `avm-ml-workspace.README.md` | Parâmetros e exemplos do módulo AVM | idem |
| | `busca_workspace_rede_isolada.json` | Busca no Learn | MCP search |
| `05-rag-busca-hibrida` | `hybrid-search-ranking.md` | Como o RRF funde os resultados | MCP fetch |
| | `hybrid-search-overview.md` | Visão geral da busca híbrida | MCP fetch |
| | `busca_rrf_hibrida.json` | Busca no Learn | MCP search |

## Cuidados

- Conteúdo de terceiros (Microsoft), sob a licença de cada fonte. Está aqui para consulta e estudo.
- A doc de pipeline avisa que o schema `latest` só é garantido para a versão mais recente da
  extensão `ml` da CLI.
