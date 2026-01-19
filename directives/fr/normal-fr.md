# Directive : Traduction Professionnelle en Français [M]

## Meta [M]
| Champ | Valeur |
|-------|--------|
| **ID** | `normal-fr` |
| **Type** | Traduction Professionnelle Standard |
| **Version** | 2.0 |
| **Direction du Texte** | LTR (Gauche-à-Droite) |
| **Niveau Cible** | Natif / C1-C2 |

---

## Objectif [M]

Traduire les textes sources en **français naturel et professionnel** tout en maintenant précision, registre et adéquation culturelle.

---

## Quand Utiliser [M]

- Documents professionnels nécessitant une traduction précise
- Textes commerciaux, juridiques ou techniques
- Contenus où la fluidité naturelle est primordiale
- Quand le FALC (A1/A2) ou le Langage Clair (B1) n'est PAS requis

---

## Paramètres de Langue [M]

### Langue de Sortie
- **Principale :** Français standard (France par défaut, ou Suisse/Belgique/Canada si spécifié)
- **Écriture :** Latine
- **Direction du Texte :** LTR

### Langues Sources Acceptées [M]
- Allemand (principal)
- Anglais (courant)
- Toute langue (sur demande explicite)

### Gestion des Écritures [M]
| Écriture Source | Traitement |
|-----------------|------------|
| Latine (DE, EN, ES...) | Traduction directe |
| Cyrillique (RU) | Translittérer les noms si nécessaire |
| CJC (ZH, JA, KO) | Romaniser les noms propres ; conserver les marques |
| Arabe/Hébreu (RTL) | Assurer l'intégration correcte dans la sortie LTR |

---

## Principes Fondamentaux [M]

### 1. Précision Avant Tout [M]
- Préserver TOUTES les informations du texte source
- Ne PAS ajouter, omettre ou inventer de contenu
- Maintenir la validité juridique/technique des énoncés
- **JAMAIS halluciner de faits** [M]

### 2. Termes Techniques [M]
- Utiliser les équivalents français établis pour les termes techniques
- Si AUCUN équivalent standard n'existe : conserver le terme original + explication à la première occurrence
- **Règle de Cohérence :** Même terme = même traduction partout [M]

**Format pour termes inconnus :**
```
[Terme Original] (explication en français)
```

### 3. Français Naturel [M]
- Utiliser un français idiomatique, PAS de traduction mot-à-mot
- Adapter la structure des phrases aux conventions françaises
- Éviter les calques syntaxiques de la langue source

### 4. Correspondance de Registre [M]
| Registre Source | Registre Cible |
|-----------------|----------------|
| Formel/Juridique | Français formel |
| Commercial | Français professionnel |
| Technique | Français technique |
| Familier | Français courant |

**Gestion des Pronoms :**
- Allemand « Sie » (formel) → « vous »
- Allemand « du » (informel) → « tu » (formulation plus décontractée)
- Anglais « you » → « vous » (défaut professionnel) ou « tu » (contexte informel)

---

## Genre Grammatical [M]

### Règles d'Accord [M]
- Accorder les adjectifs avec le genre et le nombre du nom
- Accorder les participes passés selon les règles (avoir/être)
- Attention aux noms de métiers et fonctions

### Langage Inclusif [C]
Options selon le contexte et la demande :
| Option | Exemple |
|--------|---------|
| Doublet complet | les utilisateurs et utilisatrices |
| Point médian | les utilisateur·rice·s |
| Terme épicène | la clientèle, le personnel |
| Masculin générique | les utilisateurs (contexte juridique traditionnel) |

**Règle :** Suivre les préférences du client ou utiliser des formulations épicènes par défaut.

---

## Gestion des Éléments Spécifiques [M]

### A. Mots Composés [M]
Transformer les composés sources en français naturel :

| Allemand | Français |
|----------|----------|
| Datenschutzerklärung | politique de confidentialité |
| Nutzungsbedingungen | conditions d'utilisation |
| Haftungsausschluss | clause de non-responsabilité |
| Verantwortungsbereich | domaine de responsabilité |

**Règle :** Si le composé est spécifique au domaine, vérifier l'équivalent français standard.

### B. Références Juridiques [M]
| Source | Cible |
|--------|-------|
| § | Article |
| Abs. | Alinéa |
| Nr. | Numéro |

- Conserver les numéros d'article/paragraphe intacts
- Noter les différences de juridiction si pertinent

### C. Nombres et Formats [M]

#### Conventions Numériques
| Élément | Format Français |
|---------|-----------------|
| Milliers | 1 000 (espace insécable) |
| Décimales | 0,50 (virgule) |
| Pourcentages | 50 % (espace avant %) |
| Téléphone | +33 1 23 45 67 89 |

#### Formats de Date
| Contexte | Format | Exemple |
|----------|--------|---------|
| Standard | JJ mois AAAA | 15 janvier 2024 |
| Abrégé | JJ/MM/AAAA | 15/01/2024 |
| ISO (neutre) | AAAA-MM-JJ | 2024-01-15 |

**Règle :** Utiliser le format standard français ou ISO pour les textes internationaux.

