# Beispiel-Datensätze für Leichte Sprache Übersetzung

Dieser Ordner enthält synthetische (fiktive) Fachtexte, um die Leistungsfähigkeit der Übersetzungs-Direktiven zu testen.

## Warum diese Texte?
Die Texte simulieren echte Anwendungsfälle aus Recht und Technik, sind aber inhaltlich fiktiv, um urheberrechtliche Probleme zu vermeiden (MIT License).

1.  **`agb_zeitreise.txt`**: Simuliert komplexe juristische Vertragstexte (AGB). Testet den Umgang mit Haftungsausschluss, Kausalität und Schachtelsätzen.
2.  **`sicherheit_orbitalstation.txt`**: Simuliert technische Sicherheitsunterweisungen. Testet den Umgang mit Passiv, Imperativ und zusammengesetzten Fachwörtern (Komposita).
3.  **`datenschutz_telepathie.txt`**: Simuliert DSGVO-Texte. Testet den Umgang mit abstrakten Definitionen und gesetzlichen Verweisen.

## Wie testen?
Führe Claude Code mit folgendem Befehl aus:
> "Übersetze alle Dateien im Ordner examples/input in Leichte Sprache und speichere sie in examples/output."