# Step 01 - Loops
# Objectif: ajouter la notion de BOUCLE "for" en gardant
# la base du step 00 (boucle while running).
#
# Idee simple du chapitre:
# - "while running" garde la fenetre ouverte
# - "for" repete le dessin de plusieurs cases
#
# Ici, on reste volontairement tres simple.
#
# RAPPEL METHODE:
# - while / pygame.draw.rect / evenements ont deja ete vus au step 00.
# - Nouvelle notion principale de ce step: la boucle for.

import pygame

# ------------------------------------------------------------
# 1) VARIABLES (comme au step 00)
# ------------------------------------------------------------

# Grille: 10 cases en largeur, 8 en hauteur
GRID_W = 10
GRID_H = 8

# Taille d'une case en pixels
TILE_SIZE = 64

# Taille de la fenetre en pixels
SCREEN_WIDTH = GRID_W * TILE_SIZE
SCREEN_HEIGHT = GRID_H * TILE_SIZE

# Position du joueur (en cases)
player_x = 0
player_y = 3

# Vitesse de la boucle de jeu
FPS = 6

# ------------------------------------------------------------
# 2) INITIALISATION PYGAME
# ------------------------------------------------------------

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Step 01 - Loops")
clock = pygame.time.Clock()

# ------------------------------------------------------------
# 3) BOUCLE PRINCIPALE (comme step 00)
# ------------------------------------------------------------

running = True
while running:

    # --------------------------------------------------------
    # 3A) EVENEMENTS
    # --------------------------------------------------------
    # On garde exactement la meme logique que step 00.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --------------------------------------------------------
    # 3B) DESSIN DU FOND
    # --------------------------------------------------------
    screen.fill((30, 30, 30))

    # --------------------------------------------------------
    # 3C) BOUCLE "for" (coeur du chapitre)
    # --------------------------------------------------------
    # PREMIERE RENCONTRE DETAILLEE DU "for":
    #
    # Syntaxe:
    # for variable in sequence:
    #     instructions
    #
    # - "for" veut dire: "repete ce bloc plusieurs fois"
    # - "variable" change de valeur a chaque tour
    # - le ":" est obligatoire en Python
    # - les lignes decalees (indentation) appartiennent a la boucle
    #
    # Ici:
    # - variable = colonne
    # - sequence = range(GRID_W)
    # - donc on repete une fois par colonne de la grille
    #
    # PREMIERE RENCONTRE DETAILLEE DE range(...):
    # range(10) produit:
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    # (10 est exclu)
    #
    # Cette boucle repete le dessin de plusieurs cases.
    #
    # range(GRID_W) donne:
    # 0, 1, 2, ... jusqu'a GRID_W - 1
    #
    # Donc "colonne" prend les valeurs 0 a 9.
    for colonne in range(GRID_W):
        pygame.draw.rect(
            screen,
            (70, 70, 70),  # gris
            (
                colonne * TILE_SIZE,   # x en pixels
                player_y * TILE_SIZE,  # y en pixels (ligne fixe)
                TILE_SIZE,
                TILE_SIZE,
            ),
            1,  # epaisseur du contour
        )

    # --------------------------------------------------------
    # 3D) DESSIN DU JOUEUR
    # --------------------------------------------------------
    pygame.draw.rect(
        screen,
        (200, 50, 50),  # rouge
        (
            player_x * TILE_SIZE,
            player_y * TILE_SIZE,
            TILE_SIZE,
            TILE_SIZE,
        ),
    )

    # --------------------------------------------------------
    # 3E) MOUVEMENT AUTOMATIQUE TRES SIMPLE
    # --------------------------------------------------------
    # Le joueur avance d'une case a chaque frame.
    # Ecriture equivalente:
    # player_x += 1
    #
    # On garde "player_x = player_x + 1" ici
    # car c'est plus explicite pour debuter.
    player_x = player_x + 1

    # Quand il sort de l'ecran a droite,
    # il revient au debut (colonne 0).
    if player_x == GRID_W:
        player_x = 0

    # --------------------------------------------------------
    # 3F) AFFICHAGE + TEMPO
    # --------------------------------------------------------
    pygame.display.flip()
    clock.tick(FPS)

# ------------------------------------------------------------
# 4) FERMETURE PROPRE
# ------------------------------------------------------------

pygame.quit()

# ------------------------------------------------------------
# EXERCICES
# ------------------------------------------------------------
#
# 1) Boucle for
# - Change range(GRID_W) en range(5).
# - Observe le nombre de cases grises dessinees.
#
# 2) Vitesse
# - Change FPS = 6 en FPS = 3, puis FPS = 12.
# - Observe la vitesse du joueur.
#
# 3) Ligne du joueur
# - Change player_y = 3 en 1 ou 6.
# - Observe la nouvelle ligne de dessin.
