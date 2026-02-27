# Exemples - Swiss Case Law Research

Exemples complets de workflows de recherche jurisprudentielle via Entscheidsuche.

---

## Exemple 1: Recherche Droit du Travail

### Demande Utilisateur
> "Je cherche des cas où un employeur a licencié quelqu'un pendant un arrêt maladie"

### Workflow de Recherche

#### Phase 1: Exploration
```json
{
  "query": "Kündigung Krankheit",
  "size": 30
}
```
**Résultat**: 850 décisions trouvées

#### Phase 2: Analyse Distribution
- BGer: 45%
- Cantons (ZH, BE, VD): 40%
- TAF: 15%
- Termes connexes: "Sperrfrist", "Arbeitsunfähigkeit", "fristlose"

#### Phase 3: Affinement
```json
{
  "query": "Kündigung Krankheit Sperrfrist",
  "size": 20
}
```
**Résultat**: 95 décisions ciblées

#### Phase 4: Sélection des Décisions Clés

**Décision 1**: BGE 128 III 212
- **Tribunal**: Tribunal fédéral
- **Date**: 15.05.2002
- **Principe**: La période de protection (Sperrfrist) de l'art. 336c CO suspend le délai de préavis mais n'empêche pas la notification du congé.

**Décision 2**: 4A_123/2023
- **Tribunal**: Tribunal fédéral
- **Date**: 12.09.2023
- **Principe**: L'employeur qui licencie pendant une période de protection doit prolonger le délai de congé en conséquence.

**Décision 3**: 4A_456/2022
- **Tribunal**: Tribunal fédéral
- **Date**: 28.03.2023
- **Principe**: La mauvaise foi de l'employeur peut conduire à qualifier le licenciement d'abusif même après la période de protection.

#### Phase 5: Recherche Complémentaire Français
```json
{
  "query": "licenciement maladie période protection",
  "size": 15
}
```

#### Rapport Final

```markdown
# Recherche: Licenciement pendant arrêt maladie

## Vue d'Ensemble
- **Décisions trouvées**: 95 (après affinement)
- **Période**: 2000-2024
- **Juridiction principale**: Tribunal fédéral (60%)

## Principes Juridiques Dégagés

### Protection légale (Art. 336c CO)
Le travailleur ne peut être licencié pendant:
- 30 jours la 1ère année de service
- 90 jours dès la 2ème année
- 180 jours dès la 6ème année

### Effets du licenciement notifié pendant protection
1. Le congé est **nul** s'il intervient pendant la période
2. S'il est notifié avant, le délai est **suspendu**
3. À la fin de la suspension, le délai reprend

### Licenciement abusif
- Même après la période de protection, un licenciement motivé par la maladie peut être abusif
- Indemnisation jusqu'à 6 mois de salaire (art. 336a CO)

## Application au Cas
[Appliquer selon faits spécifiques de l'utilisateur]
```

---

## Exemple 2: Recherche Protection des Données

### Demande Utilisateur
> "Quelles sont les sanctions pour violation du RGPD en Suisse?"

### Workflow de Recherche

#### Clarification Préalable
⚠️ La Suisse n'applique pas le RGPD mais la **LPD** (Loi sur la Protection des Données). Le RGPD peut s'appliquer si l'entreprise traite des données de résidents UE.

#### Phase 1: Recherche Sanctions LPD
```json
{
  "query": "Datenschutz Sanktion DSG",
  "size": 25
}
```

#### Phase 2: Recherche RGPD en Suisse
```json
{
  "query": "DSGVO Schweiz Sanktion",
  "size": 15
}
```

#### Décisions Clés

**BGE 147 I 47** (2021)
- Protection des données et libertés fondamentales
- Principe de proportionnalité

**4A_592/2020** (2021)
- Violation de la personnalité par traitement illicite de données
- Dommages-intérêts possibles

#### Rapport Final

```markdown
# Recherche: Sanctions protection des données en Suisse

## Cadre Juridique

### LPD (Droit suisse)
- **Sanctions pénales**: Amendes jusqu'à CHF 250'000 (nouvelle LPD 2023)
- **Sanctions civiles**: Dommages-intérêts, tort moral
- **Mesures administratives**: Injonctions du PFPDT

### RGPD (Si applicable)
- S'applique aux entreprises suisses traitant données UE
- Amendes jusqu'à 4% du CA mondial ou 20 Mio EUR

## Jurisprudence Pertinente
[Détails des décisions]

## ⚠️ Attention
La nouvelle LPD (sept. 2023) a renforcé les sanctions. 
Rechercher jurisprudence post-2023 pour cas actuels.
```

