# 🚀 Quick Start - Legal Assistant

Ce guide vous permet de démarrer rapidement avec votre assistant juridique suisse.

## ✅ Vérification de l'Installation

```bash
# Vérifier que les serveurs MCP sont prêts
./manage-mcp.sh status
```

Vous devriez voir :
```
✓ entscheidsuche-mcp : Prêt (compilé)
✓ onlinekommentar-mcp : Prêt (compilé)
```

## 🎯 Premiers Pas

### 1. Ouvrez votre Workspace OpenWork

Les serveurs MCP sont automatiquement chargés depuis `.opencode/mcp.json`.

### 2. Essayez vos premières recherches

#### Recherche de Jurisprudence

```
🗣️ : "Cherche des décisions récentes sur la protection des données"
```

L'assistant utilisera le serveur **entscheidsuche-mcp** pour :
- Rechercher dans la base de données de jurisprudence suisse
- Trouver les décisions pertinentes des tribunaux fédéraux et cantonaux
- Vous présenter les résultats avec liens vers les documents complets

#### Recherche de Commentaires

```
🗣️ : "Trouve des commentaires juridiques sur le droit du travail en français"
```

L'assistant utilisera le serveur **onlinekommentar-mcp** pour :
- Rechercher dans la base de commentaires juridiques
- Filtrer par langue (français)
- Vous présenter les commentaires pertinents avec leurs détails

### 3. Exemples de Questions Avancées

#### Recherche Combinée
```
🗣️ : "Cherche des décisions et des commentaires sur l'Article 328 CO concernant la protection de la personnalité du travailleur"
```

#### Recherche Multilingue
```
🗣️ : "Find German commentaries about Datenschutz and Swiss privacy law"
```

#### Analyse de Cas Spécifique
```
🗣️ : "Trouve toutes les décisions du Tribunal fédéral suisse (BGer) de 2023 concernant les licenciements abusifs"
```

## 📋 Commandes Utiles

### Gestion des Serveurs MCP

```bash
# Vérifier l'état
./manage-mcp.sh status

# Mettre à jour tous les serveurs depuis GitHub
./manage-mcp.sh update-all

# Réinstaller un serveur spécifique
./manage-mcp.sh install entscheidsuche-mcp

# Tester un serveur
./manage-mcp.sh test onlinekommentar-mcp
```

## 🔍 Types de Recherches Possibles

### Entscheidsuche (Jurisprudence)

| Type de Recherche | Exemple |
|-------------------|---------|
| **Par sujet** | "Datenschutz", "Kündigungsschutz", "Mietrecht" |
| **Par tribunal** | "Décisions du BGer", "Arrêts du Tribunal cantonal de Genève" |
| **Par date** | "Décisions récentes 2023-2024" |
| **Phrase exacte** | `"protection de la personnalité"` |
| **Champs spécifiques** | `court:BGer date:2023` |

### Onlinekommentar (Commentaires)

| Type de Recherche | Exemple |
|-------------------|---------|
| **Par sujet** | "droits constitutionnels", "propriété intellectuelle" |
| **Par langue** | "commentaires en français", "deutsche Kommentare" |
| **Par acte législatif** | "Commentaires sur le Code des Obligations" |
| **Par auteur** | "Commentaires de [nom auteur]" |

## 💡 Astuces

### 1. Soyez Précis
```
❌ "droit du travail"
✅ "décisions sur le licenciement immédiat pour motif grave selon art. 337 CO"
```

### 2. Utilisez les Langues
```
✅ "Cherche des commentaires en français sur la protection des données"
✅ "Finde deutsche Entscheidungen über Datenschutz"
✅ "Find English commentaries about Swiss contract law"
```

### 3. Combinez les Sources
```
✅ "Cherche d'abord la jurisprudence sur l'article 328 CO, puis trouve les commentaires correspondants"
```

### 4. Demandez des Formats Spécifiques
```
✅ "Récupère le document complet en PDF"
✅ "Montre-moi le contenu HTML de cette décision"
```

## 🆘 Problèmes Courants

### "Les serveurs MCP ne répondent pas"

1. Vérifiez l'état : `./manage-mcp.sh status`
2. Redémarrez OpenWork
3. Vérifiez votre connexion internet

### "Aucun résultat trouvé"

- Essayez des termes plus généraux
- Vérifiez l'orthographe
- Essayez dans une autre langue
- Utilisez des synonymes juridiques

### "Erreur de compilation"

```bash
# Réinstallez le serveur problématique
./manage-mcp.sh install entscheidsuche-mcp
./manage-mcp.sh install onlinekommentar-mcp
```

## 📚 Ressources Supplémentaires

- **[Documentation Complète](./README.md)** - Guide complet du projet
- **[Guide des Serveurs MCP](./mcp-servers/README.md)** - Détails techniques
- **[Entscheidsuche.ch](https://entscheidsuche.ch)** - Site officiel
- **[Onlinekommentar.ch](https://onlinekommentar.ch)** - Site officiel

## 🎓 Exemples Pratiques

### Cas d'Usage 1 : Recherche de Précédent

```
🗣️ : "Je travaille sur un cas de licenciement d'une employée enceinte. 
Peux-tu me trouver des décisions du Tribunal fédéral sur ce sujet?"
```

### Cas d'Usage 2 : Analyse Article de Loi

```
🗣️ : "Explique-moi l'article 62 du Code des Obligations avec 
des commentaires doctrinaux et de la jurisprudence récente"
```

### Cas d'Usage 3 : Veille Juridique

```
🗣️ : "Quelles sont les décisions importantes de 2024 
en droit de la protection des données en Suisse?"
```

---

**Prêt à commencer ?** Posez votre première question juridique ! 🎯
