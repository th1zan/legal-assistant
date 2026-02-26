# Swisslex — Guide pratique détaillé

> ⚠️ **Accès payant** : Swisslex nécessite un abonnement (disponible via universités suisses ou cabinets d'avocats).

## Opérateurs et logique de recherche

### Opérateurs booléens de base
- `and` ou espace entre mots = ET (opérateur par défaut)
- `or` = OU
- `not` = SAUF (ex. `permis not construire`)

### Opérateurs de proximité avancés
| Opérateur | Effet | Exemple |
|-----------|-------|---------|
| `"..."` | Expression exacte (désactiver le thésaurus) | `"droit de préemption"` |
| `same/1` ou `same` | Termes dans le même paragraphe | `bail same résiliation` |
| `same/n` | Termes dans un rayon de n paragraphes | `bail same/3 résiliation` |
| `near/n` | Termes dans un rayon de n mots (défaut : 7, bidirectionnel) | `bail near/5 résiliation` |
| `adj` | Mots adjacents (articles/prép. non comptés) | `bau adj bewilligung` |
| `notsame` | Termes PAS dans le même paragraphe | `bail notsame commercial` |

> Pour `near/n` : articles, prépositions et conjugaisons ne sont PAS comptés.

### Priorité des opérateurs
```
parenthèses > not > and > or
```
**Piège fréquent** :
- `autorisation or permis and construire` = `autorisation or (permis and construire)` ✗
- `(autorisation or permis) and construire` ✓

### Troncature
Le thésaurus doit être **désactivé** pour que la troncature fonctionne.

| Type | Syntaxe | Exemple | Résultat |
|------|---------|---------|----------|
| Postérieure | `mot*` | `constru*` | construire, construction, constructible |
| Antérieure | `*mot` | `*legitimation` | Baulegitimation, Beschwerdelegitimation |
| Intermédiaire | `mot*mot` | `Bau*verfahren` | Baubewilligungsverfahren |

> La troncature antérieure est **indispensable en allemand** pour les mots composés.

---

## Thésaurus de droit suisse

- Plus de 300'000 entrées
- Propose traductions, synonymes et termes associés
- Quand activé : `bail` → cherche aussi `location`, `loyer`, `contrat de bail`
- Pour une recherche littérale → décocher le thésaurus (mettre à « Non »)
- Avec le thésaurus actif, les expressions entre guillemets sont recherchées avec flexions, pluriels et déclinaisons

---

## Recherche de législation fédérale

1. Aller dans **« Consulter des documents »** > **« Législation fédérale »**
2. Dans le masque « Loi », saisir le numéro RS ou l'abréviation officielle
3. Optionnellement ajouter un numéro d'article
4. Swisslex propose une liste déroulante de suggestions

---

## Recherche de jurisprudence

### Trouver un ATF connu
- **Méthode 1** : « Consulter des documents » > « Jurisprudence » : saisir le type de document (ex. ATF II) dans « abréviation », l'année dans « Année/Vol. », la page dans le champ approprié
- **Méthode 2** (plus rapide) : onglet « Recherche avancée » > masque « Référence » (ex. `ATF 128 II 1` ou `JdT 2008 I 602`)
- Pour les arrêts non publiés : utiliser le champ « N° de dossier »

> **Important** : trier les résultats par pertinence (« Trier par » dans la colonne de droite)

### Recherche croisée par référence
Recherche dans l'ensemble du corpus (y compris jurisprudence cantonale et doctrine) :
- Par article de loi : `art. 42 CO`
- Par numéro RS
- Par mots du titre d'une loi
- Par référence jurisprudentielle : `ATF 126 II 7`, `SJ 2002 II 206`
- Par référence bibliographique : `Aemisegger RPG 25a`

### Délimiter le corpus
- **Par date** : année, mois+année, ou date complète ; date unique ou plage
- **Recherche avancée** : filtres par publications, types de documents (arrêts, commentaires, articles, etc.), cantons, domaines juridiques

### Classement des résultats
- Tri chronologique (défaut) ou par **pertinence**
- Critères de pertinence : variété des termes, rareté des termes, fréquence du même terme, proximité des termes dans le document

### Affiner les résultats
- Filtrer par type de document : commentaires d'arrêt, arrêts, articles, livres, commentaires, documents officiels
- Filtrer par langue : DE, FR, IT, EN, RM

---

## Tableau de concordance dynamique

Utiliser Swisslex pour trouver les traductions d'ATF dans les revues (JdT, SJ, etc.) :
1. Saisir la référence ATF dans le masque de recherche principal
2. Pour les arrêts post-2002 : combiner référence ATF et numéro de cause avec `or` (ex. `ATF 129 II 1 OR 2A.313/2002`)
3. Si trop de résultats → « Recherche avancée » pour filtrer par publication et type de document

---

## Méthode analogique dans Swisslex

Lors de la consultation d'un ATF, la colonne de droite affiche :
- **« Références citées »** : arrêts et textes cités dans l'ATF (recherche rétroprogressive)
- **« Document cité dans »** : documents ultérieurs citant cet ATF (recherche progressive)

→ Essentiel pour suivre l'évolution d'une jurisprudence.

---

## Recherche de doctrine

### Trois modes d'accès
1. **Par liste de publications** : « Liste des publications » > « Revues » ou « Livre/Commentaire »
2. **Par titre** : « Consulter un document » > « Revues »/« Livres »/« Commentaires » par mot-clé ou auteur
3. **Par recherche avancée** : cocher uniquement « commentaires » et « articles/livres » dans le filtre par type de document

### Revues actuelles
Les revues de l'année en cours sont accessibles via « Revues actuelles » (table des matières). Les numéros antérieurs nécessitent une recherche par mot-clé ou par référence.

---

## Recherche thématique

- Swisslex structure sa base par **15+ domaines juridiques** (droit public, code civil, droit des obligations, etc.)
- Utiliser « Recherche avancée » > « Filtrer par domaines du droit » + « Filtrer par type de document » > « arrêts »

---

## Alertes et newsletters Swisslex

1. Effectuer une recherche
2. Dans la colonne de droite, sous « Mon critère de recherche », cliquer sur **« Enregistrer cette recherche en tant que newsletter »**
3. Configurer : filtres additionnels, fréquence, jour d'envoi
