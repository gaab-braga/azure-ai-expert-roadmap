"""Portão de qualidade do repositório. Rode antes de cada commit:

    python scripts/verify.py

Reprova (sai com código 1) quando:
  1. algum arquivo de conteúdo oficial (clones, leituras/, referencias/, docs_oficiais/) está no git;
  2. algum clone oficial foi alterado ou está fora do commit do lock;
  3. a página de um módulo perde uma das 9 etapas, ou falta um arquivo do molde do módulo;
  4. um link local em Markdown aponta para um arquivo que não existe;
  5. uma revisão intercalada cita uma questão que não existe;
  6. aparece caminho absoluto de usuário ou e-mail em arquivo versionado.

Avisos (não reprovam): clone ou leitura ainda não baixados. Rode preparar_modulos.py e
atualizar_docs_oficiais.py para eles sumirem.
"""
import json
import pathlib
import re
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))
import preparar_modulos  # noqa: E402  (reaproveita a checagem de clone intacto)

MODULOS = ["01-aml-cli-foundation", "02-cicd-github-actions", "03-genaiops-ai-foundry",
           "04-enterprise-iac-bicep", "05-advanced-rag-architecture"]
ETAPAS = ["## 1. Visão geral", "## 2. Pré-teste", "## 3. Preparar o ambiente", "## 4. Estudar",
          "## 5. Ler", "## 6. Pós-teste", "## 7. Projeto do zero", "## 8. Explicar",
          "## 9. Fechar o módulo"]
ARQUIVOS_DO_MOLDE = ["README.md", "quiz.md", "diario.md", "apoio/README.md", "projeto/README.md",
                     "evidencias/README.md"]
SECOES_PROJETO = ["## Enunciado", "## Requisitos", "## Rubrica", "## Como funciona"]

# Padrões montados por partes para este arquivo não acusar a si mesmo.
DRIVE_USERS = re.compile(r"[A-Za-z]:[\\/]+" + "Users" + r"[\\/]+[^\\/\s]+", re.I)
POSIX_HOME = re.compile(r"(?<![\w.])/(?:c/)?(?:" + "Users" + "|" + "home" + r")/[a-z0-9_.-]+/", re.I)
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
EMAIL_PERMITIDO = re.compile(r"@(example\.com|users\.noreply\.github\.com)$", re.I)
LINK_MD = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
REF_QUESTAO = re.compile(r"\*\*(0[1-5]-Q\d+)\*\*")


def arquivos_versionados():
    saida = subprocess.run(["git", "ls-files", "--cached"], cwd=RAIZ, capture_output=True,
                           text=True, encoding="utf-8", check=True).stdout
    return [p for p in saida.splitlines() if (RAIZ / p).is_file()]


def prefixos_oficiais():
    lock = json.loads((RAIZ / "repos-oficiais.lock.json").read_text(encoding="utf-8"))
    return [r["destino"].rstrip("/") + "/" for r in lock["repos"]] + ["referencias/", "docs_oficiais/"]


def eh_conteudo_oficial(caminho, prefixos):
    return any(caminho.startswith(p) for p in prefixos) or "/leituras/" in f"/{caminho}"


def main():
    erros, avisos = [], []
    versionados = arquivos_versionados()
    prefixos = prefixos_oficiais()

    # 1. Conteúdo oficial fora do git
    for p in versionados:
        if eh_conteudo_oficial(p, prefixos):
            erros.append(f"[1] conteúdo oficial versionado: {p}")

    # 2. Clones intactos
    lock = json.loads((RAIZ / "repos-oficiais.lock.json").read_text(encoding="utf-8"))
    for repo in lock["repos"]:
        problemas = preparar_modulos.checar(repo)
        if problemas == [p for p in problemas if p.startswith("não baixado")]:
            avisos.extend(f"[2] {repo['nome']}: {p}" for p in problemas)
        else:
            erros.extend(f"[2] {repo['nome']}: {p}" for p in problemas)

    # 3. Molde de cada módulo
    for m in MODULOS:
        for arq in ARQUIVOS_DO_MOLDE:
            if not (RAIZ / m / arq).is_file():
                erros.append(f"[3] falta {m}/{arq}")
        pagina = RAIZ / m / "README.md"
        if pagina.is_file():
            texto = pagina.read_text(encoding="utf-8")
            posicoes = [texto.find(e) for e in ETAPAS]
            for etapa, pos in zip(ETAPAS, posicoes):
                if pos < 0:
                    erros.append(f"[3] {m}/README.md sem a etapa '{etapa}'")
            achadas = [p for p in posicoes if p >= 0]
            if achadas != sorted(achadas):
                erros.append(f"[3] {m}/README.md com as etapas fora de ordem")
        projeto = RAIZ / m / "projeto" / "README.md"
        if projeto.is_file():
            texto = projeto.read_text(encoding="utf-8")
            for s in SECOES_PROJETO:
                if s not in texto:
                    erros.append(f"[3] {m}/projeto/README.md sem a seção '{s}'")

    # 4. Links locais em Markdown
    for p in versionados:
        if not p.endswith(".md"):
            continue
        arquivo = RAIZ / p
        texto = arquivo.read_text(encoding="utf-8")
        for alvo in LINK_MD.findall(texto):
            if re.match(r"^[a-z]+:", alvo, re.I) or alvo.startswith("#"):
                continue
            caminho = (arquivo.parent / alvo.split("#")[0]).resolve()
            if caminho.exists():
                continue
            try:
                rel = caminho.relative_to(RAIZ).as_posix()
            except ValueError:
                erros.append(f"[4] {p}: link sai do repositório: {alvo}")
                continue
            if eh_conteudo_oficial(rel, prefixos):
                avisos.append(f"[4] {p}: {alvo} ainda não baixado")
            else:
                erros.append(f"[4] {p}: link quebrado: {alvo}")

    # 5. Revisões intercaladas citam questões que existem
    questoes = set()
    for m in MODULOS:
        quiz = RAIZ / m / "quiz.md"
        if quiz.is_file():
            questoes.update(re.findall(r"^\*\*(0[1-5]-Q\d+)\.\*\*", quiz.read_text(encoding="utf-8"), re.M))
    for m in MODULOS:
        quiz = RAIZ / m / "quiz.md"
        if quiz.is_file():
            for ref in REF_QUESTAO.findall(quiz.read_text(encoding="utf-8")):
                if ref not in questoes:
                    erros.append(f"[5] {m}/quiz.md cita {ref}, que não existe")

    # 6. Dados pessoais em arquivos versionados
    for p in versionados:
        try:
            texto = (RAIZ / p).read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for n, linha in enumerate(texto.splitlines(), 1):
            if DRIVE_USERS.search(linha) or POSIX_HOME.search(linha):
                erros.append(f"[6] {p}:{n}: caminho absoluto de usuário")
            for email in EMAIL.findall(linha):
                if not EMAIL_PERMITIDO.search(email):
                    erros.append(f"[6] {p}:{n}: e-mail em arquivo versionado ({email})")

    for a in avisos:
        print(f"AVISO  {a}")
    for e in erros:
        print(f"ERRO   {e}")
    print(f"\nverify: {len(erros)} erro(s), {len(avisos)} aviso(s) - {'REPROVADO' if erros else 'APROVADO'}")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
