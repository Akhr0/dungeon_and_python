"""
MVP DONJON - VERSION ULTRA PEDAGOGIQUE

Objectif de ce fichier:
- Tout est dans un seul fichier.
- Beaucoup de commentaires, style "cours".
- Code volontairement simple a lire, meme si ce n'est pas le plus "pro".

Regles du jeu:
- Une seule salle.
- A chaque niveau: murs aleatoires, monstres, coffre.
- Quand TOUS les monstres du niveau sont morts: niveau +1.
- Niveau 5+: 2 monstres par vague.
- Niveau 10: boss.
- Coffre nouveau a chaque niveau (ancien remplace).

Touches:
- Fleches ou ZQSD: bouger
- SPACE: lancer une boule de feu
- E: ouvrir le coffre (si adjacent)
- ENTER: rejouer (apres win/game over)
- ESC: quitter
"""

import os
import random
import sys

import pygame


# ============================================================
# 1) CONSTANTES GLOBALES
# ============================================================

# Grille logique (en cases)
GRID_W = 10
GRID_H = 8

# Taille visuelle d'une case (en pixels)
TILE_SIZE = 64

# Bandeau d'interface en bas de l'ecran
HUD_HEIGHT = 110

# Taille finale de la fenetre
SCREEN_WIDTH = GRID_W * TILE_SIZE
SCREEN_HEIGHT = GRID_H * TILE_SIZE + HUD_HEIGHT

# Framerate
FPS = 60

# Cooldowns / vitesses (en secondes ou cases/seconde)
PLAYER_MOVE_DELAY = 0.14
PLAYER_ATTACK_DELAY = 0.22
MONSTER_ATTACK_DELAY = 0.95
FIREBALL_SPEED = 12.0
FIREBALL_RANGE = 6.0
HIT_FLASH_TIME = 0.35

# Couleurs
BG_COLOR = (30, 30, 30)
GRID_COLOR = (55, 55, 55)
WALL_COLOR = (95, 95, 105)
CHEST_COLOR = (155, 100, 40)
HUD_COLOR = (15, 15, 15)
TEXT_COLOR = (235, 235, 235)

PLAYER_COLOR = (70, 140, 220)
SLIME_COLOR = (90, 200, 120)
GOBELIN_COLOR = (200, 180, 80)
BOSS_COLOR = (170, 60, 120)

FIREBALL_COLOR_1 = (255, 220, 80)
FIREBALL_COLOR_2 = (245, 150, 60)
FIREBALL_COLOR_3 = (220, 60, 40)

# Contenu possible d'un coffre
POTIONS = [
    {"name": "Potion mineure", "heal": 2},
    {"name": "Potion moyenne", "heal": 4},
    {"name": "Potion majeure", "heal": 6},
]


# ============================================================
# 2) PETITS OUTILS GENERIQUES
# ============================================================


def apply_cooldown(value, dt):
    """Fait descendre un timer vers 0."""
    return max(0.0, value - dt)


def in_bounds(pos):
    """True si pos = [x, y] est dans la grille."""
    x = pos[0]
    y = pos[1]
    return 0 <= x < GRID_W and 0 <= y < GRID_H


def is_adjacent(a, b):
    """Adjacence en 4 directions (pas de diagonale)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1


def direction_to_vector(direction):
    """Convertit left/right/up/down en (dx, dy)."""
    if direction == "left":
        return -1, 0
    if direction == "right":
        return 1, 0
    if direction == "up":
        return 0, -1
    return 0, 1


def direction_to_angle(direction):
    """Angle de rotation sprite selon la direction."""
    if direction == "left":
        return -90
    if direction == "right":
        return 90
    if direction == "up":
        return 180
    return 0


def is_flashing(flash_timer):
    """Alterne ON/OFF pour effet de clignotement rouge."""
    return flash_timer > 0 and int(flash_timer * 16) % 2 == 0


def load_sprite(path, size):
    """Charge une image et la redimensionne. Retourne None si erreur."""
    try:
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(image, (size, size))
    except (pygame.error, FileNotFoundError):
        return None


def make_hit_sprite(sprite):
    """Cree une version rouge d'un sprite pour le flash de degats."""
    if sprite is None:
        return None
    hit_sprite = sprite.copy()
    hit_sprite.fill((255, 0, 0, 255), special_flags=pygame.BLEND_RGBA_MULT)
    return hit_sprite


