#!/usr/bin/env python3
"""
Forensic Audit Script
Outputs all relevant project files for inspection and audit purposes.

Usage:
  python scripts/forensic-audit.py > tmp/audit-report.md
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

# Force UTF-8 output on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')


def print_separator(title):
    """Print a section separator."""
    print(f"\n{'=' * 80}")
    print(f"# {title}")
    print(f"{'=' * 80}\n")


def print_file_content(filepath):
    """Print file contents with header."""
    path = Path(filepath)
    if not path.exists():
        print(f"[MISSING] {filepath}")
        return

    print(f"## {filepath}")
    print(f"```")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
    except Exception as e:
        print(f"[ERROR reading file: {e}]")
    print(f"```\n")


def count_jobs_by_status(queue_dir):
    """Count jobs by their status."""
    pending = 0
    in_progress = 0
    done = 0

    for f in Path(queue_dir).glob("*.json"):
        name = f.stem
        if "_DONE" in name:
            done += 1
        elif "_IN_PROGRESS" in name:
            in_progress += 1
        else:
            pending += 1

    return pending, in_progress, done


def main():
    print(f"# Forensic Audit Report")
    print(f"Generated: {datetime.now().isoformat()}")

    # 1. Project Structure Overview
    print_separator("1. PROJECT STRUCTURE")

    print("### Directory Structure")
    print("```")
    for root, dirs, files in os.walk("."):
        # Skip hidden and generated directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', 'tmp']]

        level = root.replace(".", "").count(os.sep)
        indent = "  " * level
        print(f"{indent}{os.path.basename(root)}/")

        sub_indent = "  " * (level + 1)
        for file in sorted(files):
            if not file.startswith('.'):
                print(f"{sub_indent}{file}")
    print("```\n")

    # 2. Queue Status
    print_separator("2. QUEUE STATUS")

    queue_dir = Path("tickets/queue")
    if queue_dir.exists():
        pending, in_progress, done = count_jobs_by_status(queue_dir)
        print(f"- **Pending:** {pending}")
        print(f"- **In Progress:** {in_progress}")
        print(f"- **Done:** {done}")
        print(f"- **Total:** {pending + in_progress + done}")

        # Sample job content
        print("\n### Sample Job (first pending)")
        jobs = sorted(queue_dir.glob("*.json"))
        if jobs:
            job_path = jobs[0]
            print(f"```json")
            with open(job_path, 'r', encoding='utf-8') as f:
                print(f.read())
            print("```")
    else:
        print("[Queue directory does not exist]")

    # 3. All Directives
    print_separator("3. DIRECTIVES - FULL CONTENT")

    directive_files = [
        # German
        "directives/de/leichte-sprache.md",
        "directives/de/einfache-sprache.md",
        # English
        "directives/en/easy-read.md",
        "directives/en/plain-english.md",
        # Spanish
        "directives/es/lectura-facil.md",
        "directives/es/lenguaje-claro.md",
        # French
        "directives/fr/falc.md",
        "directives/fr/langage-clair.md",
        # Italian
        "directives/it/linguaggio-facile.md",
        "directives/it/linguaggio-chiaro.md",
        # Dutch
        "directives/nl/makkelijk-lezen.md",
        "directives/nl/klare-taal.md",
        # Japanese
        "directives/ja/yasashii-nihongo.md",
        "directives/ja/plain-japanese.md",
        # Meta
        "directives/new-language-protocol.md",
        "directives/direktive.md",
        "directives/commits.md",
        "directives/queue-system.md",
        "directives/worker-loop.md",
    ]

    for f in directive_files:
        print_file_content(f)

    # 4. Scripts
    print_separator("4. SCRIPTS - FULL CONTENT")

    script_files = [
        "scripts/queue_manager.py",
        "scripts/generate-jobs.py",
        "scripts/export-config.py",
    ]

    for f in script_files:
        print_file_content(f)

    # 5. Configuration Files
    print_separator("5. CONFIGURATION")

    config_files = [
        "CLAUDE.md",
        ".gitignore",
    ]

    for f in config_files:
        print_file_content(f)

    # 6. Documentation
    print_separator("6. DOCUMENTATION")

    doc_files = [
        "docs/vision.md",
        "docs/architecture.md",
    ]

    for f in doc_files:
        print_file_content(f)

    # 7. Summary Statistics
    print_separator("7. SUMMARY STATISTICS")

    # Count files by type
    md_count = len(list(Path(".").rglob("*.md")))
    py_count = len(list(Path(".").rglob("*.py")))
    json_count = len(list(Path("tickets/queue").glob("*.json"))) if Path("tickets/queue").exists() else 0

    print(f"| Metric | Count |")
    print(f"|--------|-------|")
    print(f"| Markdown files | {md_count} |")
    print(f"| Python scripts | {py_count} |")
    print(f"| Queue jobs | {json_count} |")
    print(f"| Languages | 7 |")
    print(f"| Directive pairs | 7 |")

    print("\n### Anchor Phrases by Language")
    print("| Language | Anchor Phrase |")
    print("|----------|---------------|")
    print("| DE | Das heißt: |")
    print("| EN | That means: |")
    print("| ES | Eso significa: |")
    print("| FR | Cela signifie : |")
    print("| IT | Questo significa: |")
    print("| NL | Dat betekent: |")
    print("| JA | つまり： |")

    print("\n---")
    print("*End of Forensic Audit Report*")


if __name__ == "__main__":
    main()
