# Swiss Legal Commentary Research

Recherche structurée dans les commentaires juridiques suisses via Onlinekommentar.ch

## Description

Cette skill guide l'agent dans la recherche de commentaires doctrinaux suisses en utilisant le serveur MCP **onlinekommentar**. Elle fournit des stratégies optimisées pour accéder à des commentaires juridiques de haute qualité, rédigés par des universitaires et praticiens reconnus.

## Capacités

- 📚 Accès à des commentaires doctrinaux de qualité
- 🌍 Recherche multilingue (DE, FR, IT, EN)
- 📖 Commentaires article par article sur les lois suisses
- 🎓 Accès aux auteurs et éditeurs académiques
- 🔗 Références croisées avec jurisprudence et doctrine

## Quand Utiliser Cette Skill

Invoquez cette skill quand l'utilisateur demande :
- "Explique-moi l'article [X] de [loi]"
- "Quels sont les commentaires sur [sujet juridique]"
- "Que dit la doctrine sur [question]"
- "Trouve-moi des analyses juridiques sur [thème]"
- "Comment interpréter [article de loi]"
- "Quelles sont les références académiques sur [sujet]"

## Onlinekommentar.ch - Vue d'Ensemble

### Mission
Première plateforme suisse à but non lucratif pour des commentaires juridiques en Open Access.

### Caractéristiques
- **Gratuit et accessible** : Pas de paywall
- **Académique** : Rédigé par universitaires et praticiens reconnus
- **À jour** : Mises à jour régulières
- **Multilingue** : Contenu en DE, FR, IT, EN
- **Citable** : Chaque commentaire a un identifiant unique

### Structure des Commentaires

Chaque commentaire comprend :
1. **Référence légale** : Article et loi commentés
2. **Texte de loi** : Reproduction de l'article dans toutes les langues
3. **Auteur(s)** : Experts reconnus avec affiliations
4. **Commentaire** : Analyse doctrinale approfondie
5. **Références** : Jurisprudence et doctrine citées
6. **Articles connexes** : Liens vers commentaires liés

## Actes Législatifs Couverts

### Droit Constitutionnel et Public

| Code | Titre Complet | Abréviation | Volume |
|------|---------------|-------------|--------|
| SR-101 | Constitution fédérale | Cst. / BV / FC | ~140 art. |
| SR-172.021 | Loi sur l'organisation du gouvernement | LOGA | ~50 art. |
| SR-141.1 | Loi sur le Parlement | LParl | ~80 art. |
| SR-161.1 | Loi sur les droits politiques | LDP | ~90 art. |

### Droit Civil

| Code | Titre Complet | Abréviation | Volume |
|------|---------------|-------------|--------|
| SR-210 | Code civil suisse | CC / ZGB | ~900 art. |
| SR-220 | Code des obligations | CO / OR | ~1,200 art. |
| SR-221.301 | Loi sur la poursuite et faillite | LP / SchKG | ~350 art. |

### Droit Pénal

| Code | Titre Complet | Abréviation | Volume |
|------|---------------|-------------|--------|
| SR-311.0 | Code pénal suisse | CP / StGB | ~400 art. |
| SR-312.0 | Code de procédure pénale | CPP / StPO | ~450 art. |

### Droit Administratif Spécial

| Code | Titre Complet | Abréviation | Volume |
|------|---------------|-------------|--------|
| SR-235.1 | Loi fédérale sur la protection des données | LPD / DSG | ~70 art. |
| SR-351.1 | Loi sur l'entraide pénale internationale | EIMP / IRSG | ~100 art. |
| SR-784.10 | Loi sur les télécommunications | LTC | ~100 art. |

**Note** : La plateforme couvre une sélection croissante de lois fédérales, avec focus sur les domaines les plus demandés.

## Stratégies de Recherche

### 1. Recherche par Article de Loi

**Objectif** : Trouver le commentaire d'un article spécifique.

**Processus** :
```
1. Identifier la référence exacte
   - Numéro d'article : Ex. "328"
   - Loi : Ex. "Code des Obligations"
   - Format complet : "Art. 328 CO"

2. Construire la requête
   - Utiliser le numéro d'article comme terme principal
   - Ajouter le nom ou code de la loi
   - Exemple : "Art. 328" OR "Article 328"

3. Filtrer par langue si nécessaire
   - language: "de" pour allemand
   - language: "fr" pour français
   - language: "it" pour italien
   - language: "en" pour anglais

4. Vérifier le legislative_act
   - Permet de s'assurer qu'on commente la bonne loi
   - Plusieurs lois peuvent avoir un "Art. 328"
```

