# Guide d'Utilisation des Skills Juridiques

Guide de référence rapide pour utiliser les skills de recherche juridique suisse.

## 🎯 Aperçu des Skills

### 1. swiss-case-law-research
**MCP** : entscheidsuche  
**Base de données** : >1 million de décisions judiciaires  
**Couverture** : Tribunaux fédéraux + 26 cantons  
**Langues** : DE (70%), FR (25%), IT (5%)

### 2. swiss-legal-commentary
**MCP** : onlinekommentar  
**Base de données** : Commentaires doctrinaux  
**Couverture** : Lois fédérales principales  
**Langues** : DE, FR, IT, EN (selon commentaire)

## 🚀 Invocation des Skills

Les skills sont automatiquement disponibles dans votre workspace OpenWork. L'agent les utilisera quand vous posez des questions juridiques.

### Questions Déclenchant swiss-case-law-research

```
✓ "Cherche des décisions sur [sujet]"
✓ "Trouve des arrêts du Tribunal fédéral concernant [thème]"
✓ "Quelle est la jurisprudence sur [question]"
✓ "Y a-t-il des cas récents sur [domaine]"
✓ "Montre-moi la pratique judiciaire sur [topic]"
```

### Questions Déclenchant swiss-legal-commentary

```
✓ "Explique-moi l'article [X] de [loi]"
✓ "Que dit la doctrine sur [sujet]"
✓ "Quels sont les commentaires juridiques sur [thème]"
✓ "Comment interpréter [article]"
✓ "Qu'écrivent les auteurs sur [question]"
```

## 📊 Comparaison des Deux Skills

| Critère | Case Law | Commentary |
|---------|----------|------------|
| **Type de source** | Jurisprudence (décisions) | Doctrine (analyse) |
| **Autorité** | Force contraignante | Force persuasive |
| **Volume** | >1M documents | Centaines de commentaires |
| **Mise à jour** | Quotidienne | Périodique |
| **Structuration** | Par décision | Par article de loi |
| **Couverture historique** | 1875-2024 | Focus récent |
| **Usage principal** | Trouver précédents | Comprendre la loi |

## 🔄 Workflow Recommandé

### Pour une Question Juridique Générale

```
1. DOCTRINE (commentary) → Comprendre le cadre
2. JURISPRUDENCE (case-law) → Voir l'application
3. SYNTHÈSE → Réponse complète
```

**Exemple** :
```
Question : "Un employeur peut-il licencier une femme enceinte ?"

Étape 1 - DOCTRINE
→ Recherche : Art. 336c CO (licenciement abusif)
→ Résultat : Cadre juridique et conditions

Étape 2 - JURISPRUDENCE
→ Recherche : "Kündigung Schwangerschaft"
→ Résultat : Cas concrets et jurisprudence constante

Étape 3 - SYNTHÈSE
→ Principe : Licenciement possible mais souvent abusif
→ Conditions : Motifs graves nécessaires
→ Conséquences : Indemnités jusqu'à 6 mois
```

### Pour une Question sur un Article Spécifique

```
1. DOCTRINE (commentary) → Commentaire de l'article
2. JURISPRUDENCE (case-law) → Application par tribunaux
3. SYNTHÈSE → Interprétation complète
```

### Pour une Recherche de Précédent

```
1. JURISPRUDENCE (case-law) → Trouver cas similaires
2. DOCTRINE (commentary) → Vérifier cadre théorique
3. SYNTHÈSE → Application au cas
```

## 🎯 Exemples de Questions Optimales

### Excellentes Questions (Précises)

```
✅ "Cherche des arrêts du BGer sur le licenciement pendant la grossesse"
✅ "Explique l'article 328 CO sur la protection de la personnalité"
✅ "Quelle est la jurisprudence récente (2020-2024) sur la protection des données ?"
✅ "Que dit la doctrine sur l'interprétation de l'article 8 CEDH en Suisse ?"
```

### Questions Nécessitant Clarification

```
⚠️ "Cherche sur le droit du travail"
→ Trop large, préciser : quel aspect du droit du travail ?

⚠️ "Explique la loi"
→ Quelle loi ? Quel article ?

⚠️ "Y a-t-il des décisions ?"
→ Sur quel sujet spécifiquement ?
```

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

## 🔍 Stratégies de Recherche par Domaine

### Droit du Travail

**Termes DE** : Arbeitsrecht, Kündigung, Kündigungsschutz, Lohnfortzahlung  
**Termes FR** : droit travail, licenciement, protection, salaire  
**Articles clés** : Art. 319-362 CO

**Workflow** :
1. Commentaire article pertinent (ex: Art. 336 CO licenciement abusif)
2. Jurisprudence BGer sur le sujet
3. Jurisprudence cantonale si aspect local

### Droit des Contrats

