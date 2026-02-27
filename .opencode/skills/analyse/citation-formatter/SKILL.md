---
name: citation-formatter
description: Convertit les signatures Entscheidsuche et citations brutes en format standard suisse (ATF, ATAF, TPF). Utiliser cette skill quand l'utilisateur doit citer une décision de justice suisse, formater une référence jurisprudentielle, ou générer une bibliographie d'arrêts conforme aux standards académiques et judiciaires suisses.
---

# Skill : Formatage de Citations Juridiques

**Type** : Skill d'analyse atomique  
**Domaine** : Standards de citation juridique  
**Entrée** : Signature Entscheidsuche, citation brute, ou métadonnées de décision  
**Sortie** : Citation juridique suisse formatée (format ATF, ATAF, TPF)  
**Dépendances** : Standards de citation suisses (`.opencode/skills/recherche/citation-juridique-suisse`)

---

## Objectif

Convertir les signatures Entscheidsuche et les citations brutes en formats de citation juridique suisse standardisés, conformes aux standards académiques et judiciaires suisses.

**Capacités principales** :
- Convertir les signatures Entscheidsuche → Citations standards
- Formater les références ATF, ATAF, TPF
- Gérer le formatage des dates (FR/DE/IT)
- Générer les formats courts et longs
- Valider la structure des citations

---

## Quand Utiliser Cette Skill

**Déclencher cette skill quand** :
- Besoin de citer une décision de justice suisse dans un document juridique
- Conversion de signatures Entscheidsuche en citations lisibles
- Formatage de références jurisprudentielles pour une bibliographie
- Validation de la conformité du format de citation

**Exemples de déclencheurs** :
- « Formate cette citation : CH_BGer_007_7B-529-2025_2026-01-26 »
- « Convertis cette signature en format ATF »
- « Comment citer correctement cette décision ? »
- « Génère une entrée bibliographique pour cet arrêt »

---

## Exigences d'Entrée

Cette skill accepte **l'une des options suivantes** :

### Option 1 : Signature Entscheidsuche
```
Format : CH_BGer_007_7B-529-2025_2026-01-26
Codes tribunaux : CH_BGer (TF), CH_BVGE (TAF), CH_BstGer (TPF)
```

### Option 2 : Métadonnées de Décision Parsées
```json
{
  "signature": "CH_BGer_007_7B-529-2025_2026-01-26",
  "tribunal": "Tribunal fédéral",
  "chambre": "IIe Cour de droit pénal",
  "date": "2026-01-26"
}
```

### Option 3 : Citation Existante (pour validation/reformatage)
```
ATF 148 III 217
7B_529/2025
Arrêt du Tribunal fédéral 7B_529/2025 du 26 janvier 2026
```

---

## Format de Sortie

Retourne plusieurs formats de citation :

```json
{
  "signature": "CH_BGer_007_7B-529-2025_2026-01-26",
  "citations": {
    "standard": {
      "fr": "Arrêt du Tribunal fédéral 7B_529/2025 du 26 janvier 2026",
      "de": "Urteil des Bundesgerichts 7B_529/2025 vom 26. Januar 2026",
      "it": "Sentenza del Tribunale federale 7B_529/2025 del 26 gennaio 2026"
    },
    "court": {
      "fr": "ATF (à publier) 7B_529/2025",
      "de": "BGE (zur Publikation) 7B_529/2025",
      "it": "DTF (da pubblicare) 7B_529/2025"
    },
    "academique": {
      "fr": "ATF (à publier) 7B_529/2025 du 26 janvier 2026 consid. [X]",
      "de": "BGE (zur Publikation) 7B_529/2025 vom 26. Januar 2026 E. [X]",
      "it": "DTF (da pubblicare) 7B_529/2025 del 26 gennaio 2026 consid. [X]"
    },
    "bibliographie": {
      "fr": "Tribunal fédéral, arrêt 7B_529/2025 du 26 janvier 2026",
      "de": "Bundesgericht, Urteil 7B_529/2025 vom 26. Januar 2026",
      "it": "Tribunale federale, sentenza 7B_529/2025 del 26 gennaio 2026"
    }
  },
  "metadonnees": {
    "tribunal": "TF",
    "chambre": "IIe Cour de droit pénal",
    "numero": "7B_529/2025",
    "date": "2026-01-26",
    "est_publie": false
  },
  "validation": {
    "est_valide": true,
    "problemes": []
  }
}
```

---

## Standards de Citation

### Tribunal Fédéral (TF / Bundesgericht / Tribunale federale)

**ATF publiés** :
- `ATF 148 III 217` (FR)
- `BGE 148 III 217` (DE)
- `DTF 148 III 217` (IT)

**Décisions non publiées** :
- `Arrêt du Tribunal fédéral 7B_529/2025 du 26 janvier 2026` (FR)
- `Urteil des Bundesgerichts 7B_529/2025 vom 26. Januar 2026` (DE)
- `Sentenza del Tribunale federale 7B_529/2025 del 26 gennaio 2026` (IT)

