# Step 12 - Projectiles (boules de feu)
# -------------------------------------------------------------------
# OBJECTIF PEDAGOGIQUE:
# - Ajouter l'attaque du joueur.
# - Introduire une liste d'objets "projectiles".
# - Gérer leur déplacement et collision.
#
# NOUVEAUTE:
# - SPACE lance une boule de feu.
# - Les projectiles blessent les monstres.
# - Un monstre peut mourir (alive=False).

# -------------------------------------------------------------------
# CADRE PEDAGOGIQUE UNIFIE (Step 12 - Projectiles)
# -------------------------------------------------------------------
# POUR LE PROF / ELEVE:
# - On garde: combat de base monstre vs joueur
# - Nouvelle surcouche: attaque du joueur avec une liste de projectiles et collisions
# - A retenir en priorite: on met a jour chaque projectile a chaque frame
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
HUD_HEIGHT = 100
SCREEN_WIDTH = GRID_W * TILE_SIZE
SCREEN_HEIGHT = GRID_H * TILE_SIZE + HUD_HEIGHT
FPS = 60

WALL_COUNT = 8
MONSTER_MOVE_DELAY = 0.35
MONSTER_ATTACK_DELAY = 0.9
PLAYER_ATTACK_DELAY = 0.22
FIREBALL_SPEED = 12.0
FIREBALL_RANGE = 6.0

COLOR_BG = (30, 30, 30)
COLOR_GRID = (55, 55, 55)
COLOR_WALL = (90, 90, 90)
COLOR_PLAYER = (200, 50, 50)
COLOR_MONSTER = (90, 200, 120)
COLOR_CHEST = (150, 100, 40)
COLOR_HUD = (15, 15, 15)
COLOR_TEXT = (235, 235, 235)
FIRE_1 = (255, 220, 80)
FIRE_2 = (245, 150, 60)
FIRE_3 = (220, 60, 40)


# -------------------------------------------------------------------
# 2) OUTILS
# -------------------------------------------------------------------
def apply_cooldown(value, dt):
    return max(0.0, value - dt)


def in_bounds(pos):
    return 0 <= pos[0] < GRID_W and 0 <= pos[1] < GRID_H


