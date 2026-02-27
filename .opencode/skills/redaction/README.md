# Skills de Rédaction Juridique

> **Statut** : Dossier placeholder - Skills à créer

Ce dossier contiendra les skills de rédaction de documents juridiques suisses, basées sur des **exemples concrets fournis par l'utilisateur**.

---

## Types de Documents à Implémenter

### Priorité Haute (P1)

| Document | Créativité | Exemples requis |
|----------|------------|-----------------|
| **Recours TF** (art. 72 ss LTF) | Moyenne | Modèle de recours complet |
| **Avis de droit** | Moyenne-Haute | Consultation juridique type |
| **Mémoire de réponse/réplique** | Moyenne | Échange de mémoires |
| **Conclusions principales/subsidiaires** | Basse | Exemples de conclusions |
| **Procuration / plein-pouvoir** | Basse | Modèle standard |
| **Mail/courrier client** | Basse | Exemples de correspondance |
| **Liste des pièces** | Basse | Tableau type |

### Priorité Moyenne (P2)

| Document | Créativité | Exemples requis |
|----------|------------|-----------------|
| **Demande d'effet suspensif** | Moyenne | Requête type |
| **Contrat de mandat** | Basse-Moyenne | Modèles standards |
| **Plaidoirie (script)** | Haute | Script de plaidoirie |

### Priorité Basse (P3)

| Document | Créativité | Exemples requis |
|----------|------------|-----------------|
| **En-tête + parties** | Très basse | Format suisse standard |
| **Table des matières** | Très basse | TOC dynamique |
| **Signature / date** | Très basse | Bloc final standard |

---

## Structure Attendue

Chaque skill de rédaction suivra ce modèle :

```
redaction/
├── recours-tf/
│   ├── SKILL.md           # Workflow de rédaction (< 300 lignes)
│   ├── TEMPLATES.md       # Modèles de documents
│   ├── EXAMPLES.md        # Exemples annotés
│   └── CHECKLIST.md       # Vérifications obligatoires
├── avis-de-droit/
│   ├── SKILL.md
│   ├── TEMPLATES.md
│   └── EXAMPLES.md
├── memoire-reponse/
│   └── ...
└── README.md              # Ce fichier
```

---

## Comment Contribuer

### 1. Fournir des exemples

Pour créer une skill de rédaction, il faut des **exemples concrets** :

1. **Exemples de documents rédigés** (anonymisés)
2. **Structure attendue** (sections, ordre, formules)
3. **Variations** (selon juridiction, domaine, etc.)
4. **Erreurs courantes** à éviter

### 2. Format des exemples

```markdown
# Exemple : [Type de document]

## Métadonnées
- **Juridiction** : TF / Cantonal / 1ère instance
- **Domaine** : Civil / Pénal / Administratif
- **Langue** : FR / DE / IT

## Document complet
[Texte du document anonymisé]

## Annotations
- **Section 1** : [Explication du contenu attendu]
- **Section 2** : [...]
```

---

## Dépendances

Les skills de rédaction s'appuient sur :

| Skill | Rôle |
|-------|------|
| `@analyse/extract-facts` | Extraction des faits pour l'exposé |
| `@analyse/identify-legal-issues` | Identification des questions juridiques |
| `@analyse/analyse-cas-juridique` | Analyse complète pour la motivation |
| `@mcp/swiss-case-law-research` | Recherche de jurisprudence |
| `@mcp/swiss-legal-commentary` | Recherche de doctrine |
| `@recherche/citation-juridique-suisse` | Formatage des citations |
| `@production/docx` | Génération du document Word final |

---

## Références

- **PROJECT.md** : Section 4.4 (Skills de Rédaction) et Section 5.1 (Livrables prioritaires)
- **SKILLS_GUIDE.md** : Section structure des skills
- **@analyse/recours-tf** : Skill d'analyse existante (à distinguer de la skill de rédaction)

---

**Note** : Les skills de rédaction diffèrent des skills d'analyse. Par exemple :
- `@analyse/recours-tf` → Vérifie la recevabilité et structure les griefs
- `@redaction/recours-tf` → Génère le document Word final avec formatage suisse
