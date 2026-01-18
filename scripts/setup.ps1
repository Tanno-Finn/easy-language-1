# Setup-Skript für den Leichte-Sprache-Übersetzungs-Workflow
# Ausführen: .\scripts\setup.ps1 (PowerShell als Administrator)

Write-Host "=== Leichte Sprache Workflow Setup ===" -ForegroundColor Cyan
Write-Host ""

# Zum Projekt-Root wechseln (eine Ebene über scripts/)
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDir
Set-Location $ProjectRoot
Write-Host "Arbeitsverzeichnis: $ProjectRoot" -ForegroundColor Gray
Write-Host ""

# 1. Prüfen ob Chocolatey installiert ist
Write-Host "[1/4] Prüfe Chocolatey..." -ForegroundColor Yellow
if (!(Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Host "  -> Chocolatey nicht gefunden. Installiere..." -ForegroundColor Gray
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    Write-Host "  -> Chocolatey installiert!" -ForegroundColor Green
} else {
    Write-Host "  -> Chocolatey bereits vorhanden." -ForegroundColor Green
}

# 2. Pandoc installieren
Write-Host "[2/4] Prüfe Pandoc..." -ForegroundColor Yellow
if (!(Get-Command pandoc -ErrorAction SilentlyContinue)) {
    Write-Host "  -> Pandoc nicht gefunden. Installiere..." -ForegroundColor Gray
    choco install pandoc -y
    Write-Host "  -> Pandoc installiert!" -ForegroundColor Green
} else {
    $pandocVersion = pandoc --version | Select-Object -First 1
    Write-Host "  -> Pandoc bereits vorhanden: $pandocVersion" -ForegroundColor Green
}

# 3. Python-Abhängigkeiten installieren
Write-Host "[3/4] Installiere Python-Abhängigkeiten..." -ForegroundColor Yellow
$RequirementsFile = Join-Path $ScriptDir "requirements.txt"
if (Test-Path $RequirementsFile) {
    pip install -r $RequirementsFile --quiet
    Write-Host "  -> Python-Abhängigkeiten installiert!" -ForegroundColor Green
} else {
    Write-Host "  -> requirements.txt nicht gefunden in $ScriptDir!" -ForegroundColor Red
}

# 4. Ordnerstruktur erstellen
Write-Host "[4/4] Erstelle Ordnerstruktur..." -ForegroundColor Yellow
$folders = @("input", "input/erledigt", "output")
foreach ($folder in $folders) {
    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder -Force | Out-Null
        Write-Host "  -> Ordner '$folder' erstellt." -ForegroundColor Gray
    }
}
Write-Host "  -> Ordnerstruktur bereit!" -ForegroundColor Green

Write-Host ""
Write-Host "=== Setup abgeschlossen! ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Nutzung:" -ForegroundColor White
Write-Host "  1. Quelldateien in 'input/' ablegen"
Write-Host "  2. Claude Code starten und übersetzen lassen"
Write-Host "  3. Ergebnisse in 'output/' finden"
Write-Host ""
Write-Host "Konvertierung MD -> DOCX:" -ForegroundColor White
Write-Host "  pandoc output/datei.md -o output/datei.docx"
Write-Host ""
