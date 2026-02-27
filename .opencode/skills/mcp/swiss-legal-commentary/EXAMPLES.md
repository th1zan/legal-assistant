# Exemples - Swiss Legal Commentary

Exemples complets de recherches de commentaires doctrinaux via Onlinekommentar.ch.

## Exemple 1 : Article Spécifique (Art. 328 CO)

### Question
"Explique-moi l'article 328 du Code des Obligations"

### Workflow

**Étape 1 : Recherche initiale**
```json
{
  "search": "328 Code Obligations",
  "language": "fr",
  "sort": "-date"
}
```

**Étape 2 : Si pas de résultat, variante allemande**
```json
{
  "search": "328 OR",
  "language": "de"
}
```
Note : "OR" = Obligationenrecht (abréviation allemande du CO)

**Étape 3 : Récupération détaillée**
```json
{
  "id": "[UUID récupéré de la recherche]"
}
```

### Présentation
- Texte de loi Art. 328 CO (français)
- Commentaire doctrinal complet
- Auteur(s) et affiliation
- Références jurisprudentielles (ATF sur protection de la personnalité)
- Articles connexes (328a, 328b CO)

---

## Exemple 2 : Thème Transversal (Protection des données)

### Question
"Trouve des commentaires sur la protection des données personnelles"

### Workflow

**Étape 1 : Recherche exploratoire large**
```json
{
  "search": "protection données personnelles",
  "language": "fr",
  "sort": "-date"
}
```

**Résultat typique** :
- 15 commentaires sur LPD (Loi protection des données)
- 8 commentaires sur Constitution (Art. 13 Cst.)
- 5 commentaires sur Code pénal (infractions)

**Étape 2 : Focus sur loi principale (LPD)**
```json
{
  "search": "données personnelles",
  "language": "fr",
  "legislative_act": "LPD"
}
```

