# PLAN — Classification de films et mise en production

Mise à jour : 28 octobre 2026. Travail individuel : je décide, développe, teste, déploie et retire les composants.

## Origine et limites de la reconstitution

Le brouillon du 22 octobre proposait 27 h de travail et un horizon du 22 au 29 octobre. Il existe avant les étapes API et Azure, mais son adoption effective par l'apprenant n'est pas attestée. Les 3 h attribuées aux premières tâches étaient explicitement rétrospectives. Ces propositions sont conservées ci-dessous ; elles ne deviennent pas des heures mesurées.

Les dates réalisées sont reconstituées à partir de la discussion. Une journée avec des échanges n'est pas une journée complète de travail. Aucun chronométrage fiable n'est disponible : la charge réelle reste « non mesurée ». Aucune heure de travail n'est déduite du délai entre deux messages. Les dates sont indiquées sans heures.

## Objectif et allocation

Prédire une classe 0/1 à partir du résumé d'un film. Livrer un notebook, un réseau Keras, son TF-IDF, une API, des tests, une image Docker, un workflow de publication et un déploiement Azure manuel identifié par commit.

Données observées : 2 400 films, 54 doublons supprimés, 2 346 films conservés ; apprentissage/test/production : 1 407/469/470 ; vocabulaire TF-IDF : 14 881 termes. Les noms métier des classes sont à vérifier dans la source du jeu de données.

## Tableau du plan et du réalisé

Ressource humaine pour chaque tâche : moi, apprenant seul. Matériel : ordinateur local et stockage pour T01–T10 ; ordinateur et ressources Azure pour T11–T14. Les coûts locaux et le temps humain ne sont pas valorisés : « non chiffré » ne signifie pas gratuit.

| Tâche | Dépend de | Charge estimée dans le brouillon du 22/10 | Charge réelle | Ressources humaines, matérielles et techniques | Ressources financières | Date prévue dans le brouillon | Réalisation reconstituée / état |
|---|---|---|---|---|---|---|---|
| T01 Audit et nettoyage | Aucune | 1 h, rétrospective | Non mesurée | Moi ; PC ; Python, pandas, notebook | Matériel/électricité non chiffrés | Non fixée avant réalisation | 22/10 : nettoyage exécuté |
| T02 Découpage stratifié | T01 | 1 h, rétrospective | Non mesurée | Moi ; PC ; scikit-learn | Non chiffré | Non fixée avant réalisation | 22/10 : 60/20/20 |
| T03 TF-IDF | T02 | 1 h, rétrospective | Non mesurée | Moi ; PC/RAM ; TfidfVectorizer | Non chiffré | Non fixée avant réalisation | 22/10 : vocabulaire ajusté sur apprentissage |
| T04 Modèles et recherches de réglages | T03 | 2 h | Non mesurée | Moi ; PC ; régression logistique, Bayes naïf, Keras, KerasTuner, Optuna | Non chiffré | 22/10 | 22–23/10 : trois références et recherches de 20 essais |
| T05 Évaluation finale | T04 | 2 h | Non mesurée | Moi ; PC ; F1, cinq graines, test réservé | Non chiffré | 23/10 | 23/10 : évaluation finale communiquée |
| T06 Sauvegarde et rechargement | T05 | 2 h | Non mesurée | Moi ; disque ; .keras, joblib, JSON UTF-8, CSV | Non chiffré | 23/10 | 23/10 : sauvegarde annoncée ; rechargement abordé le 26/10 |
| T07 API | T06 | 3 h | Non mesurée | Moi ; PC ; FastAPI, Uvicorn, Pydantic | Non chiffré | 24/10 | 26/10 : routes /health et /predict |
| T08 Tests et barrière qualité | T07 | 2 h | Non mesurée | Moi ; PC ; pytest, HTTPX, PyYAML | Non chiffré | 24/10 | 26–27/10 : tests, seuils et refus volontaire |
| T09 Image Docker | T08 | 2 h | Non mesurée | Moi ; PC/disque ; Dockerfile, .dockerignore | Stockage local non chiffré | 25/10 | 27/10 : construction et essai local confirmés |
| T10 Contrôles GitHub Actions | T09 | 2 h | Non mesurée | Moi ; PC et runners hébergés ; GitHub Actions | Selon offre et quotas, non relevé | 25/10 | 27/10 : chaîne verte et blocage volontaire confirmés |
| T11 Registre et publication | T10 | 2 h | Non mesurée | Moi ; Azure ACR Basic ; secrets GitHub ; job publier | Coût Azure à relever | 26/10 | 27–28/10 : configuration ; image du registre testée localement |
| T12 Déploiement manuel initial | T11 | 2 h | Non mesurée | Moi ; Azure ; film-app, environnement ivella, 1 vCPU/2 Gio, port 8000 | Coût Azure à relever | 27/10 | 28/10 : tentatives et corrections documentées ; preuve de succès à joindre |
| T13 Nouvelle version et retour arrière | T12 | 2 h | Non mesurée | Moi ; Azure ; /hello, commits et révisions | Coût Azure à relever | 28/10 | 28/10 : ajout et publication abordés ; commits et résultats publics à confirmer |
| T14 Fin de vie, preuves et bilan | T13 | 3 h | Non mesurée | Moi ; portail, Cost Management, documentation | Coût final à compléter | 29/10 | 28/10 : coûts consultés et documents actualisés ; suppression non confirmée |
| TOTAL | | 27 h proposées, dont 3 h rétrospectives | Non quantifiable | Une personne ; PC, GitHub, Azure | Coûts non consolidés | 29/10 | Activité visible les 22, 23, 26, 27 et 28/10 |

T04 et T08 sont détaillées ici pour refléter le brief réellement suivi ; le brouillon les décrivait plus sommairement. Les durées initiales ne sont pas réestimées silencieusement.

## Budget et suivi

Le brouillon proposait une enveloppe de 30 € : registre 8 €, Container Apps 10 €, journaux 5 €, divers 2 €, marge 5 €. Ce sont des allocations proposées, non des tarifs calculés ni un budget approuvé. Aucune alerte de budget configurée n'est attestée.

Le 28/10, les captures Cost Management au périmètre ivellaRG n'affichent que les comptes de stockage streamvault et indianstockage sur les journées consultées. Le coût de film-app, du registre acrfilmsivella et des journaux éventuels n'est pas encore identifié. Les 5,27 € du groupe sur octobre et les montants de stockage ne sont pas attribuables à ce seul TP. Coût du TP : non disponible à la date du relevé, à compléter après actualisation, par ressource et sur toute sa durée de vie.

ivellaRG contient d'autres projets : il doit être conservé, ainsi que leurs ressources. Toute suppression est limitée aux composants dédiés à cet exercice.

## Critères et risques

Critères effectivement utilisés : F1 binaire de la classe 1, seuil minimal 0,82 ; test d'au moins 400 exemples (469 observés) ; six tests API ; image démarrant avec /health ; publication au tag du commit ; déploiement manuel et rollback prouvés. Le seuil de F1 macro 0,75 du brouillon n'a pas été retenu.

Points à vérifier avant rendu : correspondance entre le réseau sauvegardé et son F1 dans metrics.json (0,8571 a été affiché par la barrière, alors que le réseau de graine 0 avait un F1 de 0,8609) ; commits réellement déployés ; preuve de rollback ; suppression ; coût final. Ne pas remplacer un score par un nombre historique sans vérifier le modèle concerné.
