#!/usr/bin/env python3
"""
Export-Script: Kombiniert CLAUDE.md und alle Direktiven in eine Datei.
Dynamisch - erkennt automatisch alle Sprachen in directives/[lang]/
"""

import os
from pathlib import Path
from datetime import datetime

# Projektverzeichnis (relativ zum Script)
PROJECT_ROOT = Path(__file__).parent.parent
DIRECTIVES_DIR = PROJECT_ROOT / "directives"
OUTPUT_FILE = PROJECT_ROOT / "tmp" / "export.md"


def get_language_folders():
    """Findet alle Sprach-Unterordner in directives/"""
    folders = []
    for item in sorted(DIRECTIVES_DIR.iterdir()):
        if item.is_dir():
            folders.append(item)
    return folders


def get_meta_files():
    """Findet alle .md-Dateien direkt in directives/ (nicht in Unterordnern)"""
    files = []
    for item in sorted(DIRECTIVES_DIR.iterdir()):
        if item.is_file() and item.suffix == ".md":
            files.append(item)
    return files


def read_file(path):
    """Liest eine Datei und gibt den Inhalt zurück"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"[Fehler beim Lesen: {e}]"


def main():
    # Output-Verzeichnis erstellen falls nötig
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    lines = []

    # Header
    lines.append("# Projekt-Export: Barrierefreie Übersetzungen")
    lines.append("")
    lines.append(f"**Generiert:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Lizenz-Disclaimer
    lines.append("## Lizenzhinweis")
    lines.append("")
    lines.append("**Dieses Dokument dient ausschliesslich internen Review-Zwecken.**")
    lines.append("")
    lines.append("- Alle Direktiven sind **Eigenentwicklungen**")
    lines.append("- Keine Inhalte wurden aus geschuetzten Quellen kopiert")
    lines.append("- Inspirationsquellen sind in den jeweiligen Direktiven genannt")
    lines.append("- Bei Weitergabe: Pruefen, ob eigene Lizenzangaben erforderlich")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Inhaltsverzeichnis
    lines.append("## Inhaltsverzeichnis")
    lines.append("")
    lines.append("1. [CLAUDE.md (Hauptkonfiguration)](#claudemd)")

    lang_folders = get_language_folders()
    meta_files = get_meta_files()

    section_num = 2
    for folder in lang_folders:
        lang_code = folder.name.upper()
        lines.append(f"{section_num}. [Direktiven: {lang_code}](#direktiven-{folder.name})")
        section_num += 1

    if meta_files:
        lines.append(f"{section_num}. [Meta-Direktiven](#meta-direktiven)")

    lines.append("")
    lines.append("---")
    lines.append("")

    # CLAUDE.md
    lines.append("## CLAUDE.md")
    lines.append("")
    claude_md = PROJECT_ROOT / "CLAUDE.md"
    if claude_md.exists():
        content = read_file(claude_md)
        lines.append("```markdown")
        lines.append(content)
        lines.append("```")
    else:
        lines.append("*Datei nicht gefunden*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Sprach-Direktiven
    for folder in lang_folders:
        lang_code = folder.name.upper()
        lines.append(f"## Direktiven: {lang_code}")
        lines.append("")

        md_files = sorted(folder.glob("*.md"))
        if not md_files:
            lines.append("*Keine Direktiven gefunden*")
        else:
            for md_file in md_files:
                lines.append(f"### {md_file.name}")
                lines.append("")
                lines.append(f"*Pfad: `directives/{folder.name}/{md_file.name}`*")
                lines.append("")
                content = read_file(md_file)
                lines.append("```markdown")
                lines.append(content)
                lines.append("```")
                lines.append("")

        lines.append("---")
        lines.append("")

    # Meta-Direktiven
    if meta_files:
        lines.append("## Meta-Direktiven")
        lines.append("")

        for md_file in meta_files:
            lines.append(f"### {md_file.name}")
            lines.append("")
            lines.append(f"*Pfad: `directives/{md_file.name}`*")
            lines.append("")
            content = read_file(md_file)
            lines.append("```markdown")
            lines.append(content)
            lines.append("```")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Statistik
    lines.append("## Statistik")
    lines.append("")
    lines.append(f"- **Sprachen:** {len(lang_folders)} ({', '.join(f.name.upper() for f in lang_folders)})")
    total_directives = sum(len(list(f.glob('*.md'))) for f in lang_folders)
    lines.append(f"- **Sprach-Direktiven:** {total_directives}")
    lines.append(f"- **Meta-Direktiven:** {len(meta_files)}")
    lines.append("")

    # Schreiben
    output = "\n".join(lines)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"[OK] Export erstellt: {OUTPUT_FILE}")
    print(f"  - {len(lang_folders)} Sprachen: {', '.join(f.name for f in lang_folders)}")
    print(f"  - {total_directives + len(meta_files)} Direktiven total")


if __name__ == "__main__":
    main()
