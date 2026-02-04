# Step 14 - Sprites (assets)
# -------------------------------------------------------------------
# OBJECTIF PEDAGOGIQUE:
# - Remplacer les rectangles par des images.
# - Montrer un fallback propre si les assets manquent.
#
# NOUVEAUTE:
# - Chargement de assets/mage.png, assets/slime.png, assets/gobelin.png
# - Version rouge des sprites pour le clignotement hit
#
# NOTE TEMPORAIRE:
# - Le gameplay est identique a l'etape precedente.
# - On focus surtout sur la partie affichage.

# -------------------------------------------------------------------
# CADRE PEDAGOGIQUE UNIFIE (Step 14 - Sprites assets)
# -------------------------------------------------------------------
# POUR LE PROF / ELEVE:
# - On garde: gameplay de l etape precedente
# - Nouvelle surcouche: chargement d images externes avec fallback rectangle
# - A retenir en priorite: on separe logique de jeu et rendu visuel
# - Le bloc EXERCICE GUIDE en fin de fichier reste la reference pratique.
# -------------------------------------------------------------------

import os
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
HIT_FLASH_TIME = 0.35

COLOR_BG = (30, 30, 30)
COLOR_GRID = (55, 55, 55)
COLOR_WALL = (90, 90, 90)
COLOR_PLAYER = (70, 140, 220)
COLOR_MONSTER = (90, 200, 120)
COLOR_MONSTER_2 = (200, 180, 80)
COLOR_CHEST = (150, 100, 40)
COLOR_HUD = (15, 15, 15)
COLOR_TEXT = (235, 235, 235)
COLOR_FLASH = (220, 60, 60)
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


def direction_to_angle(direction):
    if direction == "left":
        return -90
    if direction == "right":
        return 90
    if direction == "up":
        return 180
    return 0


def is_flashing(timer):
    return timer > 0 and int(timer * 16) % 2 == 0


def random_free_tile(forbidden):
    candidates = []
    for x in range(1, GRID_W - 1):
        for y in range(1, GRID_H - 1):
            if (x, y) not in forbidden:
                candidates.append((x, y))
    if len(candidates) == 0:
        return (1, 1)
    return random.choice(candidates)


def load_sprite(path, size):
    # charge une image, retourne None si erreur
    try:
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(image, (size, size))
    except (pygame.error, FileNotFoundError):
        return None


def make_hit_sprite(sprite):
    if sprite is None:
        return None
    hit = sprite.copy()
    hit.fill((255, 0, 0, 255), special_flags=pygame.BLEND_RGBA_MULT)
    return hit


# -------------------------------------------------------------------
# 3) GENERATION MONDE/ENTITES
# -------------------------------------------------------------------
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

    monsters = []
    for idx in range(2):
        tile = random_free_tile(forbidden)
        forbidden.add(tile)
        monsters.append(
            {
                "type": "slime" if idx == 0 else "gobelin",
                "pos": [tile[0], tile[1]],
                "direction": random.choice(["left", "right", "up", "down"]),
                "alive": True,
                "hp": 4,
                "atk": 1,
                "move_cooldown": 0.0,
                "attack_cooldown": 0.0,
                "hit_flash": 0.0,
            }
        )
    return monsters


def generate_chest(player_pos, walls, monsters):
    forbidden = {tuple(player_pos)}
    for wall in walls:
        forbidden.add(wall)
    for monster in monsters:
        forbidden.add(tuple(monster["pos"]))
    tile = random_free_tile(forbidden)
    return {"pos": [tile[0], tile[1]], "opened": False, "heal": random.choice([2, 4, 6])}


# -------------------------------------------------------------------
# 4) LOGIQUE JEU
# -------------------------------------------------------------------
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
        monster["hit_flash"] = apply_cooldown(monster["hit_flash"], dt)

        if is_adjacent(monster["pos"], player["pos"]):
            if monster["attack_cooldown"] <= 0:
                player["hp"] -= monster["atk"]
                player["hit_flash"] = HIT_FLASH_TIME
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
            if dx == -1:
                monster["direction"] = "left"
            elif dx == 1:
                monster["direction"] = "right"
            elif dy == -1:
                monster["direction"] = "up"
            elif dy == 1:
                monster["direction"] = "down"
            occupied_set.add(tuple(monster["pos"]))
            moved = True
            break

        if not moved:
            dx, dy = choose_random_step(monster["pos"], player["pos"], walls_set, occupied_set, chest)
            if dx != 0 or dy != 0:
                target = [monster["pos"][0] + dx, monster["pos"][1] + dy]
                occupied_set.remove(tuple(monster["pos"]))
                monster["pos"] = target
                if dx == -1:
                    monster["direction"] = "left"
                elif dx == 1:
                    monster["direction"] = "right"
                elif dy == -1:
                    monster["direction"] = "up"
                elif dy == 1:
                    monster["direction"] = "down"
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
            hit_monster["hit_flash"] = HIT_FLASH_TIME
            if hit_monster["hp"] <= 0:
                hit_monster["alive"] = False
            projectiles.remove(projectile)
            continue

        if projectile["range_left"] <= 0:
            projectiles.remove(projectile)


