---
name: methodologie-recherche-jurisprudentielle
description: "Méthodologie de recherche jurisprudentielle suisse : méthode systématique en 5 étapes (analyse, opérationnalisation, traduction, choix du corpus, évaluation), méthode analogique (rétroprogressive et progressive), recherche thématique. Utiliser cette skill quand l'utilisateur doit mener une recherche jurisprudentielle structurée, trouver des arrêts pertinents sur un sujet donné, ou appliquer une méthodologie rigoureuse de recherche en droit suisse."
---

# Méthodologie de recherche jurisprudentielle

## Deux méthodes complémentaires

| Méthode | Approche | Quand l'utiliser |
|---------|----------|-----------------|
| **Systématique** | Partir du problème → formuler une requête → interroger les bases | Sujet nouveau, recherche exhaustive |
| **Analogique** | Partir d'un arrêt connu → remonter ou avancer dans les citations | Approfondir un sujet, trouver l'évolution d'une jurisprudence |

## Méthode systématique — 5 étapes

### Étape 1 : Analyser le problème
- Qualifier juridiquement les faits
- Identifier la ou les questions de droit
- Déterminer le domaine juridique concerné

### Étape 2 : Opérationnaliser la recherche
Transformer la question juridique en éléments de recherche :

**A. Références légales**
- Identifier les articles de loi potentiellement applicables
- Rechercher directement par référence : `"art. 41 CO"`, `"art. 28 CC"`

**B. Mots-clés et expressions**
- Extraire les termes juridiques pertinents
- Identifier les synonymes et termes associés
- Préparer des expressions exactes : `"responsabilité civile"`, `"tort moral"`

**C. Traduction des termes**
- Le droit suisse est **trilingue** : une recherche sérieuse doit couvrir FR, DE et IT
- Utiliser les outils de traduction juridique → skill `terminologie-juridique-multilingue`

**D. Choix du corpus et des champs**
- Base de données : bger.ch (gratuit), Swisslex (⚠️ payant — avancé)
- Période : restreindre ou élargir selon les besoins
- Juridiction : TF seul, ou inclure TAF/cantons
- Champs : plein texte, chapeau/sommaire, descripteurs Jurivoc

### Étape 3 : Formuler la requête
Appliquer les techniques de recherche → skill `techniques-recherche-juridique`

```
Exemple de construction progressive :
1. responsabilité → trop large
2. "responsabilité civile" → mieux
3. "responsabilité civile" AND "tort moral" → plus précis
4. ("responsabilité civile" OR Haftpflicht) AND ("tort moral" OR Genugtuung) → trilingue
5. Ajouter troncature : responsab* same (tort* near/5 moral*) → encore mieux
```

### Étape 4 : Exécuter et évaluer
- Trop de résultats → restreindre (ajouter termes, opérateurs de proximité, filtres)
- Pas assez de résultats → élargir (synonymes, troncature, supprimer filtres)
- Vérifier la **pertinence** des premiers résultats
- Identifier de nouveaux **mots-clés** dans les arrêts trouvés

### Étape 5 : Affiner et itérer
- Exploiter les mots-clés découverts dans les résultats
- Croiser avec d'autres bases de données
- Passer à la méthode analogique pour approfondir

## Méthode analogique

### Rétroprogressive (remonter dans le temps)
1. Partir d'un **arrêt récent** pertinent
2. Consulter les **références citées** dans les considérants
3. Remonter aux arrêts fondamentaux plus anciens
4. Identifier la **jurisprudence constante** et les **revirements**

> **Avantage** : on suit le raisonnement du TF lui-même pour trouver les arrêts qu'il considère comme pertinents.

### Progressive (avancer dans le temps)
1. Partir d'un **arrêt fondamental** plus ancien
2. Utiliser la fonction Swisslex (⚠️ payant) **« Document cité dans »**
3. Trouver tous les arrêts ultérieurs qui citent cet arrêt
4. Suivre l'**évolution** de la jurisprudence

> **Avantage** : découvrir si la jurisprudence a évolué, été nuancée ou renversée.

## Recherche thématique

Pour des domaines spécialisés, utiliser les ressources dédiées :
- Filtrage par **domaine juridique** dans Swisslex (⚠️ payant — 15+ catégories)
- Portails spécialisés (VLP-ASPAN pour l'aménagement, DEP pour l'environnement)
- Revues spécialisées par domaine

## Obligation de recherche du praticien

Le TF a posé le principe d'une obligation pour l'avocat de connaître la jurisprudence récente (art. 398 al. 2 CO). L'ATF 134 III 534 a précisé que la publication au recueil officiel ATF est le seuil de référence pour imputer la connaissance d'une nouvelle jurisprudence.

## Exemples pratiques détaillés

Pour des exemples pas-à-pas complets (résiliation de bail, responsabilité du médecin, méthode analogique rétroprogressive et progressive) → voir `references/exemples-pratiques.md`
