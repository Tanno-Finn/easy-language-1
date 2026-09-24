# Easy Language Translation Engine · Status
Liegt als `.agent-core/STATUS.md` im Projekt. Aktualisiert: 2026-09-24

## Ziel
Showcase zeigen, dass parallele Agenten Fachtexte per Direktiven in Leichte und Einfache Sprache vieler Sprachen übersetzen; fertig, wenn jede Sprache mit Direktiven auch im Job-Generator steht und durchläuft.

## Stand (2026-01-23, ruht seitdem)
- 15 Sprachen im Job-Generator `scripts/generate-jobs.py`, Beispielausgaben in `examples/output/` (140 Dateien).
- Shakespeare-Stil als Spezialdirektive ergänzt, drei deutsche Beispiele erzeugt; Arbeitsausgabe seit 097cad3 nach `output/` (gitignored).
- offen: 8 Sprachen (bn, el, hi, id, th, tr, uk, vi) haben Direktiven und Reviews, fehlen aber in der LANGUAGES-Registry, README und CLAUDE.md.

## Nächster Schritt
`scripts/generate-jobs.py`: die 8 Sprachen in LANGUAGES eintragen, dann `python scripts/generate-jobs.py` und README-Tabelle nachziehen.

## Entscheidungen
- keine E-Einträge im Repo; Output-Ordner für Arbeitsläufe auf `output/` umgestellt (097cad3, 2026-01-23).

## Zustand woanders
master @ b0caff8 · Queue in `tickets/queue/` (gitignored, leer im Repo) · Beispiele `examples/output/` · keine Tickets

## Fallen
CLAUDE.md und worker-loop.md schreiben nach `output/`, generate-jobs.py und README nach `examples/output/`, und export.md ist auf dem 7-Sprachen-Stand von 2026-01-18.
