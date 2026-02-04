# Fiche Eleve - Step 06 - Mouvement sur grille

## 1) Notion du step (resume court)
- Assembler les notions de base dans un mini moteur de deplacement propre.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_06_mouvement_grille.py`
- Prerequis: Step 05
- Fonctions importantes: `in_bounds`, `build_blocked_set`, `try_move_player`, `draw_grid`, `draw_walls`, `draw_player`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `COLOR_BG`, `COLOR_GRID`
### Ce que ce step ajoute concretement
- Fonctions cle: `build_blocked_set`, `try_move_player`, `draw_grid`.
- Collisions limites + murs dans un flux simple.
- Structure de boucle claire: events -> update -> draw.

## 3) Aide-memoire detaille (notion principale)
- `set` est utile pour accelerer les tests d appartenance (`in`).
- Sequence de frame propre = lecture input, calcul logique, rendu.
- Separateur fort: logique (deplacement) vs affichage (draw_*).
- La grille impose un monde discret (case par case).

### Exemple minimal
```python
blocked = build_blocked_set(walls)
keys = pygame.key.get_pressed()
try_move_player(player, keys, blocked)
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- `tuple(target) in blocked` est plus rapide que sur liste.
- Tu peux preparer un systeme de collision par couche (murs, entites, objets).
- Design utile: une fonction `can_move_to(tile)` unique.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Ajouter un mur et confirmer le blocage.
- [ ] Changer spawn joueur et confirmer la nouvelle position.
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
