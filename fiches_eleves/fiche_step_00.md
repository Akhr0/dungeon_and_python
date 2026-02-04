# Fiche Eleve - Step 00 - Variables

## 1) Notion du step (resume court)
- Comprendre les variables et afficher leur valeur dans Pygame.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_00_variables.py`
- Prerequis: Aucun
- Fonctions importantes: (pas encore de `def` dans ce step)
- Constantes reperes: (non central dans ce step)
### Ce que ce step ajoute concretement
- Variables simples: `player_hp`, `player_name`, `player_is_alive`.
- Affichage texte avec `font.render(...)` puis `screen.blit(...)`.
- Condition visuelle simple: carre vert/rouge selon un booleen.

## 3) Aide-memoire detaille (notion principale)
- Une variable est une etiquette + une valeur. Le type de la valeur compte (int, str, bool).
- En Python, on assigne avec `=`. Exemple: `hp = 10`.
- Les f-strings (`f"...{var}..."`) sont ideales pour afficher des variables.
- Un booleen pilote souvent une branche `if/else`.

### Exemple minimal
```python
player_hp = 10
player_name = 'Lina'
player_is_alive = True

if player_is_alive:
    color = (50, 200, 50)
else:
    color = (200, 50, 50)
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Conversions utiles: `int('12')`, `str(25)`, `bool(0)`.
- Difference `=` (assigner) vs `==` (comparer).
- Convention de nommage debutant: noms clairs en snake_case.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Modifier les 3 variables de depart et observer l impact a l ecran.
- [ ] Ajouter une variable perso (ex: `player_level`) puis l afficher.
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
