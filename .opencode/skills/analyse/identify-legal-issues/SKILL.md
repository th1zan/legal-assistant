# Identify Legal Issues (Identification des Questions Juridiques)

**Skill Name**: `identify-legal-issues`  
**Domain**: Swiss Legal Analysis  
**Language Support**: FR, DE, IT  
**Version**: 1.1  
**Created**: 26 février 2026  
**Updated**: 27 février 2026

---

## Introduction

### Purpose

Identifier et reformuler les questions juridiques (**Fallfrage**) à partir des faits d'un cas selon la méthodologie suisse. Cette skill transforme les questions brutes du client en questions juridiques précises qui guident le raisonnement et l'identification des normes.

### When to Use

Invoquer cette skill (`@identify-legal-issues`) quand vous devez :
- **Reformuler une question brute** en termes juridiques précis
- **Identifier les questions juridiques** soulevées par un état de fait
- **Distinguer** questions préalables (recevabilité) et principales (fond)
- **Détecter les questions multiples** nécessitant des analyses séparées
- **Identifier les actions applicables** en droit civil (selon Bohnet, *Actions civiles*)
- **Structurer les questions de subsomption** pour l'analyse juridique

### Swiss Legal Context

**Principe fondamental** : La méthodologie suisse exige la **reformulation des questions brutes en termes juridiques**. C'est l'**Étape 2** de l'analyse de cas :

1. **Étape 1** (`@extract-facts`) : Extraction des faits juridiquement pertinents
2. **Étape 2** (`@identify-legal-issues`) : Identification et reformulation ← **CETTE SKILL**
3. **Étape 3** (`@analyse-cas-juridique`) : Analyse juridique avec syllogisme et subsomption

**Concepts clés** :
- **"Qui ? Quoi ? De qui ?"** (FR) / **"Wer? Was? Von wem? Woraus?"** (DE) : Formule universelle
- **Fallfrage** (DE) : Question juridique (beschränkte vs. unbeschränkte)
- **Questions préalables vs. principales** : Recevabilité avant le fond
- **Questions multiples** : Plusieurs rapports juridiques = traitement **séparé**

**Hors scope** : Cette skill ne fait PAS :
- L'extraction des faits (utiliser `@extract-facts`)
- L'analyse juridique ou subsomption (utiliser `@analyse-cas-juridique`)
- La rédaction de documents (utiliser les skills spécifiques)
- La recherche de normes (cette skill identifie seulement les normes à rechercher)

---

## Methodology

Cette skill implémente la **méthodologie suisse d'identification des questions juridiques** basée sur 4 sources académiques :

1. **UNIL** (Canapa) - *Méthode de résolution de cas juridiques* (2018)
2. **UZH** (Thommen) - *Fallbearbeitung im Strafrecht* (2016)
3. **GAIUS** (Roduit) - *Résolution pratique de cas juridiques* (2016)
4. **ODAGE** (Barreau de Genève) - *Guide pratique examen du brevet d'avocat* (2020)

### Principes Directeurs

1. **Reformulation obligatoire** : Ne jamais travailler avec la question brute
2. **"Qui ? Quoi ? De qui ?"** : Structure universelle de reformulation
3. **Questions préalables d'abord** : Recevabilité avant le fond
4. **Séparation des questions multiples** : Chaque rapport juridique = question séparée = syllogisme séparé
5. **"Vœu client"** : Identifier ce que le client veut obtenir
6. **Fonction stratégique** : Questions bien formulées facilitent la recherche de normes
7. **Cohérence avec les faits** : Chaque question doit être ancrée dans les faits extraits (Étape 1)

### Méthode en 6 Phases

#### Phase 1 : Analyse Préliminaire
- Lire l'énoncé complet du cas
- Identifier le contexte général (domaine juridique)
- Repérer les parties
- Noter dates et délais
- Identifier la "question brute" (explicite ou implicite)
- Identifier le "vœu client" (ce que le client veut obtenir)

#### Phase 2 : Reformulation en Termes Juridiques
- Appliquer **"Qui ? Quoi ? De qui ?"** :
  - **Qui ?** → Identifier le demandeur (qualité : actionnaire, créancier, victime, etc.)
  - **Quoi ?** → Formuler la prétention en termes juridiques (annulation, condamnation, etc.)
  - **De qui ?** → Identifier le défendeur (capacité : société, débiteur, auteur, etc.)
  - **D'où ?** (optionnel, tradition DE) → Base légale pressentie
- Distinguer **questions préalables** (recevabilité) des **questions principales** (fond)
- Détecter les **questions multiples**

