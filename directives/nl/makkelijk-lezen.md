# Directive: Dutch Easy Read (Makkelijk Lezen) [M]

## Purpose [M]
Defines rules for translating texts into Dutch Easy Read while maintaining legal accuracy (Hybrid Approach).
**Priority:** Legal correctness over maximum simplification. [M]

## Key Requirements [M]

### The Hybrid Rule [M]
Because texts may have legal relevance, **technical terms are preserved** and explained.

#### 1. Glossary Priority [M]
If the glossary contains an explanation: **You MUST use this explanation word-for-word.**

#### 2. The Anchor Phrase [M]
Use **exclusively** the Dutch phrase: **"Dat betekent:"** (That means).

#### 3. Anti-Doubling [M]
If the original sentence contains words like "betekent:", "wil zeggen:", "is:" -> **DELETE these words** before adding "Dat betekent:".

#### 4. Hard Line Break (Mandatory) [M]
Format:
1. Technical term (**bold**) + full stop.
2. New paragraph -> "Dat betekent:" (alone).
3. New paragraph -> Explanation.

**Correct Example:**
> **Efficiëntie**.
>
> Dat betekent:
>
> Hoeveel middelen je nodig hebt om een doel te bereiken.

### Grammar & Sentence Structure [M]
- **One sentence = One idea** [M]
- **SVO order** (Subject - Verb - Object) [M]
- **Active voice only** [M]
- **Compounds:** Split long Dutch compound words with hyphens (e.g., "gebruikers-interface") [M]

---

## Documentation & QA Log [M]
Add a QA appendix at the **very end** of every translated file:

### QA-Log (Automatisch gegenereerd)
**Behouden vaktermen:**
- [List terms]
**Uitgeschreven afkortingen:**
- [List expansions]
**Gesplitste samenstellingen:**
- [List hyphenated words]

---

**Note:** This directive was created independently.
Inspired by: Makkelijk Lezen principles (Dutch Easy Read).
No content was copied. All rules and examples are original formulations.
