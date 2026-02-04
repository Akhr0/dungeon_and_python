# Fiche Eleve - Step 11 - Monstre attaque

## 1) Notion du step (resume court)
- Ajouter les degats et le rythme d attaque cote monstre.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_11_monstre_attaque.py`
- Prerequis: Step 10
- Fonctions importantes: `apply_cooldown`, `in_bounds`, `is_adjacent`, `random_free_tile`, `generate_walls`, `generate_monsters`, `generate_chest`, `try_move_player`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `HUD_HEIGHT`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `WALL_COUNT`
### Ce que ce step ajoute concretement
- Detection adjacency monstre/joueur avant attaque.
- `attack_cooldown` pour limiter la frequence de frappe.
- Baisse de `player['hp']` et message de danger.

## 3) Aide-memoire detaille (notion principale)
- Un combat minimum = condition de portee + degats + cooldown.
- Le cooldown se decremente a chaque frame avec `apply_cooldown`.
- Toujours separer mouvement et attaque dans la logique IA.
- Tu peux centraliser degats dans une fonction `deal_damage(...)`.

### Exemple minimal
```python
if is_adjacent(monster['pos'], player['pos']) and monster['attack_cooldown'] <= 0:
    player['hp'] -= monster['atk']
    monster['attack_cooldown'] = MONSTER_ATTACK_DELAY
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Ajouter invincibilite courte cote joueur (i-frames).
- Ajouter telegraphie visuelle avant attaque pour lisibilite.
- Securiser `hp = max(0, hp)`.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Tester MONSTER_ATTACK_DELAY lent/rapide.
- [ ] Modifier degat monstre puis revenir valeur equilibrage.
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
