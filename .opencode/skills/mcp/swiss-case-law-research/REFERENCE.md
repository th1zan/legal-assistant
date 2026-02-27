# Références - Swiss Case Law Research

Structure judiciaire suisse, codes des tribunaux, et documentation technique pour Entscheidsuche.

---

## Structure Judiciaire Suisse

### Juridictions Fédérales

| Code Spider | Nom Complet | Type | Volume Approx. |
|-------------|-------------|------|----------------|
| `CH_BGer` | Bundesgericht / Tribunal fédéral | Arrêts non publiés | ~45,000 |
| `CH_BGE` | Bundesgerichtsentscheide | Arrêts publiés officiels | ~12,000 |
| `CH_BVGer` | Bundesverwaltungsgericht / TAF | Tribunal administratif fédéral | ~30,000 |
| `CH_BStGer` | Bundesstrafgericht / TPF | Tribunal pénal fédéral | ~8,000 |
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
| St. Gallen | `CH_SG_Kantonsgericht` | Kantonsgericht SG | ~3,500 |
| Luzern | `CH_LU_Kantonsgericht` | Kantonsgericht LU | ~3,000 |
| Tessin | `CH_TI_Tribunale` | Tribunale d'appello TI | ~2,500 |

**Total**: 26 cantons + 4 juridictions fédérales indexés.

---

## Hiérarchie des Sources

| Priorité | Source | Autorité | Usage |
|----------|--------|----------|-------|
| **1** | BGE (publiés) | Maximale | Jurisprudence de principe |
| **2** | BGer (non publiés) | Haute | Jurisprudence d'application |
| **3** | TAF/TPF | Fédérale spécialisée | Domaines spécifiques |
| **4** | Cantonaux | Locale | Applications régionales |

---

## API MCP Entscheidsuche

### Tool: search_case_law

**Description**: Recherche dans la base de jurisprudence

**Paramètres**:
```json
{
  "query": "string (required) - Requête de recherche",
  "size": "number (optional, default: 10, max: 50)",
  "from": "number (optional, default: 0) - Pagination"
}
```

**Retour**:
```json
{
  "signature": "Identifiant unique",
  "court": "Code tribunal (spider)",
  "language": "de/fr/it",
  "date": "YYYY-MM-DD",
  "case_number": "Numéro de référence",
  "title_de": "Titre allemand",
  "title_fr": "Titre français",
  "title_it": "Titre italien",
  "abstract_de": "Résumé allemand",
  "abstract_fr": "Résumé français",
  "abstract_it": "Résumé italien",
  "has_html": "boolean",
  "document_url": "URL du document",
  "scrapedate": "Date d'indexation"
}
```

---

### Tool: get_document

**Description**: Récupère le contenu complet d'une décision

**Paramètres**:
```json
{
  "signature": "string (required)",
  "spider": "string (optional) - extrait de signature si absent",
  "format": "enum: 'json' | 'html' | 'pdf' (default: 'json')"
}
```

**Formats**:
- **json**: Métadonnées structurées + contenu textuel
- **html**: Version HTML complète
- **pdf**: Document PDF original (si disponible)

---

### Tool: list_courts

**Description**: Liste tous les tribunaux disponibles

**Paramètres**: Aucun

**Retour**:
```json
{
  "name": "Nom du tribunal",
  "total_documents": "Nombre de documents",
  "new_documents": "Nouveaux documents",
  "last_run": "Dernière mise à jour",
  "status": "État du scraper"
}
```

---

## Syntaxe de Recherche Elasticsearch

### Opérateurs de Base

| Opérateur | Syntaxe | Exemple |
|-----------|---------|---------|
| ET | `AND` | `Datenschutz AND Arbeitsrecht` |
| OU | `OR` | `Kündigung OR licenciement` |
| NON | `NOT` ou `-` | `Datenschutz -Strafrecht` |
| Phrase | `"..."` | `"protection de la personnalité"` |

### Opérateurs Avancés

| Opérateur | Syntaxe | Exemple |
|-----------|---------|---------|
| Wildcard | `*` | `Kündig*` (Kündigung, Kündigungsschutz...) |
| Caractère unique | `?` | `199?` (1990-1999) |
| Obligatoire | `+` | `+licenciement` |
| Champ spécifique | `field:value` | `court:CH_BGer` |

