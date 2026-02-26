# Swiss Case Law Research

Recherche structurée dans la jurisprudence suisse via Entscheidsuche.ch

## Description

Cette skill guide l'agent dans la recherche de décisions de justice suisses en utilisant le serveur MCP **entscheidsuche**. Elle fournit des stratégies de recherche optimisées pour naviguer efficacement dans une base de données de plus de 1 million de décisions.

## Capacités

- 🔍 Recherche avancée dans toutes les juridictions suisses
- 📊 Filtrage par tribunal, date, canton
- 📄 Récupération de documents complets (JSON, HTML, PDF)
- 🎯 Stratégies de recherche pour différents cas d'usage
- 🏛️ Connaissance de la structure judiciaire suisse

## Quand Utiliser Cette Skill

Invoquez cette skill quand l'utilisateur demande :
- "Cherche des décisions sur [sujet juridique]"
- "Trouve des arrêts du Tribunal fédéral sur [thème]"
- "Quelle est la jurisprudence sur [question]"
- "Y a-t-il des cas récents concernant [domaine]"
- "Montre-moi des exemples de décisions sur [topic]"

## Structure Judiciaire Suisse

### Juridictions Fédérales (Codes Spider)

| Code Spider | Nom Complet | Type | Volume |
|-------------|-------------|------|--------|
| `CH_BGer` | Bundesgericht / Tribunal fédéral | Arrêts non publiés | ~45,000 |
| `CH_BGE` | Bundesgerichtsentscheide | Arrêts publiés officiels | ~12,000 |
| `CH_BVGer` | Bundesverwaltungsgericht | Tribunal administratif fédéral | ~30,000 |
| `CH_BStGer` | Bundesstrafgericht | Tribunal pénal fédéral | ~8,000 |
| `CH_BPatGer` | Bundespatentgericht | Tribunal fédéral des brevets | ~500 |

### Juridictions Cantonales Principales

| Canton | Code Spider | Tribunal | Volume Approx. |
|--------|-------------|----------|----------------|
| Zürich | `CH_ZH_Obergericht` | Obergericht Zürich | ~8,000 |
| Bern | `CH_BE_Obergericht` | Obergericht Bern | ~6,000 |
| Genève | `CH_GE_Cour` | Cour de justice de Genève | ~7,000 |
| Vaud | `CH_VD_TC` | Tribunal cantonal Vaud | ~5,000 |
| Basel-Stadt | `CH_BS_Appellationsgericht` | Appellationsgericht BS | ~3,000 |
| Aargau | `CH_AG_Obergericht` | Obergericht Aargau | ~4,000 |

**Note** : Tous les cantons suisses ont leurs décisions indexées. Total : 26 cantons + 4 juridictions fédérales.

## Stratégies de Recherche

### 1. Recherche Exploratoire Initiale

**Objectif** : Comprendre le paysage juridique sur un sujet.

**Processus** :
```
1. Requête large avec termes principaux
   - Exemple : "Datenschutz" ou "protection données"
   - Limiter à 20-30 résultats pour vue d'ensemble

2. Analyser la distribution
   - Quels tribunaux sont les plus actifs ?
   - Quelle période est la plus pertinente ?
   - Quels termes apparaissent fréquemment ?

3. Affiner progressivement
   - Ajouter des termes spécifiques
   - Filtrer par juridiction si pertinent
   - Restreindre la période si nécessaire
```

**Exemple de workflow** :
```markdown
Étape 1 : Recherche large
query: "Kündigungsschutz"
size: 30
→ Résultat : 1,250 décisions trouvées

Étape 2 : Analyse
- BGer domine avec 40% des cas
- Pic d'activité 2020-2024
- Termes connexes : "fristlose", "Diskriminierung", "Schwangerschaft"

Étape 3 : Affinement
query: "Kündigungsschutz Schwangerschaft"
size: 20
→ Résultat : 85 décisions très ciblées
```

### 2. Recherche de Précédent Spécifique

**Objectif** : Trouver des cas similaires à une situation donnée.

