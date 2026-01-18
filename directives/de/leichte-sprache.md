# Directive: German Easy Language (Leichte Sprache)

## Purpose [M]
Defines rules for translating texts into German Easy Language (Leichte Sprache) while maintaining legal accuracy (Hybrid Approach).
**Priority:** Legal correctness over maximum simplification. [M]

## Key Requirements [M]

### The Hybrid Rule [M]
Because texts may have legal relevance, **technical terms are preserved** and explained.

#### 1. Glossary Priority [M]
If the glossary contains an explanation: **You MUST use this explanation word-for-word.**

#### 2. The Anchor Phrase [M]
Use **exclusively** the German phrase: **"Das heißt:"** (That means).

#### 3. Anti-Doubling [M]
If the original sentence contains words like "bedeutet:", "heißt:", "ist:" -> **DELETE these words** before adding "Das heißt:".

#### 4. Hard Line Break (Mandatory) [M]
Format:
1. Technical term (**bold**) + full stop.
2. New paragraph -> "Das heißt:" (alone).
3. New paragraph -> Explanation.

**Correct Example:**
> **Effizienz**.
>
> Das heißt:
>
> Wie viele Mittel man braucht, um ein Ziel zu erreichen.

### Grammar & Sentence Structure [M]
- **One sentence = One idea** [M]
- **SVO order** (Subject - Verb - Object) [M]
- **No Genitive:** Use "von" instead (e.g., "Das Haus von dem Vater") [M]
- **Active voice only** [M]
- **Compounds:** Split long words with hyphens (e.g., "Benutzungs-Schnittstelle") [M]

---

## Documentation & QA Log [M]
Add a QA appendix at the **very end** of every translated file:

### QA-Log (Automatisch generiert)
**Beibehaltene Fachbegriffe:**
- [List terms]
**Aufgelöste Abkürzungen:**
- [List expansions]
**Getrennte Komposita:**
- [List hyphenated words]
