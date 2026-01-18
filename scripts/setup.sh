#!/bin/bash
# Setup-Skript für den Leichte-Sprache-Übersetzungs-Workflow
# Ausführen: chmod +x scripts/setup.sh && ./scripts/setup.sh

echo "=== Leichte Sprache Workflow Setup ==="
echo ""

# Zum Projekt-Root wechseln (eine Ebene über scripts/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"
echo "Arbeitsverzeichnis: $PROJECT_ROOT"
echo ""

# 1. Pandoc installieren
echo "[1/3] Prüfe Pandoc..."
if ! command -v pandoc &> /dev/null; then
    echo "  -> Pandoc nicht gefunden. Installiere..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        brew install pandoc
    elif [[ -f /etc/debian_version ]]; then
        # Debian/Ubuntu
        sudo apt-get update && sudo apt-get install -y pandoc
    elif [[ -f /etc/redhat-release ]]; then
        # RHEL/CentOS/Fedora
        sudo dnf install -y pandoc
    else
        echo "  -> Bitte Pandoc manuell installieren: https://pandoc.org/installing.html"
    fi
    echo "  -> Pandoc installiert!"
else
    echo "  -> Pandoc bereits vorhanden: $(pandoc --version | head -1)"
fi

# 2. Python-Abhängigkeiten installieren
echo "[2/3] Installiere Python-Abhängigkeiten..."
if [[ -f "requirements.txt" ]]; then
    pip install -r requirements.txt --quiet
    echo "  -> Python-Abhängigkeiten installiert!"
else
    echo "  -> requirements.txt nicht gefunden!"
fi

# 3. Ordnerstruktur erstellen
echo "[3/3] Erstelle Ordnerstruktur..."
mkdir -p input/erledigt output
echo "  -> Ordnerstruktur bereit!"

echo ""
echo "=== Setup abgeschlossen! ==="
echo ""
echo "Nutzung:"
echo "  1. Quelldateien in 'input/' ablegen"
echo "  2. Claude Code starten und übersetzen lassen"
echo "  3. Ergebnisse in 'output/' finden"
echo ""
echo "Konvertierung MD -> DOCX:"
echo "  pandoc output/datei.md -o output/datei.docx"
echo ""
