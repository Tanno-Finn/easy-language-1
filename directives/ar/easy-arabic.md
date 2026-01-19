# Directive: اللغة العربية السهلة (Arabic Easy Read) [M]

## Basis [M]
**Type:** Adaptation
**Framework:** Based on German Leichte Sprache model with RTL adaptations
**Origin:** Adapted for Arabic; no established Arabic Easy Read standard exists

---

## Purpose [M]
Translate text into **اللغة العربية السهلة** (Easy-to-Read Arabic).

## Language Settings [M]
- **Output Language:** Modern Standard Arabic (العربية الفصحى المبسطة)
- **Anchor Phrase:** "**وهذا يعني:**"
- **Level:** A1/A2 (CEFR equivalent)
- **Text Direction:** RTL (Right-to-Left)

---

## CRITICAL: RTL FORMATTING [M]

**MANDATORY RIGHT-TO-LEFT RULE:**
- All text MUST be formatted Right-to-Left.
- Bullet points must function correctly in RTL context.
- Numbers remain LTR within RTL text (standard behavior).
- Technical terms in Latin script should be wrapped properly.

---

## Core Rules [M]

### 1. Sentence Structure [M]
- **One sentence per line.** Hard line break after every sentence.
- Maximum 8-10 words per sentence.
- Use simple Verb-Subject-Object or Subject-Verb-Object order.
- No complex subordinate clauses.

### 2. Hybrid Rule (Technical Terms) [M]
When you encounter a technical term:

1. Keep the term in **bold**.
2. Add a period (.).
3. New paragraph.
4. Write "**وهذا يعني:**" alone on its own line.
5. New paragraph.
6. Explain in simple words.

**Example:**
```
نحن نستخدم **بياناتك الشخصية**.

وهذا يعني:

معلومات عنك.
مثل: اسمك.
```

### 3. Grammar Restrictions [M]
**SPECIAL RULE - AVOID DUAL FORM (المثنى):**
- Use plural (الجمع) instead of dual.
- Dual forms are confusing for many readers.

**Bad:** "المستخدمان" (the two users)
**Good:** "المستخدمون" (the users)

**Additional restrictions:**
- No passive voice where avoidable.
- No complex verb forms (الأوزان المعقدة).
- Avoid classical Arabic constructions.
- Use Modern Standard Arabic, not classical.

### 4. Vocabulary [M]
- Use common, everyday Arabic words.
- Avoid Quranic or classical vocabulary.
- Avoid regional dialects (stay MSA).
- Expand all abbreviations.
- For English technical terms: transliterate AND explain.

### 5. Formatting [M]
- Use bullet points for lists (RTL-compatible).
- Bold technical terms.
- Numbers as digits (Arabic-Indic ٠١٢ or Western 012 - be consistent).
- Use Arabic punctuation (، . ؟ !).

---

## QA-Log Section [M]

At the end of every translation, append:

```
---
### سجل ضمان الجودة (تم إنشاؤه تلقائياً)

**المصطلحات الفنية المحفوظة:**
- [list technical terms]

**الاختصارات الموسعة:**
- [list abbreviations expanded]

**الكلمات المركبة المبسطة:**
- [list simplified compounds]
```

---

## Example Output [M]

**Input:**
> تتم معالجة البيانات الشخصية وفقاً لقانون حماية البيانات.

**Output:**
```
نحن نستخدم **بياناتك الشخصية**.

وهذا يعني:

معلومات عنك.
مثل: اسمك وعنوانك.

هناك قانون.
اسم القانون: **قانون حماية البيانات**.

وهذا يعني:

قانون يحمي معلوماتك.
```
