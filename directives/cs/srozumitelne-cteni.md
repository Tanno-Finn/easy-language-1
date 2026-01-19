# Directive: Srozumitelné Čtení (Czech Easy Read) [M]

## Basis [M]
**Type:** Adaptation
**Framework:** Based on German Leichte Sprache model
**Origin:** Adapted for Czech; no established Czech Easy Read standard exists

---

## Purpose [M]
Translate text into **Srozumitelné Čtení** (Easy-to-Read Czech).

## Language Settings [M]
- **Output Language:** Czech
- **Anchor Phrase:** "**To znamená:**"
- **Level:** A1/A2 (CEFR equivalent)

---

## Core Rules [M]

### 1. Sentence Structure [M]
- **One sentence per line.** Hard line break after every sentence.
- Maximum 8-10 words per sentence.
- Use simple Subject-Verb-Object order.
- No subordinate clauses (který, že, když, protože).

### 2. Hybrid Rule (Technical Terms) [M]
When you encounter a technical term:

1. Keep the term in **bold**.
2. Add a period.
3. New paragraph.
4. Write "**To znamená:**" alone on its own line.
5. New paragraph.
6. Explain in simple words.

**Example:**
```
Zpracováváme vaše **osobní údaje**.

To znamená:

Informace o vás.
Například: vaše jméno.
```

### 3. Grammar Simplification [M]
Czech has 7 grammatical cases. To avoid confusion:
- Keep sentences short and clear.
- Prefer nominative and accusative.
- Avoid long genitive chains.
- No passive voice (avoid "je zpracováván").
- No participle constructions.

### 4. Vocabulary [M]
- Use everyday Czech words.
- Avoid formal/bureaucratic language.
- Avoid archaic or literary vocabulary.
- Expand all abbreviations.

### 5. Formatting [M]
- Use bullet points for lists.
- Bold technical terms.
- Numbers as digits.
- Use Czech punctuation.

---

## QA-Log Section [M]

At the end of every translation, append:

```
---
### QA-Log (Automaticky vygenerováno)

**Zachované odborné termíny:**
- [list technical terms]

**Rozepsané zkratky:**
- [list abbreviations expanded]

**Zjednodušená složená slova:**
- [list simplified compounds]
```

---

## Example Output [M]

**Input:**
> Osobní údaje budou zpracovávány v souladu se zákonem o ochraně osobních údajů.

**Output:**
```
Používáme vaše **osobní údaje**.

To znamená:

Informace o vás.
Například vaše jméno a adresa.

Je tady zákon.
Zákon se jmenuje **Zákon o ochraně osobních údajů**.

To znamená:

Zákon, který chrání vaše informace.
```
