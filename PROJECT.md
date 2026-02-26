# Legal-Assistant

> Framework modulaire open-source pour assister les avocats suisses via Skills, Agents et MCP.

**Version**: 0.1.0 (Conception)  
**Dernière mise à jour**: Février 2026

---

## 1. Vision et Objectifs

### 1.1 Vision

Développer un framework modulaire capable d'assister ou remplacer **80% des tâches répétitives** d'un avocat suisse (litige civil/admin/pénal, conseil), en respectant :
- La déontologie et le secret professionnel
- Le multilinguisme suisse (FR/DE/IT)
- La primauté de la jurisprudence ATF sur la loi (art. 1 CC)

### 1.2 Objectifs

| Objectif | Mesure de succès |
|----------|------------------|
| Couverture métier | 90% des tâches courantes via 300+ skills atomiques |
| Gain de temps | -70% sur les tâches de recherche et rédaction |
| Coût maîtrisé | < 0.5 CHF/cas en tokens |
| Précision ATF | 95% de citations correctes |

### 1.3 Public cible

- Avocats indépendants et études d'avocats suisses
- Juristes d'entreprise
- Services juridiques cantonaux/fédéraux

---

## 2. Architecture conceptuelle

### 2.1 Hiérarchie des composants

```
┌─────────────────────────────────────────────────────────────┐
│                      INSTRUCTIONS                            │
│  (Style, ton, déontologie, multilinguisme, structure IRAC)  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     META-SKILLS                              │
│     (Intervieweur Juriste, Skill Creator, Decomposer)       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                        AGENTS                                │
│  (Rechercheur Juris, Synthétiseur, Rédacteur, Risk Spotter) │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                        SKILLS                                │
│           (Blocs atomiques : 1 tâche = 1 skill)             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                          MCP                                 │
│    (Connecteurs API : Entscheidsuche, Onlinekommentar)      │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Définitions

| Composant | Définition | Exemple |
|-----------|------------|---------|
| **Instructions** | Prompt système global définissant le style, la déontologie et les règles de raisonnement | "Raisonner comme avocat suisse : structure IRAC-CH, primauté ATF, citations RS précises" |
| **Skills** | Blocs atomiques réutilisables produisant un résultat concret (intermédiaire ou final) | Extraire ratio decidendi ATF, Générer table des matières, Rédiger allégués |
| **MCP** | Connecteurs standardisés vers APIs/bases complexes | Entscheidsuche (jurisprudence), Onlinekommentar (doctrine) |
| **Agents** | Instances spécialisées avec modèle/créativité paramétrables, exécutables en parallèle | Agent Rechercheur (Sonnet, créativité basse), Agent Plaidoirie (Opus, créativité haute) |
| **Meta-Skills** | Skills orchestrant d'autres skills de manière récursive | Intervieweur Juriste, Skill Creator |

---

## 3. Théories de planification

Le framework s'appuie sur des théories éprouvées pour structurer l'atomisation :

### 3.1 Problem Decomposition

Briser les problèmes complexes en sous-problèmes gérables et indépendants.

```
Recours TF (complexe)
    ├── En-tête + parties (atomique)
    ├── Exposé des faits (décomposable)
    │       ├── Allégués chronologiques
    │       └── Preuves référencées
    ├── Motivation juridique (décomposable)
    │       ├── Recherche jurisprudence
    │       ├── Analyse primauté
    │       └── Subsumption
    └── Conclusions (atomique)
