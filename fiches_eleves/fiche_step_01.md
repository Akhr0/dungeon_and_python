# Fiche Eleve - Step 01 - Boucles (for + while)

## 1) Notion du step (resume court)
- Utiliser la boucle de jeu `while` et une boucle `for` pour repeter un dessin.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_01_loops.py`
- Prerequis: Step 00
- Fonctions importantes: (pas encore de `def` dans ce step)
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`
### Ce que ce step ajoute concretement
- `while running` garde la fenetre ouverte.
- `for colonne in range(GRID_W)` dessine une case par colonne.
- Mouvement automatique simple avec `player_x = player_x + 1`.

## 3) Aide-memoire detaille (notion principale)
- `while` = repeter tant qu une condition est vraie.
- `for` = iterer sur une sequence (`range`, liste, tuple, etc.).
- `range(n)` va de 0 a n-1. `range(a, b, pas)` existe aussi.
- Dans un jeu, la boucle principale fait: evenements -> update -> draw.

### Exemple minimal
```python
for i in range(5):
    print(i)  # 0,1,2,3,4

running = True
while running:
    # boucle du jeu
    running = False
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Mots-cle utiles: `break` (sortir de boucle), `continue` (passer au tour suivant).
- `enumerate(liste)` donne index + valeur en meme temps.
- Attention aux boucles infinies sans condition de sortie.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Tester plusieurs valeurs de `FPS`.
- [ ] Tester `range(5)` puis `range(GRID_W)` et comparer.
- [ ] Expliquer oralement la difference entre le role du while et du for.
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