---

## Exemple 3: Recherche Droit Locatif

### Demande Utilisateur
> "Un propriétaire peut-il augmenter le loyer après des rénovations?"

### Workflow de Recherche

#### Phase 1: Termes Spécifiques
```json
{
  "query": "Mietzinserhöhung Renovation wertvermehrend",
  "size": 20
}
```

#### Phase 2: Avec Référence Légale
```json
{
  "query": "\"Art. 269a OR\" Renovation",
  "size": 15
}
```

#### Phase 3: Recherche Cantonale (si ZH mentionné)
```json
{
  "query": "Mietzinserhöhung Renovation court:CH_ZH",
  "size": 10
}
```

#### Décisions Clés

**BGE 118 II 415**
- **Principe**: Distinction entre réparations (maintien) et plus-values (Mehrwert)
- Seules les plus-values justifient une augmentation

**BGE 141 III 569**
- **Principe**: Calcul du loyer après travaux plus-values
- Méthode: Coût des travaux × taux d'intérêt + amortissement

**4A_200/2022**
- **Application récente**: Rénovation énergétique = plus-value
- Augmentation justifiée si amélioration réelle

#### Rapport Final

```markdown
# Recherche: Augmentation loyer après rénovations

## Principes Juridiques (Art. 269a CO)

### Travaux d'Entretien vs Plus-Values

| Type | Définition | Effet sur loyer |
|------|------------|-----------------|
| **Entretien** | Maintien de l'état | Pas d'augmentation |
| **Plus-value** | Amélioration | Augmentation possible |

### Calcul de l'Augmentation (Plus-values)
```
Augmentation = (Coût travaux × Taux d'intérêt) + Amortissement
```
- Taux d'intérêt: Taux hypothécaire de référence + marge
- Amortissement: Répartition sur durée de vie des installations

### Exemples de Plus-Values
- Rénovation cuisine/salle de bains
- Amélioration isolation (énergétique)
- Ajout balcon, ascenseur
- Modernisation chauffage

### Procédure
1. Notification formule officielle
2. Délai de contestation: 30 jours
3. Conciliation obligatoire

## Application
[Selon travaux spécifiques décrits par l'utilisateur]
```

---

## Exemple 4: Question Rapide (Citoyen)

### Demande Utilisateur
> "Mon voisin fait du bruit la nuit, que puis-je faire?"

### Workflow Simplifié

#### Recherche Ciblée
```json
{
  "query": "Lärmbelästigung Nachbar",
  "size": 10
}
```

#### Résumé Rapide

```markdown
## Bruit de voisinage - Options Légales

### Droit Civil (Art. 684 CC)
- **Immissions excessives**: Le voisin doit s'abstenir de nuisances excessives
- **Action en cessation**: Demander au juge d'ordonner l'arrêt

### Droit Locatif (si locataire)
- Signaler au bailleur (obligation de garantir jouissance paisible)
- Réduction de loyer possible si trouble persistant

### Voie Administrative
- Règlement communal sur le bruit
- Plainte à la police (bruit nocturne)

### Jurisprudence
Le TF considère que le bruit nocturne répété constitue une atteinte illicite aux droits de voisinage (BGE 126 III 223).

### 💡 Recommandation
1. Dialogue avec le voisin (solution amiable)
2. Si échec: médiation ou plainte au bailleur/commune
3. En dernier recours: action civile

⚠️ Consultez un avocat pour évaluer votre situation spécifique.
```

---

## Points Clés des Exemples

### Structure Constante

1. **Comprendre la demande** - Identifier le domaine et la question
2. **Requête exploratoire** - Large, en allemand
3. **Analyser et affiner** - Termes connexes, filtres
4. **Sélectionner décisions clés** - 3-5 maximum
5. **Synthétiser** - Principes + application au cas
6. **Avertir** - Toujours mentionner les limitations

### Adaptation au Public

| Public | Approche |
|--------|----------|
| **Avocat** | Recherche exhaustive, citations précises, nuances |
| **Juriste d'entreprise** | Focus pratique, compliance, risques |
| **Citoyen** | Vulgarisation, options concrètes, recommandation avocat |
| **Académique** | Analyse historique, évolution, statistiques |