**Forme courte** (références subséquentes) :
- `ATF 148 III 217` ou `7B_529/2025`

### Tribunal Administratif Fédéral (TAF / BVGer)

**ATAF publiés** :
- `ATAF 2024-IV-1` (FR/DE/IT même format)

**Décisions non publiées** :
- `Arrêt du Tribunal administratif fédéral A-1234/2025 du 15 mars 2026` (FR)
- `Urteil des Bundesverwaltungsgerichts A-1234/2025 vom 15. März 2026` (DE)

### Tribunal Pénal Fédéral (TPF / BStGer)

**TPF publiés** :
- `TPF 2025 5` (FR/DE/IT même format)

**Décisions non publiées** :
- `Arrêt du Tribunal pénal fédéral SK.2024.15 du 10 avril 2026` (FR)
- `Urteil des Bundesstrafgerichts SK.2024.15 vom 10. April 2026` (DE)

---

## Workflow

### Étape 1 : Parser la Signature

Extraire les composants de la signature Entscheidsuche :

```
CH_BGer_007_7B-529-2025_2026-01-26
│    │    │   │          │
│    │    │   │          └─ Date (AAAA-MM-JJ)
│    │    │   └─ Numéro de dossier
│    │    └─ Code chambre
│    └─ Code tribunal (BGer = Tribunal fédéral)
└─ Pays (CH)
```

**Correspondance des codes tribunaux** :
- `BGer` → Tribunal fédéral (TF)
- `BVGE` → Tribunal administratif fédéral (TAF)
- `BstGer` → Tribunal pénal fédéral (TPF)

### Étape 2 : Formater la Date

Convertir la date au format approprié pour chaque langue :

```python
date = "2026-01-26"

# Français : "26 janvier 2026"
# Allemand : "26. Januar 2026"
# Italien : "26 gennaio 2026"
```

### Étape 3 : Générer les Citations

Selon le type de tribunal et le statut de publication :

**Si publié** (ATF/ATAF/TPF) :
- Utiliser le format de référence officiel
- Inclure le volume et le numéro de page

**Si non publié** :
- Utiliser le format long avec tribunal, numéro de dossier, date
- Marquer comme « à publier » / « zur Publikation » si pertinent

### Étape 4 : Valider

Vérifier la structure de la citation :
- Format de date correct
- Numéro de dossier valide
- Code tribunal reconnu
- Cohérence linguistique

---

## Scripts Utilitaires

### format_citation.py

**Objectif** : Formateur de citations principal

**Utilisation** :
```bash
python scripts/format_citation.py --signature "CH_BGer_007_7B-529-2025_2026-01-26" --langue fr
python scripts/format_citation.py --numero-dossier "7B_529/2025" --tribunal TF --date "2026-01-26" --langue fr
python scripts/format_citation.py --valider "ATF 148 III 217"
```

**Formats de sortie** :
- `--format standard` → Citation standard complète (par défaut)
- `--format court` → Référence courte
- `--format academique` → Citation académique avec placeholder consid.
- `--format bibliographie` → Entrée bibliographique
- `--format tous` → Tous les formats (JSON)

---

## Intégration avec Autres Skills

### Skills Amont (Fournissent l'Entrée)
- `@parse-decision` → Extraire les métadonnées pour le formatage
- `@mcp/swiss-case-law-research` → Récupérer les décisions à citer

### Skills Aval (Utilisent la Sortie)
- `@analyse/recours-tf` → Formater les citations dans les recours
- `@redaction/avis-de-droit` → Formater les citations dans les avis
- `@redaction/memoire-reponse` → Formater les citations dans les mémoires

---

## Critères de Succès

Cette skill est réussie si :

1. Formate correctement 100% des signatures Entscheidsuche valides
2. Supporte les trois langues officielles (FR/DE/IT)
3. Gère tous les tribunaux fédéraux suisses (TF, TAF, TPF)
4. Valide les citations avec <5% de faux positifs/négatifs
5. Complète le formatage en <10ms par citation
6. La sortie est conforme aux standards de citation suisses

---

## Références

- **Skill Standards de Citation** : `.opencode/skills/recherche/citation-juridique-suisse/SKILL.md`
- **Guide de Citation Suisse** : https://www.uzh.ch/cmsssl/ius/dam/jcr:00000000-60c4-ec4f-0000-000061d78e87/Zitierregeln_Universit%C3%A4t_Z%C3%BCrich_2020.pdf

---

## Métadonnées

```yaml
nom_skill: citation-formatter
type_skill: atomique
domaine: analyse
version: 1.0.0
cree: 2026-02-26
dependances:
  - citation-juridique-suisse skill (référence)
sorties_pour:
  - recours-tf
  - avis-de-droit
  - memoire-reponse
statut: en_developpement
priorite: P0
```
