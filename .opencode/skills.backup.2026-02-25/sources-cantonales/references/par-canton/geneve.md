# Genève (GE) — Détails

## Législation

### Recueil systématique genevois

**URL** : [silgeneve.ch/legis](https://silgeneve.ch/legis)

**Structure** :
- Classification par domaine juridique (A à Z)
- Numérotation : ex. `F 1 05` (Loi sur la police)
- Versions consolidées disponibles

**Exemple de recherche** :
1. Accéder à silgeneve.ch/legis
2. Utiliser la recherche par mots-clés ou naviguer par domaine
3. Cliquer sur la loi pour voir le texte consolidé

### Journal officiel

**Feuille d'avis officielle (FAO)** : Publication hebdomadaire des actes officiels

---

## Travaux préparatoires

### Mémorial du Grand Conseil

**URL** : [ge.ch/grandconseil/memorial](https://www.ge.ch/grandconseil/memorial)

**Couverture** : Archives numérisées depuis **1901**

**Contenu** :
- Débats parlementaires intégraux
- Interventions des députés
- Votes et décisions

**Recherche** :
- Recherche plein texte disponible
- Filtrage par date, session, député

### Projets de loi

**URL** : [ge.ch/grandconseil/projets-loi](https://www.ge.ch/grandconseil)

**Contenu** :
- Texte du projet
- Exposé des motifs du Conseil d'État
- Numéro PL (ex: PL 12345)

### Rapports de commissions

- Rapports des commissions parlementaires
- Analyse des projets avant le vote en plénière
- Recommandations de vote

### Règlements du Conseil d'État

- Pas de débats parlementaires (compétence exécutive)
- Publication directe au Journal officiel

---

## Jurisprudence

### Accès via entscheidsuche

**Code spider** : `CH_GE_Cour`

**Exemple MCP** :
```
search_case_law(query="bail à loyer", spider="CH_GE_Cour", size=20)
```

### Revues de jurisprudence

| Revue | Couverture |
|-------|------------|
| **Semaine Judiciaire (SJ)** | Jurisprudence genevoise sélectionnée |
| **RDAF** | Droit administratif et fiscal |
| **Pratique Juridique Actuelle (PJA)** | Sélection nationale |

### Cour de justice

**Composition** :
- Chambre civile
- Chambre pénale
- Chambre administrative

**Publication** : Arrêts disponibles via entscheidsuche.ch

---

## Droit communal — Ville de Genève

### Recueil des règlements

**URL** : [geneve.ch/fr/autorites/conseil-municipal](https://www.geneve.ch/fr/autorites/conseil-municipal)

### Mémorial du Conseil municipal

Délibérations du Conseil municipal de la Ville de Genève

---

## Accès technique

| Type | Méthode | Détails |
|------|---------|---------|
| **Législation** | Web | silgeneve.ch/legis |
| **Jurisprudence** | MCP | `@entscheidsuche` (spider: `CH_GE_Cour`) |
| **Travaux prép.** | Web | ge.ch/grandconseil |
| **Droit communal** | Web | geneve.ch |

**API** : Pas d'API publique connue pour la législation genevoise.

---

## Citation

**Format** :
```
art. 15 LPol/GE (RS/GE F 1 05)
```

**Éléments** :
- Numéro d'article
- Abréviation de la loi + canton
- Numéro RS/GE entre parenthèses
