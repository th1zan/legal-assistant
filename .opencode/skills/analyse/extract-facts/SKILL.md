# Extract Facts (Extraction de Faits Juridiquement Pertinents)

---
name: extract-facts
description: Extraction des faits juridiquement pertinents (rechtserheblich) selon la méthodologie suisse. Première étape obligatoire avant toute analyse juridique. Implémente le principe "Da mihi facta, dabo tibi ius".
version: 1.1
author: SwissLawAI
tags: [analyse, faits, sachverhalt, méthodologie, suisse]
---

## Introduction

### Objectif

Extraire les faits **juridiquement pertinents** (*rechtserheblich*) d'un dossier selon la méthodologie suisse. Cette skill implémente le principe fondamental **"Da mihi facta, dabo tibi ius"** (Donne-moi les faits, je te donnerai le droit).

### Quand Utiliser

Invoquer `@extract-facts` pour:
- **Commencer une analyse de cas** (toujours la première étape)
- **Séparer faits et droit** dans une consultation ou un dossier
- **Identifier parties, chronologie et faits pertinents** d'un récit
- **Filtrer les faits non pertinents** (émotions, anecdotes, détails sans incidence)

### Contexte Juridique Suisse

**Principe fondamental**: La méthodologie suisse exige une séparation stricte entre **fait (Sachverhalt)** et **droit (Rechtsfrage)**.

**Concepts clés**:
- **Rechtserheblich**: Un fait n'est pertinent que s'il correspond à un **Tatbestandsmerkmal** (élément constitutif) d'une norme
- **Prozessuale Wahrheit**: Les faits établis selon les règles procédurales
- **Wechselbeziehung**: Va-et-vient constant entre norme et faits (Karl Engisch)

**Hors champ**: Cette skill ne fait PAS:
- De raisonnement juridique → utiliser `@analyse-cas-juridique`
- D'identification des questions juridiques → utiliser `@identify-legal-issues`
- De rédaction de documents → utiliser `@recours-tf` ou skills de rédaction

---

## Méthodologie en 6 Phases

Basée sur 5 sources académiques suisses (UZH, UNIL, GAIUS, ODAGE, doctrine).

### Phase 1: Lecture Initiale (Sans Annotation)

- Lire l'énoncé complet une fois sans marquer
- Identifier le **domaine juridique** (civil, pénal, administratif)
- Repérer les **indicateurs de question** ("X peut-il...", "Y a-t-il violation de...")

### Phase 2: Identification des Parties

- Identifier toutes les **personnes physiques** (nom, âge, domicile)
- Identifier toutes les **personnes morales** (forme juridique, siège)
- Assigner les **qualifications juridiques** (acquéreur/vendeur, employeur/travailleur)

### Phase 3: Construction de la Chronologie

- Extraire **toutes les dates** mentionnées ou déductibles
- Ordonner les événements **chronologiquement**
- **Calculer les délais** entre événements clés
- Identifier la **date de référence** ("aujourd'hui", date de consultation)

### Phase 4: Extraction des Faits Rechtserheblich

Pour chaque fait, demander: **"Ce fait correspond-il à un élément constitutif d'une norme?"**

**A. Faits Constitutifs (Tatbestandsmerkmale)**
- Éléments objectifs: Qui? Quoi? À qui? Quand? Où? Comment? Quel résultat?
- Éléments subjectifs: Intention, négligence, bonne/mauvaise foi
- Causalité: Lien de cause à effet, causalité naturelle et adéquate

**B. Faits Extinctifs/Modificatifs**
- Paiement, prescription, résiliation, compensation

**C. Faits Justificatifs**
- Consentement, état de nécessité, légitime défense

**D. Faits Procéduraux**
- Domicile/siège (compétence), valeur litigieuse, conciliation préalable, qualité pour agir

### Phase 5: Qualification Juridique Préliminaire

- Utiliser la **terminologie légale précise** (acquéreur, non acheteur)
- Qualifier les **actes juridiques** (type de contrat, acte unilatéral)
- Qualifier les **choses** (mobilière/immobilière, fongible/non-fongible)

### Phase 6: Élimination des Faits Non Pertinents

**Règle d'or**: Tout fait non rechtserheblich doit être **omis**.

**À éliminer**:
- Émotions sans conséquence juridique ("A était ravi")
- Détails narratifs ("par une belle journée")
- Répétitions ou paraphrases

**Exception**: Conserver si pertinent pour intention, connaissance ou bonne foi.

---

## Instructions d'Exécution

### ÉTAPE 1: Analyse Initiale (5 min)

1. Lire l'énoncé complet
2. Identifier le domaine juridique (CO, CP, CC, CPC, PA)
3. Repérer la question juridique apparente
4. Noter la complexité (simple: 1-2 parties / complexe: multiple)

**Output**: Évaluation initiale (2-3 phrases)

### ÉTAPE 2: Extraire les Parties (5 min)

Créer une section **PARTIES** avec:
- Nom/abréviation + qualification juridique
- Statut (personne physique/morale + forme)
- Domicile/siège

