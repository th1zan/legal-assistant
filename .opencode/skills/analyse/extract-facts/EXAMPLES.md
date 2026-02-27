# Exemples - Extract Facts

Exemples complets d'extraction de faits juridiquement pertinents selon la méthodologie suisse.

---

## Exemple 1: Défaut de la Chose Vendue (CO 197)

### Énoncé du Cas

> Pierre Dubois, domicilié à Genève, cherchait une voiture pour aller au travail. Le 15 janvier 2025, il achète une BMW X5 de 2018 auprès d'AutoPlus SA, un concessionnaire lausannois au capital de CHF 100'000.-. Le véhicule affiche 50'000 km au compteur. Pierre paie CHF 35'000.- comptant et repart avec la voiture, très satisfait. Le vendeur, très sympathique, lui souhaite bonne route.
> 
> Le 20 février 2025, lors d'un contrôle chez un garagiste, Pierre découvre que le compteur a été trafiqué : le véhicule a en réalité 150'000 km. Pierre est furieux. Il consulte pour récupérer son argent.

### Extraction Structurée

---

#### I. ÉVALUATION INITIALE

Cas de droit civil (CO, partie spéciale) relatif à un contrat de vente mobilière. Parties: acquéreur personne physique contre vendeur SA. Question apparente: garantie des défauts (CO 197 ss) pour vice caché (compteur kilométrique falsifié).

---

#### II. PARTIES

