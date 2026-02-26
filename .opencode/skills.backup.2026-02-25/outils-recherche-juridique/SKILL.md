---
name: outils-recherche-juridique
description: "Outils techniques pour la recherche juridique suisse : MCP servers (entscheidsuche, onlinekommentar), CLI (Fedlex SPARQL), APIs cantonales. Skill transversale centralisant tous les outils d'accès aux sources juridiques. Utiliser cette skill quand l'utilisateur veut savoir comment accéder techniquement aux sources juridiques suisses (CLI, MCP, API, web scraping)."
---

# Outils de recherche juridique suisse

Skill transversale centralisant **tous les outils techniques** pour accéder aux sources juridiques suisses.

> **Principe** : Les skills de contenu juridique (sources-cantonales, sources-legislatives-federales, jurisprudence-suisse) décrivent **quoi** chercher. Cette skill décrit **comment** y accéder techniquement.

## Hiérarchie d'accès (priorité)

```
1. CLI (scripts locaux)     → Meilleur contrôle, reproductible
2. MCP (serveurs intégrés)  → Intégration native OpenCode
3. API (endpoints REST/JSON) → Programmable, stable
4. Web (fetch/scraping)     → Dernier recours
```

## Vue d'ensemble des outils

| Source | Type | CLI | MCP | API | Web | Priorité |
|--------|------|-----|-----|-----|-----|----------|
| **Fedlex** (législation fédérale) | Législation | ✅ `fedlex_sparql.py` | ❌ | ✅ SPARQL | ✅ | **CLI/API** |
| **entscheidsuche.ch** | Jurisprudence | ❌ | ✅ `@entscheidsuche` | ✅ JSON/ES | ✅ | **MCP/API** |
| **onlinekommentar.ch** | Doctrine | ❌ | ✅ `@onlinekommentar` | ✅ JSON | ✅ | **MCP/API** |
| **bger.ch** | Jurisprudence TF | ❌ | ❌ | ⚠️ Limited | ✅ | **Web** |
| **Lexfind** | Portail cantonal | ❌ | ❌ | ❌ | ✅ | **Web** |
| **Sites cantonaux** | Législation | ❌ | ❌ | ⚠️ Certains | ✅ | **Web/API** |

---

## 1. Fedlex — CLI SPARQL

### Description

Fedlex (data.fedlex.admin.ch) est la source officielle pour la législation fédérale suisse. Elle expose un **endpoint SPARQL** avec des données RDF/Linked Data.

Le CLI `fedlex_sparql.py` permet d'accéder à **9000+ lois fédérales** via un mapping local RS → ELI.

### Installation

```bash
# Dépendances (avec uv)
uv run --with sparqlwrapper --with requests --with beautifulsoup4 python scripts/fedlex_sparql.py --help

# Ou installation classique
pip install sparqlwrapper requests beautifulsoup4
python scripts/fedlex_sparql.py --help
```

### Commandes disponibles

| Commande | Description | Exemple |
|----------|-------------|---------|
| `generate-mapping` | Génère le mapping complet RS → ELI (~9000 lois, 10-30s) | `generate-mapping` |
| `list` | Liste toutes les lois du mapping local | `list` |
| `url <RS>` | Obtient l'URL d'une loi | `url 210` |
| `search <query>` | Recherche par mots-clés (instantané) | `search "code civil"` |
| `get <RS>` | Télécharge le contenu d'une loi | `get 210` |
| `metadata <RS>` | Affiche les métadonnées d'une loi | `metadata 210` |
| `history <RS>` | Liste les versions historiques | `history 210` |

### Utilisation

```bash
# Générer le mapping complet (à faire une fois)
python scripts/fedlex_sparql.py generate-mapping

# Rechercher une loi par numéro RS
python scripts/fedlex_sparql.py url 210

# Rechercher par mots-clés (instantané, dans le mapping local)
python scripts/fedlex_sparql.py search "protection données"

# Télécharger le HTML brut
python scripts/fedlex_sparql.py get 210

# Télécharger en texte brut (sans balises HTML)
python scripts/fedlex_sparql.py get 210 --text

# Sauvegarder dans un fichier
python scripts/fedlex_sparql.py get 210 --output code_civil.html
python scripts/fedlex_sparql.py get 210 --text --output code_civil.txt

# Télécharger en PDF
python scripts/fedlex_sparql.py get 210 --format pdf --output code_civil.pdf

# Télécharger en XML (Akoma Ntoso)
python scripts/fedlex_sparql.py get 210 --format xml --output code_civil.xml

# Télécharger en DOCX
python scripts/fedlex_sparql.py get 210 --format docx --output code_civil.docx

# Lister les versions historiques
python scripts/fedlex_sparql.py history 210
```

