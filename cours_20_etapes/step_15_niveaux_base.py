# Step 15 - Niveaux (base)
# -------------------------------------------------------------------
# OBJECTIF PEDAGOGIQUE:
# - Introduire une boucle de progression par niveau.
# - Regle: quand TOUS les monstres sont morts -> niveau +1.
#
# NOUVEAUTE:
# - Nouveau niveau = nouveaux murs, nouveau coffre, nouveaux monstres.
# - Le niveau monte de 1 en 1.
#
# NOTE TEMPORAIRE:
# - Pas encore de condition de victoire/defaite finale (ca vient ensuite).

import os
import random
import pygame

# -------------------- CONSTANTES --------------------
GRID_W = 10
GRID_H = 8
TILE_SIZE = 64
HUD_HEIGHT = 100
SCREEN_WIDTH = GRID_W * TILE_SIZE
SCREEN_HEIGHT = GRID_H * TILE_SIZE + HUD_HEIGHT
FPS = 60

PLAYER_MOVE_DELAY = 0.14
PLAYER_ATTACK_DELAY = 0.22
MONSTER_ATTACK_DELAY = 0.95
HIT_FLASH_TIME = 0.35
FIREBALL_SPEED = 12.0
FIREBALL_RANGE = 6.0

COLOR_BG = (30, 30, 30)
COLOR_GRID = (55, 55, 55)
COLOR_WALL = (95, 95, 105)
COLOR_CHEST = (155, 100, 40)
COLOR_HUD = (15, 15, 15)
COLOR_TEXT = (235, 235, 235)
COLOR_PLAYER = (70, 140, 220)
COLOR_MONSTER = (90, 200, 120)
COLOR_MONSTER_2 = (200, 180, 80)
COLOR_FLASH = (220, 60, 60)
FIRE_1 = (255, 220, 80)
FIRE_2 = (245, 150, 60)
FIRE_3 = (220, 60, 40)

POTIONS = [
    {"name": "Potion mineure", "heal": 2},
    {"name": "Potion moyenne", "heal": 4},
    {"name": "Potion majeure", "heal": 6},
]


# -------------------- OUTILS --------------------
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


# -------------------- CREATION ETATS --------------------
def create_player():
    return {
        "pos": [1, 1],
        "direction": "down",
        "hp": 20,
        "hp_max": 20,
        "atk": 2,
        "level": 1,
        "move_cooldown": 0.0,
        "attack_cooldown": 0.0,
        "hit_flash": 0.0,
    }


def wall_count_for_level(level):
    return min(3 + level, 10)


def generate_walls(level, player_pos):
    count = wall_count_for_level(level)
    forbidden = {tuple(player_pos)}

    walls = []
    for _ in range(count):
        tile = random_free_tile(forbidden)
        walls.append(tile)
        forbidden.add(tile)
    return walls


def generate_monsters(level, player_pos, walls):
    # Etape 15: on garde volontairement 1 monstre / niveau.
    forbidden = {tuple(player_pos)}
    for wall in walls:
        forbidden.add(wall)

    tile = random_free_tile(forbidden)
    return [
        {
            "type": "gobelin" if level >= 4 else "slime",
            "pos": [tile[0], tile[1]],
            "direction": random.choice(["left", "right", "up", "down"]),
            "hp": 3 + level // 2,
            "atk": 1,
            "alive": True,
            "move_cooldown": 0.0,
            "attack_cooldown": 0.0,
            "move_delay": max(0.3, 0.9 - 0.05 * level),
            "hit_flash": 0.0,
        }
    ]


def generate_chest(player_pos, monsters, walls):
    forbidden = {tuple(player_pos)}
    for wall in walls:
        forbidden.add(wall)
    for monster in monsters:
        forbidden.add(tuple(monster["pos"]))

    potion = random.choice(POTIONS)
    tile = random_free_tile(forbidden)
    return {
        "pos": [tile[0], tile[1]],
        "opened": False,
        "name": potion["name"],
        "heal": potion["heal"],
    }


def build_level_state(player):
    walls = generate_walls(player["level"], player["pos"])
    monsters = generate_monsters(player["level"], player["pos"], walls)
    chest = generate_chest(player["pos"], monsters, walls)
    projectiles = []
    msg = f"Niveau {player['level']} - Tue le monstre."
    return walls, monsters, chest, projectiles, msg


# -------------------- LOGIQUE --------------------
def try_move_player(player, keys, blocked):
    if player["move_cooldown"] > 0:
        return

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

    if in_bounds(target) and tuple(target) not in blocked:
        player["pos"] = target
        player["move_cooldown"] = PLAYER_MOVE_DELAY


def try_open_chest(player, chest):
    if chest is None or chest["opened"]:
        return None
    if not is_adjacent(player["pos"], chest["pos"]):
        return None

    chest["opened"] = True
    player["hp"] = min(player["hp_max"], player["hp"] + chest["heal"])
    return f"Coffre: {chest['name']} (+{chest['heal']} PV)"


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


def choose_random_step(monster_pos, player_pos, walls_set, occupied_set, chest):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    random.shuffle(dirs)
    for dx, dy in dirs:
        target = [monster_pos[0] + dx, monster_pos[1] + dy]
        if not is_monster_move_blocked(target, player_pos, walls_set, occupied_set, chest):
            return dx, dy
    return 0, 0


