# Opérateurs de recherche — Référence complète

> ⚠️ **Swisslex** : Accès payant (universités/cabinets d'avocats)

## Swisslex — Opérateurs de proximité (avancés)

| Opérateur | Syntaxe | Exemple | Résultat |
|-----------|---------|---------|----------|
| Même paragraphe | `same` ou `same/1` | `bail same résiliation` | Les deux termes dans le même paragraphe |
| N paragraphes | `same/n` | `bail same/3 résiliation` | Termes dans un rayon de 3 paragraphes |
| N mots | `near/n` | `bail near/5 résiliation` | Termes dans un rayon de 5 mots (bidirectionnel) |
| Adjacent | `adj` | `droit adj préemption` | Mots adjacents (articles/prépositions ignorés) |
| Pas même paragraphe | `notsame` | `bail notsame commercial` | Termes pas dans le même paragraphe |

> `near` par défaut = `near/7` (7 mots de distance)

### Troncature

| Type | Syntaxe | Exemple | Résultat |
|------|---------|---------|----------|
| Postérieure | `mot*` | `constru*` | construction, construire, construit... |
| Antérieure | `*mot` | `*legitimation` | Aktivlegitimation, Passivlegitimation... |
| Intermédiaire | `mot*mot` | `Bau*verfahren` | Baubewilligungsverfahren... |

> **Important** : La troncature antérieure est **indispensable en allemand** pour les mots composés.

### Priorité des opérateurs
```
1. Parenthèses ( )
2. not
3. and (et espace)
4. or
```

### Exemples de requêtes complexes

**Recherche de jurisprudence sur la résiliation de bail** :
```
(locataire or preneur) same (résili* or cong*) not commercial
```

**Recherche bilingue sur le droit de la construction** :
```
(permis or autorisation or Baubewilligung) same (constru* or Bau*)
```

**Recherche par article de loi dans la jurisprudence** :
```
"art. 271" same "CO" same (résili* or cong* or Kündigung)
```

---

## Google — Opérateurs utiles pour le droit

| Opérateur | Syntaxe | Exemple |
|-----------|---------|---------|
| Domaine | `site:` | `"art. 271 CO" site:bger.ch` |
| Type fichier | `filetype:` | `"droit de préemption" filetype:pdf` |
| Titre | `intitle:` | `intitle:"recherche juridique"` |
| Expression | `"..."` | `"résiliation de bail"` |

### Combinaisons pratiques pour le droit suisse

**Chercher un article de loi sur le site du TF** :
```
"art. 41 CO" site:bger.ch
```

**Chercher de la doctrine en PDF** :
```
"responsabilité civile" "droit suisse" filetype:pdf
```

**Chercher sur un site cantonal** :
```
"plan d'affectation" site:ge.ch
```

---

## bger.ch (Tribunal fédéral) — Recherche gratuite

| Opérateur | Syntaxe | Exemple |
|-----------|---------|---------|
| ET | `+` | `+bail +résiliation` |
| SAUF | `-` | `+bail -commercial` |
| Expression | `"..."` | `"art. 271 CO"` |

### Limitations du mode gratuit
- Pas de troncature
- Pas de filtres par domaine, date, cour
- Pas de descripteurs Jurivoc
- Pour ces fonctions avancées → version payante ⚠️ ou Swisslex ⚠️
