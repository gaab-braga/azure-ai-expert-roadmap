# Projeto do zero — Módulo 03

> **Status:** ⏳ não iniciado

## Enunciado

Crie um agente para **outro domínio** (sugestão: um assistente que explica termos de FP&A com base
num glossário público que você mesmo escreve) e opere esse agente como um produto: versões de prompt,
avaliação que bloqueia regressões e observabilidade.

## Requisitos

- [ ] Projeto Foundry criado por código (azd/Bicep), **não** pelo portal
- [ ] Pasta `prompts/` com pelo menos 2 versões, cada uma num commit
- [ ] Dataset de avaliação em JSONL com pelo menos 20 itens **fictícios**, com `query`, `context` e
      resposta esperada
- [ ] Script de avaliação com Groundedness, Relevance e pelo menos 1 avaliador de risco e segurança
- [ ] Workflow de avaliação com o **gatilho de PR ligado** (no lab ele vem comentado) e login por OIDC
- [ ] **Portão:** o PR reprova se a média de Groundedness ou de Relevance ficar abaixo de 3. Prove que
      ele reprova: abra um PR com um prompt propositalmente ruim
- [ ] Tracing ligado e uma comparação de **tokens e latência** entre as 2 versões de prompt

## Rubrica

| Critério | 0 | 1 | 2 |
| :-- | :-- | :-- | :-- |
| Infra como código | Portal | azd sem entender o Bicep | azd + explicação do que o Bicep cria |
| Versionamento | Prompt solto | Versões sem comparação | Versões comparadas com números |
| Avaliação | Ausente | Roda manualmente | Roda no PR e reprova de fato (com evidência) |
| Observabilidade | Ausente | Traces sem análise | Tokens e latência comparados entre versões |
| Explicação | Ausente | Lista de passos | Justificativa dos limites + "Como funciona" |

**Aprovado:** nenhum critério com 0 e pelo menos 8 pontos de 10.

## Como funciona

*(Etapa 8.)*

## Evidências

*(Links para [../evidencias/](../evidencias/).)*