def is_adjacent(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1


def direction_to_vector(direction):
    if direction == "left":
        return -1, 0
    if direction == "right":
        return 1, 0
    if direction == "up":
        return 0, -1
    return 0, 1


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
    return [
        {
            "pos": [tile[0], tile[1]],
            "alive": True,
            "hp": 5,
            "atk": 1,
            "move_cooldown": 0.0,
            "attack_cooldown": 0.0,
        }
    ]


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
        player["direction"] = "left"
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        target[0] += 1
        player["direction"] = "right"
    elif keys[pygame.K_UP] or keys[pygame.K_z]:
        target[1] -= 1
        player["direction"] = "up"
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        target[1] += 1
        player["direction"] = "down"
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


def try_player_attack(player, projectiles):
    if player["attack_cooldown"] > 0:
        return

    player["attack_cooldown"] = PLAYER_ATTACK_DELAY
    dx, dy = direction_to_vector(player["direction"])
    projectiles.append(
        {
            "pos": [float(player["pos"][0]), float(player["pos"][1])],
            "dir": [dx, dy],
            "speed": FIREBALL_SPEED,
            "range_left": FIREBALL_RANGE,
            "damage": player["atk"],
        }
    )


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
        monster["attack_cooldown"] = apply_cooldown(monster["attack_cooldown"], dt)

        if is_adjacent(monster["pos"], player["pos"]):
            if monster["attack_cooldown"] <= 0:
                player["hp"] -= monster["atk"]
                monster["attack_cooldown"] = MONSTER_ATTACK_DELAY
            continue

        if monster["move_cooldown"] > 0:
            continue

        moved = False
        for dx, dy in get_approach_steps(monster["pos"], player["pos"]):
            target = [monster["pos"][0] + dx, monster["pos"][1] + dy]
            if is_monster_move_blocked(target, player["pos"], walls_set, occupied_set, chest):
                continue
            occupied_set.remove(tuple(monster["pos"]))
            monster["pos"] = target
            occupied_set.add(tuple(monster["pos"]))
            moved = True
            break

        if not moved:
            dx, dy = choose_random_step(monster["pos"], player["pos"], walls_set, occupied_set, chest)
            if dx != 0 or dy != 0:
                target = [monster["pos"][0] + dx, monster["pos"][1] + dy]
                occupied_set.remove(tuple(monster["pos"]))
                monster["pos"] = target
                occupied_set.add(tuple(monster["pos"]))

        monster["move_cooldown"] = MONSTER_MOVE_DELAY


def update_projectiles(projectiles, monsters, walls, dt):
    walls_set = set(walls)

    for projectile in list(projectiles):
        distance = projectile["speed"] * dt
        if distance <= 0:
            continue
        if distance > projectile["range_left"]:
            distance = projectile["range_left"]

        projectile["pos"][0] += projectile["dir"][0] * distance
        projectile["pos"][1] += projectile["dir"][1] * distance
        projectile["range_left"] -= distance

        tile_x = int(projectile["pos"][0])
        tile_y = int(projectile["pos"][1])
        tile = [tile_x, tile_y]

        if not in_bounds(tile):
            projectiles.remove(projectile)
            continue
        if (tile_x, tile_y) in walls_set:
            projectiles.remove(projectile)
            continue

        hit_monster = None
        for monster in monsters:
            if not monster["alive"]:
                continue
            if monster["pos"][0] == tile_x and monster["pos"][1] == tile_y:
                hit_monster = monster
                break

        if hit_monster is not None:
            hit_monster["hp"] -= projectile["damage"]
            if hit_monster["hp"] <= 0:
                hit_monster["alive"] = False
            projectiles.remove(projectile)
            continue

        if projectile["range_left"] <= 0:
            projectiles.remove(projectile)


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


def draw_projectiles(screen, projectiles):
    for projectile in projectiles:
        px = projectile["pos"][0] * TILE_SIZE + TILE_SIZE // 2
        py = projectile["pos"][1] * TILE_SIZE + TILE_SIZE // 2
        center = (int(px), int(py))
        pygame.draw.circle(screen, FIRE_1, center, 9)
        pygame.draw.circle(screen, FIRE_2, center, 6)
        pygame.draw.circle(screen, FIRE_3, center, 3)


def draw_hud(screen, font, player, monsters, message):
    alive_count = sum(1 for monster in monsters if monster["alive"])
    hud_y = GRID_H * TILE_SIZE
    pygame.draw.rect(screen, COLOR_HUD, (0, hud_y, SCREEN_WIDTH, HUD_HEIGHT))
    line_1 = f"PV: {player['hp']}/{player['hp_max']} | Monstres vivants: {alive_count}"
    line_2 = "Bouger: fleches/ZQSD | SPACE: boule de feu | E: coffre"
    screen.blit(font.render(line_1, True, COLOR_TEXT), (10, hud_y + 8))
    screen.blit(font.render(line_2, True, COLOR_TEXT), (10, hud_y + 34))
    screen.blit(font.render(message, True, COLOR_TEXT), (10, hud_y + 62))


# -------------------------------------------------------------------
# 4) MAIN
# -------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Step 12 - Projectiles")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 18)

player = {"pos": [1, 1], "direction": "down", "hp": 12, "hp_max": 20, "atk": 2, "attack_cooldown": 0.0}
walls = generate_walls(player["pos"])
monsters = generate_monsters(player["pos"], walls)
chest = generate_chest(player["pos"], walls, monsters)
projectiles = []
message = "SPACE lance une boule de feu."

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
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            try_player_attack(player, projectiles)

    player["attack_cooldown"] = apply_cooldown(player["attack_cooldown"], dt)

    blocked = set(walls)
    for monster in monsters:
        if monster["alive"]:
            blocked.add(tuple(monster["pos"]))
    if chest is not None and not chest["opened"]:
        blocked.add(tuple(chest["pos"]))

    keys = pygame.key.get_pressed()
    try_move_player(player, keys, blocked)
    update_monsters(monsters, player, chest, walls, dt)
    update_projectiles(projectiles, monsters, walls, dt)

    screen.fill(COLOR_BG)
    draw_grid(screen)
    draw_walls(screen, walls)
    draw_chest(screen, chest)
    draw_projectiles(screen, projectiles)
    draw_monsters(screen, monsters)
    draw_player(screen, player)
    draw_hud(screen, font, player, monsters, message)

    pygame.display.flip()

pygame.quit()

# ------------------------------------------------------------
# EXERCICE GUIDE - STEP 12 (PROJECTILES)
# ------------------------------------------------------------
# Objectif de l'exercice:
# - Comprendre la vitesse et la portee des boules de feu.
#
# Etape 1:
# - Change FIREBALL_SPEED (ex: 12.0 -> 8.0).
# - Observe une boule de feu plus lente.
#
# Etape 2:
# - Change FIREBALL_RANGE (ex: 6.0 -> 9.0).
# - Observe une boule de feu qui va plus loin.
#
# Etape 3:
# - Lance plusieurs tirs avec SPACE et verifie que la liste
#   projectiles se vide quand les tirs sortent ou touchent.
# ------------------------------------------------------------

