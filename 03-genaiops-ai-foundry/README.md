# Módulo 03 — GenAIOps no Microsoft Foundry

> Esta página é o módulo inteiro. Siga as etapas de 1 a 9, nesta ordem, sem pular.
> Como estudar: [COMO-ESTUDAR.md](../COMO-ESTUDAR.md) · Seu progresso: [PROGRESSO.md](../PROGRESSO.md)

**Legenda:** ✅ provado em fonte oficial · 🔶 hipótese · ❓ em aberto

---

## 1. Visão geral

**Objetivo:** tratar um agente de IA como software: prompts versionados no Git, avaliação
automática que **reprova** mudanças ruins, e rastreio de tokens, latência e erros em produção.

**Repositório oficial:** `mslearn-genaiops` (licença MIT), em [mslearn-genaiops/](mslearn-genaiops/),
com uma [versão navegável](https://microsoftlearning.github.io/mslearn-genaiops/). É o conjunto de
labs do **curso oficial AI-300T00**, e o cenário é o "Trail Guide Agent" da Adventure Works. ✅

**Trilha oficial do Learn:** [Operationalize generative AI applications (GenAIOps)](https://learn.microsoft.com/training/paths/operationalize-gen-ai-apps/),
com 7 módulos, todos com questões de verificação. ✅

**Habilidades do exame cobertas:**
- GenAIOps infrastructure: Foundry resources and projects · managed identities and RBAC · Bicep + Azure CLI · deploy foundation models · prompt versioning with Git
- Quality and observability: test datasets · groundedness, relevance, coherence, fluency · risk and safety evaluations · automated evaluation workflows · latency, tokens and cost · tracing
- Optimization: fine-tuning methods and synthetic data

**Tempo:** labs de 15 a 40 min (200 min no total), segundo os próprios labs ✅. A trilha do Learn soma
457 min ✅. A avaliação do lab 04 (89 itens) pode levar de 15 a mais de 60 min ✅.

**Custo — atenção:**
- O `azd up` cria uma conta Foundry (AIServices S0), um projeto, Log Analytics, Application Insights
  e um deploy de modelo. ✅ No lab 04 também cria um Container Registry. ✅
- O modelo padrão no Bicep é `gpt-5-mini` (GlobalStandard, capacidade 10), embora o texto do lab
  cite GPT-5.1. A região recomendada é Sweden Central. ✅ Confira cota e disponibilidade antes.
- O lab 06 (fine-tuning) é **só uma simulação em HTML**: não cria recurso e não custa nada. ✅

---

## 2. Pré-teste

Responda o [quiz.md](quiz.md) **sem consultar** e anote a nota no [PROGRESSO.md](../PROGRESSO.md).

---

## 3. Preparar o ambiente

```bash
python scripts/preparar_modulos.py 03
```

Depois siga o [apoio/README.md](apoio/README.md). Este módulo roda **na sua máquina** (VS Code, azd),
num repositório seu criado a partir do template.

---

## 4. Estudar (Learn → lab → questões oficiais)

| # | Teoria (Learn) | Lab oficial | O que observar | Questões oficiais |
| :-- | :-- | :-- | :-- | :-- |
| 00 | — | [Pré-requisitos](mslearn-genaiops/docs/00-prerequisites.md) | VS Code, Python, Git, Azure CLI e azd; `az login` + `azd auth login` | — |
| 01 | [Plan and prepare a GenAIOps solution](https://learn.microsoft.com/training/modules/plan-prepare-genaiops/) | [Infraestrutura do projeto](mslearn-genaiops/docs/01-infrastructure-setup.md) | O que o `azd up` cria, olhando o `infra/main.bicep` | [knowledge check](https://learn.microsoft.com/training/modules/plan-prepare-genaiops/7-knowledge-check) |
| 02 | [Manage prompts with GitHub](https://learn.microsoft.com/training/modules/prompt-versioning-genaiops/) | [Versões de prompt e agente](mslearn-genaiops/docs/02-prompt-management.md) | Cada versão de prompt (v1 a v3) vira um commit comparável | [knowledge check](https://learn.microsoft.com/training/modules/prompt-versioning-genaiops/6-knowledge-check) |
| 03 | [Evaluate and optimize through experiments](https://learn.microsoft.com/training/modules/evaluate-optimize-agents/) | [Desenhar e otimizar prompts](mslearn-genaiops/docs/03-design-optimize-prompts.md) | Experimento em branch do Git; medir a economia de tokens | [knowledge check](https://learn.microsoft.com/training/modules/evaluate-optimize-agents/6-knowledge-check) |
| 04 | [Automate AI evaluations with GitHub Actions](https://learn.microsoft.com/training/modules/automated-evaluation-genaiops/) | [Avaliação automatizada](mslearn-genaiops/docs/04-automated-evaluation.md) | Aqui o lab **usa OIDC** (credencial federada) ✅; o gatilho de PR do `evaluate-agent.yml` vem **comentado** ✅ | [knowledge check](https://learn.microsoft.com/training/modules/automated-evaluation-genaiops/8-knowledge-check) |
| 05 | [Monitor your gen AI app](https://learn.microsoft.com/training/modules/monitor-generative-ai-app/) + [Tracing](https://learn.microsoft.com/training/modules/tracing-generative-ai-app/) | [Monitorar e rastrear](mslearn-genaiops/docs/05-monitoring-tracing.md) | Spans do OpenTelemetry por versão; tokens e latência no Application Insights | [check 1](https://learn.microsoft.com/training/modules/monitor-generative-ai-app/8-knowledge-check) · [check 2](https://learn.microsoft.com/training/modules/tracing-generative-ai-app/8-knowledge-check) |
| 06 | [Fine-tune models for AI agents](https://learn.microsoft.com/training/modules/optimize-finetune-agents/) | [Fine-tuning (simulação)](mslearn-genaiops/docs/06-optimize-finetuning.md) | Diferença entre SFT, RFT e DPO | [knowledge check](https://learn.microsoft.com/training/modules/optimize-finetune-agents/7-knowledge-check) |

Os arquivos `docs/plan.md`, `spec.md` e `scenario.md` **não são labs**: são os documentos de projeto
dos autores. ✅ Vale lê-los como exemplo de especificação.

---

## 5. Ler (aprofundar)

| Leitura | Por quê |
| :-- | :-- |
| [rag-evaluators.md](leituras/rag-evaluators.md) · [oficial](https://learn.microsoft.com/azure/foundry/concepts/evaluation-evaluators/rag-evaluators) | Groundedness, Relevance, Response Completeness: entradas, escala e limite |
| [trace-agent-setup.md](leituras/trace-agent-setup.md) · [oficial](https://learn.microsoft.com/azure/foundry/observability/how-to/trace-agent-setup) | Como ligar o tracing no Foundry |
| [how-to-monitor-agents-dashboard.md](leituras/how-to-monitor-agents-dashboard.md) · [oficial](https://learn.microsoft.com/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard) | Painel de tokens, latência e avaliação contínua |

---

## 6. Pós-teste

Refaça o [quiz.md](quiz.md) e a revisão intercalada que está no fim dele. Anote as notas no
[PROGRESSO.md](../PROGRESSO.md).

---

## 7. Projeto do zero

Enunciado, requisitos e rubrica: [projeto/README.md](projeto/README.md). Comece sem abrir os labs e
registre cada consulta no [diario.md](diario.md).

---

## 8. Explicar

Escreva a seção "Como funciona" do [projeto/README.md](projeto/README.md), incluindo **por que** você
escolheu os limites de aprovação da avaliação.

---

## 9. Fechar o módulo

- [ ] `azd down --purge`, service principal ou app apagado, repositório de teste apagado
      (veja [apoio/README.md](apoio/README.md#apagar-tudo))
- [ ] Evidências em [evidencias/](evidencias/)
- [ ] Projeto aprovado na rubrica e nenhum 🔶 pendente neste módulo
- [ ] Commit e push · [PROGRESSO.md](../PROGRESSO.md) com as datas de revisão
