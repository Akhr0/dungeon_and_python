# Fiche Eleve - Step 10 - IA monstre simple

## 1) Notion du step (resume court)
- Donner un comportement autonome lisible aux monstres.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_10_ia_monstre_simple.py`
- Prerequis: Step 09
- Fonctions importantes: `in_bounds`, `is_adjacent`, `apply_cooldown`, `random_free_tile`, `generate_walls`, `generate_monsters`, `generate_chest`, `try_move_player`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `HUD_HEIGHT`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `WALL_COUNT`
### Ce que ce step ajoute concretement
- Approche prioritaire du joueur (`get_approach_steps`).
- Fallback aleatoire si chemin direct bloque (`choose_random_step`).
- Rythme de deplacement via cooldown (`MONSTER_MOVE_DELAY`).

## 3) Aide-memoire detaille (notion principale)
- IA debutant: regle deterministe simple > algo complexe opaque.
- Toujours verifier collisions avant d appliquer un mouvement IA.
- Cooldown = timer de tempo pour eviter des mouvements trop rapides.
- `dt` (delta time) rend la vitesse plus stable entre machines.

### Exemple minimal
```python
if not moved:
    dx, dy = choose_random_step(monster['pos'], player['pos'], walls_set, occupied_set, chest)
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Tu pourrais ajouter un mode 'patrouille' hors vue joueur.
- A* / BFS sont des options futures pour pathfinding reelle.
- Toujours garder une issue de secours (random step) pour eviter blocage complet.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Tester valeur haute/basse de MONSTER_MOVE_DELAY.
- [ ] Verifier que le monstre se rapproche puis se debloque en aleatoire.
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
