# Liens vers les recueils systématiques cantonaux

Source : https://www.fedlex.admin.ch/fr/links

## Suisse romande

| Canton | Abrév. | Recueil systématique | Travaux préparatoires |
|--------|--------|---------------------|----------------------|
| **Genève** | GE | [silgeneve.ch/legis](https://silgeneve.ch/legis) | [ge.ch/grandconseil](https://www.ge.ch/grandconseil) (Mémorial depuis 1901) |
| **Vaud** | VD | [rsv.vd.ch](https://www.rsv.vd.ch) | [gc.vd.ch](https://www.gc.vd.ch) (Bulletin du Grand Conseil) |
| **Neuchâtel** | NE | [rsn.ne.ch](https://rsn.ne.ch) | [ne.ch/grandconseil](https://www.ne.ch/autorites/GC) |
| **Fribourg** | FR | [bdlf.fr.ch](https://bdlf.fr.ch) | [fr.ch/grandconseil](https://www.fr.ch/gc) |
| **Jura** | JU | [rsju.jura.ch](https://rsju.jura.ch) | [jura.ch/parlement](https://www.jura.ch/PLT) |
| **Valais** | VS | [vs.ch/legislation](https://www.vs.ch/web/che/legislation) | [vs.ch/grandconseil](https://www.vs.ch/web/gc) |

## Suisse alémanique

| Canton | Abrév. | Recueil systématique | Notes |
|--------|--------|---------------------|-------|
| **Zürich** | ZH | [zh.ch/zhlex](https://www.zh.ch/de/politik-staat/gesetze-beschluesse/gesetzessammlung.html) | ZH-Lex, OGD disponible |
| **Bern** | BE | [belex.sites.be.ch](https://www.belex.sites.be.ch) | BSG (Bernische Systematische Gesetzessammlung) |
| **Luzern** | LU | [srl.lu.ch](https://srl.lu.ch) | SRL |
| **Uri** | UR | [ur.ch/recht](https://www.ur.ch/recht) | — |
| **Schwyz** | SZ | [sz.ch/recht](https://www.sz.ch/behoerden/gesetzgebung.html) | SRSZ |
| **Obwalden** | OW | [ow.ch/recht](https://www.ow.ch/de/verwaltung/rechtliches/) | GDB |
| **Nidwalden** | NW | [nw.ch/recht](https://www.nw.ch/gesetzessammlung) | NG |
| **Glarus** | GL | [gl.ch/recht](https://www.gl.ch/verwaltung/staatskanzlei/gesetzessammlung.html) | GS |
| **Zug** | ZG | [bgs.zg.ch](https://bgs.zg.ch) | BGS |
| **Solothurn** | SO | [bgs.so.ch](https://bgs.so.ch) | BGS |
| **Basel-Stadt** | BS | [gesetzessammlung.bs.ch](https://www.gesetzessammlung.bs.ch) | SG BS, OGD disponible |
| **Basel-Landschaft** | BL | [bl.clex.ch](https://bl.clex.ch) | SGS |
| **Schaffhausen** | SH | [rechtsbuch.sh.ch](https://rechtsbuch.sh.ch) | SHR |
| **Appenzell A.Rh.** | AR | [bgs.ar.ch](https://www.bgs.ar.ch) | bGS |
| **Appenzell I.Rh.** | AI | [ai.ch/recht](https://www.ai.ch/themen/staat-und-recht/gesetzessammlung) | GS |
| **St. Gallen** | SG | [gesetzessammlung.sg.ch](https://www.gesetzessammlung.sg.ch) | sGS |
| **Graubünden** | GR | [gr-lex.gr.ch](https://www.gr-lex.gr.ch) | BR |
| **Aargau** | AG | [gesetzessammlungen.ag.ch](https://gesetzessammlungen.ag.ch) | SAR |
| **Thurgau** | TG | [rechtsbuch.tg.ch](https://rechtsbuch.tg.ch) | RB |

## Suisse italienne

| Canton | Abrév. | Recueil systématique | Notes |
|--------|--------|---------------------|-------|
| **Ticino** | TI | [www3.ti.ch/CAN/RLegge](https://www3.ti.ch/CAN/RLegge) | RL |

## Accès technique

### Cantons avec API/OGD

| Canton | Plateforme | URL |
|--------|-----------|-----|
| Zürich | opendata.swiss | [opendata.swiss/organization/kanton-zurich](https://opendata.swiss/fr/organization/kanton-zurich) |
| Bern | opendata.swiss | [opendata.swiss/organization/kanton-bern](https://opendata.swiss/fr/organization/kanton-bern) |
| Basel-Stadt | data.bs.ch | [data.bs.ch](https://data.bs.ch) |
| Genève | SITG | [ge.ch/sitg](https://ge.ch/sitg) |

> **Note** : Ces APIs concernent principalement les données géographiques et statistiques, pas directement les textes de loi.

### Jurisprudence cantonale

Tous les cantons sont indexés dans **entscheidsuche.ch** (MCP `@entscheidsuche`).

Codes spider par canton :
- `CH_{canton}_Obergericht` — Tribunal supérieur
- `CH_{canton}_Verwaltungsgericht` — Tribunal administratif
- `CH_{canton}_Strafgericht` — Tribunal pénal

Exemple : `CH_ZH_Obergericht`, `CH_GE_Cour`, `CH_VD_TC`

### Scraping

La plupart des sites cantonaux sont **scrapeables** mais :
- Respecter les conditions d'utilisation
- Utiliser des délais entre requêtes
- Préférer les APIs/MCP quand disponibles

## Portail centralisé

**Lexfind** (lexfind.ch) redirige vers tous les recueils cantonaux.
- Utile pour navigation rapide
- Pas d'API disponible
