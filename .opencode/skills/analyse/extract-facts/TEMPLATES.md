# Templates - Extract Facts

Templates structurés pour l'extraction de faits juridiquement pertinents selon la méthodologie suisse.

---

## Template 1: Section PARTIES

```markdown
### PARTIES

- **[Lettre/Nom] ([Abréviation])**: [Qualification juridique]
  - Statut: [Personne physique / Personne morale + forme juridique]
  - Domicile/Siège: [Ville/Canton]
  - [Infos supplémentaires: nationalité, âge si pertinent, etc.]

- **[Lettre/Nom] ([Abréviation])**: [Qualification juridique]
  - Statut: [Personne physique / Personne morale + forme juridique]
  - Domicile/Siège: [Ville/Canton]
  - [Infos supplémentaires]
```

### Qualifications juridiques par domaine

| Domaine | Partie 1 | Partie 2 |
|---------|----------|----------|
| **Vente (CO 184)** | Vendeur | Acquéreur |
| **Bail (CO 253)** | Bailleur | Locataire |
| **Travail (CO 319)** | Employeur | Travailleur |
| **Mandat (CO 394)** | Mandant | Mandataire |
| **Entreprise (CO 363)** | Maître de l'ouvrage | Entrepreneur |
| **Prêt (CO 305/312)** | Prêteur | Emprunteur |
| **RC délictuelle (CO 41)** | Auteur du dommage | Lésé |
| **Pénal (CP)** | Auteur / Prévenu | Victime / Lésé |
| **Procédure civile** | Demandeur | Défendeur |
| **Recours** | Recourant | Intimé |

---

## Template 2: Section CHRONOLOGIE

```markdown
### CHRONOLOGIE

| Date | Événement | Pertinence Juridique |
|------|-----------|---------------------|
| [Date 1] | [Description événement juridique] | ✓ [Norme/élément] |
| [Date 2] | [Description événement juridique] | ✓ [Norme/élément] |
| [Date 3] | [Description événement juridique] | ✓ [Norme/élément] |
| [Date actuelle] | [Contexte actuel] | ✓ [Question juridique] |

**Délais calculés**:
- Entre [Date 1] et [Date 2]: X jours/mois
- Délai légal applicable: [Art. Y: Z jours/mois]
- Statut: [Délai respecté / expiré / en cours]
```

### Calcul des délais - Règles

| Type de délai | Base légale | Durée | Computation |
|---------------|-------------|-------|-------------|
| Avis des défauts | CO 201 | Immédiat | Dès découverte |
| Prescription vente | CO 210 | 2 ans | Dès livraison |
| Prescription RC | CO 60 | 3 ans / 10 ans | Dès connaissance / dès acte |
| Recours TF | LTF 100 | 30 jours | Dès notification |
| Recours TAF | LTAF 50 | 30 jours | Dès notification |
| Congé bail | CO 266a | 3 mois | Terme local usuel |

---

## Template 3: Section FAITS RECHTSERHEBLICH

```markdown
### FAITS JURIDIQUEMENT PERTINENTS (RECHTSERHEBLICH)

#### A. Éléments Constitutifs [du contrat / du délit / de l'infraction]

**Éléments objectifs**:
1. **[Tatbestandsmerkmal 1]**: [Fait correspondant du cas]
2. **[Tatbestandsmerkmal 2]**: [Fait correspondant du cas]
3. **[Tatbestandsmerkmal 3]**: [Fait correspondant du cas]

**Éléments subjectifs**:
1. **Intention (Vorsatz)**: [Ce que l'auteur savait/voulait]
2. **Connaissance**: [Ce que l'auteur connaissait ou devait connaître]
3. **Bonne/Mauvaise foi**: [État d'esprit juridiquement pertinent]
4. **Dol (Absicht)**: [But/objectif de l'auteur]

**Causalité**:
1. **Lien causal**: [Connexion causale entre acte et résultat]
2. **Causalité naturelle**: [Condition sine qua non]
3. **Causalité adéquate**: [Prévisibilité]

#### B. Éléments Extinctifs/Modificatifs (si applicable)

- **Paiement**: [Date, montant, méthode]
- **Prescription**: [Statut du délai]
- **Résiliation**: [Date, forme, motifs]
- **Compensation**: [Créances réciproques]

#### C. Éléments Justificatifs (si applicable)

- **Consentement**: [Consentement de la victime?]
- **État de nécessité (Notstand)**: [Danger, proportionnalité, subsidiarité]
- **Légitime défense (Notwehr)**: [Attaque, défense proportionnée]

#### D. Éléments Procéduraux

- **Compétence territoriale**: [For basé sur domicile/siège]
- **Valeur litigieuse**: [Montant] → [Type de procédure]
- **Conciliation préalable**: [Obligatoire? Effectuée?]
- **Qualité pour agir**: [Légitimation du demandeur]
- **Délais de recours**: [Statut des délais]
- **Élément d'extranéité**: [Élément international? LDIP applicable?]
```