**Processus** :
```
1. Identifier les éléments clés du cas
   - Domaine juridique principal
   - Faits caractéristiques
   - Question juridique centrale

2. Construire une requête combinée
   - Utiliser AND pour lier les concepts essentiels
   - Utiliser des guillemets pour phrases exactes
   - Exemple : "licenciement" AND "grossesse" AND "discrimination"

3. Filtrer par pertinence
   - Commencer par BGer pour jurisprudence de principe
   - Élargir aux cantons pour applications concrètes
   - Privilégier les décisions récentes (5 dernières années)

4. Analyser la hiérarchie
   - BGE (arrêts publiés) = autorité maximale
   - BGer (non publiés) = importantes mais moins citées
   - Tribunaux cantonaux = applications locales
```

**Exemple pratique** :
```markdown
Cas de l'utilisateur : 
"Employée licenciée pendant congé maternité, PME de 12 employés"

Recherche structurée :
Query 1: "Kündigungsschutz Mutterschaftsurlaub"
→ Trouver le cadre juridique général (BGE de principe)

Query 2: "Kündigung Mutterschaftsurlaub" AND "Kleinbetrieb"
→ Trouver des cas similaires avec petites entreprises

Query 3: Check canton spécifique si pertinent
→ Jurisprudence du canton concerné
```

### 3. Recherche par Article de Loi

**Objectif** : Trouver l'application jurisprudentielle d'un article spécifique.

**Processus** :
```
1. Utiliser la référence exacte de l'article
   - Format : "Art. [numéro] [abréviation loi]"
   - Exemples : "Art. 328 OR", "Art. 8 CEDH", "Art. 13 Cst."

2. Combiner avec le domaine
   - "Art. 328 OR" AND "protection personnalité"
   - Permet de cibler l'aspect spécifique de l'article

3. Rechercher les interprétations
   - Chercher "auslegung" ou "interprétation"
   - Identifier l'évolution jurisprudentielle
```

**Tableau des abréviations légales courantes** :
| Code | Loi | Domaine |
|------|-----|---------|
| OR / CO | Code des Obligations | Contrats, travail, société |
| ZGB / CC | Code Civil | Personnes, famille, successions |
| StGB / CP | Code Pénal | Droit pénal |
| BV / Cst. | Constitution fédérale | Droits fondamentaux |
| ZPO / CPC | Code de procédure civile | Procédure |
| StPO / CPP | Code de procédure pénale | Procédure pénale |
| DSG / LPD | Loi sur la protection des données | Privacy |

### 4. Recherche par Période (Veille Jurisprudentielle)

**Objectif** : Identifier les développements récents.

**Processus** :
```
1. Utiliser les filtres temporels
   - Les résultats sont triés par date (desc) par défaut
   - Limiter à 6-12 derniers mois pour "récent"
   - 2-3 dernières années pour "tendances"

2. Surveiller les revirements
   - Comparer avec jurisprudence ancienne
   - Identifier changements de doctrine

3. Analyser par volume
   - Augmentation des cas = sujet d'actualité
   - Baisse = doctrine stabilisée
```

### 5. Recherche Multilingue

**Objectif** : Couvrir toutes les régions linguistiques.

**Stratégie** :
```
1. Recherche en allemand (langue dominante)
   - ~70% des décisions sont en allemand
   - Termes : "Datenschutz", "Kündigungsschutz", etc.

2. Recherche en français
   - ~25% des décisions
   - Termes : "protection données", "licenciement", etc.

3. Recherche en italien
   - ~5% des décisions
   - Termes : "protezione dati", "licenziamento", etc.

4. Combiner les résultats
   - Utiliser plusieurs requêtes séparées
   - Déduplication par signature
```

**Vocabulaire juridique multilingue** :
| DE | FR | IT | Domaine |
|----|----|----|---------|
| Datenschutz | Protection des données | Protezione dei dati | Privacy |
| Kündigungsschutz | Protection contre le licenciement | Protezione dal licenziamento | Travail |
| Mietrecht | Droit du bail | Diritto di locazione | Location |
| Vertragsrecht | Droit des contrats | Diritto dei contratti | Contrats |
| Strafrecht | Droit pénal | Diritto penale | Pénal |

## Syntaxe de Recherche Elasticsearch

Le MCP utilise `simple_query_string` avec les opérateurs suivants :

