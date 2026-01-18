# Directive: Spanish Easy Read (Lectura Fácil) [M]

## Purpose [M]
Defines rules for translating technical texts into Spanish Easy Read (Lectura Fácil) while maintaining legal accuracy (Hybrid Approach).

**Priority:** Legal correctness over maximum simplification. [M]

## When to Use [M]
- For all translations of technical texts to Easy Read [M]
- For legally relevant texts (contracts, training, regulations) [M]
- When target audience: people with reading comprehension difficulties

---

## Key Requirements [M]

### The Hybrid Rule (Supreme Principle) [M]
Because texts have legal relevance, **technical terms are preserved** and explained.

#### 1. Glossary Priority [M]
If the glossary (input files) contains not only the term but also an explanation:
**You MUST use that explanation literally.**
Do not invent anything new if a definition already exists.

#### 2. The "Eso significa" Anchor [M]
Use for explanations **exclusively** the phrase: **"Eso significa:"** (That means:)
No alternatives like "Esto quiere decir:", "Es decir:", "significa:" or "es:".

#### 3. Anti-Doubling (CRITICAL) [M]
If the original sentence before the technical term contains words like:
- "significa:"
- "muestra:"
- "es:"
- "describe:"
- "incluye:"

**DELETE these words** before adding "Eso significa:".
Otherwise duplications arise like "significa: Eso significa:".

| INCORRECT | CORRECT |
|-----------|---------|
| "Eficiencia significa: Eso significa: Qué tan rápido eres." | See correct format below |
| "Usabilidad es: Eso significa: Qué tan fácil de usar es algo." | See correct format below |

#### 4. Hard Line Break (Mandatory) [M]
Every explanation requires **three separate paragraphs**:

1. Write the technical term (**bold**) with period.
2. Make a **new paragraph**.
3. Write "Eso significa:" (no text after it).
4. Make a **new paragraph**.
5. Write the explanation.

**Correct Format:**
```
**Eficiencia**.

Eso significa:

Cuántos recursos necesitas para alcanzar una meta.
```

#### 5. Format on First Occurrence [M]
1. Use the correct technical term on its first occurrence [M]
2. Highlight technical term in **bold** [M]
3. Put a period after the technical term [M]
4. New paragraph [M]
5. Write "Eso significa:" alone on a line [M]
6. New paragraph [M]
7. Write the explanation [M]

**INCORRECT Example:**
> Efectividad significa: Eso significa: Si alcanzas tu meta.

**CORRECT Example:**
> **Efectividad**.
>
> Eso significa:
>
> Si alcanzas tu meta o no.

### Grammar & Sentence Structure [M]
- **One sentence = One idea** [M]
- **SVO order**: Subject - Verb - Object (Who does what?) [M]
- **No Subjunctive**: Use indicative (Not: "Si pudiera...", But: "Si puede...") [M]
- **No Passive**: Use active voice (Not: "La solicitud es revisada", But: "Nosotros revisamos la solicitud") [M]
- **Positive formulations**: Avoid negations when possible [C]

### Formatting [M]
- Each sentence starts on a **new line** [M]
- Use many paragraphs [M]
- Bullet lists instead of commas [C]

---

## Edge Cases & Special Rules [M]

### A. Anglicisms and Foreign Words [M]
Avoid English terms when a good Spanish word exists.
If the Anglicism is an established technical term, apply the Hybrid Rule.

| Incorrect | Correct |
|-----------|---------|
| "Hacemos un meeting" | "Hacemos una **reunión**" |
| "Checkea esto" | "Revisa esto" |
| "El link" | "El enlace" |

**Exception (technical term in company):**
> Por favor respete el **Compliance**.
>
> Eso significa:
>
> Las reglas para el buen comportamiento en la empresa.

### B. Abbreviations [M]
Abbreviations are major barriers. **Always expand them:**

| Abbreviation | Expanded |
|--------------|----------|
| etc. | y otras cosas más |
| p. ej. | por ejemplo |
| aprox. | aproximadamente |
| es decir | eso significa |
| § | Artículo |
| % | por ciento |
| & | y |
| € | euros |
| Nº | Número |
| incl. | incluido / con esto también |
| Sr./Sra. | Señor/Señora |

### C. Long Words [M]
Spanish has fewer compound words than German.
For very long words, split with **hyphen** for better readability:

| Original | Easy Read |
|----------|-----------|
| responsabilidad | responsabilidad |
| corresponsabilidad | co-responsabilidad |
| interdepartamental | inter-departamental |

### D. Metaphors and Idioms [M]
Avoid figurative language - it's often understood literally:

| Incorrect | Correct |
|-----------|---------|
| "Tirar la toalla" | "Rendirse" |
| "Estar en las nubes" | "No prestar atención" |
| "Ponerse las pilas" | "Trabajar con más energía" |
| "Dar en el clavo" | "Acertar exactamente" |

### E. Inclusive Language [M]
Special symbols (@, x, e) hinder reading and screen readers.
**Rule:** Use double form or neutral form:

| Incorrect | Correct |
|-----------|---------|
| L@s trabajadores | Los trabajadores y las trabajadoras |
| Todxs | Todas las personas |

