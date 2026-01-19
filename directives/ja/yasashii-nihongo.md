# Directive: やさしい日本語 (Yasashii Nihongo / Easy Japanese) [M]

## Basis [M]
**Type:** National Standard
**Framework:** やさしい日本語 (Yasashii Nihongo) - NHK/Government guidelines
**Origin:** Japan (developed post-1995 Kobe earthquake for disaster communication)

---

## Purpose [M]
Defines rules for translating texts into やさしい日本語 (Easy Japanese).
Goal: Make texts accessible for people with limited Japanese skills.

**Priority:** Comprehensibility while preserving all important information. [M]

## When to Use [M]
- Texts for non-native speakers [M]
- Official information and notices [M]
- Texts for people with learning difficulties [M]

---

## Key Requirements [M]

### The Hybrid Rule (Supreme Principle) [M]
Technical terms are **preserved** and explained.
Never delete technical terms or replace them with imprecise words.

#### 1. Glossary Priority [M]
If the glossary contains an explanation for a term:
**Use this explanation word-for-word.**

#### 2. The "Tsumari" Anchor (つまり) [M]
Use **exclusively** the phrase: **つまり：**

This phrase always stands alone on a line.
Do not use alternatives.

#### 3. Hard Line Break (Mandatory) [M]
Every explanation requires **three separate paragraphs**:

1. Write the technical term (**bold**) with period。
2. Make a **new paragraph**.
3. Write "つまり：" alone on a line.
4. Make a **new paragraph**.
5. Write the explanation.

**Correct Format:**
```
**コンプライアンス**。

つまり：

会社の ルールを まもること。
```

---

## Writing System Rules [M]

### Kanji Usage [M]
- Use only simple Kanji (elementary school level) [M]
- Write difficult Kanji in Hiragana or provide Furigana [M]
- When possible: prefer Hiragana [M]

| Difficult | Simple |
|-----------|--------|
| 購入 | 買う / かう |
| 従業員 | はたらく 人 |
| 必要 | いる / ひつよう |
| 締切 | しめきり |

### Katakana [M]
- Foreign words in Katakana with explanation [M]
- If a Japanese word exists: prefer it [C]

| Katakana | Add explanation |
|----------|-----------------|
| インターネット | インターネット（ネットの こと） |
| コンピューター | コンピューター（パソコンの こと） |

---

## Grammar & Sentence Structure [M]

### Sentence Structure [M]
- **One sentence = One statement** [M]
- **Short sentences**: Maximum 15-20 morae [M]
- **Simple structure**: Subject + Object + Verb [M]

### Verb Forms [M]
- Use **です/ます form** (polite but simple) [M]
- **No Keigo** (複雑な敬語): No complex honorific forms [M]
- **No Passive**: Prefer active sentences [M]

| Passive (avoid) | Active (correct) |
|-----------------|------------------|
| 会議が 開かれます | 会議を します |
| 書類が 送られました | 書類を おくりました |

### Conjunctions [M]
Use simple conjunctions:

| Complex | Simple |
|---------|--------|
| したがって | だから |
| および | と |
| または | か |
| なぜなら | ～から |

---

## Formatting [M]

### Word Spacing (分かち書き) [M]
Separate words with spaces for better readability:

| Without spacing | With spacing |
|-----------------|--------------|
| 今日会議があります | 今日 会議が あります |
| 申請書を提出してください | 申請書を 出して ください |

### Paragraphs [M]
- Each sentence on a **new line** [M]
- Use many paragraphs [M]
- Use bullet lists instead of commas [C]

### Numbers and Dates [M]
- Use Arabic numerals [M]
- Write dates clearly [M]

| Complex | Simple |
|---------|--------|
| 令和六年四月一日 | 2024年 4月 1日 |
| 三千円 | 3,000円 |
| 午後三時半 | 15時 30分 |

---

## What to Avoid [M]

### Complex Expressions [M]
- Avoid idioms and proverbs [M]
- Make abstract expressions concrete [M]

| Avoid | Better |
|-------|--------|
| 一石二鳥 | 2つの いい ことが ある |
| 猫の手も借りたい | とても いそがしい |
| 検討する | よく かんがえる |

### Abbreviations [M]
Expand all abbreviations:

| Abbreviation | Expanded |
|--------------|----------|
| 等 | など |
| 及び | と / および |
| 〒 | 郵便番号（ゆうびんばんごう） |

---

## Anti-Patterns [M]

### What NOT to do:
- Delete technical terms or replace with wrong words [M]
- Use difficult Kanji without explanation [M]
- Write long nested sentences [M]
- Use Keigo (complex honorific forms) [M]
- Use passive constructions [M]
- Use idioms and proverbs [M]
- Leave abbreviations unexpanded [M]
- **Put explanation on same line** as "つまり：" [M]

---

## Success Criteria [M]

### Quality Checklist:
- [ ] All technical terms still present [M]
- [ ] All technical terms explained (Hybrid Rule) [M]
- [ ] **"つまり：" stands alone on a line** [M]
- [ ] **Explanation stands on separate line** [M]
- [ ] Short sentences (max. 15-20 morae) [M]
- [ ] Simple Kanji or Hiragana [M]
- [ ] Word spacing used [M]
- [ ] No Keigo [M]
- [ ] No Passive [M]
- [ ] No idioms [M]
- [ ] Abbreviations expanded [M]

---

## Documentation & QA Log [M]

Add a QA appendix at the end of every translated file:

```markdown
---

### QA-Log (自動生成)

**Preserved technical terms:**
- [List of all technical terms]

**Converted to Hiragana:**
- [List of simplified Kanji]

**Explained foreign words:**
- [List of Katakana words with explanation]
```

---

**Note:** This directive was created independently.
Inspired by: やさしい日本語 concept (developed for disaster communication and non-native speakers).
No content was copied. All rules and examples are original formulations.
