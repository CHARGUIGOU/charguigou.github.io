---
layout: artist
# ============================================================
# MODÈLE DE FICHE COMÉDIEN / STUDIO — copie ce fichier dans artists/ sous le nom du comédien (ex : artists/jason-chau.md), retire le "_" au début du nom et remplis ce que tu connais. Tout est facultatif sauf "artist".
# Les lignes qui commencent par "#" sont désactivées : enlève le "#" pour les utiliser. Sans "photo" : silhouette grise ; sans "dates" : Unknown dates (artistes seulement).
# TEXTE LIBRE (bio) : il se met EN BAS du fichier, sous le second "---". Pour l'afficher, écris ton texte ENTRE les deux lignes "comment" et "endcomment" puis supprime ces deux lignes (celles avec les accolades).
# Pour le désactiver à nouveau, remets-les autour du texte. Un "#" ne désactive rien dans cette zone : il transforme la ligne en gros titre. HTML et Markdown fonctionnent (le Markdown n'est pas interprété à l'intérieur d'une balise HTML).
# ============================================================
# ------------------------------------------------------------
# NOMS
#   Nom d'usage (pseudo) :   nickname + native_nickname      → "Jason Chau" / "大J"        (facultatifs)
#   Nom de la personne :     family_name + first_name         → Zau Sai-hang                (lettres latines)
#                            native_name                       → 周世鏗
#   Ordre d'affichage (casts, fiches) : name_order: family  = nom de famille d'abord (Zau Sai-hang, Kovács Béla)
#                                       (absent)            = prénom d'abord          (Pedro Pérez)
#   Affiché dans les casts et les fiches :  "Jason Chau" Zau Sai-hang / "大J" 周世鏗
#   Sans pseudo (ex : cast espagnol) :  family_name: "Pérez" + first_name: "Pedro"  →  Pedro Pérez
#   Noms en plus (fiche seulement) : full_name = nom complet ; other_names = autres noms connus (« Also known as : ») ; tous deux cherchables sur la page Voice Artists
#   Sur la page Voice Artists seulement : annuaire "Nom, Prénom" → "Chau, Jason" (pseudo retourné : son dernier mot = nom de famille ;
#   pseudo d'un seul mot = tel quel), ou "Zau, Sai-hang" / "Pérez, Pedro" sans pseudo. Le classement alphabétique suit ce nom.
# ------------------------------------------------------------
artist: alberto-mieza            # l'identifiant utilisé dans les pages de cast (sans espaces ni majuscules)
family_name: "Mieza"            # nom de famille (lettres latines)
first_name: "Alberto"        # prénom (lettres latines)
# full_name: "Emilio Javier Moreno Santa Cruz"   # nom complet, affiché en petit sous le nom sur la fiche (casts et liste : inchangés). Texte libre : tu peux y mettre le nom natif à la suite, ex : "Zau Sai-hang Wai / 周世鏗"
# other_names:                  # autres noms connus : affichés « Also known as : … » sous le nom, sur la fiche. Une liste, ou un seul texte
#    - "Naranjito"
# prefix: "Slime's wife"      # texte avant le nom (rare)
# display: "Texte libre"      # texte complet affiché tel quel PARTOUT (cast, staff, chansons, fiche) à la place du nom composé
# page_name: "Texte libre"    # nom affiché SOUS LA PHOTO de la fiche uniquement (une ligne, texte libre) ; les pages de cast gardent le nom normal
# short_name: "Chau, Jason"   # nom sous la photo dans les cartes (défaut : pseudo, sinon nom composé) ET nom affiché tel quel sur la page Voice Artists

# photo: "Alberto_Mieza.png"      # NOM DU FICHIER Cloudinary seulement (l'adresse de base est dans _data/photos.yml ; les dossiers Cloudinary ne comptent pas). Sans cette ligne : silhouette grise
country: "Spain"             # pays d'origine, affiché sous l'adresse sur la fiche (sans cette ligne : rien) ; pour un studio, sert aussi au filtre Country de la page Voice Artists
# dates: "4 November 1982 -  "   # artiste : sans cette ligne, « Unknown dates » ; studio : rien ne s'affiche si la ligne est absente
# gallery:                       # photos supplémentaires : seulement le nom du fichier Cloudinary (la miniature allégée est calculée toute seule)
#   - "Jason_Chau_2.jpg | Légende facultative"
#   - "Jason_Chau_3.jpg"
#

# ------------------------------------------------------------
# CRÉDITS AJOUTÉS « EN DUR » (à la main)
# Les rôles / chansons / postes qui viennent des pages de cast s'ajoutent tout seuls. Utilise ces listes seulement pour ce qui n'a PAS de page de cast (film pas encore fait, etc.).
# Les lignes ayant le même film + année + langue sont regroupées dans une seule ligne de tableau. Les rôles ajoutés comptent dans le résumé en haut. Champs séparés par " | ".
# L'année peut être complète (2018-11-21) : tri sur la date complète, affichage de l'année seule. Chaque ligne commence par DEUX ESPACES puis un tiret ; la ligne "extra_roles:" elle-même est sans "#" et sans espace devant.
#
extra_roles:        # "rôle | film | année | langue | id du personnage (facultatif, pour la vignette)"
#  - "Ralph | Ralph Breaks the Internet | 2018 | Cantonese | ralph"
#  - "Additional voices | Frozen | 2013 | Cantonese"
# extra_songs:        # "titre | film | année | langue | personnage"
#   - "Let It Go | Frozen | 2013 | Cantonese | Elsa"
# extra_credits:      # "poste | film | année | langue"
#   - "Dialogue director | Zootopia | 2016 | Cantonese"
# ------------------------------------------------------------
---
{% comment %}
Écris ici ton texte libre (bio, anecdotes) : il s'affichera sous le nom, au-dessus des tableaux.
{% endcomment %}