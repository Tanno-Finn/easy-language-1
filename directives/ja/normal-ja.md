# Directive: Professional Japanese Translation [M]

## Meta [M]
| Field | Value |
|-------|-------|
| **ID** | `normal-ja` |
| **Type** | Standard Professional Translation |
| **Version** | 2.0 |
| **Text Direction** | LTR (horizontal) / TTB (vertical option) |
| **Target Level** | Native / N1-N2 (JLPT equivalent) |

---

## Purpose [M]

Translate source texts into **natural, professional Japanese** while maintaining accuracy, register, and cultural appropriateness.

---

## When to Use [M]

- Professional documents requiring accurate translation
- Business, legal, or technical texts
- Content where natural fluency is paramount
- When Easy Read (やさしい日本語) or Plain Language is NOT required

---

## Language Settings [M]

### Output Language
- **Primary:** Standard Japanese (標準語)
- **Script:** Kanji (漢字), Hiragana (ひらがな), Katakana (カタカナ)
- **Text Direction:** Horizontal LTR (default) or Vertical RTL (if specified)

### Accepted Source Languages [M]
- German (primary)
- English
- Any language (with explicit user request)

### Script Handling [M]
| Source Script | Handling |
|--------------|----------|
| Latin (DE, EN, FR...) | Translate; keep brand names in katakana or original |
| Cyrillic (RU) | Transliterate to katakana |
| CJK (ZH, KO) | Use appropriate kanji; adapt readings |
| Arabic/Hebrew (RTL) | Transliterate proper nouns to katakana |

---

## Core Principles [M]

### 1. Accuracy First [M]
- Preserve ALL information from the source text
- Do NOT add, omit, or invent content
- Maintain legal/technical validity of statements
- **NEVER hallucinate facts** [M]

### 2. Technical Terms [M]
- Use established Japanese equivalents for technical terms
- If NO standard equivalent exists: keep original term (in katakana or Latin script) + explanation on first use
- **Consistency Rule:** Same term = same translation throughout [M]

**Format for unknown terms:**
```
[カタカナ表記 or Original Term]（日本語での説明）
```

### 3. Natural Japanese [M]
- Use idiomatic Japanese, NOT word-for-word translation
- Adapt sentence structure to Japanese SOV conventions
- Avoid source-language syntax patterns
- Use appropriate topic markers (は/が) and particles

### 4. Register and Keigo (敬語) [M]
| Source Register | Target Register |
|----------------|-----------------|
| Formal/Legal | 敬語・丁寧語 (polite/honorific) |
| Business | ビジネス敬語 (business Japanese) |
| Technical | 専門用語 with です/ます体 |
| Casual | 普通体 (plain form) |

**Formality Levels:**
| German | English | Japanese |
|--------|---------|----------|
| Sie (formal) | you | ～ていただく・～でございます form |
| du (informal) | you | ～する・～だ form |

---

## Handling Specific Elements [M]

### A. Foreign Words and Loanwords [M]
Transform source terms appropriately:

| Source | Japanese |
|--------|----------|
| Privacy Policy | プライバシーポリシー |
| Terms of Use | 利用規約 |
| Disclaimer | 免責事項 |
| Data Protection | データ保護 |
| Software | ソフトウェア |
| Internet | インターネット |

**Rule:**
- Established loanwords → katakana
- Technical/legal terms → use Japanese equivalent if standard exists
- Brand names → keep original or official Japanese name

### B. Legal References [M]
| Source | Japanese Target |
|--------|--------|
| § | 第～条 |
| Abs. / Paragraph | 第～項 |
| Nr. / Number | 第～号 |

- Add jurisdiction context when necessary
- German laws: ドイツ民法典（BGB）など

### C. Numbers and Formats [M]

#### Number Conventions
| Element | Japanese Format |
|---------|----------------|
| Thousands | 1,000 or 1000 (comma optional) |
| Large numbers | 万 (10,000), 億 (100,000,000) |
| Decimals | 0.50 (period) |
| Percentages | 50% or 50パーセント |
| Phone | +81-3-1234-5678 |

#### Date Formats
| Context | Format | Example |
|---------|--------|---------|
| Formal | YYYY年M月D日 | 2024年1月15日 |
| Era (optional) | 元号Y年M月D日 | 令和6年1月15日 |
| Numeric | YYYY/MM/DD | 2024/01/15 |

