#!/usr/bin/env python3
"""
Global Job Dispatcher - 3-Phase Translation Pipeline

Phase A: Standard Translation (German → Target Language)
Phase B: Easy Language Conversion (Standard → Easy/Plain)
Phase C: Review (Quality Check)
"""
import os, json
from pathlib import Path

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

    print("--- GLOBAL DISPATCHER (15 LANGUAGES, 3-PHASE PIPELINE) ---")

    for filename in INPUT_FILES:
        base_name = filename.split(".")[0]

        for lang, directives in LANGUAGES.items():
            # --- JOB A (STANDARD TRANSLATION) ---
            # German input → Standard translation in target language
            # Skip for German (no translation needed)
            if lang != "de":
                a_filename = f"job_a_translate_{lang}_{base_name}.json"
                standard_output = f"examples/output/{base_name}_{lang}_standard.txt"

                if a_filename not in existing_jobs:
                    job_a = {
                        "type": "standard_translation",
                        "source_file": f"examples/input/{filename}",
                        "source_lang": "de",
                        "target_lang": lang,
                        "output_file": standard_output
                    }
                    with open(QUEUE_DIR / a_filename, "w", encoding="utf-8") as f:
                        json.dump(job_a, f, indent=2)
                    created_count += 1
            else:
                # For German, the input IS the standard file
                standard_output = f"examples/input/{filename}"

            for mode in MODES:
                job_name_base = f"{lang}_{mode}_{base_name}"

                # --- JOB B (EASY LANGUAGE CONVERSION) ---
                # Standard translation → Easy/Plain format
                b_filename = f"job_b_convert_{job_name_base}.json"

                if b_filename not in existing_jobs:
                    # For German, use original input; for others, use standard translation
                    if lang == "de":
                        source_for_conversion = f"examples/input/{filename}"
                    else:
                        source_for_conversion = f"examples/output/{base_name}_{lang}_standard.txt"

                    job_b = {
                        "type": "easy_conversion",
                        "source_file": source_for_conversion,
                        "target_lang": lang,
                        "mode": mode,
                        "directive": directives[mode],
                        "output_file": f"examples/output/{base_name}_{lang}_{mode}.txt",
                        "depends_on": f"job_a_translate_{lang}_{base_name}" if lang != "de" else None
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
                        "output_file": f"examples/output/{base_name}_{lang}_{mode}_REVIEW.md",
                        "depends_on": f"job_b_convert_{job_name_base}"
                    }
                    with open(QUEUE_DIR / c_filename, "w", encoding="utf-8") as f:
                        json.dump(job_c, f, indent=2)
                    created_count += 1

    print(f"DONE. Created {created_count} new jobs.")
    print(f"Pipeline: Phase A (Standard Translation) → Phase B (Easy Conversion) → Phase C (Review)")
    print(f"Total Coverage: {len(LANGUAGES)} languages x {len(INPUT_FILES)} files")

if __name__ == "__main__":
    main()
