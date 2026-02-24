# bger.ch — Guide de recherche détaillé

## Section gratuite

### Accès
Page d'accueil bger.ch > **« Jurisprudence (gratuit) »**

### Recherche dans les ATF

#### Par référence connue
- Sélectionner « ATF (gratuit) » > saisir la référence (ex. `ATF 118 II 91`)
- Alternative : « ATF (Arrêts principaux) » > « Index ATF dès vol. 1 (1875) »

> Note : Les ATF avant 1954 étaient historiquement accessibles via servat.unibe.ch, mais cette ressource peut ne plus être disponible. Consulter bger.ch pour les ATF depuis 1954.

#### Par référence législative
Saisir la référence entre guillemets précédée de « art. » : `"art. 10 CP"`

> **Attention** : cette méthode ne retrouve que l'expression exacte. Elle manquera `art. 10 et 11 CP` ou `art. 10 al. 2 CP`. Préférer Swisslex pour une recherche exhaustive par disposition.

#### Par référence jurisprudentielle
Saisir la référence complète d'un ATF cité en plein texte. Une requête en français retourne les résultats dans les trois langues. Limitation par date possible (1954 à aujourd'hui).

#### Sans référence connue (plein texte)
Opérateurs disponibles :
| Syntaxe | Effet |
|---------|-------|
| `"..."` | Expression exacte |
| `+` | ET (le terme doit être présent) |
| `-` | SAUF (le terme doit être absent) |
| espace | Retourne cumul ET alternative dans deux listes séparées |

Résultats classés en :
1. **Correspondance exacte** (tous les termes présents)
2. **Correspondance approximative** (la plupart des termes)
3. **Correspondance partielle** (certains termes)

### Autres arrêts (dès 2000)
- Par référence de cause : « Autres arrêts dès 2000 » > saisir le numéro (ex. `2P.44/2001`)
- Par date : sélectionner les dates dans les masques
- Sans référence : mêmes opérateurs que ci-dessus. Cliquer « suite... » pour restreindre par cour et domaine juridique

---

## Section payante ⚠️ (abonnés)

### Accès
Page d'accueil > **« Recherche avancée pour abonnés »** > identifiants universitaires ou abonnement professionnel

### Trois types de recherche

#### 1. Recherche par répertoire

**Répertoire systématique (« Répertoire systématique 111-131ss »)**
- Structure miroir du RS (Recueil systématique)
- Naviguer dans l'arborescence pour trouver une loi
- Chercher toutes les décisions relatives à une disposition spécifique
- Résultats : résumés brefs + références
- Peut être combiné avec une recherche plein texte par mots-clés

**Répertoire alphabétique (« Répertoire alphabétique 111-131ss »)**
- Sélectionner un mot-clé dans la liste alphabétique
- Choisir les volumes à interroger

#### 2. Recherche experte standard

- Interroge les ATF et/ou les autres arrêts (dès 2000)
- Option « seulement le résumé » pour restreindre au chapeau
- **Recherche par référence législative** : saisir `art. 42 CO` (sans guillemets) → le système reconnaît automatiquement la référence et étend aux subdivisions (trouve aussi art. 42 al. 1 CO). Recherche trilingue.
- **Recherche CHLexML** (ATF depuis 1990+) : saisir une référence structurée comme `<CH/LPE/11>` pour l'art. 11 LPE → élimine les décisions qui ne citent la norme qu'en passant

#### 3. Recherche experte structurée

Six masques de recherche principaux (A à F) plus options complémentaires :
- Chaque masque accepte : termes, descripteurs Jurivoc, normes, références ATF, termes avec opérateurs booléens (AND, OR, ANDNOT)
- Pour chaque masque, choisir le type de champ via menu déroulant :
  - **« normes »** : références législatives
  - **« descripteurs »** : mots-clés Jurivoc
  - **« termes »** : correspondance exacte en plein texte
  - **« flexions »** : trouve singulier/pluriel
- **Champ distance** : distance maximale en mots entre deux termes liés par un opérateur
- Les masques A-F se combinent dans le champ **« combinaison de champs »**

---

## Outils supplémentaires (section payante ⚠️)

### Descripteurs
Après chaque requête, le système propose les **descripteurs Jurivoc** pertinents. Cliquer sur un descripteur pour chercher tous les ATF indexés avec lui depuis 1990. Multilingue. Cliquer `?` pour synonymes, antonymes et termes associés.

### Assistant de recherche
- Étend la requête avec des mots-clés supplémentaires (ATF uniquement)
- Traduit en allemand/italien (ATF uniquement)
- Tri par date

### Diagramme temps/pertinence
Affichage graphique combinant l'index de pertinence avec la chronologie. Les résultats en **haut à droite** sont les plus pertinents et les plus récents.

### Outils HTML (colonne de droite d'un arrêt)
| Outil | Fonction |
|-------|----------|
| **Commentaires** | Doctrine citant cet ATF |
| **Publications** | Revues ayant publié/traduit l'arrêt (JdT, SJ, etc.) |
| **Normes** | Dispositions législatives indexées (depuis 1990) |
| **Descripteurs** | Termes d'indexation Jurivoc |

> L'outil **« Publications »** est particulièrement utile pour trouver les traductions d'un ATF dans les revues romandes (JdT, SJ, RDAF).
