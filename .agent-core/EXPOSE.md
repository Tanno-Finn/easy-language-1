# Easy Language Translation Engine · Exposé
Liegt als `.agent-core/EXPOSE.md` im Projekt. Aktualisiert: 2026-09-24

## Zweck
Proof of Concept, der Fachtexte (AGB, Sicherheit, Datenschutz) durch Claude-Code-Agenten in Leichte und Einfache Sprache vieler Sprachen übersetzt und dabei ein einfaches Dispatcher-Worker-Muster zeigt (README.md, docs/vision.md). Ausdrücklich kein Produkt; Erfolg ist, dass die Direktiven über 15+ Sprachen gleich tragen und parallele Worker die Queue sauber abarbeiten.

## Architektur
- Kein Build: Die Übersetzung macht der Agent nach Markdown-Direktiven in `directives/<sprachcode>/`; `CLAUDE.md` routet nach Eingabesprache.
- Je Sprache `normal-*`, `easy-*` (A1/A2) und `plain-*` (B1), englisch formuliert mit Beispielen in der Zielsprache (docs/architecture.md).
- Python-Scripts ohne Fremdbibliothek: `scripts/generate-jobs.py` erzeugt JSON-Jobs in drei Phasen, `scripts/queue_manager.py` verteilt sie per atomarem Umbenennen (pick, done, status, recover-zombies, retry_git).
- Hilfsscripts: `scripts/forensic-audit.py` und `scripts/export-config.py` bündeln Projektdateien, `scripts/generate-directive-reviews.py` erzeugt Review-Jobs für Direktiven.
- `scripts/convert.ps1` wandelt Markdown per pandoc in Word; `scripts/requirements.txt` nennt python-docx >=1.1.0, das kein Script importiert.
- Queue in `tickets/queue/` und Arbeitsausgabe `output/` sind gitignored (.gitignore); von den Ergebnissen ist nur `examples/output/` versioniert.

## Inhalte und Konzepte
- **Hybrid-Regel**: Fachbegriffe bleiben, fett, mit Anker-Phrase erklärt · export.md
- **Sprachstufen je Sprache**: normal, easy, plain je Sprache mit nationalem Standardnamen · docs/architecture.md
- **QA-Log**: Anhang jeder Übersetzung mit Fachbegriffen, Abkürzungen, Komposita · directives/de/leichte-sprache.md
- **English Shell**: Anweisungen englisch, Beispiele und Anker in der Zielsprache · docs/architecture.md
- **Sprach-Routing**: Sprache erkennen, Direktive wählen, nie ohne Direktive übersetzen · CLAUDE.md
- **Neue-Sprache-Protokoll**: vier Schritte zu eigenen Direktiven einer neuen Sprache, ohne Kopie · directives/new-language-protocol.md
- **Shakespeare-Stil**: Renaissance-Theatersprache für jede Sprache · directives/shakespearean.md
- **Datei-Job-Queue**: JSON-Jobs, Zustand im Dateinamen, Präfixe a/b/z · directives/queue-system.md
- **Worker-Loop**: pick, lesen, übersetzen, committen, done bis QUEUE_EMPTY · directives/worker-loop.md
- **Drei-Phasen-Pipeline**: A Übersetzung, B Vereinfachung, C Review, per depends_on verkettet · scripts/generate-jobs.py
- **Vier-Augen-Review**: zweiter Agent prüft jede Übersetzung · directives/review.md
- **Direktiven-Review**: forensische Prüfung der Direktiven selbst · directives/directive-review.md
- **Fiktiver Testkorpus**: drei erfundene Fachtexte, je eine Schwierigkeit · examples/README.md

## Ideen
- **Web-Oberfläche** für Nicht-Techniker (export.md, Nächste Schritte).
- **Übersetzungs-API** statt Datei-Ein- und Ausgabe (docs/vision.md, export.md).
- **Glossar-Verwaltung**, die der Glossar-Vorrang der Hybrid-Regel voraussetzt (export.md).
- Für einen Echtbetrieb nennt docs/vision.md außerdem Datenbank-Queue, Retries, Qualitätsmetriken und linguistische Prüfung.

## Bauen und Starten
- `python scripts/generate-jobs.py` legt die Jobs an, danach in mehreren Terminals „worker 1", „worker 2" an Claude Code (directives/worker-loop.md).
- `python scripts/queue_manager.py status` zeigt die Queue.
- `.\scripts\setup.ps1` installiert pandoc über Chocolatey, `.\scripts\convert.ps1` konvertiert nach Word.
- Zuletzt gelaufen: Worker-Commits vom 2026-01-23 (git log); seitdem nicht geprüft.

## Verwandte Projekte
Keine belegt.
