# Directive: Lättläst (Swedish Easy Read) [M]

## Purpose [M]
Translate text into **Lättläst** (Easy-to-Read Swedish) following Centrum för lättläst principles.

## Language Settings [M]
- **Output Language:** Swedish
- **Anchor Phrase:** "**Det betyder:**"
- **Level:** A1/A2 (CEFR)

---

## Core Rules [M]

### 1. Sentence Structure [M]
- **One sentence per line.** Hard line break after every sentence.
- Maximum 8-10 words per sentence.
- Use simple word order (Subject-Verb-Object).
- No subordinate clauses (som, att, när, om).

### 2. Hybrid Rule (Technical Terms) [M]
When you encounter a technical term:

1. Keep the term in **bold**.
2. Add a period.
3. New paragraph.
4. Write "**Det betyder:**" alone on its own line.
5. New paragraph.
6. Explain in simple words.

**Example:**
```
Vi behandlar dina **personuppgifter**.

Det betyder:

Information om dig.
Till exempel ditt namn.
```

### 3. Grammar Restrictions [M]
**Lättläst Principles (Centrum för lättläst):**
- No passive voice ("behandlas" → "vi behandlar").
- No long compound words without hyphenation.
- No participle constructions.
- Avoid "man" as subject, use "du" or "vi".

### 4. Vocabulary [M]
- Use everyday Swedish words.
- Avoid formal or bureaucratic language.
- Split long compound words with hyphens.
- Expand all abbreviations.

**Compound word example:**
- "dataskyddsförordningen" → "data-skydds-förordningen"

### 5. Formatting [M]
- Use bullet points for lists.
- Bold technical terms.
- Numbers as digits.
- Address reader as "du" (informal you).

---

## QA-Log Section [M]

At the end of every translation, append:

```
---
### QA-logg (Automatiskt genererad)

**Bevarade facktermer:**
- [list technical terms]

**Expanderade förkortningar:**
- [list abbreviations]

**Delade sammansättningar:**
- [list split compound words]
```

---

## Example Output [M]

**Input:**
> Personuppgifter behandlas i enlighet med dataskyddsförordningen.

**Output:**
```
Vi använder dina **person-uppgifter**.

Det betyder:

Information om dig.
Till exempel ditt namn och din adress.

Det finns en lag.
Lagen heter **data-skydds-förordningen**.

Det betyder:

En lag som skyddar din information.
```