### Opérateurs de Base

```
AND         : terme1 AND terme2 (opérateur par défaut)
OR          : terme1 OR terme2
NOT ou -    : terme1 -terme2 ou terme1 NOT terme2
"phrase"    : recherche de phrase exacte
```

### Opérateurs Avancés

```
*           : wildcard (protect* = protection, protéger, etc.)
?           : caractère unique (199? = 1990-1999)
+           : terme obligatoire (+licenciement)
field:value : recherche dans un champ spécifique
```

### Exemples Concrets

```elasticsearch
# Recherche simple (AND implicite)
Datenschutz DSGVO
→ Documents contenant les deux termes

# Phrase exacte
"protection de la personnalité du travailleur"
→ Expression exacte uniquement

# Opérateurs booléens
(Datenschutz OR "protection données") AND DSGVO
→ Terme allemand OU français + DSGVO

# Wildcard
Kündig*
→ Kündigung, Kündigungsschutz, Kündigungsfrist, etc.

# Exclusion
Datenschutz -Strafrecht
→ Protection des données mais PAS droit pénal

# Champs spécifiques
court:CH_BGer date:2023
→ Uniquement Tribunal fédéral en 2023
```

## Workflow de Recherche Recommandé

### Phase 1 : Exploration (Query Initiale)

```markdown
1. Comprendre la demande de l'utilisateur
   - Identifier le domaine juridique
   - Extraire les mots-clés principaux
   - Déterminer la juridiction pertinente

2. Construire la première requête
   - Termes larges en allemand (langue principale)
   - Limiter à 20-30 résultats
   - Pas de filtres restrictifs au début

3. Exécuter la recherche
   Tool: search_case_law
   Paramètres:
   {
     "query": "[termes principaux]",
     "size": 20,
     "from": 0
   }
```

### Phase 2 : Analyse des Résultats

```markdown
1. Évaluer la pertinence
   - Lire les abstracts des 5-10 premiers résultats
   - Identifier les termes les plus pertinents
   - Noter les tribunaux récurrents

2. Identifier les décisions clés
   - BGE (publiés) en priorité
   - BGer récents (2-3 dernières années)
   - Cantons si question locale

3. Évaluer si affinement nécessaire
   - Trop de résultats (>500) → affiner
   - Pas assez (<10) → élargir
   - Bonne quantité (10-100) → approfondir
```

### Phase 3 : Affinement (Si Nécessaire)

```markdown
1. Stratégie si TROP de résultats
   - Ajouter des termes spécifiques
   - Utiliser AND pour combiner concepts
   - Filtrer par juridiction (court:CH_BGer)
   - Restreindre à période récente

2. Stratégie si PAS ASSEZ de résultats
   - Utiliser wildcards (protect* au lieu de protection)
   - Essayer synonymes juridiques
   - Élargir à toutes juridictions
   - Rechercher en plusieurs langues

3. Relancer la recherche affinée
   Tool: search_case_law
   Paramètres ajustés selon stratégie
```

### Phase 4 : Récupération de Documents

```markdown
1. Sélectionner les décisions les plus pertinentes
   - Maximum 3-5 documents à analyser en détail
   - Privilégier BGE et BGer récents
   - Varier les perspectives si plusieurs juridictions

2. Récupérer le contenu complet
   Tool: get_document
   Paramètres:
   {
     "signature": "[signature de la décision]",
     "spider": "[code tribunal]",
     "format": "json"  // ou "html" pour lecture
   }

3. Analyser le contenu
   - Lire les faits (Sachverhalt)
   - Étudier les considérants (Erwägungen)
   - Extraire le dispositif (Urteil/Dispositif)
```

### Phase 5 : Synthèse

```markdown
1. Structurer la réponse pour l'utilisateur
   - Vue d'ensemble de la jurisprudence trouvée
   - Résumé des décisions clés (3-5 max)
   - Principes juridiques dégagés
   - Application au cas de l'utilisateur

2. Citer correctement
   - Signature complète de la décision
   - Date
   - Tribunal
   - Lien vers le document

3. Proposer des approfondissements
   - Recherches complémentaires possibles
   - Domaines connexes à explorer
```

