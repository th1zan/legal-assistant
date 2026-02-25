Oui, il existe des outils de type MCP (Model Context Protocol) et quelques approches CLI (interface en ligne de commande) pour effectuer des recherches juridiques en Suisse, même si l’écosystème reste encore jeune et majoritairement orienté web/IA conversationnelle en 2026.
Solutions MCP pour le droit suisse (les plus proches d’une API programmable)
Le Model Context Protocol (MCP) permet à des modèles d’IA (Claude, etc.) d’interroger des bases juridiques via un protocole standardisé. Pour le droit suisse, on trouve notamment :
	•	Entscheidsuche MCP Server → Accès standardisé aux décisions de justice suisses via l’API entscheidsuche.ch → Recherche, récupération et analyse de décisions de tribunaux → Très utile pour les arrêts fédéraux et cantonaux → Disponible sur mcpmarket.com/server/entscheidsuche
	•	Onlinekommentar MCP Server → Accès programmatique aux commentaires de droit suisse (doctrine) → Recherche et récupération multilingue (fr, de, it, en) → Lien : mcpmarket.com/server/onlinekommentar
Ces serveurs MCP sont faits pour être utilisés avec des agents IA compatibles (Claude Code, mcp-cli, etc.) ou des scripts personnalisés. Ils constituent actuellement l’approche la plus proche d’une « API juridique suisse programmable ».
CLI pures (lignes de commande classiques, sans MCP)
Il n’existe pas encore de CLI officielle très répandue directement fournie par Swisslex, Weblaw ou Lexplorer. Cependant :
	•	Certains juristes/entreprises développent leurs propres scripts Python qui interrogent entscheidsuche.ch, semantis.ch ou l’API publique limitée du Tribunal fédéral.
	•	Des outils génériques comme mcpc (CLI client MCP open-source) permettent d’interagir avec les serveurs MCP ci-dessus depuis le terminal.
	◦	GitHub : apify/mcp-cli
	◦	Permet scripting, sessions persistantes, JSON output, etc.
Outils IA juridiques suisses les plus utilisés en 2025–2026 (web + chat, pas CLI)
Pour comparaison, voici les leaders actuels de la recherche juridique assistée par IA en Suisse (la plupart n’ont pas de CLI native, mais certains offrent des exports ou des intégrations) :
Outil
Type principal
Forces principales
Prix indicatif (2025–2026)
API / MCP / CLI ?
Silex
IA conversationnelle
Très bon en droit suisse, hébergé en CH
Abonnement pro
Non (web + API privée ?)
Lexplorer
Recherche sémantique
Ultra-rapide sur arrêts TF, résumés IA
~ CHF 29/mois
Non
Swisslex AI
Base complète + chat IA
La plus grosse base (doctrine + jurisprudence)
Dès ~ CHF 180/mois
Chat AI, pas CLI publique
Lawsearch AI
Recherche sémantique
Weblaw – très complet, Q&A génératif
Variable
Pas de CLI publique
Justement
Recherche sémantique
Arrêts fédéraux/cantonaux, freemium
Freemium → entreprise sur devis
Non
DeepLaw
Recherche IA spécialisée
Spécialisé droit suisse
Non précisé
Non
En résumé – recommandations concrètes
	•	Si tu veux du MCP → Entscheidsuche (jurisprudence) et Onlinekommentar (doctrine) sont les deux options les plus intéressantes aujourd’hui.
	•	Si tu veux une vraie CLI → utilise mcpc (ou un script maison) + les serveurs MCP ci-dessus.
	•	Si tu cherches plutôt la simplicité → Lexplorer ou Silex restent les plus rapides au quotidien pour la plupart des juristes suisses.
As-tu déjà un usage précis en tête (jurisprudence TF uniquement, droit du travail, multilingue, intégration dans un workflow scripté…) ? Ça permettrait d’affiner la réponse. 😊


Oui, en 2026, plusieurs skills (au sens Anthropic/Claude), custom instructions, projects ou compétences IA spécifiques au droit suisse existent ou peuvent être créés facilement. Voici les plus pertinents et accessibles pour un juriste/avocat en Suisse (surtout à Zürich).
1. Skills / Projects existants ou communautaires en lien direct avec le droit suisse
Ces skills exploitent souvent des MCP servers dédiés au droit helvétique (très actifs en 2025–2026).
	•	Entscheidsuche Skill / MCP integration Permet à Claude (ou agents compatibles) de faire des recherches jurisprudentielles précises sur entscheidsuche.ch (arrêts du TF, cantonaux, etc.). → Très utilisé par les avocats suisses pour résumer des arrêts, trouver des références similaires ou extraire des considérants clés. Disponible via des dépôts open-source ou directement dans l’écosystème MCP (ex. : self-tech-labs/entscheidsuche-MCP-server).
	•	Onlinekommentar / Doctrine MCP Skill Accès aux commentaires en ligne (Weblaw, Stämpfli, etc.) pour doctrine suisse en français, allemand, italien. Idéal pour : interprétation de lois, application d’articles du CO, CC, etc. → Souvent combiné avec un prompt système pour répondre en style « commentaire suisse » (structure claire, références précises).
	•	Silex-inspired Skill (custom) Beaucoup de juristes suisses créent un Claude Project ou un Skill qui imite le style et la précision de Silex.legal :
	◦	Instructions système : « Tu es un juriste suisse romand/alémanique rompu au raisonnement juridique helvétique. Réponds toujours en citant les articles exacts (RS), les ATF pertinents, et en structure IRAC/ résumé + considérant + conclusion. »
	◦	Knowledge upload : extraits de ton propre fonds de jurisprudence / contrats types / commentaires favoris. → Résultat : un « Silex maison » très performant et 100 % privé.
