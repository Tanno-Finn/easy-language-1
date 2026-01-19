# Directive: Professional English Translation [M]

## Meta [M]
| Field | Value |
|-------|-------|
| **ID** | `normal-en` |
| **Type** | Standard Professional Translation |
| **Version** | 2.0 |
| **Text Direction** | LTR (Left-to-Right) |
| **Target Level** | Native / C1-C2 |

---

## Purpose [M]

Translate source texts into **natural, professional English** while maintaining accuracy, register, and cultural appropriateness.

**This directive serves as the MASTER TEMPLATE** for all `normal-*` translation directives.

---

## When to Use [M]

- Professional documents requiring accurate translation
- Business, legal, or technical texts
- Content where natural fluency is paramount
- When Easy Read (A1/A2) or Plain Language (B1) is NOT required

---

## Language Settings [M]

### Output Language
- **Primary:** British English (default) or American English (specify in request)
- **Script:** Latin
- **Text Direction:** LTR

### Accepted Source Languages [M]
- German (primary)
- Any language (with explicit user request)

### Script Handling [M]
| Source Script | Handling |
|--------------|----------|
| Latin (DE, FR, ES...) | Direct translation |
| Cyrillic (RU) | Transliterate names if needed |
| CJK (ZH, JA, KO) | Romanize proper nouns; keep brand names |
| Arabic/Hebrew (RTL) | Ensure correct embedding in LTR output |

---

## Core Principles [M]

### 1. Accuracy First [M]
- Preserve ALL information from the source text
- Do NOT add, omit, or invent content
- Maintain legal/technical validity of statements
- **NEVER hallucinate facts** [M]

### 2. Technical Terms [M]
- Use established English equivalents for technical terms
- If NO standard equivalent exists: keep original term + explanation on first use
- **Consistency Rule:** Same term = same translation throughout [M]

**Format for unknown terms:**
```
[Original Term] (English explanation)
```

### 3. Natural English [M]
- Use idiomatic English, NOT word-for-word translation
- Adapt sentence structure to English conventions
- Avoid source-language syntax patterns

### 4. Register Matching [M]
| Source Register | Target Register |
|----------------|-----------------|
| Formal/Legal | Formal English |
| Business | Professional English |
| Technical | Technical English |
| Casual | Conversational English |

**Pronoun Handling:**
- German "Sie" (formal) → "you" (context determines formality)
- German "du" (informal) → "you" (more casual phrasing)

---

## Handling Specific Elements [M]

### A. Compound Words [M]
Transform source compounds into natural English:

| German | English |
|--------|---------|
| Datenschutzerklärung | privacy policy |
| Nutzungsbedingungen | terms of use |
| Haftungsausschluss | disclaimer |
| Verantwortungsbereich | area of responsibility |

**Rule:** If compound is domain-specific, verify standard English equivalent exists.

### B. Legal References [M]
| Source | Target |
|--------|--------|
| § | Section / Article |
| Abs. | Paragraph / Subsection |
| Nr. | Number / Item |

- Keep paragraph/article numbers intact
- Note jurisdiction differences if legally relevant

### C. Numbers and Formats [M]

#### Number Conventions
| Element | English Format |
|---------|---------------|
| Thousands | 1,000 (comma) |
| Decimals | 0.50 (period) |
| Percentages | 50% or 50 percent |
| Phone | +44 20 1234 5678 |

#### Date Formats
| Variant | Format | Example |
|---------|--------|---------|
| British | DD Month YYYY | 15 January 2024 |
| American | Month DD, YYYY | January 15, 2024 |
| ISO (neutral) | YYYY-MM-DD | 2024-01-15 |

**Rule:** Match target audience locale or use ISO for international texts.

#### Currency
- Keep original currency with symbol: €50, £30, $100
- Add equivalent in parentheses if relevant: €50 (approx. £43)

### D. Abbreviations [M]
Expand source abbreviations and use English equivalents:

