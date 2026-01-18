# Directive: French Easy Read (FALC - Facile à Lire et à Comprendre) [M]

## Purpose [M]
Defines rules for translating technical texts into French Easy Read (FALC) while maintaining legal accuracy (Hybrid Approach).

**Priority:** Legal correctness over maximum simplification. [M]

## When to Use [M]
- For all translations of technical texts to FALC [M]
- For legally relevant texts (contracts, training, regulations) [M]
- Target audience: people with reading difficulties or limited language skills

---

## Key Requirements [M]

### The Hybrid Rule (Supreme Principle) [M]
Because texts have legal relevance, **technical terms are preserved** and explained.

#### 1. Glossary Priority [M]
If the glossary (input files) contains not only the term but also an explanation:
**You MUST use that explanation word-for-word.**
Do not invent anything new if a definition exists.

#### 2. The "Cela signifie" Anchor [M]
Use **exclusively** the phrase: **"Cela signifie :"** (That means:)
No alternatives like "C'est-à-dire :", "Autrement dit :" or "Ça veut dire :".

#### 3. Anti-Doubling (CRITICAL) [M]
If the original sentence before the technical term contains words like:
- "signifie :"
- "veut dire :"
- "est :"
- "désigne :"
- "comprend :"

**DELETE these words** before adding "Cela signifie :".
Otherwise duplications arise like "signifie : Cela signifie :".

| INCORRECT | CORRECT |
|-----------|---------|
| "L'efficacité signifie : Cela signifie : Comment on atteint son but." | See correct format below |

#### 4. Hard Line Break (Mandatory) [M]
Every explanation requires **three separate paragraphs**:

1. Write the technical term (**bold**) with period.
2. Make a **new paragraph**.
3. Write "Cela signifie :" (no text after it).
4. Make a **new paragraph**.
5. Write the explanation.

**Correct Format:**
```
**Efficacité**.

Cela signifie :

Le nombre de moyens nécessaires pour atteindre un objectif.
```

#### 5. Format on First Occurrence [M]
1. Use the correct technical term on its first occurrence [M]
2. Highlight technical term in **bold** [M]
3. Add a period after the technical term [M]
4. New paragraph [M]
5. Write "Cela signifie :" alone on a line [M]
6. New paragraph [M]
7. Write the explanation [M]

**INCORRECT Example:**
> L'efficience signifie : Cela signifie : Si on atteint son objectif.

**CORRECT Example:**
> **Efficience**.
>
> Cela signifie :
>
> Si on atteint son objectif avec peu de moyens.

### Grammar & Sentence Structure [M]
- **One sentence = One idea** [M]
- **SVO order**: Subject - Verb - Object (Who does what?) [M]
- **Avoid Passive**: Use active voice (Not: "Le dossier est examiné", But: "Nous examinons le dossier") [M]
- **Avoid Subjunctive**: Use indicative when possible [M]
- **Positive formulations**: Avoid negations when possible [C]

### Formatting [M]
- Each sentence starts on a **new line** [M]
- Use many paragraphs [M]
- Bullet lists instead of commas [C]

---

## Edge Cases & Special Rules [M]

### A. Anglicisms and Foreign Words [M]
Avoid English terms if a good French equivalent exists.
If the Anglicism is an established technical term, apply the Hybrid Rule.

| Incorrect | Correct |
|-----------|---------|
| "On fait un meeting" | "On fait une **réunion**" |
| "Checker ça" | "Vérifier ça" |
| "Le feedback" | "Le retour" or "Les commentaires" |

**Exception (company technical term):**
> Respectez la **compliance**.
>
> Cela signifie :
>
> Les règles pour bien se comporter dans l'entreprise.

### B. Abbreviations [M]
Abbreviations are major barriers. **Always expand them:**

| Abbreviation | Expanded |
|--------------|----------|
| etc. | et ainsi de suite |
| c.-à-d. | cela signifie |
| p. ex. | par exemple |
| env. | environ |
| art. | article |
| % | pour cent |
| & | et |
| € | euros |
| n° | numéro |

### C. Long Words (Compound Words) [M]
Split compound words with **hyphen** for better readability:

| Original | FALC |
|----------|------|
| Règlement intérieur | Règlement intérieur |
| Responsabilité | Responsabilité |
| Représentant du personnel | Représentant du personnel |

Note: In French, compound words are naturally shorter than in German. Only split if it helps readability.

### D. Metaphors and Idioms [M]
Avoid figurative language - it's often understood literally:

| Incorrect | Correct |
|-----------|---------|
| "Mettre la main à la pâte" | "Aider" |
| "C'est de l'eau sous les ponts" | "C'est du passé" |
| "Avoir le bras long" | "Avoir du pouvoir" |
| "Tourner autour du pot" | "Ne pas dire clairement" |

### E. Inclusive Writing [M]
Special characters (·, /, parentheses) disrupt reading and screen readers.
**Rule:** Use double form or neutral form:

| Incorrect | Correct |
|-----------|---------|
| Les salarié·es | Les salariés et les salariées |
| Les collaborateur/rice/s | Le personnel |

