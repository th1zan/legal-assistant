# Roadmap Legal-Assistant

> Mini-roadmap structurée des tâches à réaliser pour le projet legal-assistant.

**Dernière mise à jour**: Février 2026

---

## Vue d'ensemble

```
Phase 1: Validation & Infrastructure (Semaine 1-2)
    ├── 1.1 Validation stratégique
    ├── 1.2 Vérification MCP
    └── 1.3 Réorganisation skills

Phase 2: Amélioration Skills Recherche (Semaine 3-4)
    ├── 2.1 Audit liens obsolètes
    ├── 2.2 Analyse Entscheidsuche
    ├── 2.3 Migration MCP + fallback
    └── 2.4 Skill META recherche

Phase 3: Skills Analyse & Rédaction (Semaine 5-6)
    ├── 3.1 Skill analyse de cas
    ├── 3.2 Skills rédaction documents
    └── 3.3 Templates livrables

Phase 4: Skills Médicales (Semaine 7)
    ├── 4.1 Skill recherche médicale
    └── 4.2 Skill analyse expertise médicale

Phase 5: Infrastructure Cas (Semaine 8)
    ├── 5.1 Structure dossiers cas
    ├── 5.2 Format Markdown + TOC
    └── 5.3 Export Obsidian/Word
```

---

## Phase 1: Validation & Infrastructure

### 1.1 Validation stratégique
**Objectif**: Confirmer l'alignement avec la vision du projet

- [ ] **1.1.1** Relire GROK.md et PROJECT.md
  - Vérifier cohérence entre brainstorming et document structuré
  - Identifier écarts ou éléments manquants
  
- [ ] **1.1.2** Valider les priorités
  - Confirmer les 10 livrables prioritaires
  - Ajuster si nécessaire selon retours avocat

- [ ] **1.1.3** Documenter les décisions
  - Créer `DECISIONS.md` pour tracer les choix stratégiques

### 1.2 Vérification connexion MCP
**Objectif**: S'assurer que les MCP sont fonctionnels et performants

- [ ] **1.2.1** Tester connexion Entscheidsuche
  - Exécuter requête test
  - Mesurer temps de réponse (cible: < 2s)
  - Documenter format réponse

- [ ] **1.2.2** Tester connexion Onlinekommentar
  - Exécuter requête test
  - Mesurer temps de réponse
  - Documenter format réponse

- [ ] **1.2.3** Créer script de test automatisé
  - Script `test-mcp-performance.sh`
  - Métriques: latence, disponibilité, format

- [ ] **1.2.4** Documenter résultats
  - Mettre à jour `MCP_TOOLS_REFERENCE.md`
  - Ajouter benchmarks de performance

### 1.3 Réorganisation des skills
**Objectif**: Classer les skills dans une structure claire

- [ ] **1.3.1** Créer structure de dossiers
  ```
  .opencode/skills/
  ├── mcp/              # Skills utilisant des serveurs MCP
  ├── recherche/        # Skills de recherche (web, doctrine, etc.)
  └── anthropic/        # Skills génériques Anthropic/Claude
  ```

- [ ] **1.3.2** Auditer skills existantes
  - Lister toutes les skills actuelles
  - Catégoriser chaque skill

- [ ] **1.3.3** Déplacer skills dans dossiers appropriés
  - Mettre à jour les chemins dans les références
  - Vérifier que les liens [[skill]] restent valides

- [ ] **1.3.4** Mettre à jour `SKILLS_GUIDE.md`
  - Refléter nouvelle organisation
  - Ajouter index par catégorie

---

## Phase 2: Amélioration Skills Recherche

### 2.1 Audit liens obsolètes
**Objectif**: Identifier et corriger les liens morts dans les skills de recherche

- [ ] **2.1.1** Lister toutes les URLs dans les skills recherche
  - Parser les fichiers SKILL.md
  - Extraire URLs référencées

- [ ] **2.1.2** Tester chaque URL
  - Script automatisé de vérification HTTP
  - Identifier codes 404, 301, timeouts

- [ ] **2.1.3** Corriger ou supprimer liens obsolètes
  - Rechercher alternatives pour liens morts
  - Documenter changements

