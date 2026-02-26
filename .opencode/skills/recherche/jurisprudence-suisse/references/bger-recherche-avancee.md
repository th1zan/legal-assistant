# Recherche avancée sur bger.ch — Guide détaillé

> ⚠️ **Accès payant** : Les fonctions avancées décrites ci-dessous nécessitent un abonnement (accessible via universités suisses ou abonnement professionnel).

## Vue d'ensemble

bger.ch offre deux niveaux d'accès :
- **Gratuit** : recherche plein texte de base
- **Payant** ⚠️ : recherche structurée, descripteurs Jurivoc, répertoires

Ce guide couvre les techniques avancées de la section payante.

---

## Section gratuite — Rappel des techniques

### Recherche dans les ATF (depuis 1954)
- **Par référence** : `ATF 118 II 91`
- **Par article de loi** : `"art. 10 CP"` (expression exacte — limité, ne trouve pas « art. 10 al. 2 CP »)
- **Plein texte** : opérateurs `+` (ET), `-` (SAUF), `"..."` (expression exacte)

### Résultats en trois listes
1. Correspondance exacte
2. Correspondance approximative
3. Correspondance partielle

### Autres arrêts (dès 2000)
- Par numéro de cause : `2P.44/2001`
- Par date
- Plein texte avec mêmes opérateurs

---

## Section payante ⚠️ — Recherche par répertoire

### Répertoire systématique
- Structure miroir du RS (Recueil systématique)
- Navigation arborescente : choisir la loi, puis la disposition
- Résultats : résumés brefs + références
- **Combinable** avec une recherche plein texte par mots-clés

### Répertoire alphabétique
- Liste alphabétique de mots-clés
- Sélectionner un terme, puis choisir les volumes à interroger

---

## Section payante ⚠️ — Recherche experte standard

### Recherche par référence législative
Saisir `art. 42 CO` **sans guillemets** :
- Le système reconnaît automatiquement la référence
- Étend la recherche aux subdivisions (trouve aussi art. 42 al. 1, al. 2, etc.)
- Recherche **trilingue** automatique

### Recherche CHLexML (ATF depuis 1990)
Saisir une référence structurée : `<CH/LPE/11>` pour l'art. 11 LPE
- **Avantage** : élimine les décisions qui ne citent la norme qu'en passant
- Ne trouve que les arrêts où la norme est **réellement appliquée**

### Option « seulement le résumé »
Restreindre la recherche au chapeau/sommaire des ATF. Utile pour cibler les arrêts de principe.

---

## Section payante ⚠️ — Recherche experte structurée

### Les six masques (A à F)
Chaque masque accepte :
- Termes
- Descripteurs Jurivoc
- Normes
- Références ATF
- Combinaisons avec opérateurs booléens (AND, OR, ANDNOT)

### Type de champ (menu déroulant)
| Option | Fonction |
|--------|----------|
| `normes` | Recherche par référence législative |
| `descripteurs` | Recherche par mots-clés Jurivoc |
| `termes` | Correspondance exacte en plein texte |
| `flexions` | Trouve singulier et pluriel |

### Champ distance
Définir la distance maximale en mots entre deux termes liés par un opérateur. Permet de cibler les passages où les concepts sont proches.

### Combinaison des masques
Les masques A à F se combinent dans le champ **« combinaison de champs »**. Permet des requêtes très précises croisant normes, descripteurs et plein texte.

---

## Outils supplémentaires

### Descripteurs Jurivoc
Après chaque requête, le système propose les descripteurs Jurivoc pertinents :
- Cliquer sur un descripteur → rechercher tous les ATF indexés avec lui (depuis 1990)
- Multilingue (FR, DE, IT)
- Cliquer `?` → synonymes, antonymes, termes associés

### Assistant de recherche
- Étend automatiquement la requête avec des mots-clés
- Traduit en allemand/italien
- Tri par date
- Fonctionne uniquement pour les ATF

### Diagramme temps/pertinence
Graphique combinant pertinence (axe Y) et chronologie (axe X) :
- **Haut à droite** = arrêts les plus pertinents ET les plus récents
- Permet d'identifier rapidement les arrêts clés récents

### Outils dans la colonne de droite d'un arrêt

| Outil | Fonction |
|-------|----------|
| **Commentaires** | Doctrine citant cet ATF |
| **Publications** | Revues ayant publié/traduit l'arrêt (JdT, SJ, RDAF) |
| **Normes** | Dispositions législatives indexées (depuis 1990) |
| **Descripteurs** | Termes d'indexation Jurivoc |

> **« Publications »** est essentiel pour trouver les traductions d'un ATF allemand dans les revues romandes.
