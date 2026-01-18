# Directive: French Plain Language (Langage Clair)

**ID:** `langage-clair-business`
**Target Audience:** People with reading difficulties, French as second language, or readers who want to grasp information quickly (scanning).
**Level:** A2/B1 (Fluent and comprehensible text).

---

## 1. Core Principles
Unlike FALC, **flowing prose is allowed** here. The text appears more professional and adult, but remains maximally comprehensible.

### When to Use?
* For company-wide agreements for all employees.
* For emails, intranet news, or training for mixed teams.
* When FALC would be perceived as "too childish".

---

## 2. Language Rules

### A. Sentence Structure and Grammar
* **Sentence length:** Average 15 words. Maximum 20.
* **Subordinate clauses:** Allowed, but maximum one per sentence (no nested sentences).
    * *Good:* "Contactez-nous si vous avez des questions."
    * *Bad:* "Contactez-nous si vous avez des questions qui concernent le projet que nous avons lancé hier et qui implique plusieurs départements."
* **Passive voice:** Use sparingly. Active voice is always better.
    * *Acceptable:* "Le dossier est en cours de traitement."
    * *Better:* "Nous traitons votre dossier."

### B. Technical Terms and Legal Aspects (Business Context)
The strict Hybrid Rule from FALC ("Cela signifie :") does not apply here.
* **Technical terms:** May be used.
* **Explanation:** Explain difficult terms casually in context or in a subordinate clause.
* **Example:** "Respectez les règles de compliance, c'est-à-dire nos règles pour un comportement éthique dans l'entreprise."

---

## 3. Edge Cases and Formatting

### A. Anglicisms
In business contexts, common Anglicisms are acceptable in Plain Language if established.
* *Acceptable:* meeting, feedback, e-mail, deadline.
* *Avoid:* "challenger le process", "montrer du commitment". -> *Better:* "remettre en question le processus", "tenir son engagement".

### B. Abbreviations
Common abbreviations (ex., etc., Dr., M., Mme) are allowed.
Unknown or internal abbreviations (e.g., "conf. art. 5 C. trav.") must be written out or explained on first occurrence.

### C. Long Words
No systematic splitting needed, but recommended for words over 20 letters.
* *Acceptable:* Responsabilité
* *Better for very long:* Représentant-du-personnel (if really necessary)

### D. Inclusive Writing
Use neutral formulations or double form. No special characters (·, /) as they disrupt reading.
* *Good:* "Tous les employés", "Le personnel", "Les collaborateurs et collaboratrices".

### E. Formatting
* Use subheadings to structure text.
* Important information can be marked in **bold**.
* Use bullet lists for 3 or more points.

---

## 4. Examples (Comparison)

### Example 1: Legal Notice
**Original:**
"Tout manquement aux règles de sécurité peut entraîner des sanctions disciplinaires."

**Plain Language (B1):**
"Si vous ne respectez pas les règles de sécurité, il y aura des conséquences disciplinaires. Dans le pire des cas, vous pouvez recevoir un avertissement ou être licencié."

**(Comparison FALC A2 - for information only):**
"Respectez les règles.
Si vous ne le faites pas :
Vous aurez des problèmes."

### Example 2: IT Instruction
**Original:**
"Après authentification réussie dans le backend, le jeu de données doit être validé."

**Plain Language (B1):**
"Connectez-vous au système. Ensuite, vérifiez que les données sont correctes."

---

## 5. Checklist before Delivery

1.  [ ] Is the tone respectful and adult (not childish)?
2.  [ ] Have nested sentences been eliminated?
3.  [ ] Have internal technical terms been briefly explained (without interrupting reading flow)?
4.  [ ] Is the text visually structured (paragraphs, headings)?

---

## 6. Documentation & QA Log

Add at the **very end** of every translated file a brief QA appendix.
This is shorter than for FALC since rules are less strict.

**Format:**

```markdown
---

### QA-Log

**Technical terms used:**
- [Short list of main technical terms in the text]

**Language Level Check:**
- Nested sentences avoided: [Yes/No]
- Average sentence length: [approx. X words]
```

**Example:**
```markdown
---

### QA-Log

**Technical terms used:**
- Utilisabilité, Expérience utilisateur, Efficacité, Efficience, Satisfaction, Contexte d'utilisation

**Language Level Check:**
- Nested sentences avoided: Yes
- Average sentence length: approx. 14 words
```

---

**Note:** This directive was created independently.
Inspired by: Plain Language principles (Langage Clair)
No content was copied. All rules and examples are original formulations.
