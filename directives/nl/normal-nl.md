# Directive: Professional Dutch Translation [M]

## Meta [M]
| Field | Value |
|-------|-------|
| **ID** | `normal-nl` |
| **Type** | Standard Professional Translation |
| **Version** | 2.0 |
| **Text Direction** | LTR (Left-to-Right) |
| **Target Level** | Native / C1-C2 |

---

## Purpose [M]

Translate source texts into **natural, professional Dutch** while maintaining accuracy, register, and cultural appropriateness.

---

## When to Use [M]

- Professional documents requiring accurate translation
- Business, legal, or technical texts
- Content where natural fluency is paramount
- When Easy Read (A1/A2) or Plain Language (B1) is NOT required

---

## Language Settings [M]

### Output Language
- **Primary:** Standard Dutch (Netherlands) or Belgian Dutch (Flemish) — specify in request
- **Script:** Latin
- **Text Direction:** LTR

### Accepted Source Languages [M]
- German (primary)
- English (primary)
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
- Use established Dutch equivalents for technical terms
- If NO standard equivalent exists: keep original term + explanation on first use
- **Consistency Rule:** Same term = same translation throughout [M]

**Format for unknown terms:**
```
[Original Term] (Dutch explanation)
```

### 3. Natural Dutch [M]
- Use idiomatic Dutch, NOT word-for-word translation
- Adapt sentence structure to Dutch conventions
- Avoid source-language syntax patterns
- Keep Dutch sentence rhythm (verb-second in main clauses)

### 4. Register Matching [M]
| Source Register | Target Register |
|----------------|-----------------|
| Formal/Legal | Formeel Nederlands |
| Business | Zakelijk Nederlands |
| Technical | Technisch Nederlands |
| Casual | Informeel Nederlands |

**Pronoun Handling:**
- German "Sie" / English "you" (formal) → "u"
- German "du" / English "you" (informal) → "je/jij"
- **Belgian Dutch:** "u" is more common even in semi-formal contexts

---

## Handling Specific Elements [M]

### A. Compound Words [M]
Dutch uses compound words similar to German. Transform appropriately:

| German | Dutch |
|--------|-------|
| Datenschutzerklärung | privacyverklaring |
| Nutzungsbedingungen | gebruiksvoorwaarden |
| Haftungsausschluss | aansprakelijkheidsuitsluiting / disclaimer |
| Verantwortungsbereich | verantwoordelijkheidsgebied |

| English | Dutch |
|---------|-------|
| privacy policy | privacybeleid |
| terms of use | gebruiksvoorwaarden |
| disclaimer | disclaimer / vrijwaring |
| area of responsibility | verantwoordelijkheidsgebied |

**Rule:** Dutch compounds are written as one word (no spaces).
- Correct: privacyverklaring
- Incorrect: privacy verklaring

### B. Legal References [M]
| Source | Target |
|--------|--------|
| § / Section | Artikel |
| Abs. / Paragraph | Lid |
| Nr. / Number | Nummer |

- Keep paragraph/article numbers intact
- Note jurisdiction differences if legally relevant
- Reference Dutch legal system where appropriate (Burgerlijk Wetboek, etc.)

### C. Numbers and Formats [M]

#### Number Conventions
| Element | Dutch Format |
|---------|-------------|
| Thousands | 1.000 (period) |
| Decimals | 0,50 (comma) |
| Percentages | 50% or 50 procent |
| Phone | +31 20 123 4567 |

#### Date Formats
| Variant | Format | Example |
|---------|--------|---------|
| Standard | DD maand YYYY | 15 januari 2024 |
| Numeric | DD-MM-YYYY | 15-01-2024 |
| ISO (neutral) | YYYY-MM-DD | 2024-01-15 |

**Rule:** Use standard format for formal texts; ISO for international/technical texts.

#### Currency
- Keep original currency with symbol: €50, £30, $100
- Euro is primary in Netherlands/Belgium: € 50,00 (space after symbol)

### D. Abbreviations [M]
Expand source abbreviations and use Dutch equivalents:

