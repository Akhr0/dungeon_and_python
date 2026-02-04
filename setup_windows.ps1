$ErrorActionPreference = "Stop"

Write-Host "=== Setup Windows: Dungeon & Python ==="

$pythonCmd = $null
if (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCmd = "py -3"
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
} else {
    throw "Python introuvable. Installe Python depuis https://www.python.org/downloads/"
}

Write-Host "Creation du venv..."
if ($pythonCmd -eq "py -3") {
    py -3 -m venv .venv
} else {
    python -m venv .venv
}

Write-Host "Installation des dependances..."
& ".\.venv\Scripts\python.exe" -m pip install --upgrade pip
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt

Write-Host ""
Write-Host "Setup termine."
Write-Host "Active l'environnement avec:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host "Puis lance un script, par exemple:"
Write-Host "  python cours_20_etapes\step_00_variables.py"
