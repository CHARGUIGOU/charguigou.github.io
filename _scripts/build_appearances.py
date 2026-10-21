#!/usr/bin/env python3
"""
Pré-calcule _data/appearances.json : pour chaque fiche artiste (artists/*.md,
clé "artist:"), la liste des pages de doublage (cast / tabs / staff) où son
identifiant apparaît.

Pourquoi : sans ce fichier, chaque fiche parcourt TOUTES les lignes de TOUS les
casts pour retrouver ses rôles (temps de build ~ fiches x lignes de cast).
Avec ce fichier, chaque fiche ne lit que les pages où elle apparaît.

Le fichier est un SUR-ENSEMBLE volontaire : on garde toute page qui contient
l'identifiant dans n'importe quel texte de son front matter. La fiche refait
ensuite son tri exact. On ne peut donc pas perdre de crédit.

Usage (depuis la racine du dépôt) :
    python _scripts/build_appearances.py            # écrit _data/appearances.json
    python _scripts/build_appearances.py --check    # affiche seulement les stats
Ne PAS committer _data/appearances.json : il est régénéré à chaque build.
"""
import argparse, json, os, re, sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML manquant : pip install pyyaml")

SKIP_DIRS = {"node_modules", "vendor", "_site", ".git", ".github", "scripts"}
EXT = (".html", ".md", ".markdown")
FM = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.S)
SPLIT = re.compile(r"[|;=@&,<>\s]+")


def walk(root):
    for d, dirs, files in os.walk(root):
        dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS and not x.startswith((".", "_")))
        for f in sorted(files):
            if f.endswith(EXT) and not f.startswith(("_", ".")):
                yield os.path.join(d, f)


def front_matter(path):
    with open(path, encoding="utf-8-sig") as fh:
        txt = fh.read()
    m = FM.match(txt)
    if not m:
        return None
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        # une page cast illisible est une erreur franche (Jekyll aussi la rejetterait)
        if re.search(r"^(cast|tabs|staff|artist):", m.group(1), re.M):
            sys.exit("Front matter illisible dans %s : %s" % (path, e))
        return None
    return data if isinstance(data, dict) else None


def strings(node):
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for k, v in node.items():
            yield from strings(v)
    elif isinstance(node, (list, tuple)):
        for v in node:
            yield from strings(v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default=None)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    out = a.out or os.path.join(root, "_data", "appearances.json")

    slugs, dub_pages = set(), []
    for p in walk(root):
        fm = front_matter(p)
        if not fm:
            continue
        rel = os.path.relpath(p, root).replace(os.sep, "/")
        if fm.get("artist"):
            slugs.add(str(fm["artist"]).strip())
        if fm.get("cast") or fm.get("tabs") or fm.get("staff"):
            dub_pages.append((rel, fm))

    result = {}
    for rel, fm in dub_pages:
        seen = set()
        for s in strings({k: v for k, v in fm.items() if k not in ("title", "layout")}):
            for tok in SPLIT.split(s):
                if tok in slugs:
                    seen.add(tok)
        for slug in seen:
            result.setdefault(slug, []).append(rel)
    result = {k: sorted(v) for k, v in sorted(result.items())}

    print("fiches artistes : %d | pages de doublage : %d | fiches avec crédits : %d | liens : %d"
          % (len(slugs), len(dub_pages), len(result), sum(len(v) for v in result.values())))
    if not dub_pages:
        sys.exit("Aucune page cast/tabs/staff trouvée : fichier NON écrit (mauvais dossier ?)")
    if a.check:
        return
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=1)
    print("écrit :", os.path.relpath(out, root))


if __name__ == "__main__":
    main()
