# Step 02 - Conditions
# Objectif: comprendre les CONDITIONS (if / elif / else)
# et voir comment elles autorisent ou bloquent une action.

# ------------------------------------------------------------
# MINI-FICHE - CONDITIONS (if / elif / else)
# ------------------------------------------------------------
#
# Une CONDITION permet de prendre une decision.
#
# Exemple:
#   if player_hp > 0:
#       print("Le joueur est en vie")
#
# Signifie : Si la vie du joueur est supérieure à 0, affiche le message "Le joueur est en vie"
#
# SYNTAXE A RETENIR:
# - "if condition:" commence un test
# - ":" est obligatoire
# - le bloc decale en dessous (indentation) s'execute seulement
#   si la condition est vraie
#
# Exemple simple:
#   if 3 > 1:
#       print("oui")
#
# -------------------------
# COMPARAISONS UTILES
# -------------------------
#
# ==   egal
# !=   different
# <    plus petit que
# >    plus grand que
# <=   plus petit ou egal
# >=   plus grand ou egal
#
# -------------------------
# if / elif
# -------------------------
#
# Exemple:
#   if gauche == 1:
#       ...
#   elif droite == 1:
#       ...
#
# - Une seule condition est executee
# - Les autres sont ignorees
#
# -------------------------
# POURQUOI DES CONDITIONS ?
# -------------------------
#
# - Autoriser une action
# - Bloquer une action
#
# Exemple:
# - empecher le joueur de sortir de la grille
#
# ------------------------------------------------------------


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
# 2) INITIALISATION PYGAME
# ------------------------------------------------------------

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Step 02 - Conditions")
clock = pygame.time.Clock()

# ------------------------------------------------------------
# 3) VARIABLES DU JOUEUR
# ------------------------------------------------------------

player_x = 1
player_y = 1

# ------------------------------------------------------------
# 4) VARIABLES DE CONTROLE (ETAT DES TOUCHES)
# ------------------------------------------------------------
# Ces variables valent:
# - 1 si la touche est appuyée
# - 0 si la touche n'est pas appuyée

gauche = 0
droite = 0
haut = 0
bas = 0

# ------------------------------------------------------------
# 5) BOUCLE PRINCIPALE
# ------------------------------------------------------------

running = True
while running:

    # --------------------------------------------------------
    # 5A) EVENEMENTS (fermer la fenêtre)
    # --------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --------------------------------------------------------
    # 5B) LECTURE DU CLAVIER (partie technique cachée)
    # --------------------------------------------------------
    # Cette partie sert UNIQUEMENT à mettre à jour
    # les variables gauche / droite / haut / bas.
    # Les élèves n'ont PAS besoin de la comprendre pour l'instant.

    keys = pygame.key.get_pressed()

    # Ecriture "compacte" de Python:
    # gauche = 1 if condition else 0
    # Equivalent plus long:
    # if keys[pygame.K_LEFT]:
    #     gauche = 1
    # else:
    #     gauche = 0
    #
    # On garde cette version courte ici pour ne pas alourdir le fichier.
    gauche = 1 if keys[pygame.K_LEFT] else 0
    droite = 1 if keys[pygame.K_RIGHT] else 0
    haut = 1 if keys[pygame.K_UP] else 0
    bas = 1 if keys[pygame.K_DOWN] else 0

    # --------------------------------------------------------
    # 5C) CONDITIONS DE DEPLACEMENT (COEUR DU CHAPITRE)
    # --------------------------------------------------------
    # A RETENIR:
    # - On teste des VARIABLES
    # - Si la condition est vraie (== 1), on autorise l'action
    # - "elif" veut dire: "sinon si"
    # - "elif" evite de faire plusieurs mouvements en meme temps

    # ============================================================
# >>>>>>>>>>>>>> ZONE A COMPLETER PAR L'ELEVE >>>>>>>>>>>>>>>
# >>> Ecris ton code ENTRE les deux balises START / END
# >>> START CODE ELEVE
    # (Attendu: bloc if / elif pour gerer gauche, droite, haut, bas avec limites)

    # <<< END CODE ELEVE
# <<<<<<<<<<<<<< FIN ZONE A COMPLETER <<<<<<<<<<<<<<<<<<<<<<<<
# ============================================================

    # --------------------------------------------------------
    # 5D) AFFICHAGE
    # --------------------------------------------------------

    screen.fill((30, 30, 30))

    pygame.draw.rect(
        screen,
        (200, 50, 50),
        (
            player_x * TILE_SIZE + 8,
            player_y * TILE_SIZE + 8,
            TILE_SIZE - 16,
            TILE_SIZE - 16,
        ),
    )

    pygame.display.flip()
    clock.tick(6)

# ------------------------------------------------------------
# 6) FERMETURE
# ------------------------------------------------------------

pygame.quit()





# ------------------------------------------------------------
# ENONCE - ALLER D'UN COTE A L'AUTRE DE LA GRILLE
# ------------------------------------------------------------
#
# Jusqu'ici, les CONDITIONS servent a BLOQUER le joueur
# pour l'empecher de sortir de la grille.
#
# ET SI on voulait faire autrement ?
#
# Imagine un monde "magique" :
# - si le joueur sort a DROITE, il reapparait a GAUCHE
# - si le joueur sort a GAUCHE, il reapparait a DROITE
# - pareil pour le HAUT et le BAS
#
# ------------------------------------------------------------
# INDICES
# ------------------------------------------------------------
#
# 1) Tu sais deja tester une limite :
#    if player_x < GRID_W - 1
#
# 2) Tu sais tester une egalite : ==
#
# 3) Tu sais modifier une variable : x = 2
#
# ------------------------------------------------------------
# FIN
# ------------------------------------------------------------

# ------------------------------------------------------------
# EXERCICE GUIDE - STEP 02 (CONDITIONS)
# ------------------------------------------------------------
# Objectif de l'exercice:
# - Manipuler if / elif / else avec un resultat visible a l'ecran.
#
# Etape 1 (tres simple):
# - Trouve cette condition:
#     if player_x > 0:
# - Remplace "> 0" par "> 1".
# - Lance le programme et verifie: le joueur ne peut plus aller
#   sur la colonne 0.
#
# Etape 2:
# - Remets "> 0".
# - Fais la meme chose pour la droite:
#     if player_x < GRID_W - 1:
# - Essaie avec GRID_W - 2 et observe la difference.
#
# Etape 3 (bonus guide):
# - Si tu veux un comportement "tunnel", ajoute un else apres
#   le test de droite:
#     else:
#         player_x = 0
# - Meme idee possible pour gauche / haut / bas.
# ------------------------------------------------------------
