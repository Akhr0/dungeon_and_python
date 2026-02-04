# Step 00 - Variables (version simplifiée)
# Objectif: comprendre ce qu'est une VARIABLE en Python
#
# NOTE PEDAGOGIQUE IMPORTANTE:
# - Dans les premiers steps, quand une notion apparait pour la
#   PREMIERE fois, on la detaille beaucoup.
# - Quand la notion a deja ete expliquee, on ne la redeveloppe pas
#   en profondeur pour eviter de surcharger.
# - Le suivi est note dans: cours_20_etapes/JOURNAL_NOTIONS.md

# ------------------------------------------------------------
# MINI-FICHE - VARIABLES
# ------------------------------------------------------------
#
# Une VARIABLE est une boite avec un nom qui contient une valeur.
#
# Exemple:
#   player_hp = 10
#
# Ici:
# - "player_hp" est le nom de la variable
# - 10 est la valeur stockee
#
# -------------------------
# TYPES DE VARIABLES
# -------------------------
#
# int    -> nombres entiers
#   ex: 10, 0, -3
#
# str    -> texte (entre guillemets)
#   ex: "Gandalf", "Bonjour"
#
# bool   -> vrai ou faux
#   True / False
#
# -------------------------
# POURQUOI DES VARIABLES ?
# -------------------------
#
# - Pour eviter de recopier des valeurs partout
# - Pour pouvoir changer le comportement du programme
#   en modifiant UNE seule ligne
#
# ------------------------------------------------------------


import pygame  # Bibliothèque pour créer une fenêtre et afficher des choses

# ------------------------------------------------------------
# 1) VARIABLES (LE COEUR DU CHAPITRE)
# ------------------------------------------------------------

# VARIABLE de type int (nombre entier)
player_hp = 10

# VARIABLE de type string (texte)
player_name = "Gandalf"

# VARIABLE de type bool (vrai ou faux)
player_is_alive = True


# ------------------------------------------------------------
# 2) INITIALISATION PYGAME (minimum vital)
# ------------------------------------------------------------

pygame.init()  # Démarre pygame

# Création d'une petite fenêtre fixe
# pygame.display.set_mode((largeur, hauteur))
# - "display" = ce qui concerne la fenetre
# - "set_mode" = creer la fenetre
# - (400, 200) = taille en pixels
screen = pygame.display.set_mode((400, 200))

# pygame.display.set_caption("...")
# - definit le texte affiche en haut de la fenetre
pygame.display.set_caption("Step 00 - Variables")

# Police pour afficher du texte
# pygame.font.SysFont("nom", taille)
# - cree un objet "font" pour dessiner du texte plus tard
font = pygame.font.SysFont("arial", 22)

# ------------------------------------------------------------
# 3) BOUCLE PRINCIPALE
# ------------------------------------------------------------
# Même si on ne parle pas encore de "game loop",
# cette boucle est NECESSAIRE pour garder la fenêtre ouverte.

running = True
while running:

    # --------------------------------------------------------
    # 3A) EVENEMENTS (fermer la fenêtre)
    # --------------------------------------------------------
    # pygame.event.get() renvoie une liste d'evenements.
    # Exemple d'evenement:
    # - clic souris
    # - touche clavier
    # - fermeture fenetre (QUIT)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --------------------------------------------------------
    # 3B) AFFICHAGE
    # --------------------------------------------------------

    # Couleur de fond (gris foncé)
    screen.fill((30, 30, 30))

    # --------------------------------------------------------
    # 3C) TEXTE = AFFICHAGE DES VARIABLES
    # --------------------------------------------------------
    # f"..." permet d'insérer directement les variables dans le texte

    line1 = f"Nom du joueur : {player_name}"
    line2 = f"Points de vie : {player_hp}"
    line3 = f"En vie ? : {player_is_alive}"

    # Couleur du texte
    text_color = (230, 230, 230)

    # font.render(...) transforme le texte en image
    # font.render(text, antialias, color)
    # screen.blit(...) affiche cette image à l'écran
    screen.blit(font.render(line1, True, text_color), (20, 20))
    screen.blit(font.render(line2, True, text_color), (20, 55))
    screen.blit(font.render(line3, True, text_color), (20, 90))

    # --------------------------------------------------------
    # 3D) VISUALISATION DU BOOL (optionnel mais très parlant)
    # --------------------------------------------------------
    # Si la variable booléenne est True, on dessine un carré vert
    # Sinon, un carré rouge
    #
    # DETAIl IMPORTANT (premiere rencontre de pygame.draw.rect):
    # pygame.draw.rect(surface, couleur, rectangle)
    #
    # 1) surface  -> ou dessiner (ici: screen)
    # 2) couleur  -> tuple RGB (Rouge, Vert, Bleu)
    #                chaque valeur va de 0 a 255
    #                ex: (50, 200, 50) = vert
    # 3) rectangle -> (x, y, largeur, hauteur)
    #                x = position horizontale (gauche -> droite)
    #                y = position verticale (haut -> bas)
    #
    # Donc ici:
    # (300, 50, 50, 50) = carre de 50x50, place vers la droite

    if player_is_alive:
        pygame.draw.rect(screen, (50, 200, 50), (300, 50, 50, 50))
    else:
        pygame.draw.rect(screen, (200, 50, 50), (300, 50, 50, 50))

    # --------------------------------------------------------
    # 3E) RAFRAICHIR L'ECRAN
    # --------------------------------------------------------
    # pygame.display.flip() "montre" a l'ecran tout ce qu'on vient
    # de dessiner pendant cette iteration de boucle.
    pygame.display.flip()

# ------------------------------------------------------------
# 4) FERMETURE PROPRE
# ------------------------------------------------------------
pygame.quit()


# ------------------------------------------------------------
# EXERCICE - MANIPULER DES VARIABLES
# ------------------------------------------------------------
#
# Objectif :
# Comprendre qu'une VARIABLE est une valeur que l'on peut
# modifier pour changer ce qui s'affiche a l'ecran.
#
# IMPORTANT :
# - Tu n'as PAS besoin de toucher au reste du code.
# - Tu dois UNIQUEMENT modifier les VARIABLES en haut du fichier.
#
# ------------------------------------------------------------
# 1) MODIFIER DES VARIABLES SIMPLES
# ------------------------------------------------------------
#
# - Change la valeur de player_name
#   -> Mets ton propre prenom a la place.
#
# - Change la valeur de player_hp
#   -> Essaye avec 20, puis avec 1.
#
# - Change la valeur de player_is_alive
#   -> Passe-la de True a False.
#   -> Observe ce qui change a l'ecran.
#
# ------------------------------------------------------------
# 2) BONUS : AJOUTER UNE NOUVELLE VARIABLE
# ------------------------------------------------------------
#
# - Cree une nouvelle variable :
#     player_level
#
# - Donne-lui une valeur de depart (par exemple 1).
#
# - Affiche cette variable a l'ecran comme les autres.
#
# ------------------------------------------------------------
# FIN
# ------------------------------------------------------------