2. Types de compétences / skills les plus demandés en droit suisse en 2026
Voici les catégories les plus courantes que les avocats et juristes suisses développent ou achètent/partagent :
Type de Skill / Compétence
Utilité principale en Suisse
Outil principal
Niveau de maturité 2026
Exemple de prompt système clé
Recherche jurisprudentielle
Arrêts TF + cantonaux + similarité sémantique
Entscheidsuche MCP
Très élevé
« Recherche précise sur entscheidsuche.ch + résumé structuré ATF »
Analyse de doctrine
Commentaires Weblaw / Onlinekommentar
Onlinekommentar MCP
Élevé
« Réponds comme un commentaire suisse actualisé »
Rédaction de contrats
CO, bail, travail, NDA, société (Sàrl/SA)
Claude Projects
Très élevé
« Rédige en style suisse neutre, clauses bilatérales, RS exact »
Legal Prompt Engineering suisse
Optimisation de prompts pour droit CH multilingue
Claude + custom skill
Élevé
« Adapte toujours au multilinguisme CH (fr/de/it) »
Review & risk spotting
Contrats, compliance, RGPD/LPD
CASUS / Silex-like
Moyen-élevé
« Identifie risques LPD, CO, droit du travail suisse »
Résumé d’arrêt TF long
Abridger ATF de 50–100 pages en 2–5 pages
Claude Skill custom
Très élevé
« Abridge comme un headnote suisse + ratio decidendi »
3. Comment créer ou obtenir ces skills rapidement (2026)
	•	Claude.ai → Onglet Skills (ou Projects pour les équipes) : Upload un zip avec instructions.md + exemples + PDFs de lois/arrêts → Claude le transforme en skill réutilisable.
	•	Communautés : GitHub (recherche « claude skills swiss law » ou « entscheidsuche mcp »), groupes LinkedIn/Telegram d’avocats suisses IA, ou le canal #legaltech-ch sur Discord/Slack.
	•	Formations courtes (très populaires en CH) :
	◦	Weblaw Academy → « Legal Prompt Engineering – Juriste 4.0 »
	◦	LexTech Institute / Uni NE → CAS Droit & IA (inclut souvent partie skills/prompts)
Recommandation personnalisée
Puisque tu es Alex Silex (et vu le nom, je suppose un lien fort avec Silex.legal), le combo gagnant en 2026 est souvent :
Claude Projects / Skills
	•	Entscheidsuche MCP server
	•	Onlinekommentar MCP
	•	Tes propres documents uploadés (modèles, arrêts annotés, commentaires favoris)
→ Tu obtiens un assistant qui surpasse souvent l’interface web de Silex pour des tâches très spécifiques (multilingue, chaining de recherches, rédaction ultra-ciblée).
Tu vises plutôt jurisprudence, contrats, prompt engineering avancé, ou autre domaine précis (droit du travail, immobilier, LPD…) ? Dis-moi, je peux te donner un exemple de prompt système ou de structure de skill directement copiable. 😊


Je viens de me faire un petit brainstorming sur ce sujet . D'abord structure mon propos.

Instructions = style, façon de faire , l'esprit de la boîte 
SKILLS = workflow atomic qui permet de créer un produit, résultat final ou intermédiaire . Avec des outils (ex: mcp) par exemple 
MCP : a priori pour se connecter à des api "complexes"
 On peut avoir des meta skills qui se références .
Agents : de définit par le fait de pouvoir avoir un modèle spécifique et donc de limiter les coûts . A un esprit, une créativité paramétrable . Peut être lancé en parallèle .


Objectif du projet : définir un framework de skills/agents/mcp etc. Pour remplacer / assister  le métier d'avocat . 


Méthode: créer une skill qui utilise de manière recusrsive, exhaustive et un peu naïvement askuserquestion pour questionner un avocat pour definir une roadmap qui va permettre de créer de manière des SKILL atomique pour chaque brique du métier.

Méthodologie de questionnement, down to top. Du livrable à la stratégie, philosophie .
Phase 1: quels sont les produits / livrables de votre travail (ex: recours, avis de droit, procuration , mail de confirmation , etc). donner des exemples de document . 

