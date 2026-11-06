"""Baixa os repositórios oficiais da Microsoft para dentro de cada módulo, sem alterar nada neles.

Uso (na raiz do repositório):
    python scripts/preparar_modulos.py 01            # só o módulo 01
    python scripts/preparar_modulos.py all           # todos os módulos + referências
    python scripts/preparar_modulos.py all --checar  # só confere, não baixa nada
    python scripts/preparar_modulos.py all --atualizar  # move para a versão mais nova e reescreve o lock

Regras:
- A versão (commit) de cada repositório fica fixada em repos-oficiais.lock.json, para o guia
  não quebrar quando a Microsoft mudar os labs.
- Os clones ficam em pastas ignoradas pelo git: nada da Microsoft é republicado.
- Se um clone já existe, o script confere se ele está INTACTO (sem arquivo alterado e no commit do
  lock). Se não estiver, para com erro e explica como restaurar. O que você precisar acrescentar
  vai na pasta apoio/ do módulo, nunca dentro do repositório oficial.

Sai com código 0 se tudo estiver OK e 1 se algo falhar.
"""
import argparse
import json
import pathlib
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
LOCK = RAIZ / "repos-oficiais.lock.json"


def git(*args, cwd=None):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} falhou: {r.stderr.strip()}")
    return r.stdout.strip()


def ultimo_commit(url):
    """Commit atual da branch padrão do repositório remoto."""
    saida = git("ls-remote", "--symref", url, "HEAD")
    for linha in saida.splitlines():
        partes = linha.split("\t")
        if len(partes) == 2 and partes[1] == "HEAD" and not partes[0].startswith("ref:"):
            return partes[0]
    raise RuntimeError(f"não achei o HEAD de {url}")


def checar(repo):
    """Devolve a lista de problemas do clone (lista vazia = intacto)."""
    destino = RAIZ / repo["destino"]
    if not (destino / ".git").exists():
        return [f"não baixado (rode: python scripts/preparar_modulos.py {repo['modulo']})"]
    problemas = []
    head = git("rev-parse", "HEAD", cwd=destino)
    if head != repo["commit"]:
        problemas.append(f"está no commit {head[:10]}, o lock pede {repo['commit'][:10]}")
    alterados = git("status", "--porcelain", cwd=destino)
    if alterados:
        n = len(alterados.splitlines())
        problemas.append(
            f"{n} arquivo(s) alterado(s) ou criado(s) dentro do oficial. Para restaurar: "
            f"cd {repo['destino']} && git checkout -- . && git clean -fd "
            f"(antes, mova o que for seu para a pasta apoio/ do módulo)")
    return problemas


def baixar(repo):
    destino = RAIZ / repo["destino"]
    destino.parent.mkdir(parents=True, exist_ok=True)
    if repo.get("sparse"):
        git("clone", "--filter=blob:none", "--no-checkout", repo["url"], str(destino))
        git("sparse-checkout", "set", *repo["sparse"], cwd=destino)
    else:
        git("clone", "--filter=blob:none", "--no-checkout", repo["url"], str(destino))
    git("-c", "advice.detachedHead=false", "checkout", repo["commit"], cwd=destino)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("modulo", help="01, 02, 03, 04, 05, ref ou all")
    p.add_argument("--checar", action="store_true", help="só confere, não baixa")
    p.add_argument("--atualizar", action="store_true", help="move para o commit mais novo e reescreve o lock")
    a = p.parse_args()

    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    alvos = [r for r in lock["repos"] if a.modulo == "all" or r["modulo"] == a.modulo]
    if not alvos:
        print(f"Módulo '{a.modulo}' não existe no lock.")
        return 1

    falhas = 0
    for repo in alvos:
        destino = RAIZ / repo["destino"]
        try:
            if a.atualizar:
                novo = ultimo_commit(repo["url"])
                if novo != repo["commit"]:
                    print(f"[{repo['nome']}] lock: {repo['commit'][:10]} -> {novo[:10]}")
                    repo["commit"] = novo
                if (destino / ".git").exists():
                    if git("status", "--porcelain", cwd=destino):
                        raise RuntimeError("clone alterado; restaure antes de atualizar")
                    git("fetch", "origin", novo, cwd=destino)
                    git("-c", "advice.detachedHead=false", "checkout", novo, cwd=destino)
            elif not (destino / ".git").exists() and not a.checar:
                print(f"[{repo['nome']}] baixando para {repo['destino']} ...")
                baixar(repo)
            problemas = checar(repo)
        except RuntimeError as e:
            problemas = [str(e)]
        if problemas:
            falhas += 1
            for pr in problemas:
                print(f"[{repo['nome']}] FALHOU: {pr}")
        else:
            print(f"[{repo['nome']}] OK - intacto no commit {repo['commit'][:10]} ({repo['destino']})")

    if a.atualizar:
        LOCK.write_text(json.dumps(lock, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("Lock reescrito. Revise o diff e os labs antes de commitar.")
    print(f"\n{len(alvos) - falhas} OK, {falhas} com problema")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