- [ ] **2.1.4** Créer processus de vérification périodique
  - Script `check-links.sh` à exécuter mensuellement

### 2.2 Analyse contenu Entscheidsuche
**Objectif**: Comprendre l'étendue et les limites du MCP Entscheidsuche

- [ ] **2.2.1** Documenter couverture
  - Juridictions couvertes (TF, cantonaux, TAF, TPF)
  - Période temporelle disponible
  - Langues supportées

- [ ] **2.2.2** Tester requêtes types
  - Recherche par mots-clés
  - Recherche par article de loi
  - Recherche par numéro ATF
  - Filtres date/juridiction

- [ ] **2.2.3** Identifier limitations
  - Arrêts non couverts
  - Formats de sortie
  - Limites de requêtes

- [ ] **2.2.4** Documenter dans `docs/entscheidsuche-reference.md`

### 2.3 Migration MCP + fallback
**Objectif**: Remplacer les appels web par MCP quand possible, avec fallback

- [ ] **2.3.1** Pour chaque skill de recherche, analyser
  - Source actuelle (web scraping, API, manuel)
  - MCP équivalent disponible?
  - Avantages/inconvénients migration

- [ ] **2.3.2** Implémenter pattern MCP + fallback
  ```
  1. Essayer MCP (rapide, structuré)
  2. Si échec → fallback sur site web
  3. Si échec → signaler erreur avec contexte
  ```

- [ ] **2.3.3** Mettre à jour skills concernées
  - `jurisprudence-suisse` → MCP Entscheidsuche + fallback bger.ch
  - `sources-doctrinales` → MCP Onlinekommentar + fallback web

- [ ] **2.3.4** Tester les deux chemins (MCP et fallback)

### 2.4 Skill META recherche juridique
**Objectif**: Créer une skill orchestratrice de recherche

- [ ] **2.4.1** Définir le workflow de recherche complet
  ```
  1. Analyser la question juridique
  2. Identifier domaines pertinents (civil, admin, pénal, etc.)
  3. Lancer recherches parallèles:
     - Jurisprudence TF (MCP Entscheidsuche)
     - Jurisprudence cantonale
     - Doctrine (MCP Onlinekommentar)
     - Législation (RS/RO)
  4. Consolider résultats
  5. Formater avec références juridiques suisses
  6. Inclure URLs originales
  ```

- [ ] **2.4.2** Créer skill `recherche-juridique-meta`
  - Fichier `SKILL.md` avec workflow
  - Références vers sub-skills
  - Exemples d'utilisation

- [ ] **2.4.3** Intégrer skill `citation-juridique-suisse`
  - Format ATF correct (ATF 148 III 123)
  - Format RS correct (art. 41 CO; RS 220)
  - Liens Fedlex/bger.ch

- [ ] **2.4.4** Ajouter URLs sources originales
  - Lien vers arrêt complet sur bger.ch
  - Lien vers article sur Fedlex
  - Lien vers commentaire source

- [ ] **2.4.5** Tester sur 5 cas types
  - Question droit civil
  - Question droit admin
  - Question droit pénal
  - Question multilingue
  - Question avec jurisprudence cantonale

---

## Phase 3: Skills Analyse & Rédaction

### 3.1 Skill analyse de cas
**Objectif**: Permettre le découpage structuré d'un cas juridique

- [ ] **3.1.1** Définir structure d'analyse
  ```
  Cas juridique
  ├── Parties (demandeur, défendeur, etc.)
  ├── Faits
  │   ├── Chronologie
  │   └── Faits contestés vs non-contestés
  ├── Procédure
  │   ├── Historique procédural
  │   └── Instance actuelle
  ├── Questions juridiques
  │   ├── Question principale
  │   └── Questions subsidiaires
  ├── Considérants (si décision existante)
  │   ├── En fait
  │   └── En droit
  └── Prétentions/Conclusions
  ```

- [ ] **3.1.2** Créer skill `analyse-cas-juridique`
  - Input: documents du cas (PDF, texte)
  - Output: Markdown structuré selon template

- [ ] **3.1.3** Intégrer extraction automatique
  - Identifier parties automatiquement
  - Extraire dates clés
  - Détecter articles de loi mentionnés

