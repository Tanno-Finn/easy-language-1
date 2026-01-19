# Directive: Professional Chinese Translation [M]

## Meta [M]
| Field | Value |
|-------|-------|
| **ID** | `normal-zh` |
| **Type** | Standard Professional Translation |
| **Version** | 2.0 |
| **Text Direction** | LTR (Left-to-Right) |
| **Target Level** | Native / C1-C2 |
| **Script** | Simplified Chinese (default) / Traditional Chinese (on request) |

---

## Purpose [M]

Translate source texts into **natural, professional Chinese** while maintaining accuracy, register, and cultural appropriateness.

---

## When to Use [M]

- Professional documents requiring accurate translation
- Business, legal, or technical texts
- Content where natural fluency is paramount
- When Easy Read (A1/A2) or Plain Language (B1) is NOT required

---

## Language Settings [M]

### Output Language
- **Primary:** Simplified Chinese (Mainland China, default)
- **Alternative:** Traditional Chinese (Taiwan/Hong Kong, specify in request)
- **Script:** Han characters (Hanzi)
- **Text Direction:** LTR (horizontal), TTB optional (vertical, rare in modern use)

### Accepted Source Languages [M]
- German (primary)
- English
- Any language (with explicit user request)

### Script Handling [M]
| Source Script | Handling |
|--------------|----------|
| Latin (DE, EN, FR...) | Direct translation into Chinese |
| Cyrillic (RU) | Direct translation; transliterate names |
| CJK (JA, KO) | Direct translation; keep shared characters where appropriate |
| Arabic/Hebrew (RTL) | Direct translation; transliterate names |

---

## Core Principles [M]

### 1. Accuracy First [M]
- Preserve ALL information from the source text
- Do NOT add, omit, or invent content
- Maintain legal/technical validity of statements
- **NEVER hallucinate facts** [M]

### 2. Technical Terms [M]
- Use established Chinese equivalents for technical terms
- If NO standard equivalent exists: keep original term + explanation on first use
- **Consistency Rule:** Same term = same translation throughout [M]

**Format for unknown terms:**
```
[Original Term]（中文解释）
```

### 3. Natural Chinese [M]
- Use idiomatic Chinese, NOT word-for-word translation
- Adapt sentence structure to Chinese conventions
- Avoid source-language syntax patterns (especially SVO → topic-comment where natural)
- Use appropriate measure words (量词)

### 4. Register Matching [M]
| Source Register | Target Register |
|----------------|-----------------|
| Formal/Legal | 正式书面语 |
| Business | 商务用语 |
| Technical | 技术术语 |
| Casual | 口语化表达 |

**Pronoun Handling:**
- German "Sie" (formal) → 您 (formal) or 你 (standard)
- German "du" (informal) → 你
- English "you" → 您/你 based on context

---

## Handling Specific Elements [M]

### A. Compound Words [M]
Transform source compounds into natural Chinese:

| German | Chinese |
|--------|---------|
| Datenschutzerklärung | 隐私政策 |
| Nutzungsbedingungen | 使用条款 |
| Haftungsausschluss | 免责声明 |
| Verantwortungsbereich | 职责范围 |

**Rule:** If compound is domain-specific, verify standard Chinese equivalent exists.

### B. Legal References [M]
| Source | Chinese |
|--------|---------|
| § / Section | 第...条 |
| Abs. / Paragraph | 第...款 |
| Nr. / Number | 第...项 |

- Keep paragraph/article numbers intact
- Note jurisdiction differences if legally relevant
- Reference Chinese legal naming conventions where applicable

### C. Numbers and Formats [M]

#### Number Conventions
| Element | Chinese Format |
|---------|---------------|
| Thousands | 1,000 or 1000 (comma optional) |
| Large numbers | 万 (10,000), 亿 (100,000,000) |
| Decimals | 0.50 (period) |
| Percentages | 50% or 百分之五十 |
| Phone | +86 10 1234 5678 |

#### Date Formats
| Context | Format | Example |
|---------|--------|---------|
| Standard | YYYY年M月D日 | 2024年1月15日 |
| Abbreviated | YYYY/MM/DD | 2024/01/15 |
| ISO (technical) | YYYY-MM-DD | 2024-01-15 |

**Rule:** Use 年月日 format for formal documents; ISO for technical texts.

