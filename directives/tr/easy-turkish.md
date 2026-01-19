# Directive: Kolay Okunan Turkce (Cognitive Accessibility)

## Basis [M]
**Type:** Accessibility Standard
**Framework:** General Easy-to-Read principles adapted for Turkish
**Origin:** Adapted for Turkish language structure

---

## Purpose [M]
Defines rules for translating texts into Easy Read Turkish while maintaining legal accuracy (Hybrid Approach).

**Priority:** Legal correctness over maximum simplification. [M]
**Target Audience:** People with cognitive disabilities, language learners, individuals with low literacy.

## When to Use [M]
- For texts targeting people with learning disabilities [M]
- For legally relevant documents (contracts, policies, guidelines) [M]
- When maximum accessibility is required
- For content targeting diverse Turkish-speaking audiences

---

## Key Requirements [M]

### The Hybrid Rule (Supreme Directive) [M]
Because texts may have legal relevance, **technical terms are preserved** and explained.

#### 1. Glossary Priority [M]
If the glossary (input files) contains not just the term but also an explanation:
**You MUST use this explanation word-for-word.**
Do not invent new explanations when a definition exists.

#### 2. The "Bu demek ki" Anchor [M]
Use **exclusively** the phrase "Bu demek ki:" for explanations.

This is the Turkish equivalent of "That means:".

#### 3. Anti-Doubling (CRITICAL) [M]
If the original sentence contains words before the technical term like "anlamina gelir:", "demektir:", "sudur:" -> **DELETE these words** before adding "Bu demek ki:".

#### 4. Hard Line Break (Mandatory) [M]
Every explanation needs **three separate paragraphs**:
1. Technical term (**bold**) + full stop.
2. New paragraph -> "Bu demek ki:" (alone).
3. New paragraph -> Explanation.

**Correct Format:**
> **Verimlilik**.
>
> Bu demek ki:
>
> Bir hedefe ulasmak icin ne kadar kaynak harcadiginiz.

---

## Turkish-Specific Grammar Rules [M]

### A. Agglutinative Structure [M]
Turkish adds meaning through suffixes. For Easy Read:
- **Break long suffix chains** into separate words where possible [M]
- Prefer shorter word forms over complex agglutinated forms [M]
- Maximum 2-3 suffixes per word [C]

**Example:**
| Complex | Easy Read |
|---------|-----------|
| gorusturebileceklerimizden | gorusebilecegimiz kisiler |
| anlatilamayacaklardanmis | anlatilamaz seylerden |

### B. Word Order (SOV Flexibility) [M]
Turkish uses SOV (Subject-Object-Verb) order, but allows flexibility.
- **Keep natural SOV order** [M]
- **One idea per sentence** [M]
- Place the most important information at the end (verb position) [C]

**Example:**
> Cocuk elmay yedi. (The child ate the apple.)

### C. Active Voice Only [M]
Avoid passive constructions with "-il-/-in-" suffixes.

| Passive (Avoid) | Active (Use) |
|-----------------|--------------|
| Karar verildi. | Yonetim karar verdi. |
| Form doldurulacak. | Siz formu dolduracaksiniz. |

### D. Vowel Harmony Awareness [C]
Maintain correct vowel harmony in suffixes - this is natural to native speakers but critical for clarity.

---

## General Rules [M]

### Sentence Structure [M]
- **One sentence = One idea** [M]
- **Maximum 10-12 words per sentence** [M]
- **Active voice only** [M]
- **Positive statements** (avoid "degil" constructions where possible) [C]

### Formatting [M]
- Every sentence starts on a **new line** [M]
- Use many paragraphs [M]
- Use bullet points for lists [C]

### Word Choice [M]
- Use everyday words (gunluk kelimeler) [M]
- Avoid Arabic/Persian loanwords when Turkish alternatives exist [C]
- Avoid formal/bureaucratic language (resmi dil) [M]

**Examples:**
| Formal/Foreign | Easy (Oz Turkce) |
|----------------|------------------|
| tesekkur ederim | sagol |
| lutfen | rica ederim |
| mukemmel | cok iyi |
| takriben | yaklasik |
| icra etmek | yapmak |

---

## Edge Cases & Special Rules [M]

### A. Complex Words [M]
Avoid formal or archaic vocabulary.
Use common, spoken Turkish.

### B. Abbreviations [M]
**Always write them out:**
| Abbreviation | Full Form |
|--------------|-----------|
| vb. | ve benzeri |
| vs. | vesaire (veya: ve digerleri) |
| Dr. | Doktor |
| Prof. | Profesor |

### C. Suffixes and Postpositions [M]
When possible, use separate postpositions instead of case suffixes for clarity.

**Example:**
| Complex Suffix | Clear Alternative |
|----------------|-------------------|
| evimde | benim evde |
| arkadaslarimla | arkadaslarim ile |

### D. Numbers and Dates [M]
- Write numbers as **digits** (1, 2, 3)
- Write dates clearly: 1 Nisan 2024

### E. Questions [C]
Use the question particle "mi/mi/mu/mu" clearly separated:
> Anladin mi?
> Yardim ister misiniz?

---

## Documentation & QA Log [M]
Add a QA appendix at the **very end** of every translated file:

### QA Log (Auto-generated)
**Preserved Technical Terms (Korunan Terimler):**
- [List terms]
**Expanded Abbreviations (Acilan Kisaltmalar):**
- [List expansions]
**Simplified Suffix Chains (Sadelelestirilen Ekler):**
- [List examples]

---

**Note:** This directive was created independently.
Inspired by: General Easy-to-Read principles, Turkish Language Association (TDK) guidelines for clear communication.
No content was copied. All rules and examples are original formulations.
