---
name: terminologie-juridique-multilingue
description: "Outils de terminologie juridique multilingue pour le droit suisse : Jurivoc (thésaurus trilingue FR/DE/IT du TF), Termdat (base terminologique de la Chancellerie fédérale), IATE (terminologie UE), Thésaurus de droit suisse (Swisslex). Utiliser cette skill quand l'utilisateur doit traduire un terme juridique entre le français, l'allemand et l'italien, chercher des synonymes juridiques, ou préparer une recherche multilingue."
---

# Terminologie juridique multilingue

## Pourquoi le multilinguisme est essentiel

Le droit suisse est rédigé en **trois langues officielles** (FR, DE, IT) qui font **toutes foi** (art. 14 al. 1 LPubl). Une recherche sérieuse doit couvrir au minimum le français et l'allemand, car :
- La majorité de la doctrine est en allemand
- Le TF rédige dans la langue de la procédure (souvent DE)
- Les ATF ne sont **pas traduits** (seul le chapeau l'est)

## Jurivoc — Thésaurus du Tribunal fédéral

### Caractéristiques
- **Gratuit** : accessible sur jurivoc.bger.ch
- **Trilingue** : FR / DE / IT
- Utilisé comme **descripteurs** pour l'indexation des ATF
- Hiérarchique : termes génériques, spécifiques, associés

### Utilisation
1. Saisir un terme juridique en français
2. Obtenir la **traduction** en allemand et italien
3. Découvrir les **termes associés** et **synonymes**
4. Utiliser ces termes pour élargir la recherche dans les bases de données

### Troncature dans Jurivoc
- Postérieure : `constru*`
- Antérieure : `*construction`
- Intermédiaire : `bau*recht`

### Exemple
Recherche : `responsabilité civile`
→ DE : `Haftpflicht` | IT : `responsabilità civile`
→ Termes associés : `dommages-intérêts`, `faute`, `causalité`

## Termdat — Base terminologique fédérale

### Caractéristiques
- **Gratuit** : termdat.bk.admin.ch
- ~1,5 million d'entrées
- Couvre le **droit**, l'administration, et de nombreux domaines spécialisés
- Multilingue : FR, DE, IT, EN (et autres langues selon les entrées)

### Utilisation
- Recherche par terme dans une langue, affichage des équivalents
- Contexte d'usage et définitions pour chaque entrée
- Plus large que Jurivoc (couvre aussi le vocabulaire administratif et technique)

## IATE — Terminologie de l'Union européenne

### Caractéristiques
- **Gratuit** : iate.europa.eu
- 23 langues de l'UE
- Utile pour le **droit européen** et les accords bilatéraux Suisse-UE
- Termes validés par les services de traduction de l'UE

### Utilisation
Particulièrement utile quand on travaille sur :
- Les accords bilatéraux
- Le droit de la concurrence
- La protection des données (RGPD)
- Le droit de la propriété intellectuelle

## Thésaurus de droit suisse (Swisslex)

> ⚠️ **Accès payant** : intégré à Swisslex, nécessite un abonnement

### Caractéristiques
- Plus de 300'000 entrées
- Inclut des **synonymes** et **termes associés**
- Enrichit automatiquement les requêtes (expansion de termes)

### Fonctionnement
Quand le thésaurus est activé dans Swisslex :
- `bail` → cherche aussi `location`, `loyer`, `contrat de bail`
- Pour désactiver : décocher la case thésaurus (recherche littérale)

## Stratégie de recherche multilingue

### Collections entièrement traduites
- **RS, RO, FF** : textes identiques en FR, DE, IT → rechercher dans sa langue suffit
- **Constitutions cantonales** au RS fédéral : traduites

### Collections partiellement traduites
- **ATF** : seul le chapeau est traduit, l'arrêt est dans la langue de la procédure
- **Doctrine** : majoritairement en allemand ou en français selon l'auteur

### Procédure recommandée
1. Formuler la requête en **français**
2. Traduire les termes clés via **Jurivoc** ou **Termdat**
3. Reformuler en **allemand** (et italien si pertinent)
4. Lancer les recherches dans les **deux langues** au minimum
5. Combiner avec les opérateurs OR : `(bail OR Miete) AND (résiliation OR Kündigung)`
