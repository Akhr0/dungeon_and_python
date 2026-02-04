# Step 10 - IA monstre simple
# -------------------------------------------------------------------
# OBJECTIF PEDAGOGIQUE:
# - Ajouter un comportement monstre tres lisible.
# - Regle simple:
#   1) le monstre essaie de se rapprocher du joueur
#   2) si bloque par un mur, il fait un pas aleatoire
#
# NOTE "TEMPORAIRE":
# - Pas encore d'attaque joueur
# - Pas encore de projectile

# -------------------------------------------------------------------
# CADRE PEDAGOGIQUE UNIFIE (Step 10 - IA simple)
# -------------------------------------------------------------------
# POUR LE PROF / ELEVE:
# - On garde: monstre present dans la scene
# - Nouvelle surcouche: comportement automatique: se rapprocher du joueur sinon pas aleatoire
# - A retenir en priorite: une IA simple peut etre lisible sans algorithme complexe
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
HUD_HEIGHT = 90
SCREEN_WIDTH = GRID_W * TILE_SIZE
SCREEN_HEIGHT = GRID_H * TILE_SIZE + HUD_HEIGHT
FPS = 60

WALL_COUNT = 8
MONSTER_MOVE_DELAY = 0.35

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


def apply_cooldown(value, dt):
    return max(0.0, value - dt)


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
    forbidden = {tuple(player_pos)}
    for wall in walls:
        forbidden.add(wall)
    tile = random_free_tile(forbidden)
    return [{"pos": [tile[0], tile[1]], "alive": True, "move_cooldown": 0.0}]


def generate_chest(player_pos, walls, monsters):
    forbidden = {tuple(player_pos)}
    for wall in walls:
        forbidden.add(wall)
    for monster in monsters:
        forbidden.add(tuple(monster["pos"]))
    tile = random_free_tile(forbidden)
    return {"pos": [tile[0], tile[1]], "opened": False, "heal": random.choice([2, 4, 6])}


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


def is_monster_move_blocked(target, player_pos, walls_set, occupied_set, chest):
    if not in_bounds(target):
        return True
    if tuple(target) in walls_set:
        return True
    if target == player_pos:
        return True
    if tuple(target) in occupied_set:
        return True
    if chest is not None and not chest["opened"] and target == chest["pos"]:
        return True
    return False


def get_approach_steps(monster_pos, player_pos):
    dx = player_pos[0] - monster_pos[0]
    dy = player_pos[1] - monster_pos[1]
    steps = []

    # On tente d'abord l'axe dominant
    if abs(dx) >= abs(dy):
        if dx != 0:
            steps.append((1 if dx > 0 else -1, 0))
        if dy != 0:
            steps.append((0, 1 if dy > 0 else -1))
    else:
        if dy != 0:
            steps.append((0, 1 if dy > 0 else -1))
        if dx != 0:
            steps.append((1 if dx > 0 else -1, 0))

    return steps


def choose_random_step(monster_pos, player_pos, walls_set, occupied_set, chest):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    random.shuffle(directions)

    for dx, dy in directions:
        target = [monster_pos[0] + dx, monster_pos[1] + dy]
        if not is_monster_move_blocked(target, player_pos, walls_set, occupied_set, chest):
            return dx, dy
    return 0, 0


