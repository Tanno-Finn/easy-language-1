# Directive: Professional Italian Translation [M]

## Meta [M]
| Field | Value |
|-------|-------|
| **ID** | `normal-it` |
| **Type** | Standard Professional Translation |
| **Version** | 2.0 |
| **Text Direction** | LTR (Left-to-Right) |
| **Target Level** | Native / C1-C2 |

---

## Purpose [M]

Translate source texts into **natural, professional Italian** while maintaining accuracy, register, and cultural appropriateness.

---

## When to Use [M]

- Professional documents requiring accurate translation
- Business, legal, or technical texts
- Content where natural fluency is paramount
- When Easy Read (A1/A2) or Plain Language (B1) is NOT required

---

## Language Settings [M]

### Output Language
- **Primary:** Standard Italian
- **Script:** Latin
- **Text Direction:** LTR

### Accepted Source Languages [M]
- German (primary)
- English
- Any language (with explicit user request)

### Script Handling [M]
| Source Script | Handling |
|--------------|----------|
| Latin (DE, EN, FR, ES...) | Direct translation |
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
- Use established Italian equivalents for technical terms
- If NO standard equivalent exists: keep original term + explanation on first use
- **Consistency Rule:** Same term = same translation throughout [M]

**Format for unknown terms:**
```
[Original Term] (spiegazione in italiano)
```

### 3. Natural Italian [M]
- Use idiomatic Italian, NOT word-for-word translation
- Adapt sentence structure to Italian conventions
- Avoid source-language syntax patterns
- Italian prefers longer, more complex sentences than English/German

### 4. Register Matching [M]
| Source Register | Target Register |
|----------------|-----------------|
| Formal/Legal | Italiano formale |
| Business | Italiano professionale |
| Technical | Italiano tecnico |
| Casual | Italiano colloquiale |

**Pronoun Handling:**
- German "Sie" / English "you" (formal) → "Lei" (singular formal) or "Voi" (plural/very formal)
- German "du" / English "you" (informal) → "tu" (informal)
- **Consistency:** Maintain the same level of formality throughout the text

---

## Grammatical Gender [M]

Italian is a gendered language. Apply these rules:

### Agreement Rules [M]
- Adjectives agree with nouns in gender AND number
- Past participles agree with direct object pronouns
- Professional titles: use appropriate gender form when known

| Situation | Handling |
|-----------|----------|
| Unknown gender | Use masculine as default (grammatical convention) |
| Mixed group | Use masculine plural |
| Inclusive option | Use both forms: "i lettori e le lettrici" or slash notation "i/le lettori/lettrici" |

### Job Titles [M]
| English | Italian (M) | Italian (F) |
|---------|-------------|-------------|
| Director | direttore | direttrice |
| Manager | responsabile | responsabile |
| President | presidente | presidente/presidentessa |
| User | utente | utente |

---

## Handling Specific Elements [M]

### A. Compound Words [M]
Transform source compounds into natural Italian:

| German/English | Italian |
|----------------|---------|
| Datenschutzerklärung / privacy policy | informativa sulla privacy |
| Nutzungsbedingungen / terms of use | condizioni d'uso |
| Haftungsausschluss / disclaimer | esclusione di responsabilità |
| Verantwortungsbereich / area of responsibility | ambito di competenza |

**Rule:** Italian often uses prepositional phrases where German uses compounds.

### B. Legal References [M]
| Source | Target |
|--------|--------|
| § / Section | Art. / Articolo |
| Abs. / Paragraph | comma |
| Nr. / Number | n. / numero |

- Keep paragraph/article numbers intact
- Italian legal references: "Art. 5, comma 2, lettera a)"
- Note jurisdiction differences if legally relevant

### C. Numbers and Formats [M]

#### Number Conventions
| Element | Italian Format |
|---------|---------------|
| Thousands | 1.000 (period) |
| Decimals | 0,50 (comma) |
| Percentages | 50% or il 50 per cento |
| Phone | +39 02 1234 5678 |

