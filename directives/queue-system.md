# Queue System [M]

Multi-Agent Job-Queue für parallele Übersetzungsaufträge.

---

## Verzeichnisstruktur

```
tickets/
├── queue/                    # Aktive Job-Queue
│   ├── job_a_*.json         # Sequentielle Jobs (zuerst)
│   ├── job_b_*.json         # Parallele Jobs (Standard)
│   └── job_z_*.json         # Finalizer (wartet auf andere)
└── done/                    # Archiv (gitignored)
```

---

## Job-Prefixe [M]

| Prefix | Verhalten | Verwendung |
|--------|-----------|------------|
| `job_a_*` | Wird zuerst gepickt | Setup-Jobs |
| `job_b_*` | Parallel | **Standard** |
| `job_z_*` | Wartet bis alle fertig | Validierung |

---

## Worker-ID Tracking [M]

Jeder Job wird mit Worker-ID versehen:

```
Pending:      job27.json
In Progress:  job27_W3_IN_PROGRESS.json
Done:         job27_W3_DONE.json
```

---

## Queue Manager Commands

```bash
# Status anzeigen
python scripts/queue_manager.py status

# Nächsten Job holen (Auto-ID)
python scripts/queue_manager.py pick

# Nächsten Job holen (manuelle ID)
python scripts/queue_manager.py pick --worker W3

# Job als erledigt markieren
python scripts/queue_manager.py done [filename]

# Zombie-Jobs wiederherstellen
python scripts/queue_manager.py recover-zombies

# Git mit Retry
python scripts/queue_manager.py retry_git "git pull"
```

---

## Job erstellen (manuell)

Jobs werden als JSON-Dateien in `tickets/queue/` erstellt:

```json
{
  "type": "translation-job",
  "source_file": "input/dokument.md",
  "target_format": "leichte-sprache",
  "directive": "directives/de/leichte-sprache.md",
  "job_title": "Übersetze dokument.md in Leichte Sprache"
}
```

**Dateiname:** `job_b_YYYYMMDD_HHMMSS_beschreibung.json`

---

## Zombie Recovery [M]

**Zombie-Jobs:** IN_PROGRESS Jobs deren Worker abgestürzt ist.

```bash
# Alle verwaisten Jobs zurücksetzen
python scripts/queue_manager.py recover-zombies
```

Der neue Worker prüft:
1. Hat Original-Worker bereits Commits gemacht?
2. Falls ja: Nur `done` aufrufen
3. Falls nein: Job normal bearbeiten

---

## Git Safety [M]

Mehrere Worker auf demselben Repo:

1. **Nur eigene Änderungen committen**
2. **Spezifisches `git add file`** statt `git add -A`
3. **retry_git nutzen** bei Lock-Problemen

---

## Workflow Beispiel

```
User: "Bitte übersetze alle Dateien in input/leicht/"

Dispatcher-Agent:
  → Erstellt job_b_*.json für jede Datei
  → Erstellt job_z_finalizer.json für Validierung

User: "worker 1" (in Terminal 1)
User: "worker 2" (in Terminal 2)

Worker 1 & 2:
  → pick → Job holen
  → Übersetzen
  → Commit
  → done
  → Nächster Job...
  → QUEUE_EMPTY → Fertig!
```

---

## Anti-Patterns [M]

- Jobs ohne Queue arbeiten
- `git add -A` verwenden
- DONE Jobs löschen (statt archivieren)
- Mehrere Jobs in einem Commit
