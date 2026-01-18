# Easy Language Translation Engine 🌍

Ein KI-gestütztes Multi-Agenten-System zur **rechtssicheren Übersetzung** von Fachtexten in Barrierefreie Sprache.

**Status:** Production Ready ✅
**Supported Languages:** 🇩🇪 DE, 🇬🇧 EN, 🇪🇸 ES, 🇫🇷 FR, 🇮🇹 IT, 🇳🇱 NL, 🇯🇵 JA

---

## 🚀 Features

- **Hybrid-Regel:** Fachbegriffe werden erkannt, **beibehalten** und automatisch erklärt (Glossar-Treue).
- **Multi-Agent Queue:** Skalierbare Worker-Architektur für parallele Verarbeitung.
- **Auto-Review:** 4-Augen-Prinzip (Übersetzer-Agent + Reviewer-Agent).
- **Audit-Trail:** Jede Datei enthält ein QA-Log über veränderte Begriffe.
- **Universal:** Funktioniert für Verträge, Anleitungen, Richtlinien.

---

## 🛠 Installation

```bash
# 1. Clone Repo
git clone https://github.com/Tanno-Finn/easy-language-1.git

# 2. Setup (Python dependencies)
pip install -r scripts/requirements.txt
```

## ⚡ Quick Start (Worker System)

Das System nutzt eine Datei-basierte Queue.

**1. Jobs erstellen (Dispatcher)**

```bash
python scripts/generate-jobs.py
# Generiert Übersetzungs- und Review-Jobs für alle Sprachen
```

**2. Worker starten**
Öffne beliebig viele Terminals und starte in jedem:

```bash
python scripts/queue_manager.py pick
# Oder im Claude Code Chat einfach: "worker"
```

**3. Ergebnis**
Die fertigen Dateien landen in `examples/output/` (Translation + Review Report).

---

## 📂 Architektur

* `directives/` - Das Gehirn. Enthält die Sprachregeln (English Shell, Native Content).
* `tickets/queue/` - Der Posteingang für die Worker.
* `scripts/` - Die Logik (Queue Manager, Job Generator).
* `examples/` - Demo-Input und generierter Output.

## 🛡 License

MIT License. See LICENSE file.
