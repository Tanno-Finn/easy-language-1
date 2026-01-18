# Architektur: Leichte Sprache Übersetzungs-Workflow

## Überblick

```
┌─────────────────────────────────────────────────────────────────┐
│                        BENUTZER                                 │
│                           │                                     │
│                           ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    CLAUDE CODE                           │   │
│  │  (Liest CLAUDE.md, wendet Direktiven an)                │   │
│  └─────────────────────────────────────────────────────────┘   │
│                           │                                     │
│           ┌───────────────┼───────────────┐                    │
│           ▼               ▼               ▼                    │
│      ┌────────┐     ┌──────────┐    ┌──────────┐              │
│      │ input/ │     │directives│    │  output/ │              │
│      └────────┘     └──────────┘    └──────────┘              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Ordnerstruktur

```
easy-language-1/
│
├── CLAUDE.md                 # Hauptkonfiguration für Claude Code
├── .gitignore                # Ignoriert input/, output/, .idea/
│
├── docs/                     # Projektdokumentation
│   ├── vision.md             # Projektziel, Zielgruppen, Prinzipien
│   └── architecture.md       # Technische Architektur (diese Datei)
│
├── directives/              # Übersetzungs-Direktiven
│   ├── leichte-sprache.md   # Regeln für A1/A2-Niveau
│   ├── einfache-sprache.md  # Regeln für B1-Niveau
│   ├── commits.md           # Git-Commit-Richtlinien
│   └── direktive.md         # Meta: Wie neue Direktiven erstellt werden
│
├── scripts/                  # Setup- und Hilfsskripte
│   ├── setup.ps1             # Windows-Setup (PowerShell)
│   ├── setup.sh              # Linux/Mac-Setup (Bash)
│   ├── convert.ps1           # Markdown → Word Konvertierung
│   └── requirements.txt      # Python-Abhängigkeiten
│
├── input/                   # Quelldateien (gitignored)
│   ├── leicht/              # Dateien für Leichte Sprache
│   └── einfach/             # Dateien für Einfache Sprache
│
└── output/                   # Übersetzte Dateien (gitignored)
```

---

## Komponenten

### 1. CLAUDE.md (Hauptkonfiguration)

Die zentrale Steuerungsdatei. Definiert:
- Verfügbare Direktiven und wann sie anzuwenden sind
- Routing-Logik (expliziter Befehl > Ordnerstruktur > Nachfragen)
- Output-Konventionen (`_leichte_sprache.md`, `_einfache_sprache.md`)
- Sicherheitsregeln (keine Halluzinationen, Fachbegriffe beibehalten)

### 2. Direktiven

| Datei | Zweck | Priorität |
|-------|-------|-----------|
| `leichte-sprache.md` | A1/A2 Übersetzungsregeln mit Hybrid-Regel | Kernfunktion |
| `einfache-sprache.md` | B1 Übersetzungsregeln für Business-Kontext | Kernfunktion |
| `commits.md` | Git-Commit-Konventionen | Entwicklung |
| `direktive.md` | Template für neue Direktiven | Meta |

### 3. Input-Verarbeitung

**Unterstützte Formate:**
- `.txt` - Klartext
- `.md` - Markdown
- `.docx` - Word-Dokumente (via python-docx zum Lesen)

**Routing-Logik:**
```
1. Expliziter Befehl? → Nutze angegebene Direktive
2. Datei in input/leicht/? → leichte-sprache.md
3. Datei in input/einfach/? → einfache-sprache.md
4. Sonst? → NACHFRAGEN (niemals raten!)
```

### 4. Output-Generierung

**Namenskonvention:**
- `[original]_leichte_sprache.md` - Leichte Sprache Version
- `[original]_einfache_sprache.md` - Einfache Sprache Version

**QA-Log:**
Jede übersetzte Datei enthält am Ende einen automatisch generierten QA-Anhang:
```markdown
---
### QA-Log (Automatisch generiert)
**Beibehaltene Fachbegriffe:** [Liste]
**Aufgelöste Abkürzungen:** [Liste]
**Getrennte Komposita:** [Liste]
```

---

## Setup & Installation

### Voraussetzungen

- Python 3.8+
- PowerShell (Windows) oder Bash (Linux/Mac)
- Chocolatey (Windows, optional für pandoc)

### Installation

**Windows (PowerShell als Administrator):**
```powershell
cd C:\Users\michi\Home\Projects\easy-language-1
.\scripts\setup.ps1
```

**Linux/Mac:**
```bash
cd ~/Projects/easy-language-1
chmod +x scripts/setup.sh
./scripts/setup.sh
```

### Was das Setup macht

1. **Chocolatey prüfen/installieren** (nur Windows)
2. **Pandoc installieren** - Für Markdown ↔ Word Konvertierung
3. **Python-Abhängigkeiten installieren** - `python-docx` für Word-Dokumente
4. **Ordnerstruktur erstellen** - `input/`, `output/`

### Manuelle Installation

Falls das Setup-Skript nicht funktioniert:

```bash
# Pandoc (wähle dein System)
choco install pandoc          # Windows
brew install pandoc           # macOS
sudo apt install pandoc       # Ubuntu/Debian

