# 🧰 MCP Tools Reference - Legal Assistant

Ce document liste tous les outils (tools) disponibles via les serveurs MCP installés.

## 📦 Entscheidsuche MCP Server

### 🔍 Tool: `search_case_law`

Recherche dans la jurisprudence suisse (tribunaux fédéraux et cantonaux).

**Paramètres:**
- `query` (string, requis) - Requête de recherche
- `page` (number, optionnel) - Numéro de page pour la pagination
- `pageSize` (number, optionnel) - Nombre de résultats par page (défaut: 20)

**Exemples d'utilisation:**

```javascript
// Recherche simple
{
  "query": "Datenschutz DSGVO"
}

// Recherche avec pagination
{
  "query": "Kündigungsschutz",
  "page": 1,
  "pageSize": 10
}

// Recherche de phrase exacte
{
  "query": "\"protection de la personnalité\""
}

// Recherche avec opérateurs booléens
{
  "query": "travail AND licenciement NOT abusif"
}

// Recherche par champ
{
  "query": "court:BGer date:2023"
}
```

**Réponse:**
```json
{
  "total": 150,
  "hits": [
    {
      "signature": "CH_BGer_2023_1C_123_2023",
      "spider": "CH_BGer",
      "title": "Titre de la décision",
      "date": "2023-03-15",
      "court": "Bundesgericht",
      "extract": "Extrait pertinent...",
      "url": "https://entscheidsuche.ch/docs/..."
    }
  ]
}
```

---

### 📄 Tool: `get_document`

Récupère le contenu complet d'une décision de justice.

**Paramètres:**
- `signature` (string, requis) - Signature unique du document
- `spider` (string, requis) - Identifiant du tribunal (ex: "CH_BGer")
- `format` (string, optionnel) - Format souhaité: "json", "html", ou "pdf" (défaut: "json")

**Exemples d'utilisation:**

```javascript
// Récupérer en JSON (défaut)
{
  "signature": "CH_BGer_2023_1C_123_2023",
  "spider": "CH_BGer"
}

// Récupérer en HTML
{
  "signature": "CH_BGer_2023_1C_123_2023",
  "spider": "CH_BGer",
  "format": "html"
}

// Récupérer en PDF
{
  "signature": "CH_BGer_2023_1C_123_2023",
  "spider": "CH_BGer",
  "format": "pdf"
}
```

**Réponse (format JSON):**
```json
{
  "signature": "CH_BGer_2023_1C_123_2023",
  "title": "Titre complet de l'arrêt",
  "date": "2023-03-15",
  "court": "Bundesgericht",
  "chamber": "I. öffentlich-rechtliche Abteilung",
  "facts": "Exposé des faits...",
  "considerations": "Considérants...",
  "ruling": "Dispositif...",
  "full_text": "Texte intégral...",
  "pdf_url": "https://..."
}
```

---

### 🏛️ Tool: `list_courts`

Liste tous les tribunaux disponibles et le nombre de documents.

**Paramètres:** Aucun

**Exemple d'utilisation:**

```javascript
{}
```

**Réponse:**
```json
{
  "courts": [
    {
      "spider": "CH_BGer",
      "name": "Bundesgericht (Tribunal fédéral)",
      "type": "federal",
      "document_count": 45678,
      "date_range": {
        "from": "2000-01-01",
        "to": "2024-12-31"
      }
    },
    {
      "spider": "CH_BGE",
      "name": "Bundesgerichtsentscheide",
      "type": "federal_published",
      "document_count": 12345,
      "date_range": {
        "from": "1875-01-01",
        "to": "2024-12-31"
      }
    },
    {
      "spider": "CH_ZH_Obergericht",
      "name": "Obergericht Zürich",
      "type": "cantonal",
      "document_count": 8765,
      "date_range": {
        "from": "2010-01-01",
        "to": "2024-12-31"
      }
    }
  ]
}
```

---

## 📚 Onlinekommentar MCP Server

### 🔍 Tool: `search_commentaries`

Recherche dans les commentaires juridiques suisses.

**Paramètres:**
- `search` (string, requis) - Requête de recherche
- `language` (string, optionnel) - Langue du contenu: "en", "de", "fr", "it"
- `legislative_act` (string, optionnel) - Filtrer par acte législatif (ID)
- `sort` (string, optionnel) - Ordre de tri: "title", "-title", "date", "-date"
- `page` (number, optionnel) - Numéro de page (défaut: 1)

**Exemples d'utilisation:**

```javascript
// Recherche simple
{
  "search": "intellectual property"
}

// Recherche en français
{
  "search": "protection des données",
  "language": "fr"
}

// Recherche avec tri par date (plus récent d'abord)
{
  "search": "droit du travail",
  "sort": "-date",
  "language": "fr"
}

// Recherche avec pagination
{
  "search": "Vertragsrecht",
  "language": "de",
  "page": 2
}
```

**Réponse:**
```json
{
  "count": 45,
  "next": "https://onlinekommentar.ch/api/commentaries?page=2",
  "previous": null,
  "results": [
    {
      "id": "6d8aee6b-86d0-43f2-8110-2d5b7360dd18",
      "title": "Art. 328 OR - Schutz der Persönlichkeit des Arbeitnehmers",
      "title_de": "...",
      "title_fr": "...",
      "title_it": "...",
      "title_en": "...",
      "publication_date": "2023-05-15",
      "authors": ["Dr. Max Mustermann"],
      "legislative_act": {
        "id": "SR-220",
        "name": "Code des Obligations",
        "abbreviation": "CO"
      },
      "url": "https://onlinekommentar.ch/commentaries/..."
    }
  ]
}
```