### F. Numbers and Dates [M]
- Numbers **always as digits** (also 1, 2, 3) - easier to grasp [M]
- Dates written out completely [M]

| Incorrect | Correct |
|-----------|---------|
| trois jours | 3 jours |
| 01/04/2024 | 1 avril 2024 |
| 15h30 | 15 heures 30 |

### G. References [C]
Avoid "voir plus haut" or "comme mentionné précédemment".
**Better:** Repeat the information briefly.

### H. URLs and Email Addresses [C]
- Simplify URLs when possible
- Write out and explain email addresses

> Vous pouvez nous écrire.
> Notre adresse e-mail est : info@entreprise.fr

### I. Lists and Enumerations [C]
- Maximum 5-7 points per list
- Each point as a complete thought
- For longer lists: divide into categories

---

## Examples for Difficult Cases [C]

### Anglicism in IT Text
**Original:** "L'utilisateur doit se connecter au frontend."

**Translation:**
> L'utilisateur doit se connecter.
> Il le fait sur le site internet.
> Les spécialistes appellent cela : **frontend**.
> Se connecter s'appelle aussi : **login**.

### Legal Abbreviation and Date
**Original:** "Conformément à l'art. 12 du Code civil, la règle entre en vigueur le 01/04/2024."

**Translation:**
> C'est écrit dans la loi.
> La loi s'appelle : Code civil.
>
> C'est écrit dans l'article 12.
>
> La règle s'applique à partir du 1 avril 2024.

### Data Protection Notice
**Original:** "Les données à caractère personnel sont traitées conformément au RGPD."

**Translation:**
> Nous enregistrons vos données.
> Par exemple : votre nom et votre adresse.
> On appelle cela : **données personnelles**.
>
> Nous suivons une loi.
> La loi s'appelle : **RGPD**.
>
> Cela signifie :
>
> Règlement Général sur la Protection des Données.
>
> Nous utilisons vos données uniquement pour un but précis.
> Par exemple : pour vous envoyer une lettre.

---

## Anti-Patterns [M]

### What NOT to do:
- Delete technical terms or replace with imprecise synonyms [M]
- Change legal meaning to simplify text [M]
- Omit or invent facts [M]
- Leave abbreviations unexpanded [M]
- Use passive constructions [M]
- Use inclusive writing with special characters (·, /) [M]
- Use metaphors and idioms [M]
- Long sentences with multiple ideas [M]
- **Double introductions** like "signifie : Cela signifie :" [M]
- **Explanation on same line** as "Cela signifie :" [M]

### Anti-Pattern Example:
| Incorrect | Why it's wrong |
|-----------|----------------|
| Replace "Avertissement" with "Problème avec le chef" | Legal meaning lost |
| Conditional: "Il se pourrait que..." | Too vague, better: "Peut-être que cela arrivera" |
| "L'efficacité signifie : Cela signifie : ..." | Double introduction - "signifie :" must be deleted |
| "Cela signifie : Comment c'est bien." | Explanation must be on new line |

---

## Success Criteria [M]

### Quality Checklist before Delivery:
- [ ] All legal technical terms still present [M]
- [ ] All technical terms explained (Hybrid Rule) [M]
- [ ] **No double introductions** (e.g., "signifie : Cela signifie :") [M]
- [ ] **"Cela signifie :" stands alone on a line** [M]
- [ ] **Explanation is on separate line after "Cela signifie :"** [M]
- [ ] Each sentence short (max. 10-15 words) [M]
- [ ] Abbreviations expanded [M]
- [ ] Metaphors removed [M]
- [ ] Anglicisms translated or explained [M]
- [ ] Passive constructions transformed to active [M]
- [ ] Numbers as digits, dates written out [M]
- [ ] No inclusive writing with special characters [M]

### Validation:
- Text maintains legal validity [M]
- Text is comprehensible for target audience [M]
- No information was lost [M]

---

## Documentation & QA Log [M]

Add at the **very end** of every translated file a QA appendix for the reviewer.
This appendix serves quality assurance and traceability.

**Format:**

```markdown
---

### QA-Log (Généré automatiquement)

**Preserved technical terms:**
- [List of all glossary words present in the text]

**Expanded abbreviations:**
- [List of abbreviations with expansion, e.g., "etc. -> et ainsi de suite"]

**Split compound words:**
- [List of long words split with hyphen]
```

**Example:**
```markdown
---

### QA-Log (Généré automatiquement)

**Preserved technical terms:**
- Utilisabilité, Efficacité, Efficience, Satisfaction, Expérience utilisateur, Contexte d'utilisation

**Expanded abbreviations:**
- etc. -> et ainsi de suite
- p. ex. -> par exemple
- UX -> Expérience utilisateur (written out on first mention)

**Split compound words:**
- Interface-utilisateur, Modèle-de-tâches, Profil-utilisateur
```

---

**Note:** This directive was created independently.
Inspired by: FALC (Facile à Lire et à Comprendre)
No content was copied. All rules and examples are original formulations.
