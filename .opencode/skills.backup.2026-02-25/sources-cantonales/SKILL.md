---
name: sources-cantonales
description: "Recherche de législation et droit cantonal suisse : les 26 recueils systématiques cantonaux, droit communal, concordats intercantonaux, travaux préparatoires cantonaux. Utiliser cette skill quand l'utilisateur cherche une loi cantonale, un concordat, du droit communal, ou des travaux préparatoires d'un canton suisse."
---

# Sources cantonales suisses

Cette skill couvre **tout le droit infra-fédéral** : législation cantonale, concordats intercantonaux, et droit communal.

> **Accès technique** : Pour les outils d'accès (MCP, CLI, APIs), voir `@outils-recherche-juridique`.

## Structure du droit infra-fédéral

```
Droit infra-fédéral suisse
├── Droit intercantonal (concordats)
│   └── Accords entre cantons (art. 48 Cst.)
├── Droit cantonal (26 cantons)
│   ├── Constitution cantonale
│   ├── Lois cantonales
│   └── Ordonnances (décrets, règlements)
└── Droit communal
    └── Règlements communaux
```

**Hiérarchie** : Droit fédéral > Concordats > Droit cantonal > Droit communal

---

## Vue d'ensemble des 26 cantons

### Suisse romande (6 cantons)

