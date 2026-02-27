# Research Persistence - Sauvegarde des recherches juridiques

Cette instruction définit les règles de persistance des résultats de recherche pour éviter la perte de données lors de la compaction du contexte.

**Priorité** : Cette instruction a priorité sur les workflows par défaut des skills de recherche.

**Dernière mise à jour** : Février 2026

---

## Règle Obligatoire

**Toute recherche MCP DOIT sauvegarder ses résultats sur disque IMMÉDIATEMENT après chaque appel.**

Cette règle s'applique à :
- `@swiss-case-law-research` (Entscheidsuche)
- `@swiss-legal-commentary` (Onlinekommentar)
- Toute autre skill utilisant des MCP de recherche

---

## Pourquoi ?

| Problème | Solution |
|----------|----------|
| Compaction efface les résultats en contexte | Résultats persistés sur disque |
| Question utilisateur alourdit le contexte | Résumer, pas tout garder |
| Recherche interrompue = perdue | Reprise possible via fichiers |
| Pas de trace pour référence future | Historique complet conservé |

---

## Structure de Dossier

```
./LOGS/recherche/YYYY-MM-DD_HHhMM_[sujet-court]/
├── recherche.json         # Métadonnées machine
├── resultats.md           # Résultats bruts formatés (lisible)
├── selection.md           # Résultats filtrés/pertinents
├── documents/             # Documents complets récupérés
│   ├── [signature1].json
│   └── [signature2].json
└── synthese.md            # Analyse finale (si complétée)
```

### Fichiers détaillés

#### recherche.json
```json
{
  "id": "uuid-v4",
  "created": "2026-02-27T14:30:00Z",
  "subject": "Protection de la personnalité au travail",
  "source": "entscheidsuche",
  "queries": [
    {
      "timestamp": "2026-02-27T14:30:05Z",
      "query": "Persönlichkeitsschutz Arbeitsrecht",
      "params": {"size": 20},
      "total_hits": 134,
      "saved_count": 20
    }
  ],
  "selected_documents": ["CH_BGer_xxx", "CH_BGer_yyy"],
  "status": "in_progress"
}
```

#### resultats.md
```markdown
# Résultats de recherche - [Sujet]

## Requête 1 : "[query]"
**Timestamp** : [date]
**Total** : [N] résultats

### Résultat 1
- **Signature** : [signature]
- **Date** : [date]
- **Tribunal** : [tribunal]
- **Résumé** : [abstract]

### Résultat 2
...
```

---

## Workflow Obligatoire

### Phase 0 : Initialisation (AVANT toute recherche)

**CRITIQUE** : Cette phase DOIT être exécutée avant le premier appel MCP.

1. **Déterminer le sujet court** (max 30 caractères, sans espaces)
   - Exemple : `protection-personnalite-travail`

2. **Créer le dossier de recherche**
   ```bash
   mkdir -p ./LOGS/recherche/YYYY-MM-DD_HHhMM_[sujet-court]
   mkdir -p ./LOGS/recherche/YYYY-MM-DD_HHhMM_[sujet-court]/documents
   ```

3. **Créer recherche.json avec métadonnées initiales**

4. **Créer resultats.md avec en-tête**

5. **Informer l'utilisateur**
   > "Recherche initialisée. Résultats sauvegardés dans `./LOGS/recherche/[path]/`"

---

### Après CHAQUE appel MCP

**IMMÉDIATEMENT après réception des résultats** :

1. **Sauvegarder dans resultats.md** (append)
   - Formater les résultats lisiblement
   - Inclure : signature, date, tribunal, résumé

2. **Mettre à jour recherche.json**
   - Ajouter la requête à `queries[]`
   - Mettre à jour `total_hits`

3. **Résumer dans le contexte**
   - Ne PAS garder tous les résultats en contexte
   - Garder uniquement : nombre de résultats, top 5, observations clés
   - Référencer le fichier : "Voir détails dans ./LOGS/recherche/[path]/resultats.md"

---

### Avant question utilisateur

Avant de poser une question à l'utilisateur :

1. **Vérifier** que les résultats sont sauvegardés
2. **Résumer** les résultats actuels
3. **Référencer** le fichier dans la question si pertinent

---

### Lors de la sélection de documents

Quand l'utilisateur sélectionne des documents à analyser :

1. **Récupérer le document complet** via MCP
2. **Sauvegarder dans documents/** avec le nom de signature
3. **Mettre à jour** `selected_documents` dans recherche.json
4. **Créer/mettre à jour selection.md** avec les documents retenus

---

### Après compaction

Si le contexte est compacté pendant une recherche :

1. **Identifier la dernière recherche active**
   ```bash
   ls -t ./LOGS/recherche/ | head -1
   ```

2. **Lire recherche.json** pour récupérer le contexte

3. **Lire resultats.md** pour avoir les résultats

4. **Informer l'utilisateur**
   > "Session compactée. J'ai récupéré le contexte de la recherche '[sujet]' depuis ./LOGS/recherche/[path]/"

5. **Continuer** la recherche sans perte de données

---

## Bonnes Pratiques

### À FAIRE

- Créer le dossier AVANT le premier appel MCP
- Sauvegarder IMMÉDIATEMENT après chaque appel
- Résumer au lieu de tout garder en contexte
- Référencer les fichiers dans les réponses
- Marquer le status "completed" quand terminé

### À ÉVITER

- Garder tous les résultats bruts en contexte
- Attendre la fin pour sauvegarder
- Oublier de créer la structure initiale
- Ignorer les fichiers après compaction

---

## Exemple de Workflow Complet

```
User: "Cherche la jurisprudence sur la protection de la personnalité au travail"

Agent:
1. [Phase 0] Crée ./LOGS/recherche/2026-02-27_1430_protection-personnalite/
2. [Phase 0] Crée recherche.json et resultats.md
3. [Phase 0] Informe : "Recherche initialisée..."

4. [Phase 1] Appel MCP search_case_law("Persönlichkeitsschutz Arbeitsrecht")
5. [SAUVEGARDE] Écrit 134 résultats dans resultats.md
6. [SAUVEGARDE] Met à jour recherche.json

7. [Résumé au user] "J'ai trouvé 134 décisions. Voici les 5 plus pertinentes..."
   (Résultats complets dans ./LOGS/recherche/.../resultats.md)

8. [Question] "Voulez-vous que j'affine par période ou tribunal ?"

--- [Compaction survient ici] ---

Agent (après compaction):
1. Lit ./LOGS/recherche/2026-02-27_1430_protection-personnalite/recherche.json
2. Informe : "Contexte récupéré. Vous aviez 134 résultats..."
3. Continue sans perte
```

---

## Nettoyage

**Politique de rétention** : 30 jours

```bash
# Nettoyage manuel des recherches > 30 jours
find ./LOGS/recherche/ -type d -mtime +30 -exec rm -rf {} +
```

Les fichiers de recherche ne sont **pas committés** (voir `./LOGS/.gitignore`).

---

## Skills Concernées

Cette instruction DOIT être appliquée par :

| Skill | MCP |
|-------|-----|
| `@swiss-case-law-research` | entscheidsuche |
| `@swiss-legal-commentary` | onlinekommentar |

---

## Références

- Memory Management : `.opencode/instructions/09-memory-management.md` (ai-toolkit)
- Automation Hooks : `.opencode/instructions/08-automation-hooks.md` (ai-toolkit)

---

*Version 1.0 — Février 2026*
