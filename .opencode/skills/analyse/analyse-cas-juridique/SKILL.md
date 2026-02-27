# Analyse Cas Juridique (Complete Legal Case Analysis)

**Skill Name**: `analyse-cas-juridique`  
**Domain**: Swiss Legal Analysis  
**Language Support**: FR (primary), DE, IT  
**Version**: 1.1  
**Created**: 26 février 2026  
**Updated**: 27 février 2026

---

## Introduction

### Purpose

Cette skill effectue l'**analyse juridique complète** selon la méthodologie suisse, combinant :
1. **Extraction des faits** (depuis `@extract-facts`)
2. **Identification des questions** (depuis `@identify-legal-issues`)
3. **Raisonnement juridique** (syllogisme + subsomption)

C'est la **skill analytique centrale** qui applique les normes aux faits concrets.

### When to Use

Invoquer cette skill (`@analyse-cas-juridique`) quand vous devez :
- **Analyser un cas juridique complet** avec raisonnement syllogistique
- **Appliquer des normes** aux faits concrets (subsomption)
- **Rédiger des consultations** pour clients
- **Préparer des réponses d'examen** (Klausur, brevet d'avocat)
- **Combiner extraction + identification + raisonnement** en une analyse

**Invoquer APRÈS** :
1. Extraction des faits (`@extract-facts`) OU
2. Identification des questions (`@identify-legal-issues`) OU
3. Les deux étapes seront effectuées en premier si nécessaire

---

## Methodology

### Le Syllogisme Juridique

L'analyse juridique suisse est structurée autour du **syllogisme** :

> "Juristische Tätigkeit besteht also zu einem grossen Teil in der (mit Gründen versehenen) Anwendung allgemeiner Rechtsnormen auf den Einzelfall."
> — Thommen, *Fallbearbeitung im Strafrecht*, UZH

**Structure** :
- **Majeure (Obersatz)** : Règle juridique générale et abstraite
- **Mineure (Untersatz)** : Faits concrets du cas
- **Conclusion (Konklusion)** : Conséquence juridique appliquée au cas

### Subsomption : L'Opération Centrale

> "Das zentrale stilistische Mittel der strafrechtlichen Fallbearbeitung bildet die Subsumtion."
> — Thommen, UZH

**Subsomption** = Opération intellectuelle de rattachement d'un état de fait concret à une catégorie juridique abstraite.

### Principes Directeurs

1. **Da mihi facta, dabo tibi ius** — Séparation stricte faits/droit
2. **Structure syllogistique** — Majeure → Mineure → Conclusion obligatoire
3. **Subsomption en 4 étapes** — Question → Définition → Subsomption → Conclusion partielle
4. **Citations obligatoires** — Norme + ATF + doctrine pour chaque assertion
5. **Distinction problématique/non-problématique** — Concentrer l'effort sur les éléments douteux

### Deux Traditions Suisses

#### Tradition Francophone (Méthode UNIL)

**Structure** :
1. Analyse des faits (parties, chronologie, enjeux)
2. Formulation de la réponse hypothétique
3. Conditions d'application de la norme (subsomption 4 étapes)

**Question clé** : *"Qui veut quoi de qui à quelle(s) condition(s) ?"*

#### Tradition Germanophone (Gutachtenstil)

**Structure** (droit pénal) :
1. **Obersatz** : "Wer hat sich wie wonach strafbar gemacht?"
2. **Tatbestand** : Objektiver + Subjektiver Tatbestand
3. **Rechtswidrigkeit** : Justifications (Notstand, Notwehr)
4. **Schuld** : Vorsatz ou Fahrlässigkeit
5. **Fazit** : Conclusion

**Question clé** : *"Wer will was von wem woraus?"*

---

## Instructions

### Phase 1 : Préparation

1. **Lire l'énoncé** complet sans annoter
2. **Identifier le domaine** (civil, pénal, administratif)
3. **Déterminer le contexte** :
   - Examen académique (DE) → Gutachtenstil strict
   - Brevet avocat (FR) → Méthode UNIL
   - Consultation client → UNIL simplifié
   - Recours TF → Utiliser `@recours-tf`
4. **Choisir la langue** (FR, DE, IT)

### Phase 2 : Analyser les Faits

Si les faits n'ont PAS été extraits :
- Invoquer `@extract-facts` OU
- Extraire manuellement : parties, chronologie, faits pertinents, qualifications

**Output** : Section "I. ANALYSE DES FAITS" (FR) ou "SACHVERHALT" (DE)

### Phase 3 : Identifier les Questions

Si les questions n'ont PAS été identifiées :
- Invoquer `@identify-legal-issues` OU
- Identifier manuellement : reformulation, "Qui veut quoi de qui ?", questions multiples

**Output** : Section "II. QUESTION JURIDIQUE" (FR) ou "FRAGE(N)" (DE)

### Phase 4 : Rechercher les Normes

1. **Identifier le droit applicable** (articles précis : article, alinéa, chiffre, lettre)
2. **Rechercher la jurisprudence** (ATF avec numéro de considérant)
3. **Consulter la doctrine** (commentaires CR, BSK, CHK)

### Phase 5 : Formuler la Réponse Hypothétique

> "[Client] pourra obtenir [prétention] de [défendeur] sur la base de l'art. [X] [Code] **SI les conditions suivantes sont réunies** : [liste]"

**Output** : Section "III. RÉPONSE HYPOTHÉTIQUE" (FR) ou "Obersatz" (DE)

### Phase 6 : Subsomption

**Pour CHAQUE condition de la norme** :