---

## Template 4: Section FAITS ÉLIMINÉS

```markdown
### FAITS ÉLIMINÉS (Non Rechtserheblich)

Les faits suivants ont été omis car non juridiquement pertinents:

- ❌ "[Citation du cas]" → [Raison: émotion / anecdote / détail narratif]
- ❌ "[Citation du cas]" → [Raison: appréciation subjective]
- ❌ "[Citation du cas]" → [Raison: sans lien avec les éléments constitutifs]

**Exception**: Les faits suivants ont été CONSERVÉS malgré leur apparence contextuelle:

- ✅ "[Citation du cas]" → [Raison: pertinent pour élément subjectif / bonne foi / intention]
```

### Catégories de faits à éliminer

| Catégorie | Exemples | Exception |
|-----------|----------|-----------|
| **Émotions** | "A était ravi", "B était furieux" | Si révèle intention/connaissance |
| **Couleur narrative** | "par une belle journée d'été" | Jamais |
| **Appréciations subjectives** | "le vendeur, très sympathique" | Jamais |
| **Détails non pertinents** | Capital social (si non pertinent) | Si pertinent pour responsabilité |
| **Répétitions** | Paraphrases de faits déjà cités | Jamais |

---

## Template 5: Output Complet

```markdown
# EXTRACTION DES FAITS JURIDIQUES

**Cas**: [Titre/description brève du cas]  
**Domaine**: [Domaine juridique: CO, CP, CC, CPC, PA, etc.]  
**Date d'analyse**: [Date]

---

## I. ÉVALUATION INITIALE

[Résumé 2-3 phrases: domaine juridique, parties, question juridique apparente]

---

## II. PARTIES

[Tableau ou liste avec détails des parties selon Template 1]

---

## III. CHRONOLOGIE

[Tableau chronologique avec dates, événements et pertinence juridique selon Template 2]

**Délais calculés**:
[Calculs de délais et statuts par rapport aux délais légaux]

---

## IV. FAITS JURIDIQUEMENT PERTINENTS (RECHTSERHEBLICH)

[Structure complète selon Template 3]

---

## V. FAITS ÉLIMINÉS (Non Rechtserheblich)

[Liste des faits non pertinents avec justification selon Template 4]

---

## VI. REFORMULATION JURIDIQUE (Optionnel)

[Reformulation structurée du Sachverhalt si demandée]

---

## VII. PROCHAINES ÉTAPES

**Recommandations**:
- [ ] Identifier les questions juridiques avec `@identify-legal-issues`
- [ ] Procéder à l'analyse juridique avec `@analyse-cas-juridique`
- [ ] [Autres étapes spécifiques selon le type de cas]

**Lacunes identifiées** (faits manquants):
- [Liste des faits manquants à clarifier avec le client]
```

---

## Template 6: Reformulation Juridique

```markdown
### REFORMULATION JURIDIQUE DU SACHVERHALT

**I. Parties**
[Qualifications juridiques précises]

**II. Faits Constitutifs**
[Événements juridiques en ordre chronologique avec terminologie légale]

**III. Éléments Subjectifs**
[Intention, connaissance, bonne/mauvaise foi]

**IV. Situation Actuelle**
[État actuel et question juridique posée]

**Caractéristiques**:
- ✅ Terminologie juridique précise
- ✅ Chronologie exacte avec dates calculées
- ✅ Éléments constitutifs identifiés
- ✅ Faits procéduraux inclus
- ❌ Émotions et anecdotes éliminées
```

---

## Checklist Qualité

Avant de finaliser l'extraction, vérifier:

### Parties
- [ ] Toutes les parties identifiées avec qualification juridique
- [ ] Domicile/siège précisé (compétence territoriale)
- [ ] Forme juridique des personnes morales indiquée

### Chronologie
- [ ] Dates exactes (pas de "quelques jours plus tard")
- [ ] Délais calculés avec statut (respecté/expiré)
- [ ] Jours fériés vérifiés si pertinent

### Faits Rechtserheblich
- [ ] Éléments objectifs mappés aux Tatbestandsmerkmale
- [ ] Éléments subjectifs identifiés (intention, connaissance)
- [ ] Causalité établie
- [ ] Éléments procéduraux extraits

### Élimination
- [ ] Émotions éliminées (sauf si révèlent intention)
- [ ] Anecdotes éliminées
- [ ] Répétitions supprimées

### International
- [ ] Éléments d'extranéité identifiés
- [ ] LDIP mentionnée si applicable
