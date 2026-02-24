---
name: bases-donnees-juridiques
description: "Guide des bases de données juridiques suisses : Fedlex, bger.ch (Tribunal fédéral), Lexfind, Swisslex. Utiliser cette skill quand l'utilisateur veut savoir quelle base de données utiliser ou comprendre les différences entre bases gratuites et payantes."
---

# Bases de données juridiques suisses

## Vue d'ensemble

| Base | Accès | Contenu principal |
|------|-------|-------------------|
| **Fedlex** | Gratuit | RS, RO, FF (textes officiels) — fedlex.admin.ch |
| **bger.ch** | Gratuit | Arrêts TF (ATF depuis 1954, tous depuis 2000) |
| **Lexfind** | Gratuit | Portail vers législation fédérale et cantonale — lexfind.ch |
| **Swisslex** | ⚠️ Payant | Législation + jurisprudence + doctrine — swisslex.ch |
| **Weblaw/Jusletter** | Mixte | Actualités juridiques, newsletters — weblaw.ch |

> **Note** : Les anciennes URLs admin.ch/rs, admin.ch/ro, admin.ch/ff redirigent désormais vers **Fedlex** (fedlex.admin.ch), la plateforme de publication officielle depuis 2021.

---

## Fedlex — Plateforme officielle

**URL** : fedlex.admin.ch

### Recueil systématique (RS)
- Navigation par table des matières décimale ou recherche
- Chaque loi : texte HTML, PDF, historique des modifications, texte original
- Classification : 1 (État), 2 (Droit privé), 3 (Droit pénal), etc.

### Recueil officiel (RO)
- Consultation chronologique
- **Seule version faisant foi** (art. 9 al. 1 LPubl)

### Feuille fédérale (FF)
- Messages du Conseil fédéral, projets, résultats de votation

---

## bger.ch — Tribunal fédéral

**URL** : bger.ch

### Recherche gratuite
- Recherche plein texte dans les ATF (depuis 1954) et tous les arrêts (depuis 2000)
- Recherche par **référence ATF** : `ATF 118 II 91`
- Recherche par **numéro de cause** : `4A_31/2023`
- Résultats classés par pertinence

### ⚠️ Recherche avancée (accès institutionnel payant)
- Descripteurs **Jurivoc** (thésaurus trilingue FR/DE/IT)
- Recherche structurée par champs (cour, date, domaine, langue)
- Recherche dans le **répertoire** (index systématique)
- Fonction « cité par » pour la recherche progressive

> Pour les juristes ayant accès : voir `references/bger-ch-guide.md`

---

## Lexfind

**URL** : lexfind.ch

Portail renvoyant vers les recueils systématiques fédéraux et cantonaux. Utile pour :
- Accéder rapidement à la **législation cantonale** de tous les cantons
- Comparer les législations entre cantons

---

## ⚠️ Swisslex (accès payant uniquement)

**Accès** : Abonnement payant (disponible via certaines universités et études d'avocats)

Swisslex est la base de données juridique suisse la plus complète, mais elle n'est pas accessible gratuitement. Elle offre :
- **Législation** : fédérale + cantonale, avec versions historiques
- **Jurisprudence** : TF, TAF, TPF, cantons (depuis 1987)
- **Doctrine** : articles de revues, résumés
- **Thésaurus** : enrichissement automatique des requêtes
- **Fonction « Document cité dans »** : recherche progressive (trouver les arrêts ultérieurs citant un arrêt donné)

> Pour les juristes ayant accès : voir `references/swisslex-walkthrough.md`

---

## Choix de la base selon le besoin

| Besoin | Base recommandée |
|--------|-----------------|
| Texte de loi fédérale en vigueur | **Fedlex** (gratuit) |
| Version historique d'une loi | Fedlex (RO) |
| Arrêt récent du TF | **bger.ch** (gratuit) |
| Législation cantonale | **Lexfind** (gratuit) → liens vers sites cantonaux |
| Recherche avancée jurisprudence | Swisslex ⚠️ payant |
| Doctrine (articles de revues) | Swisslex ⚠️ payant |
| Travaux préparatoires | Fedlex (FF) + parlement.ch |
