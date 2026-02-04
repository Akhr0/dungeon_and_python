# Fiche Eleve - Step 08 - Coffre + potion

## 1) Notion du step (resume court)
- Ajouter une interaction contextuelle et un systeme de soin.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_08_coffre_potion.py`
- Prerequis: Step 07
- Fonctions importantes: `in_bounds`, `is_adjacent`, `random_free_tile`, `generate_random_walls`, `generate_chest`, `try_move_player`, `try_open_chest`, `draw_grid`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `WALL_COUNT`, `COLOR_BG`
### Ce que ce step ajoute concretement
- Fonctions cle: `is_adjacent`, `generate_chest`, `try_open_chest`.
- Action declenchee par evenement clavier (`KEYDOWN`, touche E).
- Etat du coffre (`opened`) + message de retour HUD.

## 3) Aide-memoire detaille (notion principale)
- Interaction de jeu = condition spatiale + input + effet.
- Adjacence Manhattan: `abs(dx) + abs(dy) == 1`.
- Toujours borner les points de vie avec `min(max_hp, hp + heal)`.
- Separer creation d objet et utilisation de l objet.

### Exemple minimal
```python
if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
    msg = try_open_chest(player, chest)
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- On peut generaliser `try_open_chest` pour d autres objets (porte, levier...).
- Pattern utile: event command (`if KEYDOWN ...`).
- Logique idempotente: ouvrir 1 fois seulement.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Ouvrir le coffre en etant adjacent.
- [ ] Verifier qu a distance E ne fait rien.
- [ ] Changer la vie max et observer le plafond de soin.
- [ ] Je peux expliquer la nouveaute de ce step avec mes mots.

## 6) Erreurs frequentes a surveiller
- Oublier de sauvegarder avant de relancer le script.
- Modifier trop de choses a la fois (garder de petits changements).
- Casser une indentation Python (erreur tres frequente en debut).

## 7) Notes eleve
- Ce que je retiens:
- Ce que je dois revoir:
- Question a poser au prochain cours:

---
Impression: ouvrir ce fichier Markdown puis `Ctrl+P` (ou `Cmd+P`).