def random_floor_tile(forbidden_tiles):
    """
    Choisit une case libre dans la zone interne (on evite les bords).

    forbidden_tiles = set de tuples interdits, par ex: {(1, 1), (3, 4)}
    """
    candidates = []

    for x in range(1, GRID_W - 1):
        for y in range(1, GRID_H - 1):
            tile = (x, y)
            if tile not in forbidden_tiles:
                candidates.append([x, y])

    if len(candidates) == 0:
        # Cas de secours tres rare
        return [1, 1]

    return random.choice(candidates)


# ============================================================
# 3) CREATION DES ENTITES (JOUEUR, MONSTRES, NIVEAU)
# ============================================================


def create_player():
    """Construit le dictionnaire joueur."""
    player = {
        "pos": [1, 1],
        "direction": "down",
        "hp_max": 20,
        "hp": 20,
        "atk": 2,
        "level": 1,
        "move_cooldown": 0.0,
        "attack_cooldown": 0.0,
        "hit_flash": 0.0,
    }
    return player


def monster_move_delay_for_level(level, monster_type):
    """
    Plus le niveau monte, plus les monstres jouent vite.
    (delay petit = rapide)
    """
    if monster_type == "boss":
        return max(0.30, 0.62 - 0.02 * level)
    return max(0.35, 0.90 - 0.045 * level)


