# Fiche Eleve - Step 18 - Game states

## 1) Notion du step (resume court)
- Gerer explicitement les etats globaux du jeu.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_18_game_states.py`
- Prerequis: Step 17
- Fonctions importantes: `apply_cooldown`, `in_bounds`, `is_adjacent`, `direction_to_vector`, `direction_to_angle`, `is_flashing`, `random_free_tile`, `load_sprite`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `HUD_HEIGHT`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `PLAYER_MOVE_DELAY`
### Ce que ce step ajoute concretement
- `game_state` prend `play`, `game_over`, `win`.
- Mise a jour logique seulement en state `play`.
- Ecrans centres de fin + restart via ENTER.

## 3) Aide-memoire detaille (notion principale)
- State machine simple = transitions predicibles et code plus propre.
- Chaque state decide quoi update et quoi dessiner.
- Transitions typiques: play->game_over, play->win, game_over->play.
- Le reset doit recreer un etat initial propre.

### Exemple minimal
```python
if game_state == 'play':
    update_game()
elif game_state == 'game_over':
    draw_game_over()
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Etats supplementaires possibles: pause, menu, loading.
- Transitions centralisees dans une fonction `set_state(...)`.
- Eviter les flags booleens multiples pour un meme systeme.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Declencher une defaite puis tester restart ENTER.
- [ ] Declencher une victoire puis tester restart ENTER.
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
