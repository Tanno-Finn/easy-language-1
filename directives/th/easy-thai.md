# Directive: Thai Easy Language (ภาษาไทยอ่านง่าย)

## Basis [M]
**Type:** Adapted Standard
**Framework:** Based on general Easy-to-Read principles adapted for Thai
**Origin:** Thailand

---

## Purpose [M]
Defines rules for translating texts into Thai Easy Language while maintaining accuracy (Hybrid Approach).
**Priority:** Accuracy over maximum simplification. [M]

## Key Requirements [M]

### The Hybrid Rule [M]
Because texts may have legal or official relevance, **technical terms are preserved** and explained.

#### 1. Glossary Priority [M]
If the glossary contains an explanation: **You MUST use this explanation word-for-word.**

#### 2. The Anchor Phrase [M]
Use **exclusively** the Thai phrase: **"หมายความว่า:"** (That means).

#### 3. Anti-Doubling [M]
If the original sentence contains words like "หมายถึง", "คือ", "แปลว่า" -> **DELETE these words** before adding "หมายความว่า:".

#### 4. Hard Line Break (Mandatory) [M]
Format:
1. Technical term (**bold**) + full stop.
2. New paragraph -> "หมายความว่า:" (alone).
3. New paragraph -> Explanation.

**Correct Example:**
> **ประสิทธิภาพ**.
>
> หมายความว่า:
>
> การใช้ทรัพยากรน้อยที่สุดเพื่อให้ได้ผลลัพธ์ที่ต้องการ

---

## Thai-Specific Rules [M]

### Word Segmentation [M]
Thai script has **no spaces between words**. For Easy Thai:
- **Add spaces between phrases** to improve readability [M]
- Use spaces to separate distinct concepts
- Keep common compound words together

**Example:**
> Standard: วันนี้อากาศดีมากครับ
> Easy Thai: วันนี้ อากาศดีมาก ครับ

### Sentence Structure [M]
- **One sentence = One idea** [M]
- **SVO order preferred** (Subject - Verb - Object) [M]
- **Keep sentences short** (ideally under 15 words) [M]
- **Active voice only** [M]

### Particles & Politeness [M]
- Use polite particles (ครับ/ค่ะ) at sentence end for formal texts
- Avoid stacking multiple particles
- Keep one particle per sentence maximum

### Vocabulary [M]
- Prefer common Thai words over formal/royal vocabulary
- Avoid Pali-Sanskrit loanwords when simple Thai alternatives exist
- Explain all technical terms using the Hybrid Rule

**Example:**
> Formal: กรุณารอสักครู่
> Easy Thai: รอ สักครู่ นะครับ

### Numbers & Dates [M]
- Use Thai numerals (๑, ๒, ๓) or Arabic numerals (1, 2, 3) consistently
- Write dates in full: วันที่ 15 มกราคม 2567
- Explain Buddhist Era (พ.ศ.) if used

---

## Grammar & Clarity [M]

### Avoid [M]
- Long, nested sentences
- Passive constructions (ถูก...โดย)
- Double negatives
- Formal/royal vocabulary (ราชาศัพท์) unless required
- Abbreviated forms without explanation

### Prefer [M]
- Short, direct sentences
- Active voice
- Common everyday vocabulary
- Clear subject-verb-object order
- Explicit subjects (don't drop pronouns)

---

## Documentation & QA Log [M]
Add a QA appendix at the **very end** of every translated file:

### บันทึก QA (สร้างอัตโนมัติ)
**คำศัพท์เทคนิคที่คงไว้:**
- [List terms]
**คำย่อที่ขยายความ:**
- [List expansions]
**การแบ่งวรรคที่เพิ่ม:**
- [List segmentation changes]

---

**Note:** This directive was created independently.
Inspired by: General Easy-to-Read principles and Thai language accessibility guidelines.
No content was copied. All rules and examples are original formulations.
