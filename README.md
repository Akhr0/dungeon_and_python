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

## 2) Installer Python (via l'installeur officiel, sans Homebrew)

Ouvre le terminal dans VS Code (menu `Terminal` → `New Terminal`) puis suis **exactement** les etapes de ton OS.

### macOS
1. Va sur `python.org` → `Downloads` → macOS.
2. Telecharge l'installeur `.pkg` le plus recent.
3. Double-clique, puis suis l'assistant.
4. Verifie dans le terminal VS Code:
```bash
python3 --version
```

### Windows
1. Va sur `python.org` → `Downloads` → Windows.
2. Telecharge l'installeur `.exe` le plus recent (64-bit).
3. Lance l'installeur et **coche "Add Python to PATH"**.
4. Verifie dans le terminal VS Code:
```powershell
python --version
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

Verifier l'installation:
```bash
python --version
```

Si `python` ne fonctionne pas, essaye:
```bash
python3 --version
```

---

## 3) Installation ultra simple (1 commande de setup)

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

## 4) Activer l'environnement virtuel

### macOS / Linux
```bash
source .venv/bin/activate
```

### Windows (PowerShell)
```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 5) Lancer les scripts

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

## 6) Workflow eleve conseille

1. Lancer une etape (ex: `step_03_listes.py`)
2. Lire le code commente
3. Faire le bloc **EXERCICE GUIDE** en bas du fichier
4. Creer ses propres fichiers de test dans le repo (ex: `mes_tests.py`)
5. Passer a l'etape suivante

---

## 7) Structure du projet

- `main.py` : jeu principal
- `cours_20_etapes/` : progression complete du cours
- `cours_20_etapes/JOURNAL_NOTIONS.md` : suivi des notions deja introduites
- `fiches_eleves/` : fiches imprimables step par step (00 -> 20)
- `assets/` : images du mage, slime, gobelin
- `requirements.txt` : dependances Python
- `setup_mac.sh`, `setup_linux.sh`, `setup_windows.ps1` : scripts d'installation

---

## 8) Depannage rapide

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

## 9) Commandes en jeu

- Fleches ou ZQSD: deplacement
- Espace: attaque / projectile
- E: interaction (coffre)
- Entree: rejouer (selon l'etape)
- Echap: quitter
