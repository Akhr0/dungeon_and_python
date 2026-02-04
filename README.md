# Le Donjon des 10 Salles

Mini-jeu pedagogique en Python / Pygame pour servir de support aux eleves.

## Installation rapide (recommandee)

Objectif: aucune dependance systeme autre que Python.

1) Installer Python 3.12 depuis https://www.python.org/downloads/
2) Ouvrir un terminal dans le dossier du projet
3) Creer et activer un venv

macOS / Linux:
```
python3.12 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):
```
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4) Installer les dependances:
```
python -m pip install -r requirements.txt
```

5) Lancer le jeu:
```
python main.py
```

## Scripts d'installation

macOS:
```
chmod +x setup_mac.sh
./setup_mac.sh
```

Linux:
```
chmod +x setup_linux.sh
./setup_linux.sh
```

Windows (PowerShell):
```
.\setup_windows.ps1
```

## Depannage (macOS)

Si vous avez une erreur du type `SDL.h` manquant ou `pygame.font` non disponible,
installez les libs SDL puis re-installez pygame:
```
brew install sdl2 sdl2_ttf
python -m pip install --force-reinstall --no-cache-dir pygame
```

## Commandes en jeu

- Fleches directionnelles ou ZQSD: deplacement
- Espace: attaquer
- E: interaction
- Entree: valider / demarrer / rejouer
- Echap: quitter
