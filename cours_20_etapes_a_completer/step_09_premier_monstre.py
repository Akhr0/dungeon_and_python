# Step 09 - Premier monstre (statique)
# -------------------------------------------------------------------
# OBJECTIF PEDAGOGIQUE:
# - Ajouter un monstre comme nouvelle entite.
# - Manipuler une LISTE de dictionnaires (monsters).
#
# NOUVEAUTE:
# - Un monstre apparait et bloque une case.
# - Pas d'IA pour l'instant (il ne bouge pas encore).

# -------------------------------------------------------------------
# CADRE PEDAGOGIQUE UNIFIE (Step 09 - Premier monstre)
# -------------------------------------------------------------------
# POUR LE PROF / ELEVE:
# - On garde: coffre, mouvement, blocage
# - Nouvelle surcouche: ajout d une entite monstre dans une liste de dictionnaires
# - A retenir en priorite: on commence a gerer plusieurs objets de meme type
# - Le bloc EXERCICE GUIDE en fin de fichier reste la reference pratique.
# -------------------------------------------------------------------

# VERSION ELEVE A COMPLETER
# Complete uniquement les zones balisees dans ce fichier.

import random
import pygame

# -------------------------------------------------------------------
# 1) CONSTANTES
# -------------------------------------------------------------------
GRID_W = 10
GRID_H = 8
TILE_SIZE = 64
HUD_HEIGHT = 90
SCREEN_WIDTH = GRID_W * TILE_SIZE
SCREEN_HEIGHT = GRID_H * TILE_SIZE + HUD_HEIGHT
FPS = 60

WALL_COUNT = 8

COLOR_BG = (30, 30, 30)
COLOR_GRID = (55, 55, 55)
COLOR_WALL = (90, 90, 90)
COLOR_PLAYER = (200, 50, 50)
COLOR_MONSTER = (90, 200, 120)
COLOR_CHEST = (150, 100, 40)
COLOR_HUD = (15, 15, 15)
COLOR_TEXT = (235, 235, 235)


# -------------------------------------------------------------------
# 2) OUTILS
# -------------------------------------------------------------------
def in_bounds(pos):
    return 0 <= pos[0] < GRID_W and 0 <= pos[1] < GRID_H


def is_adjacent(a, b):
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


def generate_walls(player_pos):
    walls = []
    forbidden = {tuple(player_pos)}
    for _ in range(WALL_COUNT):
        wall = random_free_tile(forbidden)
        walls.append(wall)
        forbidden.add(wall)
    return walls


def generate_monsters(player_pos, walls):
    # On renvoie une LISTE de dictionnaires.
    forbidden = {tuple(player_pos)}
    for wall in walls:
        forbidden.add(wall)

    monster_tile = random_free_tile(forbidden)
    monsters = [
        {
            "pos": [monster_tile[0], monster_tile[1]],
            "hp": 3,
            "alive": True,
        }
    ]
    return monsters


def generate_chest(player_pos, walls, monsters):
    forbidden = {tuple(player_pos)}
    for wall in walls:
        forbidden.add(wall)
    for monster in monsters:
        forbidden.add(tuple(monster["pos"]))

    chest_tile = random_free_tile(forbidden)
    chest = {
        "pos": [chest_tile[0], chest_tile[1]],
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
    if chest is None or chest["opened"]:
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
        pygame.draw.rect(screen, COLOR_WALL, (wx * TILE_SIZE + 8, wy * TILE_SIZE + 8, TILE_SIZE - 16, TILE_SIZE - 16))


def draw_monsters(screen, monsters):
    for monster in monsters:
        if not monster["alive"]:
            continue
        mx, my = monster["pos"]
        pygame.draw.rect(screen, COLOR_MONSTER, (mx * TILE_SIZE + 10, my * TILE_SIZE + 10, TILE_SIZE - 20, TILE_SIZE - 20))


def draw_chest(screen, chest):
    if chest is None or chest["opened"]:
        return
    cx, cy = chest["pos"]
    pygame.draw.rect(screen, COLOR_CHEST, (cx * TILE_SIZE + 12, cy * TILE_SIZE + 12, TILE_SIZE - 24, TILE_SIZE - 24))


def draw_player(screen, player):
    px, py = player["pos"]
    pygame.draw.rect(screen, COLOR_PLAYER, (px * TILE_SIZE + 8, py * TILE_SIZE + 8, TILE_SIZE - 16, TILE_SIZE - 16))


def draw_hud(screen, font, player, monsters, message):
    hud_y = GRID_H * TILE_SIZE
    pygame.draw.rect(screen, COLOR_HUD, (0, hud_y, SCREEN_WIDTH, HUD_HEIGHT))
    line_1 = f"PV: {player['hp']}/{player['hp_max']} | Monstres: {len(monsters)}"
    line_2 = "Bouger: fleches/ZQSD | E: coffre"
    screen.blit(font.render(line_1, True, COLOR_TEXT), (10, hud_y + 8))
    screen.blit(font.render(line_2, True, COLOR_TEXT), (10, hud_y + 32))
    screen.blit(font.render(message, True, COLOR_TEXT), (10, hud_y + 58))


# -------------------------------------------------------------------
# 4) MAIN
# -------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Step 09 - Premier monstre")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 18)

player = {"pos": [1, 1], "hp": 12, "hp_max": 20}
walls = generate_walls(player["pos"])
# ============================================================
# >>>>>>>>>>>>>> ZONE A COMPLETER PAR L'ELEVE >>>>>>>>>>>>>>>
# >>> Ecris ton code ENTRE les deux balises START / END
# >>> START CODE ELEVE
# (Attendu: creer la liste monsters avec generate_monsters)
monsters = []
# <<< END CODE ELEVE
# <<<<<<<<<<<<<< FIN ZONE A COMPLETER <<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
chest = generate_chest(player["pos"], walls, monsters)
message = "Le monstre est statique (temporaire)."

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
    for monster in monsters:
        if monster["alive"]:
            blocked.add(tuple(monster["pos"]))
    if chest is not None and not chest["opened"]:
        blocked.add(tuple(chest["pos"]))

    keys = pygame.key.get_pressed()
    try_move_player(player, keys, blocked)

    screen.fill(COLOR_BG)
    draw_grid(screen)
    draw_walls(screen, walls)
    draw_chest(screen, chest)
    draw_monsters(screen, monsters)
    draw_player(screen, player)
    draw_hud(screen, font, player, monsters, message)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# ------------------------------------------------------------
# EXERCICE GUIDE - STEP 09 (PREMIER MONSTRE)
# ------------------------------------------------------------
# Objectif de l'exercice:
# - Manipuler une liste de monstres.
#
# Etape 1:
# - Trouve la creation de la liste "monsters".
# - Ajoute un 2e monstre avec une autre position.
#
# Etape 2:
# - Lance le jeu et verifie que les 2 cases sont bloquees.
#
# Etape 3:
# - Change la couleur du monstre dans les constantes couleur.
# - Observe le rendu visuel.
# ------------------------------------------------------------

