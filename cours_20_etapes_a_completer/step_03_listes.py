# Step 03 - Lists
# Objectif: comprendre les LISTES en Python
# et les utiliser pour stocker plusieurs positions de murs.
#
# IDEE CLE DU CHAPITRE:
# - Une LISTE permet de stocker PLUSIEURS elements dans UNE variable
# - On peut verifier si un element est DANS une liste
# - Ici: une liste de murs empêche le joueur d'avancer



# ------------------------------------------------------------
# MINI FICHE - LISTES (A RETENIR)
# ------------------------------------------------------------
#
# Une liste = plusieurs valeurs dans une seule variable.
#
# Exemple:
#   blocks = [(3, 3), (3, 4), (4, 4)]
#
# Chaque element de la liste est ici une position (x, y).
# Une liste s'ecrit toujours entre crochets
#
# IMPORTANT:
# Ici, chaque position (x, y) est un TUPLE.
# Un tuple ressemble a une liste, mais avec des parentheses:
#   (3, 4)
# On l'utilise souvent pour des coordonnees fixes.
#
# -------------------------
# ACCES PAR INDEX
# -------------------------
# Les listes sont numerotees a partir de 0.
# On peut acceder a un élément en rentrant le nom de la liste et l'idex de l'élément entre crochets
#
#   blocks[0] -> premier element
#   blocks[1] -> deuxieme element
#
# Exemple:
#   premier_block = blocks[0]
#   x = premier_block[0]
#   y = premier_block[1]
#
# -------------------------
# AJOUTER UN ELEMENT (append)
# -------------------------
# Ajoute a la fin de la liste:
#   blocks.append((5, 5))
#
# -------------------------
# SUPPRIMER UN ELEMENT (remove)
# -------------------------
# Supprime l'element (s'il existe) :
#   blocks.remove((5, 5))
#
# Attention:
# - remove cherche la valeur
# - si elle n'existe pas, Python fait une erreur
#
# -------------------------
# SUPPRIMER PAR INDEX (pop)
# -------------------------
# Enleve l'element a un index et le renvoie.
#   dernier = blocks.pop()     # enleve le dernier
#   premier = blocks.pop(0)    # enleve le premier
#
# -------------------------
# TAILLE D'UNE LISTE (len)
# -------------------------
#   len(blocks) -> nombre d'elements dans la liste
#
# -------------------------
# TESTER "DANS LA LISTE" (in)
# -------------------------
#   (3, 3) in blocks      -> True/False
#   (3, 3) not in blocks  -> True/False
#
# ------------------------------------------------------------



# VERSION ELEVE A COMPLETER
# Complete uniquement les zones balisees dans ce fichier.

import pygame

# ------------------------------------------------------------
# 1) VARIABLES DE LA GRILLE (deja vues)
# ------------------------------------------------------------

GRID_W = 10
GRID_H = 8
TILE_SIZE = 64

SCREEN_WIDTH = GRID_W * TILE_SIZE
SCREEN_HEIGHT = GRID_H * TILE_SIZE

# ------------------------------------------------------------
# 2) INITIALISATION PYGAME
# ------------------------------------------------------------

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Step 03 - Lists")
clock = pygame.time.Clock()

# ------------------------------------------------------------
# 3) VARIABLES DU JOUEUR
# ------------------------------------------------------------

# Position du joueur EN CASES
player_x = 1
player_y = 1

# ------------------------------------------------------------
# 4) LA LISTE DE MURS (COEUR DU CHAPITRE)
# ------------------------------------------------------------
# A RETENIR:
# - Une liste est entouree de crochets [ ]
# - Elle peut contenir plusieurs elements
# - Ici, chaque mur est represente par une position (x, y)

# ============================================================
# >>>>>>>>>>>>>> ZONE A COMPLETER PAR L'ELEVE >>>>>>>>>>>>>>>
# >>> Ecris ton code ENTRE les deux balises START / END
# >>> START CODE ELEVE
# (Attendu: une liste de tuples, exemple [(3, 3), (3, 4), ...])
blocks = []
# <<< END CODE ELEVE
# <<<<<<<<<<<<<< FIN ZONE A COMPLETER <<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================

# ------------------------------------------------------------
# 5) VARIABLES DE CONTROLE (comme au Step 02)
# ------------------------------------------------------------

gauche = 0
droite = 0
haut = 0
bas = 0

# ------------------------------------------------------------
# 6) BOUCLE PRINCIPALE
# ------------------------------------------------------------

