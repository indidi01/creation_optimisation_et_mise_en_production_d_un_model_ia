# Procédure de mise en production

Projet de classification de films. Mise à jour du 28 octobre 2026.

Je décide de publier une version après une correction, une modification du modèle ou l'ajout d'une fonctionnalité. Je réalise aussi les vérifications, le déploiement et le retour arrière.

## Préparer et publier la version

Je vérifie le modèle et ses métriques, puis je lance :

```bash
python barriere_qualite.py
python -m pytest -v
```

La configuration demande un F1 minimum de 0,82 et au moins 400 films de test. Le score doit être celui du réseau sauvegardé. Je vérifie ce point avant le rendu car la barrière a affiché 0,8571, alors que le réseau de graine 0 évalué précédemment obtenait 0,8609.

J'enregistre les changements dans Git et je fais un push. GitHub Actions exécute les tests, construit et vérifie l'image, puis la publie dans acrfilmsivella.azurecr.io. L'image porte le nom films-api et son étiquette est le commit complet. J'attends les trois jobs verts avant de déployer.

## Déployer et contrôler

Je note l'image actuellement utilisée par film-app. Dans Azure Container Apps, j'ouvre Conteneurs, puis je modifie et déploie une révision avec la nouvelle étiquette. Je garde 1 vCPU, 2 Gio de mémoire et une entrée publique HTTP vers le port 8000. L'accès au registre utilise ses identifiants administrateur enregistrés comme secret.

Je vérifie la révision qui reçoit le trafic et je teste l'adresse publique. La route /health doit répondre avec la version et le commit si son suivi a été intégré. La route /predict doit accepter un résumé valide et refuser un texte vide ou trop court. Lors de l'ajout de /hello, je vérifie aussi sa réponse. Je conserve les captures et je complète le journal.

## Revenir à l'ancienne version

Je reviens en arrière si la nouvelle version ne démarre pas ou échoue aux contrôles, ainsi que pour la démonstration du TP. Je redéploie l'image de l'ancien commit et je vérifie le trafic, /health et /predict. La route /hello doit disparaître après le retour à la version qui ne la contenait pas. Je garde l'ancienne image jusqu'à la fin de cette vérification.

## Journal des versions

| Date | Commit | Changement | Résultat |
|---|---|---|---|
| 27 ou 28 octobre, à préciser | 4472cdf15d5028ec0f11de0b8ef4cb363046d183 | Publication de l'image et essai Docker local | Image récupérée depuis le registre. Cela ne prouve pas son déploiement Azure. |
| 28 octobre, à confirmer | À relever dans Azure | Première mise en ligne | Captures des contrôles publics à joindre |
| 28 octobre, à confirmer | À relever dans GitHub et Azure | Ajout de /hello | Réponse publique à joindre |
| À compléter | Ancien commit à relever | Retour arrière | Ancienne image et disparition de /hello à justifier |

Si l'ancienne image n'affiche pas son commit dans /health, je le signale et je conserve sa référence visible dans Azure. Je complète les dates et résultats avec les preuves réelles.
