# Architecture Notes

## Overview

Simple dispatcher-worker pattern using file-based job queue.

```
[Input] → [Dispatcher] → [Queue (JSON files)] → [Workers] → [Output]
```

Nothing fancy. Workers pick jobs via atomic file rename to avoid race conditions.

## Job Types

| Phase | Prefix | What it does |
|-------|--------|--------------|
| B | `job_b_*` | Translate text to Easy/Plain language |
| C | `job_c_*` | Review the translation |

## The "English Shell" Pattern

Instructions in English, content in target language. Example:

```
Use the anchor phrase: "Das heißt:"
```

This helps with consistency across languages.

## Directive Structure

Each language has:
- `easy-*.md` - Easy Read rules (A1/A2 level)
- `plain-*.md` - Plain Language rules (B1 level)

Some are based on real standards (DE, FR, ES, SV, JA), others are adaptations.

## Queue Mechanics

- Jobs live in `tickets/queue/`
- Worker picks job → renames to `*_WORKING.json`
- Worker finishes → renames to `*_DONE.json`
- Simple, no database needed

## Limitations

- No real dependency management between jobs
- No retry logic
- No monitoring
- File-based = doesn't scale

It's a POC, not production code.
