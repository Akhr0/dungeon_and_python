# Step 08 - Coffre + potion
# -------------------------------------------------------------------
# OBJECTIF PEDAGOGIQUE:
# - Ajouter une interaction simple (touche E).
# - Introduire une logique "si adjacent alors action".
# - Ajouter la notion de points de vie (hp).
#
# NOUVEAUTE:
# - Un coffre apparait dans la salle.
# - On ouvre le coffre avec E quand on est juste a cote.
# - Le coffre soigne le joueur.

# -------------------------------------------------------------------
# CADRE PEDAGOGIQUE UNIFIE (Step 08 - Coffre + potion)
# -------------------------------------------------------------------
# POUR LE PROF / ELEVE:
# - On garde: mouvement + murs aleatoires
# - Nouvelle surcouche: interaction joueur avec la touche E et systeme de soin
# - A retenir en priorite: une action se declenche seulement si la condition (adjacent) est vraie
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
SCREEN_HEIGHT = GRID_H * TILE_SIZE + 70  # bandeau HUD simple
FPS = 60

WALL_COUNT = 8

COLOR_BG = (30, 30, 30)
COLOR_GRID = (55, 55, 55)
COLOR_PLAYER = (200, 50, 50)
COLOR_WALL = (90, 90, 90)
COLOR_CHEST = (150, 100, 40)
COLOR_TEXT = (235, 235, 235)
COLOR_HUD = (15, 15, 15)


# -------------------------------------------------------------------
# 2) OUTILS
# -------------------------------------------------------------------
def in_bounds(pos):
    return 0 <= pos[0] < GRID_W and 0 <= pos[1] < GRID_H


def is_adjacent(a, b):
    # Distance Manhattan = 1 -> cases cote a cote
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1


def random_free_tile(forbidden):
    candidates = []
    for x in range(1, GRID_W - 1):
        for y in range(1, GRID_H - 1):
            if (x, y) not in forbidden:
                candidates.append((x, y))
    if len(candidates) == 0:
        return (1, 1)
    return random.choice(candidates)


def generate_random_walls(player_pos, wall_count):
    walls = []
    forbidden = {tuple(player_pos)}
    for _ in range(wall_count):
        wall = random_free_tile(forbidden)
        walls.append(wall)
        forbidden.add(wall)
    return walls


def generate_chest(player_pos, walls):
    forbidden = {tuple(player_pos)}
    for wall in walls:
        forbidden.add(wall)
    chest_pos = random_free_tile(forbidden)

    # Dictionnaire "chest"
    chest = {
        "pos": [chest_pos[0], chest_pos[1]],
        "opened": False,
        "heal": random.choice([2, 4, 6]),
    }
    return chest


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


def try_open_chest(player, chest):
    if chest is None:
        return None
    if chest["opened"]:
        return None
    if not is_adjacent(player["pos"], chest["pos"]):
        return None

    chest["opened"] = True
    player["hp"] = min(player["hp_max"], player["hp"] + chest["heal"])
    return f"Coffre ouvert: +{chest['heal']} PV"


# -------------------------------------------------------------------
# 3) DESSIN
# -------------------------------------------------------------------
def draw_grid(screen):
    for x in range(0, GRID_W * TILE_SIZE, TILE_SIZE):
        pygame.draw.line(screen, COLOR_GRID, (x, 0), (x, GRID_H * TILE_SIZE), 1)
    for y in range(0, GRID_H * TILE_SIZE, TILE_SIZE):
        pygame.draw.line(screen, COLOR_GRID, (0, y), (GRID_W * TILE_SIZE, y), 1)


def draw_walls(screen, walls):
    for wx, wy in walls:
        pygame.draw.rect(
            screen,
            COLOR_WALL,
            (wx * TILE_SIZE + 8, wy * TILE_SIZE + 8, TILE_SIZE - 16, TILE_SIZE - 16),
        )


def draw_chest(screen, chest):
    if chest is None or chest["opened"]:
        return
    cx, cy = chest["pos"]
    pygame.draw.rect(
        screen,
        COLOR_CHEST,
        (cx * TILE_SIZE + 12, cy * TILE_SIZE + 12, TILE_SIZE - 24, TILE_SIZE - 24),
    )


def draw_player(screen, player):
    px, py = player["pos"]
    pygame.draw.rect(
        screen,
        COLOR_PLAYER,
        (px * TILE_SIZE + 8, py * TILE_SIZE + 8, TILE_SIZE - 16, TILE_SIZE - 16),
    )


def draw_hud(screen, font, player, message):
    hud_y = GRID_H * TILE_SIZE
    pygame.draw.rect(screen, COLOR_HUD, (0, hud_y, SCREEN_WIDTH, 70))
    line_1 = f"PV: {player['hp']}/{player['hp_max']}"
    line_2 = "Fleches/ZQSD: bouger | E: ouvrir coffre"
    screen.blit(font.render(line_1, True, COLOR_TEXT), (10, hud_y + 8))
    screen.blit(font.render(line_2, True, COLOR_TEXT), (10, hud_y + 30))
    screen.blit(font.render(message, True, COLOR_TEXT), (10, hud_y + 50))


# -------------------------------------------------------------------
# 4) MAIN
# -------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Step 08 - Coffre + potion")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 18)

player = {
    "pos": [1, 1],
    "hp": 12,
    "hp_max": 20,
}

walls = generate_random_walls(player["pos"], WALL_COUNT)
chest = generate_chest(player["pos"], walls)
message = "Va vers le coffre et appuie sur E"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            result = try_open_chest(player, chest)
            if result is not None:
                message = result

    blocked = set(walls)
    if chest is not None and not chest["opened"]:
        blocked.add(tuple(chest["pos"]))

    keys = pygame.key.get_pressed()
    try_move_player(player, keys, blocked)

    screen.fill(COLOR_BG)
    draw_grid(screen)
    draw_walls(screen, walls)
    draw_chest(screen, chest)
    draw_player(screen, player)
    draw_hud(screen, font, player, message)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# ------------------------------------------------------------
# EXERCICE GUIDE - STEP 08 (COFFRE + POTION)
# ------------------------------------------------------------
# Objectif de l'exercice:
# - Comprendre l'interaction avec la touche E.
#
# Etape 1:
# - Lance le jeu.
# - Va a cote du coffre.
# - Appuie sur E et observe le message + les PV.
#
# Etape 2:
# - Trouve la variable de vie max du joueur (max_hp).
# - Passe-la de 10 a 14.
# - Relance et verifie le nouveau plafond de soin.
#
# Etape 3:
# - Essaie d'appuyer sur E loin du coffre.
# - Verifie que le coffre ne s'ouvre pas.
# ------------------------------------------------------------