→ Voir `TEMPLATES.md` pour le format détaillé

### ÉTAPE 3: Construire la Chronologie (10 min)

Créer une section **CHRONOLOGIE** avec:
- Tableau: Date | Événement | Pertinence Juridique
- Calcul des délais
- Statut des délais (respecté/expiré/en cours)

→ Voir `TEMPLATES.md` pour le format détaillé

### ÉTAPE 4: Extraire les Faits Pertinents (20 min)

Créer une section **FAITS RECHTSERHEBLICH** organisée par catégorie:
- A. Éléments constitutifs (objectifs + subjectifs + causalité)
- B. Éléments extinctifs/modificatifs
- C. Éléments justificatifs
- D. Éléments procéduraux

→ Voir `TEMPLATES.md` pour le format détaillé

### ÉTAPE 5: Éliminer les Faits Non Pertinents (5 min)

Créer une section **FAITS ÉLIMINÉS** listant:
- Les faits omis avec justification
- Les exceptions conservées avec raison

### ÉTAPE 6: Reformulation Juridique (Optionnel - 10 min)

Si demandé, créer une **REFORMULATION JURIDIQUE** structurée:
- Parties avec qualifications
- Faits en terminologie légale
- Chronologie exacte
- Question juridique posée

---

## Format de Sortie

```markdown
# EXTRACTION DES FAITS JURIDIQUES

**Cas**: [Titre]  
**Domaine**: [CO, CP, CC, etc.]  
**Date d'analyse**: [Date]

---

## I. ÉVALUATION INITIALE
[2-3 phrases]

## II. PARTIES
[Tableau des parties]

## III. CHRONOLOGIE
[Tableau chronologique + délais]

## IV. FAITS JURIDIQUEMENT PERTINENTS (RECHTSERHEBLICH)
### A. Éléments Constitutifs
### B. Éléments Extinctifs/Modificatifs
### C. Éléments Justificatifs
### D. Éléments Procéduraux

## V. FAITS ÉLIMINÉS (Non Rechtserheblich)
[Liste avec justifications]

## VI. REFORMULATION JURIDIQUE (Optionnel)
[Si demandée]

## VII. PROCHAINES ÉTAPES
- [ ] `@identify-legal-issues`
- [ ] `@analyse-cas-juridique`

**Lacunes identifiées**: [Faits manquants à clarifier]
```

---

## Principes Directeurs

### 8 Règles Fondamentales

1. **Séparation stricte fait/droit**: Ne jamais mélanger énoncé factuel et qualification
2. **Rechtserheblich uniquement**: Inclure seulement les faits correspondant aux éléments constitutifs
3. **Chronologie précise**: Dates exactes, délais calculés
4. **Terminologie légale**: Termes exacts des codes applicables
5. **Faits procéduraux**: Toujours extraire domicile, dates, qualité pour agir
6. **Éléments subjectifs**: Toujours identifier intention, connaissance, foi
7. **Pas de spéculation**: Travailler avec les faits établis; noter les lacunes
8. **Éliminer le non-pertinent**: Émotions, anecdotes, détails narratifs

---

## Annexes

### Documents Détaillés

| Fichier | Contenu |
|---------|---------|
| `TEMPLATES.md` | Templates structurés pour chaque section |
| `TRAPS.md` | 10 pièges courants avec exemples et solutions |
| `EXAMPLES.md` | 2 exemples complets (civil CO 197, pénal CP 144) |
| `REFERENCE.md` | Sources académiques, bases légales, bibliographie |

### Pièges Principaux (Résumé)

| # | Piège | Règle |
|---|-------|-------|
| 1 | Confusion fait/qualification | Faits d'abord, qualification ensuite |
| 2 | Faits non établis | Ne jamais spéculer |
| 3 | Oubli procédural | Extraire domicile, dates, qualité |
| 4 | Oubli subjectif | Chercher intention, connaissance |
| 5 | Mauvaise terminologie | Utiliser termes légaux exacts |

→ Voir `TRAPS.md` pour les 10 pièges détaillés

---

## Skills Connexes

### Workflow Recommandé

1. **`@extract-facts`** (cette skill) ← Commencer ici
2. **`@identify-legal-issues`** - Identifier les questions juridiques
3. **`@analyse-cas-juridique`** - Analyse juridique complète
4. **`@recours-tf`** - Rédaction de recours (si applicable)

### Outils de Recherche

- `@swiss-case-law-research` - Jurisprudence (Entscheidsuche)
- `@swiss-legal-commentary` - Doctrine (Onlinekommentar)
- `@citation-formatter` - Formatage des citations

---

## Avertissement

Cette skill est basée sur des **sources suisses exclusivement**. Le concept de **rechtserheblich** est central à la méthodologie juridique suisse romande et alémanique.

**Principe directeur**: "Da mihi facta, dabo tibi ius" — Donne-moi les faits (correctement extraits), je te donnerai le droit.

---

*Version 1.1 — Février 2026*