**Exemple pratique** :
```markdown
Utilisateur : "Explique-moi l'article 328 du Code des Obligations"

Recherche :
{
  "search": "328 Code des Obligations",
  "language": "fr",
  "sort": "-date"
}

Alternative si pas de résultat :
{
  "search": "328 OR",
  "language": "fr"
}

Note : "OR" = abréviation allemande du CO
```

### 2. Recherche Thématique

**Objectif** : Trouver tous les commentaires sur un sujet donné.

**Processus** :
```
1. Identifier le thème principal
   - Exemple : "protection des données"
   - Termes connexes : "vie privée", "RGPD", "confidentialité"

2. Recherche large initiale
   - Utiliser termes généraux
   - Ne pas filtrer par loi au début
   - Permet de découvrir tous les articles pertinents

3. Analyser la distribution
   - Quels actes législatifs sont les plus pertinents ?
   - Y a-t-il plusieurs aspects du thème ?
   - Quels articles sont les plus commentés ?

4. Affiner par acte législatif si nécessaire
   - Une fois la loi principale identifiée
   - Utiliser le filtre legislative_act
```

**Exemple pratique** :
```markdown
Utilisateur : "Trouve des commentaires sur la protection des données personnelles"

Étape 1 : Recherche exploratoire
{
  "search": "protection données personnelles",
  "language": "fr",
  "size": 30
}

Résultat : 
- 15 commentaires sur LPD (Loi protection des données)
- 8 commentaires sur Constitution (Art. 13 Cst.)
- 5 commentaires sur Code pénal (infractions)

Étape 2 : Focus sur LPD
{
  "search": "données personnelles",
  "language": "fr",
  "legislative_act": "LPD"
}
```

### 3. Recherche par Auteur

**Objectif** : Trouver les commentaires d'un expert spécifique.

**Processus** :
```
1. Identifier l'auteur
   - Nom complet ou partiel
   - Institution si connue

2. Rechercher par nom
   - Le nom de l'auteur est indexé
   - Exemple : "Müller" trouvera tous les Müller

3. Combiner avec thème si nécessaire
   - "Müller" AND "Datenschutz"
   - Pour cibler un domaine spécifique

4. Analyser les éditeurs aussi
   - Les éditeurs sont aussi des experts reconnus
   - Ils valident la qualité du commentaire
```

**Exemple pratique** :
```markdown
Utilisateur : "Quels sont les commentaires du Prof. Schlegel sur le droit constitutionnel ?"

Recherche :
{
  "search": "Schlegel constitution",
  "sort": "-date"
}

Note : Le système cherchera dans les champs authors et editors
```

### 4. Recherche Multilingue Systématique

**Objectif** : Couvrir toutes les perspectives linguistiques.

**Processus** :
```
1. Identifier le terme dans chaque langue
   DE : terme allemand
   FR : terme français
   IT : terme italien
   EN : terme anglais

2. Exécuter recherches séparées
   - Une requête par langue
   - Même sujet, différentes formulations

3. Comparer les résultats
   - Y a-t-il des commentaires uniques par langue ?
   - Certains auteurs publient dans une seule langue
   - Perspective juridique peut varier (cantons)

4. Synthétiser
   - Présenter vue d'ensemble multilingue
   - Mentionner disponibilité dans chaque langue
   - Recommander version selon préférence utilisateur
```

**Vocabulaire thématique multilingue** :

| Thème | DE | FR | IT | EN |
|-------|----|----|----|----|
| Protection données | Datenschutz | Protection des données | Protezione dei dati | Data protection |
| Droit du travail | Arbeitsrecht | Droit du travail | Diritto del lavoro | Employment law |
| Droits fondamentaux | Grundrechte | Droits fondamentaux | Diritti fondamentali | Fundamental rights |
| Contrats | Vertragsrecht | Droit des contrats | Diritto dei contratti | Contract law |
| Propriété intellectuelle | Immaterialgüterrecht | Propriété intellectuelle | Proprietà intellettuale | Intellectual property |