def create_monster(monster_type, level, pos):
    """Construit un monstre (dict) selon son type."""
    if monster_type == "slime":
        hp = 3 + (level // 3)
        atk = 1
    elif monster_type == "gobelin":
        hp = 4 + (level // 2)
        atk = 1 + (level // 6)
    else:
        # boss
        hp = 20 + level
        atk = 3

    monster = {
        "type": monster_type,
        "pos": pos,
        "direction": random.choice(["left", "right", "up", "down"]),
        "hp": hp,
        "atk": atk,
        "move_cooldown": random.uniform(0.25, 0.55),
        "attack_cooldown": 0.0,
        "move_delay": monster_move_delay_for_level(level, monster_type),
        "hit_flash": 0.0,
    }
    return monster


def monster_count_for_level(level):
    """Regle du jeu: niveau 5+ => 2 monstres, niveau 10 => boss unique."""
    if level >= 10:
        return 1
    if level >= 5:
        return 2
    return 1


def choose_monster_type(level):
    """Type de monstre selon niveau."""
    if level < 4:
        return "slime"
    if level < 10:
        return random.choice(["slime", "gobelin"])
    return "boss"


def wall_count_for_level(level):
    """Nombre de murs par niveau."""
    return min(3 + level, 10)


def generate_walls(level, player_pos):
    """
    Genere une LISTE DE TUPLES.
    Exemple: [(3, 2), (4, 2), (7, 5)]
    """
    wall_count = wall_count_for_level(level)

    forbidden_tiles = set()
    forbidden_tiles.add(tuple(player_pos))

    # Petite zone de securite pres du joueur pour eviter un start bloque.
    safe_zone = [
        (player_pos[0] + 1, player_pos[1]),
        (player_pos[0], player_pos[1] + 1),
        (player_pos[0] + 1, player_pos[1] + 1),
    ]

    for sx, sy in safe_zone:
        if 1 <= sx < GRID_W - 1 and 1 <= sy < GRID_H - 1:
            forbidden_tiles.add((sx, sy))

    walls = []
    for _ in range(wall_count):
        pos = random_floor_tile(forbidden_tiles)
        wall_tuple = (pos[0], pos[1])
        walls.append(wall_tuple)
        forbidden_tiles.add(wall_tuple)

    return walls


def generate_monsters(level, player_pos, walls):
    """Cree la vague de monstres du niveau courant."""
    count = monster_count_for_level(level)

    forced_type = None
    if level >= 10:
        forced_type = "boss"

    forbidden_tiles = set()
    forbidden_tiles.add(tuple(player_pos))
    for wall in walls:
        forbidden_tiles.add(wall)

    monsters = []
    for _ in range(count):
        pos = random_floor_tile(forbidden_tiles)
        forbidden_tiles.add(tuple(pos))

        if forced_type is None:
            monster_type = choose_monster_type(level)
        else:
            monster_type = forced_type

        monsters.append(create_monster(monster_type, level, pos))

    return monsters


def generate_chest(player_pos, monsters, walls):
    """Cree un coffre avec potion aleatoire."""
    forbidden_tiles = set()
    forbidden_tiles.add(tuple(player_pos))

    for wall in walls:
        forbidden_tiles.add(wall)

    for monster in monsters:
        forbidden_tiles.add(tuple(monster["pos"]))

    potion = random.choice(POTIONS)

    chest = {
        "pos": random_floor_tile(forbidden_tiles),
        "opened": False,
        "name": potion["name"],
        "heal": potion["heal"],
    }
    return chest


def message_for_level(level):
    """Texte d'aide affiche dans le HUD."""
    if level >= 10:
        return "Niveau 10: Boss final !"
    if level >= 5:
        return f"Niveau {level}: vague de 2 monstres."
    return f"Niveau {level}: nouvelle vague."


def start_new_game():
    """Etat complet pour recommencer une partie."""
    player = create_player()

    walls = generate_walls(player["level"], player["pos"])
    monsters = generate_monsters(player["level"], player["pos"], walls)
    chest = generate_chest(player["pos"], monsters, walls)

    projectiles = []
    message = "Niveau 1: tue tous les monstres."

    return player, walls, monsters, chest, projectiles, message


# ============================================================
# 4) ACTIONS JOUEUR
# ============================================================


def try_move_player(player, keys, blocked_tiles):
    """
    Mouvement case-par-case.
    blocked_tiles = set de tuples bloquants (murs, monstres, coffre ferme).
    """
    if player["move_cooldown"] > 0:
        return

    target = [player["pos"][0], player["pos"][1]]

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

    if in_bounds(target) and tuple(target) not in blocked_tiles:
        player["pos"] = target
        player["move_cooldown"] = PLAYER_MOVE_DELAY


def try_open_chest(player, chest):
    """Ouvre le coffre si le joueur est adjacent."""
    if chest is None:
        return None
    if chest["opened"]:
        return None
    if not is_adjacent(player["pos"], chest["pos"]):
        return None

    chest["opened"] = True
    player["hp"] = min(player["hp_max"], player["hp"] + chest["heal"])

    return f"Coffre ouvert: {chest['name']} (+{chest['heal']} PV)"


def try_player_attack(player, projectiles):
    """Le mage tire une boule de feu dans sa direction."""
    if player["attack_cooldown"] > 0:
        return

    player["attack_cooldown"] = PLAYER_ATTACK_DELAY
    dx, dy = direction_to_vector(player["direction"])

    projectile = {
        "pos": [float(player["pos"][0]), float(player["pos"][1])],
        "dir": [dx, dy],
        "speed": FIREBALL_SPEED,
        "range_left": FIREBALL_RANGE,
        "damage": player["atk"],
    }
    projectiles.append(projectile)


# ============================================================
# 5) IA MONSTRES (VERSION SIMPLE)
# ============================================================


def is_monster_move_blocked(new_pos, player_pos, walls_set, occupied_set, chest):
    """Renvoie True si le monstre ne peut pas aller sur new_pos."""
    if not in_bounds(new_pos):
        return True

    if tuple(new_pos) in walls_set:
        return True

    if new_pos == player_pos:
        # Le monstre frappe en etant adjacent, il ne rentre pas dans la case joueur.
        return True

    if tuple(new_pos) in occupied_set:
        # Case deja occupee par un autre monstre.
        return True

    if chest is not None and not chest["opened"] and new_pos == chest["pos"]:
        return True

    return False


def get_steps_to_approach_player(monster_pos, player_pos):
    """
    Retourne 1 ou 2 pas tries pour se rapprocher.
    Le pas principal est sur l'axe avec la plus grande distance.
    """
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


def choose_random_wander_step(monster_pos, player_pos, walls_set, occupied_set, chest):
    """
    Si impossible de s'approcher du joueur,
    on choisit une direction aleatoire valide.
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    random.shuffle(directions)

    for dx, dy in directions:
        new_pos = [monster_pos[0] + dx, monster_pos[1] + dy]
        if not is_monster_move_blocked(new_pos, player_pos, walls_set, occupied_set, chest):
            return dx, dy

    return 0, 0


def move_monster_to(monster, new_pos, dx, dy, occupied_set):
    """Applique le deplacement d'un monstre + met a jour sa direction."""
    old_tile = (monster["pos"][0], monster["pos"][1])
    occupied_set.remove(old_tile)

    monster["pos"] = new_pos

    if dx == -1:
        monster["direction"] = "left"
    elif dx == 1:
        monster["direction"] = "right"
    elif dy == -1:
        monster["direction"] = "up"
    elif dy == 1:
        monster["direction"] = "down"

    occupied_set.add(tuple(monster["pos"]))


def update_monsters(monsters, player, chest, walls, dt):
    """
    Logique simple demandee:
    1) Si adjacent: attaque.
    2) Sinon, essaie de se rapprocher du joueur.
    3) Si bloque, bouge aleatoirement.
    """
    walls_set = set(walls)

    occupied_set = set()
    for monster in monsters:
        occupied_set.add(tuple(monster["pos"]))

    for monster in monsters:
        # Cooldowns
        monster["move_cooldown"] = apply_cooldown(monster["move_cooldown"], dt)
        monster["attack_cooldown"] = apply_cooldown(monster["attack_cooldown"], dt)

        # Attaque au contact
        if is_adjacent(monster["pos"], player["pos"]):
            if monster["attack_cooldown"] <= 0:
                player["hp"] -= monster["atk"]
                player["hit_flash"] = HIT_FLASH_TIME
                monster["attack_cooldown"] = MONSTER_ATTACK_DELAY
            continue

        # Pas encore son tour de mouvement
        if monster["move_cooldown"] > 0:
            continue

        moved = False

        # Etape 1: tentative de rapprochement
        steps_to_try = get_steps_to_approach_player(monster["pos"], player["pos"])
        for dx, dy in steps_to_try:
            new_pos = [monster["pos"][0] + dx, monster["pos"][1] + dy]
            blocked = is_monster_move_blocked(
                new_pos,
                player["pos"],
                walls_set,
                occupied_set,
                chest,
            )
            if blocked:
                continue

            move_monster_to(monster, new_pos, dx, dy, occupied_set)
            moved = True
            break

        # Etape 2: si bloque, vagabondage aleatoire
        if not moved:
            dx, dy = choose_random_wander_step(
                monster["pos"],
                player["pos"],
                walls_set,
                occupied_set,
                chest,
            )

            if dx != 0 or dy != 0:
                new_pos = [monster["pos"][0] + dx, monster["pos"][1] + dy]
                blocked = is_monster_move_blocked(
                    new_pos,
                    player["pos"],
                    walls_set,
                    occupied_set,
                    chest,
                )
                if not blocked:
                    move_monster_to(monster, new_pos, dx, dy, occupied_set)

        # Quoi qu'il arrive, on attend le prochain "tick" de mouvement
        monster["move_cooldown"] = monster["move_delay"]


# ============================================================
# 6) PROJECTILES
# ============================================================


def update_projectiles(projectiles, monsters, walls, dt):
    """
    Fait avancer chaque boule de feu.
    Gere collisions murs + monstres.
    """
    walls_set = set(walls)

    for projectile in list(projectiles):
        # Distance parcourue pendant cette frame
        distance = projectile["speed"] * dt
        if distance <= 0:
            continue

        # Ne jamais depasser la distance restante
        if distance > projectile["range_left"]:
            distance = projectile["range_left"]

        # Deplacement
        projectile["pos"][0] += projectile["dir"][0] * distance
        projectile["pos"][1] += projectile["dir"][1] * distance
        projectile["range_left"] -= distance

        # Case courante de la boule
        tile_x = int(projectile["pos"][0])
        tile_y = int(projectile["pos"][1])
        tile = [tile_x, tile_y]

        # Sortie de grille ou collision mur
        if not in_bounds(tile):
            projectiles.remove(projectile)
            continue

        if (tile_x, tile_y) in walls_set:
            projectiles.remove(projectile)
            continue

        # Collision monstre
        hit_monster = None
        for monster in monsters:
            if monster["pos"][0] == tile_x and monster["pos"][1] == tile_y:
                hit_monster = monster
                break

        if hit_monster is not None:
            hit_monster["hp"] -= projectile["damage"]
            hit_monster["hit_flash"] = HIT_FLASH_TIME

            if hit_monster["hp"] <= 0:
                monsters.remove(hit_monster)

            projectiles.remove(projectile)
            continue

        # Fin de portee
        if projectile["range_left"] <= 0:
            projectiles.remove(projectile)


# ============================================================
# 7) GESTION DE PROGRESSION
# ============================================================


def level_up(player):
    """Passe au niveau suivant (max = 10)."""
    player["level"] = min(10, player["level"] + 1)


def build_new_level_state(player):
    """Genere murs + monstres + coffre pour le niveau courant."""
    walls = generate_walls(player["level"], player["pos"])
    monsters = generate_monsters(player["level"], player["pos"], walls)
    chest = generate_chest(player["pos"], monsters, walls)
    projectiles = []
    message = message_for_level(player["level"])
    return walls, monsters, chest, projectiles, message


# ============================================================
# 8) AFFICHAGE
# ============================================================


def draw_grid(screen):
    """Dessine les lignes de la grille."""
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, GRID_H * TILE_SIZE), 1)

    for y in range(0, GRID_H * TILE_SIZE, TILE_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y), 1)


