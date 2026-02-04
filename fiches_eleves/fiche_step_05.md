# Fiche Eleve - Step 05 - Dictionnaires

## 1) Notion du step (resume court)
- Stocker des donnees nommees d entites (joueur, coffre).

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_05_dictionnaires.py`
- Prerequis: Step 04
- Fonctions importantes: `in_bounds`, `is_adjacent`, `move_player`, `draw_world`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`
### Ce que ce step ajoute concretement
- `player` et `chest` sont des dictionnaires.
- Acces lecture/criture via `dico['cle']`.
- Interaction E + adjacency pour ouvrir le coffre.

## 3) Aide-memoire detaille (notion principale)
- Un dictionnaire mappe des cles vers des valeurs.
- Tres adapte pour des entites de jeu (position, hp, direction, etc.).
- `dico.get('cle', valeur_defaut)` evite un crash si la cle manque.
- On peut imbriquer listes/dicos pour representer des scenes.

### Exemple minimal
```python
player = {'pos': [1, 1], 'direction': 'down'}
player['direction'] = 'left'
if chest['opened'] is False:
    ...
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Parcours: `for k, v in dico.items(): ...`.
- Copie superficielle: `copy()`.
- Attention aux structures mutables partagees.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Ajouter une cle `hp` au player et l afficher dans le HUD (ou texte).
- [ ] Modifier les positions de depart via le dictionnaire.
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
