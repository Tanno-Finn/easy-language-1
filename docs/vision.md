# Vision: Leichte Sprache Übersetzungs-Workflow

## Was ist dieses Projekt?

Ein KI-gestützter Workflow zur **rechtssicheren Übersetzung** von Fachtexten in barrierefreie Sprache.

---

## Problem

Fachtexte (Verträge, Schulungen, Richtlinien) sind für viele Menschen schwer verständlich:
- Menschen mit Lernschwierigkeiten
- Menschen mit Deutsch als Zweitsprache
- Menschen mit Leseschwäche
- Menschen, die Informationen schnell erfassen müssen

Bestehende Lösungen haben Schwächen:
- **Manuelle Übersetzung:** Teuer, langsam, inkonsistent
- **Einfache KI-Übersetzung:** Verliert rechtliche Bedeutung, halluziniert, ignoriert Fachbegriffe

---

## Lösung

Ein strukturierter Workflow mit:

### 1. Zwei Sprachniveaus
| Niveau | Zielgruppe | Komplexität |
|--------|------------|-------------|
| **Leichte Sprache** (A1/A2) | Menschen mit kognitiven Einschränkungen | Sehr einfach, 1 Satz pro Zeile |
| **Einfache Sprache** (B1) | Allgemeine Verständlichkeit | Fließtext, aber klar strukturiert |

### 2. Rechtssicherheit durch Hybrid-Regel
- Fachbegriffe bleiben **erhalten** (nicht gelöscht oder ersetzt)
- Fachbegriffe werden **erklärt** (nicht nur vereinfacht)
- Glossar-Priorität: Vorgegebene Definitionen werden übernommen

### 3. Qualitätssicherung
- Automatisches QA-Log am Ende jeder Übersetzung
- Checklisten in den Direktiven
- Nachvollziehbare Dokumentation

---

## Zielgruppen

### Primäre Nutzer (des Workflows)
- Redakteure für barrierefreie Kommunikation
- HR-Abteilungen (Betriebsvereinbarungen, Schulungen)
- Compliance-Teams
- Öffentliche Einrichtungen

### Endnutzer (der übersetzten Texte)
- Menschen mit Lernschwierigkeiten
- Menschen mit geringer Lesekompetenz
- Menschen mit Deutsch als Zweitsprache
- Alle, die klare Kommunikation bevorzugen

---

## Kernprinzipien

### 1. Rechtliche Korrektheit vor Vereinfachung
Ein juristisch korrekter, aber komplexerer Text ist besser als ein vereinfachter Text mit falscher Bedeutung.

### 2. Glossar-Treue
Wenn Definitionen vorgegeben sind, werden diese wörtlich übernommen. Keine eigenen Interpretationen.

### 3. Transparenz
Jede Übersetzung dokumentiert, welche Fachbegriffe beibehalten und welche Abkürzungen aufgelöst wurden.

### 4. Reproduzierbarkeit
Gleiche Eingabe + gleiche Direktive = gleiches Ergebnis.

---

## Nicht-Ziele

- **Kein Ersatz für professionelle Prüfung:** Übersetzungen sollten von Fachleuten geprüft werden
- **Keine kreative Texterstellung:** Nur Übersetzung, keine Neuerfindung von Inhalten
- **Kein universelles Übersetzungstool:** Fokus auf Deutsch, Fachtexte, Barrierefreiheit

---

## Erfolgsmetriken

- [ ] Alle Fachbegriffe aus dem Glossar bleiben erhalten
- [ ] Keine rechtlichen Bedeutungsänderungen
- [ ] Lesbarkeit entspricht dem Zielniveau (A1/A2 oder B1)
- [ ] QA-Log vollständig und korrekt
- [ ] Übersetzung in < 5 Minuten pro Dokument

---

## Roadmap (Ideen)

### Phase 1: Grundfunktionalität (aktuell)
- [x] Leichte Sprache Direktive
- [x] Einfache Sprache Direktive
- [x] Routing-Logik
- [x] QA-Log

### Phase 2: Erweiterungen
- [ ] Word-Dokument Input/Output (pandoc)
- [ ] Batch-Verarbeitung mehrerer Dateien
- [ ] Glossar-Management (zentrale Begriffsdatenbank)

### Phase 3: Integration
- [ ] Web-Interface
- [ ] API für externe Systeme
- [ ] Versionierung von Übersetzungen