## Format de Réponse Recommandé

### Structure de Réponse Complète

```markdown
# Recherche Jurisprudentielle : [Sujet]

## 📊 Vue d'Ensemble
- **Décisions trouvées** : [nombre]
- **Période couverte** : [années]
- **Principales juridictions** : [tribunaux]

## 🔍 Résultats de la Recherche

### Requête utilisée
```
[query exacte]
```

### Distribution
- Tribunal fédéral (BGer/BGE) : X décisions
- Tribunaux cantonaux : Y décisions
- Autres : Z décisions

## ⚖️ Décisions Clés

### 1. [Titre de la décision] - [Signature]
**Tribunal** : [Nom du tribunal]  
**Date** : [Date]  
**Références** : [Numéro de cas]

**Résumé** :
[Résumé des faits et de la décision en 2-3 phrases]

**Principe juridique** :
[Règle de droit dégagée]

**Lien** : [URL du document]

---

### 2. [Deuxième décision]
[Même structure...]

---

### 3. [Troisième décision]
[Même structure...]

## 📝 Analyse Jurisprudentielle

### Principes Généraux
[Synthèse des règles de droit établies]

### Évolution
[Tendances observées dans le temps]

### Application Pratique
[Comment ces décisions s'appliquent au cas de l'utilisateur]

## 🔗 Recherches Complémentaires Suggérées

1. [Piste de recherche 1]
2. [Piste de recherche 2]
3. [Piste de recherche 3]

## ⚠️ Avertissement

Ces décisions sont fournies à titre informatif. Pour des conseils juridiques spécifiques, consultez un avocat qualifié.
```

## Cas d'Usage Spécifiques

### Cas 1 : Recherche pour un Client

**Contexte** : Avocat qui prépare un dossier

**Workflow** :
1. Recherche exhaustive sur le sujet exact
2. Récupération de tous les BGE pertinents (autorité max)
3. Analyse des tendances dans BGer récents
4. Vérification de la jurisprudence cantonale locale
5. Rapport structuré avec citations

### Cas 2 : Veille Juridique

**Contexte** : Suivi des développements récents

**Workflow** :
1. Requêtes sauvegardées sur sujets clés
2. Exécution mensuelle avec filtre temporel
3. Comparaison avec période précédente
4. Alerte si nouveau BGE publié
5. Bulletin des nouveautés

### Cas 3 : Recherche Académique

**Contexte** : Étude doctrinale approfondie

**Workflow** :
1. Recherche historique complète (toutes périodes)
2. Analyse quantitative (évolution dans le temps)
3. Comparaison inter-cantonale
4. Identification des revirements jurisprudentiels
5. Synthèse critique avec statistiques

### Cas 4 : Question Rapide

**Contexte** : Citoyen avec question ponctuelle

**Workflow** :
1. Recherche simple avec termes courants
2. Focus sur 2-3 décisions les plus récentes
3. Explication vulgarisée
4. Recommandation de consulter un professionnel

## Gestion des Limitations

### Grande Base de Données (>1M décisions)

**Problème** : Risque de surcharge

**Solutions** :
1. **Pagination intelligente**
   - Limiter à 20-30 résultats par requête
   - Utiliser `from` pour naviguer si nécessaire
   - Maximum 50 résultats par appel (limite MCP)

2. **Filtrage progressif**
   - Commencer large, affiner ensuite
   - Ne pas récupérer tous les documents
   - Sélectionner 3-5 décisions max pour analyse détaillée

3. **Ciblage par juridiction**
   - Si question fédérale → court:CH_BGer
   - Si question locale → court:CH_[canton]
   - Éviter recherches tous azimuts

### Résultats Multilingues

**Problème** : Résultats dispersés par langue

**Solutions** :
1. **Requête principale en allemand** (70% des cas)
2. **Requête secondaire en français** si nécessaire
3. **Fusion manuelle** des résultats pertinents
4. **Vocabulaire juridique unifié** pour utilisateur

### Documents Non Disponibles

**Problème** : Certains PDF/HTML peuvent manquer