```

### 3.2 Work Breakdown Structure (WBS)

Hiérarchie top-down/bottom-up des livrables vers les tâches.

| Niveau | Exemple |
|--------|---------|
| 1 - Livrable | Recours en matière civile au TF |
| 2 - Partie | Motivation juridique |
| 3 - Étape | Recherche jurisprudence similaire |
| 4 - Sous-étape | Requête MCP Entscheidsuche |

### 3.3 Lean Management

- **Value mapping** : Prioriser les skills à haute valeur ajoutée
- **Éliminer le waste** : Pas de skills redondantes, MCP calls minimales
- **Kaizen** : Itérations continues pour raffiner les skills

### 3.4 Divide & Conquer

Division récursive jusqu'à obtenir des skills indépendantes et parallélisables.

---

## 4. Catégories de Skills

### 4.1 Vue d'ensemble

| Catégorie | % estimé | Exemples |
|-----------|----------|----------|
| **Recherche** | 30% | Jurisprudence (MCP), doctrine, médicale, factuelle |
| **Analyse** | 25% | Primauté ATF, détection incohérences, risk spotting |
| **Rédaction** | 20% | Stricte (conclusions, TOC) vs créative (plaidoirie) |
| **Production** | 15% | Génération .docx, formatage, styles suisses |
| **Autres** | 10% | Daily digest, veille juridique, traduction |

### 4.2 Skills de Recherche

| Skill | Outil/MCP | Input | Output |
|-------|-----------|-------|--------|
| Recherche jurisprudence TF | Entscheidsuche MCP | Mots-clés, filtres | Liste ATF pertinents |
| Recherche doctrine | Onlinekommentar MCP | Article de loi | Commentaires liés |
| Recherche médicale | Web search / PubMed | Termes médicaux | Synthèse expertise |
| Recherche factuelle | Web search | Question | Sources vérifiées |

### 4.3 Skills d'Analyse

| Skill | Description | Garde-fous |
|-------|-------------|------------|
| Extraire ratio decidendi | Identifier le principe juridique d'un ATF | Vérif. date < 1 an |
| Analyse primauté | ATF vs loi cantonale/fédérale | Hiérarchie art. 1 CC |
| Détection antinomies | Incohérences entre sources | Signaler conflits |
| Risk spotting | Identifier risques LPD, CO, déontologie | Checklist compliance |

### 4.4 Skills de Rédaction

| Skill | Type | Créativité |
|-------|------|------------|
| Rédiger en-tête | Strict | Basse |
| Générer conclusions | Strict | Basse |
| Rédiger allégués factuels | Semi-strict | Moyenne |
| Rédiger motivation juridique | Créatif | Moyenne |
| Rédiger plaidoirie | Créatif | Haute |

### 4.5 Skills de Production

| Skill | Outil | Output |
|-------|-------|--------|
| Générer .docx | python-docx | Document Word formaté |
| Appliquer styles suisses | Templates | Document avec styles |
| Générer table des matières | Word automation | TOC dynamique |
| Inventaire pièces | Template | Tableau numéroté |

### 4.6 Skills Quotidiennes

| Skill | Fréquence | Description |
|-------|-----------|-------------|
| Daily ATF Digest | Quotidien | Top 5-10 ATF récents + résumé + impact |
| Veille législative | Hebdomadaire | Nouvelles lois/ordonnances |
| Alertes domaine | Configurable | Nouveautés par domaine (travail, bail, etc.) |

---

## 5. Livrables et décomposition

### 5.1 Livrables prioritaires

| Livrable | Fréquence | Complexité | Priorité |
|----------|-----------|------------|----------|
| Recours en matière civile TF | Haute | Haute | 1 |
| Avis de droit | Haute | Haute | 2 |
| Mémoire de réponse/réplique | Haute | Moyenne | 3 |
| Conclusions principales/subsidiaires | Haute | Moyenne | 4 |
| Procuration / plein-pouvoir | Haute | Basse | 5 |
| Demande d'effet suspensif | Moyenne | Moyenne | 6 |
| Mail/courrier client | Très haute | Basse | 7 |
| Contrat de mandat | Moyenne | Moyenne | 8 |
| Plaidoirie (script) | Moyenne | Haute | 9 |
| Liste des pièces | Haute | Basse | 10 |

### 5.2 Exemple de décomposition : Recours TF (art. 72 ss LTF)

| Partie | Atomicité | Type de skill | Output attendu |
|--------|-----------|---------------|----------------|
| En-tête + parties | Très haute | Format en-tête suisse | Bloc Word avec RS, dates, signatures |
| Exposé des faits | Moyenne | Rédaction allégués factuels | Paragraphes numérotés chronologiques |
| Liste des conclusions | Haute | Conclusions principales/sub | Numérotées, claires, subsidiaires |
| Sommaire / table matières | Très haute | Génération TOC automatique | Word TOC stylé |
| Motivation juridique | Basse | Recherche + subsumption | Considérants structurés + ATF cités |
| Liste des pièces jointes | Haute | Inventaire pièces | Tableau numéroté + descriptions |
| Signature / date | Très haute | Fermeture document | Bloc final + formules usuelles |

### 5.3 Workflow upstream : Motivation juridique

```
1. Identifier questions juridiques clés
       │
       ▼
2. Recherche doctrine (Onlinekommentar MCP)
       │
       ▼
3. Recherche jurisprudence (Entscheidsuche MCP)
       │
       ▼
4. Analyse primauté ATF vs loi
       │
       ▼
5. Subsumption faits → droit
       │
       ▼
6. Rédaction argumentative (style suisse)
       │
       ▼
7. Vérification cohérence / risques nova (art. 99 LTF)
```

---

## 6. Agents

### 6.1 Architecture des agents

| Agent | Modèle suggéré | Créativité | Rôle |
|-------|----------------|------------|------|
| Rechercheur Juris | Sonnet | Basse | Requêtes MCP, collecte sources |
| Rechercheur Médical | Sonnet | Moyenne | Analyse expertises médicales |
| Synthétiseur | Sonnet | Moyenne | Consolide outputs recherche |
| Rédacteur Strict | Haiku | Basse | Formatage, TOC, conclusions |
| Rédacteur Créatif | Opus | Haute | Plaidoirie, argumentation |
| Risk Spotter | Sonnet | Basse | Scan LPD, CO, déontologie, nova |
| Chef d'orchestre | Opus | Moyenne | Décide séquence, consolide |

### 6.2 Orchestration parallèle

```
                    ┌─────────────────┐
                    │ Chef d'orchestre │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ Rechercheur     │ │ Rechercheur     │ │ Risk Spotter    │
