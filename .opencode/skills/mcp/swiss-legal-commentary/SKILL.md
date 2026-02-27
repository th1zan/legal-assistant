---
name: swiss-legal-commentary
description: Recherche structurée dans les commentaires juridiques suisses via Onlinekommentar.ch. Utiliser cette skill quand l'utilisateur demande d'expliquer un article de loi, cherche la doctrine juridique, ou veut comprendre l'interprétation académique d'une disposition légale suisse. Commentaires Open Access en DE, FR, IT, EN.
---

# Swiss Legal Commentary Research

Recherche structurée dans les commentaires juridiques suisses via Onlinekommentar.ch.

## Description

Cette skill guide l'agent dans la recherche de commentaires doctrinaux suisses en utilisant le serveur MCP **onlinekommentar**. Elle fournit des stratégies optimisées pour accéder à des commentaires juridiques de haute qualité, rédigés par des universitaires et praticiens reconnus.

## Capacités

- Accès à des commentaires doctrinaux de qualité académique
- Recherche multilingue (DE, FR, IT, EN)
- Commentaires article par article sur les lois suisses
- Accès aux auteurs et éditeurs académiques
- Références croisées avec jurisprudence et doctrine

## Quand Utiliser

Invoquez cette skill quand l'utilisateur demande :
- "Explique-moi l'article [X] de [loi]"
- "Quels sont les commentaires sur [sujet juridique]"
- "Que dit la doctrine sur [question]"
- "Trouve-moi des analyses juridiques sur [thème]"
- "Comment interpréter [article de loi]"

## Outils MCP Disponibles

### search_commentaries

Recherche dans la base de commentaires juridiques.

**Paramètres** :
- `search` (requis) : Requête de recherche full-text
- `language` (optionnel) : `de`, `fr`, `it`, `en`
- `legislative_act` (optionnel) : ID de l'acte législatif
- `sort` (optionnel) : `title`, `-title`, `date`, `-date`
- `page` (optionnel) : Page pour pagination

### get_commentary_by_id

Récupère le contenu complet d'un commentaire spécifique.

**Paramètres** :
- `id` (requis) : UUID du commentaire

## Stratégies de Recherche

### 1. Recherche par Article de Loi

**Objectif** : Trouver le commentaire d'un article spécifique.

**Processus** :
1. Identifier la référence exacte : "Art. 328 CO"
2. Construire la requête : `"328 Code Obligations"` ou `"328 OR"` (allemand)
3. Filtrer par langue si nécessaire
4. Récupérer le commentaire complet via `get_commentary_by_id`

### 2. Recherche Thématique

**Objectif** : Trouver tous les commentaires sur un sujet donné.

**Processus** :
1. Recherche large initiale (ex: "protection données personnelles")
2. Analyser la distribution par loi
3. Affiner par `legislative_act` si nécessaire
4. Sélectionner les 3-5 commentaires les plus pertinents

### 3. Recherche Multilingue

**Objectif** : Couvrir toutes les perspectives linguistiques.

**Processus** :
1. Exécuter recherches séparées par langue
2. Comparer les résultats et auteurs
3. Synthétiser avec mention de disponibilité par langue

### 4. Recherche par Auteur

**Processus** :
1. Rechercher par nom d'auteur
2. Le système cherche dans `authors` et `editors`
3. Combiner avec thème si nécessaire

## Workflow Recommandé

### Phase 1 : Identification
- Question = article spécifique ou thème général ?
- Langue préférée ?
- Niveau de détail souhaité ?

### Phase 2 : Recherche Initiale
```json
{
  "search": "[termes]",
  "language": "fr",
  "sort": "-date"
}
```

**Évaluation** :
- 0 résultats → élargir recherche
- 1-10 résultats → parfait
- >20 résultats → affiner avec `legislative_act`

### Phase 3 : Sélection
- Maximum 3-5 commentaires à analyser
- Privilégier : récents, auteurs reconnus, pertinents
- Récupérer contenu complet via `get_commentary_by_id`

### Phase 4 : Synthèse
- Vue d'ensemble du sujet
- Analyse de chaque commentaire
- Consensus et débats doctrinaux
- Application au cas de l'utilisateur
- Citation correcte (auteur, titre, date, lien)

## Combinaison avec Jurisprudence

Workflow intégré recommandé :

```
1. DOCTRINE (cette skill)
   → Cadre juridique et principes
   → Noter les ATF/BGE mentionnés

2. JURISPRUDENCE (@swiss-case-law-research)
   → Rechercher arrêts mentionnés
   → Vérifier jurisprudence récente

3. SYNTHÈSE
   → Doctrine + Jurisprudence
   → Cohérence ou divergence
   → Application pratique
```

## Gestion des Limitations

### Plateforme en développement
- Couverture partielle : tous les articles ne sont pas commentés
- Lois prioritaires : Cst., CO, CC, CP, LPD
- Si pas de commentaire : mentionner explicitement, proposer alternatives

### Langue de publication
- Pas tous les commentaires dans toutes les langues
- Si commentaire uniquement en allemand : le mentionner
- Proposer traduction des concepts clés

### Commentaires anciens
- Toujours mentionner la date
- Compléter avec jurisprudence récente si nécessaire

## Meilleures Pratiques

### À FAIRE
- Commencer spécifique si article connu
- Vérifier les auteurs (reconnus = qualité)
- Lire le texte de loi d'abord
- Noter les références jurisprudentielles
- Privilégier commentaires récents (`sort: "-date"`)
- Citer correctement (auteur, titre, date, lien)

### À ÉVITER
- Ignorer la disponibilité linguistique
- Se limiter à un seul commentaire
- Négliger les éditeurs (validation académique)
- Oublier les articles connexes
- Substituer à un conseil juridique

## Ressources Complémentaires

### Fichiers Annexes (même dossier)
- **TEMPLATES.md** : Templates de présentation et requêtes
- **TRAPS.md** : Pièges courants et solutions
- **EXAMPLES.md** : Exemples complets de recherches
- **REFERENCE.md** : Documentation MCP et actes législatifs

### Skills Complémentaires
- `@swiss-case-law-research` : Jurisprudence TF/TAF/TPF
- `@parse-decision` : Extraction structurée d'arrêts
- `@citation-formatter` : Formatage citations juridiques

### Liens Externes
- Site : https://onlinekommentar.ch
- À propos : https://onlinekommentar.ch/de/ueber-onlinekommentar

---

**Version** : 2.0.0  
**Dernière mise à jour** : Février 2026  
**Auteur** : Legal Assistant Workspace
