# Pré-calcul des apparitions (optionnel, à activer plus tard)

## Où on en est
- `_layouts/artist.html` (nouvelle version) fonctionne dans les DEUX cas :
  - sans `_data/appearances.json` : comportement actuel, rien ne change ;
  - avec `_data/appearances.json` : chaque fiche ne lit que les pages où l'artiste apparaît.
- Le fichier `_data/appearances.json` n'est PAS à committer : il est créé à chaque build par le script.
- Ce dossier commence par `_` : Jekyll ne le publie pas sur le site.

## Quand l'activer
Quand l'étape « Build with Jekyll » dépasse ~60 à 90 secondes, ou quand il y a plusieurs centaines de fiches.

## Comment l'activer (5 minutes)
1. Crée `.github/workflows/pages.yml` avec le contenu de `_scripts/pages-workflow.yml.disabled`
   (vérifie le nom de ta branche, `main` ou `master`, ligne `branches`).
2. Sur GitHub : Settings > Pages > Build and deployment > Source : choisis « GitHub Actions ».
3. Fais un commit. Le premier run affiche « fiches artistes : N | pages de doublage : M ... ».
4. Compare une fiche avant/après : les rôles doivent être identiques.

## Pour revenir en arrière
Settings > Pages > Source : « Deploy from a branch », et supprime `.github/workflows/pages.yml`.
Rien d'autre à changer, aucun contenu n'est touché.

## Tester le script à la main (facultatif)
    pip install pyyaml
    python _scripts/build_appearances.py --check