### F. Numbers and Dates [M]
- Numbers **always as digits** (also 1, 2, 3) - easier to grasp [M]
- Dates are written out completely [M]

| Incorrect | Correct |
|-----------|---------|
| tres días | 3 días |
| 01/04/2024 | 1 de abril de 2024 |
| 15:30 | 3 y media de la tarde |

### G. References [C]
Avoid "see above" or "as already mentioned".
**Better:** Repeat the information briefly.

### H. URLs and Email Addresses [C]
- Simplify URLs when possible
- Write out and explain email addresses

> Puede escribirnos.
> Nuestra dirección de correo es: info@empresa.es

### I. Lists and Enumerations [C]
- Maximum 5-7 points per list
- Each point as its own complete idea
- For long lists: Divide into categories

---

## Examples for Difficult Cases [C]

### Anglicism in IT Text
**Original:** "El user debe hacer login en el frontend."

**Translation:**
> El usuario debe iniciar sesión.
> Eso lo hace en la página web.
> Los expertos dicen: **Frontend**.
> Iniciar sesión también se llama: **Login**.

### Legal Abbreviation and Date
**Original:** "Conforme al Art. 12 del CC la norma entra en vigor el 01/04/2024."

**Translation:**
> Está escrito en la ley.
> La ley se llama: Código Civil.
> La abreviatura es: **CC**.
> Está en el Artículo 12.
>
> La norma vale desde el 1 de abril de 2024.

### Data Protection Notice
**Original:** "Los datos personales se procesan exclusivamente con fines específicos según el Art. 6 RGPD."

**Translation:**
> Guardamos sus datos.
> Por ejemplo: Su nombre y su dirección.
> Eso lo llamamos: **datos personales**.
>
> Seguimos una ley para esto.
> La ley se llama: **RGPD**.
>
> Eso significa:
>
> Reglamento General de Protección de Datos.
>
> Usamos los datos solo para un fin determinado.
> Por ejemplo: Para poder enviarle una carta.

---

## Anti-Patterns [M]

### What NOT to do:
- Delete technical terms or replace with imprecise synonyms [M]
- Change legal meaning to simplify text [M]
- Omit or invent facts [M]
- Leave abbreviations unexplained [M]
- Use passive constructions [M]
- Use inclusive language with symbols (@, x, e) [M]
- Use metaphors and idioms [M]
- Long sentences with multiple ideas [M]
- **Double introductions** like "significa: Eso significa:" [M]
- **Explanation on same line** as "Eso significa:" [M]

### Anti-Pattern Example:
| Incorrect | Why it's wrong |
|-----------|----------------|
| Instead of "Amonestación" only "Problema con el jefe" | Legal meaning lost |
| Subjunctive: "Podría ser que..." | Too vague, better: "Tal vez pase esto" |
| "Eficiencia significa: Eso significa: ..." | Double introduction - "significa:" must be deleted |
| "Eso significa: Qué tan bueno es algo." | Explanation must be on new line |

---

## Success Criteria [M]

### Quality Checklist before Delivery:
- [ ] All legal technical terms still present [M]
- [ ] All technical terms explained (Hybrid Rule) [M]
- [ ] **No double introductions** (e.g. "significa: Eso significa:") [M]
- [ ] **"Eso significa:" stands alone on a line** [M]
- [ ] **Explanation is on separate line after "Eso significa:"** [M]
- [ ] Each sentence short (max. 10-15 words) [M]
- [ ] Abbreviations expanded [M]
- [ ] Long words hyphenated [M]
- [ ] Metaphors removed [M]
- [ ] Anglicisms translated or explained [M]
- [ ] Passive constructions resolved [M]
- [ ] Numbers as digits, dates written out [M]
- [ ] No inclusive language with symbols [M]

### Validation:
- Text maintains legal validity [M]
- Text is comprehensible for target audience [M]
- No information was lost [M]

---

## Documentation & QA Log [M]

Add at the **end** of every translated file a QA appendix for the reviewer.
This appendix serves quality control and traceability.

**Format:**

```markdown
---

### QA-Log (Generado automáticamente)

**Preserved technical terms:**
- [List of all glossary words that appeared in the text]

**Expanded abbreviations:**
- [List of abbreviations with expansion, e.g. "etc. -> y otras cosas más"]

**Hyphenated long words:**
- [List of long words that were hyphenated]
```

**Example:**
```markdown
---

### QA-Log (Generado automáticamente)

**Preserved technical terms:**
- Usabilidad, Efectividad, Eficiencia, Satisfacción, Experiencia de Usuario, Contexto de Uso

**Expanded abbreviations:**
- etc. -> y otras cosas más
- p. ej. -> por ejemplo
- UX -> Experiencia de Usuario (written out on first mention)

**Hyphenated long words:**
- Inter-departamental, Co-responsabilidad
```

---

**Note:** This directive was created independently.
Inspired by: UNE 153101 (Spanish Easy Read Standard), IFLA Easy-to-Read Guidelines
No content was copied. All rules and examples are original formulations.
