# Pièges à Éviter - Swiss Legal Commentary

Pièges courants lors de la recherche de commentaires doctrinaux et comment les éviter.

## Pièges de Recherche

### 1. Aucun commentaire trouvé

**Symptôme** : La recherche retourne 0 résultat

**Causes possibles** :
- Article pas encore commenté sur la plateforme
- Loi non couverte actuellement
- Termes de recherche inadaptés
- Orthographe incorrecte

**Solutions** :
1. Vérifier orthographe (numéro article, nom loi)
2. Essayer variantes : "Art. 328" vs "328" vs "article 328"
3. Élargir à thème général plutôt qu'article spécifique
4. Rechercher articles connexes
5. Combiner avec `@swiss-case-law-research` pour jurisprudence
6. Mentionner explicitement la limite de couverture à l'utilisateur

**Conséquence si ignoré** : Utilisateur croit que le sujet n'est pas documenté alors que la plateforme a simplement une couverture partielle.

---

### 2. Commentaire uniquement en allemand

**Symptôme** : Résultats uniquement avec `language: "de"`

**Causes** :
- Tous les commentaires ne sont pas traduits
- Certains auteurs publient uniquement en allemand
- La version allemande est souvent publiée en premier

**Solutions** :
1. Mentionner clairement la langue disponible à l'utilisateur
2. Proposer traduction des concepts principaux
3. Rechercher si version autre langue existe (parfois publiée plus tard)
4. Expliquer le contenu en langue préférée de l'utilisateur

**Conséquence si ignoré** : Utilisateur francophone reçoit un lien vers contenu allemand sans explication.

---

### 3. Trop de résultats (>20)

**Symptôme** : Recherche thématique retourne des dizaines de commentaires

**Causes** :
- Termes de recherche trop généraux
- Thème transversal touchant plusieurs lois

**Solutions** :
1. Affiner avec `legislative_act` pour cibler une loi
2. Ajouter termes plus spécifiques
3. Filtrer par langue si pas déjà fait
4. Limiter présentation aux 3-5 plus pertinents (récents, auteurs reconnus)

**Conséquence si ignoré** : Surcharge d'information, utilisateur perdu dans les résultats.

---

### 4. Confondre articles de différentes lois

**Symptôme** : Résultats mélangent Art. 328 CO et Art. 328 CC par exemple

**Causes** :
- Plusieurs lois peuvent avoir le même numéro d'article
- Recherche par numéro seul sans contexte

**Solutions** :
1. Toujours ajouter le nom ou code de la loi : "328 CO" ou "328 Code Obligations"
2. Utiliser le filtre `legislative_act` si disponible
3. Vérifier la loi dans les résultats avant de présenter

**Conséquence si ignoré** : Présenter un commentaire sur le mauvais article de loi, information juridiquement incorrecte.

---

## Pièges de Contenu

### 5. Commentaire ancien non mis à jour

**Symptôme** : Date de publication ancienne (>3 ans)

**Risques** :
- Changement législatif depuis publication
- Nouvelle jurisprudence non intégrée
- Position doctrinale peut avoir évolué

**Solutions** :
1. Toujours mentionner la date de publication
2. Vérifier s'il y a mise à jour récente (champ date)
3. Compléter avec jurisprudence récente via `@swiss-case-law-research`
4. Noter si changement législatif depuis publication
5. Avertir que doctrine plus récente peut exister

**Conséquence si ignoré** : Fournir information potentiellement obsolète comme si elle était actuelle.

---

### 6. Commentaire en cours de rédaction

**Symptôme** : Contenu incomplet ou indication "draft"

**Solutions** :
1. Vérifier date de publication et complétude
2. Mentionner si commentaire récent (peut évoluer)
3. Croiser avec autres commentaires si disponibles
4. Compléter avec jurisprudence

**Conséquence si ignoré** : Présenter analyse incomplète comme définitive.

---

### 7. Commentaire très technique pour non-juriste

**Symptôme** : Utilisateur non-juriste ne comprend pas le jargon

**Solutions** :
1. Vulgariser les concepts principaux
2. Fournir exemples concrets d'application
3. Structurer par questions-réponses simples
4. Mettre en évidence l'essentiel pour un non-juriste
5. Recommander consultation professionnelle si cas complexe

**Conséquence si ignoré** : Utilisateur frustré, information inutilisable.

---

## Pièges Méthodologiques

### 8. Se limiter à un seul commentaire

**Symptôme** : Présenter un seul point de vue doctrinal

**Risques** :
- Positions doctrinales peuvent varier
- Vision partielle du débat juridique
- Manquer nuances importantes

**Solutions** :
1. Toujours rechercher 2-3 commentaires si disponibles
2. Comparer les positions des auteurs
3. Mentionner si consensus ou débat
4. Indiquer auteurs de référence dans le domaine

**Conséquence si ignoré** : Présenter une opinion comme consensus alors qu'il y a débat doctrinal.

---

### 9. Ignorer les références du commentaire

**Symptôme** : Ne pas explorer la jurisprudence et doctrine citées

**Opportunités manquées** :
- Arrêts clés du Tribunal fédéral
- Ouvrages de référence
- Vision pratique via jurisprudence

**Solutions** :
1. Toujours noter les ATF/BGE cités
2. Proposer recherche via `@swiss-case-law-research`
3. Mentionner doctrine complémentaire si pertinent

**Conséquence si ignoré** : Analyse doctrinale isolée, sans ancrage jurisprudentiel.

---

### 10. Négliger les articles connexes

**Symptôme** : Ne pas explorer les `related_articles` du commentaire

**Opportunités manquées** :
- Vision systématique de la loi
- Cohérence d'interprétation
- Articles complémentaires importants

**Solutions** :
1. Vérifier le champ `related_articles` dans la réponse
2. Mentionner articles connexes pertinents
3. Proposer exploration si utilisateur intéressé

**Conséquence si ignoré** : Vision fragmentaire du cadre juridique.

---

## Pièges de Présentation

### 11. Ne pas citer correctement

**Symptôme** : Omission d'informations de citation

**Exigences** :
- Auteur(s) complet(s)
- Titre du commentaire
- Date de publication/mise à jour
- Lien vers onlinekommentar.ch

**Conséquence si ignoré** : Utilisateur ne peut pas retrouver la source, problème de crédibilité académique.

---

### 12. Substituer le commentaire à un conseil juridique

**Symptôme** : Présenter le commentaire comme conseil définitif pour un cas concret

**Rappel** :
- Commentaire = ressource académique, pas conseil
- Cas concret = nécessite consultation avocat
- Responsabilité limitée de la plateforme

**Solution** : Toujours inclure avertissement pour cas concrets.

**Conséquence si ignoré** : Risque juridique si utilisateur applique doctrine sans conseil professionnel.

---

## Checklist Anti-Pièges

Avant de présenter des résultats :

- [ ] Vérifier que l'article est le bon (bonne loi)
- [ ] Vérifier la date du commentaire
- [ ] Mentionner la langue disponible
- [ ] Comparer 2-3 sources si possible
- [ ] Noter les références jurisprudentielles
- [ ] Citer correctement (auteur, titre, date, lien)
- [ ] Vulgariser si utilisateur non-juriste
- [ ] Inclure avertissement si cas concret
- [ ] Proposer approfondissements (articles connexes, jurisprudence)
