"""Baixa de novo as referências oficiais para docs_oficiais/.

Uso (na raiz do repositório):
    python scripts/atualizar_docs_oficiais.py

Duas origens:
1. Servidor MCP público do Microsoft Learn (https://learn.microsoft.com/api/mcp), chamado por
   JSON-RPC via HTTP: ferramentas microsoft_docs_search e microsoft_docs_fetch.
2. Download direto de arquivos oficiais que o MCP não serve (JSON schemas da CLI v2, módulo
   Bicep AVM e o guia do exame em Markdown).

Grava um log em docs_oficiais/_log_mcp.json. Só usa a biblioteca padrão do Python.
"""
import datetime
import json
import pathlib
import urllib.request

RAIZ = pathlib.Path(__file__).resolve().parent.parent
OUT = RAIZ / "docs_oficiais"
MCP = "https://learn.microsoft.com/api/mcp"
UA = {"User-Agent": "azure-ai-expert-roadmap/1.0"}

BUSCAS = [
    ("01-schemas-cli-v2", "busca_pipeline_job_yaml", "Azure Machine Learning CLI v2 pipeline job YAML schema reference"),
    ("02-cicd-oidc", "busca_github_actions_oidc", "GitHub Actions azure/login OpenID Connect federated credential Azure Machine Learning"),
    ("03-avaliacao-groundedness", "busca_groundedness", "Microsoft Foundry groundedness evaluator RAG evaluators threshold"),
    ("04-bicep-rede-isolada", "busca_workspace_rede_isolada", "Azure Machine Learning workspace Bicep publicNetworkAccess Disabled managed network allow_only_approved_outbound"),
    ("05-rag-busca-hibrida", "busca_rrf_hibrida", "Azure AI Search hybrid search Reciprocal Rank Fusion RRF scoring"),
]
PAGINAS = [
    ("01-schemas-cli-v2", "reference-yaml-job-pipeline", "https://learn.microsoft.com/en-us/azure/machine-learning/reference-yaml-job-pipeline?view=azureml-api-2"),
    ("02-cicd-oidc", "connect-from-azure-openid-connect", "https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect"),
    ("02-cicd-oidc", "how-to-github-actions-machine-learning", "https://learn.microsoft.com/en-us/azure/machine-learning/how-to-github-actions-machine-learning?view=azureml-api-2"),
    ("03-avaliacao-groundedness", "rag-evaluators", "https://learn.microsoft.com/azure/foundry/concepts/evaluation-evaluators/rag-evaluators"),
    ("04-bicep-rede-isolada", "bicep-ref-workspaces", "https://learn.microsoft.com/en-us/azure/templates/microsoft.machinelearningservices/workspaces"),
    ("04-bicep-rede-isolada", "how-to-managed-network", "https://learn.microsoft.com/en-us/azure/machine-learning/how-to-managed-network?view=azureml-api-2"),
    ("05-rag-busca-hibrida", "hybrid-search-ranking", "https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking"),
    ("05-rag-busca-hibrida", "hybrid-search-overview", "https://learn.microsoft.com/en-us/azure/search/hybrid-search-overview"),
]
SCHEMAS = "https://azuremlschemas.azureedge.net/latest"
AVM = "https://raw.githubusercontent.com/Azure/bicep-registry-modules/main/avm/res/machine-learning-services/workspace"
DIRETOS = [
    ("01-schemas-cli-v2/pipelineJob.schema.json", f"{SCHEMAS}/pipelineJob.schema.json", None),
    ("01-schemas-cli-v2/commandJob.schema.json", f"{SCHEMAS}/commandJob.schema.json", None),
    ("01-schemas-cli-v2/sweepJob.schema.json", f"{SCHEMAS}/sweepJob.schema.json", None),
    ("04-bicep-rede-isolada/avm-ml-workspace.main.bicep", f"{AVM}/main.bicep", None),
    ("04-bicep-rede-isolada/avm-ml-workspace.README.md", f"{AVM}/README.md", None),
    ("00-exame-ai-300/study-guide-ai-300.md",
     "https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-300", "text/markdown"),
]


def chamar_mcp(ferramenta, argumentos, rid):
    corpo = json.dumps({"jsonrpc": "2.0", "id": rid, "method": "tools/call",
                        "params": {"name": ferramenta, "arguments": argumentos}}).encode()
    req = urllib.request.Request(MCP, data=corpo, headers={
        **UA, "Content-Type": "application/json", "Accept": "application/json, text/event-stream"})
    bruto = urllib.request.urlopen(req, timeout=90).read().decode("utf-8")
    # A resposta vem em SSE: linhas "data: {...}"
    payload = "".join(l[5:].strip() for l in bruto.splitlines() if l.startswith("data:"))
    msg = json.loads(payload or bruto)
    if "error" in msg:
        raise RuntimeError(msg["error"])
    return "".join(c.get("text", "") for c in msg["result"]["content"])


def baixar(url, accept):
    headers = dict(UA)
    if accept:
        headers["Accept"] = accept
    return urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=90).read()


def main():
    log, rid = [], 0
    for pasta, nome, consulta in BUSCAS:
        rid += 1
        destino = OUT / pasta / f"{nome}.json"
        try:
            dados = json.loads(chamar_mcp("microsoft_docs_search", {"query": consulta}, rid))
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")
            log.append(["OK", "mcp:microsoft_docs_search", consulta, destino.relative_to(OUT).as_posix()])
        except Exception as e:  # registra e segue: uma fonte fora do ar não deve parar as outras
            log.append(["FALHOU", "mcp:microsoft_docs_search", consulta, str(e)[:160]])
    for pasta, nome, url in PAGINAS:
        rid += 1
        destino = OUT / pasta / f"{nome}.md"
        try:
            texto = chamar_mcp("microsoft_docs_fetch", {"url": url}, rid)
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(texto, encoding="utf-8")
            log.append(["OK", "mcp:microsoft_docs_fetch", url, destino.relative_to(OUT).as_posix()])
        except Exception as e:
            log.append(["FALHOU", "mcp:microsoft_docs_fetch", url, str(e)[:160]])
    for rel, url, accept in DIRETOS:
        destino = OUT / rel
        try:
            conteudo = baixar(url, accept)
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_bytes(conteudo)
            log.append(["OK", "download", url, rel])
        except Exception as e:
            log.append(["FALHOU", "download", url, str(e)[:160]])

    (OUT / "_log_mcp.json").write_text(json.dumps(
        {"data": datetime.date.today().isoformat(), "servidor_mcp": MCP, "chamadas": log},
        ensure_ascii=False, indent=2), encoding="utf-8")
    for linha in log:
        print(" | ".join(linha))
    falhas = sum(1 for l in log if l[0] != "OK")
    print(f"\n{len(log) - falhas} OK, {falhas} falha(s)")
    raise SystemExit(1 if falhas else 0)


if __name__ == "__main__":
    main()
