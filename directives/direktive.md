# Directive Management

## Purpose [M]
Definiert den systematischen Prozess zum Erstellen, Aktualisieren und Pflegen von Direktiven in diesem Projekt.

## When to Use [M]
- Vor dem Erstellen einer neuen Direktive [M]
- Beim Aktualisieren bestehender Direktiven
- Bei der Qualitätssicherung des Direktiven-Systems

## Key Requirements [M]

### Pflicht-Elemente einer Direktive [M]
Jede Direktive MUSS enthalten:
- **Purpose [M] Section** - Klare Aussage zum Zweck [M]
- **When to Use [M] Section** - Wann wird diese Direktive angewendet [M]
- **Key Requirements [M] Section** - Pflichtanforderungen mit [M] Markern [M]
- **Anti-Patterns Section** - Was NICHT zu tun ist [M]
- **Success Criteria Section** - Wann ist die Aufgabe erfolgreich [M]

### Marker-System [M]
- **[M] = Mandatory** - Vom User festgelegte Pflichtanforderungen [M]
  - Nur User kann [M] Marker hinzufugen/entfernen
  - Claude darf [M] Marker NIEMALS eigenmachtig andern
- **[C] = Claude-Created** - Von Claude empfohlene Best Practices [C]
  - Claude kann [C] Marker bei Verbesserungen anpassen

### Dateistruktur [C]
- Speicherort: `/directives/[name].md`
- Naming: kebab-case (lowercase with hyphens, e.g., `easy-read.md`, `commits.md`)
- Referenz in CLAUDE.md hinzufügen

## Anti-Patterns [M]
- Direktiven ohne [M] Marker fur Pflichtanforderungen erstellen [M]
- Direktiven ohne CLAUDE.md Integration anlegen [M]
- Unfokussierte Direktiven die mehrere Themen vermischen [M]
- [M] Marker fur Claude-Empfehlungen verwenden [M]

## Success Criteria [M]
- Alle Pflicht-Sections vorhanden [M]
- Direktive in CLAUDE.md referenziert [M]
- Klare, ausfuhrbare Anweisungen [M]
- Anti-Patterns dokumentiert [M]
