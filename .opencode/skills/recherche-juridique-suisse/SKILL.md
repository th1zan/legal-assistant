---
name: recherche-juridique-suisse
description: "Carte de navigation (MOC) pour la recherche juridique suisse informatisée. Utiliser cette skill quand l'utilisateur pose une question de droit suisse, cherche une loi, un arrêt, de la doctrine, ou a besoin d'aide pour formuler une recherche juridique. Cette skill oriente vers les skills spécialisées appropriées : sources législatives, jurisprudence, doctrine, bases de données, citations, méthodologie, droit cantonal, droit international, terminologie multilingue et veille juridique."
---

# Recherche juridique suisse — Carte de navigation

Cette skill est le point d'entrée pour toute recherche juridique en droit suisse. Elle oriente vers la skill spécialisée adaptée au besoin.

> **Source** : Flückiger/Krähenbühl, *Recherche juridique informatisée*, Université de Genève, 2011-2012.

## Arbre de décision

Identifier le besoin de l'utilisateur, puis charger la skill correspondante :

| Besoin | Skill à charger |
|--------|-----------------|
| Chercher une **loi fédérale** (RS, RO, FF) | `sources-legislatives-federales` |
| Chercher une **loi cantonale** ou intercantonal | `droit-cantonal-intercantonal` |
| Chercher un **arrêt** (TF, TAF, TPF, cantonal) | `jurisprudence-suisse` |
| Comprendre la **méthode** de recherche (systématique, analogique) | `methodologie-recherche-jurisprudentielle` |
| Utiliser une **base de données** (Swisslex, bger.ch, Lexfind) | `bases-donnees-juridiques` |
| Formuler une requête avec **opérateurs booléens** / troncature | `techniques-recherche-juridique` |
| **Citer** correctement une source (loi, arrêt, doctrine) | `citation-juridique-suisse` |
| Chercher de la **doctrine** (ouvrages, articles, revues) | `sources-doctrinales` |
| Traduire un **terme juridique** (FR/DE/IT) | `terminologie-juridique-multilingue` |
| Chercher du **droit international** / traités / CEDH | `droit-international-suisse` |
| Mettre en place une **veille juridique** | `veille-juridique` |

## Réflexe de base du juriste

Toute recherche juridique suit ce schéma fondamental :

```
1. Qualifier le problème juridique
2. Identifier les sources pertinentes (loi → jurisprudence → doctrine)
3. Formuler la requête (mots-clés, opérateurs, multilinguisme)
4. Choisir l'outil adapté (gratuit vs payant, officiel vs privé)
5. Évaluer les résultats et affiner
```

## Les trois piliers des sources juridiques suisses

```
Sources juridiques suisses
├── Législation (lois, ordonnances, Constitution)
│   ├── Fédérale → sources-legislatives-federales
│   ├── Cantonale → droit-cantonal-intercantonal
│   └── Internationale → droit-international-suisse
├── Jurisprudence (arrêts, décisions)
│   └── → jurisprudence-suisse
└── Doctrine (ouvrages, articles, commentaires)
    └── → sources-doctrinales
```

## Combinaisons fréquentes

- **Recherche complète sur un article de loi** : charger `sources-legislatives-federales` + `jurisprudence-suisse` + `citation-juridique-suisse`
- **Recherche avancée Swisslex** : charger `bases-donnees-juridiques` + `techniques-recherche-juridique`
- **Recherche en allemand d'un concept français** : charger `terminologie-juridique-multilingue` + `techniques-recherche-juridique`
