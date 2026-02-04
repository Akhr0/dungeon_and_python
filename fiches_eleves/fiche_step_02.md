# Fiche Eleve - Step 02 - Conditions (if / elif / else)

## 1) Notion du step (resume court)
- Autoriser ou bloquer les actions selon des conditions.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_02_conditions.py`
- Prerequis: Step 01
- Fonctions importantes: (pas encore de `def` dans ce step)
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`
### Ce que ce step ajoute concretement
- Lecture des touches puis conversion en variables directionnelles.
- Blocage des sorties de grille avec des tests de limites.
- Une seule direction appliquee grace a `if/elif`.

## 3) Aide-memoire detaille (notion principale)
- `if` teste une condition, `elif` teste une alternative, `else` est le cas restant.
- Operateurs de comparaison: `== != < > <= >=`.
- On combine des conditions avec `and`, `or`, `not`.
- Dans un jeu grille, chaque mouvement se valide par des gardes simples.

### Exemple minimal
```python
if player_x < GRID_W - 1:
    player_x += 1
else:
    player_x = 0
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Ecriture compacte: `x = a if condition else b`.
- Priorite logique: `not` > `and` > `or`.
- Bonne pratique: des conditions courtes et lisibles.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Modifier une limite (ex: `GRID_W - 2`) et observer.
- [ ] Essayer une logique tunnel (sortie droite -> retour gauche).
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
