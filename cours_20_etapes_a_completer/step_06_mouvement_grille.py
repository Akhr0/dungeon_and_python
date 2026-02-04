# Step 06 - Mouvement sur une grille (version dictionnaires + listes)
# -------------------------------------------------------------------
# OBJECTIF PEDAGOGIQUE:
# - Consolider ce qu'on vient de voir:
#   1) dictionnaires
#   2) listes
#   3) fonctions
#   4) conditions
# - Avoir une base de jeu "propre" avant d'ajouter les monstres.
#
# CE QU'ON AJOUTE DANS CETTE ETAPE:
# - Une grille 10x8
# - Un joueur (dictionnaire)
# - Des murs (liste de tuples)
# - Un deplacement bloque par les murs
#
# CE QU'ON N'A PAS ENCORE:
# - Pas de monstre
# - Pas de projectile
# - Pas de niveau

# -------------------------------------------------------------------
# CADRE PEDAGOGIQUE UNIFIE (Step 06 - Mouvement grille)
# -------------------------------------------------------------------
# POUR LE PROF / ELEVE:
# - On garde: variables, conditions, listes, fonctions, dictionnaires
# - Nouvelle surcouche: assembler ces notions dans une base de jeu complete et lisible
# - A retenir en priorite: on se deplace case par case et on bloque les cases interdites
# - Le bloc EXERCICE GUIDE en fin de fichier reste la reference pratique.
# -------------------------------------------------------------------

# VERSION ELEVE A COMPLETER
# Complete uniquement les zones balisees dans ce fichier.

import pygame

# -------------------------------------------------------------------
# 1) CONSTANTES (variables globales de reglage)
# -------------------------------------------------------------------
GRID_W = 10
GRID_H = 8
TILE_SIZE = 64
SCREEN_WIDTH = GRID_W * TILE_SIZE
SCREEN_HEIGHT = GRID_H * TILE_SIZE
FPS = 60

# Couleurs (R, G, B)
COLOR_BG = (30, 30, 30)
COLOR_GRID = (55, 55, 55)
COLOR_PLAYER = (200, 50, 50)
COLOR_WALL = (90, 90, 90)


# -------------------------------------------------------------------
# 2) FONCTIONS UTILITAIRES
# -------------------------------------------------------------------
def in_bounds(pos):
    # pos est une liste [x, y]
    # La fonction renvoie True si la position reste dans la grille.
    return 0 <= pos[0] < GRID_W and 0 <= pos[1] < GRID_H


def build_blocked_set(walls):
    # Pourquoi un set ?
    # - "in" est tres rapide sur un set.
    # - On convertit donc la liste de tuples en set.
    return set(walls)


def try_move_player(player, keys, blocked):
    # Cette fonction essaie de bouger le joueur d'une case.
    # Si le mouvement est interdit, le joueur ne bouge pas.

    # On part de la position actuelle.
    target = player["pos"][:]

    # "if / elif" = une seule direction par frame.
    if keys[pygame.K_LEFT] or keys[pygame.K_q]:
        target[0] -= 1
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        target[0] += 1
    elif keys[pygame.K_UP] or keys[pygame.K_z]:
        target[1] -= 1
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        target[1] += 1
    else:
        # Aucune touche direction -> rien a faire
        return

    # Condition 1: rester dans la grille
    if not in_bounds(target):
        return

    # Condition 2: ne pas entrer dans une case bloquee
    if tuple(target) in blocked:
        return

    # Si tout est valide, on applique la nouvelle position.
    player["pos"] = target


# -------------------------------------------------------------------
# 3) DESSIN
# -------------------------------------------------------------------
def draw_grid(screen):
    # Dessine les lignes verticales
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(screen, COLOR_GRID, (x, 0), (x, SCREEN_HEIGHT), 1)

    # Dessine les lignes horizontales
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, COLOR_GRID, (0, y), (SCREEN_WIDTH, y), 1)


def draw_walls(screen, walls):
    # On parcourt la liste de tuples: [(x1, y1), (x2, y2), ...]
    for wx, wy in walls:
        pygame.draw.rect(
            screen,
            COLOR_WALL,
            (wx * TILE_SIZE + 8, wy * TILE_SIZE + 8, TILE_SIZE - 16, TILE_SIZE - 16),
        )


def draw_player(screen, player):
    px = player["pos"][0]
    py = player["pos"][1]
    pygame.draw.rect(
        screen,
        COLOR_PLAYER,
        (px * TILE_SIZE + 8, py * TILE_SIZE + 8, TILE_SIZE - 16, TILE_SIZE - 16),
    )


# -------------------------------------------------------------------
# 4) PROGRAMME PRINCIPAL
# -------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Step 06 - Mouvement grille")
clock = pygame.time.Clock()

# Le joueur est un dictionnaire (comme vu au step dictionnaires)
player = {
    "pos": [1, 1],
}

# Les murs sont une liste de tuples (comme vu au step listes)
walls = [
    (3, 3),
    (3, 4),
    (4, 4),
    (6, 2),
    (6, 3),
]

running = True
while running:
    # 1) Evenements (fermeture de fenetre)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2) Mise a jour logique
    keys = pygame.key.get_pressed()
    # ============================================================
# >>>>>>>>>>>>>> ZONE A COMPLETER PAR L'ELEVE >>>>>>>>>>>>>>>
# >>> Ecris ton code ENTRE les deux balises START / END
# >>> START CODE ELEVE
    # (Attendu: creer blocked avec build_blocked_set puis appeler try_move_player)

    # <<< END CODE ELEVE
# <<<<<<<<<<<<<< FIN ZONE A COMPLETER <<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================

    # 3) Dessin
    screen.fill(COLOR_BG)
    draw_grid(screen)
    draw_walls(screen, walls)
    draw_player(screen, player)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# ------------------------------------------------------------
# EXERCICE GUIDE - STEP 06 (MOUVEMENT SUR GRILLE)
# ------------------------------------------------------------
# Objectif de l'exercice:
# - Comprendre le lien entre la liste "walls" et le blocage du joueur.
#
# Etape 1:
# - Dans la liste walls, ajoute un nouveau mur, par exemple:
#     (2, 1)
# - Lance le jeu et verifie que le joueur est bloque sur cette case.
#
# Etape 2:
# - Supprime ce mur ajoute.
# - Verifie que le passage est de nouveau libre.
#
# Etape 3:
# - Change la position de depart du joueur:
#     "pos": [1, 1] -> "pos": [5, 5]
# - Verifie que le joueur apparait au bon endroit.
# ------------------------------------------------------------

