# Directive: Easy Vietnamese (Cognitive Accessibility)

## Basis [M]
**Type:** Accessibility Standard
**Framework:** General Easy-to-Read Principles adapted for Vietnamese
**Origin:** Vietnam / International Accessibility Guidelines

---

## Purpose [M]
Defines rules for translating texts into Easy Vietnamese while maintaining accuracy (Hybrid Approach).

**Priority:** Accuracy over maximum simplification. [M]
**Inspiration:** General international Easy-to-Read principles, adapted for Vietnamese linguistic structure.

## When to Use [M]
- For texts targeting people with cognitive disabilities [M]
- For legally relevant documents (contracts, policies, guidelines) [M]
- For readers with limited literacy
- When maximum accessibility is required

---

## Key Requirements [M]

### The Hybrid Rule (Supreme Directive) [M]
Because texts may have legal relevance, **technical terms are preserved** and explained.

#### 1. Glossary Priority [M]
If the glossary (input files) contains not just the term but also an explanation:
**You MUST use this explanation word-for-word.**
Do not invent new explanations when a definition exists.

#### 2. The "Nghĩa là" Anchor [M]
Use **exclusively** the phrase "Nghĩa là:" for explanations.

#### 3. Anti-Doubling (CRITICAL) [M]
If the original sentence contains words before the technical term like "nghĩa là:", "có nghĩa là:", "là:" -> **DELETE these words** before adding "Nghĩa là:".

#### 4. Hard Line Break (Mandatory) [M]
Every explanation needs **three separate paragraphs**:
1. Technical term (**bold**) + full stop.
2. New paragraph -> "Nghĩa là:" (alone).
3. New paragraph -> Explanation.

**Correct Format:**
> **Hiệu quả**.
>
> Nghĩa là:
>
> Bạn cần bao nhiêu nguồn lực để đạt được mục tiêu.

### Grammar & Sentence Structure [M]
- **One sentence = One idea** [M]
- **SVO order** (Subject - Verb - Object) [M]
- **Active voice only** [M]
- **Positive statements** [C]

### Vietnamese-Specific Rules [M]

#### Tonal Diacritics [M]
- **ALWAYS preserve diacritics** (dấu thanh) correctly [M]
- Example: "nghĩa" not "nghia", "là" not "la"
- All 6 tones must be marked: à, á, ả, ã, ạ

#### Classifiers [M]
- Use common classifiers (từ loại) consistently
- Example: "một người" (a person), "một cái bàn" (a table)
- Avoid rare or literary classifiers

#### Sino-Vietnamese Words (Từ Hán Việt) [M]
- Explain Sino-Vietnamese terms with native Vietnamese words
- Example: **Hiệu quả** (Sino-Vietnamese) -> Explain with simpler words

#### Sentence Length [M]
- Maximum 12 words per sentence [M]
- One verb per sentence preferred [C]

### Formatting [M]
- Every sentence starts on a **new line** [M]
- Use many paragraphs [M]
- Use bullet points for lists [C]

---

## Edge Cases & Special Rules [M]

### A. Complex Words [M]
- Prefer native Vietnamese (từ thuần Việt) over Sino-Vietnamese (từ Hán Việt)
- Example: Use "nhà" instead of "gia đình" when possible

### B. Abbreviations [M]
- **Always write them out** [M]
- Example: "Việt Nam" not "VN"

### C. Pronouns [M]
- Use simple, neutral pronouns
- "Bạn" for "you" (neutral, friendly)
- "Chúng tôi" for "we" (formal)
- Avoid complex kinship-based pronouns

### D. Numbers and Dates [M]
- Write numbers as **digits** (1, 2, 3)
- Write dates clearly: "ngày 1 tháng 4 năm 2024"

### E. Metaphors [M]
- Avoid figurative language and idioms (thành ngữ)
- Use literal, concrete language

---

## Documentation & QA Log [M]
Add a QA appendix at the **very end** of every translated file:

### QA Log (Auto-generated)
**Preserved Technical Terms (Thuật ngữ giữ nguyên):**
- [List terms]
**Sino-Vietnamese Terms Explained (Từ Hán Việt đã giải thích):**
- [List terms]
**Expanded Abbreviations (Viết tắt đã mở rộng):**
- [List expansions]

---

**Note:** This directive was created independently.
Inspired by: International Easy-to-Read principles and Vietnamese linguistic accessibility research.
No content was copied. All rules and examples are original formulations.
