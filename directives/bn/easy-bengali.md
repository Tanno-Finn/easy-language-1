# Directive: Easy Bengali (সহজ বাংলা) - Cognitive Accessibility

## Basis [M]
**Type:** Adapted Standard
**Framework:** Based on general accessibility principles and Bengali linguistic structure
**Origin:** Bangladesh/India (West Bengal)
**Speakers:** ~270 million native speakers

---

## Purpose [M]
Defines rules for translating texts into Easy Bengali while maintaining legal accuracy (Hybrid Approach).

**Priority:** Legal correctness over maximum simplification. [M]

## When to Use [M]
- For texts targeting people with learning disabilities [M]
- For legally relevant documents (contracts, policies, guidelines) [M]
- When maximum accessibility is required
- For readers with limited literacy

---

## Key Requirements [M]

### The Hybrid Rule (Supreme Directive) [M]
Because texts may have legal relevance, **technical terms are preserved** and explained.

#### 1. Glossary Priority [M]
If the glossary (input files) contains not just the term but also an explanation:
**You MUST use this explanation word-for-word.**
Do not invent new explanations when a definition exists.

#### 2. The "That means" Anchor [M]
Use **exclusively** the phrase **"এর মানে হলো:"** (Er mane holo:) for explanations.

Alternative accepted: **"অর্থাৎ:"** (Orthaat:)

#### 3. Anti-Doubling (CRITICAL) [M]
If the original sentence contains words before the technical term like "মানে হলো", "বোঝায়", "হলো" -> **DELETE these words** before adding "এর মানে হলো:".

#### 4. Hard Line Break (Mandatory) [M]
Every explanation needs **three separate paragraphs**:
1. Technical term (**bold**) + full stop (।)
2. New paragraph -> "এর মানে হলো:" (alone)
3. New paragraph -> Explanation

**Correct Format:**
> **দক্ষতা**।
>
> এর মানে হলো:
>
> কোনো লক্ষ্য অর্জনে কতটা সম্পদ প্রয়োজন।

### Grammar & Sentence Structure [M]
- **One sentence = One idea** [M]
- **SOV order** (Subject - Object - Verb) - Bengali's natural order [M]
- **Active voice only** (কর্তৃবাচ্য) [M]
- **Positive statements** [C]
- Avoid complex verb forms (causatives, conjunct verbs)

### Bengali-Specific Rules [M]
- **Script:** Use standard Bengali script (বাংলা লিপি)
- **Avoid Sanskritic/Tatsama words** - prefer colloquial (চলিত) forms
- **Avoid Persian/Arabic loanwords** when Bengali alternatives exist
- **Use simple postpositions** (avoid compound postpositions)

### Formatting [M]
- Every sentence starts on a **new line** [M]
- Use many paragraphs [M]
- Use Bengali punctuation: দাঁড়ি (।) for full stop

---

## Edge Cases & Special Rules [M]

### A. Complex Words [M]
Avoid complex/formal words. Examples:
- Use "শুরু" not "আরম্ভ" (start)
- Use "শেষ" not "সমাপ্তি" (end)
- Use "সাহায্য" not "সহায়তা" (help)

### B. Abbreviations [M]
**Always write them out** in Bengali:
- "যেমন" instead of "য."
- "এবং" instead of "ও" when clarity needed

### C. Compound Words (সমাস) [M]
Break compound words for clarity. Use hyphens (হাইফেন) if needed:
- "জন-স্বাস্থ্য" (public health)
- "কর্ম-স্থল" (workplace)

### D. Metaphors [M]
Avoid figurative language and idioms (প্রবাদ).

### E. Numbers and Dates [M]
- Write numbers as **Bengali digits** (১, ২, ৩) or international digits (1, 2, 3) consistently
- Write dates in full: ১ এপ্রিল ২০২৪

### F. Honorifics [M]
Use neutral forms. Avoid complex honorific verb endings.

---

## Documentation & QA Log [M]
Add a QA appendix at the **very end** of every translated file:

### QA Log (Auto-generated)
**Preserved Technical Terms:**
- [List terms with Bengali explanations]
**Expanded Abbreviations:**
- [List expansions]
**Script Check:**
- Bengali script used: [Yes/No]
- Colloquial forms preferred: [Yes/No]

---

**Note:** This directive was created independently.
Inspired by: General accessibility principles, Inclusion Europe Easy-to-Read Guidelines (adapted for Bengali)
No content was copied. All rules and examples are original formulations.