- [ ] **3.1.4** Ajouter garde-fous
  - Signaler éléments manquants
  - Demander clarifications si ambiguïté

- [ ] **3.1.5** Tester sur 3 types de cas
  - Cas civil (contrat)
  - Cas admin (permis)
  - Cas pénal

### 3.2 Skills rédaction documents
**Objectif**: Créer des skills pour chaque type de livrable

- [ ] **3.2.1** Identifier types de documents prioritaires
  1. Recours au TF
  2. Avis de droit
  3. Mémoire de réponse
  4. Conclusions
  5. Procuration
  
- [ ] **3.2.2** Pour chaque type, créer skill dédiée
  - `redaction-recours-tf`
  - `redaction-avis-droit`
  - `redaction-memoire-reponse`
  - `redaction-conclusions`
  - `redaction-procuration`

- [ ] **3.2.3** Définir inputs/outputs pour chaque skill
  - Input: Analyse de cas + Recherches
  - Output: Document Markdown structuré

- [ ] **3.2.4** Intégrer styles rédactionnels suisses
  - Formules d'usage
  - Structure IRAC-CH
  - Ton formel approprié

### 3.3 Templates livrables
**Objectif**: Créer des modèles Word pour chaque type de document

- [ ] **3.3.1** Collecter modèles existants
  - Demander à l'utilisateur ses templates actuels
  - Identifier éléments communs

- [ ] **3.3.2** Créer templates Word (.dotx)
  - Styles prédéfinis (Titre 1, Corps, Citation, etc.)
  - En-têtes/pieds de page standards
  - Numérotation automatique

- [ ] **3.3.3** Stocker dans `templates/`
  ```
  templates/
  ├── recours-tf.dotx
  ├── avis-droit.dotx
  ├── memoire-reponse.dotx
  └── ...
  ```

- [ ] **3.3.4** Intégrer avec skill `docx` existante
  - Mapper Markdown → Styles Word
  - Générer .docx depuis template

---

## Phase 4: Skills Médicales

### 4.1 Skill recherche médicale
**Objectif**: Fournir des sources médicales fiables

- [ ] **4.1.1** Identifier sources médicales suisses/internationales
  - PubMed / MEDLINE
  - Cochrane Library
  - UpToDate
  - Revues médicales suisses (SMF, etc.)
  - Guidelines SUVA/LAA

- [ ] **4.1.2** Créer skill `recherche-medicale`
  - Requêtes PubMed structurées
  - Filtres: langue, date, type d'étude
  - Priorisation sources suisses

- [ ] **4.1.3** Intégrer niveau de preuve
  - Classification evidence-based medicine
  - Signaler méta-analyses vs case reports

- [ ] **4.1.4** Formater pour usage juridique
  - Citations complètes
  - Résumés accessibles (non-médecin)

### 4.2 Skill analyse expertise médicale
**Objectif**: Analyser expertises et vérifier conformité aux bonnes pratiques

- [ ] **4.2.1** Définir structure d'analyse expertise
  ```
  Expertise médicale
  ├── Médecin expert (qualifications)
  ├── Patient / Contexte
  ├── Anamnèse rapportée
  ├── Examen clinique
  ├── Examens complémentaires
  ├── Diagnostic(s)
  ├── Causalité (naturelle, adéquate)
  ├── Incapacité de travail
  └── Conclusions
  ```

- [ ] **4.2.2** Créer skill `analyse-expertise-medicale`
  - Input: PDF expertise
  - Output: Analyse structurée + points critiques

- [ ] **4.2.3** Intégrer vérification bonnes pratiques
  - Guidelines SUVA pour expertises
  - Critères jurisprudentiels (ATF sur expertises)
  - Détection incohérences

- [ ] **4.2.4** Comparer aux risques usuels
  - Base de données complications connues
  - Statistiques par intervention
  - Signaler écarts significatifs

- [ ] **4.2.5** Générer points de contestation
  - Arguments juridiques potentiels
  - Questions pour contre-expertise

---

## Phase 5: Infrastructure Cas

### 5.1 Structure dossiers cas
**Objectif**: Organiser les données par cas juridique

