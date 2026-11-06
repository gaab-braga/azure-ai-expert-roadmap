# Como estudar

Este repositório funciona como um curso. Cada módulo é **uma pasta e uma página**, e você só passa
para o próximo depois de fechar o ciclo completo do atual.

## A ideia em uma frase

**Primeiro você aprende com o material oficial da Microsoft. Depois prova que aprendeu refazendo do
zero, do seu jeito, um projeto diferente.**

## O ciclo de cada módulo

Toda página de módulo tem as mesmas 9 etapas. Ao lado de cada uma, a técnica de estudo que ela usa.

| Etapa | O que você faz | Técnica | Por que funciona |
| :-- | :-- | :-- | :-- |
| 1. Visão geral | Lê o objetivo, as habilidades do exame e os custos | — | Saber aonde vai chegar |
| 2. Pré-teste | Responde o quiz **sem saber** | Metacognição + pré-teste | Mostra as lacunas, e errar antes deixa a resposta certa mais marcante |
| 3. Preparar | Baixa a referência e monta o ambiente | — | Tira o atrito antes de começar |
| 4. Estudar | Teoria no Learn → lab oficial → questões oficiais **de memória** | Prática de recuperação | Lembrar fixa mais do que reler |
| 5. Ler | Documentação oficial do módulo | Elaboração | Liga o "como" do lab ao "porquê" |
| 6. Pós-teste | Mesmo quiz + questões de módulos anteriores | Intercalação + repetição | Misturar assuntos treina **escolher** a ferramenta certa, que é o que a prova cobra |
| 7. Projeto do zero | Refaz com outro dataset ou com uma versão mais segura, **sem olhar** primeiro | Dificuldade desejável | O esforço de lembrar sozinho é o que consolida |
| 8. Explicar | Escreve "Como funciona" para um colega | Técnica de Feynman | Onde não sai explicação simples, falta entendimento |
| 9. Fechar | Apaga recursos, commit, marca as revisões | Repetição espaçada | Revisar em +1, +7 e +30 dias segura a memória |

## Regras

1. **O repositório oficial não se altera.** As pastas `mslearn-*`, `mlops-v2` e
   `azure-search-openai-demo` dentro dos módulos são cópias **só para leitura**, na versão fixada em
   `repos-oficiais.lock.json`. O lab roda numa cópia de trabalho, criada como o próprio lab manda
   (Cloud Shell, template do GitHub ou `azd init`). O que faltar vai na pasta `apoio/` do módulo.
   O `scripts/verify.py` reprova se alguma cópia for alterada.
2. **Um módulo de cada vez.** O próximo só abre quando o projeto passar na rubrica e não houver 🔶
   pendente no atual. Hipótese acumulada vira erro difícil de achar lá na frente.
3. **Consultar é permitido, mas registrado.** No projeto do zero, cada consulta vai para o
   `diario.md`. A lista de consultas é a sua lista de revisão.
4. **Apague os recursos no fim de cada sessão.** Os labs costumam só parar a compute; use
   `scripts/apagar-ambiente.sh` para apagar o grupo de recursos inteiro.
5. **Nada real no Git.** IDs de assinatura e de tenant, chaves e e-mails ficam em secrets ou em
   arquivos ignorados, e as evidências vão com esses dados borrados.

## Revisão espaçada

Ao fechar um módulo, marque no [PROGRESSO.md](PROGRESSO.md) três datas: **+1**, **+7** e **+30** dias.
Em cada uma, refaça o quiz do módulo **sem consultar** (leva 10 minutos). Errou alguma? Releia a
fonte indicada no gabarito.

## Fechamento do curso

Depois do módulo 05:

1. Refaça a avaliação prática oficial (link no guia do exame) e compare com a nota do módulo 00.
2. Para cada domínio com nota baixa, volte aos módulos dele (tabela no [ROADMAP.md](ROADMAP.md)) e
   refaça os quizzes e as questões oficiais.
3. Agende a prova (nota mínima: 700).
4. O que fica para mostrar numa entrevista: cada `projeto/README.md`, com evidências e o diário de
   erros resolvidos.
