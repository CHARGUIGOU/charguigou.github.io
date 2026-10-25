# Dossier _scripts : outils lancés à la construction du site

Ces fichiers ne sont pas publiés (le nom du dossier commence par `_`). Ils ne servent que
quand le workflow GitHub personnalisé est activé (voir « Activer » plus bas).

## 1. Le tableau unique des artistes (`_data/artists.xlsx`)
Une ligne = une fiche. Au moment de la construction, `generate_artists.py` crée
automatiquement `artists/<identifiant>.md` pour chaque ligne. Plus de fichiers à écrire à la main,
plus d'erreurs de guillemets : le script écrit la fiche correctement.

- Le fichier `artists.xlsx` contient une feuille « Artistes » (le tableau) et une feuille « Aide »
  (explication de chaque colonne).
- Les lignes dont l'identifiant commence par `#` sont ignorées (les 3 exemples en gris).
- Les fiches écrites à la main dans `artists/` restent PRIORITAIRES : si le même identifiant existe
  en .md, la ligne du tableau est ignorée. À garder en .md : les fiches avec rôles ajoutés à la main
  (`extra_roles`), ou un champ ancien (`romanization`, `native`).
- Pour modifier : ouvre `artists.xlsx` dans Excel, change ou ajoute des lignes, enregistre,
  puis sur GitHub : dossier `_data` > Add file > Upload files > commit (il remplace l'ancien).
- Un fichier `artists.csv` fonctionne aussi (séparateur virgule ou point-virgule, UTF-8).

## 2. Le pré-calcul (`build_appearances.py`)
Accélère le build quand il y a beaucoup de fiches (chaque fiche ne lit que les pages de cast où
l'artiste apparaît). Le fichier `_data/appearances.json` est créé à chaque build : ne pas le committer.

## Activer (une seule fois, environ 5 minutes)
1. Crée `.github/workflows/pages.yml` avec le contenu de `_scripts/pages-workflow.yml.disabled`
   (vérifie le nom de ta branche, `main` ou `master`, ligne `branches`).
2. Sur GitHub : Settings > Pages > Build and deployment > Source : choisis « GitHub Actions ».
3. Fais un commit. Le run affiche dans le journal les lignes « fiches à générer : N ... »
   et « fiches artistes : N | pages de doublage : M ... ».
4. Ouvre une fiche et une page de cast pour vérifier.

## Revenir en arrière
Settings > Pages > Source : « Deploy from a branch », et supprime `.github/workflows/pages.yml`.
Aucun contenu n'est touché (le tableau et tes fiches .md restent là, mais les fiches du tableau
ne seront plus créées).

## Tester à la main (facultatif)
    pip install pyyaml openpyxl
    python _scripts/generate_artists.py --check     # vérifie le tableau

## 3. Le tableau des personnages (`_data/characters.xlsx`)
Même principe que pour les artistes : le fichier `_data/characters.yml` est recréé à chaque build à partir du tableau.
- Feuille « Personnages » : une ligne = un personnage (id, name, img, franchise, keywords, link, **visible**).
- Feuille « Apparitions » : une ligne = un film où il apparaît (character, film, year, keywords, img, lead, upcoming).
- `visible` = `no` : le personnage n'apparaît pas sur la page Character voices, mais son image reste utilisable dans les casts et les fiches.
- Pour modifier : ouvre `characters.xlsx`, change ou ajoute des lignes, enregistre, puis sur GitHub : dossier `_data` > Add file > Upload files > commit.
- Ne modifie plus `characters.yml` à la main : il est réécrit à chaque build. Seul `image_base` (début des URLs d'images) y reste lu.
- Vérifier le tableau à la main : `python _scripts/generate_characters.py --check`
