# Directive: Quality Assurance for Language Directives [M]

## Purpose [M]
Perform a **forensic quality review** of a language directive to ensure it meets the highest standards of consistency, completeness, and linguistic accuracy.

---

## Review Checklist [M]

### 1. Structure Compliance ✓

- [ ] **English Shell Pattern:** Instructions are in English
- [ ] **Native Content:** Examples and anchor phrases are in the target language
- [ ] **Section Headers Present:**
  - [ ] Purpose
  - [ ] Language Settings
  - [ ] Core Rules
  - [ ] Hybrid Rule (Technical Terms)
  - [ ] QA-Log Section
  - [ ] Example Output

### 2. Anchor Phrase Verification ✓

- [ ] **Anchor phrase is defined** in Language Settings section
- [ ] **Anchor phrase is grammatically correct** in the target language
- [ ] **Anchor phrase matches cultural conventions** (e.g., French space before colon)
- [ ] **Anchor phrase is used consistently** in all examples

| Language | Expected Anchor | Verified |
|----------|-----------------|----------|
| DE | "Das heißt:" | [ ] |
| EN | "That means:" | [ ] |
| ES | "Eso significa:" | [ ] |
| FR | "Cela signifie :" | [ ] |
| IT | "Questo significa:" | [ ] |
| NL | "Dat betekent:" | [ ] |
| JA | "つまり：" | [ ] |
| PT | "Isto significa:" | [ ] |
| PL | "To znaczy:" | [ ] |
| RU | "Это значит:" | [ ] |
| SV | "Det betyder:" | [ ] |
| ZH | "意思是：" | [ ] |
| KO | "즉:" | [ ] |
| AR | "وهذا يعني:" | [ ] |
| CS | "To znamená:" | [ ] |

### 3. Hybrid Rule Format ✓

The directive MUST specify this exact format:
```
1. Technical term in **bold**
2. Period after term
3. New paragraph (blank line)
4. Anchor phrase ALONE on its own line
5. New paragraph (blank line)
6. Simple explanation
```

- [ ] Format is explicitly documented
- [ ] Example demonstrates the format correctly
- [ ] No variations or shortcuts allowed

### 4. Language-Specific Rules ✓

- [ ] **Special rules are documented** (if applicable)
- [ ] **Grammar restrictions are appropriate** for the target language
- [ ] **Vocabulary guidance is realistic** (not overly restrictive)

**Known Special Rules to Verify:**
| Language | Special Rule | Present |
|----------|--------------|---------|
| PL | Declension handling (SVO order) | [ ] |
| RU | No participle constructions | [ ] |
| AR | RTL formatting mandatory | [ ] |
| ZH | No Chengyu (4-char idioms) | [ ] |
| KO | Haeyo-che speech level | [ ] |
| SV | Lättläst principles | [ ] |
| JA | Word spacing (分かち書き) | [ ] |

### 5. QA-Log Template ✓

- [ ] QA-Log section exists at bottom of directive
- [ ] Template includes:
  - [ ] Preserved technical terms
  - [ ] Expanded abbreviations
  - [ ] Language-specific items (compounds, pinyin, etc.)
- [ ] QA-Log labels are in the **target language**

### 6. Example Quality ✓

- [ ] Example input is realistic (legal/technical text)
- [ ] Example output demonstrates ALL rules correctly
- [ ] Example shows the Hybrid Rule in action
- [ ] Example is in the **correct target language** (no copy-paste errors)

### 7. Cross-Directive Consistency ✓

Compare with reference directive (`directives/de/leichte-sprache.md`):
- [ ] Same section order
- [ ] Same rule numbering
- [ ] Same level of detail
- [ ] Same [M] markers for mandatory sections

---

## Output Format [M]

Create a review report with this structure:

```markdown
# Directive Review: [filename]

**Language:** [language name]
**Reviewer:** [Worker ID]
**Date:** [date]

## Verdict: [PASS / FAIL / NEEDS REVISION]

## Checklist Results

### 1. Structure Compliance
- [x] or [ ] for each item

### 2. Anchor Phrase
- Defined: [YES/NO]
- Correct: [YES/NO]
- Phrase: "[actual phrase]"

### 3. Hybrid Rule Format
- [x] or [ ] for each item

### 4. Language-Specific Rules
- [x] or [ ] with notes

### 5. QA-Log Template
- [x] or [ ] for each item

### 6. Example Quality
- [x] or [ ] for each item

### 7. Cross-Directive Consistency
- [x] or [ ] for each item

## Issues Found

[List specific issues with line numbers if applicable]

## Recommendations

[List specific fixes needed, or "None - ready for production"]

## Final Status

[ ] APPROVED FOR PRODUCTION
[ ] REQUIRES FIXES (see above)
```

---

## Severity Levels [M]

| Level | Description | Action |
|-------|-------------|--------|
| **CRITICAL** | Wrong anchor phrase, wrong language, missing Hybrid Rule | FAIL - Must fix |
| **MAJOR** | Missing sections, inconsistent formatting | FAIL - Must fix |
| **MINOR** | Typos, suboptimal examples | PASS with notes |
| **STYLE** | Formatting preferences | PASS |

---

## Review Process [M]

1. **Read the directive completely** before checking anything
2. **Compare with DE reference** (`directives/de/leichte-sprache.md`)
3. **Verify native language content** is actually in the correct language
4. **Check all examples** for copy-paste errors
5. **Document everything** - be thorough

**CRITICAL:** If you are not fluent in the target language, flag this in your review. Linguistic accuracy requires native-level verification.