**Termes DE** : Vertragsrecht, Vertragsabschluss, Gewährleistung  
**Termes FR** : droit contrats, formation contrat, garantie  
**Articles clés** : Art. 1-40 CO (partie générale)

**Workflow** :
1. Commentaire article(s) applicable(s)
2. BGE de principe (arrêts publiés)
3. Application récente

### Protection des Données

**Termes DE** : Datenschutz, DSGVO, Persönlichkeitsschutz  
**Termes FR** : protection données, RGPD, vie privée  
**Articles clés** : Art. 13 Cst., LPD complète

**Workflow** :
1. Commentaire LPD (nouvelle loi 2023)
2. Jurisprudence récente (évolution rapide)
3. Références CEDH si pertinent

### Droit Pénal

**Termes DE** : Strafrecht, Straftat, Strafzumessung  
**Termes FR** : droit pénal, infraction, fixation peine  
**Articles clés** : CP complet selon infraction

**Workflow** :
1. Commentaire article d'infraction
2. BGer sur application/interprétation
3. Jurisprudence cantonale sur quantum peine

## 💡 Astuces et Bonnes Pratiques

### Recherche Multilingue

```markdown
Toujours rechercher en ALLEMAND d'abord (70% des décisions)
→ Puis compléter en français si nécessaire
→ Italien pour Tessin uniquement

Exemple :
1. "Kündigungsschutz Schwangerschaft" (DE)
2. "licenciement grossesse" (FR)
→ Fusionner les résultats pertinents
```

### Filtrage par Juridiction

```markdown
Question FÉDÉRALE → Filtrer BGer/BGE
Question LOCALE → Inclure canton pertinent
Question MIXTE → Les deux

Exemple :
"Peut-on augmenter le loyer ?" (droit fédéral)
→ Priorité BGer

"Application règlement construction Genève" (droit local)
→ Priorité CH_GE + BGer si recours
```

### Gestion de la Temporalité

```markdown
Sujet STABLE → Jurisprudence ancienne OK
Sujet EN ÉVOLUTION → Privilégier 2-3 dernières années
NOUVEAU domaine → Toute jurisprudence utile

Exemple :
Droit successions : Principes stables → BGE anciens valables
Protection données : Nouvelle LPD 2023 → Focus récent
```

### Hiérarchie des Sources

```markdown
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

## 🚨 Limitations et Avertissements

### Limitations Techniques

1. **Pagination** : Max 50 résultats par requête
2. **Format documents** : JSON toujours disponible, PDF parfois absent
3. **Couverture doctrine** : En développement, pas tous articles commentés
4. **Langues** : Commentaires pas toujours multilingues

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

## 📚 Ressources Complémentaires

### Documentation Détaillée

- **Skill Case Law** : `.opencode/skills/swiss-case-law-research/SKILL.md`
- **Skill Commentary** : `.opencode/skills/swiss-legal-commentary/SKILL.md`
- **MCP Tools** : `MCP_TOOLS_REFERENCE.md`
- **README Principal** : `README.md`

### Sites Officiels

- **Entscheidsuche.ch** : https://entscheidsuche.ch
- **Onlinekommentar.ch** : https://onlinekommentar.ch
- **Recueil systématique** : https://www.fedlex.admin.ch

### Support Technique

```bash
# Vérifier état des serveurs MCP
./manage-mcp.sh status

# Mettre à jour les serveurs
./manage-mcp.sh update-all

