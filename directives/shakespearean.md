# Directive: Shakespearean Style (Multilingual)

## Basis [M]
**Type:** Stylistic Transformation
**Framework:** Early Modern / Renaissance theatrical language
**Applies to:** All languages

---

## Purpose [M]
Transforms modern texts into a Shakespearean/Renaissance theatrical style in ANY language while preserving meaning and technical terminology.

**Priority:** Dramatic authenticity while maintaining comprehensibility. [M]
**Standards:** Based on theatrical conventions of the Renaissance period (c. 1550-1650).

## When to Use [M]
- When user requests "Shakespeare" or "Shakespearean" style [M]
- For creative/theatrical transformations of texts [M]
- Applies to input text in ANY language [M]

---

## Key Requirements [M]

### The Hybrid Rule (Supreme Directive) [M]
Technical terms are **preserved** but introduced with dramatic flair.

### Language-Specific Transformations [M]

---

### DEUTSCH (Frühneuhochdeutsch-Stil)

| Modern | Shakespearean |
|--------|---------------|
| du | Ihr (höflich) / du (vertraut) |
| Sie | Euer Gnaden / Ihr |
| ist | ist / sei |
| haben | habt / habet |
| werden | werdet / sollt |
| ja | fürwahr / wahrlich |
| nein | mitnichten / keineswegs |
| sehr | gar / überaus |
| vielleicht | vielleicht mag es sein |
| weil | denn / sintemal |
| deshalb | darum / demnach |

**Dramatische Elemente:**
- "Hört!" / "Vernehmet!" / "Wohlan!"
- "O!" / "Ach!" / "Wehe!"
- "Bei meiner Treu!" / "Beim Himmel!"
- Inversionen: "Wisst Ihr nicht?" statt "Wissen Sie nicht?"

**Beispiel:**
> **Original:** Der Usability-Test zeigt, ob das Design geändert werden muss.
>
> **Shakespearean:** Hört! Der **Usability-Test** offenbaret uns, ob Euer Design der Änderung bedarf. Fürwahr, durch solche Prüfung wird ersichtlich, welche Wandlung vonnöten sei!

---

### ENGLISH (Early Modern English)

| Modern | Shakespearean |
|--------|---------------|
| you (singular) | thou/thee |
| you (plural) | ye |
| your | thy/thine |
| is/are | art/doth/be |
| do/does | dost/doth |
| have/has | hast/hath |
| will | shall/wilt |
| yes | aye/yea |
| no | nay |
| very | most/verily |
| perhaps | perchance/mayhap |

**Verb Conjugations:**
- **Thou** + "-st"/"-est": thou art, thou hast, thou speakest
- **He/She/It** + "-th"/"-eth": he hath, she doth, it seemeth

**Dramatic Elements:**
- "Hark!" / "O!" / "Fie!" / "Alack!" / "Prithee!"
- Inversions: "Know you not?" instead of "Don't you know?"

---

### ESPAÑOL (Castellano Clásico - Siglo de Oro)

| Moderno | Shakespeariano |
|---------|----------------|
| tú | vos |
| usted | vuestra merced |
| tienes | tenéis / habéis |
| es | es / sea |
| sí | así es / en verdad |
| no | en modo alguno |
| muy | harto / en demasía |
| porque | pues / ca |

**Elementos Dramáticos:**
- "¡Oíd!" / "¡Escuchad!" / "¡Pardiez!"
- "¡Oh!" / "¡Ay!" / "¡Vive Dios!"

---

### FRANÇAIS (Français Classique - XVIIe siècle)

| Moderne | Shakespearien |
|---------|---------------|
| tu | tu (intime) / vous (respect) |
| vous | Votre Grâce |
| est | est / soit |
| oui | certes / assurément |
| non | point / nullement |
| très | fort / grandement |
| peut-être | peut-être qu'il en soit ainsi |

**Éléments Dramatiques:**
- "Oyez!" / "Écoutez!" / "Morbleu!"
- "Ô!" / "Hélas!" / "Tudieu!"

---

### ITALIANO (Italiano Rinascimentale)

| Moderno | Shakespeariano |
|---------|----------------|
| tu | voi (rispetto) / tu (intimo) |
| Lei | Vostra Signoria |
| è | è / sia |
| sì | invero / certamente |
| no | giammai / punto |
| molto | assai / grandemente |

**Elementi Drammatici:**
- "Udite!" / "Ascoltate!" / "Perdinci!"
- "Oh!" / "Ahimè!" / "Per Bacco!"

---

### NEDERLANDS (Klassiek Nederlands)

| Modern | Shakespeariaans |
|--------|-----------------|
| jij/je | gij |
| u | Uwe Genade |
| is | is / zij |
| ja | voorwaar / gewis |
| nee | geenszins |
| heel | zeer / uitermate |

**Dramatische Elementen:**
- "Hoort!" / "Verneemt!" / "Welaan!"
- "O!" / "Ach!" / "Wee!"

---

### 日本語 (古典的・能/歌舞伎風)

| 現代 | シェイクスピア風 |
|------|------------------|
| です/ます | でござる / である |
| あなた | そなた / 御身 |
| はい | 然り / 左様 |
| いいえ | 否 / 断じて |
| とても | いと / 甚だ |

**劇的要素:**
- 「聞け！」「見よ！」「おお！」「嗚呼！」

---

## Universal Dramatic Techniques [M]

1. **Exclamations** - Add period-appropriate interjections [M]
2. **Inversions** - Reverse subject-verb order for emphasis [C]
3. **Rhetorical Questions** - "Know you not...?" / "Wisst Ihr nicht...?" [C]
4. **Nature Metaphors** - Reference stars, fate, fortune, seasons [C]
5. **Formal Address** - Use archaic formal pronouns [M]

---

## Anti-Patterns [M]

### Do NOT [M]
- Use modern slang or contractions [M]
- Make text incomprehensible - clarity over authenticity when needed [M]
- Delete or translate technical terms [M]
- Mix different historical periods randomly [M]
- Overdo archaisms to the point of parody [M]

---

## Output [M]
Speicherort: `output/`
Namenskonvention: `{name}_{lang}_shakespeare.txt`

Example: `output/agb_de_shakespeare.txt`, `output/privacy_en_shakespeare.txt`

---

## Documentation & QA Log [M]
Add at the end of every transformed file:

### QA Log (Auto-generated)
**Source Language:** [Language]
**Preserved Technical Terms:**
- [List terms]
**Shakespearean Elements Used:**
- Archaic pronouns: [Yes/No]
- Period exclamations: [List]
- Verb archaisms: [List]
**Readability Check:**
- Meaning preserved: [Yes/No]
