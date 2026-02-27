---
name: swiss-case-law-research
description: Recherche structurée dans la jurisprudence suisse via Entscheidsuche.ch. Utiliser cette skill quand l'utilisateur cherche des arrêts du Tribunal fédéral, de la jurisprudence cantonale, ou des précédents judiciaires sur un sujet juridique suisse. Accès à plus d'1 million de décisions de justice.
version: 1.1
author: SwissLawAI
tags: [jurisprudence, recherche, tribunal-federal, mcp, entscheidsuche]
---

# Swiss Case Law Research

Recherche structurée dans la jurisprudence suisse via Entscheidsuche.ch

## Description

Cette skill guide la recherche de décisions de justice suisses en utilisant le serveur MCP **entscheidsuche**. Elle fournit des stratégies optimisées pour naviguer dans une base de plus de **1 million de décisions**.

## Capacités

- 🔍 Recherche avancée dans toutes les juridictions suisses
- 📊 Filtrage par tribunal, date, canton
- 📄 Récupération de documents complets (JSON, HTML, PDF)
- 🎯 Stratégies de recherche pour différents cas d'usage
- 🏛️ Connaissance de la structure judiciaire suisse

## Quand Utiliser

Invoquer `@swiss-case-law-research` quand l'utilisateur demande:
- "Cherche des décisions sur [sujet juridique]"
- "Trouve des arrêts du Tribunal fédéral sur [thème]"
- "Quelle est la jurisprudence sur [question]"
- "Y a-t-il des cas récents concernant [domaine]"

---

## Workflow de Recherche

### Phase 1: Exploration

1. **Comprendre la demande**
   - Identifier le domaine juridique
   - Extraire les mots-clés principaux
   - Déterminer la juridiction pertinente

2. **Première requête** (termes larges, en allemand)
   ```json
   {
     "query": "[termes principaux]",
     "size": 20
   }
   ```

### Phase 2: Analyse des Résultats

1. **Évaluer la pertinence**
   - Lire les abstracts des 5-10 premiers résultats
   - Identifier termes et tribunaux récurrents

2. **Évaluer le volume**
   - >500 résultats → affiner
   - <10 résultats → élargir
   - 10-100 résultats → approfondir

### Phase 3: Affinement

**Si TROP de résultats:**
- Ajouter termes spécifiques (AND)
- Filtrer par juridiction (`court:CH_BGer`)
- Restreindre la période

**Si PAS ASSEZ de résultats:**
- Utiliser wildcards (`protect*`)
- Essayer synonymes juridiques
- Rechercher en plusieurs langues

### Phase 4: Récupération des Documents

1. Sélectionner **3-5 décisions** les plus pertinentes
2. Privilégier: BGE > BGer > Cantonal
3. Récupérer le contenu complet:
   ```json
   {
     "signature": "[signature]",
     "format": "json"
   }
   ```

### Phase 5: Synthèse

1. Structurer la réponse selon le template
2. Citer correctement (signature, date, tribunal)
3. Appliquer au cas de l'utilisateur
4. Suggérer recherches complémentaires

---

## Stratégies de Recherche

### 1. Recherche Exploratoire
- Requête large avec termes principaux
- Limiter à 20-30 résultats
- Analyser la distribution

### 2. Recherche de Précédent Spécifique
- Identifier éléments clés du cas
- Construire requête combinée (AND)
- Commencer par BGer pour jurisprudence de principe

### 3. Recherche par Article de Loi
- Format: `"Art. [numéro] [abréviation]"`
- Exemple: `"Art. 328 OR" AND "protection personnalité"`

### 4. Recherche Multilingue
- **Allemand** (70% des décisions) - prioritaire
- **Français** (25%) - complémentaire
- **Italien** (5%) - si pertinent

→ Voir `REFERENCE.md` pour vocabulaire trilingue

---

## Syntaxe de Recherche

| Opérateur | Syntaxe | Exemple |
|-----------|---------|---------|
| ET | `AND` | `Datenschutz AND Arbeitsrecht` |
| OU | `OR` | `Kündigung OR licenciement` |
| NON | `-` | `Datenschutz -Strafrecht` |
| Phrase | `"..."` | `"protection personnalité"` |
| Wildcard | `*` | `Kündig*` |
| Champ | `field:value` | `court:CH_BGer` |

---

## Commandes MCP

### search_case_law
```json
{
  "query": "string (required)",
  "size": "number (default: 10, max: 50)",
  "from": "number (default: 0)"
}
```

### get_document
```json
{
  "signature": "string (required)",
  "spider": "string (optional)",
  "format": "'json' | 'html' | 'pdf' (default: 'json')"
}
```

### list_courts
Liste tous les tribunaux disponibles avec statistiques.

---

## Hiérarchie des Sources

| Priorité | Source | Autorité |
|----------|--------|----------|
| **1** | BGE (publiés) | Maximale |
| **2** | BGer (non publiés) | Haute |
| **3** | TAF/TPF | Fédérale spécialisée |
| **4** | Cantonaux | Locale |

→ Voir `REFERENCE.md` pour codes complets des tribunaux

---

## Bonnes Pratiques

### ✅ DO

1. **Commencer large, affiner progressivement**
2. **Utiliser l'allemand en priorité** (70% des décisions)
3. **Limiter les résultats** (20-30 exploration, max 50)
4. **Privilégier décisions récentes** (5 dernières années)
5. **Citer correctement** (signature, date, tribunal)
6. **Structurer la réponse** (vue d'ensemble, décisions clés, synthèse)

### ❌ DON'T

1. **Ne pas récupérer trop de documents** (max 5 complets)
2. **Ne pas ignorer la hiérarchie** (BGE > BGer > Cantonal)
3. **Ne pas traduire littéralement** (utiliser termes juridiques natifs)
4. **Ne pas sur-généraliser** (vérifier cohérence avec autres arrêts)
5. **Ne pas oublier les limites** (avertissement obligatoire)

→ Voir `TRAPS.md` pour les 10 pièges détaillés

---

## Format de Réponse

```markdown
# Recherche Jurisprudentielle : [Sujet]

## 📊 Vue d'Ensemble
- **Décisions trouvées** : [nombre]
- **Période couverte** : [années]
- **Principales juridictions** : [tribunaux]

## ⚖️ Décisions Clés

### 1. [Signature]
**Tribunal** : [Nom]
**Date** : [Date]
**Principe** : [Règle dégagée]

[Répéter pour 2-3 décisions]

## 📝 Synthèse
[Principes généraux dégagés]

## ⚠️ Avertissement
Ces informations ne constituent pas un avis juridique.
```

→ Voir `TEMPLATES.md` pour templates complets

---

## Annexes

| Fichier | Contenu |
|---------|---------|
| `TEMPLATES.md` | Templates de rapports et fiches de décision |
| `TRAPS.md` | 10 pièges à éviter avec solutions |
| `EXAMPLES.md` | 4 exemples complets de workflows |
| `REFERENCE.md` | Structure judiciaire, codes tribunaux, API MCP |

---

## Skills Connexes

| Skill | Usage |
|-------|-------|
| `@swiss-legal-commentary` | Recherche doctrine (Onlinekommentar) |
| `@parse-decision` | Parsing décisions TF/TAF |
| `@citation-formatter` | Formatage citations ATF, RS |
| `@recherche-juridique-suisse` | MOC navigation recherche juridique |

---

## Avertissement

⚠️ Les résultats de recherche sont **indicatifs, non exhaustifs**. Pour des conseils juridiques spécifiques, consultez un avocat qualifié.

---

*Version 1.1 — Février 2026*