---

### 📖 Tool: `get_commentary`

Récupère le contenu complet d'un commentaire spécifique.

**Paramètres:**
- `id` (string, requis) - Identifiant unique du commentaire

**Exemples d'utilisation:**

```javascript
{
  "id": "6d8aee6b-86d0-43f2-8110-2d5b7360dd18"
}
```

**Réponse:**
```json
{
  "id": "6d8aee6b-86d0-43f2-8110-2d5b7360dd18",
  "title": "Art. 328 OR - Protection de la personnalité du travailleur",
  "title_de": "Art. 328 OR - Schutz der Persönlichkeit des Arbeitnehmers",
  "title_fr": "Art. 328 OR - Protection de la personnalité du travailleur",
  "title_it": "Art. 328 CO - Protezione della personalità del lavoratore",
  "title_en": "Art. 328 CO - Protection of the employee's personality",
  
  "legislative_act": {
    "id": "SR-220",
    "name": "Code des Obligations",
    "abbreviation": "CO",
    "article": "328",
    "title": "Protection de la personnalité du travailleur"
  },
  
  "authors": [
    {
      "name": "Dr. Max Mustermann",
      "institution": "Université de Zurich"
    }
  ],
  
  "editors": [
    {
      "name": "Prof. Dr. Jane Doe"
    }
  ],
  
  "publication_date": "2023-05-15",
  "last_updated": "2024-01-20",
  
  "legal_text": {
    "de": "Text des Gesetzesartikels...",
    "fr": "Texte de l'article de loi...",
    "it": "Testo dell'articolo di legge...",
    "en": "Text of the legal article..."
  },
  
  "commentary": {
    "de": "Ausführlicher Kommentar...",
    "fr": "Commentaire détaillé...",
    "it": "Commento dettagliato...",
    "en": "Detailed commentary..."
  },
  
  "references": [
    {
      "type": "case_law",
      "citation": "BGE 140 II 136",
      "url": "https://..."
    },
    {
      "type": "literature",
      "citation": "Müller, Kommentar zum OR, 2020",
      "page": "234-245"
    }
  ],
  
  "related_articles": [
    {
      "id": "another-commentary-id",
      "article": "328a",
      "title": "Article connexe"
    }
  ],
  
  "url": "https://onlinekommentar.ch/commentaries/6d8aee6b-86d0-43f2-8110-2d5b7360dd18"
}
```

---

## 🎯 Cas d'Usage Combinés

### Exemple 1 : Recherche Complète sur un Sujet

```javascript
// 1. Chercher la jurisprudence
search_case_law({
  "query": "Art. 328 CO protection personnalité travailleur"
})

// 2. Chercher les commentaires
search_commentaries({
  "search": "Article 328 Code Obligations",
  "language": "fr"
})

// 3. Récupérer un document spécifique
get_document({
  "signature": "CH_BGer_2023_4A_123_2023",
  "spider": "CH_BGer",
  "format": "html"
})

// 4. Récupérer un commentaire détaillé
get_commentary({
  "id": "6d8aee6b-86d0-43f2-8110-2d5b7360dd18"
})
```

### Exemple 2 : Analyse Multilingue

```javascript
// Chercher en allemand
search_case_law({
  "query": "Datenschutz DSGVO"
})

search_commentaries({
  "search": "Datenschutz",
  "language": "de"
})

// Puis chercher les équivalents en français
search_commentaries({
  "search": "protection des données",
  "language": "fr"
})
```

---

## 📝 Notes sur l'Utilisation

### Syntaxe de Recherche Elasticsearch (Entscheidsuche)

- **Phrase exacte** : `"protection de la personnalité"`
- **ET logique** : `travail AND licenciement`
- **OU logique** : `congé OR démission`
- **NON logique** : `contrat NOT travail`
- **Recherche par champ** : `court:BGer`, `date:2023`, `title:"licenciement"`
- **Wildcard** : `protect*` (tous les mots commençant par protect)
- **Proximité** : `"protection personnalité"~5` (dans un rayon de 5 mots)

### Codes des Tribunaux Principaux

- **CH_BGer** : Bundesgericht / Tribunal fédéral
- **CH_BGE** : Bundesgerichtsentscheide (arrêts publiés)
- **CH_BVGer** : Bundesverwaltungsgericht / Tribunal administratif fédéral
- **CH_BStGer** : Bundesstrafgericht / Tribunal pénal fédéral
- **CH_ZH_Obergericht** : Obergericht Zürich
- **CH_GE_Cour** : Cour de justice de Genève
- ... et bien d'autres cantons

### Langues Supportées

| Code | Langue |
|------|--------|
| `de` | Allemand |
| `fr` | Français |
| `it` | Italien |
| `en` | Anglais |

---

## 🔗 Ressources API

- **Entscheidsuche API** : `https://entscheidsuche.ch/_search.php`
- **Onlinekommentar API** : `https://onlinekommentar.ch/api`

Pour plus d'informations, consultez la [documentation détaillée des serveurs](./mcp-servers/README.md).
