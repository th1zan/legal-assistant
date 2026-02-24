# Legal Assistant - Swiss Law Research Tool

Un assistant juridique spécialisé pour la recherche dans le droit suisse, utilisant des serveurs MCP (Model Context Protocol) pour accéder à la jurisprudence et aux commentaires juridiques.

## 🎯 Fonctionnalités

### Recherche de Jurisprudence (Entscheidsuche)
- 🔍 Recherche dans les décisions des tribunaux fédéraux et cantonaux suisses
- 📄 Récupération de documents complets (JSON, HTML, PDF)
- 🏛️ Informations sur tous les tribunaux disponibles

### Commentaires Juridiques (Onlinekommentar)
- 📚 Accès aux commentaires juridiques suisses
- 🌍 Support multilingue (DE, FR, IT, EN)
- 🎯 Filtres avancés par acte législatif, date, etc.

## 🚀 Installation

### Prérequis
- Node.js (version 14+)
- npm ou yarn
- OpenWork (pour l'intégration MCP)

### Étapes d'installation

1. **Cloner le projet** (si ce n'est pas déjà fait)
   ```bash
   git clone <votre-repo>
   cd legal-assistant
   ```

2. **Les serveurs MCP sont déjà installés et configurés !**
   
   Vérifiez leur état :
   ```bash
   ./manage-mcp.sh status
   ```

3. **Redémarrez votre session OpenWork** pour activer les serveurs MCP

## 📖 Utilisation

### Recherche de Jurisprudence

Dans votre conversation avec l'assistant OpenWork, vous pouvez poser des questions comme :

```
- "Cherche des décisions sur le droit du travail et les licenciements"
- "Trouve des arrêts récents sur la protection des données"
- "Recherche jurisprudence suisse DSGVO"
- "Trouve des cas de droit locatif concernant les augmentations de loyer"
```

### Recherche de Commentaires

```
- "Cherche des commentaires sur les droits constitutionnels en français"
- "Trouve des commentaires juridiques sur la propriété intellectuelle"
- "Recherche commentaires sur le droit pénal suisse"
```

## 🛠️ Gestion des Serveurs MCP

Un script pratique `manage-mcp.sh` est fourni pour gérer les serveurs :

```bash
# Afficher l'état des serveurs
./manage-mcp.sh status

# Installer un serveur spécifique
./manage-mcp.sh install entscheidsuche-mcp

# Mettre à jour tous les serveurs
./manage-mcp.sh update-all

# Tester un serveur
./manage-mcp.sh test onlinekommentar-mcp

# Voir l'aide
./manage-mcp.sh help
```

## 📁 Structure du Projet

```
legal-assistant/
├── .opencode/
│   ├── mcp.json              # Configuration des serveurs MCP
│   ├── openwork.json         # Configuration du workspace
│   ├── agents/               # Agents personnalisés
│   └── skills/               # Compétences du workspace
├── mcp-servers/
│   ├── entscheidsuche-mcp/   # Serveur de jurisprudence
│   ├── onlinekommentar-mcp/  # Serveur de commentaires
│   └── README.md             # Documentation détaillée des serveurs
├── logs/                     # Logs de l'application
├── manage-mcp.sh             # Script de gestion des serveurs
└── README.md                 # Ce fichier
```

## 🔧 Configuration

### Configuration MCP

Les serveurs MCP sont configurés dans `.opencode/mcp.json`. Cette configuration est automatiquement chargée par OpenWork.

### Variables d'Environnement

Aucune variable d'environnement n'est nécessaire pour le moment. Les serveurs utilisent les API publiques d'Entscheidsuche et Onlinekommentar.

## 📚 Documentation Détaillée

- **[Documentation des serveurs MCP](./mcp-servers/README.md)** - Guide complet des serveurs
- **[Entscheidsuche API](https://entscheidsuche.ch)** - Documentation officielle
- **[Onlinekommentar API](https://onlinekommentar.ch)** - Documentation officielle

## 🐛 Dépannage

### Les serveurs MCP n'apparaissent pas

1. Vérifiez que les serveurs sont compilés :
   ```bash
   ./manage-mcp.sh status
   ```

2. Si nécessaire, recompilez :
   ```bash
   ./manage-mcp.sh install-all
   ```

3. Redémarrez OpenWork

### Erreurs de connexion aux API

Testez manuellement les API :
```bash
# Test Entscheidsuche
curl "https://entscheidsuche.ch/status"

# Test Onlinekommentar
curl "https://onlinekommentar.ch/api/commentaries?search=test"
```

### Problèmes de compilation

```bash
# Réinstallez les dépendances
cd mcp-servers/entscheidsuche-mcp
npm install
npm run build

cd ../onlinekommentar-mcp
npm install
npm run build
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalite`)
3. Committez vos changements (`git commit -am 'Ajout de ma fonctionnalité'`)
4. Push vers la branche (`git push origin feature/ma-fonctionnalite`)
5. Créez une Pull Request

## 📄 Licence

Ce projet est un outil de recherche juridique. Les serveurs MCP utilisés sont open source :
- [entscheidsuche-MCP-server](https://github.com/self-tech-labs/entscheidsuche-MCP-server) - MIT License
- [onlinekommentar-mcp](https://github.com/self-tech-labs/onlinekommentar-mcp) - Open Source

## ⚖️ Note Légale

Cet outil fournit un accès à des informations juridiques publiques à des fins de recherche uniquement. 

**Important** :
- Vérifiez toujours les informations via les sources officielles
- Cet outil est destiné à la recherche uniquement
- Consultez des professionnels juridiques qualifiés pour des conseils juridiques
- Respectez les conditions d'utilisation d'entscheidsuche.ch et onlinekommentar.ch

## 👥 Remerciements

- [self-tech-labs](https://github.com/self-tech-labs) pour le développement des serveurs MCP
- [Entscheidsuche.ch](https://entscheidsuche.ch) pour l'accès à la jurisprudence suisse
- [Onlinekommentar.ch](https://onlinekommentar.ch) pour les commentaires juridiques
- [Model Context Protocol](https://modelcontextprotocol.io) pour le framework MCP

## 📞 Support

Pour toute question ou problème :
- Consultez la [documentation détaillée](./mcp-servers/README.md)
- Ouvrez une issue sur GitHub
- Consultez la section dépannage ci-dessus

---

**Version**: 1.0.0  
**Dernière mise à jour**: Février 2026
