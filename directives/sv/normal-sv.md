# Directive: Professional Swedish Translation [M]

## Meta [M]
| Field | Value |
|-------|-------|
| **ID** | `normal-sv` |
| **Type** | Standard Professional Translation |
| **Version** | 2.0 |
| **Text Direction** | LTR (Left-to-Right) |
| **Target Level** | Native / C1-C2 |

---

## Purpose [M]

Translate source texts into **natural, professional Swedish** while maintaining accuracy, register, and cultural appropriateness.

---

## When to Use [M]

- Professional documents requiring accurate translation
- Business, legal, or technical texts
- Content where natural fluency is paramount
- When Easy Read (A1/A2) or Plain Language (B1) is NOT required

---

## Language Settings [M]

### Output Language
- **Primary:** Standard Swedish (Rikssvenska)
- **Script:** Latin
- **Text Direction:** LTR

### Accepted Source Languages [M]
- German (primary)
- English (common)
- Any language (with explicit user request)

### Script Handling [M]
| Source Script | Handling |
|--------------|----------|
| Latin (DE, EN, FR...) | Direct translation |
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
- Use established Swedish equivalents for technical terms
- If NO standard equivalent exists: keep original term + explanation on first use
- **Consistency Rule:** Same term = same translation throughout [M]

**Format for unknown terms:**
```
[Original Term] (svensk förklaring)
```

### 3. Natural Swedish [M]
- Use idiomatic Swedish, NOT word-for-word translation
- Adapt sentence structure to Swedish conventions
- Avoid source-language syntax patterns

### 4. Register Matching [M]
| Source Register | Target Register |
|----------------|-----------------|
| Formal/Legal | Formell svenska |
| Business | Affärssvenska |
| Technical | Teknisk svenska |
| Casual | Vardaglig svenska |

**Pronoun Handling (Du-reformen):**
- Modern Swedish predominantly uses "du" (informal)
- "Ni" (formal) only in very formal or historical contexts
- Legal/official texts may use passive constructions

---

## Handling Specific Elements [M]

### A. Compound Words [M]
Swedish uses compound words similar to German. Maintain natural compounds:

| German | Swedish |
|--------|---------|
| Datenschutzerklärung | integritetspolicy |
| Nutzungsbedingungen | användarvillkor |
| Haftungsausschluss | ansvarsfriskrivning |
| Verantwortungsbereich | ansvarsområde |

**Rule:** Use established Swedish compounds. Avoid creating awkward new formations.

### B. Legal References [M]
| Source | Swedish |
|--------|---------|
| § | § (paragraf) |
| Abs. | st. (stycke) |
| Nr. | nr / punkt |

- Keep paragraph/article numbers intact
- Reference Swedish law equivalents when contextually appropriate

### C. Numbers and Formats [M]

#### Number Conventions
| Element | Swedish Format |
|---------|---------------|
| Thousands | 1 000 (space) |
| Decimals | 0,50 (comma) |
| Percentages | 50 % or 50 procent |
| Phone | +46 8 123 45 67 |

#### Date Formats
| Format | Example |
|--------|---------|
| Standard | 15 januari 2024 |
| Numeric | 2024-01-15 (ISO, common in Sweden) |
| Short | 15/1 2024 |

**Rule:** Use ISO format (YYYY-MM-DD) for formal/international texts, written format for flowing prose.

#### Currency
- Swedish Krona: 50 kr or SEK 50
- Foreign currency: Keep original with symbol: €50, $100
- Add SEK equivalent if relevant: €50 (ca 550 kr)

### D. Abbreviations [M]
Expand source abbreviations and use Swedish equivalents:

| Source | Swedish |
|--------|---------|
| z.B. / e.g. | t.ex. (till exempel) |
| d.h. / i.e. | dvs. (det vill säga) |
| u.a. | bl.a. (bland annat) |
| etc. | etc. / osv. (och så vidare) |
| usw. | osv. |
| ggf. / if applicable | i tillämpliga fall |
| bzgl. / regarding | gällande / angående |
| inkl. | inkl. (inklusive) |
| exkl. | exkl. (exklusive) |

### E. Punctuation [M]
| Element | Swedish Rule |
|---------|-------------|
| Quotation marks | "citattecken" (straight) or "citattecken" (curly) |
| Lists | No Oxford comma (not used in Swedish) |
| Colons | Lowercase after colon unless proper noun |
| Dashes | En-dash for ranges (1–10), tankstreck for breaks |

---

## Cultural Adaptation [M]

### Idioms and Metaphors [M]
- Do NOT translate literally
- Find equivalent Swedish idiom OR rephrase neutrally

| German Idiom | NOT | INSTEAD |
|--------------|-----|---------|
| Das ist nicht mein Bier | Det är inte min öl | Det är inte min sak |
| Tomaten auf den Augen haben | Ha tomater på ögonen | Inte se det uppenbara |

### Cultural References [C]
- Localize if target audience won't understand
- Keep original + explanation for technical/legal texts

**Example:**
> "...nach dem BGB" → "...enligt den tyska civillagen (BGB)"

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
| Missing reference | Flag with [REFERENS SAKNAS] |
| Ambiguous term | Translate most likely meaning, note in QA-Log |
| Corrupted text | Mark as [OLÄSLIGT] |

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
Example: `agb_zeitreise_sv.txt`

---

## Quality Checklist [M]

Before delivery, verify ALL items:

- [ ] All content accurately translated [M]
- [ ] Technical terms consistent throughout [M]
- [ ] Natural Swedish flow (no "translatese") [M]
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
- [Källterm] → [Svensk översättning]

**Abbreviations Expanded:**
- [Källa] → [Expansion]

**Cultural Adaptations:**
- [Originalreferens] → [Lokaliserad version]

**Flagged Items:**
- [Eventuella oklarheter eller problem]
```

---

## Disclaimer [M]

This directive provides professional translation guidelines for Swedish.
All rules and examples are original formulations.
Inspired by: ISO 17100 Translation Services, Swedish Language Council guidelines.

---

**[END OF DIRECTIVE]**