#### Phase 3 : Identification des Actions (Droit Civil)
- Qualifier le cas (type de contrat, type de responsabilité, type de dommage)
- Identifier les actions possibles (Bohnet, *Actions civiles*) :
  - **Actions en exécution** : Paiement, livraison, exécution en nature
  - **Actions en résolution/annulation** : Vice du consentement, défaut
  - **Actions en réparation** : Dommages-intérêts (CO 97, CO 41)
  - **Actions en constatation** : Existence/inexistence d'un droit
  - **Actions conservatoires** : Séquestre, mesures provisionnelles
- Évaluer cumul ou priorité des actions

#### Phase 4 : Vérification de la Recevabilité
- **Qualité pour agir** (CPC 59) : Intérêt juridiquement protégé ?
- **Capacité d'être partie** : Bon défendeur ?
- **Compétence matérielle** : Civil, pénal, administratif ?
- **Compétence territoriale** : For du domicile, for contractuel, élection de for ?
- **Délais** : Délai légal respecté ? Féries, suspensions, prescription ?
- **Exigences de forme** : Conciliation préalable ? Forme écrite ? Représentation obligatoire ?

#### Phase 5 : Formulation Finale
- Rédiger chaque question précisément avec terminologie juridique exacte
- Mentionner les parties par leur nom
- Indiquer la base légale pressentie si connue
- Ordonner logiquement :
  1. Questions préalables (recevabilité) en premier
  2. Questions principales (fond) ensuite
  3. Questions subsidiaires en dernier
- Vérifier cohérence avec les faits extraits (Étape 1)

#### Phase 6 : Documentation et Préparation Recherche
- Annoter les questions avec indices de recherche
- Identifier le domaine juridique (CO, CC, CP, CPC, etc.)
- Lister les articles pressentis
- Identifier mots-clés pour recherche dans les codes
- Préparer transition vers Étape 3 (recherche de normes)

---

## Instructions

### Process Step-by-Step

Quand cette skill est invoquée, suivre ces instructions :

#### STEP 1 : Analyse Préliminaire (5 min)

1. **Lire l'énoncé** (ou utiliser output de `@extract-facts` si disponible)
2. **Identifier la question brute** : Chercher "Que peut faire X ?", "A vous consulte...", etc.
3. **Identifier le vœu client** (ODAGE) : Position ? Objectif concret ?
4. **Identifier le domaine** : Civil (CO, CC), pénal (CP), administratif (PA) ?

**Output** : Évaluation brève (2-3 phrases)

#### STEP 2 : Appliquer "Qui ? Quoi ? De qui ?" (10 min)