### 5. Recherche de Références Croisées

**Objectif** : Trouver les connexions entre articles et domaines.

**Processus** :
```
1. Commencer par l'article principal
   - Récupérer le commentaire complet
   - Identifier les références citées

2. Explorer les articles connexes
   - Chaque commentaire liste "related_articles"
   - Suivre ces liens pour vision systématique

3. Vérifier les références jurisprudentielles
   - Les commentaires citent les arrêts pertinents
   - Permet de combiner avec skill "case-law-research"

4. Construire une carte conceptuelle
   - Article central
   - Articles liés
   - Jurisprudence applicable
   - Doctrine complémentaire
```

## Workflow de Recherche Recommandé

### Phase 1 : Identification du Besoin

```markdown
1. Comprendre la question de l'utilisateur
   - Article spécifique ou thème général ?
   - Langue préférée (ou multilingue) ?
   - Niveau de détail souhaité ?

2. Déterminer la stratégie
   - Recherche par article → Stratégie 1
   - Recherche thématique → Stratégie 2
   - Auteur spécifique → Stratégie 3
   - Vue d'ensemble → Stratégie 4

3. Préparer les paramètres de recherche
   - Termes de recherche
   - Langue(s)
   - Filtres éventuels
```

### Phase 2 : Recherche Initiale

```markdown
1. Exécuter la première requête
   Tool: search_commentaries
   Paramètres:
   {
     "search": "[termes]",
     "language": "[de|fr|it|en]",  // optionnel
     "sort": "-date",               // plus récents d'abord
     "page": 1
   }

2. Analyser les résultats
   - Nombre de commentaires trouvés
   - Pertinence des titres
   - Distribution par loi
   - Dates de publication

3. Évaluer si affinement nécessaire
   - 0 résultats → élargir recherche
   - 1-10 résultats → parfait
   - >20 résultats → affiner
```

### Phase 3 : Sélection des Commentaires

```markdown
1. Identifier les plus pertinents
   - Lire les titres
   - Vérifier l'acte législatif
   - Noter les auteurs (reconnus ?)
   - Privilégier commentaires récents

2. Limiter le nombre
   - Maximum 3-5 commentaires à analyser
   - Éviter surcharge d'information
   - Qualité > quantité

3. Préparer la récupération
   - Noter les IDs des commentaires sélectionnés
   - Ordre logique (général → spécifique)
```

### Phase 4 : Récupération Détaillée

```markdown
1. Récupérer le contenu complet
   Tool: get_commentary_by_id
   Paramètres:
   {
     "id": "[commentary_id]"
   }

2. Pour chaque commentaire sélectionné
   - Lire le commentaire complet
   - Noter les références clés
   - Identifier les articles connexes
   - Extraire les principes principaux

3. Structure du commentaire récupéré
   - Titre et référence légale
   - Texte de loi commenté (toutes langues)
   - Auteur(s) et éditeur(s)
   - Commentaire doctrinal complet
   - Références jurisprudentielles
   - Références doctrinales
   - Articles connexes
```

### Phase 5 : Synthèse et Présentation

```markdown
1. Structurer la réponse
   - Vue d'ensemble du sujet
   - Analyse de chaque commentaire
   - Synthèse des positions doctrinales
   - Application au cas de l'utilisateur

2. Citer correctement
   - Auteur(s) complet(s)
   - Titre du commentaire
   - Date de publication
   - Lien vers onlinekommentar.ch

3. Proposer approfondissements
   - Articles connexes à explorer
   - Jurisprudence mentionnée (→ case-law skill)
   - Doctrine complémentaire
```

## Format de Réponse Recommandé

### Structure de Réponse Complète

