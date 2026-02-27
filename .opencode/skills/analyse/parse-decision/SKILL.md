---
name: parse-decision
description: Parse les décisions de justice suisses (TF, TAF, TPF) récupérées via Entscheidsuche et extrait les sections structurées (Faits, Droit, Considérants, Dispositif). Utiliser cette skill quand l'utilisateur fournit une signature Entscheidsuche et veut analyser le contenu structuré d'un arrêt, extraire les faits ou le raisonnement juridique.
---

# Skill : Analyse de Décisions de Justice

**Type** : Skill d'analyse atomique  
**Domaine** : Analyse de documents juridiques  
**Entrée** : Décision de justice suisse (HTML, JSON ou PDF depuis Entscheidsuche)  
**Sortie** : Sections structurées extraites de la décision  
**Dépendances** : Serveur MCP Entscheidsuche

---

## Objectif

Parser les décisions de justice suisses récupérées via Entscheidsuche et extraire les sections structurées pour utilisation dans la génération de documents juridiques.

**Capacités principales** :
- Extraire les sections standards : Faits, Droit, Considérants, Dispositif
- Gérer les formats multiples (HTML du TF, PDF du TAF/BVGE en fallback)
- Préserver les références de citation et le formatage
- Extraire les métadonnées (date, signature, tribunal, chambre, juges)

---

## Quand Utiliser Cette Skill

**Déclencher cette skill quand** :
- L'utilisateur demande de « parser une décision »
- L'utilisateur fournit une signature Entscheidsuche et veut le contenu structuré
- Construction d'un document juridique référençant une décision
- Besoin d'extraire les faits ou le raisonnement juridique d'un arrêt

**Exemples de déclencheurs** :
- « Parse l'ATF 148 III 217 »
- « Extrais les faits de la décision 7B_529/2025 »
- « Quels sont les considérants de cet arrêt ? »
- « Analyse la structure de ce jugement »

---

## Exigences d'Entrée

Cette skill requiert **l'une des options suivantes** :

### Option 1 : Signature Entscheidsuche
```
Format : CH_BGer_007_7B-529-2025_2026-01-26
Codes tribunaux : CH_BGer (TF), CH_BVGE (TAF), CH_BstGer (TPF)
```

### Option 2 : HTML/JSON Déjà Récupéré
```
Contenu HTML direct depuis le MCP Entscheidsuche
OU
Métadonnées JSON avec HTML intégré
```

### Option 3 : Citation Suisse Standard
```
ATF 148 III 217
ATAF 2024-IV-1
TPF 2025 5
```

---

## Format de Sortie

Retourne un objet structuré avec les sections extraites :

```json
{
  "metadonnees": {
    "signature": "CH_BGer_007_7B-529-2025_2026-01-26",
    "citation": "7B_529/2025 du 26 janvier 2026",
    "tribunal": "Tribunal fédéral",
    "chambre": "IIe Cour de droit pénal",
    "date": "2026-01-26",
    "juges": ["Président: Juge fédéral A.", "..."],
    "langue": "fr"
  },
  "sections": {
    "faits": {
      "html_brut": "<div>...</div>",
      "texte": "Les faits pertinents sont les suivants...",
      "sous_sections": ["A. Faits de la cause", "B. Procédure"]
    },
    "droit": {
      "html_brut": "<div>...</div>",
      "texte": "En droit:\n\n1. Le recours...",
      "sous_sections": ["1. Recevabilité", "2. Fond"]
    },
    "considerants": {
      "html_brut": "<div>...</div>",
      "texte": "Considérant en droit:\n\n1.1 ...",
      "elements_numerotes": [
        {"numero": "1.1", "texte": "..."},
        {"numero": "1.2", "texte": "..."}
      ]
    },
    "dispositif": {
      "html_brut": "<div>...</div>",
      "texte": "Par ces motifs, le Tribunal fédéral prononce:\n\n1. Le recours est admis.",
      "decisions": [
        "Le recours est admis.",
        "L'arrêt attaqué est annulé."
      ]
    }
  },
  "references": {
    "legislatives": ["art. 97 al. 1 LTF", "art. 641 CC"],
    "jurisprudence": ["ATF 148 III 217", "ATF 147 I 73"],
    "doctrine": []
  },
  "format": "html",
  "problemes_parsing": []
}
```

---

## Workflow

### Étape 1 : Récupérer la Décision (si nécessaire)

Si seule une signature ou citation est fournie, récupérer d'abord le document complet :

```python
# Utiliser le MCP Entscheidsuche
resultat = entscheidsuche_get_document(
    signature="CH_BGer_007_7B-529-2025_2026-01-26",
    format="html"  # Préférer HTML pour le parsing structuré
)
```

**Stratégie de fallback** :
- Si HTML indisponible (`has_html: false`), demander les métadonnées JSON d'abord
- Si HTML toujours indisponible, demander le PDF et noter la limitation

### Étape 2 : Parser la Structure HTML

