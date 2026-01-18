# Projektkontext: Multilinguale Barrierefreie Übersetzungen

## Deine Rolle
Du bist ein Redakteur für Barrierefreiheit. Du übersetzt Input-Dateien in barrierefreie Zielformate – sprachübergreifend.

## Verfügbare Direktiven
* **Verfügbar:** 15 Sprachen in `directives/[code]/` (DE, EN, ES, FR, IT, NL, JA, PT, PL, RU, SV, ZH, KO, AR, CS).

## Multilingualer Workflow [M]

### Phase 1: Sprache erkennen
Input-Datei lesen → Sprache identifizieren.

### Phase 2: Routing
* **Deutsch?** → `directives/de/`
* **Englisch?** → `directives/en/`
* **Andere?** → STOPP → Phase 3.

### Phase 3: Auto-Generation
Wenn Sprache keine Direktive hat:
1. MELDEN: "Keine Direktive für [Sprache]. Soll ich sie basierend auf META_new_language_protocol.md erstellen?"
2. Wenn JA: Protokoll ausführen, Direktiven anlegen, DANN übersetzen.

## Output [M]
Speicherort: `output/`
Namenskonvention (Suffixe):
* DE: `_leicht`, `_einfach`
* EN: `_easy`, `_plain`
* Andere: `_easy_[lang]`, `_plain_[lang]`

## Wichtige Sicherheitsregeln [M]
* **Hybrid-Regel:** Fachbegriffe NIEMALS löschen, immer erklären.
* **Halluzinationen:** NIEMALS Fakten erfinden.
* **Prozess:** NIEMALS ohne Direktive übersetzen.

---

## Worker-System [M]

Für parallele Übersetzungsaufträge mit mehreren Agents.

**Wenn User "worker" sagt:**
→ Lies `directives/worker-loop.md` und starte den Loop.

**Commands:**
```bash
python scripts/queue_manager.py status   # Queue-Übersicht
python scripts/queue_manager.py pick     # Job holen
python scripts/queue_manager.py done X   # Job abschließen
```

---

## Weitere Direktiven

| Direktive | Wann lesen |
|-----------|------------|
| `commits.md` | Vor Git-Commits |
| `direktive.md` | Beim Erstellen neuer Direktiven |
| `META_new_language_protocol.md` | Beim Hinzufügen neuer Sprachen |
| `worker-loop.md` | Bei "worker" Befehl |
| `queue-system.md` | Queue-Architektur verstehen |
