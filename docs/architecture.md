# Architecture: Global Translation Engine

## System Overview

Das System folgt einer **asynchronen Multi-Agenten-Architektur**. Es gibt keine zentrale Steuerung während der Laufzeit; die Logik liegt in der Queue.

```
[Input Files] ──▶ [Dispatcher Script]
                          │
                          ▼
                  [Job Queue (JSON)] ◀───┐
                          │              │
        ┌─────────────────┼──────────────┼─────────────────┐
        ▼                 ▼              ▼                 ▼
   [Worker 1]        [Worker 2]     [Worker 3]        [Worker N]
        │                 │              │                 │
        └───────┬─────────┴──────────────┴─────────┬───────┘
                │                                  │
                ▼                                  ▼
      [Output: Translation]               [Output: Review Report]
```

## Core Components

### 1. The Directives ("English Shell")

Wir nutzen das **English Shell / Native Content** Pattern.

* Die Anweisung an die KI ist immer Englisch (z.B. "Use the anchor phrase:").
* Der Inhalt ist in der Zielsprache (z.B. "Das heißt:").

Dies verhindert Logik-Fehler bei Sprachen, die das Modell schlechter beherrscht.

### 2. The Queue System

* **Path:** `tickets/queue/`
* **Locking:** Atomic Rename (`os.rename`).
* **Phases:**
  * `job_b_*`: Translation (Muss zuerst erfolgen).
  * `job_c_*`: Review (Wartet, bis Translation existiert).

### 3. The Dispatcher (`generate-jobs.py`)

* **Idempotenz:** Prüft vor Erstellung, ob ein Job schon existiert.
* **Scope:** Unterstützt alle 15 Sprachen (Tier 1 + Tier 2).
* **Quality:** Erstellt automatisch den passenden Review-Job für jede Übersetzung.

## Language Support Details

### Special Handlers

* **RTL (Right-To-Left):** Arabisch (`ar`) nutzt spezifische Prompting-Regeln für Layout.
* **High Context:** Japanisch (`ja`), Chinesisch (`zh`), Koreanisch (`ko`) nutzen strikte "Hybrid Rules" für Schriftzeichen (Kanji/Hanja).
* **Complex Grammar:** Polnisch (`pl`), Russisch (`ru`), Tschechisch (`cs`) nutzen vereinfachte SVO-Strukturen zur Vermeidung von Kasus-Fehlern.
