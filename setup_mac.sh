#!/usr/bin/env bash
set -euo pipefail

echo "=== Setup macOS: Dungeon & Python ==="

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "Python introuvable. Installe Python depuis https://www.python.org/downloads/"
  exit 1
fi

echo "Python utilise: $($PYTHON_BIN --version)"

$PYTHON_BIN -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo ""
echo "Setup termine."
echo "Active l'environnement avec:"
echo "  source .venv/bin/activate"
echo "Puis lance un script, par exemple:"
echo "  python cours_20_etapes/step_00_variables.py"
