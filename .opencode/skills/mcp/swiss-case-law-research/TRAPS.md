# Pièges à Éviter - Swiss Case Law Research

Erreurs courantes et solutions pour la recherche de jurisprudence suisse via Entscheidsuche.

---

## Piège 1: Recherche Uniquement en Français

### Erreur
Rechercher uniquement avec des termes français.

### Conséquence
- Manquer **70% des décisions** (allemand dominant)
- Jurisprudence incomplète
- Biais géographique vers cantons romands

### Solution
```
1. Recherche PRINCIPALE en allemand
   Query: "Kündigungsschutz"
   
2. Recherche COMPLÉMENTAIRE en français
   Query: "protection contre licenciement"
   
3. Fusion des résultats pertinents
```

---

## Piège 2: Trop de Résultats Sans Affinement

### Erreur
Requête trop large retournant >500 résultats sans analyse.

### Conséquence
- Surcharge d'information
- Décisions pertinentes noyées
- Analyse impossible

### Solution
```
Stratégie d'affinement:

1. Si >500 résultats:
   - Ajouter termes spécifiques (AND)
   - Filtrer par juridiction (court:CH_BGer)
   - Restreindre période
   
2. Cible idéale: 20-100 résultats

3. Exemple:
   ❌ "Datenschutz" → 2000+ résultats
   ✅ "Datenschutz" AND "Arbeitsrecht" AND court:CH_BGer → 45 résultats
```

---

## Piège 3: Ignorer la Hiérarchie des Sources

### Erreur
Traiter toutes les décisions comme équivalentes.

### Conséquence
- Citer jurisprudence cantonale comme autorité suprême
- Ignorer BGE de principe
- Conseils juridiques incorrects

### Solution
**Hiérarchie à respecter:**

| Priorité | Source | Autorité |
|----------|--------|----------|
| 1 | **BGE** (arrêts publiés) | Autorité maximale |
| 2 | **BGer** (non publiés) | Haute autorité |
| 3 | **TAF/TPF** | Autorité fédérale spécialisée |
| 4 | **Tribunaux cantonaux** | Application locale |

```
Workflow correct:
1. Chercher d'abord les BGE sur le sujet
2. Compléter avec BGer récents
3. Vérifier application cantonale si pertinent
```

---

## Piège 4: Traduction Littérale des Termes Juridiques

### Erreur
Traduire mot-à-mot les concepts juridiques.

### Conséquence
- Résultats non pertinents
- Concepts juridiques différents entre langues
- Faux amis juridiques

### Solution
**Utiliser la terminologie juridique native:**

| ❌ Traduction littérale | ✅ Terme juridique correct |
|------------------------|---------------------------|
| "protection personnelle" | "Persönlichkeitsschutz" |
| "bon comportement" | "Treu und Glauben" (bonne foi) |
| "proportionnel" | "verhältnismässig" |

**Ressource:** Consulter Jurivoc (thésaurus juridique trilingue du TF)

---

## Piège 5: Récupérer Trop de Documents Complets

### Erreur
Télécharger 20+ documents complets pour analyse détaillée.

### Conséquence
- Surcharge de contexte
- Temps de traitement excessif
- Perte de focus

### Solution
```
Règle: Maximum 3-5 documents complets

Workflow:
1. Recherche → 20-30 résultats (métadonnées)
2. Lecture abstracts → sélection 5-8 candidats
3. Récupération complète → 3-5 décisions max
4. Analyse détaillée de ces décisions
```

---

## Piège 6: Ignorer les Dates et l'Évolution

### Erreur
Ne pas vérifier si la jurisprudence est actuelle.

### Conséquence
- Citer jurisprudence obsolète
- Ignorer revirements récents
- Conseils dépassés

### Solution
```
Vérifications obligatoires:

1. Date de la décision
   - < 5 ans = actuelle
   - 5-10 ans = vérifier s'il y a eu évolution
   - > 10 ans = chercher confirmation récente

2. Recherche de revirement
   Query: "[concept]" AND (date:2023 OR date:2024)
   
3. Comparer avec décisions antérieures
   - Même principe maintenu?
   - Nuances ajoutées?
```