### Exemples de Requêtes

```elasticsearch
# Recherche simple (AND implicite)
Datenschutz DSGVO

# Phrase exacte
"protection de la personnalité du travailleur"

# Opérateurs booléens
(Datenschutz OR "protection données") AND DSGVO

# Wildcard
Kündig*

# Exclusion
Datenschutz -Strafrecht

# Filtres
court:CH_BGer date:2023
```

---

## Abréviations Légales

### Codes Principaux

| Code DE | Code FR | Loi | Domaine |
|---------|---------|-----|---------|
| OR | CO | Code des Obligations | Contrats, travail, société |
| ZGB | CC | Code Civil | Personnes, famille, successions |
| StGB | CP | Code Pénal | Droit pénal |
| BV | Cst. | Constitution fédérale | Droits fondamentaux |
| ZPO | CPC | Code de procédure civile | Procédure civile |
| StPO | CPP | Code de procédure pénale | Procédure pénale |
| DSG | LPD | Loi protection des données | Privacy |
| BGG | LTF | Loi sur le Tribunal fédéral | Organisation judiciaire |
| VwVG | PA | Procédure administrative | Droit administratif |

---

## Glossaire Juridique Trilingue

### Termes Procéduraux

| DE | FR | IT | Signification |
|----|----|----|---------------|
| Beschwerde | Recours | Ricorso | Voie de recours |
| Urteil | Jugement/Arrêt | Sentenza | Décision finale |
| Verfügung | Décision | Decisione | Acte administratif |
| Erwägungen | Considérants | Considerandi | Raisonnement |
| Sachverhalt | État de fait | Fatti | Exposé des faits |
| Dispositiv | Dispositif | Dispositivo | Partie décisoire |

### Termes Substantiels

| DE | FR | IT | Domaine |
|----|----|----|---------|
| Kündigungsschutz | Protection contre licenciement | Protezione dal licenziamento | Travail |
| Persönlichkeitsschutz | Protection de la personnalité | Protezione della personalità | Civil |
| Treu und Glauben | Bonne foi | Buona fede | Général |
| Verhältnismässigkeit | Proportionnalité | Proporzionalità | Droit public |
| Rechtsmissbrauch | Abus de droit | Abuso di diritto | Général |
| Datenschutz | Protection des données | Protezione dei dati | Privacy |

---

## Ressources Externes

### Bases de Données Officielles

| Ressource | URL | Contenu |
|-----------|-----|---------|
| Entscheidsuche | https://entscheidsuche.ch | Agrégateur jurisprudence |
| Tribunal fédéral | https://www.bger.ch | Arrêts TF officiels |
| TAF | https://www.bvger.ch | Arrêts TAF |
| TPF | https://www.bstger.ch | Arrêts TPF |

### Outils Terminologiques

| Ressource | URL | Usage |
|-----------|-----|-------|
| Jurivoc | https://www.bger.ch/jurivoc | Thésaurus juridique TF |
| Termdat | https://www.termdat.ch | Terminologie Confédération |

---

## Documentation Technique

### Installation MCP Server

```bash
cd mcp-servers/entscheidsuche-mcp
npm install
npm run build
```

### Configuration

Voir `/mcp-servers/README.md` pour la configuration complète.

### Référence Outils

Voir `/MCP_TOOLS_REFERENCE.md` pour la documentation détaillée des tools.

---

## Skills Connexes

| Skill | Usage |
|-------|-------|
| `@swiss-legal-commentary` | Recherche doctrine (Onlinekommentar) |
| `@parse-decision` | Parsing de décisions TF/TAF |
| `@citation-formatter` | Formatage citations ATF, RS |
| `@recherche-juridique-suisse` | MOC navigation recherche juridique |

---

## Statistiques Base de Données

- **Total décisions**: > 1,000,000
- **Tribunaux indexés**: 30+
- **Langues**: DE (70%), FR (25%), IT (5%)
- **Période**: ~1954 - présent
- **Mise à jour**: Continue (scraping quotidien)

---

*Dernière mise à jour: Février 2026*