- [ ] **5.1.1** Définir structure standard
  ```
  cases/
  └── [NOM_CAS]/
      ├── README.md           # Vue d'ensemble du cas
      ├── 01-faits/
      │   ├── chronologie.md
      │   └── pieces/         # Documents sources
      ├── 02-analyse/
      │   ├── analyse-cas.md
      │   └── questions-juridiques.md
      ├── 03-recherche/
      │   ├── jurisprudence.md
      │   ├── doctrine.md
      │   └── legislation.md
      ├── 04-medical/         # Si applicable
      │   ├── expertise-analyse.md
      │   └── recherche-medicale.md
      └── 05-livrables/
          ├── recours-draft.md
          └── recours-final.docx
  ```

- [ ] **5.1.2** Créer script de création de cas
  - `scripts/new-case.sh [nom-cas]`
  - Génère structure vide avec templates

- [ ] **5.1.3** Documenter conventions de nommage
  - Format date: `YYYY-MM-DD`
  - Format cas: `client-sujet-date`

### 5.2 Format Markdown + TOC
**Objectif**: Assurer lisibilité Obsidian et navigation

- [ ] **5.2.1** Définir template Markdown standard
  ```markdown
  ---
  cas: [NOM_CAS]
  type: [analyse|recherche|livrable]
  date: YYYY-MM-DD
  status: [draft|review|final]
  ---
  
  # Titre
  
  ## Table des matières
  - [Section 1](#section-1)
  - [Section 2](#section-2)
  
  ## Section 1
  ...
  ```

- [ ] **5.2.2** Créer script génération TOC automatique
  - Parse headers Markdown
  - Génère liens ancres

- [ ] **5.2.3** Ajouter métadonnées YAML frontmatter
  - Cas associé
  - Type de document
  - Statut
  - Liens vers autres documents

- [ ] **5.2.4** Créer MOC par cas
  - `cases/[CAS]/README.md` comme index
  - Liens vers tous les documents du cas

### 5.3 Export Obsidian/Word
**Objectif**: Permettre export vers formats utilisables

- [ ] **5.3.1** Configurer Obsidian vault
  - Pointer vers `cases/`
  - Configurer plugins (TOC, dataview)

- [ ] **5.3.2** Créer workflow Markdown → Word
  - Utiliser skill `docx` existante
  - Mapper styles Markdown → Word
  - Préserver TOC, numérotation

- [ ] **5.3.3** Automatiser export final
  - Script `scripts/export-livrable.sh [cas] [document]`
  - Génère .docx avec template approprié

- [ ] **5.3.4** Ajouter export PDF (optionnel)
  - Via pandoc ou Word → PDF
  - Préserver mise en page

---

## Suivi et priorisation

### Légende statuts

| Statut | Signification |
|--------|---------------|
| [ ] | À faire |
| [~] | En cours |
| [x] | Terminé |
| [-] | Annulé/reporté |

### Priorités

| Priorité | Tâches |
|----------|--------|
| **P0 - Critique** | 1.2 (MCP), 2.4 (META recherche), 3.1 (analyse cas) |
| **P1 - Important** | 1.3 (réorg skills), 2.3 (migration MCP), 3.2 (rédaction) |
| **P2 - Normal** | 2.1 (audit liens), 2.2 (analyse Entscheidsuche), 5.x (infra) |
| **P3 - Nice-to-have** | 4.x (médical), templates avancés |

### Dépendances

```
1.2 (Test MCP) ──────┐
                     ├──► 2.3 (Migration MCP) ──► 2.4 (META recherche)
1.3 (Réorg skills) ──┘
                                                          │
3.1 (Analyse cas) ────────────────────────────────────────┼──► 3.2 (Rédaction)
                                                          │
5.1 (Structure cas) ──► 5.2 (Format MD) ──► 5.3 (Export) ─┘
```

---

## Notes

### Questions ouvertes

1. Quels templates Word utilises-tu actuellement?
2. Quels types de cas sont les plus fréquents?
3. As-tu des exemples anonymisés pour tester les skills?
4. Préfères-tu Obsidian local ou vault partagé?

### Ressources nécessaires

- Accès MCP Entscheidsuche (déjà configuré?)
- Accès MCP Onlinekommentar
- Templates Word existants
- Exemples de cas anonymisés

---

*Document généré à partir du brainstorming TODO - Février 2026*