| Source | English |
|--------|---------|
| z.B. | e.g. / for example |
| d.h. | i.e. / that is |
| u.a. | among others |
| etc. | etc. (keep) |
| usw. | etc. |
| ggf. | if applicable / where relevant |
| bzgl. | regarding / concerning |
| inkl. | including |
| exkl. | excluding |

### E. Punctuation [M]
| Element | English Rule |
|---------|-------------|
| Quotation marks | "double" (US) or 'single' (UK) |
| Lists | Oxford comma optional (be consistent) |
| Colons | Capitalize after colon if full sentence follows (US) |
| Dashes | En-dash for ranges (1–10), em-dash for breaks |

---

## Cultural Adaptation [M]

### Idioms and Metaphors [M]
- Do NOT translate literally
- Find equivalent English idiom OR rephrase neutrally

| German Idiom | NOT | INSTEAD |
|--------------|-----|---------|
| Das ist nicht mein Bier | That is not my beer | That's not my concern |
| Tomaten auf den Augen haben | Have tomatoes on eyes | Miss the obvious |

### Cultural References [C]
- Localize if target audience won't understand
- Keep original + explanation for technical/legal texts

**Example:**
> "...nach dem BGB" → "...under the German Civil Code (BGB)"

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
| Acronym without context | Keep original, add [?] note |
| Missing reference | Flag with [REFERENCE NEEDED] |
| Ambiguous term | Translate most likely meaning, note in QA-Log |
| Corrupted text | Mark as [ILLEGIBLE] |

### Conflict Resolution [M]
- Source accuracy > target fluency
- If unsure: flag and ask

---

## Output Specifications [M]

### Format [M]
- Match source document structure (headings, paragraphs, lists)
- Preserve formatting markers if present
- Clean text output (no translator notes inline)

### File Naming [M]
```
{original_name}_{lang}.txt
```
Example: `agb_zeitreise_en.txt`

---

## Quality Checklist [M]

Before delivery, verify ALL items:

- [ ] All content accurately translated [M]
- [ ] Technical terms consistent throughout [M]
- [ ] Natural English flow (no "translatese") [M]
- [ ] Register matches source [M]
- [ ] No information added or omitted [M]
- [ ] Grammar and spelling correct [M]
- [ ] Numbers/dates in correct format [M]
- [ ] Glossary terms applied (if provided) [M]
- [ ] Cultural references appropriately handled [C]

---

## QA-Log Section [C]

For complex translations, append at the end:

```
---
### QA-Log (Auto-generated)

**Technical Terms:**
- [German term] → [English translation]

**Abbreviations Expanded:**
- [Source] → [Expansion]

**Cultural Adaptations:**
- [Original reference] → [Localized version]

**Flagged Items:**
- [Any ambiguities or issues noted]
```

---

## Adaptation Guide (For Other Languages) [M]

When creating `normal-{lang}.md` for a new language, adjust:

| Section | Adaptation Required |
|---------|-------------------|
| Meta: Text Direction | LTR or RTL |
| Language Settings | Target language specifics |
| Script Handling | Relevant scripts for that language |
| Number Formats | Local conventions (e.g., 1.000,50 for DE) |
| Date Formats | Local conventions |
| Punctuation | Language-specific rules (e.g., « » for FR) |
| Cultural Adaptation | Target culture examples |

### RTL Languages (AR, HE) [M]
Add section:
```markdown
## RTL Formatting [M]
- All output text MUST be RTL
- Embedded LTR elements (numbers, Latin text) handled per Unicode Bidi
- Use RTL-compatible punctuation
```

### Languages Without Spaces (JA, ZH) [M]
Add section:
```markdown
## Segmentation [M]
- No spaces between words (standard)
- Western punctuation vs. full-width (specify)
```

### Gendered Languages (DE, FR, ES) [M]
Add section:
```markdown
## Grammatical Gender [M]
- Agreement rules for target language
- Inclusive language options (if applicable)
```

---

## Disclaimer [M]

This directive provides professional translation guidelines.
All rules and examples are original formulations.
Inspired by: ISO 17100 Translation Services, ATA Guidelines.

---

**[END OF DIRECTIVE]**
