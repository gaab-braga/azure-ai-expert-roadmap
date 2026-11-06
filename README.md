# azure-ai-expert-roadmap

Curso prático de **MLOps e GenAIOps no Azure**, montado sobre os repositórios oficiais da
Microsoft, rumo à certificação **AI-300 — Operationalizing Machine Learning and Generative AI
Solutions**.

Cada módulo segue o mesmo ciclo: **estudar com o material oficial → responder às questões → refazer
do zero um projeto próprio → explicar**. O resultado é um portfólio em que cada pasta mostra o que
foi construído, como rodar e qual problema de engenharia foi resolvido.

## Comece aqui

1. [Módulo 00 — Preparação](00-preparacao/README.md): conta, ferramentas, download do material e simulado inicial
2. [COMO-ESTUDAR.md](COMO-ESTUDAR.md): o método, as regras e a revisão espaçada
3. [PROGRESSO.md](PROGRESSO.md): o seu painel de acompanhamento

## Módulos

| # | Módulo | Repositório oficial | Questões oficiais do Learn |
| :-- | :-- | :-- | :-- |
| 01 | [Fundação na CLI v2](01-aml-cli-foundation/README.md) | `mslearn-aml-cli` | — (quiz próprio) |
| 02 | [Ciclo de vida de ML e CI/CD](02-cicd-github-actions/README.md) | `mslearn-mlops` | 7 módulos |
| 03 | [GenAIOps no Microsoft Foundry](03-genaiops-ai-foundry/README.md) | `mslearn-genaiops` | 7 módulos |
| 04 | [Infraestrutura corporativa em Bicep](04-enterprise-iac-bicep/README.md) | `mlops-v2` | — (quiz próprio) |
| 05 | [Arquitetura RAG avançada](05-advanced-rag-architecture/README.md) | `azure-search-openai-demo` | — (quiz próprio) |

O mapa do exame, as correções ao relatório de origem e a avaliação de fontes estão em [ROADMAP.md](ROADMAP.md).

## Estrutura de um módulo

```text
0X-nome-do-modulo/
├── README.md        A página do módulo: as 9 etapas, em ordem
├── <repo-oficial>/  Cópia de referência intacta (baixada por script, fora do git)
├── leituras/        Documentação oficial do módulo (baixada por script, fora do git)
├── apoio/           Nossos acréscimos: pré-requisitos, recriar e apagar o ambiente
├── quiz.md          Questões com gabarito e fonte
├── projeto/         O projeto do zero: enunciado, rubrica e o seu código
├── evidencias/      Prints e saídas que provam que funcionou
└── diario.md        Observações, consultas e erros resolvidos
```

## Por que os repositórios da Microsoft não estão no GitHub deste projeto

- **Preservar o original:** cada um é baixado na versão fixada em `repos-oficiais.lock.json` e fica
  intacto. O `scripts/verify.py` reprova se algo for alterado neles.
- **Licença:** o `mslearn-mlops` não declara licença, então não pode ser republicado. ✅ Os outros são
  MIT, mas manter todos de fora deixa a regra simples.
- **Tamanho:** só o `azureml-examples` tem cerca de 800 MB. O script baixa apenas as pastas usadas.

## Scripts

| Script | Para que serve |
| :-- | :-- |
| `python scripts/preparar_modulos.py <01..05\|ref\|all>` | Baixa os repositórios oficiais ou confere se estão intactos (`--checar`, `--atualizar`) |
| `python scripts/atualizar_docs_oficiais.py [módulo]` | Baixa as leituras oficiais (via MCP do Microsoft Learn) |
| `python scripts/verify.py` | Portão de qualidade: rode antes de cada commit |
| `bash scripts/apagar-ambiente.sh <grupo>` | Apaga um grupo de recursos inteiro, com confirmação |

## Glossário rápido

| Termo | O que é, em uma linha |
| :-- | :-- |
| **MLOps** | Práticas para levar um modelo do notebook à produção de forma repetível |
| **GenAIOps** | O mesmo para aplicações com LLM: prompts versionados, avaliação, custo de tokens |
| **CLI v2** | O comando `az ml ...`, que cria recursos e jobs a partir de YAML |
| **OIDC** | Login do GitHub no Azure **sem senha guardada**, por confiança federada |
| **IaC / Bicep** | Infraestrutura descrita em arquivo, e não em cliques no portal |
| **Private Endpoint** | Um IP interno para o serviço, que deixa de ser acessível pela internet |
| **RAG** | O LLM responde com base em documentos buscados na hora |
| **Groundedness** | Nota de 1 a 5 de quanto a resposta se apoia só no contexto (mede alucinação) |

## Regras do repositório

- Nenhum segredo, ID real ou e-mail em arquivo versionado.
- Afirmações técnicas trazem a fonte. Legenda: ✅ provado · 🔶 hipótese · ❓ em aberto.
- Rode `python scripts/verify.py` antes de commitar.
