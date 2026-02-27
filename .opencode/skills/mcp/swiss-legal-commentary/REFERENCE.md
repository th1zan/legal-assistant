# Références - Swiss Legal Commentary

Sources, documentation MCP et actes législatifs couverts par Onlinekommentar.ch.

## Onlinekommentar.ch - Présentation

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

---

## Actes Législatifs Couverts

### Droit Constitutionnel et Public

| Code RS | Titre | Abréviation | Volume |
|---------|-------|-------------|--------|
| SR-101 | Constitution fédérale | Cst. / BV / FC | ~140 art. |
| SR-172.021 | Loi sur l'organisation du gouvernement | LOGA | ~50 art. |
| SR-141.1 | Loi sur le Parlement | LParl | ~80 art. |
| SR-161.1 | Loi sur les droits politiques | LDP | ~90 art. |

### Droit Civil

| Code RS | Titre | Abréviation | Volume |
|---------|-------|-------------|--------|
| SR-210 | Code civil suisse | CC / ZGB | ~900 art. |
| SR-220 | Code des obligations | CO / OR | ~1,200 art. |
| SR-221.301 | Loi sur la poursuite et faillite | LP / SchKG | ~350 art. |

### Droit Pénal

| Code RS | Titre | Abréviation | Volume |
|---------|-------|-------------|--------|
| SR-311.0 | Code pénal suisse | CP / StGB | ~400 art. |
| SR-312.0 | Code de procédure pénale | CPP / StPO | ~450 art. |

### Droit Administratif Spécial

| Code RS | Titre | Abréviation | Volume |
|---------|-------|-------------|--------|
| SR-235.1 | Loi fédérale sur la protection des données | LPD / DSG | ~70 art. |
| SR-351.1 | Loi sur l'entraide pénale internationale | EIMP / IRSG | ~100 art. |
| SR-784.10 | Loi sur les télécommunications | LTC | ~100 art. |

**Note** : La plateforme couvre une sélection croissante de lois fédérales, avec focus sur les domaines les plus demandés.

---

## Commandes MCP

### search_commentaries

**Description** : Recherche dans la base de commentaires juridiques

**Paramètres** :
| Paramètre | Type | Requis | Description |
|-----------|------|--------|-------------|
| `search` | string | ✅ Oui | Requête de recherche full-text |
| `language` | enum | Non | Langue: `de`, `fr`, `it`, `en` |
| `legislative_act` | string | Non | ID de l'acte législatif |
| `sort` | enum | Non | Tri: `title`, `-title`, `date`, `-date` |
| `page` | number | Non | Page pour pagination (défaut: 1) |

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
| Paramètre | Type | Requis | Description |
|-----------|------|--------|-------------|
| `id` | string | ✅ Oui | UUID du commentaire |

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

---

## Liens Utiles

### Documentation Officielle
- **Site principal** : https://onlinekommentar.ch
- **À propos** : https://onlinekommentar.ch/de/ueber-onlinekommentar
- **Auteurs et éditeurs** : https://onlinekommentar.ch/de/autorinnen
- **Soutiens** : https://onlinekommentar.ch/de/unterstuetzerinnen

### Documentation Interne
- **MCP README** : `mcp-servers/README.md`
- **Référence outils** : `MCP_TOOLS_REFERENCE.md`

### Mise à Jour du Serveur MCP

```bash
cd mcp-servers/onlinekommentar-mcp
git pull
npm install
npm run build
```

---

## Complémentarité avec Autres Skills

### Workflow Doctrine + Jurisprudence

```
1. DOCTRINE (cette skill - @swiss-legal-commentary)
   → Identifier cadre juridique
   → Comprendre principes généraux
   → Noter arrêts clés mentionnés

2. JURISPRUDENCE (@swiss-case-law-research)
   → Rechercher arrêts mentionnés dans commentaire
   → Vérifier jurisprudence récente
   → Analyser application pratique

3. SYNTHÈSE
   → Principe doctrinal + Application jurisprudentielle
   → Cohérence ou divergence
   → Recommandation finale
```

### Skills Complémentaires

| Skill | Usage |
|-------|-------|
| `@swiss-case-law-research` | Recherche jurisprudence TF/TAF/TPF |
| `@parse-decision` | Extraction structurée d'arrêts |
| `@citation-formatter` | Formatage citations juridiques |
| `@identify-legal-issues` | Identification questions juridiques |

---

## Meilleures Pratiques

### À FAIRE ✅

1. **Commencer spécifique** : Si article connu, rechercher directement
2. **Vérifier les auteurs** : Auteurs reconnus = commentaire de qualité
3. **Lire le texte de loi d'abord** : Essentiel pour comprendre le commentaire
4. **Noter les références** : ATF/BGE cités → rechercher avec jurisprudence
5. **Privilégier commentaires récents** : Trier par date (`sort: "-date"`)
6. **Citer correctement** : Auteur(s), titre, date, lien

### À ÉVITER ❌

1. **Ne pas ignorer la langue** : Toujours vérifier disponibilité multilingue
2. **Ne pas limiter à un seul commentaire** : Comparer 2-3 si disponibles
3. **Ne pas négliger les éditeurs** : Rôle de validation important
4. **Ne pas oublier les articles connexes** : Vision systématique
5. **Ne pas substituer à conseil juridique** : Commentaire ≠ conseil

---

## Format de Citation

### Citation Standard

```
[Auteur], [Titre du commentaire], in: Onlinekommentar, [Date], 
disponible sur: [URL] (consulté le [date])
```

### Exemple

```
MÜLLER Peter, Art. 328 CO - Protection de la personnalité, 
in: Onlinekommentar, 15.03.2024, disponible sur: 
https://onlinekommentar.ch/fr/commentaries/or328 (consulté le 27.02.2026)
```
