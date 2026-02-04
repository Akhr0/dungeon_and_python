# Step 05 - Dictionaries (version ultra simple)
# Objectif: comprendre les DICTIONNAIRES (dict) en Python
# avec seulement 1 ou 2 dictionnaires maximum.
#
# IDEE CLE DU CHAPITRE:
# - Un dictionnaire = une "fiche" avec des infos nommees (cles)
# - On lit: dico["cle"]
# - On modifie: dico["cle"] = ...
#
# Dans ce step:
# - player est un dictionnaire (pos + direction)
# - chest est un dictionnaire (pos + opened)
# - Interaction: touche E pour ouvrir le coffre si on est a cote

# VERSION ELEVE A COMPLETER
# Complete uniquement les zones balisees dans ce fichier.

import pygame

# ------------------------------------------------------------
# 1) VARIABLES DE LA GRILLE
# ------------------------------------------------------------

GRID_W = 10
GRID_H = 8
TILE_SIZE = 64

SCREEN_WIDTH = GRID_W * TILE_SIZE
SCREEN_HEIGHT = GRID_H * TILE_SIZE

# ------------------------------------------------------------
# 2) MINI-FICHE - DICTIONNAIRES (A RETENIR)
# ------------------------------------------------------------
#
# Un dictionnaire se note avec { } et contient des "cles".
#
# Chaque element du dictionnaire est une paire:
#   cle: valeur
# Exemple:
#   "hp": 10
# Ici:
# - "hp" est la cle (le nom du champ)
# - 10 est la valeur stockee dans ce champ
#
# Exemple:
#   player = {"hp": 10, "name": "Gandalf"}
#
# Lire une valeur:
#   player["hp"] -> 10
#
# Modifier une valeur:
#   player["hp"] = 5
#
# Ajouter une nouvelle cle:
#   player["atk"] = 2
#
# ATTENTION DEBUTANT:
# - La cle doit exister quand on lit player["hp"]
#   sinon Python fait une erreur (KeyError).
# - Pour ce cours, on cree toujours les cles principales
#   au moment de creer le dictionnaire.
#
# ------------------------------------------------------------

# ------------------------------------------------------------
# 3) FONCTIONS UTILES (simples)
# ------------------------------------------------------------

def in_bounds(pos):
    # pos est une liste [x, y]
    x = pos[0]
    y = pos[1]
    return 0 <= x < GRID_W and 0 <= y < GRID_H


def is_adjacent(a, b):
    # a et b sont des positions [x, y]
    # On verifie si elles sont cote a cote (pas en diagonale).
    #
    # abs() enlève le signe - et garde seulement la valeur.
    # Exemple: abs(-1) = 1
    #
    # Si la somme des distances en x et y vaut 1,
    # alors on est adjacent.
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1


def move_player(player, keys):
    # player est un dictionnaire
    # On lit/modifie ses infos avec des cles, ex:
    #   player["pos"], player["direction"]

    # Position actuelle
    x = player["pos"][0]
    y = player["pos"][1]

    # Position "voulue"
    new_x = x
    new_y = y

    if keys[pygame.K_LEFT]:
        new_x -= 1
        player["direction"] = "left"
    elif keys[pygame.K_RIGHT]:
        new_x += 1
        player["direction"] = "right"
    elif keys[pygame.K_UP]:
        new_y -= 1
        player["direction"] = "up"
    elif keys[pygame.K_DOWN]:
        new_y += 1
        player["direction"] = "down"

    # On verifie seulement les limites de la grille
    new_pos = [new_x, new_y]
    if in_bounds(new_pos) == True:
        player["pos"] = new_pos


def draw_world(screen, player, chest):
    # Dessiner fond
    screen.fill((30, 30, 30))

    # Dessiner le coffre (si pas ouvert)
    if chest["opened"] == False:
        cx = chest["pos"][0]
        cy = chest["pos"][1]
        pygame.draw.rect(
            screen,
            (150, 100, 40),  # marron
            (cx * TILE_SIZE, cy * TILE_SIZE, TILE_SIZE, TILE_SIZE),
        )

    # Dessiner le joueur
    px = player["pos"][0]
    py = player["pos"][1]
    pygame.draw.rect(
        screen,
        (200, 50, 50),  # rouge
        (px * TILE_SIZE, py * TILE_SIZE, TILE_SIZE, TILE_SIZE),
    )

# ------------------------------------------------------------
# 4) INITIALISATION PYGAME
# ------------------------------------------------------------

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Step 05 - Dictionaries (simple)")
clock = pygame.time.Clock()

# ------------------------------------------------------------
# 5) DONNEES: 2 DICTIONNAIRES MAX
# ------------------------------------------------------------

# ============================================================
# >>>>>>>>>>>>>> ZONE A COMPLETER PAR L'ELEVE >>>>>>>>>>>>>>>
# >>> Ecris ton code ENTRE les deux balises START / END
# >>> START CODE ELEVE
# (Attendu: dictionnaire player avec pos et direction)
player = {}

# (Attendu: dictionnaire chest avec pos et opened)
chest = {}
# <<< END CODE ELEVE
# <<<<<<<<<<<<<< FIN ZONE A COMPLETER <<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================

# ------------------------------------------------------------
# 6) BOUCLE PRINCIPALE
# ------------------------------------------------------------

running = True
while running:

    # Evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Interaction: touche E -> ouvrir le coffre si adjacent
        # ============================================================
# >>>>>>>>>>>>>> ZONE A COMPLETER PAR L'ELEVE >>>>>>>>>>>>>>>
# >>> Ecris ton code ENTRE les deux balises START / END
# >>> START CODE ELEVE
        # (Attendu: si touche E + coffre ferme + adjacent -> chest["opened"] = True)

        # <<< END CODE ELEVE
# <<<<<<<<<<<<<< FIN ZONE A COMPLETER <<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================

    # Mouvement
    keys = pygame.key.get_pressed()
    move_player(player, keys)

    # Affichage
    draw_world(screen, player, chest)
    pygame.display.flip()
    clock.tick(6)

pygame.quit()

# ------------------------------------------------------------
# EXERCICE - DICTIONNAIRES (SIMPLE)
# ------------------------------------------------------------
#
# Objectif:
# S'entrainer a lire/modifier des valeurs dans un dictionnaire.
#
# ------------------------------------------------------------
# 1) MODIFIER DES VALEURS
# ------------------------------------------------------------
#
# - Change la position du joueur au depart:
#     player["pos"] = [ ... , ... ]
#
# - Change la position du coffre:
#     chest["pos"] = [ ... , ... ]
#
# ------------------------------------------------------------
# 2) AJOUTER UNE CLE AU JOUEUR
# ------------------------------------------------------------
#
# - Ajoute une cle "hp" au dictionnaire player:
#     player["hp"] = 10
#
# - (Option) Ajoute une cle "name":
#     player["name"] = "..."
#
# Pour l'instant ca ne s'affiche pas, mais ca existe dans la fiche du joueur.
#
# ------------------------------------------------------------
# 3) BONUS (petit)
# ------------------------------------------------------------
#
# - Quand le coffre s'ouvre, change sa couleur au lieu de le cacher.
#   Indice:
#   - ajoute une cle "color" dans chest
#   - et change-la quand opened passe a True
#
# Exemple:
#   chest["color"] = (150, 100, 40)
#   puis:
#   chest["color"] = (200, 200, 0)
#
# ------------------------------------------------------------