running = True
while running:

    # --------------------------------------------------------
    # 6A) EVENEMENTS (fermer la fenêtre)
    # --------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --------------------------------------------------------
    # 6B) LECTURE DU CLAVIER (partie technique)
    # --------------------------------------------------------
    keys = pygame.key.get_pressed()

    gauche = 1 if keys[pygame.K_LEFT] else 0
    droite = 1 if keys[pygame.K_RIGHT] else 0
    haut = 1 if keys[pygame.K_UP] else 0
    bas = 1 if keys[pygame.K_DOWN] else 0

    # --------------------------------------------------------
    # 6C) CALCUL DE LA NOUVELLE POSITION (sans bouger encore)
    # --------------------------------------------------------
    # IMPORTANT:
    # - On ne bouge PAS le joueur tout de suite
    # - On calcule d'abord la position qu'il AURAIT si on autorise le mouvement

    new_x = player_x
    new_y = player_y

    if gauche == 1:
        new_x -= 1
    elif droite == 1:
        new_x += 1
    elif haut == 1:
        new_y -= 1
    elif bas == 1:
        new_y += 1

    # --------------------------------------------------------
    # 6D) CONDITIONS AVEC LA LISTE DE MURS
    # --------------------------------------------------------
    # A RETENIR:
    # - "in" permet de verifier si une valeur est dans une liste
    # - (new_x, new_y) est UNE position
    # - blocks est la liste de toutes les positions bloquees

    # 1) On verifie que la position est dans la grille
    if 0 <= new_x < GRID_W and 0 <= new_y < GRID_H:

        # 2) On verifie que la position n'est PAS dans la liste des murs
        if (new_x, new_y) not in blocks:
            player_x = new_x
            player_y = new_y

    # --------------------------------------------------------
    # 6E) AFFICHAGE
    # --------------------------------------------------------

    screen.fill((30, 30, 30))

    # Dessin des murs
    # A RETENIR:
    # - On utilise une boucle for pour parcourir la liste
    # - Chaque element de la liste est une position (x, y)
    # - "for wx, wy in blocks" veut dire:
    #   Python prend chaque tuple (x, y) et le "decompose"
    #   automatiquement en 2 variables:
    #   wx = x et wy = y
    for wx, wy in blocks:
        pygame.draw.rect(
            screen,
            (80, 80, 80),
            (
                wx * TILE_SIZE,
                wy * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE,
            ),
        )

    # Dessin du joueur
    pygame.draw.rect(
        screen,
        (200, 50, 50),
        (
            player_x * TILE_SIZE,
            player_y * TILE_SIZE,
            TILE_SIZE,
            TILE_SIZE,
        ),
    )

    pygame.display.flip()
    clock.tick(6)

# ------------------------------------------------------------
# 7) FIN DU PROGRAMME
# ------------------------------------------------------------

pygame.quit()


# ------------------------------------------------------------
# EXERCICE - MANIPULER DES LISTES
# ------------------------------------------------------------
#
# Objectif :
# Comprendre qu'une LISTE permet de stocker plusieurs positions
# et de controler le comportement du jeu.
#
# IMPORTANT :
# - Tu ne dois PAS modifier la logique du programme
# - Tu travailles UNIQUEMENT avec la liste "blocks"
#
# ------------------------------------------------------------
# 1) MODIFIER LA LISTE (ajouter des elements)
# ------------------------------------------------------------
#
# - Ajoute un nouveau block a la position (5, 5)
# - Ajoute un block juste a droite du joueur au depart
#   (le joueur commence en (1, 1), donc a droite c'est (2, 1))
#
# Observe ce qui se passe quand tu essaies de passer dessus.
#
# ------------------------------------------------------------
# 2) CREER UNE LIGNE DE BLOCKS (avec une boucle for)
# ------------------------------------------------------------
#
# Objectif :
# - Creer une ligne horizontale de blocks sur y = 6
#
# Indices :
# - Tu peux partir d'une liste vide:
#     blocks = []
# - Tu peux ajouter un element a une liste avec:
#     blocks.append((x, y))
# - Tu peux repeter une action avec une boucle for:
#     for x in range(...):
#         ...
#
# ------------------------------------------------------------
# 3) BONUS - CREER UNE OUVERTURE DANS LA LIGNE
# ------------------------------------------------------------
#
# Objectif :
# - Faire un "passage" dans ta ligne de blocks (une case sans mur)
#
# Indices :
# - Tu peux supprimer un element de la liste avec:
#     blocks.remove((x, y))
#
# Exemple :
# - Si tu veux une ouverture en (5, 6), tu dois supprimer (5, 6) de la liste.
#
# ------------------------------------------------------------
# FIN
# ------------------------------------------------------------