def update_monsters(monsters, player, chest, walls, dt):
    walls_set = set(walls)
    occupied_set = {tuple(monster["pos"]) for monster in monsters if monster["alive"]}

    for monster in monsters:
        if not monster["alive"]:
            continue

        monster["move_cooldown"] = apply_cooldown(monster["move_cooldown"], dt)
        if monster["move_cooldown"] > 0:
            continue

        moved = False

        # 1) essaie de se rapprocher du joueur
        for dx, dy in get_approach_steps(monster["pos"], player["pos"]):
            target = [monster["pos"][0] + dx, monster["pos"][1] + dy]
            if is_monster_move_blocked(target, player["pos"], walls_set, occupied_set, chest):
                continue

            occupied_set.remove(tuple(monster["pos"]))
            monster["pos"] = target
            occupied_set.add(tuple(monster["pos"]))
            moved = True
            break

        # 2) si bloque, pas aleatoire
        if not moved:
            dx, dy = choose_random_step(monster["pos"], player["pos"], walls_set, occupied_set, chest)
            if dx != 0 or dy != 0:
                target = [monster["pos"][0] + dx, monster["pos"][1] + dy]
                occupied_set.remove(tuple(monster["pos"]))
                monster["pos"] = target
                occupied_set.add(tuple(monster["pos"]))

        monster["move_cooldown"] = MONSTER_MOVE_DELAY


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


def draw_chest(screen, chest):
    if chest is None or chest["opened"]:
        return
    cx, cy = chest["pos"]
    pygame.draw.rect(screen, COLOR_CHEST, (cx * TILE_SIZE + 12, cy * TILE_SIZE + 12, TILE_SIZE - 24, TILE_SIZE - 24))


def draw_monsters(screen, monsters):
    for monster in monsters:
        if not monster["alive"]:
            continue
        mx, my = monster["pos"]
        pygame.draw.rect(screen, COLOR_MONSTER, (mx * TILE_SIZE + 10, my * TILE_SIZE + 10, TILE_SIZE - 20, TILE_SIZE - 20))


def draw_player(screen, player):
    px, py = player["pos"]
    pygame.draw.rect(screen, COLOR_PLAYER, (px * TILE_SIZE + 8, py * TILE_SIZE + 8, TILE_SIZE - 16, TILE_SIZE - 16))


def draw_hud(screen, font, player, message):
    hud_y = GRID_H * TILE_SIZE
    pygame.draw.rect(screen, COLOR_HUD, (0, hud_y, SCREEN_WIDTH, HUD_HEIGHT))
    screen.blit(font.render(f"PV: {player['hp']}/{player['hp_max']}", True, COLOR_TEXT), (10, hud_y + 8))
    screen.blit(font.render("Bouger: fleches/ZQSD | E: coffre", True, COLOR_TEXT), (10, hud_y + 32))
    screen.blit(font.render(message, True, COLOR_TEXT), (10, hud_y + 58))


# -------------------------------------------------------------------
# 4) MAIN
# -------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Step 10 - IA monstre simple")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 18)

player = {"pos": [1, 1], "hp": 12, "hp_max": 20}
walls = generate_walls(player["pos"])
monsters = generate_monsters(player["pos"], walls)
chest = generate_chest(player["pos"], walls, monsters)
message = "Le monstre te suit, sinon il vagabonde."

running = True
while running:
    dt = clock.tick(FPS) / 1000.0

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
    update_monsters(monsters, player, chest, walls, dt)

    screen.fill(COLOR_BG)
    draw_grid(screen)
    draw_walls(screen, walls)
    draw_chest(screen, chest)
    draw_monsters(screen, monsters)
    draw_player(screen, player)
    draw_hud(screen, font, player, message)

    pygame.display.flip()

pygame.quit()

# ------------------------------------------------------------
# EXERCICE GUIDE - STEP 10 (IA MONSTRE SIMPLE)
# ------------------------------------------------------------
# Objectif de l'exercice:
# - Comprendre la vitesse et le comportement de l'IA.
#
# Etape 1:
# - Change MONSTER_MOVE_DELAY (ex: 0.35 -> 0.55).
# - Verifie que le monstre bouge plus lentement.
#
# Etape 2:
# - Mets MONSTER_MOVE_DELAY a 0.20.
# - Verifie que le monstre bouge plus vite.
#
# Etape 3:
# - Trouve le message initial du HUD.
# - Change le texte pour expliquer la regle "se rapprocher sinon aleatoire".
# ------------------------------------------------------------

