#!/usr/bin/env python3
"""
Génère les fiches artistes (artists/<identifiant>.md) à partir d'UN tableau Excel :
    _data/artists.xlsx      (ou _data/artists.csv)

Une ligne du tableau = une fiche. Les fiches écrites à la main dans artists/ restent
prioritaires : si un identifiant existe déjà en .md, la ligne du tableau est ignorée.

Les fiches générées ne sont PAS à committer : elles sont recréées à chaque build
(étape du workflow GitHub, voir LISEZMOI.md).

Usage (depuis la racine du dépôt) :
    python _scripts/generate_artists.py            # génère artists/*.md
    python _scripts/generate_artists.py --check    # vérifie le tableau, n'écrit rien
"""
import argparse, csv, datetime, glob, io, os, re, sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML manquant : pip install pyyaml")

COLUMNS = ["artist", "nickname", "native_nickname", "family_name", "first_name", "native_name",
           "name_order", "full_name", "other_names", "prefix", "display", "page_name", "short_name",
           "script", "photo", "address", "country", "dates", "kind", "thumb_fit", "gallery", "bio"]
LIST_COLS = {"other_names", "gallery"}
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARK = "generated: true"


def norm_header(h):
    return re.sub(r"[\s\-]+", "_", str(h or "").strip().lower())


def cell_text(v):
    if v is None:
        return ""
    if isinstance(v, (datetime.datetime, datetime.date)):
        d = v.date() if isinstance(v, datetime.datetime) else v
        return "%d %s %d -  " % (d.day, d.strftime("%B"), d.year)
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return str(v).strip()


def read_xlsx(path):
    try:
        import openpyxl
    except ImportError:
        sys.exit("openpyxl manquant : pip install openpyxl")
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb["Artistes"] if "Artistes" in wb.sheetnames else wb[wb.sheetnames[0]]
    rows = list(ws.iter_rows(values_only=True))
    return rows


def read_csv(path):
    raw = open(path, encoding="utf-8-sig", newline="").read()
    first = raw.splitlines()[0] if raw else ""
    delim = max([",", ";", "\t"], key=first.count)
    return list(csv.reader(io.StringIO(raw), delimiter=delim))


def existing_hand_slugs(artists_dir):
    slugs = {}
    for p in glob.glob(os.path.join(artists_dir, "*.md")):
        if os.path.basename(p).startswith("_"):
            continue
        txt = open(p, encoding="utf-8-sig").read()
        if re.search(r"^generated:\s*true\s*$", txt.split("\n---", 1)[0], re.M):
            os.remove(p)            # ancienne fiche générée (exécution locale) : on la refait
            continue
        m = re.match(r"---\r?\n(.*?)\r?\n---", txt, re.S)
        try:
            fm = yaml.safe_load(m.group(1)) if m else None
        except yaml.YAMLError:
            fm = None
        slug = fm.get("artist") if isinstance(fm, dict) else None
        slugs[str(slug or os.path.splitext(os.path.basename(p))[0])] = p
    return slugs


def split_items(text):
    parts = re.split(r"[\r\n]+", text)
    return [x.strip() for x in parts if x.strip()]


def build_front(row):
    fm = {"layout": "artist", "generated": True}
    fm["artist"] = row["artist"]
    for col in COLUMNS[1:]:
        v = row.get(col, "")
        if col == "bio" or v == "":
            continue
        if col == "other_names":
            items = [x.strip() for x in re.split(r"[;\r\n]+", v) if x.strip()]
            v = items if len(items) > 1 else (items[0] if items else "")
        elif col == "gallery":
            v = split_items(v)
        elif col == "name_order":
            if v.lower() not in ("family", "famille", "nom"):
                continue
            v = "family"
        elif col == "kind":
            if v.lower() != "studio":
                continue
            v = "studio"
        elif col == "thumb_fit":
            if v.lower() != "cover":
                continue
            v = "cover"
        elif col == "script":
            v = v.lower()
        if v != "" and v != []:
            fm[col] = v
    return fm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--table", default=None)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    artists_dir = os.path.join(root, "artists")

    table = a.table
    if not table:
        for cand in ("_data/artists.xlsx", "_data/artists.csv"):
            if os.path.exists(os.path.join(root, cand)):
                table = os.path.join(root, cand)
                break
    if not table or not os.path.exists(table):
        print("Aucun tableau (_data/artists.xlsx ou .csv) : rien à générer.")
        return
    rows = read_xlsx(table) if table.lower().endswith(".xlsx") else read_csv(table)
    if not rows:
        print("Tableau vide.")
        return

    headers = [norm_header(h) for h in rows[0]]
    unknown = [h for h in headers if h and h not in COLUMNS]
    for h in unknown:
        print("ATTENTION : colonne inconnue ignorée :", h)
    if "artist" not in headers:
        sys.exit("ERREUR : la colonne « artist » (identifiant) est introuvable en première ligne du tableau.")

    hand = existing_hand_slugs(artists_dir) if os.path.isdir(artists_dir) else {}
    made, skipped_hand, problems, seen = [], [], [], set()
    for n, r in enumerate(rows[1:], start=2):
        row = {h: cell_text(r[i]) if i < len(r) else "" for i, h in enumerate(headers) if h in COLUMNS}
        slug = row.get("artist", "")
        if not any(row.values()) or slug.startswith("#"):
            continue
        if not slug:
            problems.append("ligne %d : identifiant (artist) vide, ligne ignorée" % n)
            continue
        if not SLUG.match(slug):
            problems.append("ligne %d : identifiant « %s » invalide (minuscules, chiffres et tirets, sans accent ni espace), ligne ignorée" % (n, slug))
            continue
        if slug in seen:
            problems.append("ligne %d : identifiant « %s » en double, ligne ignorée" % (n, slug))
            continue
        seen.add(slug)
        if slug in hand:
            skipped_hand.append(slug)
            continue
        fm = build_front(row)
        if not any(k in fm for k in ("nickname", "family_name", "first_name", "display", "native_name", "full_name")):
            problems.append("ligne %d (%s) : aucun nom renseigné, la fiche s'affichera avec son identifiant" % (n, slug))
        made.append((slug, fm, row.get("bio", "")))

    print("tableau : %s" % os.path.relpath(table, root))
    print("fiches à générer : %d | fiches manuelles prioritaires (ignorées) : %d | problèmes : %d"
          % (len(made), len(skipped_hand), len(problems)))
    for p in problems:
        print("  -", p)
    if skipped_hand:
        print("  fiches manuelles gardées :", ", ".join(sorted(skipped_hand)))
    if a.check:
        return
    os.makedirs(artists_dir, exist_ok=True)
    for slug, fm, bio in made:
        head = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False, width=10000)
        body = (bio + "\n") if bio else ""
        txt = ("---\n# Fiche GÉNÉRÉE depuis _data/artists.xlsx : modifie le tableau, pas ce fichier.\n"
               + head + "---\n" + body)
        with open(os.path.join(artists_dir, slug + ".md"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(txt)
    print("écrit : %d fichiers dans artists/" % len(made))


if __name__ == "__main__":
    main()
