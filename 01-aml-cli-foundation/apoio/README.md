# Apoio — Módulo 01

Arquivos **nossos**, que complementam o lab oficial sem alterá-lo.

## Pré-requisitos

- Assinatura do Azure, com alerta de orçamento (ver [módulo 00](../../00-preparacao/README.md)).
- Os labs rodam no **Azure Cloud Shell (Bash)**, aberto pelo botão `[>_]` no portal do Azure.
  Nada precisa ser instalado na sua máquina.

## Usar no Cloud Shell a mesma versão do lab que está aqui

O lab manda fazer `git clone` no Cloud Shell. O clone pega a versão **mais nova**, que pode ser
diferente da cópia de referência deste módulo. Para ficar igual, rode no Cloud Shell, logo depois
do clone:

```bash
cd mslearn-aml-cli && git checkout 191e8804f8005b2cad8eb4230ffb7cf5ada14068 && cd ..
```

(O commit é o que está em [repos-oficiais.lock.json](../../repos-oficiais.lock.json).)

## Recriar o ambiente

Os labs 02 a 06 pressupõem que o lab 01 já foi feito. Se você apagou os recursos entre uma sessão e
outra, o próprio lab diz que é preciso **repetir o lab 01**. O script [recriar-ambiente.sh](recriar-ambiente.sh)
faz exatamente os comandos do lab 01, de uma vez. Rode no Cloud Shell, na pasta que contém o clone
`mslearn-aml-cli/`:

```bash
bash recriar-ambiente.sh
```

Para usar outros nomes (por exemplo, se o nome da compute já estiver em uso na região):

```bash
RG=meu-rg WS=meu-ws CI=minha-ci-123 LOCAL=eastus bash recriar-ambiente.sh
```

## Apagar tudo

Os labs só param a compute ou apagam o workspace, o que deixa o grupo de recursos e o storage para
trás. Para não sobrar nada cobrando, apague o grupo inteiro:

```bash
bash ../../scripts/apagar-ambiente.sh diabetes-dev-rg
```

(O script pede confirmação antes de apagar.)