│ Juris (MCP)     │ │ Médical         │ │                 │
└────────┬────────┘ └────────┬────────┘ └────────┬────────┘
         │                   │                   │
         └───────────────────┼───────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Synthétiseur  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Rédacteur    │
                    └─────────────────┘
```

---

## 7. Intégration MCP

### 7.1 Serveurs MCP disponibles

| Serveur | Source | Fonction |
|---------|--------|----------|
| **Entscheidsuche** | mcpmarket.com/server/entscheidsuche | Jurisprudence TF + cantonale |
| **Onlinekommentar** | mcpmarket.com/server/onlinekommentar | Doctrine suisse multilingue |

### 7.2 Utilisation dans les skills

```yaml
# Exemple de skill avec MCP
name: Recherche ATF similaires
mcp_server: entscheidsuche
input:
  - keywords: string[]
  - date_from: date
  - jurisdiction: enum[TF, cantonal]
output:
  - atf_list: ATF[]
  - relevance_score: float
```

---

## 8. Intégration Obsidian

### 8.1 Structure du Vault

```
legal-assistant/
├── skills/
│   ├── recherche/
│   │   ├── Skill_RechercheATF.md
│   │   ├── Skill_RechercheDoctrine.md
│   │   └── ...
│   ├── analyse/
│   ├── redaction/
│   └── production/
├── mocs/
│   ├── MOC_Recherche.md
│   ├── MOC_Civil.md
│   ├── MOC_Admin.md
│   └── MOC_Decomposition.md
├── exemples/
│   ├── Exemple_ATF148.md
│   └── ...
├── agents/
│   ├── Agent_Rechercheur.md
│   └── ...
└── instructions/
    └── Instructions_Base.md
```

### 8.2 Template Skill Markdown

```markdown
---
name: Extraire Ratio Decidendi ATF
atomicite: haute
theorie: problem_decomposition
coverage: [recours TF, avis droit]
depends_on: [[Skill_RechercheATF]]
mcp: entscheidsuche
lean_waste: none
---

# Extraire Ratio Decidendi ATF

## Description
Input : ATF ID → Output : JSON ratio decidendi

## Outils
- MCP : [[Entscheidsuche MCP]]

## Exemples
- [[Exemple_ATF148.md]]
  - Input: "ATF 148 III 123"
  - Output: `{ratio: "Primauté contrat (art. 1 CO)", citations: ["cons. 4.2"]}`

## Garde-fous
- Vérifier date < 1 an pour actualité
- Confirmer juridiction (TF vs cantonal)

## Liens
- [[MOC_Recherche]]
- [[MOC_Analyse]]
```

### 8.3 MOC (Map of Content)

```markdown
# MOC Recherche Juridique

## Skills
- [[Skill_RechercheATF]] - Jurisprudence TF via MCP
- [[Skill_RechercheDoctrine]] - Doctrine via Onlinekommentar
- [[Skill_RechercheMedicale]] - Expertises médicales

## Coverage
- Litige : 80%
- Conseil : 70%
- Gaps : Pénal (à développer)

## Atomic Map
![[graph_recherche.png]]
```

---

## 9. Meta-Skills

### 9.1 Intervieweur Juriste

**Objectif** : Questionner récursivement un avocat pour cartographier exhaustivement le métier.

**Méthode** :
1. Phase 1 : Livrables finaux
2. Phase 2 : Décomposition en parties
3. Phase 3 : Workflows upstream
4. Phase 4 : Sous-étapes atomiques

**Prompt système** :
```
Tu es un intervieweur spécialisé dans l'analyse de processus métier juridiques.
Pose des questions ouvertes, reformule les réponses, demande des exemples concrets.
Objectif : créer une cartographie exhaustive des skills nécessaires.
Utilise ask_user_question de manière récursive jusqu'à épuisement des branches.
```

### 9.2 Skill Creator

**Objectif** : Générer automatiquement des fichiers Markdown de skills.

**Contraintes appliquées** :
- Atomicité : < 3 étapes par skill
- Cohérence : Template YAML standard
- Coverage : Lien vers livrables concernés

### 9.3 Decomposer

**Objectif** : Appliquer les théories de planification (WBS, Lean, Divide & Conquer) sur un input.

---

## 10. Instructions de base

### 10.1 Prompt système global

```
Tu es un assistant juridique suisse expert. Tu respectes :

