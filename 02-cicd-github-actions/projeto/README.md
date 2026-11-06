# Projeto do zero — Módulo 02

> **Status:** ⏳ não iniciado

## Enunciado

Pegue o modelo do seu projeto do módulo 01 e construa a esteira completa no **seu** repositório. A
diferença em relação ao lab: tudo **mais seguro** e sem passos manuais.

## Requisitos

- [ ] **Login por OIDC**: credencial federada + `permissions: id-token: write` + `azure/login` com
      os 3 IDs. **Nenhum** `AZURE_CREDENTIALS` com segredo (o lab usa um; aqui não)
- [ ] **Menor privilégio**: teste um papel mais restrito que *Contributor* no grupo de recursos e
      registre no diário o que funcionou e o que falhou. 🔶 O papel mínimo não está documentado nas
      leituras: descobrir é parte do projeto
- [ ] `train.yml`: roda o treino num **pull request** e comenta a métrica no PR
- [ ] `deploy.yml`: só roda depois de aprovação manual (GitHub *environment* `prod`)
- [ ] Endpoint online com **dois deployments** (blue/green): espelhar 10% para o green → validar →
      trocar o tráfego aos poucos → registrar um **rollback**
- [ ] Coleta de dados + monitor de **data drift**, com uma simulação de drift
- [ ] `SEGREDOS.md`: quais secrets e variáveis existem, para que servem e qual papel cada identidade tem
      (sem nenhum valor real)

## Rubrica

| Critério | 0 | 1 | 2 |
| :-- | :-- | :-- | :-- |
| Autenticação | Segredo guardado | OIDC com papel amplo sem teste | OIDC + teste de privilégio documentado |
| Automação | Passos manuais | Treino automático, deploy manual | PR → treino → aprovação → deploy |
| Rollout | Deploy direto | Blue/green sem espelho | Espelho → troca gradual → rollback, com evidência |
| Monitoramento | Ausente | Coleta sem monitor | Monitor com drift simulado e alerta |
| Explicação | Ausente | Lista de passos | Diagrama do fluxo + "Como funciona" |

**Aprovado:** nenhum critério com 0 e pelo menos 8 pontos de 10.

## Como funciona

*(Etapa 8.)*

## Evidências

*(Links para [../evidencias/](../evidencias/).)*
