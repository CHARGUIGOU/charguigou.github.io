---
layout: artist
# ============================================================
# MODÈLE DE FICHE COMÉDIEN / STUDIO — copie ce fichier dans artists/ sous le nom du comédien (ex : artists/jason-chau.md), retire le "_" au début du nom et remplis ce que tu connais. Tout est facultatif sauf "artist".
# Les lignes qui commencent par "#" sont désactivées : enlève le "#" pour les utiliser.
# Sans "photo" : silhouette grise ; sans "dates" : Unknown dates (artistes seulement).
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
#   Sur la page Voice Artists seulement : annuaire "Nom, Prénom" → "Chau, Jason" (pseudo retourné : son dernier mot = nom de famille ;
#   pseudo d'un seul mot = tel quel), ou "Zau, Sai-hang" / "Pérez, Pedro" sans pseudo. Le classement alphabétique suit ce nom.
# ------------------------------------------------------------
artist: jason-chau            # l'identifiant utilisé dans les pages de cast (sans espaces ni majuscules)
nickname: "Jason Chau"        # pseudo / nom d'usage entre guillemets (version latine)
# native_nickname: "大J"      # pseudo natif entre guillemets
family_name: "Zau"            # nom de famille (lettres latines)
first_name: "Sai-hang"        # prénom (lettres latines)
native_name: "周世鏗"          # nom natif
name_order: family            # "family" = nom de famille d'abord à l'affichage ; supprime cette ligne pour « Prénom Nom »
# prefix: "Slime's wife"      # texte avant le nom (rare)
# display: "Texte libre"      # texte complet affiché tel quel PARTOUT (cast, staff, chansons, fiche) à la place du nom composé
# page_name: "Texte libre"    # nom affiché SOUS LA PHOTO de la fiche uniquement (une ligne, texte libre) ; les pages de cast gardent le nom normal
# short_name: "Chau, Jason"   # nom sous la photo dans les cartes (défaut : pseudo, sinon nom composé) ET nom affiché tel quel sur la page Voice Artists
# script: cantonese           # police du nom natif (une seule est chargée). Valeurs : arabic, armenian, bengali, cantonese, chinese-simplified, chinese-traditional, cyrillic, georgian, greek, hebrew, hindi, marathi, japanese, kannada, korean, malayalam, tamil, telugu, thai

# photo: "https://res.cloudinary.com/dofvjifeo/image/upload/Jason_Chau.png"   # sans cette ligne : silhouette grise
# address: "Rue, ville"          # ligne d'adresse (surtout pour les studios), affichée sous les dates et au-dessus du pays
country: "Hong Kong"             # pays d’origine, affiché sous l’adresse sur la fiche ; pour un studio, sert aussi au filtre Country de la page Voice Artists
# dates: "4 November 1982 -  "   # artiste : sans cette ligne, « Unknown dates » ; studio : rien ne s'affiche si la ligne est absente
# kind: studio                   # fiche d'un STUDIO : icône de bâtiment, dates facultatives ; nom complet dans display. photo, address, country et texte libre fonctionnent comme pour un artiste
# thumb_fit: cover               # studios seulement : recadre la vignette de la page Voice Artists en carré (sans cette ligne : image entière, pour les logos)
# gallery:                       # photos supplémentaires : colle seulement le lien Cloudinary ORIGINAL (la miniature allégée est calculée toute seule)
#   - "https://res.cloudinary.com/dofvjifeo/image/upload/Jason_Chau_2.jpg | Légende facultative"
#   - "https://res.cloudinary.com/dofvjifeo/image/upload/Jason_Chau_3.jpg"
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