STYLE & TON
- Multilinguisme CH (fr/de/it selon contexte)
- Style formel mais direct
- Précision terminologique

RAISONNEMENT
- Structure IRAC-CH : Faits → Droit → Subsumption → Conclusion
- Primauté ATF sur loi (art. 1 CC)
- Citations RS précises (ex: art. 41 CO)
- Références ATF complètes (ex: ATF 148 III 123)

DÉONTOLOGIE
- Secret professionnel absolu
- Indépendance (règles FSA/Barreau)
- Signaler conflits d'intérêts potentiels

OUTPUT
- Format Markdown pour Obsidian
- Liens [[SkillName]] quand pertinent
- Frontmatter YAML pour metadata
```

### 10.2 Règles de primauté

1. ATF publié > ATF non publié
2. ATF récent > ATF ancien (sauf principe établi)
3. ATF > Loi fédérale > Loi cantonale
4. Doctrine majoritaire > Doctrine minoritaire

---

## 11. Roadmap

### Phase 1 : Setup & Cartographie (Mois 1)

- [ ] Créer structure Vault Obsidian
- [ ] Développer meta-skill Intervieweur
- [ ] Développer meta-skill Skill Creator
- [ ] Interroger 5 avocats pour 10 livrables prioritaires
- [ ] Générer 50 skills atomiques initiales
- [ ] Coverage cible : 40% civil/admin

### Phase 2 : Décomposition (Mois 2)

- [ ] Générer 150 skills via Skill Creator
- [ ] Créer 5 MOCs par domaine
- [ ] Intégrer exemples anonymisés
- [ ] Tests unitaires : 20 cas
- [ ] Intégrer MCP Entscheidsuche + Onlinekommentar

### Phase 3 : Agents & Orchestration (Mois 3)

- [ ] Créer 10-15 agents spécialisés
- [ ] Implémenter parallélisme
- [ ] Développer Daily ATF Digest
- [ ] Value stream mapping des workflows

### Phase 4-5 : Packaging (Mois 4-5)

- [ ] Export Claude Projects (zip)
- [ ] Repo GitHub avec Vault + scripts
- [ ] Documentation utilisateur
- [ ] Tests : 30 cas, mesure coverage
- [ ] Licence open-source (MIT)

### Phase 6 : Scaling (Mois 6)

- [ ] Beta-test avec 15 avocats (Zürich)
- [ ] Mesure KPIs (temps, coût, précision)
- [ ] Évolutions : nouveaux domaines (immobilier, travail)
- [ ] Coverage cible : 90%

---

## 12. KPIs et métriques

| Métrique | Cible | Méthode de mesure |
|----------|-------|-------------------|
| Coverage métier | 90% | Audit MOCs (skills vs livrables) |
| Précision ATF | 95% | Validation manuelle échantillon |
| Gain de temps | -70% | Benchmark avant/après |
| Coût tokens | < 0.5 CHF/cas | Monitoring API |
| Satisfaction utilisateur | > 4/5 | Feedback beta-testeurs |

---

## 13. Stack technique

| Composant | Technologie |
|-----------|-------------|
| IA principale | Claude (Opus, Sonnet, Haiku) |
| Orchestration | Claude Projects / OpenWork |
| Knowledge base | Obsidian Vault (Markdown) |
| MCP servers | Entscheidsuche, Onlinekommentar |
| Production docs | python-docx, templates Word |
| Versioning | Git / GitHub |
| CI/CD | GitHub Actions |

---

## 14. Risques et mitigations

| Risque | Impact | Mitigation |
|--------|--------|------------|
| Hallucinations ATF | Critique | Double-vérification via MCP, garde-fous |
| Violation secret pro | Critique | Données anonymisées, pas de cloud non-CH |
| Coûts tokens élevés | Moyen | Agents Haiku pour tâches simples |
| MCP indisponible | Moyen | Fallback manuel, cache local |
| Adoption faible | Moyen | UX simple, formation, quick wins |

---

## 15. Références

### Outils et services

- **Entscheidsuche** : [mcpmarket.com/server/entscheidsuche](https://mcpmarket.com/server/entscheidsuche)
- **Onlinekommentar** : [mcpmarket.com/server/onlinekommentar](https://mcpmarket.com/server/onlinekommentar)
- **Silex.legal** : Assistant IA juridique suisse (benchmark)
- **Lexplorer** : Recherche sémantique ATF

### Théories

- Problem Decomposition
- Work Breakdown Structure (WBS)
- Lean Management / Kaizen
- Divide & Conquer

### Droit suisse

- LTF (Loi sur le Tribunal fédéral)
- CC art. 1 (Primauté jurisprudence)
- CO (Code des obligations)
- Règles déontologiques FSA

---

*Document généré à partir du brainstorming GROK.md - Février 2026*
