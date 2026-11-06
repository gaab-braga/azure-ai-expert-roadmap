#!/usr/bin/env bash
# Apaga um grupo de recursos inteiro: workspace, storage, key vault, computes, endpoints...
# Os labs oficiais costumam só parar a compute ou apagar o workspace, o que deixa recursos cobrando.
# Uso: bash scripts/apagar-ambiente.sh <nome-do-grupo-de-recursos>
set -euo pipefail

RG="${1:-}"
if [ -z "$RG" ]; then
  echo "Uso: bash scripts/apagar-ambiente.sh <nome-do-grupo-de-recursos>" >&2
  echo "Grupos existentes na assinatura atual:" >&2
  az group list --query "[].name" -o tsv >&2
  exit 1
fi

echo "Recursos em '$RG':"
az resource list --resource-group "$RG" --query "[].{tipo:type, nome:name}" -o table

read -r -p "Apagar o grupo '$RG' e TUDO o que está nele? Digite o nome do grupo para confirmar: " resp
if [ "$resp" != "$RG" ]; then
  echo "Cancelado: o nome digitado não confere."
  exit 1
fi

az group delete --name "$RG" --yes --no-wait
echo "Exclusão iniciada (roda em segundo plano). Confira com: az group exists --name $RG"
