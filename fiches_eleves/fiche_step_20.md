# Fiche Eleve - Step 20 - Jeu final

## 1) Notion du step (resume court)
- Disposer d une version de reference stable pour le cours.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_20_jeu_final.py`
- Prerequis: Step 19
- Fonctions importantes: `apply_cooldown`, `in_bounds`, `is_adjacent`, `direction_to_vector`, `direction_to_angle`, `is_flashing`, `load_sprite`, `make_hit_sprite`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `HUD_HEIGHT`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `PLAYER_MOVE_DELAY`
### Ce que ce step ajoute concretement
- Version finale complete et jouable en 1 salle.
- Progression niveau + vagues + boss + states de fin.
- Pipeline pedagogique complet de step_00 a step_20.

## 3) Aide-memoire detaille (notion principale)
- Le final sert de reference fonctionnelle, pas forcement d architecture ideale.
- Stabilite > sophistication pour un support de cours debutant.
- On peut maintenant refactoriser en modules sans changer le comportement.
- Toujours garder un point de comparaison (golden behavior).

### Exemple minimal
```python
# final loop
while True:
    handle_events()
    if game_state == 'play':
        update_world()
    draw_world_or_screen()
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Refacto possible: `entities.py`, `combat.py`, `ui.py`, `world.py`.
- Ajouter sauvegarde progression (json).
- Ajouter tests unitaires sur fonctions pures.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Finir une run jusqu au boss.
- [ ] Tester au moins une victoire et une defaite.
- [ ] Modifier une constante d equilibrage et noter l effet.
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