```markdown
# Commentaire Doctrinal : [Sujet]

## 📚 Vue d'Ensemble
- **Commentaires trouvés** : [nombre]
- **Acte(s) législatif(s)** : [lois concernées]
- **Langue(s)** : [langues disponibles]

## 🔍 Recherche Effectuée

### Requête utilisée
```
[termes de recherche]
```

### Filtres appliqués
- Langue : [langue ou "toutes"]
- Acte législatif : [loi spécifique ou "tous"]
- Tri : [ordre de tri]

## 📖 Commentaires Sélectionnés

### 1. [Titre du Commentaire]
**Référence** : [Article X de la Loi Y]  
**Auteur(s)** : [Nom(s) complet(s)]  
**Éditeur(s)** : [Nom(s) complet(s)]  
**Institution** : [Université/Cabinet]  
**Date de publication** : [Date]  
**Dernière mise à jour** : [Date]

#### Texte de Loi
[Reproduction de l'article dans la langue demandée]

#### Analyse Doctrinale
[Résumé du commentaire en 3-5 paragraphes clés]

**Points clés** :
1. [Premier principe important]
2. [Deuxième principe important]
3. [Troisième principe important]

#### Références Jurisprudentielles
- [BGE/ATF référence 1] : [Court résumé]
- [BGE/ATF référence 2] : [Court résumé]

#### Doctrine Citée
- [Auteur, Ouvrage, année] : [Page/passage pertinent]

**Lien** : [URL vers onlinekommentar.ch]

---

### 2. [Deuxième Commentaire]
[Même structure...]

---

### 3. [Troisième Commentaire]
[Même structure...]

## 📊 Synthèse Doctrinale

### Consensus Académique
[Points sur lesquels les auteurs s'accordent]

### Débats Doctrinaux
[Points de désaccord ou d'interprétation divergente]

### Évolution de la Doctrine
[Comment la position doctrinale a évolué dans le temps]

### Rapport avec la Jurisprudence
[Degré d'alignement entre doctrine et jurisprudence]

## 💼 Application Pratique

### Au Cas de l'Utilisateur
[Comment ces commentaires s'appliquent à la situation spécifique]

### Recommandations
[Conseils basés sur l'analyse doctrinale]

## 🔗 Approfondissements Suggérés

### Articles Connexes
1. [Article X] : [Pourquoi pertinent]
2. [Article Y] : [Pourquoi pertinent]

### Jurisprudence à Consulter
[Utiliser skill "case-law-research" pour :]
- [Arrêt 1 mentionné dans commentaire]
- [Arrêt 2 mentionné dans commentaire]

### Doctrine Complémentaire
- [Ouvrage 1 cité]
- [Article de revue 2 cité]

## ⚠️ Avertissement

Ces commentaires doctrinaux sont fournis à titre informatif et académique. Pour des conseils juridiques spécifiques, consultez un avocat qualifié.

---

**Sources** :
- Onlinekommentar.ch (plateforme Open Access)
- Auteurs : [Liste des auteurs consultés]
- Consultation effectuée : [Date]
```

## Combinaison avec Swiss Case Law Research

### Workflow Intégré : Doctrine + Jurisprudence

```markdown
1. Commencer par la DOCTRINE (cette skill)
   - Identifier le cadre juridique
   - Comprendre les principes généraux
   - Noter les arrêts clés mentionnés

2. Basculer vers JURISPRUDENCE (case-law skill)
   - Rechercher les arrêts mentionnés dans le commentaire
   - Vérifier jurisprudence récente (pas toujours dans commentaire)
   - Analyser l'application pratique

3. SYNTHÉTISER les deux sources
   - Principe doctrinal
   - Application jurisprudentielle
   - Cohérence ou divergence
   - Tendances actuelles

4. RÉPONDRE à l'utilisateur
   - Vue théorique (doctrine)
   - Vue pratique (jurisprudence)
   - Application à son cas
```

### Exemple Concret : Protection de la Personnalité

```markdown
Question : "Un employeur peut-il surveiller les emails professionnels ?"

PHASE 1 - DOCTRINE (onlinekommentar)
→ Rechercher : "Art. 328 CO" (protection personnalité travailleur)
→ Rechercher : "Art. 13 Cst." (droit à la vie privée)
→ Résultat : Cadre juridique et principes généraux

PHASE 2 - JURISPRUDENCE (entscheidsuche)
→ Rechercher : "Überwachung Email Arbeitgeber" OR "surveillance email employeur"
→ Filtrer : BGer (principe) + cantons (applications)
→ Résultat : Cas concrets et limites admises

PHASE 3 - SYNTHÈSE
→ Doctrine : Protection forte mais pas absolue
→ Jurisprudence : Surveillance admise si proportionnée et transparente
→ Application : Politique claire requise, consentement préférable

PHASE 4 - RÉPONSE
→ Présentation intégrée des deux sources
→ Recommandations pratiques
→ Référence aux commentaires ET arrêts pertinents
```