def update_monsters(monsters, player, chest, walls, dt):
    walls_set = set(walls)
    occupied = {tuple(monster["pos"]) for monster in monsters if monster["alive"]}

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
            if is_monster_move_blocked(target, player["pos"], walls_set, occupied, chest):
                continue

            occupied.remove(tuple(monster["pos"]))
            monster["pos"] = target
            if dx == -1:
                monster["direction"] = "left"
            elif dx == 1:
                monster["direction"] = "right"
            elif dy == -1:
                monster["direction"] = "up"
            elif dy == 1:
                monster["direction"] = "down"
            occupied.add(tuple(monster["pos"]))
            moved = True
            break

        if not moved:
            dx, dy = choose_random_step(monster["pos"], player["pos"], walls_set, occupied, chest)
            if dx != 0 or dy != 0:
                target = [monster["pos"][0] + dx, monster["pos"][1] + dy]
                occupied.remove(tuple(monster["pos"]))
                monster["pos"] = target
                if dx == -1:
                    monster["direction"] = "left"
                elif dx == 1:
                    monster["direction"] = "right"
                elif dy == -1:
                    monster["direction"] = "up"
                elif dy == 1:
                    monster["direction"] = "down"
                occupied.add(tuple(monster["pos"]))

        monster["move_cooldown"] = monster["move_delay"]


def update_projectiles(projectiles, monsters, walls, dt):
    walls_set = set(walls)

    for projectile in list(projectiles):
        dist = projectile["speed"] * dt
        if dist <= 0:
            continue
        if dist > projectile["range_left"]:
            dist = projectile["range_left"]

        projectile["pos"][0] += projectile["dir"][0] * dist
        projectile["pos"][1] += projectile["dir"][1] * dist
        projectile["range_left"] -= dist

        tile_x = int(projectile["pos"][0])
        tile_y = int(projectile["pos"][1])
        tile = [tile_x, tile_y]

        if not in_bounds(tile) or (tile_x, tile_y) in walls_set or projectile["range_left"] <= 0:
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


# -------------------- DESSIN --------------------
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


def draw_projectiles(screen, projectiles):
    for projectile in projectiles:
        px = projectile["pos"][0] * TILE_SIZE + TILE_SIZE // 2
        py = projectile["pos"][1] * TILE_SIZE + TILE_SIZE // 2
        center = (int(px), int(py))
        pygame.draw.circle(screen, FIRE_1, center, 9)
        pygame.draw.circle(screen, FIRE_2, center, 6)
        pygame.draw.circle(screen, FIRE_3, center, 3)


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
            fallback = COLOR_MONSTER
        else:
            sprite = hit_sprites["gobelin"] if flash else sprites["gobelin"]
            fallback = COLOR_MONSTER_2

        if sprite is not None:
            rotated = pygame.transform.rotate(sprite, angle)
            rect = rotated.get_rect(center=(px + TILE_SIZE // 2, py + TILE_SIZE // 2))
            screen.blit(rotated, rect)
        else:
            color = COLOR_FLASH if flash else fallback
            shape = pygame.Surface((TILE_SIZE - 20, TILE_SIZE - 20), pygame.SRCALPHA)
            shape.fill(color)
            rotated = pygame.transform.rotate(shape, angle)
            rect = rotated.get_rect(center=(px + TILE_SIZE // 2, py + TILE_SIZE // 2))
            screen.blit(rotated, rect)


def draw_hud(screen, font, player, monsters, message):
    alive_count = sum(1 for monster in monsters if monster["alive"])
    hud_y = GRID_H * TILE_SIZE
    pygame.draw.rect(screen, COLOR_HUD, (0, hud_y, SCREEN_WIDTH, HUD_HEIGHT))
    line_1 = f"PV: {player['hp']}/{player['hp_max']} | Niveau: {player['level']} | Monstres: {alive_count}"
    line_2 = "SPACE: boule de feu | E: coffre"
    screen.blit(font.render(line_1, True, COLOR_TEXT), (10, hud_y + 8))
    screen.blit(font.render(line_2, True, COLOR_TEXT), (10, hud_y + 34))
    screen.blit(font.render(message, True, COLOR_TEXT), (10, hud_y + 62))


# -------------------- MAIN --------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Step 15 - Niveaux base")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 18)

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

player = create_player()
walls, monsters, chest, projectiles, message = build_level_state(player)

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

    player["move_cooldown"] = apply_cooldown(player["move_cooldown"], dt)
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

    # Regle de progression de l'etape 15
    alive_count = sum(1 for monster in monsters if monster["alive"])
    if alive_count == 0:
        player["level"] += 1
        walls, monsters, chest, projectiles, message = build_level_state(player)

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
# EXERCICE GUIDE - STEP 15 (NIVEAUX BASE)
# ------------------------------------------------------------
# Objectif de l'exercice:
# - Voir la progression quand tous les monstres sont morts.
#
# Etape 1:
# - Lance le jeu et elimine tous les monstres.
# - Verifie que le niveau augmente de +1.
#
# Etape 2:
# - Observe qu'un nouveau coffre apparait au niveau suivant.
# - Verifie que l'ancien coffre n'existe plus.
#
# Etape 3:
# - Dans le message HUD de creation de niveau, ajoute
#   le nombre de monstres pour mieux debug.
# ------------------------------------------------------------
