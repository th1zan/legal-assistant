# Guide d'Utilisation des Skills Juridiques

Guide de référence rapide pour utiliser les skills de recherche juridique suisse.

**Dernière mise à jour** : 2026-02-25  
**Structure** : Hiérarchique (6 catégories)

---

## 📚 Table des Matières

1. [Vue d'Ensemble](#vue-densemble)
2. [Skills par Catégorie](#skills-par-catégorie)
3. [Workflows Recommandés](#workflows-recommandés)
4. [Guide des Abréviations](#guide-des-abréviations)
5. [Stratégies de Recherche](#stratégies-de-recherche)
6. [Limitations](#limitations)
7. [Ressources](#ressources)

---

## 🎯 Vue d'Ensemble

### Structure des Skills

Les skills sont organisés en **6 catégories** :

```
.opencode/skills/
├── mcp/          → Skills utilisant les serveurs MCP (2)
├── recherche/    → Skills de recherche juridique (13)
├── analyse/      → Skills d'analyse de cas (0 - à créer)
├── redaction/    → Skills de rédaction (0 - à créer)
├── production/   → Production de documents (4)
└── anthropic/    → Skills génériques Claude (3)
```

### Invocation des Skills

**Format** : `@category/skill-name`

**Exemples** :
```
@mcp/swiss-case-law-research
@recherche/recherche-juridique-suisse
@production/docx
```

---

## 📂 Skills par Catégorie

### 1. MCP (Accès aux Bases de Données)

Skills qui interrogent directement les serveurs MCP pour accéder aux bases de données juridiques suisses.

#### @mcp/swiss-case-law-research

**MCP** : entscheidsuche  
**Base de données** : >1 million de décisions judiciaires  
**Couverture** : Tribunaux fédéraux + 26 cantons  
**Langues** : DE (70%), FR (25%), IT (5%)  
**Performance** : ~1.2s par requête

**Utiliser quand** :
- ✓ Chercher des arrêts du Tribunal fédéral
- ✓ Trouver de la jurisprudence cantonale
- ✓ Identifier des précédents judiciaires
- ✓ Vérifier la pratique judiciaire sur un sujet

**Exemples de questions** :
```
"Cherche des décisions du BGer sur le licenciement pendant la grossesse"
"Quelle est la jurisprudence récente (2020-2024) sur la protection des données ?"
"Trouve des arrêts du Tribunal fédéral sur l'art 8 CEDH discrimination"
```

---

#### @mcp/swiss-legal-commentary

**MCP** : onlinekommentar  
**Base de données** : Commentaires juridiques doctrinaux  
**Couverture** : Lois fédérales principales  
**Langues** : DE, FR, IT, EN (selon commentaire)  
**Performance** : ~0.8s par requête

**Utiliser quand** :
- ✓ Expliquer un article de loi spécifique
- ✓ Comprendre la doctrine juridique
- ✓ Trouver des commentaires d'auteurs
- ✓ Interpréter une disposition légale

**Exemples de questions** :
```
"Explique l'article 328 CO sur la protection de la personnalité"
"Que dit la doctrine sur l'interprétation de l'art 641 CC (propriété)"
"Quels sont les commentaires juridiques sur la nouvelle LPD 2023"
```

---

### 2. Recherche (Méthodologie et Sources)

Skills qui fournissent des guides méthodologiques et accès aux sources juridiques.

#### @recherche/recherche-juridique-suisse ⭐ META

**Type** : META skill - Carte de navigation (MOC)  
**Rôle** : Orchestre tous les autres skills de recherche

**Utiliser quand** :
- ✓ Question juridique générale (le skill route automatiquement)
- ✓ Besoin d'aide pour formuler une recherche
- ✓ Incertain de quel skill utiliser

**Exemples** :
```
@recherche/recherche-juridique-suisse "Comment chercher de la jurisprudence sur les contrats de travail ?"
@recherche/recherche-juridique-suisse "Je dois analyser l'art 8 CEDH, par où commencer ?"
```

---

#### @recherche/outils-recherche-juridique

**Type** : Outils techniques (MCP, CLI, APIs)  
**Contenu** :
- Serveurs MCP (entscheidsuche, onlinekommentar)
- CLI Fedlex SPARQL (9000+ lois fédérales)
- APIs cantonales

**Utiliser quand** :
- ✓ Accéder techniquement aux sources juridiques
- ✓ Utiliser le CLI Fedlex pour recherche législative
- ✓ Comprendre l'infrastructure MCP

---

#### @recherche/bases-donnees-juridiques

**Type** : Guide des bases de données  
**Contenu** : Fedlex, bger.ch, Lexfind, Swisslex (comparaison)

**Utiliser quand** :
- ✓ Savoir quelle base de données utiliser
- ✓ Comprendre différences entre bases gratuites et payantes
- ✓ Choisir la source appropriée pour une recherche

---

#### @recherche/jurisprudence-suisse

**Type** : Guide de la jurisprudence  
**Contenu** :
- ATF (Arrêts du Tribunal fédéral publiés)
- ATAF (Tribunal administratif fédéral)
- TPF (Tribunal pénal fédéral)
- Structure des arrêts, codes des cours

**Utiliser quand** :
- ✓ Comprendre la structure d'un arrêt du TF
- ✓ Identifier une cour par son code
- ✓ Chercher de la jurisprudence cantonale
- ✓ Comprendre la hiérarchie des décisions

---

#### @recherche/sources-legislatives-federales

**Type** : Guide de la législation fédérale  
**Contenu** :
- Recueil systématique (RS)
- Recueil officiel (RO)
- Feuille fédérale (FF)
- Travaux préparatoires

**Utiliser quand** :
- ✓ Chercher une loi fédérale
- ✓ Trouver un article de la Constitution
- ✓ Accéder aux travaux préparatoires
- ✓ Comprendre la procédure législative

---

#### @recherche/sources-cantonales

**Type** : Guide du droit cantonal  
**Contenu** :
- 26 recueils systématiques cantonaux
- Concordats intercantonaux
- Droit communal

**Utiliser quand** :
- ✓ Chercher une loi cantonale
- ✓ Trouver un concordat
- ✓ Accéder au droit communal
- ✓ Travaux préparatoires cantonaux

---

#### @recherche/sources-doctrinales

**Type** : Guide de la doctrine  
**Contenu** :
- Traités, manuels, commentaires
- Catalogues de bibliothèques (RERO, Alexandria)
- Google Scholar

**Utiliser quand** :
- ✓ Chercher un ouvrage juridique
- ✓ Trouver un article de revue
- ✓ Identifier les commentaires d'une loi
- ✓ Recherche bibliographique

---

#### @recherche/droit-international-suisse

**Type** : Guide du droit international  
**Contenu** :
- Traités internationaux
- Accords bilatéraux avec l'UE
- CEDH, CIJ, soft law

**Utiliser quand** :
- ✓ Chercher un traité international liant la Suisse
- ✓ Accords bilatéraux Suisse-UE
- ✓ Jurisprudence CEDH
- ✓ Droit international public

---

#### @recherche/citation-juridique-suisse

**Type** : Guide des conventions de citation  
**Contenu** :
- Lois fédérales (RS, RO)
- Arrêts du TF (ATF)
- Feuille fédérale (FF)
- Doctrine

**Utiliser quand** :
- ✓ Citer une source juridique suisse
- ✓ Comprendre une référence
- ✓ Rédiger des notes de bas de page
- ✓ Format académique ou judiciaire

---

#### @recherche/techniques-recherche-juridique

**Type** : Méthodologie de recherche  
**Contenu** :
- Troncature (essentielle pour l'allemand)
- Opérateurs de proximité
- Stratégie multilingue

**Utiliser quand** :
- ✓ Formuler une requête de recherche optimisée
- ✓ Recherche multilingue (FR/DE/IT)
- ✓ Comprendre les spécificités de la recherche juridique

---

#### @recherche/methodologie-recherche-jurisprudentielle

**Type** : Méthodologie avancée  
**Contenu** :
- Méthode systématique en 5 étapes
- Méthode analogique (rétroprogressive et progressive)
- Recherche thématique

**Utiliser quand** :
- ✓ Mener une recherche jurisprudentielle structurée
- ✓ Trouver des arrêts pertinents sur un sujet
- ✓ Appliquer une méthodologie rigoureuse

---

#### @recherche/terminologie-juridique-multilingue

**Type** : Outils de terminologie  
**Contenu** :
- Jurivoc (thésaurus trilingue FR/DE/IT du TF)
- Termdat (Chancellerie fédérale)
- IATE (terminologie UE)

**Utiliser quand** :
- ✓ Traduire un terme juridique (FR/DE/IT)
- ✓ Chercher des synonymes juridiques
- ✓ Préparer une recherche multilingue

---

#### @recherche/veille-juridique

**Type** : Outils de veille  
**Contenu** :
- Alertes automatiques
- Flux RSS
- Newsletters juridiques
- Saved searches (Swisslex)

**Utiliser quand** :
- ✓ Mettre en place un système de veille
- ✓ Suivre l'évolution du droit
- ✓ Surveiller nouveaux arrêts
- ✓ Modifications législatives

---

### 3. Analyse (À Créer - P2 Priority)

Skills pour l'analyse structurée de cas juridiques.

**À créer** :
- [ ] `analyse-cas-structuree` - Décomposition structurée (faits → droit → raisonnement)
- [ ] `analyse-recevabilite` - Analyse de recevabilité (recours TF)
- [ ] `analyse-jurisprudence-pertinente` - Identification d'arrêts pertinents
- [ ] `verification-delais` - Vérification des délais procéduraux
- [ ] `qualification-juridique` - Qualification juridique des faits

**Statut** : Phase 3 (Semaines 5-6)

---

### 4. Rédaction (À Créer - P1/P2 Priority)

Skills pour la rédaction de documents juridiques.

**À créer (P1 - Priorité)** :
- [ ] `recours-tf` - Recours au Tribunal fédéral
- [ ] `avis-droit` - Avis de droit / Gutachten

**À créer (P2 - Moyen)** :
- [ ] `memoire-reponse` - Mémoire de réponse/réplique
- [ ] `conclusions` - Conclusions (principales et subsidiaires)
- [ ] `courrier-client` - Courrier client

**Statut** : Phase 3-4 (Semaines 5-7)

---

### 5. Production (Documents)

Skills pour créer et manipuler des documents dans différents formats.

#### @production/docx

**Type** : Création/édition de documents Word  
**Format** : .docx

**Utiliser quand** :
- ✓ Créer un document Word
- ✓ Éditer un document existant
- ✓ Générer des rapports, mémoires, lettres
- ✓ Exporter vers format requis par tribunaux

---

#### @production/pdf

**Type** : Manipulation de PDF  
**Format** : .pdf

**Utiliser quand** :
- ✓ Fusionner plusieurs PDFs
- ✓ Extraire pages d'un PDF
- ✓ Annoter un document
- ✓ Créer un PDF à partir d'autres formats

---

#### @production/pptx

**Type** : Création de présentations  
**Format** : .pptx

**Utiliser quand** :
- ✓ Créer une présentation
- ✓ Préparer des slides pour plaidoirie
- ✓ Support visuel pour formation

---

#### @production/xlsx

**Type** : Feuilles de calcul  
**Format** : .xlsx

**Utiliser quand** :
- ✓ Créer un tableau de dommages
- ✓ Calculer des coûts
- ✓ Gérer des données tabulaires

---

### 6. Anthropic (Skills Génériques)

Skills génériques Claude/Anthropic non spécifiques au droit.

#### @anthropic/skill-creator

**Type** : Méta-skill  
**Utiliser pour** : Créer de nouveaux skills OpenCode

---

#### @anthropic/mcp-builder

**Type** : Méta-skill  
**Utiliser pour** : Créer de nouveaux serveurs MCP

---

#### @anthropic/doc-coauthoring

**Type** : Workflow de co-rédaction  
**Utiliser pour** : Rédiger de la documentation structurée

---

## 🔄 Workflows Recommandés

### Workflow 1 : Question Juridique Générale

```
1. @recherche/recherche-juridique-suisse
   → Le META skill route automatiquement vers les skills appropriés

2. Doctrine (@mcp/swiss-legal-commentary)
   → Comprendre le cadre juridique

3. Jurisprudence (@mcp/swiss-case-law-research)
   → Voir l'application par les tribunaux

4. Synthèse
   → Réponse complète avec sources
```

**Exemple** :
```
Question : "Un employeur peut-il licencier une femme enceinte ?"

Étape 1 : @recherche/recherche-juridique-suisse (routage)
Étape 2 : @mcp/swiss-legal-commentary → Art. 336c CO
Étape 3 : @mcp/swiss-case-law-research → "Kündigung Schwangerschaft"
Étape 4 : Synthèse → Principe, conditions, conséquences
```

---

### Workflow 2 : Recherche sur un Article Spécifique

```
1. @mcp/swiss-legal-commentary
   → Commentaire doctrinal de l'article

2. @mcp/swiss-case-law-research
   → Application par les tribunaux

3. @recherche/citation-juridique-suisse
   → Citer correctement les sources trouvées
```

---

### Workflow 3 : Recherche de Précédent

```
1. @mcp/swiss-case-law-research
   → Trouver des cas similaires

2. @recherche/methodologie-recherche-jurisprudentielle
   → Méthode analogique pour élargir

3. @mcp/swiss-legal-commentary
   → Vérifier le cadre théorique

4. Synthèse
   → Application au cas concret
```

---

### Workflow 4 : Rédaction d'un Recours TF (P1 - À Créer)

```
1. @analyse/analyse-recevabilite (à créer)
   → Vérifier conditions de recevabilité

2. @analyse/analyse-cas-structuree (à créer)
   → Décomposer faits/droit/raisonnement

3. @mcp/swiss-case-law-research
   → Trouver jurisprudence pertinente

4. @redaction/recours-tf (à créer)
   → Générer le recours structuré

5. @production/docx
   → Exporter en Word avec template
```

---

## 📖 Guide des Abréviations Juridiques

### Lois Principales

| Abréviation | Nom Complet | Code SR |
|-------------|-------------|---------|
| **Cst. / BV** | Constitution fédérale | SR-101 |
| **CC / ZGB** | Code civil suisse | SR-210 |
| **CO / OR** | Code des obligations | SR-220 |
| **CP / StGB** | Code pénal suisse | SR-311.0 |
| **CPC / ZPO** | Code de procédure civile | SR-272 |
| **CPP / StPO** | Code de procédure pénale | SR-312.0 |
| **LPD / DSG** | Loi sur la protection des données | SR-235.1 |

### Tribunaux

| Code | Nom FR | Nom DE | Nom IT |
|------|--------|--------|--------|
| **BGer** | Tribunal fédéral | Bundesgericht | Tribunale federale |
| **BGE** | Arrêts publiés TF | Bundesgerichtsentscheide | Decisioni del TF |
| **BVGer** | Tribunal administratif fédéral | Bundesverwaltungsgericht | Tribunale amministrativo federale |
| **BStGer** | Tribunal pénal fédéral | Bundesstrafgericht | Tribunale penale federale |

---

## 🔍 Stratégies de Recherche par Domaine

### Droit du Travail

**Termes DE** : Arbeitsrecht, Kündigung, Kündigungsschutz, Lohnfortzahlung  
**Termes FR** : droit travail, licenciement, protection, salaire  
**Articles clés** : Art. 319-362 CO

**Workflow** :
1. @mcp/swiss-legal-commentary → Art. 336 CO (licenciement abusif)
2. @mcp/swiss-case-law-research → BGer sur le sujet
3. Jurisprudence cantonale si aspect local

---

### Droit des Contrats

**Termes DE** : Vertragsrecht, Vertragsabschluss, Gewährleistung  
**Termes FR** : droit contrats, formation contrat, garantie  
**Articles clés** : Art. 1-40 CO (partie générale)

**Workflow** :
1. @mcp/swiss-legal-commentary → Article(s) applicable(s)
2. @mcp/swiss-case-law-research → BGE de principe
3. Application récente

---

### Protection des Données

**Termes DE** : Datenschutz, DSGVO, Persönlichkeitsschutz  
**Termes FR** : protection données, RGPD, vie privée  
**Articles clés** : Art. 13 Cst., LPD complète

**Workflow** :
1. @mcp/swiss-legal-commentary → LPD (nouvelle loi 2023)
2. @mcp/swiss-case-law-research → Jurisprudence récente
3. @recherche/droit-international-suisse → CEDH si pertinent

---

### Droit Pénal

**Termes DE** : Strafrecht, Straftat, Strafzumessung  
**Termes FR** : droit pénal, infraction, fixation peine  
**Articles clés** : CP complet selon infraction

**Workflow** :
1. @mcp/swiss-legal-commentary → Article d'infraction
2. @mcp/swiss-case-law-research → Application/interprétation
3. Jurisprudence cantonale sur quantum peine

---

## 💡 Astuces et Bonnes Pratiques

### Recherche Multilingue

```
Toujours rechercher en ALLEMAND d'abord (70% des décisions)
→ Puis compléter en français si nécessaire
→ Italien pour Tessin uniquement

Exemple :
1. "Kündigungsschutz Schwangerschaft" (DE)
2. "licenciement grossesse" (FR)
→ Fusionner les résultats pertinents

Utiliser : @recherche/terminologie-juridique-multilingue pour traductions
```

### Filtrage par Juridiction

```
Question FÉDÉRALE → Filtrer BGer/BGE
Question LOCALE → Inclure canton pertinent
Question MIXTE → Les deux

Exemple :
"Peut-on augmenter le loyer ?" (droit fédéral)
→ Priorité BGer

"Application règlement construction Genève" (droit local)
→ Priorité CH_GE + BGer si recours
```

### Hiérarchie des Sources

```
AUTORITÉ MAXIMALE
1. BGE (arrêts publiés du TF)
2. BGer (arrêts non publiés du TF)
3. Tribunaux cantonaux
4. Doctrine académique

STRATÉGIE
→ Commencer par BGE pour principes
→ BGer pour applications récentes
→ Cantons pour pratique locale
→ Doctrine pour analyse théorique
```

---

## 🚨 Limitations et Avertissements

### Limitations Techniques

1. **Pagination** : Max 50 résultats par requête (MCP)
2. **Performance** : Entscheidsuche ~1.2s, Onlinekommentar ~0.8s
3. **Format documents** : JSON toujours disponible, PDF parfois absent
4. **Couverture doctrine** : En développement, pas tous articles commentés
5. **Langues** : Commentaires pas toujours multilingues

### Limitations Juridiques

1. **Pas un avis juridique** : Information générale uniquement
2. **Consultation avocat** : Toujours recommandée pour cas concret
3. **Base non exhaustive** : Malgré 1M+ décisions, 100% impossible
4. **Évolution constante** : Droit change, vérifier actualité

### Quand Consulter un Professionnel

```
🔴 TOUJOURS pour :
- Cas concret nécessitant représentation
- Décisions avec conséquences importantes
- Procédures judiciaires
- Rédaction actes officiels

🟡 RECOMMANDÉ pour :
- Interprétation complexe
- Situations ambiguës
- Montants importants en jeu
- Délais légaux à respecter

🟢 Information générale OK :
- Compréhension d'une loi
- Culture juridique générale
- Recherche académique
- Préparation première consultation
```

---

## 📚 Ressources Complémentaires

### Documentation Détaillée

**MCP Skills** :
- `.opencode/skills/mcp/swiss-case-law-research/SKILL.md`
- `.opencode/skills/mcp/swiss-legal-commentary/SKILL.md`

**Recherche Skills** :
- `.opencode/skills/recherche/recherche-juridique-suisse/SKILL.md` (META)
- `.opencode/skills/recherche/outils-recherche-juridique/SKILL.md`
- Autres : Voir `.opencode/skills/recherche/`

**Production Skills** :
- `.opencode/skills/production/docx/SKILL.md`
- `.opencode/skills/production/pdf/SKILL.md`

**Projet** :
- `MCP_TOOLS_REFERENCE.md` - Référence complète des outils MCP
- `MCP_BENCHMARK_RESULTS.md` - Tests de performance
- `DECISIONS.md` - Décisions stratégiques du projet
- `SKILLS_AUDIT.md` - Audit de réorganisation
- `README.md` - Introduction générale

### Sites Officiels

- **Entscheidsuche.ch** : https://entscheidsuche.ch (jurisprudence)
- **Fedlex** : https://www.fedlex.admin.ch (législation fédérale)
- **BGer** : https://www.bger.ch (Tribunal fédéral)
- **Onlinekommentar** : https://onlinekommentar.ch (doctrine)

---

## 📊 Statistiques du Projet

**Skills Totaux** : 22  
**Par Catégorie** :
- MCP : 2 skills (opérationnels, <2s)
- Recherche : 13 skills (complets)
- Analyse : 0 skills (à créer en Phase 3)
- Rédaction : 0 skills (à créer en Phase 3-4)
- Production : 4 skills (opérationnels)
- Anthropic : 3 skills (outils de dev)

**Performance MCP** :
- Entscheidsuche : ~1.2s (1.8M+ décisions)
- Onlinekommentar : ~0.8s (commentaires doctrinaux)

**Couverture** : 80% des tâches juridiques répétitives (objectif)

---

## 🔄 Mises à Jour

**Version** : 2.0 (réorganisé)  
**Date** : 2026-02-25  
**Changements majeurs** :
- Structure hiérarchique (6 catégories)
- 10 skills non-juridiques supprimés
- Performance MCP validée (<2s)
- Documentation mise à jour

**Prochaine mise à jour** : Ajout des skills d'analyse et rédaction (Phase 3)

---

**Pour toute question** : Consulter `PROJECT.md` ou `TODO.md`