**Solutions** :
1. **Toujours récupérer JSON d'abord** (métadonnées toujours présentes)
2. **HTML en second choix** (souvent disponible)
3. **PDF en dernier recours** (pas toujours accessible)
4. **Utiliser content_url** des résultats de recherche

## Commandes MCP Disponibles

### search_case_law

**Description** : Recherche dans la base de jurisprudence

**Paramètres** :
```json
{
  "query": "string (required) - Requête de recherche",
  "size": "number (optional, default: 10, max: 50) - Nombre de résultats",
  "from": "number (optional, default: 0) - Position de départ (pagination)"
}
```

**Retour** :
```json
{
  "signature": "Identifiant unique de la décision",
  "court": "Code du tribunal (spider)",
  "language": "Langue du document (de/fr/it)",
  "date": "Date de la décision (YYYY-MM-DD)",
  "case_number": "Numéro de référence du cas",
  "title_de": "Titre en allemand",
  "title_fr": "Titre en français",
  "title_it": "Titre en italien",
  "abstract_de": "Résumé en allemand",
  "abstract_fr": "Résumé en français",
  "abstract_it": "Résumé en italien",
  "has_html": "boolean - Document HTML disponible",
  "document_url": "URL du document",
  "scrapedate": "Date d'indexation"
}
```

### get_document

**Description** : Récupère le contenu complet d'une décision

**Paramètres** :
```json
{
  "signature": "string (required) - Signature de la décision",
  "spider": "string (optional) - Code du tribunal (extrait de signature si absent)",
  "format": "enum (optional, default: 'json') - Format: 'json', 'html', ou 'pdf'"
}
```

**Formats disponibles** :
- **json** : Métadonnées structurées + contenu textuel
- **html** : Version HTML complète du document
- **pdf** : Document PDF original (si disponible)

### list_courts

**Description** : Liste tous les tribunaux disponibles

**Paramètres** : Aucun

**Retour** :
```json
{
  "name": "Nom du tribunal",
  "total_documents": "Nombre de documents",
  "new_documents": "Nouveaux documents",
  "last_run": "Dernière mise à jour",
  "status": "État du scraper"
}
```

## Exemples de Requêtes Complexes

### Exemple 1 : Recherche Droit du Travail

```markdown
Demande utilisateur : 
"Je cherche des cas où un employeur a licencié quelqu'un pendant un arrêt maladie"

Stratégie :
1. Termes allemands (langue dominante) :
   Query: "Kündigung Krankheit" OR "Kündigung Arbeitsunfähigkeit"
   
2. Affinement si trop de résultats :
   Query: "fristlose Kündigung" AND "Krankheit" AND "Sperrfrist"
   
3. Version française :
   Query: "licenciement maladie" OR "résiliation pendant incapacité"

Résultat attendu : 50-200 décisions pertinentes
```

### Exemple 2 : Recherche Protection des Données

```markdown
Demande utilisateur :
"Quelles sont les sanctions pour violation du RGPD en Suisse ?"

Stratégie :
1. Termes multilingues :
   Query 1: "Datenschutz" AND "Sanktion" AND ("DSG" OR "DSGVO")
   Query 2: "protection données" AND "sanction" AND "LPD"
   
2. Filtrer juridiction :
   court:CH_BGer (décisions de principe)
   
3. Période récente :
   Privilégier date:2020-2024 (nouveau DSG depuis 2023)

Résultat attendu : 20-50 décisions de principe
```

### Exemple 3 : Recherche Droit Locatif

```markdown
Demande utilisateur :
"Un propriétaire peut-il augmenter le loyer après des rénovations ?"

Stratégie :
1. Termes spécifiques :
   Query: "Mietzinserhöhung" AND ("Renovation" OR "wertvermehrend")
   
2. Référence légale :
   Ajouter : "Art. 269a OR"
   
3. Canton spécifique si mentionné :
   Exemple pour Zürich : court:CH_ZH_Mietwesen

Résultat attendu : 30-100 décisions, mix BGer + cantonal
```

## Meilleures Pratiques

### DO ✅

1. **Commencer large, affiner progressivement**
   - Première requête exploratoire
   - Analyse des résultats
   - Affinement ciblé

2. **Utiliser la langue allemande en priorité**
   - 70% des décisions
   - Compléter avec français si nécessaire