| German | Dutch |
|--------|-------|
| z.B. | bijv. / bijvoorbeeld |
| d.h. | d.w.z. / dat wil zeggen |
| u.a. | o.a. / onder andere |
| etc. | enz. / enzovoort |
| usw. | enz. |
| ggf. | indien van toepassing |
| bzgl. | m.b.t. / met betrekking tot |
| inkl. | incl. / inclusief |
| exkl. | excl. / exclusief |

| English | Dutch |
|---------|-------|
| e.g. | bijv. / bijvoorbeeld |
| i.e. | d.w.z. / dat wil zeggen |
| etc. | enz. / enzovoort |
| incl. | incl. / inclusief |
| excl. | excl. / exclusief |

### E. Punctuation [M]
| Element | Dutch Rule |
|---------|-----------|
| Quotation marks | "dubbel" or 'enkel' (no guillemets) |
| Lists | No Oxford comma (standard Dutch) |
| Colons | Lowercase after colon |
| Dashes | En-dash for ranges (1–10) |

---

## Grammatical Gender [M]

Dutch has two grammatical genders for articles:
- **de** (common gender: masculine/feminine)
- **het** (neuter gender)

### Gender Rules [M]
- Check article in authoritative dictionary (Van Dale, Woordenlijst)
- Diminutives always use "het" (het huisje, het meisje)
- Loanwords: often follow source gender or take "de"
- **Consistency Rule:** Same noun = same article throughout [M]

### Common Examples
| Noun | Article | Translation |
|------|---------|-------------|
| website | de | the website |
| document | het | the document |
| gebruiker | de | the user |
| systeem | het | the system |
| voorwaarde | de | the condition |
| beleid | het | the policy |

---

## Cultural Adaptation [M]

### Idioms and Metaphors [M]
- Do NOT translate literally
- Find equivalent Dutch idiom OR rephrase neutrally

| Source Idiom | NOT | INSTEAD |
|--------------|-----|---------|
| It's not my cup of tea | Het is niet mijn kop thee | Het is niet mijn ding |
| Das ist nicht mein Bier | Dat is niet mijn bier | Dat is mijn zaak niet |
| To beat around the bush | Om de struik slaan | Eromheen draaien |

### Cultural References [C]
- Localize if target audience won't understand
- Keep original + explanation for technical/legal texts

**Example:**
> "...under the BGB" → "...volgens het Duitse Burgerlijk Wetboek (BGB)"

### Netherlands vs. Belgium [C]
Be aware of regional differences:
| Netherlands | Belgium (Flemish) |
|-------------|-------------------|
| pinpas | bankkaart |
| mobiel | gsm |
| computer | computer |
| sorry | excuseer |

**Rule:** Default to Netherlands Dutch unless otherwise specified.

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
| Missing reference | Flag with [REFERENTIE NODIG] |
| Ambiguous term | Translate most likely meaning, note in QA-Log |
| Corrupted text | Mark as [ONLEESBAAR] |

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
{original_name}_nl.txt
```
Example: `agb_zeitreise_nl.txt`

---

## Quality Checklist [M]

Before delivery, verify ALL items:

- [ ] All content accurately translated [M]
- [ ] Technical terms consistent throughout [M]
- [ ] Natural Dutch flow (no "translatese") [M]
- [ ] Register matches source [M]
- [ ] No information added or omitted [M]
- [ ] Grammar and spelling correct [M]
- [ ] Numbers/dates in correct format [M]
- [ ] Glossary terms applied (if provided) [M]
- [ ] Article gender correct (de/het) [M]
- [ ] Cultural references appropriately handled [C]

---

## QA-Log Section [C]

For complex translations, append at the end:

```
---
### QA-Log (Auto-generated)

**Technical Terms:**
- [Source term] → [Dutch translation]

**Abbreviations Expanded:**
- [Source] → [Expansion]

**Article Gender Verified:**
- [de/het + noun]

**Cultural Adaptations:**
- [Original reference] → [Localized version]

**Flagged Items:**
- [Any ambiguities or issues noted]
```

---

## Disclaimer [M]

This directive provides professional translation guidelines.
All rules and examples are original formulations.
Inspired by: ISO 17100 Translation Services, Nederlandse Taalunie guidelines.

---

**[END OF DIRECTIVE]**
