# Fiche Eleve - Step 04 - Fonctions

## 1) Notion du step (resume court)
- Decouper le programme en blocs reutilisables.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_04_functions.py`
- Prerequis: Step 03
- Fonctions importantes: `in_bounds`, `compute_next_position`, `move_player`, `draw_world`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`
### Ce que ce step ajoute concretement
- Fonctions presentes: `in_bounds`, `compute_next_position`, `move_player`, `draw_world`.
- `return` renvoie un resultat a l appelant.
- Moins de duplication, logique plus lisible.

## 3) Aide-memoire detaille (notion principale)
- `def nom(parametres):` cree une fonction.
- Une fonction doit avoir une responsabilite claire.
- Parametres = entrees, `return` = sortie.
- Fonctions pures (sans effet de bord) utiles pour tester la logique.

### Exemple minimal
```python
def in_bounds(x, y):
    return 0 <= x < GRID_W and 0 <= y < GRID_H

new_x, new_y = compute_next_position(x, y, keys)
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Parametres optionnels: `def f(x, speed=1): ...`.
- Portee (scope): variable locale vs globale.
- Docstring: `"""role de la fonction"""`.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Creer `is_blocked(x, y, blocks)` puis l utiliser.
- [ ] Extraire encore le dessin en sous-fonctions (`draw_player`, `draw_blocks`).
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
