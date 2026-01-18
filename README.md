# Easy Language Translation Engine 🌍

Ein Enterprise-Grade Multi-Agenten-System zur **rechtssicheren Übersetzung** und **Qualitätssicherung** von Fachtexten in 15 Sprachen.

**Status:** Production Ready (v1.1) ✅
**Architecture:** Decoupled Dispatcher-Worker Pattern

---

## 🌐 Supported Languages (Tier 1 & Tier 2)

| Tier | Sprachen | Status |
|------|----------|--------|
| **Core (Tier 1)** | 🇩🇪 DE, 🇬🇧 EN, 🇪🇸 ES, 🇫🇷 FR, 🇮🇹 IT, 🇳🇱 NL, 🇯🇵 JA | **Active** |
| **Expansion (Tier 2)** | 🇵🇹 PT, 🇵🇱 PL, 🇷🇺 RU, 🇸🇪 SV, 🇨🇳 ZH, 🇰🇷 KO, 🇸🇦 AR, 🇨🇿 CS | **Active** |

---

## 🚀 Key Features

- **Hybrid-Regel:** Fachbegriffe werden erkannt, beibehalten und erklärt.
- **English Shell Pattern:** Alle Direktiven nutzen englische Logik-Anweisungen für maximale Konsistenz.
- **Auto-Review (4-Augen-Prinzip):** Jeder Übersetzung folgt automatisch ein Review-Job durch einen zweiten Agenten.
- **Idempotenter Dispatcher:** Generiert nur fehlende Jobs, verhindert Duplikate.
- **Atomic Queue:** Race-Condition-freies File-Locking für beliebig viele parallele Worker.

---

## 🛠 Quick Start

**1. Jobs generieren (Dispatcher)**
```bash
python scripts/generate-jobs.py
# Erstellt Übersetzungs- (Phase B) und Review-Jobs (Phase C) für alle 15 Sprachen
```

**2. Worker starten (Parallel Processing)**
Öffne beliebig viele Terminals:

```bash
python scripts/queue_manager.py pick
# Oder im Chat: "worker"
```

**3. Output**
Ergebnisse landen in `examples/output/` (inklusive `_REVIEW.md` Reports).

---

## 📂 Project Structure

* `directives/` - Das "Gesetzbuch" (Regeln für 15 Sprachen).
* `scripts/` - Die "Maschine" (Queue Manager, Generator).
* `tickets/queue/` - Der "Arbeitsspeicher" (JSON Jobs).
* `docs/` - Detaillierte Architektur-Dokumentation.

## 🛡 License

MIT License.