#### Currency
- Keep original currency with symbol: €50, £30, $100
- Add Chinese equivalent if relevant: €50（约合人民币390元）
- RMB format: ¥100 or 100元

### D. Abbreviations [M]
Expand source abbreviations and use Chinese equivalents:

| Source | Chinese |
|--------|---------|
| z.B. / e.g. | 例如、如 |
| d.h. / i.e. | 即、也就是说 |
| u.a. / among others | 等、其中包括 |
| etc. / usw. | 等、等等 |
| ggf. / if applicable | 如适用、必要时 |
| bzgl. / regarding | 关于、就...而言 |
| inkl. / including | 包括、含 |
| exkl. / excluding | 不包括、不含 |

### E. Punctuation [M]
| Element | Chinese Rule |
|---------|-------------|
| Quotation marks | ""（外层）''（内层） |
| Lists | 顿号（、）for series; comma for clauses |
| Period | 。(full-width) |
| Comma | ，(full-width) |
| Colon | ：(full-width) |
| Question mark | ？(full-width) |
| Exclamation | ！(full-width) |
| Parentheses | （）(full-width for Chinese text) |

**Important:** Use full-width punctuation for Chinese text, half-width for embedded Latin/numbers.

---

## Segmentation [M]

- No spaces between Chinese characters (standard)
- Add space between Chinese and Latin text/numbers for readability
- Example: 本文件遵循 ISO 9001 标准

---

## Cultural Adaptation [M]

### Idioms and Metaphors [M]
- Do NOT translate literally
- Find equivalent Chinese idiom (成语/俗语) OR rephrase neutrally

| German Idiom | NOT | INSTEAD |
|--------------|-----|---------|
| Das ist nicht mein Bier | 那不是我的啤酒 | 这不关我的事 |
| Tomaten auf den Augen haben | 眼睛上有番茄 | 视而不见 |

### Cultural References [C]
- Localize if target audience won't understand
- Keep original + explanation for technical/legal texts

**Example:**
> "...nach dem BGB" → "...根据《德国民法典》（BGB）"

### Measurement Units [M]
| Source | Chinese |
|--------|---------|
| km, m, cm | 公里、米、厘米 (SI units standard) |
| kg, g | 公斤、克 |
| Traditional option | 里、斤 (only if culturally appropriate) |

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
| Missing reference | Flag with [待补充参考资料] |
| Ambiguous term | Translate most likely meaning, note in QA-Log |
| Corrupted text | Mark as [文本不清] |

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
{original_name}_zh.txt
```
Example: `agb_zeitreise_zh.txt`

---

## Quality Checklist [M]

Before delivery, verify ALL items:

- [ ] All content accurately translated [M]
- [ ] Technical terms consistent throughout [M]
- [ ] Natural Chinese flow (no "翻译腔") [M]
- [ ] Register matches source [M]
- [ ] No information added or omitted [M]
- [ ] Grammar correct [M]
- [ ] Numbers/dates in correct format [M]
- [ ] Glossary terms applied (if provided) [M]
- [ ] Full-width punctuation used correctly [M]
- [ ] Cultural references appropriately handled [C]

---

## QA-Log Section [C]

For complex translations, append at the end:

```
---
### QA-Log (Auto-generated)

**Technical Terms:**
- [Source term] → [Chinese translation]

**Abbreviations Expanded:**
- [Source] → [Expansion]

**Cultural Adaptations:**
- [Original reference] → [Localized version]

**Flagged Items:**
- [Any ambiguities or issues noted]
```

---

## Simplified vs. Traditional Chinese [M]

| Aspect | Simplified (简体) | Traditional (繁體) |
|--------|------------------|-------------------|
| Region | Mainland China, Singapore | Taiwan, Hong Kong, Macau |
| Character set | GB2312/GBK | Big5 |
| Default | Yes | Specify in request |

**Conversion Rules:**
- Simple character conversion is NOT sufficient
- Vocabulary differences exist (e.g., 软件 vs. 軟體 for "software")
- When creating Traditional version, verify regional vocabulary

---

## Disclaimer [M]

This directive provides professional translation guidelines.
All rules and examples are original formulations.
Inspired by: ISO 17100 Translation Services, GB/T 19363.1 Translation Service Standards.

---

**[END OF DIRECTIVE]**