| Partie | Qualification | Statut | Domicile/Siège |
|--------|---------------|--------|----------------|
| **Pierre Dubois (P)** | Acquéreur | Personne physique | Genève |
| **AutoPlus SA (A)** | Vendeur | SA (capital CHF 100'000.-) | Lausanne |

---

#### III. CHRONOLOGIE

| Date | Événement | Pertinence Juridique |
|------|-----------|---------------------|
| 15 janvier 2025 | Conclusion du contrat de vente (BMW X5 2018, affiché 50'000 km) | ✓ Formation du contrat (CO 184) |
| 15 janvier 2025 | Paiement du prix (CHF 35'000.-) et livraison | ✓ Exécution du contrat |
| 20 février 2025 | Découverte du vice (compteur trafiqué: réellement 150'000 km) | ✓ Découverte du défaut (CO 201) |
| [Date actuelle] | Consultation juridique | ✓ Question juridique |

**Délais calculés**:
- Entre livraison et découverte: **36 jours**
- Délai d'avis des défauts (CO 201): "immédiatement après découverte" → **délai en cours**
- Prescription (CO 210): 2 ans dès livraison → expire le **15 janvier 2027**

---

#### IV. FAITS JURIDIQUEMENT PERTINENTS (RECHTSERHEBLICH)

**A. Éléments Constitutifs du Contrat de Vente (CO 184)**

**Éléments objectifs**:
1. **Parties**: Vendeur (AutoPlus SA) et acquéreur (P)
2. **Objet**: Véhicule BMW X5 de 2018
3. **Prix**: CHF 35'000.-
4. **Transfert**: Livraison et paiement effectués le 15.01.2025

**B. Éléments Constitutifs du Défaut (CO 197)**

**Éléments objectifs**:
1. **Chose livrée**: BMW X5 avec compteur affichant 50'000 km
2. **Qualité promise/attendue**: Kilométrage de 50'000 km (affiché)
3. **Qualité réelle**: Kilométrage de 150'000 km (réel)
4. **Défaut**: Écart de 100'000 km = 200% du kilométrage affiché
5. **Qualification du défaut**: Défaut majeur (vice caché, non apparent)

**Éléments subjectifs**:
- **Connaissance du vendeur**: À déterminer (a-t-il trafiqué ou acheté ainsi?)
- **Bonne foi de l'acquéreur**: P ignorait le vice (découvert par garagiste)

**C. Éléments Procéduraux**

- **Compétence territoriale**: Lausanne (siège du défendeur) ou Genève (domicile du demandeur, consommateur)
- **Valeur litigieuse**: CHF 35'000.- → procédure ordinaire (> CHF 30'000.-)
- **Conciliation préalable**: Obligatoire (CPC 197)

---

#### V. FAITS ÉLIMINÉS (Non Rechtserheblich)

| Citation | Raison d'élimination |
|----------|---------------------|
| ❌ "cherchait une voiture pour aller au travail" | Motivation personnelle sans incidence juridique |
| ❌ "Le vendeur, très sympathique" | Appréciation subjective |
| ❌ "très satisfait" | Émotion |
| ❌ "lui souhaite bonne route" | Détail narratif |
| ❌ "Pierre est furieux" | Émotion |

---

#### VI. PROCHAINES ÉTAPES

**Recommandations**:
- [ ] Identifier les questions juridiques avec `@identify-legal-issues`
- [ ] Vérifier les conditions de CO 197 (défaut) et CO 201 (avis)
- [ ] Examiner les options: réduction (CO 205), résolution (CO 205), dommages-intérêts (CO 208)

**Lacunes identifiées**:
- Date exacte de l'avis des défauts au vendeur?
- Le vendeur savait-il le compteur trafiqué?

---

## Exemple 2: Cas Pénal - Dommages à la Propriété avec État de Nécessité (CP 144 + CP 17)

### Énoncé du Cas

> Par une chaude journée d'été, Marc, un sympathique voisin de 35 ans, passe devant la maison de Jean. Il remarque de la fumée s'échappant du rez-de-chaussée. Inquiet, il tente d'appeler les pompiers, mais son téléphone est sans batterie. La maison est fermée à clé. Marc, paniqué, décide de briser la baie vitrée (valeur: CHF 2'000.-) pour entrer et éteindre le début d'incendie avec un extincteur. Grâce à son intervention rapide, la maison est sauvée, seuls quelques meubles sont légèrement endommagés.
> 
> Jean, propriétaire de la maison, rentre de vacances et découvre sa baie vitrée brisée. Il porte plainte contre Marc pour dommages à la propriété.

### Extraction Structurée

---

#### I. ÉVALUATION INITIALE

Cas de droit pénal relatif à des dommages à la propriété (CP 144) avec fait justificatif potentiel (état de nécessité, CP 17). Parties: auteur (M) et propriétaire/lésé (J). Question: l'état de nécessité justifie-t-il la destruction de la baie vitrée?

---

#### II. PARTIES

| Partie | Qualification | Statut |
|--------|---------------|--------|
| **Marc (M)** | Auteur (prévenu) | Personne physique, 35 ans |
| **Jean (J)** | Lésé (partie plaignante) | Personne physique, propriétaire |

---

#### III. CHRONOLOGIE

| Date/Moment | Événement | Pertinence Juridique |
|-------------|-----------|---------------------|
| [Jour X] | M observe fumée au rez-de-chaussée de la maison de J | ✓ Situation de danger (CP 17) |
| [Jour X] | M tente d'appeler les pompiers - téléphone sans batterie | ✓ Subsidiarité (CP 17) |
| [Jour X] | M brise la baie vitrée (CHF 2'000.-) | ✓ Dommages à la propriété (CP 144) |
| [Jour X] | M éteint l'incendie - maison sauvée | ✓ Résultat de l'intervention |
| [Date ultérieure] | J porte plainte contre M | ✓ Plainte pénale déposée |

---

#### IV. FAITS JURIDIQUEMENT PERTINENTS (RECHTSERHEBLICH)

**A. Éléments Constitutifs - Dommages à la Propriété (CP 144)**

**Éléments objectifs**:
1. **Täter (auteur)**: Marc (M)
2. **Tathandlung (action)**: Briser (einschlagen) la baie vitrée
3. **Tatobjekt (objet)**: Baie vitrée de Jean (fremde Sache - chose d'autrui)
4. **Erfolg (résultat)**: Destruction de la vitre, valeur CHF 2'000.-

**Éléments subjectifs**:
- **Intention**: M a **volontairement** brisé la vitre (Vorsatz établi)
- **But**: Éteindre l'incendie et sauver la maison

**B. Éléments Justificatifs - État de Nécessité (CP 17)**

**Notstandslage (situation de détresse)**:
1. **Bien juridique menacé**: Propriété de J (maison, valeur élevée)
2. **Danger**: Incendie (feu au rez-de-chaussée)
3. **Immédiateté**: Danger immédiat et actuel

**Notstandshandlung (action de nécessité)**:
1. **Subsidiarité**: Aucune autre solution disponible
   - Pompiers injoignables (téléphone sans batterie)
   - Maison fermée à clé
2. **Proportionnalité**: Bien sacrifié << Bien sauvé
   - Bien sacrifié: Baie vitrée (CHF 2'000.-)
   - Bien sauvé: Maison entière (plusieurs centaines de milliers CHF)
   - Ratio: largement proportionné

**C. Éléments Procéduraux**

- **Plainte déposée**: Oui (CP 144 est un délit poursuivi sur plainte)
- **Délai de plainte**: 3 mois dès connaissance (CP 31) - à vérifier

---

#### V. FAITS ÉLIMINÉS (Non Rechtserheblich)

| Citation | Raison d'élimination |
|----------|---------------------|
| ❌ "Par une chaude journée d'été" | Contexte météo sans incidence |
| ❌ "un sympathique voisin de 35 ans" | Appréciation subjective |
| ❌ "Inquiet" | Émotion (mais conservé implicitement pour intention) |
| ❌ "paniqué" | Émotion |

**Exception - Faits CONSERVÉS**:

| Citation | Raison de conservation |
|----------|----------------------|
| ✅ "téléphone sans batterie" | Démontre la **subsidiarité** (pas d'alternative) |
| ✅ "maison fermée à clé" | Démontre la **subsidiarité** |
| ✅ "maison sauvée, seuls quelques meubles endommagés" | Démontre la **proportionnalité** du résultat |

---

#### VI. PROCHAINES ÉTAPES

**Recommandations**:
- [ ] Identifier les questions juridiques avec `@identify-legal-issues`
- [ ] Analyser CP 144 (éléments constitutifs) puis CP 17 (justification)
- [ ] Conclusion probable: Marc est justifié par l'état de nécessité

**Points à clarifier**:
- Délai exact entre découverte par J et dépôt de plainte
- J savait-il que M avait sauvé sa maison?

---

## Points Clés des Exemples

### Différences Droit Civil vs Droit Pénal

| Aspect | Exemple 1 (Civil) | Exemple 2 (Pénal) |
|--------|-------------------|-------------------|
| **Terminologie** | Acquéreur/Vendeur | Auteur/Lésé |
| **Éléments subjectifs** | Bonne/mauvaise foi | Intention (Vorsatz) |
| **Faits extinctifs** | Prescription, paiement | Faits justificatifs |
| **Procédure** | Valeur litigieuse, conciliation | Plainte, délai de plainte |

### Éléments Toujours à Extraire

1. **Parties** avec qualification juridique précise
2. **Chronologie** avec dates exactes et délais calculés
3. **Éléments objectifs** mappés aux Tatbestandsmerkmale
4. **Éléments subjectifs** (intention, connaissance, foi)
5. **Éléments procéduraux** (compétence, délais, recevabilité)
6. **Faits à éliminer** avec justification

### Règle d'Or

> **"Rechtserheblich nur"**: Seuls les faits correspondant à un élément constitutif d'une norme juridique méritent d'être extraits et reformulés.