#### Date Formats
| Context | Format | Example |
|---------|--------|---------|
| Standard | DD mese YYYY | 15 gennaio 2024 |
| Abbreviated | DD/MM/YYYY | 15/01/2024 |
| ISO (neutral) | YYYY-MM-DD | 2024-01-15 |

**Months (lowercase in Italian):**
gennaio, febbraio, marzo, aprile, maggio, giugno, luglio, agosto, settembre, ottobre, novembre, dicembre

**Rule:** Use spelled-out dates for formal documents, numeric for tables/data.

#### Currency
- Keep original currency with symbol: 50 EUR, 30 GBP, 100 USD
- Italian format: EUR 50,00 or 50,00 EUR
- Add equivalent in parentheses if relevant: EUR 50 (circa GBP 43)

### D. Abbreviations [M]
Expand source abbreviations and use Italian equivalents:

| Source (DE/EN) | Italian |
|----------------|---------|
| z.B. / e.g. | ad es. / per esempio |
| d.h. / i.e. | cioè / vale a dire |
| u.a. / among others | tra l'altro / fra gli altri |
| etc. | ecc. |
| usw. / etc. | ecc. |
| ggf. / if applicable | se del caso / eventualmente |
| bzgl. / regarding | riguardo a / relativamente a |
| inkl. / including | incluso/a / compreso/a |
| exkl. / excluding | escluso/a |

### E. Punctuation [M]
| Element | Italian Rule |
|---------|-------------|
| Quotation marks | «virgolette basse» (preferred) or "virgolette alte" |
| Lists | No Oxford comma in Italian |
| Colons | Lowercase after colon (unlike English) |
| Dashes | Trattino (-) for compound words; lineetta (–) for ranges |
| Spaces before punctuation | No space before : ; ? ! (unlike French) |

---

## Cultural Adaptation [M]

### Idioms and Metaphors [M]
- Do NOT translate literally
- Find equivalent Italian idiom OR rephrase neutrally

| Source | NOT | INSTEAD |
|--------|-----|---------|
| Das ist nicht mein Bier | Non è la mia birra | Non sono affari miei |
| That's not my cup of tea | Non è la mia tazza di tè | Non è il mio genere |
| To cost an arm and a leg | Costare un braccio e una gamba | Costare un occhio della testa |

### Cultural References [C]
- Localize if target audience won't understand
- Keep original + explanation for technical/legal texts

**Example:**
> "...nach dem BGB" → "...ai sensi del Codice Civile tedesco (BGB)"
> "...under GDPR" → "...ai sensi del GDPR (Regolamento UE 2016/679)"

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
| Missing reference | Flag with [RIFERIMENTO NECESSARIO] |
| Ambiguous term | Translate most likely meaning, note in QA-Log |
| Corrupted text | Mark as [ILLEGGIBILE] |

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
Example: `agb_zeitreise_it.txt`

---

## Quality Checklist [M]

Before delivery, verify ALL items:

- [ ] All content accurately translated [M]
- [ ] Technical terms consistent throughout [M]
- [ ] Natural Italian flow (no "traduttese") [M]
- [ ] Register matches source [M]
- [ ] No information added or omitted [M]
- [ ] Grammar and spelling correct [M]
- [ ] Gender agreement correct throughout [M]
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
- [Source term] → [Italian translation]

**Abbreviations Expanded:**
- [Source] → [Expansion]

**Cultural Adaptations:**
- [Original reference] → [Localized version]

**Gender Decisions:**
- [Term] → [Gender used and rationale]

**Flagged Items:**
- [Any ambiguities or issues noted]
```

---

## Disclaimer [M]

This directive provides professional translation guidelines.
All rules and examples are original formulations.
Inspired by: ISO 17100 Translation Services, Accademia della Crusca recommendations.

---

**[END OF DIRECTIVE]**
