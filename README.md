# Leichte Sprache Workflow

> KI-gestützte, rechtssichere Übersetzung von Fachtexten in barrierefreie Sprache

[![Made with Claude Code](https://img.shields.io/badge/Made%20with-Claude%20Code-blueviolet)](https://github.com/anthropics/claude-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: German](https://img.shields.io/badge/Language-German-blue.svg)](https://de.wikipedia.org/wiki/Leichte_Sprache)

---

## Warum dieses Projekt?

Fachtexte sind für viele Menschen schwer verständlich:

| Zielgruppe | Problem |
|------------|---------|
| Menschen mit Lernschwierigkeiten | Komplexe Satzstrukturen |
| Deutsch als Zweitsprache | Fachvokabular, Redewendungen |
| Menschen mit Leseschwäche | Lange Texte, kleine Schrift |
| Eilige Leser | Zu viel Information auf einmal |

**Bestehende Lösungen versagen:**
- **Manuelle Übersetzung:** Teuer, langsam, inkonsistent
- **Standard-KI:** Verliert rechtliche Bedeutung, halluziniert, ignoriert Fachbegriffe

---

## Die Lösung: Hybrid-Ansatz

```
┌─────────────────────────────────────────────────────────────┐
│  FACHBEGRIFF BLEIBT ERHALTEN  +  WIRD ERKLÄRT              │
│                                                             │
│  "Wir speichern Ihre **personenbezogenen Daten**."         │
│  Das heißt:                                                 │
│  Informationen über Sie, zum Beispiel Ihr Name.            │
└─────────────────────────────────────────────────────────────┘
```

**Rechtssicherheit:** Fachbegriffe werden nie gelöscht oder ersetzt
**Verständlichkeit:** Jeder Begriff wird erklärt
**Konsistenz:** Glossar-Definitionen werden wörtlich übernommen

---

## Zwei Sprachniveaus

| | Leichte Sprache | Einfache Sprache |
|---|---|---|
| **Niveau** | A1/A2 | B1 |
| **Zielgruppe** | Kognitive Einschränkungen | Allgemeine Verständlichkeit |
| **Satzbau** | 1 Satz pro Zeile | Fließtext erlaubt |
| **Fachbegriffe** | Immer mit "Das heißt:" erklären | Beiläufig im Kontext erklären |
| **Nebensätze** | Verboten | Max. 1 pro Satz |
| **Output** | `_leichte_sprache.md` | `_einfache_sprache.md` |

---

## Schnellstart

### 1. Installation

```bash
git clone https://github.com/DEIN-USERNAME/easy-language-1.git
cd easy-language-1
```

**Windows (PowerShell):**
```powershell
.\scripts\setup.ps1
```

**Linux/Mac:**
```bash
chmod +x scripts/setup.sh && ./scripts/setup.sh
```

### 2. Quelldatei ablegen

```
input/mein-dokument.txt
```

### 3. Claude Code starten

```bash
claude
```

```
> Übersetze mein-dokument.txt in Leichte Sprache
```

### 4. Ergebnis

```
output/
├── mein-dokument_leichte_sprache.md
└── mein-dokument_leichte_sprache.docx
```

---

## Projektstruktur

```
easy-language-1/
├── CLAUDE.md                 # Hauptkonfiguration (Routing-Logik)
├── README.md                 # Diese Datei
│
├── directives/               # Übersetzungsregeln
│   ├── leichte-sprache.md    # A1/A2 mit Hybrid-Regel
│   └── einfache-sprache.md   # B1 für Business
│
├── scripts/                  # Setup & Tools
│   ├── setup.ps1             # Windows
│   ├── setup.sh              # Linux/Mac
│   └── convert.ps1           # MD → DOCX
│
├── docs/                     # Dokumentation
│   ├── vision.md             # Projektziele
│   └── architecture.md       # Technische Details
│
├── input/                    # Quelldateien (gitignored)
└── output/                   # Ergebnisse (gitignored)
```

---

## Beispiel: Vorher/Nachher

### Original (Juristendeutsch)
> Die personenbezogenen Daten werden gemäß Art. 6 Abs. 1 lit. a DSGVO ausschließlich zweckgebunden verarbeitet und nach Ablauf der gesetzlichen Aufbewahrungsfristen gelöscht.

### Leichte Sprache (A1/A2)
> Wir speichern Ihre **personenbezogenen Daten**.
> Das heißt:
> Informationen über Sie, zum Beispiel Ihr Name.
>
> Das steht in einem Gesetz.
> Das Gesetz heißt: **DSGVO**.
> Das heißt:
> Daten-Schutz-Grund-Verordnung.
>
> Wir benutzen die Daten nur für einen bestimmten Zweck.
> Danach löschen wir die Daten wieder.

### Einfache Sprache (B1)
> Wir verarbeiten Ihre personenbezogenen Daten (also Informationen wie Name und Adresse) nur für den vereinbarten Zweck. Das regelt die Datenschutz-Grundverordnung (DSGVO). Nach Ablauf der gesetzlichen Fristen löschen wir die Daten.

---

## QA-Log

Jede Übersetzung enthält automatisch einen Qualitäts-Anhang:

```markdown
---
### QA-Log (Automatisch generiert)

**Beibehaltene Fachbegriffe:**
- personenbezogene Daten, DSGVO, Aufbewahrungsfrist

**Aufgelöste Abkürzungen:**
- Abs. → Absatz
- lit. → Buchstabe

**Getrennte Komposita:**
- Daten-Schutz-Grund-Verordnung
- Aufbewahrungs-Frist
```

---

## Voraussetzungen

- [Claude Code](https://github.com/anthropics/claude-code)
- Python 3.8+
- Pandoc (wird automatisch installiert)

---

## Dokumentation

| Dokument | Inhalt |
|----------|--------|
| [Vision](docs/vision.md) | Projektziele & Prinzipien |
| [Architektur](docs/architecture.md) | Technische Details & Setup |
| [Leichte Sprache Direktive](directives/leichte-sprache.md) | Alle Regeln für A1/A2 |
| [Einfache Sprache Direktive](directives/einfache-sprache.md) | Alle Regeln für B1 |

---

## Roadmap

- [x] Leichte Sprache Direktive mit Hybrid-Regel
- [x] Einfache Sprache Direktive
- [x] QA-Log System
- [x] Word-Export (Pandoc)
- [x] Setup-Skripte (Windows/Linux/Mac)
- [ ] Glossar-Verwaltung
- [ ] Web-Interface
- [ ] API

---

## Beitragen

1. Fork erstellen
2. Feature-Branch: `git checkout -b feature/mein-feature`
3. Änderungen committen
4. Pull Request öffnen

---

## Lizenz

MIT License - siehe [LICENSE](LICENSE)

---

## Hinweis

Dieses Tool ist ein **Hilfsmittel**. Übersetzungen sollten von Fachleuten geprüft werden, besonders bei rechtlich relevanten Texten.

---

**Inspiriert von:** [Netzwerk Leichte Sprache](https://www.leichte-sprache.org/) | [Pandoc](https://pandoc.org/) | [Claude Code](https://github.com/anthropics/claude-code)