# -------------------------------------------------------------------
# 5) DESSIN
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


def draw_player(screen, player, sprites, hit_sprites):
    px = player["pos"][0] * TILE_SIZE
    py = player["pos"][1] * TILE_SIZE
    angle = direction_to_angle(player["direction"])
    flash = is_flashing(player["hit_flash"])

    if sprites["player"] is not None:
        base = hit_sprites["player"] if flash else sprites["player"]
        rotated = pygame.transform.rotate(base, angle)
        rect = rotated.get_rect(center=(px + TILE_SIZE // 2, py + TILE_SIZE // 2))
        screen.blit(rotated, rect)
    else:
        color = COLOR_FLASH if flash else COLOR_PLAYER
        shape = pygame.Surface((TILE_SIZE - 16, TILE_SIZE - 16), pygame.SRCALPHA)
        shape.fill(color)
        rotated = pygame.transform.rotate(shape, angle)
        rect = rotated.get_rect(center=(px + TILE_SIZE // 2, py + TILE_SIZE // 2))
        screen.blit(rotated, rect)


def draw_monsters(screen, monsters, sprites, hit_sprites):
    for monster in monsters:
        if not monster["alive"]:
            continue

        px = monster["pos"][0] * TILE_SIZE
        py = monster["pos"][1] * TILE_SIZE
        angle = direction_to_angle(monster["direction"])
        flash = is_flashing(monster["hit_flash"])

        if monster["type"] == "slime":
            sprite = hit_sprites["slime"] if flash else sprites["slime"]
            fallback_color = COLOR_MONSTER
        else:
            sprite = hit_sprites["gobelin"] if flash else sprites["gobelin"]
            fallback_color = COLOR_MONSTER_2

        if sprite is not None:
            rotated = pygame.transform.rotate(sprite, angle)
            rect = rotated.get_rect(center=(px + TILE_SIZE // 2, py + TILE_SIZE // 2))
            screen.blit(rotated, rect)
        else:
            color = COLOR_FLASH if flash else fallback_color
            shape = pygame.Surface((TILE_SIZE - 20, TILE_SIZE - 20), pygame.SRCALPHA)
            shape.fill(color)
            rotated = pygame.transform.rotate(shape, angle)
            rect = rotated.get_rect(center=(px + TILE_SIZE // 2, py + TILE_SIZE // 2))
            screen.blit(rotated, rect)


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
    line_2 = "SPACE: boule de feu | E: coffre"
    screen.blit(font.render(line_1, True, COLOR_TEXT), (10, hud_y + 8))
    screen.blit(font.render(line_2, True, COLOR_TEXT), (10, hud_y + 34))
    screen.blit(font.render(message, True, COLOR_TEXT), (10, hud_y + 62))


# -------------------------------------------------------------------
# 6) MAIN
# -------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Step 14 - Sprites assets")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 18)

# Chargement des images depuis le dossier assets
# On cherche d'abord assets/ a cote de ce fichier.
# Si absent, on essaie un niveau au-dessus (racine du projet).
current_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(current_dir, "assets")
if os.path.isdir(assets_dir) is False:
    assets_dir = os.path.join(os.path.dirname(current_dir), "assets")

sprites = {
    "player": load_sprite(os.path.join(assets_dir, "mage.png"), TILE_SIZE - 16),
    "slime": load_sprite(os.path.join(assets_dir, "slime.png"), TILE_SIZE - 20),
    "gobelin": load_sprite(os.path.join(assets_dir, "gobelin.png"), TILE_SIZE - 20),
}
hit_sprites = {
    "player": make_hit_sprite(sprites["player"]),
    "slime": make_hit_sprite(sprites["slime"]),
    "gobelin": make_hit_sprite(sprites["gobelin"]),
}

player = {
    "pos": [1, 1],
    "direction": "down",
    "hp": 14,
    "hp_max": 20,
    "atk": 2,
    "attack_cooldown": 0.0,
    "hit_flash": 0.0,
}

walls = generate_walls(player["pos"])
monsters = generate_monsters(player["pos"], walls)
chest = generate_chest(player["pos"], walls, monsters)
projectiles = []
message = "Sprites actifs (fallback rectangles si besoin)."

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
    player["hit_flash"] = apply_cooldown(player["hit_flash"], dt)

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
    draw_monsters(screen, monsters, sprites, hit_sprites)
    draw_player(screen, player, sprites, hit_sprites)
    draw_hud(screen, font, player, monsters, message)

    pygame.display.flip()

pygame.quit()

# ------------------------------------------------------------
# EXERCICE GUIDE - STEP 14 (SPRITES / ASSETS)
# ------------------------------------------------------------
# Objectif de l'exercice:
# - Comprendre comment un asset remplace un rectangle.
#
# Etape 1:
# - Verifie que les fichiers image existent dans assets/.
# - Lance le jeu et observe les sprites.
#
# Etape 2 (test de secours/fallback):
# - Renomme temporairement un sprite (ex: mage.png -> mage_tmp.png).
# - Relance: le jeu doit rester jouable avec le fallback.
#
# Etape 3:
# - Remets le nom d'origine du fichier sprite.
# ------------------------------------------------------------
