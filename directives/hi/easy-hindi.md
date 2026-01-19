# Directive: Easy Hindi / सरल हिंदी (Cognitive Accessibility)

## Basis [M]
**Type:** Adapted Standard
**Framework:** Inspired by international Easy-to-Read principles, adapted for Hindi
**Script:** Devanagari (देवनागरी)
**Speakers:** ~600 million

---

## Purpose [M]
Defines rules for translating texts into Easy Hindi (सरल हिंदी) while maintaining accuracy (Hybrid Approach).

**Priority:** Accuracy over maximum simplification. [M]
**Inspiration:** General Easy-to-Read principles adapted for Hindi grammar and Devanagari script.

## When to Use [M]
- For texts targeting people with learning disabilities [M]
- For legally relevant documents (contracts, policies, guidelines) [M]
- When maximum accessibility is required
- For readers with limited literacy

---

## Key Requirements [M]

### The Hybrid Rule (Supreme Directive) [M]
Because texts may have legal relevance, **technical terms are preserved** and explained.

#### 1. Glossary Priority [M]
If the glossary (input files) contains not just the term but also an explanation:
**You MUST use this explanation word-for-word.**
Do not invent new explanations when a definition exists.

#### 2. The "That means" Anchor [M]
Use **exclusively** the phrase **"इसका मतलब है:"** (Iska matlab hai:) for explanations.

#### 3. Anti-Doubling (CRITICAL) [M]
If the original sentence contains words before the technical term like "का अर्थ है:", "यानी:", "मतलब:" -> **DELETE these words** before adding "इसका मतलब है:".

#### 4. Hard Line Break (Mandatory) [M]
Every explanation needs **three separate paragraphs**:
1. Technical term (**bold**) + full stop (।).
2. New paragraph -> "इसका मतलब है:" (alone).
3. New paragraph -> Explanation.

**Correct Format:**
> **दक्षता**।
>
> इसका मतलब है:
>
> किसी लक्ष्य को पाने के लिए कितने साधनों की जरूरत होती है।

### Grammar & Sentence Structure [M]
- **One sentence = One idea** [M]
- **SOV order** (Subject - Object - Verb) - Hindi natural word order [M]
- **Active voice only** (कर्तृवाच्य) [M]
- **Positive statements** [C]
- **Simple verb forms** - avoid complex tenses [M]

### Hindi-Specific Rules [M]

#### A. Postpositions [M]
Keep postpositions (में, पर, को, से, के लिए) close to their noun.

**Example:**
> Good: मेज पर किताब है।
> Avoid: किताब है मेज पर।

#### B. Gender Agreement [M]
Ensure verb endings match subject gender consistently.

**Example:**
> लड़का जाता है। (masculine)
> लड़की जाती है। (feminine)

#### C. Honorifics [M]
Use respectful forms (आप) for formal texts.
Use familiar forms (तुम/तू) only when explicitly appropriate.

### Formatting [M]
- Every sentence starts on a **new line** [M]
- Use many paragraphs [M]
- Use **पूर्ण विराम** (।) at sentence end, not period (.) [M]

---

## Edge Cases & Special Rules [M]

### A. Complex Words [M]
Avoid Sanskrit-heavy (तत्सम) words when simpler alternatives exist.

**Examples:**
| Avoid | Use Instead |
|-------|-------------|
| अभिलाषा | इच्छा |
| प्रारंभ | शुरू |
| समाप्त | खत्म |
| अपेक्षित | जरूरी |

### B. Abbreviations [M]
**Always write them out.**

**Example:**
> "उदाहरण के लिए" instead of "उदा."

### C. Compound Words [M]
Split long compound words (समास) into simpler phrases.

**Example:**
> "राष्ट्रपति" can stay, but explain: इसका मतलब है: देश का सबसे बड़ा नेता।

### D. English Loanwords [M]
Common English words used in Hindi can stay, but add Devanagari transliteration.

**Example:**
> कंप्यूटर (Computer)
> इंटरनेट (Internet)

### E. Numbers and Dates [M]
- Write numbers in **Devanagari numerals** (१, २, ३) or Arabic numerals (1, 2, 3) - be consistent.
- Write dates clearly: १ अप्रैल २०२४ or 1 अप्रैल 2024.

---

## Devanagari Script Rules [M]

### A. Matra Clarity [M]
Ensure vowel marks (मात्राएं) are clearly visible and correctly placed.

### B. Conjunct Characters [M]
Avoid complex conjuncts when possible. Use halant (्) form or split words.

**Example:**
> Prefer: विद्या
> Explain complex forms when unavoidable.

### C. Punctuation [M]
- Use पूर्ण विराम (।) not period (.)
- Use अर्ध विराम (;) sparingly
- Question mark (?) is acceptable

---

## Documentation & QA Log [M]
Add a QA appendix at the **very end** of every translated file:

### QA Log (Auto-generated)
**Preserved Technical Terms / संरक्षित शब्द:**
- [List terms with explanations provided]

**Simplified Words / सरलीकृत शब्द:**
- [List: original -> simplified]

---

**Note:** This directive was created independently.
Inspired by: International Easy-to-Read principles and Hindi linguistic conventions.
No content was copied. All rules and examples are original formulations.