#### Éléments Non-Problématiques (traitement simplifié)
> Affirmation simple (1-2 phrases) : "A est une personne physique capable."

#### Éléments Problématiques (subsomption 4 étapes)

**1. QUESTION**
> [Élément] est-[il/elle] réalisé(e) au sens de l'art. [X] [Code] ?

**2. DÉFINITION**
> Selon l'art. [X] al. [Y] [Code] et ATF [XXX III XXX] consid. [X.X] : "[définition]"

**3. SUBSOMPTION**
> En l'espèce : [faits pertinents] → [confrontation avec définition] → [argumentation]

**4. CONCLUSION PARTIELLE**
> ✅ / ❌ [Condition] [est/n'est pas] réalisée.

→ Voir templates détaillés dans [TEMPLATES.md](./TEMPLATES.md)

### Phase 7 : Conclusion Globale

1. **Synthétiser** les conclusions partielles
2. **Appliquer** la conséquence juridique
3. **Répondre** directement à la question originale

**Output** : Section "V. CONCLUSION" (FR) ou "FAZIT" (DE)

### Phase 8 : Éléments Professionnels (consultation client)

Si consultation client, ajouter :
- **Stratégie recommandée** : Prochaines étapes
- **Moyens de preuve** : Documents à réunir
- **Chances de succès** : Évaluation (%)
- **Risques** : Prescription, fardeau de la preuve, etc.

---

## Output Format

### Structure Francophone (FR)

```
## I. ANALYSE DES FAITS
## II. QUESTION JURIDIQUE
## III. RÉPONSE HYPOTHÉTIQUE
## IV. CONDITIONS D'APPLICATION
## V. CONCLUSION
## VI. RECOMMANDATIONS (si consultation)
```

### Structure Germanophone (DE)

```
# [Titel]
## Obersatz
## I. Tatbestand
## II. Rechtswidrigkeit
## III. Schuld
## Fazit
```

→ Templates complets dans [TEMPLATES.md](./TEMPLATES.md)

---

## Pièges à Éviter

⚠️ **12 pièges courants** documentés dans [TRAPS.md](./TRAPS.md).

**Les plus critiques** :
1. **Confusion fait/droit** → Séparer strictement les sections
2. **Subsomption inversée** → Ordre Question → Définition → Subsomption → Conclusion
3. **Oublier la recevabilité** → Vérifier compétence, qualité, délais AVANT le fond
4. **Traiter tout également** → Identifier le Schwerpunkt, développer les éléments problématiques
5. **Citations imprécises** → Article + alinéa + chiffre + lettre
6. **Syllogisme absent** → Expliciter Majeure → Mineure → Conclusion

---

## Examples

📚 **3 exemples complets** dans [EXAMPLES.md](./EXAMPLES.md) :

1. **Défaut de la chose vendue** (CO 197) — Méthode UNIL complète
2. **Droit pénal** (CP 144 + CP 17 Notstand) — Gutachtenstil
3. **Recours administratif** (PA) — Structure 4 niveaux

---

## References

📖 **Sources complètes** dans [REFERENCE.md](./REFERENCE.md) :

**4 sources méthodologiques primaires** :
- UNIL (Canapa) — Méthode de résolution de cas (2022)
- ODAGE (Genève) — Guide pratique brevet d'avocat (2020)
- GAIUS (Roduit) — Résolution de cas en droit (2015)
- UZH (Thommen) — Fallbearbeitung im Strafrecht

**Doctrine de référence** :
- CR-CO, CR-CP, CR-CPC — Commentaires romands
- BSK-OR, BSK-StGB, BSK-ZPO — Basler Kommentar
- Tercier/Pichonnaz, Gauch/Schluep/Schmid — Manuels

---

## Related Skills

### Workflow Recommandé

```
1. @extract-facts           → Extraire les faits pertinents
2. @identify-legal-issues   → Formuler les questions juridiques
3. @analyse-cas-juridique   → Analyse syllogistique (CETTE SKILL)
4. @recours-tf              → Rédiger recours TF (si applicable)
```

### Skills Complémentaires

- **@parse-decision** — Parser décisions suisses (Entscheidsuche)
- **@citation-formatter** — Formater citations juridiques
- **@swiss-case-law-research** — Recherche jurisprudence
- **@swiss-legal-commentary** — Recherche doctrine

---

## Checklist Qualité

Avant de livrer l'analyse, vérifier :

- [ ] Structure syllogistique complète (Majeure → Mineure → Conclusion)
- [ ] Subsomption 4 étapes pour TOUS les éléments problématiques
- [ ] Citations ATF avec numéro de considérant
- [ ] Citations doctrine avec auteur, titre, marge/page
- [ ] Citations légales précises (alinéa, chiffre, lettre)
- [ ] Conclusions partielles claires (✅/❌) pour chaque condition
- [ ] Réponse finale directe à la question originale
- [ ] Éléments professionnels inclus (si consultation client)

---

## Version History

**v1.1** (27 février 2026) :
- Refactoring atomique : extraction templates, pièges, exemples, références
- Réduction de 885 → ~280 lignes

**v1.0** (26 février 2026) :
- Implémentation initiale basée sur recherche Phase 5
- Méthodologie UNIL + Gutachtenstil
- 12 pièges documentés
- Exemples complets

---

**Annexes** :
- [TEMPLATES.md](./TEMPLATES.md) — Templates de sortie FR/DE
- [TRAPS.md](./TRAPS.md) — 12 pièges à éviter
- [EXAMPLES.md](./EXAMPLES.md) — 3 exemples complets
- [REFERENCE.md](./REFERENCE.md) — Sources et bibliographie
