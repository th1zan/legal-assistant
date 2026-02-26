---
name: jurisprudence-suisse
description: "Recherche de jurisprudence suisse : arrêts du Tribunal fédéral (ATF), Tribunal administratif fédéral (ATAF), Tribunal pénal fédéral (TPF), jurisprudence cantonale, JAAC. Structure des arrêts, numérotation des cours, codes de référence. Utiliser cette skill quand l'utilisateur cherche un arrêt, veut comprendre la structure d'une décision du TF, identifier une cour par son code, ou rechercher de la jurisprudence cantonale."
---

# Jurisprudence suisse

## Tribunal fédéral (TF)

### Structure d'un arrêt publié aux ATF

```
Arrêt du Tribunal fédéral
├── Désignation de la cour
├── Date de la décision
├── Désignation des parties
├── Chapeau (sommaire trilingue FR/DE/IT)
│   ├── Mots-clés + dispositions légales appliquées
│   └── Résumé des principaux résultats
├── Questions de recevabilité
└── Questions de fond (considérants)
```

> Le **chapeau** n'existe que pour les arrêts publiés au recueil officiel (5-10% des arrêts). Les arrêts en ligne n'ont pas de sommaire.

### Publication
- **Recueil officiel (ATF)** : ~5-10% des arrêts (arrêts « de principe »)
- **Base de données bger.ch** : tous les arrêts depuis 2000, ATF depuis 1954
- Langue : langue originale de la procédure ; seul le chapeau est traduit

### Cinq parties du recueil ATF
| Partie | Domaine | Depuis |
|--------|---------|--------|
| I | Droit constitutionnel | 1995 (vol. 121) |
| II | Droit administratif, droit international public | 1995 |
| III | Droit civil, LP | 1995 |
| IV | Droit pénal, exécution des peines | 1942 |
| V | Droit des assurances sociales | 1970 (vol. 96) |

### Codes de référence des arrêts non publiés

Format depuis 2007 : **`pQ_r/s`**

**p = numéro de la Cour** :
| Code | Cour |
|------|------|
| 1 | 1ère Cour de droit public |
| 2 | 2ème Cour de droit public |
| 4 | 1ère Cour de droit civil |
| 5 | 2ème Cour de droit civil |
| 6 | Cour de droit pénal |
| 8 | 1ère Cour de droit social |
| 9 | 2ème Cour de droit social |

**Q = type de procédure** :
| Lettre | Procédure |
|--------|-----------|
| A | Recours en matière civile |
| B | Recours en matière pénale |
| C | Recours en matière de droit public |
| D | Recours constitutionnel subsidiaire |
| F | Révision |

**r** = n° d'ordre du dossier | **s** = année d'arrivée

> Exemple : `4A_31/2007` = 31e recours en matière civile de 2007 auprès de la 1ère Cour de droit civil.

### Recherche sur bger.ch

Deux modes :
1. **Gratuit** : recherche plein texte avec `+`, `-`, `"..."` ; résultats en 3 listes (exact, approx., partiel)
2. **Payant** ⚠️ : recherche structurée par descripteurs Jurivoc, champs (date, cour, domaine), répertoire — accessible via universités ou abonnement

Pour les techniques de recherche avancée → skill `techniques-recherche-juridique`
Pour la recherche sur Swisslex → skill `bases-donnees-juridiques`

## Outils d'accès

### MCP Server entscheidsuche (recommandé)

Le MCP server `entscheidsuche` permet une recherche programmatique dans la jurisprudence suisse (TF, TAF, TPF, cantons).

**Outils disponibles** :
- `search_decisions` : Recherche par texte, tribunal, date, canton
- `get_decision` : Récupérer le texte complet d'un arrêt

**Exemple** :
```
# Recherche d'arrêts du TF sur la responsabilité civile
search_decisions(query="responsabilité civile", court="CH_BGer")

# Jurisprudence cantonale genevoise
search_decisions(query="bail", court="CH_GE")
```

**Codes des tribunaux** : `CH_BGer` (TF), `CH_BVGer` (TAF), `CH_BStGer` (TPF), `CH_{canton}` (ex: `CH_GE`, `CH_VD`)

→ Pour la documentation complète des outils : skill `@outils-recherche-juridique`
→ Pour les workflows détaillés entscheidsuche : skill `@swiss-case-law-research`

## Autres juridictions fédérales

| Juridiction | Abrév. | Depuis | Publication |
|-------------|--------|--------|-------------|
| Tribunal pénal fédéral | TPF | 2004 | bstger.ch + Recueil TPF |
| Tribunal administratif fédéral | ATAF | 2007 | bvger.ch + Recueil ATAF |
| Tribunal militaire de cassation | ATMC | 1915 | Publication spécifique |
| Autorités administratives (JAAC) | JAAC | — | En ligne depuis 2007 uniquement |

## Jurisprudence cantonale

- Publiée dans les **recueils cantonaux** officiels ou officieux
- Revues à vocation nationale : RSJ, PJA
- Recherche via **Swisslex** (⚠️ payant — jurisprudence cantonale indexée) ou sites cantonaux
- Pour Genève : SJ (Semaine judiciaire), RDAF

Pour les conventions de citation → skill `citation-juridique-suisse`
Pour la méthodologie de recherche → skill `methodologie-recherche-jurisprudentielle`

## Guide détaillé bger.ch

Pour le guide pas-à-pas de la recherche avancée sur bger.ch (⚠️ section payante, répertoires, recherche experte structurée, outils supplémentaires) → voir `references/bger-recherche-avancee.md`