### Options de la commande `get`

| Option | Description | Défaut |
|--------|-------------|--------|
| `--format`, `-f` | Format: html, pdf, xml, docx | html |
| `--lang` | Langue: fr, de, it | fr |
| `--text`, `-t` | Extraire le texte brut (HTML uniquement) | false |
| `--output`, `-o` | Sauvegarder dans un fichier | - |

### Endpoints

| Endpoint | URL | Format |
|----------|-----|--------|
| SPARQL | `https://fedlex.data.admin.ch/sparqlendpoint` | RDF/SPARQL |
| Linked Data | `https://fedlex.data.admin.ch/eli/cc/{rs}` | RDF/JSON-LD |
| Filestore | `https://fedlex.data.admin.ch/filestore/...` | PDF/HTML/DOCX/XML |

### Architecture des données Fedlex

```
ConsolidationAbstract (loi abstraite, identifiée par RS)
└── Consolidation (version datée)
    └── Expression (version linguistique)
        └── Manifestation (format de fichier)
            └── isExemplifiedBy → URL de téléchargement
```

### Exemple de requête SPARQL

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?act ?title ?sr WHERE {
  ?act a jolux:ConsolidationAbstract ;
       skos:prefLabel ?title ;
       jolux:classifiedByTaxonomyEntry ?sr .
  FILTER(CONTAINS(LCASE(?title), "code civil"))
  FILTER(LANG(?title) = "fr")
}
LIMIT 10
```

---

## 2. Entscheidsuche — MCP Server

### Description

Serveur MCP pour la recherche de jurisprudence suisse (1M+ décisions). Couvre les tribunaux fédéraux ET cantonaux.

### Configuration

Déjà configuré dans `.opencode/mcp.json` :

```json
{
  "mcpServers": {
    "entscheidsuche": {
      "command": "node",
      "args": ["mcp-servers/entscheidsuche-mcp/build/index.js"]
    }
  }
}
```

### Outils disponibles

| Outil | Description | Paramètres |
|-------|-------------|------------|
| `search_case_law` | Recherche de décisions | `query`, `size`, `spider`, `date_from`, `date_to` |
| `get_document` | Récupérer un document complet | `doc_id`, `format` (json/html/pdf) |
| `list_courts` | Liste des tribunaux indexés | — |

### Codes des tribunaux (spider)

**Fédéraux** :
- `CH_BGer` — Tribunal fédéral (arrêts non publiés)
- `CH_BGE` — ATF (arrêts publiés)
- `CH_BVGer` — Tribunal administratif fédéral
- `CH_BStGer` — Tribunal pénal fédéral
- `CH_BPatGer` — Tribunal fédéral des brevets

**Cantonaux (exemples)** :
- `CH_ZH_Obergericht` — Obergericht Zürich
- `CH_GE_Cour` — Cour de justice Genève
- `CH_VD_TC` — Tribunal cantonal Vaud
- `CH_BE_Obergericht` — Obergericht Bern

### Exemple d'utilisation

```
User: Cherche des décisions du Tribunal fédéral sur la protection des données depuis 2020

Agent: [Utilise search_case_law avec query="protection des données", spider="CH_BGer", date_from="2020-01-01"]
```

### API directe (alternative au MCP)

```bash
# Recherche
curl "https://entscheidsuche.ch/_search.php?query=Datenschutz&size=10"

# Document spécifique
curl "https://entscheidsuche.ch/docs/{court}/{year}/{doc_id}.json"

# Statut des tribunaux
curl "https://entscheidsuche.ch/status"
```

---

## 3. Onlinekommentar — MCP Server

### Description

Serveur MCP pour accéder aux commentaires juridiques suisses open access. Premier commentaire non-profit de Suisse.

### Configuration

Déjà configuré dans `.opencode/mcp.json` :

```json
{
  "mcpServers": {
    "onlinekommentar": {
      "command": "node",
      "args": ["mcp-servers/onlinekommentar-mcp/build/index.js"]
    }
  }
}
```

### Outils disponibles

| Outil | Description | Paramètres |
|-------|-------------|------------|
| `search_commentaries` | Recherche de commentaires | `query`, `language`, `law_code` |
| `get_commentary` | Récupérer un commentaire par ID | `id` |

### Lois couvertes

- **Droit constitutionnel** : Cst. (SR 101)
- **Droit civil** : CC (SR 210), CO (SR 220), LP (SR 281.1)
- **Droit pénal** : CP (SR 311.0), CPP (SR 312.0)
- **Droit administratif** : LPD (SR 235.1), LTC (SR 784.10)

### Langues

Allemand (DE), Français (FR), Italien (IT), Anglais (EN)

### API directe (alternative au MCP)

```bash
# Recherche
curl "https://onlinekommentar.ch/api/commentaries?search=Art.%20328%20CO&language=fr"

