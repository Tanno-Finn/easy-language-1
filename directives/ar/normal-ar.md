# Directive: Professional Arabic Translation [M]

## Meta [M]
| Field | Value |
|-------|-------|
| **ID** | `normal-ar` |
| **Type** | Standard Professional Translation |
| **Version** | 2.0 |
| **Text Direction** | RTL (Right-to-Left) |
| **Target Level** | Native / C1-C2 |

---

## Purpose [M]

Translate source texts into **natural, professional Arabic (Modern Standard Arabic)** while maintaining accuracy, register, and cultural appropriateness.

---

## When to Use [M]

- Professional documents requiring accurate translation
- Business, legal, or technical texts
- Content where natural fluency is paramount
- When Easy Read (A1/A2) or Plain Language (B1) is NOT required

---

## Language Settings [M]

### Output Language
- **Primary:** Modern Standard Arabic (MSA / الفصحى)
- **Script:** Arabic
- **Text Direction:** RTL (Right-to-Left)

### Accepted Source Languages [M]
- German (primary)
- English
- Any language (with explicit user request)

### Script Handling [M]
| Source Script | Handling |
|--------------|----------|
| Latin (DE, EN, FR...) | Translate; transliterate proper nouns if no standard Arabic form |
| Cyrillic (RU) | Translate; transliterate names |
| CJK (ZH, JA, KO) | Translate; transliterate proper nouns |
| Arabic | Direct processing |
| Hebrew | Direct translation (related Semitic structure) |

---

## RTL Formatting [M]

- All output text MUST be RTL
- Embedded LTR elements (numbers, Latin brand names) handled per Unicode Bidi Algorithm
- Use Arabic punctuation marks where standard
- Numbers may appear LTR within RTL text (standard behavior)
- Preserve logical order for mixed-direction content

---

## Core Principles [M]

### 1. Accuracy First [M]
- Preserve ALL information from the source text
- Do NOT add, omit, or invent content
- Maintain legal/technical validity of statements
- **NEVER hallucinate facts** [M]

### 2. Technical Terms [M]
- Use established Arabic equivalents for technical terms
- If NO standard equivalent exists: keep original term + Arabic explanation on first use
- **Consistency Rule:** Same term = same translation throughout [M]

**Format for unknown terms:**
```
[Original Term] (التفسير بالعربية)
```

### 3. Natural Arabic [M]
- Use idiomatic Arabic, NOT word-for-word translation
- Adapt sentence structure to Arabic conventions (VSO or SVO as appropriate)
- Avoid source-language syntax patterns
- Maintain proper Arabic rhetoric flow (البلاغة)

### 4. Register Matching [M]
| Source Register | Target Register |
|----------------|-----------------|
| Formal/Legal | Formal Arabic (الفصحى الرسمية) |
| Business | Professional Arabic |
| Technical | Technical Arabic |
| Casual | Conversational MSA |

**Pronoun Handling:**
- German "Sie" (formal) → أنتم / حضرتكم (formal plural)
- German "du" (informal) → أنتَ / أنتِ (gender-appropriate singular)
- English "you" → Context determines formality level

---

## Handling Specific Elements [M]

### A. Compound Words [M]
Transform source compounds into natural Arabic (typically إضافة constructions):

| German | Arabic |
|--------|--------|
| Datenschutzerklärung | سياسة الخصوصية |
| Nutzungsbedingungen | شروط الاستخدام |
| Haftungsausschluss | إخلاء المسؤولية |
| Verantwortungsbereich | نطاق المسؤولية |

**Rule:** Arabic compounds often use إضافة (genitive construct) or وصفية (adjectival) structures.

### B. Legal References [M]
| Source | Arabic |
|--------|--------|
| § / Section | المادة |
| Abs. / Paragraph | الفقرة |
| Nr. / Number | البند / رقم |
| Article | المادة |

- Keep paragraph/article numbers intact (Arabic-Indic or Western numerals per context)
- Note jurisdiction differences if legally relevant

### C. Numbers and Formats [M]

#### Numeral Systems
| Context | System | Example |
|---------|--------|---------|
| General text | Western Arabic (0-9) | 1,000 |
| Traditional/Religious | Arabic-Indic (٠-٩) | ١٬٠٠٠ |
| Mixed contexts | Prefer Western Arabic for consistency |

#### Number Conventions
| Element | Arabic Format |
|---------|---------------|
| Thousands | 1,000 or 1.000 (context-dependent) |
| Decimals | 0.50 or 0,50 |
| Percentages | 50% or ٥٠٪ |
| Phone | +966 XX XXX XXXX (regional format) |

#### Date Formats
| System | Format | Example |
|--------|--------|---------|
| Gregorian | DD/MM/YYYY | 15/01/2024 |
| Gregorian (written) | DD شهر YYYY | 15 يناير 2024 |
| Hijri (if required) | DD/MM/YYYY هـ | 03/07/1445 هـ |

**Rule:** Use Gregorian unless Hijri specifically required. Include both for official documents if culturally appropriate.

