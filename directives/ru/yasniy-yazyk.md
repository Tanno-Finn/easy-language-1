# Directive: Ясный Язык (Russian Easy Read) [M]

## Purpose [M]
Translate text into **Ясный Язык** (Clear Russian / Easy-to-Read Russian).

## Language Settings [M]
- **Output Language:** Russian
- **Anchor Phrase:** "**Это значит:**"
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
4. Write "**Это значит:**" alone on its own line.
5. New paragraph.
6. Explain in simple words.

**Example:**
```
Мы обрабатываем ваши **персональные данные**.

Это значит:

Информация о вас.
Например: ваше имя.
```

### 3. Grammar Restrictions [M]
**SPECIAL RULE - AVOID PARTICIPLE CONSTRUCTIONS:**
- NO participle clauses (причастные обороты).
- NO adverbial participles (деепричастия).
- Break complex constructions into separate sentences.

**Bad:** "Данные, обрабатываемые компанией, хранятся..."
**Good:** "Компания обрабатывает данные. Данные хранятся..."

**Additional restrictions:**
- No passive voice with "-ся" where avoidable.
- Use "мы" (we) instead of impersonal constructions.
- Avoid genitive chains.

### 4. Vocabulary [M]
- Use everyday Russian words.
- Avoid Church Slavonic or formal bureaucratic terms.
- Expand all abbreviations.
- Prefer Russian words over foreign loanwords when a simple alternative exists.

### 5. Formatting [M]
- Use bullet points for lists.
- Bold technical terms.
- Numbers as digits.
- Use "вы" (formal you) for addressing the reader.

---

## QA-Log Section [M]

At the end of every translation, append:

```
---
### QA-лог (Сгенерировано автоматически)

**Сохранённые термины:**
- [list technical terms]

**Расшифрованные сокращения:**
- [list abbreviations expanded]

**Упрощённые конструкции:**
- [list simplified constructions]
```

---

## Example Output [M]

**Input:**
> Персональные данные обрабатываются в соответствии с законодательством о защите данных.

**Output:**
```
Мы используем ваши **персональные данные**.

Это значит:

Информация о вас.
Например: ваше имя и адрес.

Есть закон.
Закон защищает ваши данные.
Мы соблюдаем этот закон.
```
