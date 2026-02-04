# Fiche Eleve - Step 19 - Pre-final integration

## 1) Notion du step (resume court)
- Valider toutes les mecaniques ensemble avant la version finale.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_19_pre_final.py`
- Prerequis: Step 18
- Fonctions importantes: `apply_cooldown`, `in_bounds`, `is_adjacent`, `direction_to_vector`, `direction_to_angle`, `is_flashing`, `load_sprite`, `make_hit_sprite`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `HUD_HEIGHT`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `PLAYER_MOVE_DELAY`
### Ce que ce step ajoute concretement
- Fichier integration complete avec fonctions isolees.
- Boucle principale robuste: events, update, draw selon state.
- Toutes les regles metier presentes (coffre, vagues, boss, win/lose).

## 3) Aide-memoire detaille (notion principale)
- Pre-final = etape de stabilisation, pas d ajout massif de features.
- But: detecter incoherences et regressions avant gel final.
- Checklist fonctionnelle obligatoire pour valider la build.
- Conserver lisibilite avant refactor multi-fichiers.

### Exemple minimal
```python
# integration: toutes les couches tournent ensemble
update_player(...)
update_monsters(...)
update_projectiles(...)
check_level_transition(...)
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Ajoute une mini matrice de tests manuels par feature.
- Noter les dettes techniques avant refacto.
- Mesurer difficulte reelle avec sessions courtes de playtest.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Passer la checklist complete (deplacement, tir, coffre, progression, boss).
- [ ] Identifier 1 point de lisibilite a ameliorer.
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
