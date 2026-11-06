"""Baixa a documentação oficial de cada módulo para a pasta leituras/ dele.

Uso (na raiz do repositório):
    python scripts/atualizar_docs_oficiais.py        # todos os módulos
    python scripts/atualizar_docs_oficiais.py 03     # só o módulo 03

Duas origens:
1. Servidor MCP público do Microsoft Learn (https://learn.microsoft.com/api/mcp), chamado por
   JSON-RPC via HTTP com a ferramenta microsoft_docs_fetch (página inteira em Markdown).
2. Download direto do que o MCP não serve: JSON schemas da CLI v2, módulo Bicep AVM e o guia do
   exame.

As pastas leituras/ são ignoradas pelo git (é conteúdo da Microsoft; não republicamos).
Grava o log em <módulo>/leituras/_log.json. Só usa a biblioteca padrão do Python.
"""
import datetime
import json
import pathlib
import sys
import urllib.request

RAIZ = pathlib.Path(__file__).resolve().parent.parent
MCP = "https://learn.microsoft.com/api/mcp"
UA = {"User-Agent": "azure-ai-expert-roadmap/1.0"}
L = "https://learn.microsoft.com/en-us/azure"
ML = f"{L}/machine-learning"
V2 = "?view=azureml-api-2"
SCHEMAS = "https://azuremlschemas.azureedge.net/latest"
AVM = "https://raw.githubusercontent.com/Azure/bicep-registry-modules/main/avm/res/machine-learning-services/workspace"

# (pasta do módulo, nome do arquivo, url, como baixar: "mcp" | "md" (Accept markdown) | "raw")
FONTES = [
    ("00-preparacao", "study-guide-ai-300.md",
     "https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-300", "md"),

    ("01-aml-cli-foundation", "reference-yaml-job-pipeline.md", f"{ML}/reference-yaml-job-pipeline{V2}", "mcp"),
    ("01-aml-cli-foundation", "how-to-tune-hyperparameters.md", f"{ML}/how-to-tune-hyperparameters{V2}", "mcp"),
    ("01-aml-cli-foundation", "how-to-use-mlflow-cli-runs.md", f"{ML}/how-to-use-mlflow-cli-runs{V2}", "mcp"),
    ("01-aml-cli-foundation", "pipelineJob.schema.json", f"{SCHEMAS}/pipelineJob.schema.json", "raw"),
    ("01-aml-cli-foundation", "commandJob.schema.json", f"{SCHEMAS}/commandJob.schema.json", "raw"),
    ("01-aml-cli-foundation", "sweepJob.schema.json", f"{SCHEMAS}/sweepJob.schema.json", "raw"),

    ("02-cicd-github-actions", "connect-from-azure-openid-connect.md",
     f"{L}/developer/github/connect-from-azure-openid-connect", "mcp"),
    ("02-cicd-github-actions", "how-to-github-actions-machine-learning.md",
     f"{ML}/how-to-github-actions-machine-learning{V2}", "mcp"),
    ("02-cicd-github-actions", "how-to-safely-rollout-online-endpoints.md",
     f"{ML}/how-to-safely-rollout-online-endpoints{V2}", "mcp"),
    ("02-cicd-github-actions", "concept-model-monitoring.md", f"{ML}/concept-model-monitoring{V2}", "mcp"),

    ("03-genaiops-ai-foundry", "rag-evaluators.md",
     f"{L}/foundry/concepts/evaluation-evaluators/rag-evaluators", "mcp"),
    ("03-genaiops-ai-foundry", "trace-agent-setup.md", f"{L}/foundry/observability/how-to/trace-agent-setup", "mcp"),
    ("03-genaiops-ai-foundry", "how-to-monitor-agents-dashboard.md",
     f"{L}/foundry/observability/how-to/how-to-monitor-agents-dashboard", "mcp"),

    ("04-enterprise-iac-bicep", "bicep-ref-workspaces.md",
     f"{L}/templates/microsoft.machinelearningservices/workspaces", "mcp"),
    ("04-enterprise-iac-bicep", "how-to-managed-network.md", f"{ML}/how-to-managed-network{V2}", "mcp"),
    ("04-enterprise-iac-bicep", "how-to-configure-private-link.md", f"{ML}/how-to-configure-private-link{V2}", "mcp"),
    ("04-enterprise-iac-bicep", "avm-ml-workspace.main.bicep", f"{AVM}/main.bicep", "raw"),
    ("04-enterprise-iac-bicep", "avm-ml-workspace.README.md", f"{AVM}/README.md", "raw"),

    ("05-advanced-rag-architecture", "hybrid-search-overview.md", f"{L}/search/hybrid-search-overview", "mcp"),
    ("05-advanced-rag-architecture", "hybrid-search-ranking.md", f"{L}/search/hybrid-search-ranking", "mcp"),
    ("05-advanced-rag-architecture", "semantic-search-overview.md", f"{L}/search/semantic-search-overview", "mcp"),
]


def mcp_fetch(url, rid):
    corpo = json.dumps({"jsonrpc": "2.0", "id": rid, "method": "tools/call",
                        "params": {"name": "microsoft_docs_fetch", "arguments": {"url": url}}}).encode()
    req = urllib.request.Request(MCP, data=corpo, headers={
        **UA, "Content-Type": "application/json", "Accept": "application/json, text/event-stream"})
    bruto = urllib.request.urlopen(req, timeout=90).read().decode("utf-8")
    # A resposta vem em SSE: linhas "data: {...}"
    payload = "".join(l[5:].strip() for l in bruto.splitlines() if l.startswith("data:"))
    msg = json.loads(payload or bruto)
    if "error" in msg:
        raise RuntimeError(msg["error"])
    texto = "".join(c.get("text", "") for c in msg["result"]["content"])
    if not texto.strip():
        raise RuntimeError("resposta vazia")
    return texto.encode("utf-8")


def baixar(url, accept=None):
    headers = dict(UA)
    if accept:
        headers["Accept"] = accept
    return urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=90).read()


def main():
    filtro = sys.argv[1] if len(sys.argv) > 1 else None
    alvos = [f for f in FONTES if not filtro or f[0].startswith(filtro)]
    logs, falhas = {}, 0
    for rid, (modulo, nome, url, modo) in enumerate(alvos, start=1):
        destino = RAIZ / modulo / "leituras" / nome
        try:
            if modo == "mcp":
                conteudo = mcp_fetch(url, rid)
            elif modo == "md":
                conteudo = baixar(url, "text/markdown")
            else:
                conteudo = baixar(url)
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_bytes(conteudo)
            linha = ["OK", modo, url, f"{modulo}/leituras/{nome}"]
        except Exception as e:  # registra e segue: uma fonte fora do ar não deve parar as outras
            falhas += 1
            linha = ["FALHOU", modo, url, str(e)[:160]]
        logs.setdefault(modulo, []).append(linha)
        print(" | ".join(linha))

    hoje = datetime.date.today().isoformat()
    for modulo, linhas in logs.items():
        pasta = RAIZ / modulo / "leituras"
        pasta.mkdir(parents=True, exist_ok=True)
        (pasta / "_log.json").write_text(json.dumps(
            {"data": hoje, "servidor_mcp": MCP, "chamadas": linhas}, ensure_ascii=False, indent=2),
            encoding="utf-8")
    print(f"\n{len(alvos) - falhas} OK, {falhas} falha(s)")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