3. **Limiter le nombre de résultats**
   - 20-30 pour exploration
   - 10-15 pour analyse détaillée
   - Max 50 par requête (limite technique)

4. **Privilégier les décisions récentes**
   - 5 dernières années pour jurisprudence actuelle
   - Vérifier s'il n'y a pas eu de revirement

5. **Citer correctement**
   - Signature complète
   - Date et tribunal
   - Lien vers document

6. **Structurer la réponse**
   - Vue d'ensemble
   - Décisions clés (3-5 max)
   - Synthèse juridique
   - Application au cas

### DON'T ❌

1. **Ne pas récupérer trop de documents**
   - Éviter >100 résultats sans affinement
   - Ne pas analyser en détail >5 décisions
   - Risque de surcharge

2. **Ne pas ignorer la hiérarchie des sources**
   - BGE > BGer > Cantonal
   - Arrêts publiés > non publiés
   - Récent > ancien (sauf étude historique)

3. **Ne pas traduire les termes juridiques**
   - Utiliser termes natifs pour recherche
   - Traduire seulement pour l'utilisateur

4. **Ne pas sur-généraliser**
   - Une décision ≠ jurisprudence constante
   - Vérifier cohérence avec autres arrêts
   - Mentionner exceptions

5. **Ne pas oublier les limites**
   - Ceci n'est PAS un avis juridique
   - Toujours recommander consultation avocat pour cas concret
   - Base de données pas 100% exhaustive

## Glossaire Juridique Suisse

### Termes Procéduraux

| Terme | Traduction | Signification |
|-------|------------|---------------|
| Beschwerde | Recours | Voie de recours |
| Urteil | Jugement/Arrêt | Décision finale |
| Verfügung | Décision | Acte administratif |
| Erwägungen | Considérants | Raisonnement du tribunal |
| Sachverhalt | État de fait | Exposé des faits |
| Dispositiv | Dispositif | Partie décisoire |

### Termes Substantiels

| Terme | Traduction | Domaine |
|-------|------------|---------|
| Kündigungsschutz | Protection contre licenciement | Travail |
| Persönlichkeitsschutz | Protection de la personnalité | Civil |
| Treu und Glauben | Bonne foi | Général |
| Verhältnismässigkeit | Proportionnalité | Droit public |
| Rechtsmissbrauch | Abus de droit | Général |

## Support et Dépannage

### Problème : Aucun résultat trouvé

**Causes possibles** :
- Termes trop spécifiques
- Faute d'orthographe
- Langue inadaptée

**Solutions** :
1. Élargir les termes de recherche
2. Utiliser wildcards (*)
3. Essayer en allemand
4. Rechercher termes synonymes

### Problème : Trop de résultats (>1000)

**Solutions** :
1. Ajouter des termes spécifiques (AND)
2. Filtrer par juridiction (court:)
3. Utiliser phrases exactes (" ")
4. Restreindre la période

### Problème : Document non accessible

**Solutions** :
1. Vérifier format demandé (JSON toujours dispo)
2. Essayer format alternatif (HTML au lieu de PDF)
3. Utiliser content_url des résultats de recherche
4. Vérifier signature exacte

### Problème : Résultats non pertinents

**Solutions** :
1. Utiliser phrases exactes pour concepts précis
2. Ajouter termes obligatoires (+terme)
3. Exclure termes parasites (-terme)
4. Vérifier langue de recherche

## Ressources Additionnelles

### Documentation Officielle
- Entscheidsuche.ch : https://entscheidsuche.ch
- Elasticsearch Query Syntax : Documentation MCP

### Support Utilisateur
- Fichier : `mcp-servers/README.md`
- Référence outils : `MCP_TOOLS_REFERENCE.md`

### Mise à Jour de la Skill
Cette skill est basée sur la version actuelle du MCP entscheidsuche. Pour mises à jour :
```bash
cd mcp-servers/entscheidsuche-mcp
git pull
npm install
npm run build
```

---

**Version** : 1.0.0  
**Dernière mise à jour** : Février 2026  
**Auteur** : Legal Assistant Workspace  
**Licence** : Usage interne
