# Fiche Eleve - Step 12 - Projectiles

## 1) Notion du step (resume court)
- Permettre au joueur d attaquer a distance.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_12_projectiles.py`
- Prerequis: Step 11
- Fonctions importantes: `apply_cooldown`, `in_bounds`, `is_adjacent`, `direction_to_vector`, `random_free_tile`, `generate_walls`, `generate_monsters`, `generate_chest`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `HUD_HEIGHT`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `WALL_COUNT`
### Ce que ce step ajoute concretement
- Creation projectile sur SPACE via `try_player_attack`.
- Update continue de la liste `projectiles`.
- Collision projectile vs murs / monstres + suppression.

## 3) Aide-memoire detaille (notion principale)
- Un projectile stocke position float, direction, vitesse, portee, degats.
- Iteration sur copie (`for p in list(projectiles)`) utile quand on supprime.
- Un tile hit est calcule via `int(pos)` en monde grille.
- Toujours borner la portee (`range_left`).

### Exemple minimal
```python
projectiles.append({
    'pos': [float(px), float(py)],
    'dir': [dx, dy],
    'speed': FIREBALL_SPEED,
    'range_left': FIREBALL_RANGE,
})
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Tu peux ajouter penetration, explosion ou rebond.
- Separateur utile: logique physique vs logique degats.
- Pour perf, spatial hashing si beaucoup de projectiles.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Tester vitesse et portee.
- [ ] Verifier mort monstre quand hp <= 0.
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