---

## Piège 7: Sur-généraliser à Partir d'une Décision

### Erreur
Conclure "la jurisprudence dit X" sur base d'une seule décision.

### Conséquence
- Généralisation abusive
- Ignorer exceptions
- Mauvaise analyse juridique

### Solution
```
Validation de jurisprudence:

1. Trouver au minimum 2-3 décisions concordantes
2. Vérifier s'il y a des décisions contraires
3. Distinguer:
   - Jurisprudence constante (mehrfach bestätigt)
   - Décision isolée
   - Revirement récent
   
4. Formuler avec nuance:
   ✅ "Dans sa jurisprudence constante, le TF considère..."
   ✅ "Dans l'arrêt [X], le TF a jugé que..."
   ❌ "La jurisprudence dit que..." (sur base d'un seul arrêt)
```

---

## Piège 8: Mauvaise Syntaxe de Recherche

### Erreur
Utiliser une syntaxe incorrecte pour les requêtes.

### Exemples Fréquents

| ❌ Erreur | ✅ Correct | Explication |
|----------|-----------|-------------|
| `terme1, terme2` | `terme1 AND terme2` | Virgule n'est pas opérateur |
| `"mot"` unique | `mot` | Guillemets pour phrases |
| `protect*ion` | `protect*` | Wildcard en fin seulement |
| `NOT terme` seul | `autre NOT terme` | NOT doit suivre un terme |

### Syntaxe Correcte
```elasticsearch
# AND (les deux termes requis)
Datenschutz AND Arbeitsrecht

# OR (l'un ou l'autre)
Kündigung OR licenciement

# Phrase exacte
"protection de la personnalité"

# Wildcard
Kündig* → Kündigung, Kündigungsschutz, etc.

# Exclusion
Datenschutz -Strafrecht

# Combinaison
(Datenschutz OR "protection données") AND Arbeitsrecht
```

---

## Piège 9: Oublier les Éléments Procéduraux

### Erreur
Se focaliser uniquement sur le fond sans considérer la procédure.

### Conséquence
- Citer décision d'irrecevabilité comme précédent de fond
- Ignorer le contexte procédural
- Mauvaise compréhension de la portée

### Solution
```
Vérifier systématiquement:

1. Type de décision
   - Fond (au mérite) vs Procédure
   - Irrecevabilité vs Rejet

2. Considérants pertinents
   - Erwägungen sur la recevabilité
   - Erwägungen sur le fond (seuls ceux-ci font jurisprudence)

3. Dispositif
   - Admis → principe validé
   - Rejeté → principe réfuté
   - Irrecevable → pas de jugement de fond
```

---

## Piège 10: Ne Pas Avertir des Limitations

### Erreur
Présenter les résultats comme exhaustifs et définitifs.

### Conséquence
- Fausse impression de certitude
- Responsabilité en cas d'erreur
- Attentes irréalistes de l'utilisateur

### Solution
**Toujours inclure les avertissements:**

```markdown
## ⚠️ Avertissement

- Cette recherche est indicative, non exhaustive
- La base de données peut ne pas être à jour
- Ces informations ne constituent pas un avis juridique
- Pour des conseils spécifiques, consultez un avocat
- La jurisprudence peut évoluer
```

---

## Récapitulatif

| # | Piège | Solution Clé |
|---|-------|--------------|
| 1 | Recherche FR uniquement | Priorité à l'allemand (70%) |
| 2 | Trop de résultats | Affiner avec AND, filtres |
| 3 | Ignorer hiérarchie | BGE > BGer > Cantonal |
| 4 | Traduction littérale | Termes juridiques natifs |
| 5 | Trop de documents | Max 3-5 complets |
| 6 | Ignorer dates | Vérifier actualité, revirements |
| 7 | Sur-généraliser | Min 2-3 décisions concordantes |
| 8 | Mauvaise syntaxe | AND, OR, "", *, - |
| 9 | Oublier procédure | Vérifier type de décision |
| 10 | Pas d'avertissement | Toujours mentionner limitations |
