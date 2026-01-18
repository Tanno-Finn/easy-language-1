#!/usr/bin/env python3
"""
Directive Quality Review Dispatcher

Generates review jobs for all language directives to ensure
consistency and quality across the entire directive library.
"""

import json
from pathlib import Path

QUEUE_DIR = Path("tickets/queue")
DIRECTIVES_DIR = Path("directives")
REVIEW_DIRECTIVE = "directives/directive-review.md"

# All language directives to review
DIRECTIVES_TO_REVIEW = {
    # Tier 1
    "de": ["leichte-sprache.md", "einfache-sprache.md"],
    "en": ["easy-read.md", "plain-english.md"],
    "es": ["lectura-facil.md", "lenguaje-claro.md"],
    "fr": ["falc.md", "langage-clair.md"],
    "it": ["linguaggio-facile.md", "linguaggio-chiaro.md"],
    "nl": ["makkelijk-lezen.md", "klare-taal.md"],
    "ja": ["yasashii-nihongo.md", "plain-japanese.md"],
    # Tier 2
    "pt": ["leitura-facil.md", "linguagem-clara.md"],
    "pl": ["tekst-latwy.md", "jezyk-prosty.md"],
    "ru": ["yasniy-yazyk.md", "prostoy-yazyk.md"],
    "sv": ["lattlast.md", "klarsprack.md"],
    "zh": ["easy-read.md", "plain-language.md"],
    "ko": ["easy-korean.md", "plain-korean.md"],
    "ar": ["easy-arabic.md", "plain-arabic.md"],
    "cs": ["srozumitelne-cteni.md", "plain-czech.md"],
}

def main():
    if not QUEUE_DIR.exists():
        QUEUE_DIR.mkdir(parents=True)

    existing_jobs = [f.name for f in QUEUE_DIR.glob("*.json")]
    created_count = 0

    print("--- DIRECTIVE QUALITY REVIEW DISPATCHER ---")
    print(f"Review directive: {REVIEW_DIRECTIVE}")
    print()

    for lang, files in DIRECTIVES_TO_REVIEW.items():
        for filename in files:
            directive_path = f"directives/{lang}/{filename}"

            # Check if directive exists
            if not Path(directive_path).exists():
                print(f"  WARNING: {directive_path} not found, skipping")
                continue

            # Generate deterministic job name
            job_name = f"job_d_directive_review_{lang}_{filename.replace('.md', '')}.json"

            # Skip if already exists
            if job_name in existing_jobs:
                print(f"  SKIP: {job_name} (already exists)")
                continue

            job = {
                "type": "directive_review",
                "directive_to_review": directive_path,
                "review_directive": REVIEW_DIRECTIVE,
                "language": lang,
                "output_file": f"directives/{lang}/{filename}_REVIEW.md"
            }

            with open(QUEUE_DIR / job_name, "w", encoding="utf-8") as f:
                json.dump(job, f, indent=2)

            created_count += 1
            print(f"  CREATED: {job_name}")

    print()
    print(f"DONE. Created {created_count} directive review jobs.")
    print(f"Total directives to review: {sum(len(v) for v in DIRECTIVES_TO_REVIEW.values())}")

if __name__ == "__main__":
    main()