**Rule:** Use Western calendar (西暦) for international texts. Add era (和暦) only if legally required.

#### Currency
- Keep original with symbol: €50、£30、$100
- Convert to yen if relevant: €50（約8,000円）
- Japanese yen: ¥10,000 or 1万円

### D. Abbreviations [M]
Expand source abbreviations and use Japanese equivalents:

| Source | Japanese |
|--------|---------|
| z.B. / e.g. | 例えば、たとえば |
| d.h. / i.e. | すなわち、つまり |
| u.a. / among others | ～など |
| etc. / usw. | など、等 |
| ggf. / if applicable | 必要に応じて、該当する場合 |
| bzgl. / regarding | ～について、～に関して |
| inkl. / including | ～を含む |
| exkl. / excluding | ～を除く |

### E. Punctuation [M]
| Element | Japanese Rule |
|---------|-------------|
| Period | 。(full-width) |
| Comma | 、(full-width) |
| Quotation marks | 「」(single) 『』(double/titles) |
| Parentheses | （）(full-width) or () (half-width for numbers) |
| Colon | ：(full-width) or none (restructure sentence) |
| Question mark | ？(full-width, use sparingly in formal text) |

**Spacing Rule:**
- NO spaces between Japanese characters
- Space before/after Latin text blocks (optional)

---

## Segmentation [M]

- No spaces between Japanese words (standard)
- Line breaks: avoid breaking within words or particles
- Use full-width punctuation in running text
- Half-width for numbers and Latin characters (recommended)

---

## Cultural Adaptation [M]

### Idioms and Metaphors [M]
- Do NOT translate literally
- Find equivalent Japanese expression OR rephrase neutrally

| German Idiom | NOT | INSTEAD |
|--------------|-----|---------|
| Das ist nicht mein Bier | それは私のビールではない | それは私には関係ありません |
| Ins Fettnäpfchen treten | 脂の小鍋に踏む | 失言をする / 地雷を踏む |

### Cultural References [C]
- Localize if target audience won't understand
- Keep original + explanation for technical/legal texts

**Example:**
> "...nach dem BGB" → "...ドイツ民法典（BGB）に基づき"

### Politeness Adaptations [M]
- Japanese business culture expects higher formality than Western equivalents
- Add appropriate keigo even when source is neutral

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
| Acronym without context | Keep original + katakana if pronounceable + [?] note |
| Missing reference | Flag with [要確認] |
| Ambiguous term | Translate most likely meaning, note in QA-Log |
| Corrupted text | Mark as [判読不能] |

### Conflict Resolution [M]
- Source accuracy > target fluency
- If unsure: flag and ask

---

## Output Specifications [M]

### Format [M]
- Match source document structure (headings, paragraphs, lists)
- Preserve formatting markers if present
- Clean text output (no translator notes inline)
- Use full-width punctuation for Japanese text

### File Naming [M]
```
{original_name}_{lang}.txt
```
Example: `agb_zeitreise_ja.txt`

---

## Quality Checklist [M]

Before delivery, verify ALL items:

- [ ] All content accurately translated [M]
- [ ] Technical terms consistent throughout [M]
- [ ] Natural Japanese flow (no "翻訳調") [M]
- [ ] Register and keigo appropriate [M]
- [ ] No information added or omitted [M]
- [ ] Grammar and particle usage correct [M]
- [ ] Numbers/dates in correct format [M]
- [ ] Glossary terms applied (if provided) [M]
- [ ] Cultural references appropriately handled [C]
- [ ] Full-width/half-width characters used correctly [M]

---

## QA-Log Section [C]

For complex translations, append at the end:

```
---
### QA-Log (自動生成)

**Technical Terms / 専門用語:**
- [Source term] → [日本語訳]

**Abbreviations Expanded / 略語展開:**
- [Source] → [展開形]

**Cultural Adaptations / 文化的調整:**
- [Original reference] → [日本語版]

**Flagged Items / 確認事項:**
- [Any ambiguities or issues noted]
```

---

## Disclaimer [M]

This directive provides professional translation guidelines.
All rules and examples are original formulations.
Inspired by: ISO 17100 Translation Services, JTF Translation Guidelines.

---

**[END OF DIRECTIVE]**