## Cas d'Usage Spécifiques

### Cas 1 : Étudiant en Droit

**Contexte** : Préparation d'un examen ou mémoire

**Workflow** :
1. Recherche thématique large
2. Lecture de 2-3 commentaires de référence
3. Identification des auteurs principaux
4. Exploration des articles connexes
5. Synthèse académique structurée

**Exemple** :
```
Question : "Prépare un résumé sur le droit de la filiation"
1. Recherche : "filiation" dans CC
2. Identification : Art. 252-269 CC couverts
3. Lecture commentaires clés (Art. 252, 255, 260)
4. Synthèse avec structure claire
```

### Cas 2 : Avocat Praticien

**Contexte** : Préparation d'un dossier client

**Workflow** :
1. Recherche par article spécifique pertinent au cas
2. Lecture approfondie du commentaire
3. Note des références jurisprudentielles citées
4. Basculement vers case-law pour jurisprudence récente
5. Rédaction argumentaire basée doctrine + jurisprudence

**Exemple** :
```
Cas : Contestation d'un licenciement
1. Commentaire Art. 336 CO (licenciement abusif)
2. Extraction principes et conditions
3. Recherche arrêts BGer mentionnés
4. Vérification jurisprudence 2023-2024
5. Construction argumentation juridique
```

### Cas 3 : Citoyen avec Question

**Contexte** : Besoin de comprendre un article de loi

**Workflow** :
1. Recherche article spécifique en langue simple
2. Présentation vulgarisée du commentaire
3. Focus sur application pratique
4. Éviter jargon technique excessif
5. Recommandation consultation professionnelle si nécessaire

**Exemple** :
```
Question : "Que dit l'article 328 CO exactement ?"
1. Récupération commentaire Art. 328 CO en français
2. Explication claire : protection personnalité au travail
3. Exemples concrets d'application
4. Mention : consulter avocat pour cas personnel
```

### Cas 4 : Recherche Comparative

**Contexte** : Comparer positions doctrinales

**Workflow** :
1. Recherche multilingue sur même sujet
2. Identification des différences d'approche
3. Analyse des raisons (contexte cantonal, école de pensée)
4. Synthèse comparative
5. Recommandation selon contexte utilisateur

**Exemple** :
```
Question : "Comment la doctrine suisse aborde le RGPD ?"
1. Recherche : "DSGVO" (allemand) + "RGPD" (français)
2. Comparaison auteurs alémaniques vs romands
3. Identification consensus et divergences
4. Présentation équilibrée
```

## Gestion des Limitations

### Plateforme en Développement

**Réalité** : Onlinekommentar.ch est en croissance continue

**Implications** :
1. **Couverture partielle**
   - Tous les articles ne sont pas encore commentés
   - Certaines lois ont priorité (Cst., CO, CC, CP, LPD)
   - Nouveaux commentaires ajoutés régulièrement

2. **Solutions** :
   - Si pas de commentaire : mentionner explicitement
   - Proposer articles connexes commentés
   - Suggérer doctrine traditionnelle (ouvrages papier)
   - Combiner avec jurisprudence (case-law skill)

### Commentaires en Cours de Rédaction

**Réalité** : Certains commentaires sont en draft ou incomplets

**Solutions** :
1. Vérifier date de publication
2. Mentionner si commentaire récent (peut évoluer)
3. Croiser avec autres commentaires si disponibles
4. Compléter avec jurisprudence

### Langue de Publication

**Réalité** : Pas tous les commentaires dans toutes les langues

**Solutions** :
1. Recherche multilingue systématique
2. Si commentaire uniquement en allemand : le mentionner
3. Proposer traduction des concepts clés
4. Indiquer disponibilité par langue

## Commandes MCP Disponibles

### search_commentaries

**Description** : Recherche dans la base de commentaires juridiques

**Paramètres** :
```json
{
  "search": "string (required) - Requête de recherche full-text",
  "language": "enum (optional) - Langue: 'de', 'fr', 'it', 'en'",
  "legislative_act": "string (optional) - ID de l'acte législatif",
  "sort": "enum (optional) - Tri: 'title', '-title', 'date', '-date'",
  "page": "number (optional, default: 1) - Page pour pagination"
}
```