def draw_walls(screen, walls):
    """Dessine chaque mur (liste de tuples)."""
    for wx, wy in walls:
        px = wx * TILE_SIZE
        py = wy * TILE_SIZE
        pygame.draw.rect(screen, WALL_COLOR, (px + 8, py + 8, TILE_SIZE - 16, TILE_SIZE - 16))
        pygame.draw.rect(screen, (70, 70, 80), (px + 12, py + 12, TILE_SIZE - 24, TILE_SIZE - 24), 2)


def draw_chest(screen, chest):
    """Dessine le coffre s'il n'est pas ouvert."""
    if chest is None:
        return
    if chest["opened"]:
        return

    px = chest["pos"][0] * TILE_SIZE
    py = chest["pos"][1] * TILE_SIZE
    pygame.draw.rect(screen, CHEST_COLOR, (px + 12, py + 12, TILE_SIZE - 24, TILE_SIZE - 24))


def draw_projectiles(screen, projectiles):
    """Dessine les boules de feu."""
    for projectile in projectiles:
        px = projectile["pos"][0] * TILE_SIZE + TILE_SIZE // 2
        py = projectile["pos"][1] * TILE_SIZE + TILE_SIZE // 2
        center = (int(px), int(py))

        pygame.draw.circle(screen, FIREBALL_COLOR_1, center, 9)
        pygame.draw.circle(screen, FIREBALL_COLOR_2, center, 6)
        pygame.draw.circle(screen, FIREBALL_COLOR_3, center, 3)


