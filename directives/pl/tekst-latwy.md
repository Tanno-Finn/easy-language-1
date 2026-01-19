# Directive: Tekst Łatwy do Czytania (Polish Easy Read) [M]

## Basis [M]
**Type:** Adaptation
**Framework:** Based on German Leichte Sprache model
**Origin:** Adapted for Polish; no established national standard exists

---

## Purpose [M]
Translate text into **Tekst Łatwy do Czytania** (Easy-to-Read Polish).

## Language Settings [M]
- **Output Language:** Polish
- **Anchor Phrase:** "**To znaczy:**"
- **Level:** A1/A2 (CEFR)

---

## Core Rules [M]

### 1. Sentence Structure [M]
- **One sentence per line.** Hard line break after every sentence.
- Maximum 8-10 words per sentence.
- **CRITICAL:** Use strict Subject-Verb-Object order to avoid case confusion.
- No subordinate clauses.

### 2. Hybrid Rule (Technical Terms) [M]
When you encounter a technical term:

1. Keep the term in **bold** (in nominative case if possible).
2. Add a period.
3. New paragraph.
4. Write "**To znaczy:**" alone on its own line.
5. New paragraph.
6. Explain in simple words.

**Example:**
```
Przetwarzamy Twoje **dane osobowe**.

To znaczy:

Informacje o Tobie.
Na przykład: Twoje imię.
```

### 3. Grammar Simplification [M]
**SPECIAL RULE - DECLENSION HANDLING:**
Polish has 7 grammatical cases. To avoid confusion:
- Keep sentences extremely short.
- Use nominative case where possible.
- Avoid genitive chains (e.g., "przetwarzanie danych użytkownika systemu").
- Break complex phrases into multiple simple sentences.

**Avoid:**
- Participles (imiesłowy)
- Passive constructions with "zostać"
- Complex case sequences

### 4. Vocabulary [M]
- Use everyday words.
- Avoid formal/bureaucratic language.
- Expand all abbreviations.

### 5. Formatting [M]
- Use bullet points for lists.
- Bold technical terms.
- Numbers as digits.

---

## QA-Log Section [M]

At the end of every translation, append:

```
---
### QA-Log (Wygenerowano automatycznie)

**Zachowane terminy techniczne:**
- [list all technical terms]

**Rozwinięte skróty:**
- [list abbreviations expanded]

**Uproszczone złożenia:**
- [list simplified compounds]
```

---

## Example Output [M]

**Input:**
> Dane osobowe będą przetwarzane zgodnie z RODO.

**Output:**
```
Używamy Twoich **danych osobowych**.

To znaczy:

Informacje o Tobie.
Na przykład Twoje imię i adres.

Jest takie prawo.
To prawo nazywa się **RODO**.

To znaczy:

Ogólne Rozporządzenie o Ochronie Danych.
```
