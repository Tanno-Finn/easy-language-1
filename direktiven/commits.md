# Git Commit Guidelines

## Purpose [M]
Definiert einheitliche Standards für Git-Commits in diesem Projekt.

## When to Use [M]
- Bei jedem Commit in diesem Repository [M]
- Vor dem Erstellen von Pull Requests

## Key Requirements [M]

### Commit Message Format [M]
Verwende Conventional Commits:
- `feat:` - Neue Features
- `fix:` - Bug-Fixes
- `refactor:` - Code-Refactoring
- `docs:` - Dokumentations-Updates
- `chore:` - Wartungsaufgaben

### AI-Attribution [M]
**WICHTIG**: Keine AI-Attribution in Commits:
- **NICHT** "Generated with Claude Code" hinzufugen
- **NICHT** "Co-Authored-By: Claude" verwenden
- Commits sollen wie vom menschlichen Entwickler geschrieben wirken [M]

### Best Practices [C]
- Kleine, fokussierte Commits erstellen
- Beschreibende Commit-Messages die erklaren WAS und WARUM
- Einen "testbaren Zustand" vor dem Commit erreichen
- Bei komplexen Anderungen Bullet-Points verwenden

## Anti-Patterns [M]
- Riesige Commits mit vielen unzusammenhangenden Anderungen [M]
- Nichtssagende Messages wie "fix" oder "update" [M]
- AI-Attribution hinzufugen [M]

## Success Criteria [M]
- Commit-Message folgt Conventional Commits Format [M]
- Anderungen sind nachvollziehbar beschrieben [M]
- Keine AI-Attribution vorhanden [M]
