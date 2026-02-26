---
name: techniques-recherche-juridique
description: "Techniques de recherche juridique : troncature (essentielle pour l'allemand), opérateurs de proximité, stratégie multilingue. Utiliser cette skill quand l'utilisateur a besoin de formuler une requête de recherche optimisée ou comprendre les spécificités de la recherche juridique suisse."
---

# Techniques de recherche juridique

## Spécificités de la recherche juridique suisse

### Le multilinguisme est obligatoire
Le droit suisse est rédigé en trois langues officielles qui font **toutes foi**. Une recherche sérieuse doit couvrir **au minimum FR et DE** car :
- La majorité de la doctrine est en allemand
- Le TF rédige dans la langue de la procédure (souvent DE)
- Les ATF ne sont **pas traduits** (seul le chapeau l'est)

→ Pour la traduction des termes : skill `terminologie-juridique-multilingue`

### La troncature est essentielle en allemand
L'allemand forme des mots composés. Sans troncature, on manque des résultats.

| Type | Syntaxe | Exemple | Résultat |
|------|---------|---------|----------|
| Postérieure | `mot*` | `constru*` | construction, construire, construit |
| **Antérieure** | `*mot` | `*legitimation` | Aktivlegitimation, Passivlegitimation |
| Intermédiaire | `mot*mot` | `Bau*verfahren` | Baubewilligungsverfahren |

> **Important** : la troncature ne fonctionne pas dans les moteurs de recherche web classiques. Elle nécessite des bases de données spécialisées (⚠️ Swisslex payant, bger.ch section payante).

---

## Opérateurs de proximité (bases spécialisées)

Ces opérateurs ne sont disponibles que dans les bases de données juridiques spécialisées (⚠️ Swisslex payant).

| Syntaxe | Effet |
|---------|-------|
| `same` | Termes dans le **même paragraphe** |
| `same/n` | Termes dans un rayon de **n paragraphes** |
| `near/n` | Termes dans un rayon de **n mots** |
| `adj` | Mots **adjacents** |

**Utilité** : quand une recherche par mots-clés retourne trop de résultats, les opérateurs de proximité permettent de cibler les passages où les concepts sont proches.

---

## Recherche sur bger.ch (gratuit)

Le moteur de recherche gratuit de bger.ch est limité :
- Guillemets `"..."` pour expression exacte
- Pas de troncature
- Pas d'opérateurs de proximité
- Résultats classés par pertinence

---

## Stratégie de formulation

1. **Qualifier** le problème juridique
2. **Identifier** les articles de loi potentiellement applicables
3. **Traduire** les termes clés en DE (et IT si pertinent) → skill `terminologie-juridique-multilingue`
4. **Utiliser la troncature** pour couvrir les variantes morphologiques
5. **Affiner** : si trop de résultats, ajouter des critères ; si pas assez, élargir

### Exemple pratique

Recherche sur la résiliation de bail :
1. Articles concernés : art. 271, 271a CO
2. Termes FR : résiliation, bail, abusif, congé
3. Termes DE : Kündigung, Miete, missbräuchlich
4. Recherche combinée (sur base payante) : `("art. 271" OR "art. 271a") AND (résili* OR Kündigung*)`
