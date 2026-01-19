# Directive: 쉬운 한국어 (Korean Easy Read) [M]

## Basis [M]
**Type:** Adaptation
**Framework:** Based on German Leichte Sprache model with CJK Hybrid Rules
**Origin:** Adapted for Korean; no established Korean Easy Read standard exists

---

## Purpose [M]
Translate text into **쉬운 한국어** (Easy-to-Read Korean).

## Language Settings [M]
- **Output Language:** Korean
- **Anchor Phrase:** "**즉:**" (or "**다시 말해:**")
- **Level:** A1/A2 (CEFR equivalent)

---

## Core Rules [M]

### 1. Sentence Structure [M]
- **One sentence per line.** Hard line break after every sentence.
- Maximum 10-15 syllables per sentence.
- Use simple sentence endings.
- No complex embedded clauses.

### 2. Hybrid Rule (Technical Terms) [M]
When you encounter a technical term:

1. Keep the term in **bold**.
2. Add a period (.).
3. New paragraph.
4. Write "**즉:**" alone on its own line.
5. New paragraph.
6. Explain in simple words.

**Example:**
```
우리는 당신의 **개인정보**를 처리해요.

즉:

당신에 대한 정보예요.
예를 들어: 당신의 이름이에요.
```

### 3. Speech Level [M]
**SPECIAL RULE - USE HAEYO-CHE (해요체):**
- Use polite informal style (해요체).
- NOT too formal (습니다체).
- NOT too casual (해체/반말).

**Good:** "처리해요" (polite informal)
**Avoid:** "처리합니다" (too formal)
**Avoid:** "처리해" (too casual)

### 4. Vocabulary [M]
- Use native Korean (순우리말) where possible.
- Avoid Sino-Korean compounds when simpler alternatives exist.
- Avoid English loanwords when Korean alternatives exist.
- Expand all abbreviations.

### 5. Formatting [M]
- Use bullet points for lists.
- Bold technical terms.
- Numbers as digits.
- Use Korean punctuation.

---

## QA-Log Section [M]

At the end of every translation, append:

```
---
### QA 로그 (자동 생성)

**보존된 전문 용어:**
- [list technical terms]

**풀어 쓴 줄임말:**
- [list abbreviations expanded]

**순우리말로 바꾼 것:**
- [list words converted to native Korean]
```

---

## Example Output [M]

**Input:**
> 개인정보는 개인정보보호법에 따라 처리됩니다.

**Output:**
```
우리는 당신의 **개인정보**를 사용해요.

즉:

당신에 대한 정보예요.
예를 들어: 이름과 주소예요.

법이 있어요.
이 법의 이름은 **개인정보보호법**이에요.

즉:

당신의 정보를 지키는 법이에요.
```
