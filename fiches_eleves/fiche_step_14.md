# Fiche Eleve - Step 14 - Sprites assets

## 1) Notion du step (resume court)
- Passer du rendu rectangle au rendu image avec fallback.

## 2) Dans le code de ce step (precis)
- Script a lancer:
  - `python cours_20_etapes/step_14_sprites_assets.py`
- Prerequis: Step 13
- Fonctions importantes: `apply_cooldown`, `in_bounds`, `is_adjacent`, `direction_to_vector`, `direction_to_angle`, `is_flashing`, `random_free_tile`, `load_sprite`
- Constantes reperes: `GRID_W`, `GRID_H`, `TILE_SIZE`, `HUD_HEIGHT`, `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `FPS`, `WALL_COUNT`
### Ce que ce step ajoute concretement
- Chargement images via `load_sprite` (mage, slime, gobelin).
- Sprites rouges via `make_hit_sprite` pour flash degats.
- Fallback automatique en rectangle si image absente.

## 3) Aide-memoire detaille (notion principale)
- Un asset est un fichier externe charge au runtime.
- Toujours gerer l erreur de chargement (fichier manquant).
- `convert_alpha()` conserve la transparence PNG.
- Rendu: sprite normal vs sprite hit selon `hit_flash`.

### Exemple minimal
```python
sprite = load_sprite(path, TILE_SIZE - 16)
if sprite is None:
    pygame.draw.rect(screen, fallback_color, rect)
```

## 4) Aller plus loin (au dela de ce qu on code ici)
- Sprite sheets pour animations multi-frames.
- Cache de surfaces pour eviter de recalculer.
- Pipeline simple: load -> scale -> rotate -> blit.

## 5) Ce que tu dois avoir fait / vu / modifie dans ce step
- [ ] Confirmer sprites visibles.
- [ ] Renommer temporairement un png et verifier fallback.
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