# Python-Abhängigkeiten
pip install -r scripts/requirements.txt
```

---

## Workflow

### Typischer Übersetzungs-Workflow

```
1. Quelldatei in input/ ablegen
   └── Optional: in input/leicht/ oder input/einfach/ für automatisches Routing

2. Claude Code starten
   └── "Übersetze die Datei XY in Leichte Sprache"
   └── Oder: "Übersetze alles im input-Ordner"

3. Claude liest Direktive und übersetzt
   └── Wendet Hybrid-Regel an (Fachbegriffe erhalten + erklären)
   └── Generiert QA-Log

4. Output in output/ prüfen
   └── [name]_leichte_sprache.md oder [name]_einfache_sprache.md

5. Optional: Zu Word konvertieren
   └── .\scripts\convert.ps1
```

### Konvertierung zu Word

```powershell
# Alle Markdown-Dateien im output-Ordner zu Word konvertieren
.\scripts\convert.ps1

# Einzelne Datei konvertieren
pandoc output/datei_leichte_sprache.md -o output/datei_leichte_sprache.docx
```

---

## Marker-System

Direktiven verwenden ein Marker-System zur Kennzeichnung von Regeln:

| Marker | Bedeutung | Wer darf ändern |
|--------|-----------|-----------------|
| `[M]` | Mandatory | Nur der User |
| `[C]` | Claude-Created | Claude darf anpassen |

**Beispiel:**
```markdown
- Fachbegriffe müssen erklärt werden [M]
- Maximal 5-7 Punkte pro Liste [C]
```

---

## Erweiterbarkeit

### Neue Direktive hinzufügen

1. Neue `.md`-Datei in `directives/` erstellen
2. Template aus `directives/direktive.md` verwenden
3. In `CLAUDE.md` unter "Verfügbare Direktiven" eintragen

### Neue Sprache/Niveau hinzufügen

1. Direktive erstellen (z.B. `sehr-leichte-sprache.md`)
2. Routing-Logik in `CLAUDE.md` erweitern
3. Ordner `input/sehr-leicht/` anlegen (optional)

---

## Fehlerbehebung

### Pandoc nicht gefunden

```powershell
# Windows: Als Administrator ausführen
choco install pandoc -y

# Danach Terminal neu starten
```

### python-docx nicht gefunden

```bash
pip install python-docx
```

### Übersetzung verwendet falsche Direktive

1. Prüfen: Liegt die Datei im richtigen Unterordner?
2. Prüfen: Wurde die Direktive explizit angegeben?
3. Claude sollte nachfragen, wenn unklar

---

## Versionierung

| Version | Datum | Änderungen |
|---------|-------|------------|
| 1.0 | 2026-01-18 | Initiales Setup mit Leichte/Einfache Sprache |
