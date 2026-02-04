# Fiche Eleve - Step 16 - Vagues + boss

## 1) Notion du step (resume court)
- Introduire les paliers de difficulte et le boss du niveau 10.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_16_vagues_et_boss.py`
- Prerequis: Step 15
- Fonctions importantes: `apply_cooldown`, `in_bounds`, `is_adjacent`, `direction_to_vector`, `direction_to_angle`, `is_flashing`, `random_free_tile`, `load_sprite`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `HUD_HEIGHT`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `PLAYER_MOVE_DELAY`
### Ce que ce step ajoute concretement
- Regles: niveaux 1-4 (1 monstre), 5-9 (2 monstres), 10 (boss).
- Monstres plus rapides quand le niveau monte.
- Progression bornee pour garder le palier boss.

## 3) Aide-memoire detaille (notion principale)
- Le game design se code souvent en fonctions de palier (`if level >= ...`).
- Le boss est une variation d entite (stats, type, comportement).
- Toujours garder les regles lisibles et centralisees.
- Equilibrage = ajuster peu de constantes, tester souvent.

### Exemple minimal
```python
if level >= 10:
    spawn_boss()
elif level >= 5:
    spawn_two_monsters()
else:
    spawn_one_monster()
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Data-driven design: stocker les paliers dans un dictionnaire de config.
- Courbes progressives (lineaire, exponentielle, clamp).
- Difficulte percue != difficulte numerique (feedback important).

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Verifier palier 5 et palier 10 en jeu.
- [ ] Modifier temporairement un seuil puis revenir a la valeur cours.
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
