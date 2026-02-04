# Fiche Eleve - Step 15 - Niveaux base

## 1) Notion du step (resume court)
- Declencher la progression quand tous les monstres sont morts.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_15_niveaux_base.py`
- Prerequis: Step 14
- Fonctions importantes: `apply_cooldown`, `in_bounds`, `is_adjacent`, `direction_to_vector`, `direction_to_angle`, `is_flashing`, `random_free_tile`, `load_sprite`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `HUD_HEIGHT`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `PLAYER_MOVE_DELAY`
### Ce que ce step ajoute concretement
- Condition de passage: `alive_count == 0`.
- Reconstruction niveau via `build_level_state(player)`.
- Nouveau coffre et nouveaux murs a chaque niveau.

## 3) Aide-memoire detaille (notion principale)
- Un niveau est un etat complet: murs + monstres + coffre + message.
- Regenerer un etat evite de laisser des restes du niveau precedent.
- Le joueur garde ses stats globales (hp, level) selon design choisi.
- La fonction de build centralise la logique de spawn.

### Exemple minimal
```python
alive_count = sum(1 for m in monsters if m['alive'])
if alive_count == 0:
    player['level'] += 1
    walls, monsters, chest, projectiles, message = build_level_state(player)
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Tu peux injecter une seed par niveau pour reproductibilite.
- Tu peux stocker des templates de salles predefinies.
- Penser au scaling progressif hp/atk/vitesse.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Nettoyer le niveau et verifier +1 level.
- [ ] Confirmer remplacement coffre/murs/monstres au changement de niveau.
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
