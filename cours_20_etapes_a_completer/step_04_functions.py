# Step 04 - Functions
# Objectif: comprendre les FONCTIONS en Python
# et organiser le code en petits blocs reutilisables.
#
# IDEE CLE DU CHAPITRE:
# - Une fonction sert a "regrouper" du code sous un nom
# - On peut appeler cette fonction plusieurs fois
# - Ca rend le code plus lisible et plus facile a modifier
#
# Dans ce step, on va:
# - separer le code en 3 fonctions principales
#   1) in_bounds : verifier si une position est dans la grille
#   2) move_player : calculer le deplacement du joueur
#   3) draw_world : dessiner le monde (murs + joueur)
#
# PREMIERE RENCONTRE DETAILLEE DE "def":
# def nom_fonction(param1, param2):
#     instructions
#
# - "def" sert a CREER une fonction
# - les parametres (entre parentheses) sont les informations
#   qu'on envoie a la fonction
# - "return" sert a RENVOYER un resultat
# - pour utiliser la fonction, on l'appelle par son nom:
#   resultat = nom_fonction(...)

# VERSION ELEVE A COMPLETER
# Complete uniquement les zones balisees dans ce fichier.

import pygame

# ------------------------------------------------------------
# 1) VARIABLES DE LA GRILLE (deja vues)
# ------------------------------------------------------------

GRID_W = 10
GRID_H = 8
TILE_SIZE = 64

SCREEN_WIDTH = GRID_W * TILE_SIZE
SCREEN_HEIGHT = GRID_H * TILE_SIZE

# ------------------------------------------------------------
# 2) FONCTIONS (COEUR DU CHAPITRE)
# ------------------------------------------------------------

def in_bounds(x, y):
    # Fonction: in_bounds
    # Role: dire si une position (x, y) est DANS la grille.
    #
    # Une fonction peut RENVOYER une valeur avec "return".
    # Ici, on renvoie soit True soit False.
    #
    # Exemple:
    # in_bounds(0, 0) -> True
    # in_bounds(-1, 0) -> False
    # ============================================================
# >>>>>>>>>>>>>> ZONE A COMPLETER PAR L'ELEVE >>>>>>>>>>>>>>>
# >>> Ecris ton code ENTRE les deux balises START / END
# >>> START CODE ELEVE

    # <<< END CODE ELEVE
# <<<<<<<<<<<<<< FIN ZONE A COMPLETER <<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================
    return False


def compute_next_position(x, y, keys):
    # Fonction: compute_next_position
    # Role: calculer la position suivante du joueur en fonction du clavier.
    #
    # IMPORTANT:
    # - Ici, on calcule seulement la "position voulue"
    # - On ne verifie pas encore les murs ou les limites
    #
    # Cette fonction renvoie un "couple" (x, y)
    # Exemple: return new_x, new_y

    new_x = x
    new_y = y

    # On traite une seule direction a la fois (if/elif)
    if keys[pygame.K_LEFT]:
        new_x -= 1
    elif keys[pygame.K_RIGHT]:
        new_x += 1
    elif keys[pygame.K_UP]:
        new_y -= 1
    elif keys[pygame.K_DOWN]:
        new_y += 1

    return new_x, new_y


def move_player(x, y, blocks, keys):
    # Fonction: move_player
    # Role: bouger le joueur SI le mouvement est autorise.
    #
    # Etapes:
    # 1) calculer la position voulue
    # 2) verifier si on reste dans la grille
    # 3) verifier si on ne va pas sur un block
    # 4) renvoyer la nouvelle position (ou l'ancienne si c'est bloque)

    # 1) Position voulue
    new_x, new_y = compute_next_position(x, y, keys)

    # 2) Verifier les limites de la grille
    is_inside = in_bounds(new_x, new_y)
    if is_inside == False:
        return x, y  # mouvement refuse -> on ne bouge pas

    # 3) Verifier les blocks (liste)
    if (new_x, new_y) in blocks:
        return x, y  # mouvement refuse -> on ne bouge pas

    # 4) Mouvement accepte
    return new_x, new_y