**Retour** :
```json
{
  "id": "UUID unique du commentaire",
  "title": "Titre du commentaire",
  "date": "Date de publication (YYYY-MM-DD)",
  "language": "Langue du commentaire (de/fr/it/en)",
  "authors": [
    {
      "id": "UUID de l'auteur",
      "name": "Nom complet de l'auteur"
    }
  ],
  "editors": [
    {
      "id": "UUID de l'éditeur",
      "name": "Nom complet de l'éditeur"
    }
  ],
  "legislative_act": {
    "id": "UUID de l'acte législatif",
    "title": "Titre complet de la loi"
  },
  "html_link": "URL vers le commentaire sur onlinekommentar.ch"
}
```

### get_commentary_by_id

**Description** : Récupère le contenu complet d'un commentaire spécifique

**Paramètres** :
```json
{
  "id": "string (required) - UUID du commentaire"
}
```

**Retour** :
```json
{
  "id": "UUID unique",
  "title": "Titre complet",
  "language": "Langue principale",
  "date": "Date de publication",
  "legislative_act": {
    "id": "UUID de la loi",
    "title": "Titre de la loi",
    "article": "Numéro d'article commenté"
  },
  "legal_domain": {
    "id": "UUID du domaine",
    "name": "Nom du domaine juridique"
  },
  "authors": [
    {
      "id": "UUID",
      "name": "Nom complet",
      "institution": "Affiliation institutionnelle"
    }
  ],
  "editors": [
    {
      "id": "UUID",
      "name": "Nom complet"
    }
  ],
  "content": "Texte complet du commentaire (peut être HTML)",
  "html_link": "URL vers onlinekommentar.ch",
  "related_articles": [
    {
      "id": "UUID d'article connexe",
      "article": "Numéro article",
      "title": "Titre"
    }
  ]
}
```

**Note** : Le champ `content` peut ne pas toujours être rempli dans les résultats de recherche. Utiliser `get_commentary_by_id` pour le contenu complet.

## Meilleures Pratiques

### DO ✅

1. **Commencer spécifique si possible**
   - Si article connu : rechercher directement
   - Économise temps et requêtes

2. **Vérifier les auteurs**
   - Auteurs reconnus = commentaire de qualité
   - Noter affiliations universitaires

3. **Lire le texte de loi d'abord**
   - Disponible dans toutes les langues
   - Essentiel pour comprendre le commentaire

4. **Noter les références**
   - Jurisprudence citée → rechercher avec case-law skill
   - Doctrine citée → approfondir si nécessaire

5. **Privilégier commentaires récents**
   - Trier par date (`sort: "-date"`)
   - Droit évolue, doctrine aussi

6. **Citer correctement**
   - Auteur(s) complet(s)
   - Titre du commentaire
   - Date de publication/mise à jour
   - Lien vers onlinekommentar.ch

### DON'T ❌

1. **Ne pas ignorer la langue**
   - Commentaire peut exister dans une seule langue
   - Toujours vérifier disponibilité multilingue

2. **Ne pas limiter à un seul commentaire**
   - Comparer 2-3 commentaires si disponibles
   - Positions doctrinales peuvent varier

3. **Ne pas négliger les éditeurs**
   - Rôle de validation important
   - Garantie de qualité académique

4. **Ne pas oublier les articles connexes**
   - Vision systématique de la loi
   - Cohérence d'interprétation

5. **Ne pas substituer à conseil juridique**
   - Commentaire = ressource académique
   - Cas concret → avocat

## Glossaire des Domaines Juridiques

| Terme DE | Terme FR | Terme IT | Terme EN | Description |
|----------|----------|----------|----------|-------------|
| Verfassungsrecht | Droit constitutionnel | Diritto costituzionale | Constitutional law | Droits fondamentaux, organisation État |
| Zivilrecht | Droit civil | Diritto civile | Civil law | Personnes, famille, contrats, biens |
| Strafrecht | Droit pénal | Diritto penale | Criminal law | Infractions et sanctions |
| Verwaltungsrecht | Droit administratif | Diritto amministrativo | Administrative law | Organisation et action administrative |
| Verfahrensrecht | Droit de procédure | Diritto processuale | Procedural law | Règles de procédure |
| Arbeitsrecht | Droit du travail | Diritto del lavoro | Employment law | Relations de travail |
| Sozialversicherungsrecht | Droit des assurances sociales | Diritto delle assicurazioni sociali | Social insurance law | AVS, AI, chômage, etc. |
| Immaterialgüterrecht | Propriété intellectuelle | Proprietà intellettuale | Intellectual property | Brevets, marques, copyright |

