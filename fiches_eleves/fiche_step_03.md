# Fiche Eleve - Step 03 - Listes

## 1) Notion du step (resume court)
- Utiliser une liste de positions pour representer les murs.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_03_listes.py`
- Prerequis: Step 02
- Fonctions importantes: (pas encore de `def` dans ce step)
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`
### Ce que ce step ajoute concretement
- `blocks = [(x, y), ...]` contient les cases bloquees.
- Test d appartenance avec `(new_x, new_y) not in blocks`.
- Boucle `for wx, wy in blocks` pour dessiner tous les murs.

## 3) Aide-memoire detaille (notion principale)
- Une liste garde un ordre et peut etre modifiee (`append`, `pop`, `remove`).
- Les indexes commencent a 0.
- Tuples `(x, y)` pratiques pour des coordonnees de grille.
- `in` et `not in` servent beaucoup en gameplay.

### Exemple minimal
```python
blocks = [(3, 3), (3, 4)]
if (new_x, new_y) not in blocks:
    player_x = new_x
    player_y = new_y
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Slices: `liste[1:4]`.
- Comprehensions: `[x*x for x in range(5)]`.
- Difference liste (mutable) vs tuple (plutot fixe).

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Ajouter/supprimer des murs dans `blocks`.
- [ ] Construire une ligne de murs avec une boucle `for`.
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
