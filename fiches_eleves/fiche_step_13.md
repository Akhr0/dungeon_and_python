# Fiche Eleve - Step 13 - Rotation + flash rouge

## 1) Notion du step (resume court)
- Ameliorer le feedback visuel de direction et degats.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_13_rotation_flash.py`
- Prerequis: Step 12
- Fonctions importantes: `apply_cooldown`, `in_bounds`, `is_adjacent`, `direction_to_vector`, `direction_to_angle`, `is_flashing`, `random_free_tile`, `generate_walls`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `HUD_HEIGHT`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `WALL_COUNT`
### Ce que ce step ajoute concretement
- `direction_to_angle` pilote la rotation du rendu.
- `hit_flash` + `is_flashing(...)` pour clignotement degats.
- Effet applique au joueur et aux monstres.

## 3) Aide-memoire detaille (notion principale)
- Feedback visuel = information immediate pour le joueur.
- Timer court (`HIT_FLASH_TIME`) suffit pour signaler un impact.
- Rotation depend d une direction logique (`left/right/up/down`).
- Toujours garder fallback visuel simple (rectangle) pour debug.

### Exemple minimal
```python
flash = is_flashing(entity['hit_flash'])
color = COLOR_FLASH if flash else BASE_COLOR
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Tu peux ajouter shake camera, son, particles.
- Un feedback trop long peut nuire a la lisibilite.
- Separer etat gameplay et etat visuel est une bonne pratique.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Tester flash long/court.
- [ ] Verifier rotation correcte dans les 4 directions.
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
