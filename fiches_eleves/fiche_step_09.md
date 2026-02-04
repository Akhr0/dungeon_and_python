# Fiche Eleve - Step 09 - Premier monstre (statique)

## 1) Notion du step (resume court)
- Introduire une nouvelle entite dans la scene.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_09_premier_monstre.py`
- Prerequis: Step 08
- Fonctions importantes: `in_bounds`, `is_adjacent`, `random_free_tile`, `generate_walls`, `generate_monsters`, `generate_chest`, `try_move_player`, `try_open_chest`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `HUD_HEIGHT`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `WALL_COUNT`
### Ce que ce step ajoute concretement
- `monsters` devient une liste de dictionnaires.
- Le monstre occupe une case et bloque le passage.
- Rendu dedie via `draw_monsters`.

## 3) Aide-memoire detaille (notion principale)
- Une entite = donnees + regles + rendu.
- Liste d entites = boucle unique pour update/draw.
- Champ `alive` prepare deja les futures suppressions.
- Structure standard monstre: pos, hp, atk, direction, alive.

### Exemple minimal
```python
monsters = [
    {'pos': [6, 2], 'alive': True, 'hp': 3, 'atk': 1}
]
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Tu peux passer a une classe plus tard, mais dictionnaire reste pedagogique.
- Garder des fonctions de creation (factory) simplifie les resets de niveau.
- Eviter de dupliquer la logique de collision entre entites.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Ajouter un second monstre et verifier le blocage.
- [ ] Modifier la couleur/type et observer.
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
