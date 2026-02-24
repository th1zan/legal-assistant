# Méthode systématique — Exemples pratiques

## Exemple 1 : Résiliation de bail abusive

### Étape 1 — Analyse du problème
Un locataire conteste la résiliation de son bail. Le bailleur a résilié le bail pour effectuer des travaux de rénovation. Le locataire suspecte une résiliation de représailles suite à une demande de baisse de loyer.

**Question juridique** : La résiliation est-elle abusive au sens de l'art. 271 CO ?

### Étape 2 — Opérationnalisation

**Références légales** :
- art. 271 CO (résiliation annulable)
- art. 271a CO (résiliation abusive du bailleur)
- art. 270a CO (contestation du loyer)

**Mots-clés FR** : résiliation, bail, abusive, représailles, congé, annulable, loyer, baisse
**Mots-clés DE** : Kündigung, Miete, missbräuchlich, Vergeltung, Mietzinsherabsetzung

### Étape 3 — Formulation

**Sur Swisslex** (⚠️ payant) :
```
("art. 271" or "art. 271a") same CO same (résili* or cong*) same (abus* or représaill*)
```

**Version bilingue** :
```
("art. 271" or "art. 271a") same (abus* or missbräuchlich* or représaill* or Vergeltung*)
```

**Sur bger.ch (gratuit)** :
```
+"art. 271" +CO +résiliation +abusive
```

### Étape 4 — Évaluation
- Si trop de résultats → ajouter `same (loyer or Mietzins)`
- Si pas assez → supprimer « représailles », garder « abusive »

---

## Exemple 2 : Responsabilité du médecin

### Étape 1 — Analyse
Un patient subit un dommage lors d'une intervention chirurgicale. Il veut engager la responsabilité civile du médecin.

**Questions juridiques** :
- Art. 97 CO (responsabilité contractuelle) ?
- Art. 41 CO (responsabilité délictuelle) ?
- Faute, causalité, dommage ?

### Étape 2 — Opérationnalisation

**Références** : art. 97 CO, art. 41 CO, art. 398 al. 2 CO
**Mots-clés FR** : médecin, responsabilité, faute, erreur médicale, dommage, patient
**Mots-clés DE** : Arzt, Haftung, Kunstfehler, Schaden, Patient, ärztliche Sorgfalt

### Étape 3 — Formulation

```
(médecin or Arzt) same (responsab* or Haftung or Haftpflicht) same (faute or erreur or Kunstfehler or Sorgfalt*)
```

---

## Exemple 3 : Méthode analogique — Rétroprogressive

### Point de départ
ATF 135 III 397 (arrêt récent sur la responsabilité contractuelle)

### Démarche
1. Lire les **considérants** : identifier les arrêts cités
   - ATF 133 III 121
   - ATF 127 III 453
   - ATF 116 II 305
2. Consulter chacun de ces arrêts → noter leurs propres références
3. Remonter jusqu'aux arrêts **fondateurs** du principe
4. Dresser un arbre de la jurisprudence

### Résultat
```
ATF 135 III 397 (2009) ← cite
├── ATF 133 III 121 (2007) ← cite
│   └── ATF 116 II 305 (1990) ← arrêt fondateur
└── ATF 127 III 453 (2001) ← cite
    └── ATF 116 II 305 (1990) ← même arrêt fondateur
```

---

## Exemple 4 : Méthode analogique — Progressive

### Point de départ
ATF 116 II 305 (arrêt fondateur)

### Démarche sur Swisslex (⚠️ payant)
1. Ouvrir l'arrêt ATF 116 II 305
2. Cliquer sur **« Document cité dans »**
3. Obtenir la liste de tous les arrêts ultérieurs citant cet arrêt
4. Filtrer par date, domaine, pertinence
5. Identifier les **confirmations**, **nuances** et **revirements**