| Canton | Abrév. | Recueil systématique | Jurisprudence (entscheidsuche) |
|--------|--------|---------------------|-------------------------------|
| **Genève** | GE | [silgeneve.ch/legis](https://silgeneve.ch/legis) | `CH_GE_Cour` |
| **Vaud** | VD | [rsv.vd.ch](https://www.rsv.vd.ch) | `CH_VD_TC` |
| **Neuchâtel** | NE | [rsn.ne.ch](https://rsn.ne.ch) | `CH_NE_TC` |
| **Fribourg** | FR | [bdlf.fr.ch](https://bdlf.fr.ch) | `CH_FR_TC` |
| **Jura** | JU | [rsju.jura.ch](https://rsju.jura.ch) | `CH_JU_TC` |
| **Valais** | VS | [lex.vs.ch](https://lex.vs.ch) | `CH_VS_TC` |

### Suisse alémanique (19 cantons)

| Canton | Abrév. | Recueil systématique | Jurisprudence (entscheidsuche) |
|--------|--------|---------------------|-------------------------------|
| **Zürich** | ZH | [zh.ch/zhlex](https://www.zh.ch/de/politik-staat/gesetze-beschluesse/gesetzessammlung.html) | `CH_ZH_Obergericht` |
| **Bern** | BE | [belex.sites.be.ch](https://www.belex.sites.be.ch) | `CH_BE_Obergericht` |
| **Luzern** | LU | [srl.lu.ch](https://srl.lu.ch) | `CH_LU_Obergericht` |
| **Uri** | UR | [ur.lexspider.com](https://ur.lexspider.com) | `CH_UR_Obergericht` |
| **Schwyz** | SZ | [sz.ch](https://www.sz.ch/behoerden/gesetzessammlung.html/72-512-468) | `CH_SZ_Kantonsgericht` |
| **Obwalden** | OW | [gdb.ow.ch](https://gdb.ow.ch) | `CH_OW_Obergericht` |
| **Nidwalden** | NW | [gesetzessammlung.nw.ch](https://www.gesetzessammlung.nw.ch) | `CH_NW_Obergericht` |
| **Glarus** | GL | [gs.gl.ch](https://gs.gl.ch) | `CH_GL_Obergericht` |
| **Zug** | ZG | [bgs.zg.ch](https://bgs.zg.ch) | `CH_ZG_Verwaltungsgericht` |
| **Solothurn** | SO | [bgs.so.ch](https://bgs.so.ch) | `CH_SO_Obergericht` |
| **Basel-Stadt** | BS | [gesetzessammlung.bs.ch](https://www.gesetzessammlung.bs.ch) | `CH_BS_Appellationsgericht` |
| **Basel-Landschaft** | BL | [bl.clex.ch](https://bl.clex.ch) | `CH_BL_Kantonsgericht` |
| **Schaffhausen** | SH | [rechtsbuch.sh.ch](https://rechtsbuch.sh.ch) | `CH_SH_Obergericht` |
| **Appenzell A.Rh.** | AR | [bgs.ar.ch](https://www.bgs.ar.ch) | `CH_AR_Obergericht` |
| **Appenzell I.Rh.** | AI | [ai.clex.ch](https://ai.clex.ch) | `CH_AI_Kantonsgericht` |
| **St. Gallen** | SG | [gesetzessammlung.sg.ch](https://www.gesetzessammlung.sg.ch) | `CH_SG_Kantonsgericht` |
| **Graubünden** | GR | [gr-lex.gr.ch](https://www.gr-lex.gr.ch) | `CH_GR_Kantonsgericht` |
| **Aargau** | AG | [gesetzessammlungen.ag.ch](https://gesetzessammlungen.ag.ch) | `CH_AG_Obergericht` |
| **Thurgau** | TG | [rechtsbuch.tg.ch](https://rechtsbuch.tg.ch) | `CH_TG_Obergericht` |

### Suisse italienne (1 canton)

| Canton | Abrév. | Recueil systématique | Jurisprudence (entscheidsuche) |
|--------|--------|---------------------|-------------------------------|
| **Ticino** | TI | [ti.ch/RLeggi](https://www3.ti.ch/CAN/RLeggi/) | `CH_TI_Tribunale` |

---

## Accès technique par canton

Pour chaque canton, voici les méthodes d'accès disponibles :

| Canton | Législation | Jurisprudence | Travaux prép. | Priorité |
|--------|-------------|---------------|---------------|----------|
| **GE** | Web (silgeneve) | MCP `@entscheidsuche` | Web (Mémorial) | MCP/Web |
| **VD** | Web (rsv.vd.ch) | MCP `@entscheidsuche` | Web (gc.vd.ch) | MCP/Web |
| **ZH** | Web + OGD | MCP `@entscheidsuche` | Web | MCP/API |
| **BE** | Web (belex) | MCP `@entscheidsuche` | Web | MCP/Web |
| *Autres* | Web | MCP `@entscheidsuche` | Web (si dispo) | MCP/Web |

> **Note** : Tous les cantons sont indexés dans `entscheidsuche.ch` pour la jurisprudence.

---

## Cantons romands — Détails

### Genève (GE)

**Législation** :
- **Recueil systématique** : [silgeneve.ch/legis](https://silgeneve.ch/legis)
- Classification par domaine juridique
- Versions consolidées

**Travaux préparatoires** :
- **Mémorial du Grand Conseil** : [ge.ch/grandconseil/memorial](https://www.ge.ch/grandconseil/memorial)
  - Archives numérisées depuis **1901**
  - Recherche plein texte disponible
- **Projets de loi** : publiés avec exposé des motifs
- **Rapports de commissions** : analyses avant le vote

**Jurisprudence** :
- MCP `@entscheidsuche` avec spider `CH_GE_Cour`
- Revue : Semaine Judiciaire (SJ), RDAF

→ Détails : `references/par-canton/geneve.md`

---

### Vaud (VD)

**Législation** :
- **RSV** : [rsv.vd.ch](https://www.rsv.vd.ch)

**Travaux préparatoires** :
- **Bulletin du Grand Conseil** : [gc.vd.ch](https://www.gc.vd.ch)
- Procès-verbaux des séances
- Exposés des motifs du Conseil d'État

**Jurisprudence** :
- MCP `@entscheidsuche` avec spider `CH_VD_TC`

→ Détails : `references/par-canton/vaud.md`

---

### Neuchâtel (NE)

**Législation** :
- **RSN** : [rsn.ne.ch](https://rsn.ne.ch)

**Travaux préparatoires** :
- [ne.ch/grandconseil](https://www.ne.ch/autorites/GC)
- Procès-verbaux, rapports

**Jurisprudence** :
- MCP `@entscheidsuche` avec spider `CH_NE_TC`

---

### Fribourg (FR)

**Législation** :
- **BDLF** : [bdlf.fr.ch](https://bdlf.fr.ch)
- Bilingue français/allemand

**Travaux préparatoires** :
- [fr.ch/grandconseil](https://www.fr.ch/gc)

**Jurisprudence** :
- MCP `@entscheidsuche` avec spider `CH_FR_TC`

---

### Jura (JU)

**Législation** :
- **RSJU** : [rsju.jura.ch](https://rsju.jura.ch)

**Travaux préparatoires** :
- [jura.ch/parlement](https://www.jura.ch/PLT)

**Jurisprudence** :
- MCP `@entscheidsuche` avec spider `CH_JU_TC`

---

### Valais (VS)

**Législation** :
- **RS/VS** : [lex.vs.ch](https://lex.vs.ch)
- Bilingue français/allemand

**Travaux préparatoires** :
- [vs.ch/grandconseil](https://www.vs.ch/web/gc)

**Jurisprudence** :
- MCP `@entscheidsuche` avec spider `CH_VS_TC`

---

## Droit intercantonal (concordats)

### Définition

Accords de droit public entre cantons créant des droits et obligations. Ils l'emportent sur le droit cantonal mais doivent respecter le droit fédéral (art. 48 al. 3 Cst.).

### Sources de recherche

| Source | URL | Contenu |
|--------|-----|---------|
| **Institut du fédéralisme** (Fribourg) | [federalism.ch](https://www.federalism.ch) | Répertoire des concordats |
| **Conférence des gouvernements cantonaux** | [kdk.ch](https://www.kdk.ch) | Coordination intercantonale |
| **Recueils cantonaux** | Via Lexfind | Textes intégrés dans les RS cantonaux |

> **Note** : Depuis la nouvelle LPubl, les concordats ne sont **plus publiés au RS fédéral** sauf si la Confédération est partie.

### Concordats importants

- **Concordat sur l'arbitrage** (jurisprudence CAS)
- **Concordat sur la police** (coopération intercantonale)
- **Concordats universitaires** (HarmoS, formation)
- **Convention romande** sur la protection des mineurs

---

## Droit communal

### Communes avec recueil systématique

Les grandes communes publient leurs règlements en ligne :

| Commune | URL |
|---------|-----|
| **Genève (Ville)** | [geneve.ch/fr/autorites/conseil-municipal](https://www.geneve.ch/fr/autorites/conseil-municipal) |
| **Lausanne** | [lausanne.ch/conseil-communal](https://www.lausanne.ch/officiel/conseil-communal) |
| **Zürich** | [stadt-zuerich.ch/recht](https://www.stadt-zuerich.ch/portal/de/index/politik_u_recht.html) |
| **Bern** | [bern.ch/recht](https://www.bern.ch/politik-und-verwaltung/gemeinderat) |
| **Fribourg (Ville)** | [ville-fribourg.ch](https://www.ville-fribourg.ch) |
| **Neuchâtel (Ville)** | [neuchatelville.ch](https://www.neuchatelville.ch) |
| **Sion** | [sion.ch](https://www.sion.ch) |
| **Delémont** | [delemont.ch](https://www.delemont.ch) |

### Travaux préparatoires communaux

- **Genève** : Mémorial du Conseil municipal
- **Lausanne** : Procès-verbaux du Conseil communal
- **Fribourg** : Conseil général
- **Autres** : Sites des communes respectives

> **Note** : Pas toujours de recueil systématique → contacter l'administration communale si nécessaire.

---

## Publications cantonales (structure type)

Chaque canton a généralement trois types de publications :

| Type | Équivalent fédéral | Fonction |
|------|-------------------|----------|
| **Journal officiel** | Feuille fédérale | Promulgation hebdomadaire |
| **Recueil chronologique** | Recueil officiel (RO) | Publication chronologique annuelle |
| **Recueil systématique** | RS fédéral | Lois en vigueur par matière |

---

## Recherche d'actes cantonaux abrogés

Pour trouver des versions historiques :

1. Consulter le **recueil chronologique** cantonal
2. Vérifier l'historique des modifications dans le RS cantonal en ligne
3. Certains cantons offrent un accès aux versions historiques (ex: ZH, GE)
4. Archives cantonales si non disponible en ligne

---

## Citation du droit cantonal

Les principes de citation du droit fédéral s'appliquent **par analogie** au droit cantonal.

Exemples :
- Loi genevoise : `art. 15 LPol/GE` (RS/GE F 1 05)
- Loi vaudoise : `art. 8 LPol/VD` (RSV 131.11)
- Concordat : `art. 5 Concordat sur l'arbitrage`

→ Pour les détails : skill `@citation-juridique-suisse`

---

## Portail centralisé

**Lexfind** ([lexfind.ch](https://www.lexfind.ch)) :
- Portail renvoyant vers **tous** les recueils cantonaux
- Utile pour navigation rapide entre cantons
- Pas d'API disponible

**Fedlex** ([fedlex.admin.ch/fr/links](https://www.fedlex.admin.ch/fr/links)) :
- Liste officielle des liens vers les recueils cantonaux

---

## Outils techniques

Pour accéder aux sources cantonales :

| Besoin | Outil | Action |
|--------|-------|--------|
| **Jurisprudence cantonale** | MCP `@entscheidsuche` | `search_case_law(spider="CH_{canton}_...")` |
| **Législation cantonale** | Web (sites officiels) | Voir tableaux ci-dessus |
| **Concordats** | Web (federalism.ch) | Répertoire des concordats |

→ Pour plus de détails : skill `@outils-recherche-juridique`

---

## Références

- `references/par-canton/tous-les-cantons.md` — **URLs officielles des 26 recueils systématiques**
- `references/par-canton/geneve.md` — Détails Genève
- `references/par-canton/vaud.md` — Détails Vaud
- `references/concordats.md` — Liste des concordats importants
- `@outils-recherche-juridique` — Accès technique (MCP, CLI, APIs)
- `@citation-juridique-suisse` — Conventions de citation