def draw_world(screen, player_pos, blocks):
    # Fonction: draw_world
    # Role: dessiner toute la scene.
    #
    # IMPORTANT:
    # - Cette fonction ne change AUCUNE variable du jeu
    # - Elle sert seulement a afficher

    # Fond
    screen.fill((30, 30, 30))

    # Dessiner les blocks (liste de positions)
    # Chaque element de "blocks" est une position sous la forme:
    # (x, y)
    #
    # Pour l'instant, on ne "separe" PAS directement (x, y).
    # On utilise les indices:
    # - position[0] -> x
    # - position[1] -> y

    for block in blocks:
        bx = block[0]  # coordonnee x du block
        by = block[1]  # coordonnee y du block

        pygame.draw.rect(
            screen,
            (80, 80, 80),
            (bx * TILE_SIZE, by * TILE_SIZE, TILE_SIZE, TILE_SIZE),
        )

    # Dessiner le joueur
    # player_pos est un couple (x, y)
    # On recupere chaque valeur avec les indices

    px = player_pos[0]
    py = player_pos[1]

    pygame.draw.rect(
        screen,
        (200, 50, 50),
        (px * TILE_SIZE, py * TILE_SIZE, TILE_SIZE, TILE_SIZE),
    )


# ------------------------------------------------------------
# 3) INITIALISATION PYGAME
# ------------------------------------------------------------

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Step 04 - Functions")
clock = pygame.time.Clock()

# ------------------------------------------------------------
# 4) VARIABLES DU JEU (donnees)
# ------------------------------------------------------------

player_x, player_y = 1, 1

# Liste de blocks (comme Step 03)
blocks = [
    (3, 3),
    (3, 4),
    (4, 4),
    (6, 2),
]

# ------------------------------------------------------------
# 5) BOUCLE PRINCIPALE
# ------------------------------------------------------------

running = True
while running:

    # Fermeture fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lecture clavier
    keys = pygame.key.get_pressed()

    # Mise a jour: on appelle UNE fonction au lieu de recopier du code
    # ============================================================
# >>>>>>>>>>>>>> ZONE A COMPLETER PAR L'ELEVE >>>>>>>>>>>>>>>
# >>> Ecris ton code ENTRE les deux balises START / END
# >>> START CODE ELEVE
    # (Attendu: appel de move_player puis appel de draw_world)

    # <<< END CODE ELEVE
# <<<<<<<<<<<<<< FIN ZONE A COMPLETER <<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================

    pygame.display.flip()
    clock.tick(6)

pygame.quit()

# ------------------------------------------------------------
# EXERCICE - APPRENDRE LES FONCTIONS
# ------------------------------------------------------------
#
# Objectif:
# Comprendre qu'une fonction permet de reutiliser du code
# et de rendre le programme plus clair.
#
# IMPORTANT:
# - Tu ne dois PAS casser le programme
# - Tu vas surtout modifier / ajouter des fonctions
#
# ------------------------------------------------------------
# 1) MODIFIER UNE FONCTION
# ------------------------------------------------------------
#
# - Dans in_bounds(x, y), change la taille de la zone autorisee:
#   Exemple: autoriser seulement un rectangle 0..7 en x et 0..5 en y
#   -> Observe: le joueur est maintenant "coince" dans une zone plus petite
#
# ------------------------------------------------------------
# 2) AJOUTER UNE FONCTION
# ------------------------------------------------------------
#
# - Cree une fonction:
#     is_blocked(x, y, blocks)
#   qui renvoie True si (x, y) est dans blocks, sinon False.
#
# - Puis utilise cette fonction dans move_player
#   au lieu d'ecrire directement:
#     if (new_x, new_y) in blocks:
#
# ------------------------------------------------------------
# 3) FONCTION = REUTILISATION
# ------------------------------------------------------------
#
# - Cree une fonction:
#     draw_player(screen, x, y)
#   qui dessine le joueur.
#
# - Cree une fonction:
#     draw_blocks(screen, blocks)
#   qui dessine tous les blocks.
#
# - Ensuite, dans draw_world, appelle draw_blocks et draw_player
#   au lieu de tout dessiner dans draw_world.
#
# ------------------------------------------------------------
# 4) QUESTION (REFLEXION)
# ------------------------------------------------------------
#
# - Pourquoi c'est pratique d'avoir des fonctions ?
# - Si tu veux changer la couleur du joueur, tu dois la changer
#   a UN seul endroit ou a plusieurs endroits ?
#
# ------------------------------------------------------------
# FIN
# ------------------------------------------------------------
