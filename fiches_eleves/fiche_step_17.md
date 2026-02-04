# Fiche Eleve - Step 17 - Progression affinee

## 1) Notion du step (resume court)
- Rendre la progression plus lisible via HUD et messages explicites.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_17_progression_affinee.py`
- Prerequis: Step 16
- Fonctions importantes: `apply_cooldown`, `in_bounds`, `is_adjacent`, `direction_to_vector`, `direction_to_angle`, `is_flashing`, `random_free_tile`, `load_sprite`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `HUD_HEIGHT`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `PLAYER_MOVE_DELAY`
### Ce que ce step ajoute concretement
- HUD enrichi (niveau, pv, murs, monstres).
- Messages de niveau plus informatifs.
- Confirmation du remplacement coffre a chaque niveau.

## 3) Aide-memoire detaille (notion principale)
- UX gameplay: montrer clairement ce que le joueur doit faire maintenant.
- Le HUD doit rester court, stable et lisible en permanence.
- Les messages d etat servent a guider sans tutoriel externe.
- L affineur ne change pas la regle coeur, il clarifie l experience.

### Exemple minimal
```python
line_1 = f"PV: {player['hp']}/{player['hp_max']} | Niveau: {player['level']}"
line_2 = f"Monstres: {alive_count} | Murs: {len(walls)}"
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Codes couleurs uniformes pour infos positives/alertes.
- Prioriser 3-4 infos max a l ecran.
- Ajouter historique court des derniers evenements.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Verifier lecture HUD a chaud pendant combat.
- [ ] Reformuler un message pour le rendre plus clair.
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