**Étape 3 : Récupérer les 3 plus pertinents**
- Art. 1 LPD (but et champ d'application)
- Art. 4 LPD (principes généraux)
- Art. 12 LPD (droits de la personne concernée)

### Présentation
- Vue d'ensemble multi-lois
- Focus sur LPD avec principes clés
- Liens avec droits constitutionnels (Art. 13 Cst.)
- Synthèse transversale

---

## Exemple 3 : Recherche Comparative Multilingue

### Question
"Comment les juristes alémaniques et romands abordent-ils le droit de la famille ?"

### Workflow

**Étape 1 : Recherche en allemand**
```json
{
  "search": "Familienrecht",
  "language": "de",
  "sort": "-date"
}
```

**Étape 2 : Recherche en français**
```json
{
  "search": "droit famille",
  "language": "fr",
  "sort": "-date"
}
```

**Étape 3 : Analyse comparative**
- Identifier auteurs principaux dans chaque langue
- Comparer approches doctrinales
- Noter différences terminologiques
- Synthétiser consensus et divergences

### Présentation
- Auteurs alémaniques de référence
- Auteurs romands de référence
- Points de convergence
- Nuances régionales/linguistiques

---

## Exemple 4 : Recherche par Auteur

### Question
"Quels sont les commentaires du Prof. Schlegel sur le droit constitutionnel ?"

### Workflow

**Recherche**
```json
{
  "search": "Schlegel constitution",
  "sort": "-date"
}
```

Note : Le système cherche dans les champs `authors` et `editors`.

### Présentation
- Liste des commentaires de l'auteur
- Domaines d'expertise identifiés
- Chronologie des publications
- Évolution de la position doctrinale

---

## Exemple 5 : Workflow Intégré Doctrine + Jurisprudence

### Question
"Un employeur peut-il surveiller les emails professionnels ?"

### Workflow en 4 phases

**PHASE 1 - DOCTRINE (cette skill)**

Recherche 1 : Protection personnalité travailleur
```json
{
  "search": "Art. 328 CO surveillance",
  "language": "fr"
}
```

Recherche 2 : Droit à la vie privée
```json
{
  "search": "Art. 13 Cst. vie privée",
  "language": "fr"
}
```

Résultat : Cadre juridique et principes généraux

**PHASE 2 - JURISPRUDENCE (`@swiss-case-law-research`)**

Recherche : Arrêts sur surveillance au travail
```
"Überwachung Email Arbeitgeber" OR "surveillance email employeur"
```

Filtrer : BGer (principe) + cantons (applications)
Résultat : Cas concrets et limites admises

**PHASE 3 - SYNTHÈSE**
- Doctrine : Protection forte mais pas absolue
- Jurisprudence : Surveillance admise si proportionnée et transparente
- Application : Politique claire requise, consentement préférable

**PHASE 4 - RÉPONSE**
- Présentation intégrée des deux sources
- Recommandations pratiques
- Référence aux commentaires ET arrêts pertinents

---

## Cas d'Usage par Profil

### Étudiant en Droit

**Contexte** : Préparation d'un examen sur le droit de la filiation

**Workflow** :
1. Recherche : "filiation" dans CC
2. Identification : Art. 252-269 CC couverts
3. Lecture commentaires clés (Art. 252, 255, 260)
4. Synthèse structurée pour révision

**Requête**
```json
{
  "search": "filiation",
  "legislative_act": "CC",
  "language": "fr"
}
```

---

### Avocat Praticien

**Contexte** : Préparation d'un dossier de licenciement abusif

**Workflow** :
1. Commentaire Art. 336 CO (licenciement abusif)
2. Extraction principes et conditions
3. Recherche arrêts BGer mentionnés (via `@swiss-case-law-research`)
4. Vérification jurisprudence récente 2023-2024
5. Construction argumentation juridique

**Requête**
```json
{
  "search": "336 licenciement abusif",
  "language": "fr",
  "sort": "-date"
}
```

---

### Citoyen avec Question

**Contexte** : Comprendre ses droits de protection de la personnalité au travail

**Workflow** :
1. Récupération commentaire Art. 328 CO en français
2. Explication claire et vulgarisée
3. Exemples concrets d'application
4. Mention : consulter avocat pour cas personnel

**Présentation adaptée** :
- Langage simple, pas de jargon
- Exemples de la vie quotidienne
- Points clés en gras
- Avertissement pour cas concret

---

## Exemple de Réponse Complète

### Question : "Quels sont mes droits si mon employeur lit mes emails ?"

### Réponse Structurée

```markdown
# Protection de la Personnalité au Travail : Surveillance des Emails

## Vue d'Ensemble
- **Article principal** : Art. 328 CO (protection de la personnalité)
- **Cadre constitutionnel** : Art. 13 Cst. (vie privée)
- **Commentaires consultés** : 2

## Principe Doctrinal

**Art. 328 CO** impose à l'employeur de protéger la personnalité du 
travailleur, y compris sa vie privée sur le lieu de travail.

**Points clés selon la doctrine** :
1. L'employeur ne peut pas surveiller les communications privées
2. Les emails professionnels peuvent être contrôlés sous conditions
3. Une politique claire de surveillance doit exister
4. Le consentement du travailleur est recommandé

## Application Pratique

### Ce que l'employeur PEUT faire :
- Surveiller l'usage professionnel avec politique claire
- Contrôler en cas de soupçon fondé d'abus
- Mettre en place un règlement informatique

### Ce que l'employeur NE PEUT PAS faire :
- Lire les emails marqués "privé/personnel"
- Surveiller de façon cachée sans information préalable
- Utiliser les données à d'autres fins que celles prévues

## Références

**Commentaire consulté** :
- [Auteur], Art. 328 CO, Onlinekommentar, [date]
- Lien : [URL]

**Arrêts mentionnés** (à consulter via jurisprudence) :
- ATF 130 II 425 : Principes de surveillance
- ATF 139 II 7 : Proportionnalité

## Recommandation

Pour votre situation spécifique, je vous conseille de :
1. Vérifier si votre entreprise a un règlement informatique
2. Consulter un avocat spécialisé en droit du travail

---
*Source : Onlinekommentar.ch - Consultation [date]*
*Ces informations sont à titre indicatif. Consultez un professionnel pour votre cas.*
```

---

## Erreurs Courantes et Corrections

### Erreur 1 : Recherche trop vague

❌ `{"search": "travail"}`
→ Des centaines de résultats non ciblés

✅ `{"search": "Art. 336 CO licenciement", "language": "fr"}`
→ Résultats précis et pertinents

### Erreur 2 : Ignorer la langue

❌ Présenter un commentaire allemand à un utilisateur francophone sans explication

✅ "Le commentaire le plus complet est disponible en allemand. Voici les points clés traduits..."

### Erreur 3 : Ne pas vérifier la date

❌ Présenter un commentaire de 2018 comme actuel

✅ "Ce commentaire date de 2018. La loi a été révisée en 2023, certains points peuvent avoir évolué."
