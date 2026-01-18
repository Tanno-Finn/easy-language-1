# Directive: Quality Assurance Review [M]

## Purpose [M]
Review a translated file to ensure strict adherence to accessibility standards.

## Checklist [M]

### 1. Structure Check
- [ ] Is the "Anchor Phrase" present? (e.g. "Das heißt:", "That means:", "つまり：")
- [ ] Is the Anchor Phrase on its own separate line?
- [ ] Is the Explanation on a separate line below the Anchor?

### 2. Content Check
- [ ] Are technical terms preserved (not translated/deleted)?
- [ ] Is the QA-Log present at the very bottom?

### 3. Hallucination Check
- [ ] Does the translation contain facts not present in the source? (If yes -> FAIL)

## Output Format [M]
Create a new file `[filename]_REVIEW.md` containing:
1. **Pass/Fail** Verdict.
2. List of specific errors found (if any).
3. If Pass: "READY FOR PUBLICATION".