def draw_player(screen, player, sprites, hit_sprites):
    """Dessine le joueur avec rotation + flash rouge si touche."""
    px = player["pos"][0] * TILE_SIZE
    py = player["pos"][1] * TILE_SIZE

    angle = direction_to_angle(player["direction"])
    flash_on = is_flashing(player["hit_flash"])

    normal_sprite = sprites["player"]
    hit_sprite = hit_sprites["player"]

    if normal_sprite is not None:
        sprite_to_draw = normal_sprite
        if flash_on and hit_sprite is not None:
            sprite_to_draw = hit_sprite

        rotated = pygame.transform.rotate(sprite_to_draw, angle)
        rect = rotated.get_rect(center=(px + TILE_SIZE // 2, py + TILE_SIZE // 2))
        screen.blit(rotated, rect)
    else:
        color = PLAYER_COLOR
        if flash_on:
            color = (220, 60, 60)

        shape = pygame.Surface((TILE_SIZE - 16, TILE_SIZE - 16), pygame.SRCALPHA)
        shape.fill(color)

        rotated = pygame.transform.rotate(shape, angle)
        rect = rotated.get_rect(center=(px + TILE_SIZE // 2, py + TILE_SIZE // 2))
        screen.blit(rotated, rect)


def draw_monsters(screen, monsters, sprites, hit_sprites):
    """Dessine tous les monstres vivants."""
    for monster in monsters:
        px = monster["pos"][0] * TILE_SIZE
        py = monster["pos"][1] * TILE_SIZE

        angle = direction_to_angle(monster["direction"])
        flash_on = is_flashing(monster["hit_flash"])

        # Choix sprite / couleur de base
        sprite = None
        hit_sprite = None
        fallback_color = BOSS_COLOR

        if monster["type"] == "slime":
            sprite = sprites["slime"]
            hit_sprite = hit_sprites["slime"]
            fallback_color = SLIME_COLOR
        elif monster["type"] == "gobelin":
            sprite = sprites["gobelin"]
            hit_sprite = hit_sprites["gobelin"]
            fallback_color = GOBELIN_COLOR

        if sprite is not None:
            sprite_to_draw = sprite
            if flash_on and hit_sprite is not None:
                sprite_to_draw = hit_sprite

            rotated = pygame.transform.rotate(sprite_to_draw, angle)
            rect = rotated.get_rect(center=(px + TILE_SIZE // 2, py + TILE_SIZE // 2))
            screen.blit(rotated, rect)
        else:
            color = fallback_color
            if flash_on:
                color = (220, 60, 60)

            shape = pygame.Surface((TILE_SIZE - 20, TILE_SIZE - 20), pygame.SRCALPHA)
            shape.fill(color)

            rotated = pygame.transform.rotate(shape, angle)
            rect = rotated.get_rect(center=(px + TILE_SIZE // 2, py + TILE_SIZE // 2))
            screen.blit(rotated, rect)


def draw_hud(screen, font, player, walls, monsters, chest, message):
    """Dessine les infos en bas de l'ecran."""
    hud_y = GRID_H * TILE_SIZE
    pygame.draw.rect(screen, HUD_COLOR, (0, hud_y, SCREEN_WIDTH, HUD_HEIGHT))

    line_1 = (
        f"PV: {player['hp']}/{player['hp_max']}   "
        f"Niveau: {player['level']}   "
        f"Monstres: {len(monsters)}   "
        f"Murs: {len(walls)}"
    )

    if chest is not None and not chest["opened"]:
        line_2 = f"Coffre: {chest['name']} (appuie sur E pres du coffre)"
    else:
        line_2 = "Coffre: deja ouvert"

    line_3 = message

    controls = "Fleches/ZQSD: bouger | SPACE: feu | E: coffre | ESC: quitter"

    screen.blit(font.render(line_1, True, TEXT_COLOR), (10, hud_y + 8))
    screen.blit(font.render(line_2, True, TEXT_COLOR), (10, hud_y + 32))
    screen.blit(font.render(line_3, True, TEXT_COLOR), (10, hud_y + 56))
    screen.blit(font.render(controls, True, (190, 190, 190)), (10, hud_y + 80))


def draw_center_text(screen, font, text):
    """Ecran simple avec texte centre (win/game over)."""
    screen.fill((20, 20, 20))
    label = font.render(text, True, TEXT_COLOR)
    rect = label.get_rect(center=(SCREEN_WIDTH // 2, (GRID_H * TILE_SIZE) // 2))
    screen.blit(label, rect)


# ============================================================
# 9) BOUCLE PRINCIPALE
# ============================================================


def main():
    # --- Initialisation Pygame ---
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Donjon MVP - 1 salle")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("arial", 20)
    big_font = pygame.font.SysFont("arial", 28)

    # --- Chargement des sprites (optionnel) ---
    base_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_dir, "assets")

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

    # --- Etat de jeu initial ---
    player, walls, monsters, chest, projectiles, message = start_new_game()
    game_state = "play"  # play | game_over | win

    while True:
        dt = clock.tick(FPS) / 1000.0

        # ====================================================
        # A) EVENEMENTS (touches ponctuelles)
        # ====================================================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if game_state == "play":
                    if event.key == pygame.K_e:
                        chest_message = try_open_chest(player, chest)
                        if chest_message is not None:
                            message = chest_message

                    if event.key == pygame.K_SPACE:
                        try_player_attack(player, projectiles)

                elif game_state in {"game_over", "win"}:
                    if event.key == pygame.K_RETURN:
                        player, walls, monsters, chest, projectiles, message = start_new_game()
                        game_state = "play"

        # ====================================================
        # B) UPDATE LOGIQUE (seulement pendant la partie)
        # ====================================================
        if game_state == "play":
            # Cooldowns joueur
            player["move_cooldown"] = apply_cooldown(player["move_cooldown"], dt)
            player["attack_cooldown"] = apply_cooldown(player["attack_cooldown"], dt)
            player["hit_flash"] = apply_cooldown(player["hit_flash"], dt)

            # Cooldown visuel hit des monstres
            for monster in monsters:
                monster["hit_flash"] = apply_cooldown(monster["hit_flash"], dt)

            # Cases bloquees pour le joueur
            blocked_tiles = set()

            for wall in walls:
                blocked_tiles.add(wall)

            for monster in monsters:
                blocked_tiles.add(tuple(monster["pos"]))

            if chest is not None and not chest["opened"]:
                blocked_tiles.add(tuple(chest["pos"]))

            # Mouvement joueur
            keys = pygame.key.get_pressed()
            try_move_player(player, keys, blocked_tiles)

            # IA monstres + projectiles
            update_monsters(monsters, player, chest, walls, dt)
            update_projectiles(projectiles, monsters, walls, dt)

            # Progression: niveau suivant quand TOUS les monstres sont morts
            if len(monsters) == 0:
                # Si on vide le niveau 10 (boss), victoire
                if player["level"] >= 10:
                    game_state = "win"
                else:
                    level_up(player)
                    walls, monsters, chest, projectiles, message = build_new_level_state(player)

            # Defaite
            if player["hp"] <= 0:
                game_state = "game_over"

        # ====================================================
        # C) DESSIN
        # ====================================================
        if game_state == "play":
            screen.fill(BG_COLOR)
            draw_grid(screen)
            draw_walls(screen, walls)
            draw_chest(screen, chest)
            draw_projectiles(screen, projectiles)
            draw_monsters(screen, monsters, sprites, hit_sprites)
            draw_player(screen, player, sprites, hit_sprites)
            draw_hud(screen, font, player, walls, monsters, chest, message)

        elif game_state == "game_over":
            draw_center_text(screen, big_font, "Game Over - ENTER pour recommencer")

        elif game_state == "win":
            draw_center_text(screen, big_font, "Victoire ! Boss vaincu - ENTER pour rejouer")

        pygame.display.flip()


if __name__ == "__main__":
    main()
