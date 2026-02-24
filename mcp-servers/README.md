# MCP Servers Configuration - Legal Assistant

Ce projet utilise deux serveurs MCP (Model Context Protocol) spécialisés pour la recherche juridique suisse.

## Serveurs installés

### 1. Entscheidsuche MCP Server

**Source**: https://github.com/self-tech-labs/entscheidsuche-MCP-server

**Description**: Permet de rechercher et accéder à la jurisprudence suisse (décisions de tribunaux fédéraux et cantonaux).

**Outils disponibles**:
- `search_case_law`: Rechercher des décisions de justice avec des requêtes en langage naturel
- `get_document`: Récupérer le contenu complet d'un document (JSON, HTML, ou PDF)
- `list_courts`: Obtenir des informations sur les tribunaux disponibles

**Exemples d'utilisation**:
```
- "Cherche des décisions sur le droit du travail et les licenciements"
- "Trouve des arrêts récents sur la protection des données"
- "Recherche jurisprudence suisse sur les contrats de bail"
```

**API utilisées**:
- `https://entscheidsuche.ch/_search.php` - Recherche Elasticsearch
- `https://entscheidsuche.ch/docs/` - Repository de documents
- `https://entscheidsuche.ch/status` - Informations sur les tribunaux

### 2. Onlinekommentar MCP Server

**Source**: https://github.com/self-tech-labs/onlinekommentar-mcp

**Description**: Accès aux commentaires juridiques suisses depuis onlinekommentar.ch.

**Outils disponibles**:
- `search_commentaries`: Recherche de commentaires juridiques avec filtres avancés
- `get_commentary`: Récupération d'un commentaire spécifique par ID

**Langues supportées**: Anglais, Allemand, Français, Italien

**Exemples d'utilisation**:
```
- "Cherche des commentaires sur les droits constitutionnels en français"
- "Trouve des commentaires juridiques sur la propriété intellectuelle"
- "Recherche commentaires sur le droit pénal suisse"
```

**API utilisée**:
- Base URL: `https://onlinekommentar.ch/api`
- `/commentaries` - Recherche de commentaires
- `/commentaries/{id}` - Commentaire spécifique

## Configuration

Les serveurs MCP sont configurés dans `.opencode/mcp.json` et sont automatiquement disponibles dans votre workspace OpenWork.

## Mise à jour des serveurs

Pour mettre à jour les serveurs MCP :

```bash
# Entscheidsuche
cd mcp-servers/entscheidsuche-mcp
git pull
npm install
npm run build

# Onlinekommentar
cd ../onlinekommentar-mcp
git pull
npm install
npm run build
```

## Dépannage

### Les serveurs n'apparaissent pas

1. Vérifiez que les serveurs sont bien compilés :
   ```bash
   ls -la mcp-servers/*/build/index.js
   ```

2. Vérifiez la configuration dans `.opencode/mcp.json`

3. Redémarrez votre session OpenWork

### Erreurs de connexion API

- Vérifiez votre connexion internet
- Testez manuellement les API :
  ```bash
  curl "https://entscheidsuche.ch/status"
  curl "https://onlinekommentar.ch/api/commentaries?search=test"
  ```

## Note légale

Ces outils fournissent un accès à des informations juridiques publiques à des fins de recherche uniquement. Consultez toujours des professionnels juridiques qualifiés pour des conseils juridiques.

## Contributeurs

- Serveurs MCP développés par [self-tech-labs](https://github.com/self-tech-labs)
- Intégration dans legal-assistant par votre équipe