Créer une section **REFORMULATION** selon le template dans [TEMPLATES.md](./TEMPLATES.md#reformulation-en-termes-juridiques).

**Guidelines** :
- Utiliser la **terminologie juridique exacte** (pas le langage courant)
- Pour **Qui** : Vérifier qualité pour agir (CPC 59)
- Pour **Quoi** : Utiliser verbes "obtenir", "exiger", "faire annuler", "faire constater"
- Pour **De qui** : Vérifier capacité d'être partie (bon défendeur)

#### STEP 3 : Distinguer Questions Préalables vs. Principales (10 min)

Créer une section **QUESTIONS IDENTIFIÉES** selon le template dans [TEMPLATES.md](./TEMPLATES.md#questions-juridiques-identifiées).

Structure obligatoire :
- **A. Questions Préalables** : Q1a (qualité), Q1b (compétence matérielle), Q1c (compétence territoriale), Q1d (délais), Q1e (forme)
- **B. Questions Principales** : Q2 avec conditions à vérifier
- **C. Questions Subsidiaires** : Q3 si applicable

#### STEP 4 : Identifier les Actions (Droit Civil - 10 min)

Si le cas implique le **droit civil** (CO, CC), créer une section **ACTIONS ENVISAGEABLES** selon le template dans [TEMPLATES.md](./TEMPLATES.md#actions-envisageables-droit-civil).

#### STEP 5 : Détecter les Questions Multiples (5 min)

Si le cas implique **plusieurs rapports juridiques**, créer une section **QUESTIONS MULTIPLES** selon le template dans [TEMPLATES.md](./TEMPLATES.md#questions-multiples).

**Déclencheurs** :
- Plusieurs demandeurs ou défendeurs
- Plusieurs actes juridiques (2 contrats, contrat + délit)
- Plusieurs infractions potentielles (droit pénal)
- Cumul d'actions (résolution + dommages-intérêts)
- Prétentions principales + subsidiaires

#### STEP 6 : Préparer la Recherche Juridique (5 min)

Créer une section **RECHERCHE JURIDIQUE** selon le template dans [TEMPLATES.md](./TEMPLATES.md#préparation-recherche-juridique).

---

## Output Format

Le format de sortie complet est documenté dans [TEMPLATES.md](./TEMPLATES.md#output-format-complet).

Structure résumée :
```
# IDENTIFICATION DES QUESTIONS JURIDIQUES
## I. PRELIMINARY ANALYSIS
## II. REFORMULATION EN TERMES JURIDIQUES
## III. QUESTIONS IDENTIFIÉES
## IV. ACTIONS ENVISAGEABLES (si droit civil)
## V. QUESTIONS MULTIPLES (si applicable)
## VI. PRÉPARATION DE LA RECHERCHE JURIDIQUE
## VII. NEXT STEPS
```

---

## Pièges à Éviter

⚠️ **12 pièges courants** sont documentés en détail dans [TRAPS.md](./TRAPS.md).

**Les plus critiques** :
1. **Ne pas reformuler** la question brute → Toujours appliquer "Qui ? Quoi ? De qui ?"
2. **Oublier les questions préalables** → Vérifier recevabilité AVANT le fond
3. **Confondre plusieurs questions** → Chaque rapport juridique = question séparée
4. **Utiliser des termes non juridiques** → Terminologie exacte des codes
5. **Négliger les délais** → Calculer précisément (notification → échéance)
6. **Négliger l'élément d'extranéité** → Vérifier LDIP si élément international

---

## Examples

📚 **4 exemples complets** sont documentés dans [EXAMPLES.md](./EXAMPLES.md) :

1. **Défaut de la chose vendue** (CO 197) - Questions multiples
2. **Recours administratif** (PA) - 4 niveaux de questions
3. **Droit pénal** (CP) - Gutachtenstil allemand
4. **Élément d'extranéité** (LDIP) - Questions internationales

---

## References

📖 **Sources complètes** dans [REFERENCE.md](./REFERENCE.md) :

**4 sources académiques primaires** :
- UNIL (Canapa) - Méthode de résolution de cas juridiques (2018)
- UZH (Thommen) - Fallbearbeitung im Strafrecht (2016)
- GAIUS (Roduit) - Résolution pratique de cas juridiques (2016)
- ODAGE (Genève) - Guide pratique examen du brevet d'avocat (2020)

**Bibliographie complémentaire** :
- Bohnet (dir.), *Actions civiles*, Helbing Lichtenhahn
- Valerius, *Einführung in den Gutachtenstil*, Springer (2017)
- Tercier/Roten, *La recherche et la rédaction juridiques*, Schulthess (2021)

---

## Related Skills

### Workflow Recommandé

1. **@extract-facts** (PRÉCÉDENT) → Extraction des faits
2. **@identify-legal-issues** (CETTE SKILL) ← Étape actuelle
3. **@analyse-cas-juridique** (SUIVANT) → Analyse juridique complète
4. **@recours-tf** (SI APPLICABLE) → Rédaction recours TF

### Autres Skills Connexes

- **@parse-decision** : Parser les décisions suisses depuis Entscheidsuche
- **@citation-formatter** : Formater les citations juridiques suisses
- **@recherche-juridique-suisse** (MOC) : Naviguer les ressources de recherche

---

## Version History

**v1.1** (27 février 2026) :
- Refactoring atomique : extraction des templates, pièges, exemples et références en annexes
- Réduction de 986 → ~250 lignes

**v1.0** (26 février 2026) :
- Implémentation initiale basée sur recherche Phase 5
- Méthodologie en 6 phases
- 12 pièges documentés
- 2 exemples complets

---

## Notes

### Avertissement

Cette skill est basée sur des **sources suisses exclusivement**. Le principe de **reformulation "Qui ? Quoi ? De qui ?"** est universel en Suisse romande, et correspond au **"Wer? Was? Von wem? Woraus?"** en Suisse alémanique.

### Principe Directeur

> **"Qui veut quoi de qui ?"** — La reformulation des questions en termes juridiques est **obligatoire** et **déterminante** pour la qualité de l'analyse juridique.

---

**Annexes** :
- [TEMPLATES.md](./TEMPLATES.md) — 8 templates de reformulation et structures
- [TRAPS.md](./TRAPS.md) — 12 pièges à éviter
- [EXAMPLES.md](./EXAMPLES.md) — 4 exemples complets
- [REFERENCE.md](./REFERENCE.md) — Sources académiques et bibliographie
