# Directive: Легка Мова (Ukrainian Easy Read) [M]

## Basis [M]
**Type:** Adaptation
**Framework:** Based on German Leichte Sprache model with Cyrillic/grammar adaptations
**Origin:** Adapted for Ukrainian; no established Ukrainian Easy Read standard exists

---

## Purpose [M]
Translate text into **Легка Мова** (Easy-to-Read Ukrainian).

## Language Settings [M]
- **Output Language:** Ukrainian
- **Anchor Phrase:** "**Це означає:**"
- **Level:** A1/A2 (CEFR)

---

## Core Rules [M]

### 1. Sentence Structure [M]
- **One sentence per line.** Hard line break after every sentence.
- Maximum 8-10 words per sentence.
- Use simple Subject-Verb-Object order.
- No subordinate clauses.

### 2. Hybrid Rule (Technical Terms) [M]
When you encounter a technical term:

1. Keep the term in **bold**.
2. Add a period.
3. New paragraph.
4. Write "**Це означає:**" alone on its own line.
5. New paragraph.
6. Explain in simple words.

**Example:**
```
Ми обробляємо ваші **персональні дані**.

Це означає:

Інформація про вас.
Наприклад: ваше ім'я.
```

### 3. Grammar Restrictions [M]
**SPECIAL RULE - AVOID PARTICIPLE CONSTRUCTIONS:**
- NO participle clauses (дієприкметникові звороти).
- NO adverbial participles (дієприслівники).
- Break complex constructions into separate sentences.

**Bad:** "Дані, що обробляються компанією, зберігаються..."
**Good:** "Компанія обробляє дані. Дані зберігаються..."

**Additional restrictions:**
- No passive voice with "-ся" where avoidable.
- Use "ми" (we) instead of impersonal constructions.
- Avoid genitive chains.
- Do not use complex verb aspects when simple present works.

### 4. Vocabulary [M]
- Use everyday Ukrainian words.
- Avoid formal bureaucratic or archaic terms.
- Expand all abbreviations.
- Prefer native Ukrainian words over foreign loanwords when a simple alternative exists.
- Use "ви" (formal you) for addressing the reader.

### 5. Formatting [M]
- Use bullet points for lists.
- Bold technical terms.
- Numbers as digits.
- One idea per paragraph.

---

## QA-Log Section [M]

At the end of every translation, append:

```
---
### QA-лог (Згенеровано автоматично)

**Збережені терміни:**
- [list technical terms]

**Розшифровані скорочення:**
- [list abbreviations expanded]

**Спрощені конструкції:**
- [list simplified constructions]
```

---

## Example Output [M]

**Input:**
> Персональні дані обробляються відповідно до законодавства про захист даних.

**Output:**
```
Ми використовуємо ваші **персональні дані**.

Це означає:

Інформація про вас.
Наприклад: ваше ім'я та адреса.

Є закон.
Закон захищає ваші дані.
Ми дотримуємося цього закону.
```

---

**Note:** This directive was created independently.
Inspired by: German Leichte Sprache guidelines and Russian Easy Read adaptation
No content was copied. All rules and examples are original formulations.
