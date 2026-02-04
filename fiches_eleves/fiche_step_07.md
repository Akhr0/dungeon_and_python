# Fiche Eleve - Step 07 - Murs aleatoires

## 1) Notion du step (resume court)
- Generer proceduralement la salle avec `random`.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_07_murs_aleatoires.py`
- Prerequis: Step 06
- Fonctions importantes: `in_bounds`, `random_free_tile`, `generate_random_walls`, `try_move_player`, `draw_grid`, `draw_walls`, `draw_player`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `WALL_COUNT`, `COLOR_BG`
### Ce que ce step ajoute concretement
- `generate_random_walls(...)` construit la liste des murs.
- `random_free_tile(...)` evite les cases interdites.
- Le gameplay reste identique, seul le layout change.

## 3) Aide-memoire detaille (notion principale)
- Generation proceduralle = produire du contenu avec des regles.
- Toujours separer zones interdites (forbidden) et candidates.
- Un seed fixe (`random.seed(1)`) permet la reproductibilite.
- L aleatoire doit rester jouable (eviter de bloquer le spawn).

### Exemple minimal
```python
random.seed(1)
walls = generate_random_walls(player['pos'], WALL_COUNT)
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- `random.choice`, `randint`, `shuffle` sont les bases.
- Pour debug, logguer la liste finale des murs.
- Pour equilibrage, borner la densite de murs.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Tester WALL_COUNT bas puis haut.
- [ ] Tester seed fixe et verifier meme carte a chaque run.
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
