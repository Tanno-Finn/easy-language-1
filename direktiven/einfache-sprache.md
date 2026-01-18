# Direktive: Übersetzung in Einfache Sprache (B1-Niveau)

**ID:** `einfache-sprache-business`
**Zielgruppe:** Menschen mit Leseschwäche, Deutsch als Zweitsprache oder Leser, die Informationen schnell erfassen wollen (Scan-Reading).
**Niveau:** A2/B1 (Gut verständlicher Fließtext).

---

## 1. Grundprinzipien
Im Gegensatz zur Leichten Sprache darf hier **Fließtext** stehen. Der Text wirkt professioneller und erwachsener, bleibt aber maximal verständlich.

### Wann nutzen?
* Bei Betriebsvereinbarungen für alle Mitarbeiter.
* Bei E-Mails, Intranet-News oder Schulungen für gemischte Teams.
* Wenn Leichte Sprache als "zu kindlich" empfunden würde.

---

## 2. Die Sprach-Regeln

### A. Satzbau & Grammatik
* **Satzlänge:** Durchschnittlich 15 Wörter. Maximal 20.
* **Nebensätze:** Erlaubt, aber maximal einer pro Satz (keine Schachtelsätze).
    * *Gut:* "Bitte melden Sie sich, wenn Sie Fragen haben."
    * *Schlecht:* "Bitte melden Sie sich, wenn Sie Fragen haben, die sich auf das Projekt beziehen, welches wir gestern starteten."
* **Genitiv:** Erlaubt, wenn er geläufig ist ("Das Ziel des Projekts"). Bei komplexen Konstruktionen lieber "von" nutzen.
* **Passiv:** Sparsam nutzen. Aktiv ist immer besser.
    * *Ok:* "Der Antrag wird bearbeitet."
    * *Besser:* "Wir bearbeiten Ihren Antrag."

### B. Fachbegriffe & Rechtliches (Business-Kontext)
Hier gilt nicht die strikte Hybrid-Regel der Leichten Sprache ("Das heißt...").
* **Fachbegriffe:** Dürfen verwendet werden.
* **Erklärung:** Erkläre schwierige Begriffe beiläufig im Kontext oder in einem Nebensatz.
* **Beispiel:** "Bitte achten Sie auf die Compliance-Richtlinien, also unsere Regeln für faires Verhalten im Unternehmen."

---

## 3. Edge Cases & Formatierung

### A. Anglizismen
Im Business-Umfeld sind gängige Anglizismen in Einfacher Sprache okay, wenn sie etabliert sind.
* *Ok:* Meeting, Download, Team, Online.
* *Vermeiden:* "Vorgehen challengen", "Commitment zeigen". -> *Besser:* "Vorgehen hinterfragen", "Zusage einhalten".

### B. Abkürzungen
Gängige Abkürzungen (z.B., usw., Dr., PKW) sind erlaubt.
Unbekannte oder interne Abkürzungen (z.B. "gem. § 5 ArbSchG") müssen beim ersten Mal ausgeschrieben oder aufgelöst werden.

### C. Lange Wörter (Komposita)
Du musst keine Bindestriche setzen, aber es wird empfohlen bei Wörtern über 20 Buchstaben.
* *Ok:* Arbeitssicherheitsunterweisung
* *Besser:* Arbeitssicherheits-Unterweisung

### D. Gendern
Nutze neutrale Formulierungen oder die Paarform. Keine Sonderzeichen (*, _, :), da diese den Lesefluss stören.
* *Gut:* "Alle Mitarbeitenden", "Das Team", "Mitarbeiter und Mitarbeiterinnen".

### E. Formatierung
* Nutze Zwischenüberschriften, um den Text zu gliedern.
* Wichtige Infos dürfen **fett** markiert werden.
* Nutze Aufzählungslisten für 3 oder mehr Punkte.

---

## 4. Beispiele (Vergleich)

### Beispiel 1: Rechtlicher Hinweis
**Original:**
"Zuwiderhandlungen gegen die Sicherheitsbestimmungen können arbeitsrechtliche Konsequenzen nach sich ziehen."

**Einfache Sprache (B1):**
"Wenn Sie gegen die Sicherheitsregeln verstoßen, hat das arbeitsrechtliche Folgen. Im schlimmsten Fall können Sie abgemahnt oder gekündigt werden."

**(Vergleich Leichte Sprache A2 - nur zur Info):**
"Halten Sie sich an die Regeln.
Wenn Sie das nicht tun:
Dann bekommen Sie Ärger."

### Beispiel 2: IT-Anweisung
**Original:**
"Nach erfolgreicher Authentifizierung im Backend ist der Datensatz zu validieren."

**Einfache Sprache (B1):**
"Melden Sie sich im System an. Danach müssen Sie prüfen, ob die Daten korrekt sind."

---

## 5. Checkliste vor Ausgabe

1.  [ ] Ist der Ton respektvoll und erwachsen (nicht kindlich)?
2.  [ ] Sind Schachtelsätze aufgelöst?
3.  [ ] Sind interne Fachbegriffe kurz erklärt (ohne den Lesefluss zu stoppen)?
4.  [ ] Ist der Text optisch gegliedert (Absätze, Überschriften)?

---

## 6. Dokumentation & QA-Log

Füge am **ganz unteren Ende** jeder übersetzten Datei einen kurzen QA-Anhang an.
Dieser ist kürzer als bei Leichter Sprache, da weniger strikte Regeln gelten.

**Format:**

```markdown
---

### QA-Log

**Verwendete Fachbegriffe:**
- [Kurze Liste der wichtigsten Fachbegriffe im Text]

**Sprach-Niveau Check:**
- Schachtelsätze vermieden: [Ja/Nein]
- Durchschnittliche Satzlänge: [ca. X Wörter]
```

**Beispiel:**
```markdown
---

### QA-Log

**Verwendete Fachbegriffe:**
- Usability, User Experience, Effektivität, Effizienz, Zufriedenstellung, Nutzungskontext

**Sprach-Niveau Check:**
- Schachtelsätze vermieden: Ja
- Durchschnittliche Satzlänge: ca. 14 Wörter
```