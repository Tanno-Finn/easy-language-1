# Directive: Professional Czech Translation [M]

## Meta [M]
| Field | Value |
|-------|-------|
| **ID** | `normal-cs` |
| **Type** | Standard Professional Translation |
| **Version** | 2.0 |
| **Text Direction** | LTR (Left-to-Right) |
| **Target Level** | Native / C1-C2 |

---

## Purpose [M]

Translate source texts into **natural, professional Czech** while maintaining accuracy, register, and cultural appropriateness.

---

## When to Use [M]

- Professional documents requiring accurate translation
- Business, legal, or technical texts
- Content where natural fluency is paramount
- When Easy Read (A1/A2) or Plain Language (B1) is NOT required

---

## Language Settings [M]

### Output Language
- **Primary:** Standard Czech (spisovná čeština)
- **Script:** Latin (with háčky and čárky: č, ř, ž, š, á, é, í, ó, ú, ů, ý)
- **Text Direction:** LTR

### Accepted Source Languages [M]
- German (primary)
- English (common)
- Any language (with explicit user request)

### Script Handling [M]
| Source Script | Handling |
|--------------|----------|
| Latin (DE, EN, FR...) | Direct translation |
| Cyrillic (RU) | Transliterate names to Czech conventions |
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
- Use established Czech equivalents for technical terms
- If NO standard equivalent exists: keep original term + explanation on first use
- **Consistency Rule:** Same term = same translation throughout [M]

**Format for unknown terms:**
```
[Original Term] (český vysvětlivka)
```

### 3. Natural Czech [M]
- Use idiomatic Czech, NOT word-for-word translation
- Adapt sentence structure to Czech conventions
- Utilize Czech's flexible word order for emphasis and flow
- Apply correct declension and conjugation

### 4. Register Matching [M]
| Source Register | Target Register |
|----------------|-----------------|
| Formal/Legal | Formal Czech (spisovná čeština) |
| Business | Professional Czech |
| Technical | Technical Czech |
| Casual | Conversational Czech (hovorová čeština) |

**Pronoun Handling:**
- German "Sie" / English "you" (formal) → Czech "vy" (vykání)
- German "du" / English "you" (informal) → Czech "ty" (tykání)

---

## Grammatical Gender [M]

Czech has three grammatical genders that affect declension:

| Gender | Example | Declension Pattern |
|--------|---------|-------------------|
| Masculine animate | uživatel (user) | Full 7-case declension |
| Masculine inanimate | dokument (document) | Different accusative |
| Feminine | smlouva (contract) | -a/-e/-ost patterns |
| Neuter | právo (right) | -o/-í/-e patterns |

**Agreement Rules:**
- Adjectives must agree in gender, number, and case
- Past tense verbs agree in gender and number
- Maintain consistency throughout the document

**Inclusive Language:**
- Use gender-neutral alternatives where appropriate: "uživatelé a uživatelky" or "osoby"
- For generic references, masculine plural is standard but alternatives exist

---

## Handling Specific Elements [M]

### A. Compound Words [M]
Transform source compounds into natural Czech:

| German | Czech |
|--------|-------|
| Datenschutzerklärung | prohlášení o ochraně osobních údajů |
| Nutzungsbedingungen | podmínky užívání |
| Haftungsausschluss | vyloučení odpovědnosti |
| Verantwortungsbereich | oblast odpovědnosti |

**Rule:** Czech often uses prepositional phrases or genitive constructions instead of compounds.

### B. Legal References [M]
| Source | Czech |
|--------|-------|
| § | § (keep) |
| Article | článek (čl.) |
| Paragraph | odstavec (odst.) |
| Section | oddíl |
| Number/Item | bod / písmeno |

- Keep paragraph/article numbers intact
- Reference Czech legal terminology (zákon, vyhláška, nařízení)

### C. Numbers and Formats [M]

#### Number Conventions
| Element | Czech Format |
|---------|-------------|
| Thousands | 1 000 (non-breaking space) |
| Decimals | 0,50 (comma) |
| Percentages | 50 % (space before %) |
| Phone | +420 123 456 789 |

#### Date Formats
| Format | Example |
|--------|---------|
| Standard | 15. ledna 2024 |
| Numeric | 15. 1. 2024 |
| ISO (neutral) | 2024-01-15 |

**Month names (genitive for dates):**
ledna, února, března, dubna, května, června, července, srpna, září, října, listopadu, prosince

#### Currency
- Czech koruna: 500 Kč or CZK 500
- Foreign currencies: 50 € (approx. 1 250 Kč)
- Keep original currency with equivalent if relevant

### D. Abbreviations [M]
Expand source abbreviations and use Czech equivalents:

| Source | Czech |
|--------|-------|
| e.g. / z.B. | např. (například) |
| i.e. / d.h. | tj. (to jest) |
| etc. / usw. | atd. (a tak dále) |
| approx. / ca. | cca / přibl. (přibližně) |
| if applicable | popř. (popřípadě) |
| regarding | ohledně / ve věci |
| including | vč. (včetně) |
| excluding | bez / vyjma |

### E. Punctuation [M]
| Element | Czech Rule |
|---------|-----------|
| Quotation marks | „double" (99-66 style) or »guillemets« |
| Lists | No Oxford comma (Czech standard) |
| Colons | Lowercase after colon |
| Dashes | Pomlčka (–) for ranges and breaks |
| Decimal separator | Comma (,) |

**Quotation hierarchy:**
1. Primary: „text"
2. Secondary (nested): ‚text' or »text«

---

## Cultural Adaptation [M]

### Idioms and Metaphors [M]
- Do NOT translate literally
- Find equivalent Czech idiom OR rephrase neutrally

| Source | NOT | INSTEAD |
|--------|-----|---------|
| That's not my concern | To není můj koncern | To není moje starost |
| Break a leg | Zlom nohu | Zlom vaz |

### Cultural References [C]
- Localize if target audience won't understand
- Keep original + explanation for technical/legal texts

**Example:**
> "...under the BGB" → "...podle německého občanského zákoníku (BGB)"

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
| Corrupted text | Mark as [NEČITELNÉ] |

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
{original_name}_cs.txt
```
Example: `agb_zeitreise_cs.txt`

---

## Quality Checklist [M]

Before delivery, verify ALL items:

- [ ] All content accurately translated [M]
- [ ] Technical terms consistent throughout [M]
- [ ] Natural Czech flow (no "překladatelština") [M]
- [ ] Register matches source [M]
- [ ] No information added or omitted [M]
- [ ] Grammar correct (declension, conjugation, agreement) [M]
- [ ] Diacritics correct (háčky, čárky) [M]
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
- [Source term] → [Czech translation]

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
Inspired by: ISO 17100 Translation Services, Czech Language Institute (ÚJČ) guidelines.

---

**[END OF DIRECTIVE]**