## Support et Dépannage

### Problème : Aucun commentaire trouvé

**Causes possibles** :
- Article pas encore commenté sur la plateforme
- Loi non couverte actuellement
- Termes de recherche inadaptés

**Solutions** :
1. Vérifier orthographe (numéro article, nom loi)
2. Élargir à thème général
3. Rechercher articles connexes
4. Combiner avec case-law skill pour jurisprudence
5. Mentionner limite de couverture à l'utilisateur

### Problème : Commentaire uniquement en allemand

**Solutions** :
1. Mentionner clairement la langue disponible
2. Proposer traduction des concepts principaux
3. Rechercher si version autre langue existe
4. Expliquer contenu en langue préférée utilisateur

### Problème : Commentaire très technique

**Solutions** :
1. Vulgariser les concepts principaux
2. Fournir exemples concrets
3. Structurer par questions-réponses
4. Highlighter l'essentiel pour utilisateur non-juriste

### Problème : Commentaire ancien

**Solutions** :
1. Mentionner la date
2. Vérifier s'il y a mise à jour récente
3. Compléter avec jurisprudence récente (case-law skill)
4. Noter si changement législatif depuis publication

## Ressources Additionnelles

### Documentation Officielle
- Onlinekommentar.ch : https://onlinekommentar.ch
- API Documentation : https://onlinekommentar.ch/api

### Liens Utiles
- À propos : https://onlinekommentar.ch/de/ueber-onlinekommentar
- Auteurs et éditeurs : https://onlinekommentar.ch/de/autorinnen
- Soutiens : https://onlinekommentar.ch/de/unterstuetzerinnen

### Support Utilisateur
- Fichier : `mcp-servers/README.md`
- Référence outils : `MCP_TOOLS_REFERENCE.md`

### Mise à Jour de la Skill
Cette skill est basée sur la version actuelle du MCP onlinekommentar. Pour mises à jour :
```bash
cd mcp-servers/onlinekommentar-mcp
git pull
npm install
npm run build
```

## Exemples de Requêtes Complètes

### Exemple 1 : Article Spécifique

```markdown
Question : "Explique-moi l'article 328 du Code des Obligations"

Requête MCP :
{
  "search": "328 Code Obligations",
  "language": "fr",
  "sort": "-date"
}

Récupération détaillée :
{
  "id": "[UUID récupéré]"
}

Présentation à l'utilisateur :
- Texte de loi Art. 328 CO (français)
- Commentaire doctrinal complet
- Auteur(s) et affiliation
- Références jurisprudentielles
- Articles connexes (328a, 328b, etc.)
```

### Exemple 2 : Thème Transversal

```markdown
Question : "Quels sont les commentaires sur la protection des lanceurs d'alerte ?"

Requête 1 - Exploration :
{
  "search": "lanceur alerte whistleblower",
  "sort": "-date"
}

Résultat : Commentaires dispersés dans plusieurs lois
- Code des Obligations (protection travailleur)
- Code pénal (dénonciation)
- Loi sur la fonction publique

Requête 2 - Approfondissement par loi :
Pour chaque loi identifiée, récupérer commentaires pertinents

Présentation :
Vue d'ensemble multi-lois avec synthèse transversale
```

### Exemple 3 : Comparaison Linguistique

```markdown
Question : "Comment les juristes alémaniques et romands abordent-ils le droit de la famille ?"

Requête 1 - Allemand :
{
  "search": "Familienrecht",
  "language": "de"
}

Requête 2 - Français :
{
  "search": "droit famille",
  "language": "fr"
}

Analyse :
- Identifier auteurs principaux dans chaque langue
- Comparer approches doctrinales
- Noter différences terminologiques
- Synthétiser consensus et divergences
```

---

**Version** : 1.0.0  
**Dernière mise à jour** : Février 2026  
**Auteur** : Legal Assistant Workspace  
**Licence** : Usage interne