#### Currency
- Keep original currency with symbol: €50، £30، $100
- Add Arabic name if relevant: 50 يورو (€50)
- Gulf currencies: ريال، درهم، دينار

### D. Abbreviations [M]
Expand source abbreviations and use Arabic equivalents:

| Source | Arabic |
|--------|--------|
| z.B. / e.g. | مثل / على سبيل المثال |
| d.h. / i.e. | أي / بمعنى |
| u.a. / among others | من بين أمور أخرى |
| etc. | إلخ |
| ggf. / if applicable | عند الاقتضاء / إن وُجد |
| bzgl. / regarding | بشأن / فيما يتعلق بـ |
| inkl. / including | بما في ذلك / شاملاً |
| exkl. / excluding | باستثناء / غير شامل |

### E. Punctuation [M]
| Element | Arabic Rule |
|---------|-------------|
| Full stop | . (standard) |
| Comma | ، (Arabic comma U+060C) or , |
| Question mark | ؟ (Arabic question mark U+061F) |
| Semicolon | ؛ (Arabic semicolon U+061B) |
| Quotation marks | « » (guillemets) or " " |
| Lists | No Oxford comma in Arabic |
| Parentheses | ( ) — same orientation |

---

## Grammatical Gender [M]

Arabic has grammatical gender for nouns, verbs, and adjectives:

### Gender Agreement [M]
- All adjectives must agree with noun gender
- Verbs must agree with subject gender
- Plurals have complex gender rules (جمع المذكر السالم، جمع المؤنث السالم، جمع التكسير)

### Gender-Neutral Options [M]
For inclusive language when gender is unknown:
- Use masculine plural (traditional default)
- Use dual forms: المستخدم/ة، الموظف/ة (user m/f)
- Rephrase to avoid gender: "الأشخاص الذين..." instead of gendered singular

---

## Cultural Adaptation [M]

### Idioms and Metaphors [M]
- Do NOT translate literally
- Find equivalent Arabic idiom OR rephrase neutrally

| German Idiom | NOT | INSTEAD |
|--------------|-----|---------|
| Das ist nicht mein Bier | هذا ليس بيرتي | هذا ليس من شأني |
| Tomaten auf den Augen haben | عنده طماطم على عينيه | لا يرى ما هو واضح |

### Cultural Sensitivity [M]
- Avoid cultural/religious conflicts in phrasing
- Adapt examples to culturally appropriate alternatives
- Keep alcohol, pork, and gambling references neutral or substitute where appropriate
- Religious expressions (إن شاء الله, بإذن الله) — add only if culturally expected in context

### Cultural References [C]
- Localize if target audience won't understand
- Keep original + Arabic explanation for technical/legal texts

**Example:**
> "...nach dem BGB" → "...وفقاً للقانون المدني الألماني (BGB)"

---

## Glossary Integration [M]

### Priority Order [M]
1. **Client glossary** (if provided) — use EXACT terms
2. **Domain glossary** (if exists in `glossaries/`)
3. **Standard translation** (your professional judgment)

### Glossary Override Rule [M]
If glossary contains a term: **USE IT VERBATIM**.
Do NOT invent alternatives when a definition exists.

---

## Error Handling [M]

### Untranslatable Elements [M]
| Situation | Action |
|-----------|--------|
| Acronym without context | Keep original, add [؟] note |
| Missing reference | Flag with [مرجع مطلوب] |
| Ambiguous term | Translate most likely meaning, note in QA-Log |
| Corrupted text | Mark as [غير مقروء] |

### Conflict Resolution [M]
- Source accuracy > target fluency
- If unsure: flag and ask

---

## Output Specifications [M]

### Format [M]
- Match source document structure (headings, paragraphs, lists)
- Preserve formatting markers if present
- Clean text output (no translator notes inline)
- Ensure proper RTL rendering

### File Naming [M]
```
{original_name}_ar.txt
```
Example: `agb_zeitreise_ar.txt`

---

## Quality Checklist [M]

Before delivery, verify ALL items:

- [ ] All content accurately translated [M]
- [ ] Technical terms consistent throughout [M]
- [ ] Natural Arabic flow (no "translatese") [M]
- [ ] Register matches source [M]
- [ ] No information added or omitted [M]
- [ ] Grammar and spelling correct [M]
- [ ] Gender agreement correct throughout [M]
- [ ] Numbers/dates in correct format [M]
- [ ] RTL formatting correct [M]
- [ ] Arabic punctuation used appropriately [M]
- [ ] Glossary terms applied (if provided) [M]
- [ ] Cultural references appropriately handled [C]

---

## QA-Log Section [C]

For complex translations, append at the end:

```
---
### QA-Log (Auto-generated)

**Technical Terms:**
- [Source term] → [Arabic translation]

**Abbreviations Expanded:**
- [Source] → [Expansion]

**Cultural Adaptations:**
- [Original reference] → [Localized version]

**Flagged Items:**
- [Any ambiguities or issues noted]
```

---

## Disclaimer [M]

This directive provides professional translation guidelines.
All rules and examples are original formulations.
Inspired by: ISO 17100 Translation Services, ATA Guidelines.

---

**[END OF DIRECTIVE]**
