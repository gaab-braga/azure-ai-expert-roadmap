#!/usr/bin/env bash
# Recria o ambiente do lab 01 do mslearn-aml-cli (os labs 02 a 06 dependem dele).
# Mesmos comandos do lab oficial 01-create-workspace.md, na mesma ordem.
# Rode no Azure Cloud Shell (Bash), na pasta que contém o clone "mslearn-aml-cli/".
set -euo pipefail

RG="${RG:-diabetes-dev-rg}"
WS="${WS:-aml-diabetes-dev}"
CI="${CI:-testdev-vm}"          # até 24 caracteres e único na região
LOCAL="${LOCAL:-eastus}"
LAB="./mslearn-aml-cli/Allfiles/Labs/01"

if [ ! -d "$LAB" ]; then
  echo "Não achei $LAB. Rode este script na pasta que contém o clone mslearn-aml-cli/." >&2
  exit 1
fi

echo "1/6 Extensão ml da CLI"
az extension add -n ml -y

echo "2/6 Grupo de recursos $RG ($LOCAL)"
az group create --name "$RG" --location "$LOCAL" -o none
az configure --defaults group="$RG"

echo "3/6 Workspace $WS"
az ml workspace create --name "$WS" -o none
az configure --defaults workspace="$WS"

echo "4/6 Compute instance $CI (leva de 2 a 5 minutos)"
az ml compute create --name "$CI" --size STANDARD_DS11_V2 --type ComputeInstance -o none

echo "5/6 Environment"
az ml environment create --file "$LAB/basic-env.yml" -o none

echo "6/6 Data asset"
az ml data create --file "$LAB/data-local-path.yml" -o none

echo
echo "Pronto. Ao terminar a sessão, pare a compute para não pagar por ela parada:"
echo "  az ml compute stop --name \"$CI\" --no-wait"
