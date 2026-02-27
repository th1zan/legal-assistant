# Templates - Swiss Case Law Research

Templates structurés pour la recherche de jurisprudence suisse via Entscheidsuche.

---

## Template 1: Rapport de Recherche Complet

```markdown
# Recherche Jurisprudentielle : [Sujet]

## 📊 Vue d'Ensemble
- **Décisions trouvées** : [nombre]
- **Période couverte** : [années]
- **Principales juridictions** : [tribunaux]

## 🔍 Résultats de la Recherche

### Requête utilisée
```
[query exacte]
```

### Distribution
- Tribunal fédéral (BGer/BGE) : X décisions
- Tribunaux cantonaux : Y décisions
- Autres : Z décisions

## ⚖️ Décisions Clés

### 1. [Titre] - [Signature]
**Tribunal** : [Nom]  
**Date** : [Date]  
**Références** : [Numéro]

**Résumé** :
[2-3 phrases]

**Principe juridique** :
[Règle dégagée]

**Lien** : [URL]

---

### 2. [Deuxième décision]
[Même structure...]

---

### 3. [Troisième décision]
[Même structure...]

## 📝 Analyse Jurisprudentielle

### Principes Généraux
[Synthèse des règles de droit]

### Évolution
[Tendances observées]

### Application Pratique
[Application au cas de l'utilisateur]

## 🔗 Recherches Complémentaires Suggérées

1. [Piste 1]
2. [Piste 2]
3. [Piste 3]

## ⚠️ Avertissement

Ces décisions sont fournies à titre informatif. Pour des conseils juridiques spécifiques, consultez un avocat qualifié.
```

---

## Template 2: Fiche de Décision

```markdown
## [Signature de la décision]

### Métadonnées
| Champ | Valeur |
|-------|--------|
| **Tribunal** | [Nom complet] |
| **Date** | [JJ.MM.AAAA] |
| **Numéro de cas** | [Référence] |
| **Langue** | [DE/FR/IT] |
| **Type** | [BGE publié / BGer non publié / Cantonal] |

### Résumé
[Résumé en 3-5 phrases des faits et de la décision]

### Faits Clés (Sachverhalt)
- [Fait 1]
- [Fait 2]
- [Fait 3]

### Question Juridique
[Question centrale tranchée]

### Considérants Principaux (Erwägungen)
> [Citation du considérant clé]

### Dispositif
[Résultat: admis/rejeté/partiellement admis]

### Principe Juridique Dégagé
[Règle de droit établie par cette décision]

### Pertinence pour le Cas
[Comment cette décision s'applique à la situation]

### Lien
[URL complète]
```

---

## Template 3: Tableau Comparatif de Décisions

```markdown
## Tableau Comparatif : [Sujet]

| Critère | Décision 1 | Décision 2 | Décision 3 |
|---------|------------|------------|------------|
| **Signature** | [Sig1] | [Sig2] | [Sig3] |
| **Date** | [Date1] | [Date2] | [Date3] |
| **Tribunal** | [Trib1] | [Trib2] | [Trib3] |
| **Faits clés** | [Faits1] | [Faits2] | [Faits3] |
| **Question** | [Q1] | [Q2] | [Q3] |
| **Solution** | [Sol1] | [Sol2] | [Sol3] |
| **Principe** | [Princ1] | [Princ2] | [Princ3] |

### Synthèse Comparative
[Analyse des similitudes et différences]

### Évolution Jurisprudentielle
[Comment la jurisprudence a évolué entre ces décisions]
```

---

## Template 4: Requêtes de Recherche

### Format Requête Simple
```
[terme1] AND [terme2]
```

### Format Requête Multilingue
```
Query DE: "[terme allemand]" AND "[concept]"
Query FR: "[terme français]" AND "[concept]"
```

### Format Requête avec Filtres
```
Query: "[termes]" AND court:[code_tribunal]
Period: [année début]-[année fin]
```

---

## Template 5: Checklist de Recherche

```markdown
## Checklist Recherche Jurisprudentielle

### Phase 1: Préparation
- [ ] Identifier le domaine juridique
- [ ] Extraire les mots-clés principaux
- [ ] Déterminer la juridiction pertinente
- [ ] Préparer termes en allemand (langue principale)

### Phase 2: Exploration
- [ ] Requête large (20-30 résultats)
- [ ] Analyser distribution tribunaux
- [ ] Identifier termes connexes
- [ ] Évaluer volume de résultats

### Phase 3: Affinement
- [ ] Ajouter termes spécifiques si trop de résultats
- [ ] Élargir avec wildcards si pas assez
- [ ] Essayer recherche multilingue si nécessaire

### Phase 4: Sélection
- [ ] Identifier 3-5 décisions clés
- [ ] Privilégier BGE (publiés)
- [ ] Inclure BGer récents
- [ ] Vérifier jurisprudence cantonale si pertinent

### Phase 5: Analyse
- [ ] Récupérer documents complets
- [ ] Lire Sachverhalt et Erwägungen
- [ ] Extraire principes juridiques
- [ ] Vérifier cohérence inter-décisions

### Phase 6: Synthèse
- [ ] Structurer rapport selon template
- [ ] Citer correctement (signature, date, tribunal)
- [ ] Appliquer au cas de l'utilisateur
- [ ] Suggérer recherches complémentaires
```

---

## Vocabulaire Juridique Multilingue

### Termes de Recherche Courants

| Domaine | DE | FR | IT |
|---------|----|----|-----|
| **Protection données** | Datenschutz | Protection des données | Protezione dei dati |
| **Licenciement** | Kündigung | Licenciement | Licenziamento |
| **Protection licenciement** | Kündigungsschutz | Protection contre licenciement | Protezione dal licenziamento |
| **Bail** | Mietrecht | Droit du bail | Diritto di locazione |
| **Contrats** | Vertragsrecht | Droit des contrats | Diritto dei contratti |
| **Droit pénal** | Strafrecht | Droit pénal | Diritto penale |
| **Bonne foi** | Treu und Glauben | Bonne foi | Buona fede |
| **Abus de droit** | Rechtsmissbrauch | Abus de droit | Abuso di diritto |

### Termes Procéduraux

| DE | FR | IT | Signification |
|----|----|----|---------------|
| Beschwerde | Recours | Ricorso | Voie de recours |
| Urteil | Jugement/Arrêt | Sentenza | Décision finale |
| Verfügung | Décision | Decisione | Acte administratif |
| Erwägungen | Considérants | Considerandi | Raisonnement |
| Sachverhalt | État de fait | Fatti | Exposé des faits |
| Dispositiv | Dispositif | Dispositivo | Partie décisoire |

---

## Abréviations Légales Courantes

| Code | Loi | Domaine |
|------|-----|---------|
| OR / CO | Code des Obligations | Contrats, travail |
| ZGB / CC | Code Civil | Personnes, famille |
| StGB / CP | Code Pénal | Droit pénal |
| BV / Cst. | Constitution fédérale | Droits fondamentaux |
| ZPO / CPC | Code de procédure civile | Procédure |
| StPO / CPP | Code de procédure pénale | Procédure pénale |
| DSG / LPD | Loi protection des données | Privacy |
| BGG / LTF | Loi Tribunal fédéral | Organisation judiciaire |