#### Devises
- Conserver la devise originale avec symbole : 50 €, 30 £, 100 $
- Le symbole € se place APRÈS le nombre avec espace : 50 €
- Ajouter l'équivalent entre parenthèses si pertinent : 50 € (environ 55 $)

### D. Abréviations [M]
Développer les abréviations sources et utiliser les équivalents français :

| Source | Français |
|--------|----------|
| z.B. / e.g. | p. ex. / par exemple |
| d.h. / i.e. | c.-à-d. / c'est-à-dire |
| u.a. / among others | entre autres |
| etc. | etc. (conserver) |
| usw. | etc. |
| ggf. / if applicable | le cas échéant |
| bzgl. / regarding | concernant |
| inkl. / incl. | y c. / y compris |
| exkl. / excl. | non compris |

### E. Ponctuation [M]
| Élément | Règle Française |
|---------|-----------------|
| Guillemets | « guillemets » (avec espaces insécables) |
| Point-virgule | Espace insécable avant ; |
| Deux-points | Espace insécable avant : |
| Point d'exclamation | Espace insécable avant ! |
| Point d'interrogation | Espace insécable avant ? |
| Tirets | Tiret demi-cadratin pour incises – comme ceci – |
| Listes | Pas de virgule Oxford en français standard |

---

## Adaptation Culturelle [M]

### Expressions Idiomatiques [M]
- Ne PAS traduire littéralement
- Trouver l'expression française équivalente OU reformuler de façon neutre

| Allemand | NE PAS | PLUTÔT |
|----------|--------|--------|
| Das ist nicht mein Bier | Ce n'est pas ma bière | Ce n'est pas mon affaire |
| Tomaten auf den Augen haben | Avoir des tomates sur les yeux | Ne pas voir l'évidence |

| Anglais | NE PAS | PLUTÔT |
|---------|--------|--------|
| It's raining cats and dogs | Il pleut des chats et des chiens | Il pleut des cordes |
| Break a leg | Casse-toi une jambe | Bonne chance / Merde |

### Références Culturelles [C]
- Localiser si le public cible ne comprendra pas
- Conserver l'original + explication pour textes techniques/juridiques

**Exemples :**
> « ...nach dem BGB » → « ...en vertu du Code civil allemand (BGB) »
> « ...under UK law » → « ...en vertu du droit britannique »

---

## Intégration du Glossaire [M]

### Ordre de Priorité [M]
1. **Glossaire client** (si fourni) — utiliser les termes EXACTS
2. **Glossaire du domaine** (si existe dans `glossaries/`)
3. **Traduction standard** (votre jugement professionnel)

### Règle de Priorité du Glossaire [M]
Si le glossaire contient un terme : **L'UTILISER TEXTUELLEMENT**.
Ne PAS inventer d'alternatives quand une définition existe.

---

## Gestion des Erreurs [M]

### Éléments Intraduisibles [M]
| Situation | Action |
|-----------|--------|
| Acronyme sans contexte | Conserver l'original, ajouter note [?] |
| Référence manquante | Signaler avec [RÉFÉRENCE REQUISE] |
| Terme ambigu | Traduire le sens le plus probable, noter dans QA-Log |
| Texte corrompu | Marquer comme [ILLISIBLE] |

### Résolution de Conflits [M]
- Précision source > fluidité cible
- En cas de doute : signaler et demander

---

## Spécifications de Sortie [M]

### Format [M]
- Respecter la structure du document source (titres, paragraphes, listes)
- Préserver les marqueurs de formatage si présents
- Sortie texte propre (pas de notes du traducteur en ligne)

### Nommage des Fichiers [M]
```
{nom_original}_{lang}.txt
```
Exemple : `agb_zeitreise_fr.txt`

---

## Liste de Contrôle Qualité [M]

Avant livraison, vérifier TOUS les points :

- [ ] Tout le contenu traduit avec précision [M]
- [ ] Termes techniques cohérents partout [M]
- [ ] Fluidité naturelle du français (pas de « traductionese ») [M]
- [ ] Registre correspondant à la source [M]
- [ ] Aucune information ajoutée ou omise [M]
- [ ] Grammaire et orthographe correctes [M]
- [ ] Nombres/dates au format correct [M]
- [ ] Termes du glossaire appliqués (si fourni) [M]
- [ ] Références culturelles traitées de façon appropriée [C]
- [ ] Accords de genre corrects [M]
- [ ] Ponctuation française respectée (espaces insécables) [M]

---

## Section QA-Log [C]

Pour les traductions complexes, ajouter à la fin :

```
---
### QA-Log (Auto-généré)

**Termes Techniques :**
- [Terme source] → [Traduction française]

**Abréviations Développées :**
- [Source] → [Développement]

**Adaptations Culturelles :**
- [Référence originale] → [Version localisée]

**Éléments Signalés :**
- [Toute ambiguïté ou problème noté]
```

---

## Avertissement [M]

Cette directive fournit des lignes directrices pour la traduction professionnelle.
Toutes les règles et exemples sont des formulations originales.
Inspiré par : ISO 17100 Services de Traduction, Norme NF EN 17100.

---

**[FIN DE LA DIRECTIVE]**
