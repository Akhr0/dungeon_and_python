# Dungeon And Python (cours debutant)

Projet Pygame pedagogique avec:
- un jeu final: `main.py`
- un parcours incremental: `cours_20_etapes/step_00` -> `step_20`
- des assets partages: `assets/`

## 1) Recuperer le projet

Option A (recommandee): cloner le repo
```bash
git clone https://github.com/Akhr0/dungeon_and_python.git
cd dungeon_and_python
```

Option B: Download ZIP depuis GitHub, puis dezipper le dossier.

---

## 2) Installation ultra simple (1 commande de setup)

Prerequis: Python installe sur la machine (idealement Python 3.11+).

### macOS
```bash
./setup_mac.sh
```

### Linux
```bash
./setup_linux.sh
```

### Windows (PowerShell)
```powershell
.\setup_windows.ps1
```

Si PowerShell bloque les scripts:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\setup_windows.ps1
```

---

## 3) Activer l'environnement virtuel

### macOS / Linux
```bash
source .venv/bin/activate
```

### Windows (PowerShell)
```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 4) Lancer les scripts

Premier cours:
```bash
python cours_20_etapes/step_00_variables.py
```

Jeu final du cours:
```bash
python cours_20_etapes/step_20_jeu_final.py
```

Version principale a la racine:
```bash
python main.py
```

---

## 5) Workflow eleve conseille

1. Lancer une etape (ex: `step_03_listes.py`)
2. Lire le code commente
3. Faire le bloc **EXERCICE GUIDE** en bas du fichier
4. Creer ses propres fichiers de test dans le repo (ex: `mes_tests.py`)
5. Passer a l'etape suivante

---

## 6) Structure du projet

- `main.py` : jeu principal
- `cours_20_etapes/` : progression complete du cours
- `cours_20_etapes/JOURNAL_NOTIONS.md` : suivi des notions deja introduites
- `assets/` : images du mage, slime, gobelin
- `requirements.txt` : dependances Python
- `setup_mac.sh`, `setup_linux.sh`, `setup_windows.ps1` : scripts d'installation

---

## 7) Depannage rapide

### Erreur: `ModuleNotFoundError: No module named 'pygame'`
Tu n'es pas dans le bon environnement.

- Active `.venv`
- Puis relance le script

### Reinstaller les dependances
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## 8) Commandes en jeu

- Fleches ou ZQSD: deplacement
- Espace: attaque / projectile
- E: interaction (coffre)
- Entree: rejouer (selon l'etape)
- Echap: quitter