# Commentaire spécifique
curl "https://onlinekommentar.ch/api/commentaries/{id}"
```

---

## 4. APIs cantonales

### Cantons avec API/OGD

| Canton | Type | URL | Format |
|--------|------|-----|--------|
| **Zürich** | OGD | opendata.swiss (filter: zh) | JSON/CSV |
| **Bern** | OGD | opendata.swiss (filter: be) | JSON/CSV |
| **Genève** | SITG | ge.ch/sitg | GeoJSON |
| **Basel-Stadt** | OGD | data.bs.ch | JSON |

> **Note** : La plupart des APIs cantonales concernent les données géographiques, pas la législation. Pour la législation, utiliser les sites officiels (voir `@sources-cantonales`).

### Portail Fedlex vers les cantons

Fedlex fournit les liens vers tous les recueils cantonaux :
- **URL** : https://www.fedlex.admin.ch/fr/links
- Voir `references/liens-cantonaux.md` pour la liste complète

---

## 5. Autres sources (Web uniquement)

### bger.ch — Tribunal fédéral

- **URL** : https://www.bger.ch/ext/eurospider/live/fr/php/aza/index.php
- **Accès** : Recherche plein texte gratuite
- **API** : Non disponible publiquement
- **Recommandation** : Utiliser `@entscheidsuche` (MCP) pour la recherche, bger.ch pour les documents officiels

### Lexfind — Portail cantonal

- **URL** : https://www.lexfind.ch
- **Accès** : Liens vers tous les recueils cantonaux
- **API** : Non disponible
- **Recommandation** : Utiliser comme portail de navigation, puis accéder aux sites cantonaux directement

### Swisslex (payant)

- **URL** : https://www.swisslex.ch
- **Accès** : Abonnement requis (universités, études d'avocats)
- **API** : Non disponible publiquement
- **Contenu** : Législation + jurisprudence + doctrine (le plus complet)

---

## Tableau récapitulatif par usage

### Pour la législation fédérale

| Besoin | Outil recommandé | Commande/Action |
|--------|------------------|-----------------|
| Texte de loi en vigueur | CLI Fedlex | `fedlex_sparql.py get 210` |
| Texte brut (sans HTML) | CLI Fedlex | `fedlex_sparql.py get 210 --text` |
| Télécharger en PDF | CLI Fedlex | `fedlex_sparql.py get 210 -f pdf -o loi.pdf` |
| Recherche par mots-clés | CLI Fedlex | `fedlex_sparql.py search "..."` |
| Version historique | CLI Fedlex | `fedlex_sparql.py history 210` |

### Pour la jurisprudence

| Besoin | Outil recommandé | Commande/Action |
|--------|------------------|-----------------|
| Recherche TF | MCP entscheidsuche | `search_case_law(query="...", spider="CH_BGer")` |
| Recherche cantonale | MCP entscheidsuche | `search_case_law(query="...", spider="CH_GE_Cour")` |
| Document complet | MCP entscheidsuche | `get_document(doc_id="...", format="pdf")` |

### Pour la doctrine

| Besoin | Outil recommandé | Commande/Action |
|--------|------------------|-----------------|
| Commentaire d'article | MCP onlinekommentar | `search_commentaries(query="Art. 328 CO")` |
| Commentaire par ID | MCP onlinekommentar | `get_commentary(id="...")` |

### Pour la législation cantonale

| Besoin | Outil recommandé | Action |
|--------|------------------|--------|
| Recherche de loi | Web (site cantonal) | Voir `@sources-cantonales` |
| Jurisprudence cantonale | MCP entscheidsuche | `search_case_law(spider="CH_{canton}_...")` |

---

## Références

- `references/liens-cantonaux.md` — Liens vers tous les recueils cantonaux
- `references/sparql-examples.md` — Exemples de requêtes SPARQL pour Fedlex
- `scripts/fedlex_sparql.py` — CLI pour Fedlex

## Skills connexes

Pour le **contenu juridique** (quoi chercher) :
- `@sources-legislatives-federales` — Législation fédérale
- `@sources-cantonales` — Législation cantonale
- `@jurisprudence-suisse` — Jurisprudence
- `@sources-doctrinales` — Doctrine

Pour les **méthodologies** :
- `@techniques-recherche-juridique` — Opérateurs booléens, troncature
- `@methodologie-recherche-jurisprudentielle` — Méthode systématique