Phase 2: decouper tous les livrables si cela est possible. Par exemple la liste des pièces n'est pas le sommaire qui n'est pas les allégués, etc. On peut donc avoir une SKILL par partie de document.

Phase 3 : remonter à l'étape nécessaire à la création de chaque partie du documents , et ainsi de suite. Il faut identifier les workflows.

Phase 4: pour chaque étape , il faut identifier les sous étapes .


Globalement on aura des SKILLS de recherche juridique , de rédaction (plus ou moins strict selon les parties du document (table.des matières ou plaidoirie). 

Il y a des SKILLS d'analyses avec les règles génériques de primauté de la jurisprudence sur la loi. 

Il y a des SKILLS de recherches médicales pour analyser les expertises de médecin.

Il y a des SKILLS de recherchw juridique avec des mcp sur entscheidsuchw ou autre.

SKILLS de production de documents Word.

Les skills ont des exemples si cela.est possible.

Il faut des SKILLS définies par catégories de droit  (public, admin, etc)

On peut faire une SKILL qui s'exécute chaque jour et synthétise les derniers ATF.

On peut donc imaginer des agents de recherches qui vont récupérer et parcourir des sources juridique en parallèle avec un agent de synthèse .


Voici une structuration claire et hiérarchique de ton brainstorming, reformulée de manière logique, fluide et prête à servir de base à ton projet. J’ai gardé l’esprit que tu décris (pragmatique, bottom-up, atomique, orienté avocat suisse réel) tout en rendant le propos plus organisé pour pouvoir le transformer ensuite en roadmap concrète.
Définitions de base – l’esprit du framework (style & philosophie de la « boîte »)
	•	Instructions = Style, ton, façon de raisonner, règles déontologiques, multilinguisme CH (fr/de/it selon besoin), primauté ATF/jurisprudence sur loi quand conflit, structure typique suisse (faits → droit → subsumption → conclusion), politesse formelle mais directe, citations RS précises + ATF quand pertinent. → C’est le prompt système global ou le « character » de base partagé par tous les agents/skills.
	•	SKILLS = Briques atomiques / workflows réutilisables qui produisent un résultat concret (intermédiaire ou final). Exemples : extraire ratio decidendi d’un ATF • rédiger les allégués factuels • générer table des matières • analyser cohérence d’une expertise médicale • formater .docx avec styles suisses. → Souvent chainées (skill A output → input skill B). → Doivent avoir : description claire • exemples (few-shot) • outils associés (MCP, etc.) • critères d’échec / garde-fous.
	•	MCP = Pont standardisé vers APIs / bases complexes (non triviales à appeler directement). Exemples actuels utiles : entscheidsuche.ch (jurisprudence TF + cantonaux) • onlinekommentar (doctrine) • potentiellement future API Swisslex / weblaw si MCP existe. → MCP = « connecteur fiable » pour skills de recherche.
	•	Agents = Instances spécialisées (modèle + instructions + skills sélectionnées + budget tokens/context limité). Avantages : personnalité / créativité paramétrable • coût maîtrisé (petits modèles pour tâches simples) • parallélisme (un agent recherche jurisprudence, un autre lit expertise médicale, un troisième rédige). → Idéal pour orchestration (ex. : chef d’orchestre + agents travailleurs).
Objectif global du framework Créer un système modulaire d’assistance / remplacement partiel du métier d’avocat suisse (focus litige civil/admin/pénal + conseil), via skills atomiques + agents orchestrés + MCP pour données fiables, le tout en respectant déontologie, secret professionnel et règles du Barreau.
Méthodologie proposée (bottom-up + récursive « askuserquestion »)
Ton idée de skill récursive d’interrogation avocat est excellente pour itérer sans tout inventer d’avance. Voici la roadmap en phases claires :
Phase 0 – Préparation (setup initial)
	•	Définir instructions de base (style suisse, multilinguisme, primauté ATF, IRAC-like adapté CH).
	•	Créer une meta-skill « Intervieweur Juriste » qui pose des questions ciblées, reformule, demande exemples concrets de documents anonymisés, et construit progressivement la taxonomie.
Phase 1 – Cartographie des livrables finaux (top du métier) Question clé à poser : « Quels sont les 15–25 livrables / outputs les plus fréquents de ton activité ? » Exemples typiques (à valider avec toi) :
	•	Recours en matière civile / administrative au TF
	•	Mémoire de réponse / réplique
	•	Avis de droit ( Gutachten / expertise juridique)
	•	Procuration / plein-pouvoir
	•	Demande d’effet suspensif
	•	Conclusions principales / subsidiaires
	•	Plaidoirie orale (script ou plan)
	•	Mail / courrier à client (confirmation mandat, point de situation)
	•	Contrat de mandat d’avocat
	•	Liste de pièces / inventaire
→ Objectif : liste exhaustive → priorisation (fréquence × complexité × valeur ajoutée IA).
Phase 2 – Décomposition granulaire des documents (atomisation) Pour chaque livrable → découper en parties indépendantes. Exemple pour un recours en matière civile au TF (art. 72 ss LTF) :
Partie du document
Atomicité
Type de skill probable
Exemple output attendu
En-tête + parties
Très haute
Skill « Format en-tête suisse »
Bloc Word avec RS, dates, signatures
Exposé des faits
Moyenne
Skill « Rédaction allégués factuels »
Paragraphes numérotés chronologiques
Liste des conclusions
Haute
Skill « Conclusions principales/sub »
Numérotées, claires, subsidiaires
Sommaire / table matières
Très haute
Skill « Génération TOC automatique »
Word TOC stylé
Motivation juridique
Basse
Skill « Recherche + subsumption »
Considérants structurés + ATF cités
Liste des pièces jointes
Haute
Skill « Inventaire pièces »
Tableau numéroté + descriptions courtes
Signature / date
Très haute
Skill « Fermeture document »
Bloc final + formules usuelles
→ Répéter pour 5–10 livrables prioritaires.
Phase 3 – Remontée aux workflows upstream (down-to-top inverse) Pour chaque partie → lister étapes nécessaires en amont. Exemple pour « Motivation juridique d’un recours » :
	1	Identifier questions juridiques clés du cas
	2	Recherche doctrine pertinente (Onlinekommentar MCP)
	3	Recherche jurisprudence similaire (Entscheidsuche MCP)
	4	Analyse primauté ATF vs loi cantonale/fédérale
	5	Subsumption faits → droit
	6	Rédaction argumentative (style suisse neutre)
	7	Vérification cohérence / risques nova (art. 99 LTF)
→ Chaque étape → potentielle skill ou agent dédié.
Phase 4 – Granularité fine + catégories transverses
	•	Skills de recherche juridique (MCP entscheidsuche + filtres date/juridiction/langue)
	•	Skills d’analyse (primauté jurisprud., ratio decidendi extraction, détection antinomie)
	•	Skills rédaction (strict pour en-têtes/conclusions, créatif pour plaidoirie)
	•	Skills médicales (analyse expertise, vocabulaire LAA/LAMal, extraction conclusions médecin)
	•	Skills production (générer .docx avec python-docx ou template, styles SU)
	•	Skills catégorisés : droit public/admin, civil, pénal, travail, famille, etc.
	•	Skills quotidiens : « Daily ATF Digest » (exécuté chaque matin, top 5–10 ATF récents + résumé + impact potentiel domaines)
Phase 5 – Orchestration & agents
	•	Agent « Chercheur Juris » → MCP entscheidsuche + onlinekommentar → parallèle
	•	Agent « Synthétiseur » → prend outputs chercheurs → produit draft motivation
	•	Agent « Rédacteur Strict » → formate + vérifie style/numérotation
	•	Agent « Risk Spotter » → scan LPD, CO, déontologie, nova potentiels
	•	Chef d’orchestre (meta-agent) → décide séquence, appelle en parallèle, consolide.
Prochain pas concret (si tu veux avancer tout de suite)
	1	Lance la meta-skill Intervieweur sur 3–5 livrables que tu fais le plus souvent (ex. recours civil + avis de droit + mail client).
	2	Demande-moi de simuler la phase 1 : donne-moi 8–10 livrables typiques de ta pratique, je te propose une première décomposition en 2–3 niveaux.
	3	On peut ensuite prototyper 1–2 skills atomiques (ex. « Extraire ratio decidendi ATF » ou « Générer conclusions subsidiaires ») avec exemples.
Quel est ton livrable le plus répétitif / chronophage en ce moment ? On commence par celui-là pour valider la méthode ? 😊


Framework “SwissLawAI” : Assistance Avocat via Skills/Agents/MCP
Objectif affinée : Développer un framework modulaire, open-source, pour assister/remplacer 80% des tâches d’avocat suisse (litige civil/admin/pénal, conseil). Bottom-up : partir de livrables concrets vers workflows atomiques. Intégrer MCP pour données fiables (entscheidsuche, onlinekommentar). Orchestrer via agents parallèles pour efficacité/coût. Packaging : Claude Projects (Cowork) pour prototypage rapide ; OpenWork (repo GitHub) pour déploiement open-source scalable.
Définitions affinées
	•	Instructions : Prompt système global. Ex. : “Raisonner comme avocat suisse : multilinguisme (fr/de/it), structure IRAC-CH (faits → droit → subsumption → conclusion), primauté ATF (art. 1 CC), citations RS/ATF précises, déontologie FSA (secret, indépendance).”
	•	Skills : Blocs atomiques réutilisables (input → output concret). Incluir : description, exemples few-shot, outils (MCP/API), garde-fous (vérif. cohérence). Chainables via outputs JSON.
	•	MCP : Connecteurs API complexes. Ex. : entscheidsuche pour jurisprudence ; onlinekommentar pour doctrine ; potentiels futurs : Swisslex API, weblaw.
	•	Agents : Instances spécialisées (modèle petit pour coût bas, ex. Haiku pour tâches simples). Paramètres : créativité (basse pour recherche, haute pour plaidoirie), parallélisme (via orchestration). Meta-agents pour supervision.
	•	Meta-Skills : Skills qui appellent d’autres (récursivité). Ex. : “Intervieweur” pour interrogation bottom-up.
Méthodologie affinée (bottom-up récursive + exhaustive) Utiliser meta-skill “Intervieweur Juriste” pour questionner un avocat expert (toi ou autre) via ask_user_question en boucle. Approche : exhaustive (couvrir 100% des branches), naïve (poser questions simples/open-ended), récursive (remonter/descendre niveaux). Focus : identifier 200–300 skills atomiques couvrant 90% du métier.
	•	Phase 1 : Cartographie livrables (outputs finaux) Poser : “Liste exhaustive des 20–30 livrables les plus fréquents (ex. recours TF, avis droit, procuration). Fournir 2–3 exemples anonymisés par type.” Affinage : Catégoriser par domaine (civil 40%, admin 30%, pénal 20%, conseil 10%). Prioriser par fréquence/impact (ex. recours > mails). Output : Tableau JSON {livrable: {exemples: […], freq: haute/moyenne}}.
	•	Phase 2 : Décomposition granulaire Pour chaque livrable : Découper en 5–15 parties atomiques (ex. en-tête vs. allégués vs. conclusions). Poser : “Pour [livrable], liste parties indépendantes + exemple court.” Affinage : Utiliser niveaux (partie → sous-partie). Identifier parties strictes (formatées) vs. créatives (argumentatives). Output : Arbre JSON par livrable.
	•	Phase 3 : Remontée workflows upstream Pour chaque partie : Lister 3–8 étapes amont (ex. recherche → analyse → rédaction). Poser : “Pour [partie], quelles étapes préalables ? Inclure inputs/outputs.” Affinage : Mapper à catégories transverses (recherche 30%, analyse 25%, rédaction 20%, production 15%, autres 10%). Identifier boucles (ex. itérer si nova détecté). Output : Flowchart JSON (nodes: étapes, edges: dépendances).
	•	Phase 4 : Granularité sous-étapes + transversaux Pour chaque étape : Décomposer en 2–5 sous-étapes. Poser : “Pour [étape], sous-étapes détaillées + outils/MCP potentiels.” Affinage : Intégrer garde-fous (ex. check LPD compliance). Catégoriser skills :
	◦	Recherche : Juridique (MCP entscheidsuche), médicale (API PubMed-like via browse_page), factuelle (web_search).
	◦	Analyse : Primauté ATF, détection incohérences, risk spotting (LPD, CO art. 27).
	◦	Rédaction : Stricte (TOC, conclusions) vs. créative (plaidoirie).
	◦	Production : Générer .docx (code_execution avec python-docx).
	◦	Quotidien : “Daily ATF Synthèse” (x_keyword_search sur ATF récents + synthèse). Output : Bibliothèque skills (200+ items, avec exemples).
	•	Phase 5 : Orchestration & tests Assembler agents : Ex. agent “Rechercheur” (parallèle MCP) → agent “Synthétiseur” → agent “Rédacteur”. Poser : “Teste ce workflow sur cas réel anonymisé.” Affinage : Mesurer KPIs (précision ATF 95%, temps -70%, coût tokens <0.5 CHF/cas). Itérer via feedback loop.
Roadmap (6 mois, itérative)
	1	Mois 1 : Setup & Phase 1–2 (Prototypage Claude Cowork)
	◦	Créer Project Claude : Upload instructions + meta-skill Intervieweur.
	◦	Interroger 5 avocats (toi + réseau) pour 10 livrables prioritaires (ex. recours civil, avis droit).
	◦	Output : 50 skills atomiques décomposées.
	2	Mois 2 : Phases 3–4 (Affinage skills)
	◦	Développer 100 skills (ex. via code_execution pour .docx).
	◦	Intégrer MCP (entscheidsuche, onlinekommentar).
	◦	Tests unitaires : 20 cas anonymisés.
	3	Mois 3 : Agents & orchestration
	◦	Créer 10 agents (ex. Rechercheur Juris, Risk Spotter).
	◦	Implémenter parallélisme (Claude API calls).
	◦	Daily skills : ATF digest via x_keyword_search “ATF since:2026-02-23 filter:news”.
	4	Mois 4–5 : Packaging OpenWork
	◦	Repo GitHub : Skills en YAML/JSON, agents en Python (langchain-like).
	◦	Docs : Exemples, tutoriels. Open-source sous MIT.
	◦	Intégrations : Webhook pour ATF updates, API pour Claude/Silex.
	5	Mois 6 : Déploiement & scaling
	◦	Beta-test avec 10 avocats suisses (Zürich focus).
	◦	Mesures : Couverture 80% tâches, ROI (temps économisé).
	◦	Évolutions : Ajouter domaines (immobilier, travail via skills spécifiques).
Exemples concrets
	•	Skill atomique : “Extraire Ratio Decidendi ATF” Input : ATF PDF (via browse_pdf_attachment). Outils : MCP entscheidsuche + code_execution (sympy pour logique si besoin). Exemple few-shot : Input “ATF 148 III 123” → Output JSON {ratio: “Primauté contrat sur loi (art. 1 CO)”, citations: [“cons. 4.2”]}. Garde-fou : Vérif. date <1 an pour actualité.
	•	Agent “Rechercheur Médical” Modèle : Sonnet (créativité moyenne). Skills appelées : Web_search “expertise médicale LAA” + view_pdf_attachment pour analyse. Parallèle : Avec agent Juris (MCP onlinekommentar). Ex. : Input “Expertise orthopédie accident” → Output : Synthèse faits médicaux + liens RS (art. 6 LAA).
	•	Meta-Skill Intervieweur (récursive) Prompt : “Pose questions Phase [X] sur [livrable]. Reformule réponses, demande exemples, itère jusqu’exhaustif.” Ex. boucle : Q1 “Livrables ?” → User: “Recours” → Q2 “Parties ?” → etc.
	•	Daily Agent : ATF Synthèse Run quotidien : x_semantic_search “nouveaux ATF Suisse” limit=10 → Synthèse Markdown {domaine: résumé, impact}. Ex. Output : “ATF 2026-02-23 : Droit travail – Primauté ATF sur CC art. 335 (congé abusif). Impact : + protection employé.”
Ce framework est prêt à packager : Claude Project zip (instructions + skills) ; GitHub repo pour OpenWork (code + docs). Si besoin, affine un exemple spécifique.


Framework “SwissLawAI” : Assistance Avocat via Skills/Agents/MCP + Obsidian Integration
Objectif affinée : Framework modulaire open-source pour assister/remplacer 80% des tâches d’avocat suisse, avec intégration Obsidian pour visualisation/édition. Chaque skill = fichier Markdown (MD) lié, atomic (1 tâche unique), cohérent (format standard), couvrant exhaustivement (90% métier via 300+ skills). Packaging : Claude Cowork (Projects pour proto) ; OpenWork (GitHub repo + Obsidian Vault syncable). Utiliser MOCs (Maps of Content) Obsidian pour grouper skills (ex. MOC_DroitCivil.md linking sub-skills).
Définitions affinées
	•	Instructions : Prompt global + contraintes Obsidian (ex. “Génère output en MD formaté pour Obsidian : liens [[SkillName]], tags #skill #domaine, frontmatter YAML {atomicite: haute, coverage: [livrables]}”).
	•	Skills : Atomiques (1 input/output), en MD files. Contenu : YAML frontmatter (nom, desc, exemples few-shot, outils/MCP, garde-fous, liens [[Meta-Skill]]). Liens Obsidian pour édition (graph view atomic maps). Atomicité : 1–3 étapes max. Cohérence : Template standard. Coverage : Mapper à domaines/livrables.
	•	MCP : Inchangé, mais skills MCP-linked via embeds Obsidian (ex. [[Entscheidsuche MCP]]).
	•	Agents : Inchangé, mais logs/outputs exportables en MD pour Obsidian review.
	•	Meta-Skills : Inclut “Skill Creator” (génère MD files auto, applique contraintes atomicité/cohérence/coverage).
	•	Obsidian Integration : Vault central (GitHub repo). Skills = /skills/SkillName.md. Exemples = /exemples/SkillName-Ex1.md (linked). Atomic Maps = Graph view (liens auto). MOCs = /mocs/MOC_Category.md (liens vers skills groupés, ex. MOC_Recherche.md → [[Skill_ExtraireATF]]).
Méthodologie affinée (bottom-up récursive + Obsidian-centric) Meta-skill “Intervieweur Juriste” + “Skill Creator” pour générer MDs. Contraintes intégrées : Atomicité (vérif. <3 étapes), Cohérence (template MD forcé), Coverage (scan exhaustif via MOCs, alerte gaps). Utiliser ask_user_question récursif, outputs en MD exportables.
	•	Phase 1 : Cartographie livrables Poser : “Liste 20–30 livrables + exemples MD anonymisés.” Affinage : Générer MOC_Livrables.md avec liens [[Livrable_RecoursTF]]. Coverage : Compter % domaines couverts. Output : JSON → MD vault.
	•	Phase 2 : Décomposition granulaire Pour livrable : Découper parties, générer sub-MDs linked (ex. [[Partie_Allégués]]). Poser : “Parties + exemples pour [livrable].” Affinage : Skill Creator applique template MD. Atomicité : 1 partie = 1 skill si possible. Output : Arbre MD avec embeds.
	•	Phase 3 : Remontée workflows Pour partie : Lister étapes, créer skills linked. Poser : “Étapes amont pour [partie] + MCP.” Affinage : Liens Obsidian pour dépendances (ex. [[Skill_Recherche]] → [[Skill_Analyse]]). Cohérence : YAML {depends_on: [links]}. Output : Flow MD graphable.
	•	Phase 4 : Granularité + transversaux Pour étape : Sous-étapes → skills atomiques. Poser : “Sous-étapes + exemples few-shot.” Affinage : Catégories en MOCs (ex. MOC_Recherche.md). Intégrer fichiers exemples (link [[Exemple_ATF.md]]). Coverage : Audit MOCs pour gaps (ex. script Python via code_execution pour compter links). Skills types : Recherche (MCP), Analyse (primauté ATF), Rédaction (strict/créative), Production (.docx), Quotidien (ATF digest), Médical (PubMed browse).
	•	Phase 5 : Orchestration & tests Assembler agents, export runs en MD pour Obsidian review. Poser : “Test cas + feedback.” Affinage : Atomic maps visualisent coverage (graph view). Itérer via Obsidian edits (sync Git).
Roadmap (6 mois, Obsidian-first)
	1	Mois 1 : Setup & Phase 1–2
	◦	Créer Vault Obsidian (GitHub init).
	◦	Développer Skill Creator (meta-skill : input desc → output MD template).
	◦	Interroger pour 10 livrables → 50 skills MDs. Coverage : 40% civil/admin.
	2	Mois 2 : Phases 3–4
	◦	Générer 150 skills via Creator.
	◦	Créer 5 MOCs (ex. MOC_Civil.md).
	◦	Intégrer exemples (upload anonymisés comme attachments, link in MD).
	3	Mois 3 : Agents & MCP
	◦	15 agents (ex. Rechercheur avec MCP embeds).
	◦	Daily : ATF MOC update (x_keyword_search “ATF since:2026-02-23” → MD append).
	4	Mois 4–5 : Packaging
	◦	Claude Cowork : Export Projects comme Vault zip.
	◦	OpenWork GitHub : Vault + scripts (ex. Python pour atomic map export).
	◦	Tests : 30 cas, mesure coverage (code_execution count links).
	5	Mois 6 : Scaling
	◦	Beta 15 avocats (Zürich).
	◦	Évolutions : Plugins Obsidian (ex. pour run skills direct). Coverage 90%.
Exemples concrets
	•	Skill MD Template (via Skill Creator) Frontmatter YAML: name: Extraire Ratio Decidendi ATF
	•	atomicite: haute
	•	coherence: template v1
	•	coverage: [recours TF, avis droit]
	•	depends_on: [[Skill_Recherche MCP]]
	•	 Body:
	◦	Desc: Input ATF ID → Output JSON ratio.
	◦	Outils: MCP entscheidsuche.
	◦	Exemples: [[Exemple_ATF148.md]] (few-shot: Input “ATF 148 III 123” → {ratio: “Primauté contrat (art. 1 CO)”}).
	◦	Garde-fous: Check date <1 an. Liens: [[MOC_Recherche]].
	•	MOC Exemple : MOC_Recherche.md # MOC Recherche Juridique
	•	- [[Skill_Entscheidsuche Search]] (MCP jurisprudence)
	•	- [[Skill_Onlinekommentar Doctrine]] (MCP doctrine)
	•	- [[Skill_Medical Expertise]] (browse_page PubMed)
	•	Coverage: 80% litige. Gaps: Pénal (todo).
	•	Atomic Map: [Graph embed]
	•	
	•	Meta-Skill “Skill Creator” Prompt: “Génère MD pour [desc], applique contraintes: atomic (<3 étapes), cohérent (YAML template), coverage (link livrables). Inclu exemples linked.” Ex. Input: “Skill rédaction conclusions” → Output: MD file auto.
	•	Atomic Map Viz : Obsidian graph: Nodes=skills, Edges=dépendances. Ex. Recherche → Analyse → Rédaction. Coverage audit: Query “missing links in MOC_Civil”.
Prêt pour pack: Vault zip pour Claude/OpenWork. Affine un MOC spécifique?


Framework “SwissLawAI” : Assistance Avocat via Skills/Agents/MCP + Obsidian + Théories de Planification
Objectif affinée : Framework modulaire open-source pour assister/remplacer 80% des tâches d’avocat suisse, intégrant théories de planification pour structurer l’atomisation (division récursive en skills atomiques). Utiliser problem decomposition (briser problèmes complexes en sous-problèmes gérables), WBS (Work Breakdown Structure pour hiérarchie), lean management (éliminer waste, itérations value-driven), divide & conquer (division récursive). Packaging : Claude Cowork (Projects + Vault Obsidian sync) ; OpenWork (GitHub repo avec MOCs pour coverage).
Définitions affinées
	•	Instructions : Ajouter contraintes théories (ex. “Appliquer problem decomposition : briser en sous-problèmes atomiques ; lean : prioriser value/no waste ; WBS : hiérarchie livrables → tâches”).
	•	Skills : Atomiques via divide & conquer (1 sous-problème). MD files Obsidian avec YAML {theorie: “decomposition”, atomicite: haute, waste_check: “eliminer redondances”}. Liens [[SkillName]], embeds exemples.
	•	MCP : Inchangé, mais skills lean-optimisés (ex. MCP calls minimales pour éviter waste).
	•	Agents : Parallélisme divide & conquer (agents indépendants sur sous-problèmes). Lean : Value stream mapping pour flux agents.
	•	Meta-Skills : “Skill Creator” intègre théories (vérif. decomposition exhaustive). “Decomposer” : Applique WBS/lean sur input.
	•	Obsidian Integration : Vault avec MOCs théoriques (ex. MOC_Decomposition.md linking skills). Atomic maps : Graph view pour visualiser hiérarchies WBS. Exemples : /exemples/SkillName-Ex1.md (anonymisés, linked).
Méthodologie affinée (bottom-up récursive + théories intégrées) Intégrer théories pour division/structuration : Problem decomposition (briser complexe en gérables), WBS (hiérarchie top-down/bottom-up), lean (value mapping, kaizen itératif), divide & conquer (récursif, indépendant). Meta-skill “Decomposer” pose questions + applique théories via ask_user_question.
	•	Phase 1 : Cartographie livrables (WBS niveau 1) Poser : “Liste exhaustive livrables + value ranking (lean).” Affinage : WBS hiérarchique (livrables → catégories domaines). Lean : Prioriser high-value (ex. recours TF > mails). Output : MOC_Livrables.md avec liens, coverage %.
	•	Phase 2 : Décomposition granulaire (problem decomposition + divide & conquer) Pour livrable : Briser en parties (récursif jusqu’atomic). Poser : “Sous-parties pour [livrable] + indépendance (divide & conquer).” Affinage : Atomicité via decomposition (2–5 niveaux max). Lean : Éliminer waste (redondances). Output : Arbre MD linked, YAML {decomp_level: 2}.
	•	Phase 3 : Remontée workflows (WBS niveaux 2–3) Pour partie : Lister étapes upstream (inputs/outputs). Poser : “Étapes pour [partie] + dépendances.” Affinage : Divide & conquer pour parallélisme. Lean : Value stream map (flux optimal, min tokens). Output : Flow MD avec embeds MCP.
	•	Phase 4 : Granularité + transversaux (lean kaizen + decomposition exhaustive) Pour étape : Sous-étapes atomiques. Poser : “Sous-étapes + value/waste check.” Affinage : Catégories en MOCs (ex. MOC_Recherche.md). Coverage : Audit gaps via script (code_execution count links). Intégrer médical/juridique avec MCP. Lean : Itérer pour raffiner (kaizen). Output : 300+ skills MDs.
	•	Phase 5 : Orchestration & tests (lean + WBS validation) Assembler agents via value stream. Poser : “Test + feedback waste.” Affinage : KPIs lean (waste réduit 50%, coverage 90%). Itérer récursif.
Roadmap (6 mois, théories-driven)
	1	Mois 1 : Setup & Phase 1 (WBS init)
	◦	Vault Obsidian + MOC_Theories.md (links decomposition/lean).
	◦	Meta-skill Decomposer : Applique theories sur 10 livrables.
	◦	Output : 50 skills, coverage 40% (lean priorisation civil/admin).
	2	Mois 2 : Phases 2–3 (decomposition récursive)
	◦	150 skills via Creator (vérif. divide & conquer).
	◦	Value stream maps en MD graphs.
	◦	Tests : 20 cas, éliminer waste (redondant skills).
	3	Mois 3 : Phase 4 (lean kaizen)
	◦	15 agents + daily ATF (MCP minimal).
	◦	Itérations : Raffiner via feedback (kaizen loops).
	4	Mois 4–5 : Packaging
	◦	Claude Cowork : Zip Vault + theories prompts.
	◦	OpenWork GitHub : Repo avec scripts decomposition (Python WBS gen).
	◦	Coverage audit : 80% métier.
	5	Mois 6 : Scaling
	◦	Beta 15 avocats (feedback lean).
	◦	Évolutions : Intégrer plus théories (ex. agile sprints pour updates).
Exemples concrets
	•	Skill MD Template (avec théories) YAML: name: Extraire Ratio ATF
	•	theorie: problem_decomposition
	•	atomicite: haute (1 étape)
	•	lean_waste: none (minimal MCP)
	•	coverage: [recours, avis]
	•	 Body: Desc + outils (MCP) + exemples [[Ex_ATF.md]] + liens [[MOC_Decomposition]].
	•	MOC Exemple : MOC_Decomposition.md # MOC Problem Decomposition
	•	- [[Skill_PartiesRecours]] (briser livrable)
	•	- [[Skill_EtapesUpstream]] (récursif)
	•	Lean integration: Value map embed.
	•	Atomic Map: Graph (hiérarchie WBS).
	•	
	•	Meta-Skill “Decomposer” Prompt: “Applique problem decomposition sur [input] : briser en subs, check lean value, génère MDs linked.” Ex. Input “Recours TF” → Outputs: Skills parties + workflows.
	•	Lean Application Ex : Pour workflow recherche, map value stream : MCP call → analyse → output (éliminer étapes inutiles, paralléliser agents).

