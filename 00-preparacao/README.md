# Módulo 00 — Preparação

> Faça uma vez só, antes do módulo 01. Leva menos de uma hora, mais o tempo do simulado.

## 1. Conta e orçamento

- [ ] Uma assinatura do Azure em que você possa criar grupos de recursos.
- [ ] **Alerta de orçamento**: no portal, abra *Cost Management* › *Budgets* e crie um orçamento
      mensal com alerta por e-mail (por exemplo, em 50% e 90%). 🔶 O caminho no portal pode mudar de
      nome. Recurso esquecido ligado é o erro mais caro de quem estuda Azure.

## 2. Ferramentas

- [ ] Git e Python 3.10+
- [ ] Azure CLI + extensão de ML: `az extension add --name ml`
- [ ] Azure Developer CLI (azd), usado nos módulos 03 e 05
- [ ] VS Code com as extensões **Azure Machine Learning** e **Bicep**
- [ ] Uma conta no GitHub

## 3. Baixar o material

Na raiz deste repositório:

```bash
python scripts/preparar_modulos.py all
```

```bash
python scripts/atualizar_docs_oficiais.py
```

O primeiro baixa os 6 repositórios oficiais nas versões fixadas (intactos, fora do git). O segundo
baixa as leituras oficiais de cada módulo. Confira se está tudo certo:

```bash
python scripts/verify.py
```

## 4. Simulado inicial (linha de base)

- [ ] Leia o [guia oficial do exame](leituras/study-guide-ai-300.md)
      ([versão online](https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-300)):
      os 5 domínios e o que cada um cobra.
- [ ] Faça a **avaliação prática oficial** no AI Skills Navigator (exige login). O link está no guia
      do exame. ✅
- [ ] Anote a nota geral e a de cada domínio no [PROGRESSO.md](../PROGRESSO.md).

Tirar nota baixa agora é normal e útil: no fim do curso você faz o simulado de novo e compara.

## 5. Ler o método

- [ ] [COMO-ESTUDAR.md](../COMO-ESTUDAR.md): o ciclo que se repete em cada módulo. Depois disso,
      siga para o [Módulo 01](../01-aml-cli-foundation/README.md).
