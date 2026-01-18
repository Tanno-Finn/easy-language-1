# Worker Loop Directive [M]

Du bist ein autonomer Worker-Agent. Dein Auftrag: Jobs aus der Queue holen und abarbeiten.

---

## Quick Start [M]

Wenn der User "worker" oder "worker X" sagt:
1. Du bist Worker (Auto-ID oder X)
2. Lies diese Direktive
3. Starte den Loop

---

## Der Loop [M]

**Endlosschleife bis Queue leer!**

```
WIEDERHOLE:
  1. pick  → Job holen
  2. read  → Direktive lesen
  3. do    → Job ausführen
  4. commit → Änderungen committen
  5. done  → Job abschließen
  → ZURÜCK ZU 1
```

### 1. Job holen [M]

```bash
python scripts/queue_manager.py pick
# oder mit manueller ID:
python scripts/queue_manager.py pick --worker W3
```

**Mögliche Outputs:**
- `QUEUE_EMPTY` → Fertig! Abschiedsnachricht ausgeben.
- `NO_MORE_JOBS` → Fertig! Keine Jobs mehr für dich.
- JSON → Das ist dein Job. Weiter zu Schritt 2.

### 2. Job verstehen [M]

Das JSON enthält:
```json
{
  "type": "translation-job",
  "source_file": "input/datei.md",
  "target_format": "leichte-sprache",
  "directive": "directives/de/leichte-sprache.md",
  "job_title": "Übersetze datei.md in Leichte Sprache"
}
```

### 3. Job ausführen [M]

1. **Lies die Direktive** (`directive` Feld)
2. **Lies die Quelldatei** (`source_file` Feld)
3. **Übersetze gemäß Direktive**
4. **Speichere nach `output/`**

**KRITISCH:**
- NIEMALS ohne Queue-Job arbeiten [M]
- IMMER Quelldatei lesen, nie aus Gedächtnis [M]
- NIEMALS Fakten halluzinieren [M]

### 4. Commit [M]

```bash
git add output/[deine-datei]
git commit -m "feat(translate): [Job-Titel] - Worker X

Job: [source_file]
Worker: X"
```

**Regeln:**
- Nur DEINE Dateien committen
- NIEMALS `git add -A`
- Job-Referenz im Commit pflicht

### 5. Job abschließen [M]

```bash
python scripts/queue_manager.py done [job_filename]
```

### 6. Loop fortsetzen [M]

**SOFORT zurück zu Schritt 1!**

Du hörst NUR auf wenn:
- `QUEUE_EMPTY` kommt
- `NO_MORE_JOBS` kommt

---

## Abschiedsnachricht [M]

```
═══════════════════════════════════════
WORKER [ID] FINISHED
───────────────────────────────────────
Jobs completed: [ANZAHL]
Status: Queue empty
═══════════════════════════════════════
```

---

## Commands Quick Reference

```bash
# Status anzeigen
python scripts/queue_manager.py status

# Nächsten Job holen
python scripts/queue_manager.py pick

# Job als erledigt markieren
python scripts/queue_manager.py done [filename]

# Zombie-Jobs wiederherstellen
python scripts/queue_manager.py recover-zombies
```

---

## Fehlerbehandlung [M]

**Job fehlgeschlagen:**
- Dokumentiere den Fehler
- Markiere Job als done mit FAILED-Hinweis
- Hole nächsten Job

**Git Lock:**
```bash
python scripts/queue_manager.py retry_git "git add ..."
```

---

## Anti-Patterns [M]

```
VERBOTEN:
- Selbstständig entscheiden "ich übersetze jetzt X"
- Arbeit aus dem Gedächtnis machen
- Bei QUEUE_EMPTY improvisieren
- Mehrere Jobs batchen

PFLICHT:
- Immer erst `pick` ausführen
- Quelldatei vor Übersetzung lesen
- Ein Job = Ein Commit
```
