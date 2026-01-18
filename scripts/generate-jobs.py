#!/usr/bin/env python3
import os, json, shutil
from pathlib import Path
from datetime import datetime

QUEUE_DIR = Path("tickets/queue")
LANGUAGES = ["de", "en", "es", "fr", "it", "nl", "ja"]
MODES = ["easy", "plain"]
INPUT_FILES = ["agb_zeitreise.txt", "datenschutz_telepathie.txt", "sicherheit_orbitalstation.txt"]

def main():
    # 1. Clean Slate (Alte Queue löschen für sauberen Neustart)
    if QUEUE_DIR.exists():
        for f in QUEUE_DIR.glob("*.json"):
            f.unlink()
    else:
        QUEUE_DIR.mkdir(parents=True, exist_ok=True)

    job_counter = 0

    print("--- GENERATING JOBS ---")

    for filename in INPUT_FILES:
        base_name = filename.split(".")[0]

        for lang in LANGUAGES:
            for mode in MODES:
                # --- PHASE B: TRANSLATION JOB ---
                job_counter += 1
                b_id = f"job_b_{job_counter:03d}_{lang}_{mode}_{base_name}"

                # Directive mapping
                if lang == "de" and mode == "easy": directive = "directives/de/leichte-sprache.md"
                elif lang == "de" and mode == "plain": directive = "directives/de/einfache-sprache.md"
                elif lang == "en" and mode == "easy": directive = "directives/en/easy-read.md"
                elif lang == "en" and mode == "plain": directive = "directives/en/plain-english.md"
                elif lang == "es" and mode == "easy": directive = "directives/es/lectura-facil.md"
                elif lang == "es" and mode == "plain": directive = "directives/es/lenguaje-claro.md"
                elif lang == "fr" and mode == "easy": directive = "directives/fr/falc.md"
                elif lang == "fr" and mode == "plain": directive = "directives/fr/langage-clair.md"
                elif lang == "it" and mode == "easy": directive = "directives/it/linguaggio-facile.md"
                elif lang == "it" and mode == "plain": directive = "directives/it/linguaggio-chiaro.md"
                elif lang == "nl" and mode == "easy": directive = "directives/nl/makkelijk-lezen.md"
                elif lang == "nl" and mode == "plain": directive = "directives/nl/klare-taal.md"
                elif lang == "ja" and mode == "easy": directive = "directives/ja/yasashii-nihongo.md"
                elif lang == "ja" and mode == "plain": directive = "directives/ja/plain-japanese.md"
                else: directive = "directives/en/easy-read.md" # Fallback

                target_file = f"examples/output/{base_name}_{lang}_{mode}.txt"

                job_b = {
                    "type": "translation",
                    "source_file": f"examples/input/{filename}",
                    "target_lang": lang,
                    "mode": mode,
                    "directive": directive,
                    "output_file": target_file
                }

                with open(QUEUE_DIR / f"{b_id}.json", "w", encoding="utf-8") as f:
                    json.dump(job_b, f, indent=2)

                # --- PHASE C: REVIEW JOB ---
                # Hängt von Phase B ab. Da Queue alphabetisch sortiert ist (job_b vor job_c),
                # wird dieser Job erst später gepickt.

                c_id = f"job_c_{job_counter:03d}_{lang}_{mode}_{base_name}_REVIEW"

                job_c = {
                    "type": "review",
                    "target_file_to_review": target_file,
                    "directive": "directives/review.md",
                    "output_file": f"{target_file}_REVIEW.md"
                }

                with open(QUEUE_DIR / f"{c_id}.json", "w", encoding="utf-8") as f:
                    json.dump(job_c, f, indent=2)

    print(f"SUCCESS: Generated {job_counter * 2} jobs (Translation + Review) in tickets/queue/")

if __name__ == "__main__":
    main()
