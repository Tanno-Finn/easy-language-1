# New Language Protocol [M]

**This is a generator directive.** Use it when a requested language has no directive yet.

---

## License & Plagiarism Protection [M]

### NEVER copy [M]
- **No Copy & Paste** from external documents, websites, or standards
- Formulate rules and principles **in your own words**
- **Invent examples yourself**, do not take them from sources

### Source Attribution [M]
- Mention researched standards as **inspiration**, not as quoted sources
- Format: "Inspired by: [Name of Standard]"
- **No URLs** to protected documents

### What is allowed [C]
- General linguistic principles (e.g., "short sentences", "active voice")
- Publicly known language level definitions (A1, A2, B1, B2)
- Own formulations based on **general knowledge**

### What is NOT allowed [M]
- Literal adoption of rule formulations
- Copying example sentences from standards
- Adoption of specific checklists or tables
- Embedding protected logos or trademarks

---

## The 4-Step Protocol [M]

### Step 1: Research (Mandatory)
Search for official "Easy-to-Read" and "Plain Language" standards for the target language.

**Research for orientation only:**
- What principles apply in this language?
- What grammatical peculiarities exist?
- How is "Das heißt:" (That means:) expressed in this language?

**Known Standards (reference only):**
- French: FALC (Facile à Lire et à Comprendre)
- Spanish: Lectura Fácil
- Italian: Linguaggio Facile da Leggere
- Japanese: やさしい日本語 (Yasashii Nihongo)

### Step 2: Adaptation
Create TWO files in `directives/[lang]/`:
1. Easy Read equivalent (Strict rules, Hybrid Rule, "That means" anchor translated).
2. Plain Language equivalent (Moderate rules).

**CRITICAL RULE: English Shell** [M]
Write the directive instructions in **English**.
Only the following elements should be in the target language:
- Examples and sample texts
- Anchor phrases (e.g., "Das heißt:", "つまり:", "Eso significa:")
- Specific grammar terms and references
- QA-Log field labels (optional, can be English)

**Create original content:**
- Formulate rules yourself
- Invent examples yourself
- Build tables yourself

### Step 3: Fallback (If No Standards Found)
Use `directives/de/leichte-sprache.md` or `directives/en/easy-read.md` as a template.
- Adapt SVO/Grammar rules to target language.
- Translate "That means:" anchor (e.g., "Eso significa:", "Cela signifie :", "つまり:").
- **Keep all [M] markers.**

### Step 4: Quality Gate
Check:
- [ ] Hybrid Rule preserved?
- [ ] "That means" anchor on separate line?
- [ ] QA Log format included?
- [ ] **No copied texts?** [M]
- [ ] **Examples invented yourself?** [M]
- [ ] **Inspiration source mentioned?** [M]
- [ ] **Instructions written in English?** [M]

---

## Disclaimer Template [M]

Every newly created directive must include this notice at the end:

```markdown
---
**Note:** This directive was created independently.
Inspired by: [Name of Standard/Guideline]
No content was copied. All rules and examples are original formulations.
```
