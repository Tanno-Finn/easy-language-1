#!/usr/bin/env python3
import os, json
from pathlib import Path
from datetime import datetime

QUEUE_DIR = Path("tickets/queue")

# COMPLETE LANGUAGE REGISTRY
LANGUAGES = {
    "de": { "easy": "directives/de/leichte-sprache.md", "plain": "directives/de/einfache-sprache.md" },
    "en": { "easy": "directives/en/easy-read.md",       "plain": "directives/en/plain-english.md" },
    "es": { "easy": "directives/es/lectura-facil.md",   "plain": "directives/es/lenguaje-claro.md" },
    "fr": { "easy": "directives/fr/falc.md",            "plain": "directives/fr/langage-clair.md" },
    "it": { "easy": "directives/it/linguaggio-facile.md","plain": "directives/it/linguaggio-chiaro.md" },
    "nl": { "easy": "directives/nl/makkelijk-lezen.md", "plain": "directives/nl/klare-taal.md" },
    "ja": { "easy": "directives/ja/yasashii-nihongo.md","plain": "directives/ja/plain-japanese.md" },
    # TIER 2
    "pt": { "easy": "directives/pt/leitura-facil.md",   "plain": "directives/pt/linguagem-clara.md" },
    "pl": { "easy": "directives/pl/tekst-latwy.md",     "plain": "directives/pl/jezyk-prosty.md" },
    "ru": { "easy": "directives/ru/yasniy-yazyk.md",    "plain": "directives/ru/prostoy-yazyk.md" },
    "sv": { "easy": "directives/sv/lattlast.md",        "plain": "directives/sv/klarsprack.md" },
    "zh": { "easy": "directives/zh/easy-read.md",       "plain": "directives/zh/plain-language.md" },
    "ko": { "easy": "directives/ko/easy-korean.md",     "plain": "directives/ko/plain-korean.md" },
    "ar": { "easy": "directives/ar/easy-arabic.md",     "plain": "directives/ar/plain-arabic.md" },
    "cs": { "easy": "directives/cs/srozumitelne-cteni.md","plain": "directives/cs/plain-czech.md" }
}

MODES = ["easy", "plain"]
INPUT_FILES = ["agb_zeitreise.txt", "datenschutz_telepathie.txt", "sicherheit_orbitalstation.txt"]

def main():
    if not QUEUE_DIR.exists(): QUEUE_DIR.mkdir(parents=True)

    existing_jobs = [f.name for f in QUEUE_DIR.glob("*.json")]
    created_count = 0

    print("--- GLOBAL DISPATCHER (15 LANGUAGES) ---")

    for filename in INPUT_FILES:
        base_name = filename.split(".")[0]

        for lang, directives in LANGUAGES.items():
            for mode in MODES:
                # ID Generation
                # Wir nutzen deterministische Namen, um Duplikate zu vermeiden
                job_name_base = f"{lang}_{mode}_{base_name}"

                # --- JOB B (TRANSLATION) ---
                b_filename = f"job_b_trans_{job_name_base}.json"

                # Check duplication (skip if ANY job with this base exists, strictly speaking we check filename)
                # Aber wir wollen sichergehen, dass wir auch 'done' jobs nicht neu machen.
                # Hier: simpler Check im Queue Ordner.
                if b_filename not in existing_jobs:
                    job_b = {
                        "type": "translation",
                        "source_file": f"examples/input/{filename}",
                        "target_lang": lang,
                        "mode": mode,
                        "directive": directives[mode],
                        "output_file": f"examples/output/{base_name}_{lang}_{mode}.txt"
                    }
                    with open(QUEUE_DIR / b_filename, "w", encoding="utf-8") as f:
                        json.dump(job_b, f, indent=2)
                    created_count += 1

                # --- JOB C (REVIEW) ---
                c_filename = f"job_c_review_{job_name_base}.json"
                if c_filename not in existing_jobs:
                    job_c = {
                        "type": "review",
                        "target_file_to_review": f"examples/output/{base_name}_{lang}_{mode}.txt",
                        "directive": "directives/review.md",
                        "output_file": f"examples/output/{base_name}_{lang}_{mode}_REVIEW.md"
                    }
                    with open(QUEUE_DIR / c_filename, "w", encoding="utf-8") as f:
                        json.dump(job_c, f, indent=2)
                    created_count += 1

    print(f"DONE. Created {created_count} new jobs.")
    print(f"Total Coverage: {len(LANGUAGES)} languages x {len(INPUT_FILES)} files x 2 modes x 2 phases")

if __name__ == "__main__":
    main()
