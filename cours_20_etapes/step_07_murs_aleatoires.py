# Step 07 - Murs aleatoires
# -------------------------------------------------------------------
# OBJECTIF PEDAGOGIQUE:
# - Introduire "random" de maniere progressive.
# - Montrer comment creer une liste de tuples automatiquement.
# - Garder le meme gameplay que l'etape precedente.
#
# NOUVEAUTE:
# - Les murs ne sont plus ecrits "a la main".
# - On les genere au lancement du programme.

# -------------------------------------------------------------------
# CADRE PEDAGOGIQUE UNIFIE (Step 07 - Murs aleatoires)
# -------------------------------------------------------------------
# POUR LE PROF / ELEVE:
# - On garde: base de mouvement du step 06
# - Nouvelle surcouche: generation aleatoire avec random pour creer les murs automatiquement
# - A retenir en priorite: meme logique de jeu, monde different a chaque lancement
# - Le bloc EXERCICE GUIDE en fin de fichier reste la reference pratique.
# -------------------------------------------------------------------

import random
import pygame

# -------------------------------------------------------------------
# 1) CONSTANTES
# -------------------------------------------------------------------
GRID_W = 10
GRID_H = 8
TILE_SIZE = 64
SCREEN_WIDTH = GRID_W * TILE_SIZE
SCREEN_HEIGHT = GRID_H * TILE_SIZE
FPS = 60

WALL_COUNT = 8

COLOR_BG = (30, 30, 30)
COLOR_GRID = (55, 55, 55)
COLOR_PLAYER = (200, 50, 50)
COLOR_WALL = (90, 90, 90)


# -------------------------------------------------------------------
# 2) OUTILS
# -------------------------------------------------------------------
def in_bounds(pos):
    return 0 <= pos[0] < GRID_W and 0 <= pos[1] < GRID_H


def random_free_tile(forbidden):
    # forbidden est un set de tuples a eviter
    candidates = []

    # On evite les bords (1..GRID_W-2) pour garder des marges visuelles
    for x in range(1, GRID_W - 1):
        for y in range(1, GRID_H - 1):
            if (x, y) not in forbidden:
                candidates.append((x, y))

    if len(candidates) == 0:
        return (1, 1)

    return random.choice(candidates)


def generate_random_walls(player_pos, wall_count):
    # On construit une liste de tuples, comme demande.
    walls = []

    # On interdit au moins la case joueur.
    forbidden = {tuple(player_pos)}

    for _ in range(wall_count):
        wall = random_free_tile(forbidden)
        walls.append(wall)
        forbidden.add(wall)

    return walls


def try_move_player(player, keys, blocked):
    target = player["pos"][:]

    if keys[pygame.K_LEFT] or keys[pygame.K_q]:
        target[0] -= 1
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        target[0] += 1
    elif keys[pygame.K_UP] or keys[pygame.K_z]:
        target[1] -= 1
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        target[1] += 1
    else:
        return

    if not in_bounds(target):
        return

    if tuple(target) in blocked:
        return

    player["pos"] = target


# -------------------------------------------------------------------
# 3) DESSIN
# -------------------------------------------------------------------
def draw_grid(screen):
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(screen, COLOR_GRID, (x, 0), (x, SCREEN_HEIGHT), 1)
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        pygame.draw.line(screen, COLOR_GRID, (0, y), (SCREEN_WIDTH, y), 1)


def draw_walls(screen, walls):
    for wx, wy in walls:
        pygame.draw.rect(
            screen,
            COLOR_WALL,
            (wx * TILE_SIZE + 8, wy * TILE_SIZE + 8, TILE_SIZE - 16, TILE_SIZE - 16),
        )


def draw_player(screen, player):
    px, py = player["pos"]
    pygame.draw.rect(
        screen,
        COLOR_PLAYER,
        (px * TILE_SIZE + 8, py * TILE_SIZE + 8, TILE_SIZE - 16, TILE_SIZE - 16),
    )


# -------------------------------------------------------------------
# 4) MAIN
# -------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Step 07 - Murs aleatoires")
clock = pygame.time.Clock()

player = {"pos": [1, 1]}

# Murs aleatoires generes une seule fois au debut.
walls = generate_random_walls(player["pos"], WALL_COUNT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    blocked = set(walls)
    keys = pygame.key.get_pressed()
    try_move_player(player, keys, blocked)

    screen.fill(COLOR_BG)
    draw_grid(screen)
    draw_walls(screen, walls)
    draw_player(screen, player)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# ------------------------------------------------------------
# EXERCICE GUIDE - STEP 07 (MURS ALEATOIRES)
# ------------------------------------------------------------
# Objectif de l'exercice:
# - Voir l'effet du hasard sur la generation des murs.
#
# Etape 1:
# - Change WALL_COUNT de 8 a 4.
# - Lance le jeu: il y a moins de murs.
#
# Etape 2:
# - Change WALL_COUNT de 4 a 12.
# - Lance le jeu: il y a plus de murs.
#
# Etape 3 (bonus tres utile):
# - Ajoute juste avant la creation des murs:
#     random.seed(1)
# - Resultat: les murs seront identiques a chaque lancement.
# ------------------------------------------------------------

