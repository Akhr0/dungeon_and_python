# Journal Des Notions (Parcours Debutant)

Objectif:
- garder une trace de la **premiere etape** qui explique une notion;
- eviter de reexpliquer 10 fois la meme chose;
- savoir quand il faut etre tres detaille (premiere rencontre).

Regle d'ecriture:
- si la notion apparait pour la premiere fois: explication tres detaillee;
- si la notion a deja ete vue: rappel court uniquement.

## Notions deja introduites

- Step 00:
  - variable (`int`, `str`, `bool`)
  - `import`
  - boucle `while`
  - evenements Pygame (`pygame.event.get`, `QUIT`)
  - dessin d'un rectangle (`pygame.draw.rect`)
  - affichage texte (`font.render`, `screen.blit`)
  - rafraichissement (`pygame.display.flip`)

- Step 01:
  - boucle `for`
  - `range(...)`
  - incrementation simple (`x = x + 1`)

- Step 02:
  - conditions `if / elif / else`
  - comparaisons (`==`, `<`, `>`, etc.)

- Step 03:
  - listes `[]`
  - tuples `(x, y)`
  - test d'appartenance `in` / `not in`

- Step 04:
  - fonctions `def`
  - parametres
  - `return`

- Step 05:
  - dictionnaires `{}` (cles/valeurs)
  - lecture/modification via `dico["cle"]`

- Step 06:
  - assemblage des notions de base dans une boucle de jeu complete
  - collisions simples (murs + limites)

- Step 07:
  - generation aleatoire (`random`)
  - monde variable au lancement

- Step 08:
  - interaction joueur (touche d action)
  - soin via coffre

- Step 09:
  - premiere entite monstre
  - liste de dictionnaires pour gerer plusieurs entites

- Step 10:
  - IA simple: approche joueur sinon deplacement aleatoire

- Step 11:
  - degats
  - cooldown d attaque

- Step 12:
  - projectiles
  - mise a jour d une liste dynamique + collisions

- Step 13:
  - feedback visuel (rotation directionnelle + flash degats)

- Step 14:
  - chargement d assets image
  - fallback si fichier image absent

- Step 15:
  - progression par niveaux
  - regeneration de l etat de niveau

- Step 16:
  - paliers de difficulte
  - boss niveau 10

- Step 17:
  - lisibilite HUD et messages de progression

- Step 18:
  - etats globaux de jeu (`play`, `game_over`, `win`)

- Step 19:
  - integration complete (pre-final)
  - validation de toutes les regles

- Step 20:
  - version finale de reference
  - base pour futur refactoring en plusieurs fichiers
