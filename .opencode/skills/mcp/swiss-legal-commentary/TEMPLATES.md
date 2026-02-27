# Templates - Swiss Legal Commentary

Templates de présentation pour les recherches de commentaires doctrinaux via Onlinekommentar.ch.

## Template de Réponse Complète

```markdown
# Commentaire Doctrinal : [Sujet]

## Vue d'Ensemble
- **Commentaires trouvés** : [nombre]
- **Acte(s) législatif(s)** : [lois concernées]
- **Langue(s)** : [langues disponibles]

## Recherche Effectuée

### Requête utilisée
```
[termes de recherche]
```

### Filtres appliqués
- Langue : [langue ou "toutes"]
- Acte législatif : [loi spécifique ou "tous"]
- Tri : [ordre de tri]

## Commentaires Sélectionnés

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

## Synthèse Doctrinale

### Consensus Académique
[Points sur lesquels les auteurs s'accordent]

### Débats Doctrinaux
[Points de désaccord ou d'interprétation divergente]

### Évolution de la Doctrine
[Comment la position doctrinale a évolué dans le temps]

### Rapport avec la Jurisprudence
[Degré d'alignement entre doctrine et jurisprudence]

## Application Pratique

### Au Cas de l'Utilisateur
[Comment ces commentaires s'appliquent à la situation spécifique]

### Recommandations
[Conseils basés sur l'analyse doctrinale]

## Approfondissements Suggérés

### Articles Connexes
1. [Article X] : [Pourquoi pertinent]
2. [Article Y] : [Pourquoi pertinent]

### Jurisprudence à Consulter
[Utiliser skill "@swiss-case-law-research" pour :]
- [Arrêt 1 mentionné dans commentaire]
- [Arrêt 2 mentionné dans commentaire]

### Doctrine Complémentaire
- [Ouvrage 1 cité]
- [Article de revue 2 cité]

## Avertissement

Ces commentaires doctrinaux sont fournis à titre informatif et académique. Pour des conseils juridiques spécifiques, consultez un avocat qualifié.

---

**Sources** :
- Onlinekommentar.ch (plateforme Open Access)
- Auteurs : [Liste des auteurs consultés]
- Consultation effectuée : [Date]
```

## Template de Requête MCP

### Recherche par Article

```json
{
  "search": "[numéro article] [nom loi]",
  "language": "fr",
  "sort": "-date"
}
```

### Recherche Thématique

```json
{
  "search": "[thème principal]",
  "language": "fr",
  "sort": "-date",
  "page": 1
}
```

### Recherche par Auteur

```json
{
  "search": "[nom auteur] [domaine optionnel]",
  "sort": "-date"
}
```

### Récupération Détaillée

```json
{
  "id": "[UUID du commentaire]"
}
```

## Template de Synthèse Courte

Pour les questions simples, utiliser ce format condensé :

```markdown
## [Titre : Article X Loi Y]

**Auteur** : [Nom] ([Institution])  
**Mise à jour** : [Date]

### Principe
[1-2 phrases résumant le principe principal]

### Application
[1-2 phrases sur l'application pratique]

### Références clés
- ATF [référence] : [point clé]
- [Doctrine] : [point clé]

**Source** : [Lien onlinekommentar.ch]
```

## Vocabulaire Thématique Multilingue

| Thème | DE | FR | IT | EN |
|-------|----|----|----|----|
| Protection données | Datenschutz | Protection des données | Protezione dei dati | Data protection |
| Droit du travail | Arbeitsrecht | Droit du travail | Diritto del lavoro | Employment law |
| Droits fondamentaux | Grundrechte | Droits fondamentaux | Diritti fondamentali | Fundamental rights |
| Contrats | Vertragsrecht | Droit des contrats | Diritto dei contratti | Contract law |
| Propriété intellectuelle | Immaterialgüterrecht | Propriété intellectuelle | Proprietà intellettuale | Intellectual property |
| Responsabilité civile | Haftpflichtrecht | Responsabilité civile | Responsabilità civile | Tort law |
| Droit de la famille | Familienrecht | Droit de la famille | Diritto di famiglia | Family law |
| Droit des sociétés | Gesellschaftsrecht | Droit des sociétés | Diritto societario | Corporate law |

## Glossaire des Domaines Juridiques

| Terme DE | Terme FR | Description |
|----------|----------|-------------|
| Verfassungsrecht | Droit constitutionnel | Droits fondamentaux, organisation État |
| Zivilrecht | Droit civil | Personnes, famille, contrats, biens |
| Strafrecht | Droit pénal | Infractions et sanctions |
| Verwaltungsrecht | Droit administratif | Organisation et action administrative |
| Verfahrensrecht | Droit de procédure | Règles de procédure |
| Arbeitsrecht | Droit du travail | Relations de travail |
| Sozialversicherungsrecht | Droit des assurances sociales | AVS, AI, chômage, etc. |
