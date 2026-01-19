# Easy Language Translation Engine

A simple proof-of-concept for translating texts into Easy Language formats across multiple languages. This project showcases a basic dispatcher-worker pattern for parallel job processing.

---

## What This Is

A small showcase exploring:
- How to structure translation directives for different languages
- A simple file-based job queue (JSON files + atomic rename)
- The "English Shell" pattern (English instructions, native content)

**Not production-ready.** Just a showcase.

---

## Supported Languages

| Code | Language | Easy Read | Plain Language |
|------|----------|-----------|----------------|
| DE | German | Leichte Sprache | Einfache Sprache |
| EN | English | Easy Read | Plain English |
| ES | Spanish | Lectura Fácil | Lenguaje Claro |
| FR | French | FALC | Langage Clair |
| IT | Italian | Linguaggio Facile | Linguaggio Chiaro |
| NL | Dutch | Makkelijk Lezen | Klare Taal |
| JA | Japanese | Yasashii Nihongo | Plain Japanese |
| PT | Portuguese | Leitura Fácil | Linguagem Clara |
| PL | Polish | Tekst Łatwy | Język Prosty |
| RU | Russian | Yasniy Yazyk | Prostoy Yazyk |
| SV | Swedish | Lättläst | Klarspråk |
| ZH | Chinese | Easy Read | Plain Language |
| KO | Korean | Easy Korean | Plain Korean |
| AR | Arabic | Easy Arabic | Plain Arabic |
| CS | Czech | Srozumitelné Čtení | Plain Czech |

---

## How It Works

```bash
# Generate jobs
python scripts/generate-jobs.py

# Process jobs (run in multiple terminals for parallelism)
python scripts/queue_manager.py pick
```

Output goes to `examples/output/`.

---

## Project Structure

```
directives/     # Translation rules per language
scripts/        # Job generator + queue manager
tickets/queue/  # JSON job files
examples/       # Input/output files
docs/           # Notes
```

## License

MIT
