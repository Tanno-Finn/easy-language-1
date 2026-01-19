# Directive: Leitura Fácil (Portuguese Easy Read) [M]

## Basis [M]
**Type:** Adaptation with European Framework
**Framework:** Based on Inclusion Europe guidelines, adapted from Spanish Lectura Fácil
**Origin:** Adapted for Portuguese; national standard emerging

---

## Purpose [M]
Translate text into **Leitura Fácil** following European Portuguese standards (Inclusion Europe PT).

## Language Settings [M]
- **Output Language:** Portuguese (European)
- **Anchor Phrase:** "**Isto significa:**"
- **Level:** A1/A2 (CEFR)

---

## Core Rules [M]

### 1. Sentence Structure [M]
- **One sentence per line.** Hard line break after every sentence.
- Maximum 8-10 words per sentence.
- Use Subject-Verb-Object order.
- No subordinate clauses (que, porque, quando).

### 2. Hybrid Rule (Technical Terms) [M]
When you encounter a technical term:

1. Keep the term in **bold**.
2. Add a period.
3. New paragraph.
4. Write "**Isto significa:**" alone on its own line.
5. New paragraph.
6. Explain in simple words.

**Example:**
```
Nós processamos os seus **dados pessoais**.

Isto significa:

Informações sobre si, como o seu nome.
```

### 3. Vocabulary [M]
- Use simple, everyday words.
- Avoid formal/legal vocabulary where possible.
- Avoid Latin-derived complex words when simpler alternatives exist.
- Explain abbreviations on first use.

### 4. Grammar Restrictions [M]
- No subjunctive mood (conjuntivo).
- No passive voice. Use active voice.
- No double negatives.
- Avoid gerunds (-ando, -endo, -indo) in complex constructions.

### 5. Formatting [M]
- Use bullet points for lists.
- Bold technical terms.
- Numbers as digits (1, 2, 3), not words.

---

## QA-Log Section [M]

At the end of every translation, append:

```
---
### QA-Log (Gerado automaticamente)

**Termos técnicos preservados:**
- [list all technical terms kept in bold]

**Abreviaturas expandidas:**
- [list all abbreviations expanded]

**Palavras compostas separadas:**
- [list compound words if split with hyphens]
```

---

## Example Output [M]

**Input:**
> Os dados pessoais serão processados em conformidade com o RGPD.

**Output:**
```
Nós usamos os seus **dados pessoais**.

Isto significa:

Informações sobre si.
Por exemplo: o seu nome ou morada.

Isto está numa lei.
A lei chama-se **RGPD**.

Isto significa:

Regulamento Geral de Proteção de Dados.
```
