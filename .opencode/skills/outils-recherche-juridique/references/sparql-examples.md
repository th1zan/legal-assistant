# Exemples de requêtes SPARQL pour Fedlex

Endpoint : `https://fedlex.data.admin.ch/sparqlendpoint`

## Préfixes communs

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX eli: <http://data.europa.eu/eli/ontology#>
```

## 1. Rechercher une loi par numéro RS

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?act ?title ?dateInForce WHERE {
  ?act a jolux:ConsolidationAbstract ;
       skos:prefLabel ?title ;
       jolux:dateEntryInForce ?dateInForce ;
       jolux:classifiedByTaxonomyEntry ?taxonomy .
  
  # Filtrer par numéro RS (ex: 210 = Code civil)
  FILTER(CONTAINS(STR(?taxonomy), "/210"))
  FILTER(LANG(?title) = "fr")
}
LIMIT 10
```

## 2. Rechercher une loi par titre

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?act ?title ?sr WHERE {
  ?act a jolux:ConsolidationAbstract ;
       skos:prefLabel ?title ;
       jolux:classifiedByTaxonomyEntry ?sr .
  
  # Recherche par mots-clés (insensible à la casse)
  FILTER(CONTAINS(LCASE(?title), "protection des données"))
  FILTER(LANG(?title) = "fr")
}
ORDER BY ?title
LIMIT 20
```

## 3. Obtenir les métadonnées d'une loi

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dcterms: <http://purl.org/dc/terms/>

SELECT ?title ?dateAdoption ?dateInForce ?abbreviation WHERE {
  <https://fedlex.data.admin.ch/eli/cc/24/233_245_233> 
       skos:prefLabel ?title ;
       jolux:dateDocument ?dateAdoption ;
       jolux:dateEntryInForce ?dateInForce .
  
  OPTIONAL { ?act skos:altLabel ?abbreviation . }
  
  FILTER(LANG(?title) = "fr")
}
```

## 4. Lister les versions historiques

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX eli: <http://data.europa.eu/eli/ontology#>

SELECT ?version ?dateApplicable WHERE {
  <https://fedlex.data.admin.ch/eli/cc/24/233_245_233> 
       jolux:isRealizedBy ?version .
  
  ?version eli:date_applicability ?dateApplicable .
}
ORDER BY DESC(?dateApplicable)
LIMIT 50
```

## 5. Rechercher des ordonnances d'une loi

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?ordonnance ?title WHERE {
  ?ordonnance a jolux:ConsolidationAbstract ;
              skos:prefLabel ?title ;
              jolux:legalResourceSubdivisionType <http://data.legilux.public.lu/resource/authority/subdivision-type/ordonnance> .
  
  # Lien avec la loi mère
  ?ordonnance jolux:isBasedOnTreatyLegalResource <https://fedlex.data.admin.ch/eli/cc/24/233_245_233> .
  
  FILTER(LANG(?title) = "fr")
}
```

## 6. Rechercher dans la Feuille fédérale (FF)

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?doc ?title ?date WHERE {
  ?doc a jolux:Act ;
       skos:prefLabel ?title ;
       jolux:dateDocument ?date ;
       jolux:publicationReference ?pubRef .
  
  # Filtrer par Feuille fédérale
  FILTER(CONTAINS(STR(?pubRef), "BBl"))
  
  # Recherche par mots-clés
  FILTER(CONTAINS(LCASE(?title), "message"))
  FILTER(LANG(?title) = "fr")
}
ORDER BY DESC(?date)
LIMIT 20
```

## 7. Obtenir les URLs de téléchargement

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX eli: <http://data.europa.eu/eli/ontology#>

SELECT ?format ?url WHERE {
  <https://fedlex.data.admin.ch/eli/cc/24/233_245_233/fr>
       eli:is_embodied_by ?manifestation .
  
  ?manifestation eli:format ?format ;
                 eli:uri_schema ?url .
}
```

## URLs directes de téléchargement

Pour télécharger directement sans SPARQL :

| Format | Pattern URL |
|--------|-------------|
| PDF | `https://www.fedlex.admin.ch/eli/cc/{rs}/{lang}/pdf-a` |
| HTML | `https://www.fedlex.admin.ch/eli/cc/{rs}/{lang}/html` |
| DOCX | `https://www.fedlex.admin.ch/eli/cc/{rs}/{lang}/docx` |
| XML | `https://www.fedlex.admin.ch/eli/cc/{rs}/{lang}/xml` |

**Exemples** :
- Code civil (PDF, FR) : `https://www.fedlex.admin.ch/eli/cc/24/233_245_233/fr/pdf-a`
- CO (HTML, DE) : `https://www.fedlex.admin.ch/eli/cc/27/317_321_377/de/html`

## Outils pour tester

- **Yasgui** : https://yasgui.triply.cc (coller le endpoint Fedlex)
- **curl** : 
  ```bash
  curl -X POST https://fedlex.data.admin.ch/sparqlendpoint \
       -H "Accept: application/sparql-results+json" \
       -d "query=SELECT * WHERE { ?s ?p ?o } LIMIT 10"
  ```