# Aide complète
./manage-mcp.sh help
```

## 🎓 Exemples de Cas Complets

### Exemple 1 : Question Travailleur

**Question** : *"Mon employeur m'a licencié une semaine après que je lui ai annoncé ma grossesse. Est-ce légal ?"*

**Workflow** :

1. **DOCTRINE** (commentary)
   ```
   Recherche : "Art. 336c CO"
   Résultat : Licenciement pendant grossesse = présomption d'abus
   ```

2. **JURISPRUDENCE** (case-law)
   ```
   Recherche : "Kündigung Schwangerschaft Sperrfrist"
   Résultat : 
   - BGE 127 III 310 : Principe général
   - BGer 4A_456/2022 : Application récente
   - Quantum indemnités : 2-6 mois selon durée service
   ```

3. **RÉPONSE SYNTHÉTIQUE**
   ```
   En principe ILLÉGAL (licenciement abusif selon Art. 336c al. 1 lit. c CO)
   
   SAUF si :
   - Motifs graves sans lien avec grossesse
   - Employeur peut prouver raisons objectives
   
   CONSÉQUENCES :
   - Licenciement reste valable (ne peut être annulé)
   - Indemnité due : 2 à 6 mois de salaire
   - Charge de la preuve : employeur doit justifier
   
   RECOMMANDATION : 
   Consulter avocat spécialisé droit du travail
   Délai : Action dans 180 jours (Art. 336b CO)
   ```

### Exemple 2 : Question Locataire

**Question** : *"Mon propriétaire veut augmenter le loyer de 15% après avoir rénové la cuisine. Peut-il faire ça ?"*

**Workflow** :

1. **DOCTRINE** (commentary)
   ```
   Recherche : "Art. 269a CO" (augmentation loyer)
   Résultat : Possible si investissements "wertvermehrend" (créateurs de valeur)
   ```

2. **JURISPRUDENCE** (case-law)
   ```
   Recherche : "Mietzinserhöhung wertvermehrend Küche"
   Résultat :
   - BGer 4A_177/2020 : Critères investissements
   - Rénovation simple ≠ augmentation valeur
   - Limite : 50-70% coûts amortissables sur 15-20 ans
   ```

3. **RÉPONSE SYNTHÉTIQUE**
   ```
   EN PRINCIPE POSSIBLE mais CONDITIONS STRICTES :
   
   CRITÈRES (Art. 269a CO) :
   ✓ Investissements créateurs de valeur (pas simple entretien)
   ✓ Amélioration objective du logement
   ✓ Calcul basé sur amortissement (15-20 ans)
   
   POUR VOTRE CAS :
   - Cuisine neuve = possiblement créateur valeur
   - MAIS 15% semble élevé
   - Taux admis généralement : 2-5% selon ampleur travaux
   
   VOS DROITS :
   - Demander décompte détaillé travaux
   - Contester si disproportionné
   - Formulaire officiel requis (délai 30 jours réponse)
   
   RECOMMANDATION :
   1. Demander justificatif chiffré
   2. Si montant excessif : contestation commission conciliation
   3. Consulter ASLOCA ou avocat spécialisé
   ```

### Exemple 3 : Question Étudiant

**Question** : *"Pour mon mémoire, j'analyse l'évolution de la protection de la personnalité au travail. Peux-tu m'aider ?"*

**Workflow** :

1. **DOCTRINE** (commentary) - Cadre théorique
   ```
   Recherche : "Art. 328 CO" + "Art. 28 CC"
   Résultat : 
   - Commentaire Art. 328 CO (protection personnalité travailleur)
   - Commentaire Art. 28 CC (protection personnalité générale)
   - Auteurs principaux : Rehbinder, Streiff/von Kaenel
   ```

2. **JURISPRUDENCE** (case-law) - Évolution pratique
   ```
   Recherche chronologique :
   - Années 80-90 : Focus harcèlement physique
   - Années 2000-10 : Émergence cybersurveillance
   - Années 2010-24 : Protection données, réseaux sociaux
   
   Arrêts clés :
   - BGE 130 III 28 (2003) : Surveillance email
   - BGE 143 II 146 (2017) : Caméras lieu travail
   - BGer 4A_682/2022 : Réseaux sociaux
   ```

3. **RÉPONSE ACADÉMIQUE**
   ```
   STRUCTURE MÉMOIRE SUGGÉRÉE :
   
   I. CADRE JURIDIQUE
      A. Fondements constitutionnels (Art. 13 Cst.)
      B. Protection civile (Art. 28 CC)
      C. Protection travail (Art. 328 CO)
   
   II. ÉVOLUTION JURISPRUDENTIELLE (analyse chronologique)
      A. Phase 1 (1980-2000) : Protection physique
      B. Phase 2 (2000-2015) : Ère numérique
      C. Phase 3 (2015-2024) : Big data et IA
   
   III. ENJEUX ACTUELS
      A. Télétravail et vie privée
      B. Surveillance algorithmique
      C. Équilibre intérêts employeur/employé
   
   BIBLIOGRAPHIE :
   - Doctrine : Commentaires onlinekommentar.ch
   - Jurisprudence : BGE + BGer sélection via entscheidsuche.ch
   - Législation : CO, CC, LPD
   ```

## ✅ Checklist Recherche de Qualité

Avant de finaliser votre réponse, vérifiez :

- [ ] Sources primaires citées (BGE, BGer, commentaires)
- [ ] Références complètes (date, tribunal, auteur)
- [ ] Langue appropriée (même langue que question ou traduit)
- [ ] Hiérarchie respectée (BGE > BGer > cantonal > doctrine)
- [ ] Actualité vérifiée (date des décisions/commentaires)
- [ ] Nuances mentionnées (exceptions, débats doctrinaux)
- [ ] Limitations indiquées (avis non-juridique, consulter avocat)
- [ ] Liens fournis vers documents originaux
- [ ] Structure claire et logique
- [ ] Application au cas de l'utilisateur

---

**Version** : 1.0.0  
**Dernière mise à jour** : Février 2026  
**Pour** : Legal Assistant Workspace  

**Note** : Ce guide est un document de référence. Consultez les SKILL.md détaillés pour informations complètes.