Utiliser le script utilitaire pour extraire les sections :

```bash
python .opencode/skills/analyse/parse-decision/scripts/parse_decision.py \
    --input decision.html \
    --format html \
    --output structure.json
```

### Étape 3 : Extraire les Métadonnées

Depuis le HTML ou JSON, extraire :
- Informations tribunal et chambre
- Date et signature
- Composition du tribunal (juges)
- Langue (fr/de/it)

### Étape 4 : Identifier les Sections

**Structure standard TF** (Français) :
- **En fait** ou **Faits** → Section des faits
- **En droit** ou **Droit** → Section du cadre juridique
- **Considérant en droit** ou **Considérants** → Raisonnement juridique
- **Par ces motifs** ou **Dispositif** → Décision/Jugement

**Structure standard TF** (Allemand) :
- **Sachverhalt** → Faits
- **Rechtliche Würdigung** → Appréciation juridique
- **Erwägungen** → Considérants
- **Demnach erkennt** → Dispositif

**Structure standard TF** (Italien) :
- **In fatto** → Faits
- **In diritto** → Cadre juridique
- **Considerando in diritto** → Raisonnement juridique
- **Per questi motivi** → Dispositif

### Étape 5 : Extraire les Références

Scanner le texte pour :
- **Références législatives** : Pattern regex `art\.?\s+\d+.*?[A-Z]{2,}`
- **Références jurisprudentielles** : `ATF \d+`, `ATAF \d+`, `\d+[A-Z]_\d+/\d+`
- **Références doctrinales** : Noms d'auteurs + patterns d'année

### Étape 6 : Structurer la Sortie

Retourner l'objet JSON structuré avec toutes les informations extraites.

---

## Cas Limites et Limitations

### Problèmes Connus

1. **Format PDF** : Les décisions TAF/BVGE peuvent retourner du PDF au lieu de HTML
   - **Mitigation** : Parser les métadonnées JSON d'abord, extraire le texte brut si disponible
   - **Futur** : Ajouter l'extraction de texte PDF avec `pdfplumber`

2. **Décisions multilingues** : Certaines décisions contiennent des langues mixtes
   - **Mitigation** : Détecter la langue principale, noter les langues secondaires
   - **Sortie** : Inclure `langue: "fr/de"` dans les métadonnées

3. **Structure complexe** : Certaines décisions ont des sections non standard
   - **Mitigation** : Utiliser une détection flexible avec patterns de fallback
   - **Sortie** : Inclure `problemes_parsing: [...]` pour revue manuelle

4. **Grandes décisions** : Certains ATF sont très longs (>100 pages)
   - **Mitigation** : Extraire le résumé/sections clés d'abord
   - **Performance** : Parsing en streaming pour les grands documents

### Validation

Après parsing, valider :
- Au moins une section majeure extraite (Faits OU Droit OU Dispositif)
- Métadonnées incluent signature et date
- Pas de sections tronquées (vérifier HTML complet)
- Langue détectée correctement

---

## Intégration avec Autres Skills

Cette skill est conçue pour être **composable** avec d'autres skills :

### Skills Amont (Fournissent l'Entrée)
- `@mcp/swiss-case-law-research` → Rechercher et récupérer des décisions
- `@recherche/recherche-juridique-suisse` → Naviguer vers la recherche jurisprudentielle

### Skills Aval (Utilisent la Sortie)
- `@analyse/citation-formatter` → Formater les citations depuis les métadonnées extraites
- `@analyse/recours-tf` → Utiliser les faits/considérants dans la génération de recours
- `@redaction/avis-de-droit` → Utiliser le raisonnement juridique dans les avis
- `@analyse/extract-facts` → Analyser plus en détail la section des faits

---

## Critères de Succès

Cette skill est réussie si :

1. Extrait Faits, Droit, Considérants, Dispositif de 90%+ des décisions TF HTML
2. Gère les trois langues officielles (FR/DE/IT)
3. Dégradation gracieuse pour les décisions PDF-only (extraire métadonnées minimum)
4. Complète le parsing en < 500ms pour les décisions typiques
5. Fournit des messages d'erreur clairs pour les cas limites
6. Le format de sortie est consommable par les skills aval

---

## Références

- **MCP Entscheidsuche** : `.opencode/skills/mcp/swiss-case-law-research/SKILL.md`
- **Standards de Citation** : `.opencode/skills/recherche/citation-juridique-suisse/SKILL.md`
- **Spec Projet** : `PROJECT.md`

---

## Métadonnées

```yaml
nom_skill: parse-decision
type_skill: atomique
domaine: analyse
version: 1.0.0
cree: 2026-02-26
dependances:
  - Serveur MCP Entscheidsuche
  - BeautifulSoup4 (package Python)
  - lxml (package Python)
sorties_pour:
  - citation-formatter
  - extract-facts
  - recours-tf
  - avis-de-droit
statut: en_developpement
priorite: P0
```
