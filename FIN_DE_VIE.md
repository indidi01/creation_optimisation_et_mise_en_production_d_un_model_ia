# Fin de vie du projet

Mise à jour du 28 octobre 2026. Je décide de l'arrêt et je réalise les suppressions après avoir conservé les preuves nécessaires au rendu.

## Fin de vie partielle

Une nouvelle version remplace l'ancienne, mais l'application reste disponible. Je conserve l'ancienne image et sa référence jusqu'à la vérification du retour arrière. Une fois cette étape terminée et la version en service validée, je peux retirer les versions qui ne servent plus.

## Fin de vie totale

À la fin du TP, je ferme le service et je supprime les ressources qui lui sont dédiées. Je conserve les sources, les documents et les éléments nécessaires à l'évaluation.

| Composant | Quand et comment le retirer | Ordre de retrait | Ce que je conserve | Coût si je le laisse en place |
|---|---|---|---|---|
| Application film-app et révisions | Après les contrôles et le retour arrière, supprimer l'application dans Azure | 1, après sauvegarde des preuves | Captures, URL historique, commits et résultats | Calcul et requêtes selon l'utilisation |
| Modèle reseau.keras et TF-IDF | Retirer les copies de production avec l'application et les images | 2 | Modèle local, TF-IDF, metrics.json et code nécessaires au rendu | Espace de stockage selon le support |
| Images Docker | Retirer les copies locales inutiles et supprimer les images du registre avec celui-ci | 2 | Dockerfile, références des images et preuves des tests | Stockage local et stockage dans le registre |
| Registre acrfilmsivella | Supprimer le registre après l'application | 3 | Liste des versions utilisées et coût relevé | L'offre Basic reste facturée tant que le registre existe |
| Environnement ivella | Vérifier qu'il n'héberge aucun autre service, puis le supprimer s'il est dédié au TP | 4 | Inventaire avant et après | Selon les ressources et le profil utilisés |
| Journaux associés | Identifier l'espace Log Analytics lié, conserver les preuves utiles et le supprimer seulement s'il est dédié | 5 | Extraits utiles sans secrets | Ingestion et conservation des journaux selon l'offre |
| Secrets Azure et GitHub | Retirer les trois secrets ACR du dépôt après fermeture. Les secrets de l'application sont retirés avec elle. Déconnecter Docker local du registre | 6 | Noms des secrets, sans leurs valeurs | Aucun coût direct relevé, mais des accès peuvent rester actifs |
| Dépôt et GitHub Actions | Désactiver la publication inutile et conserver le dépôt pour l'évaluation. L'archiver ensuite selon les consignes | 7 | Code, historique, documents et preuves | Stockage et exécutions selon les quotas GitHub |
| Données | Supprimer les copies temporaires et garder uniquement les données autorisées utiles à la reproduction | 7 | Provenance, données autorisées et reference.csv | Stockage selon leur emplacement |

Le groupe ivellaRG est partagé. Je le conserve avec les comptes streamvault et indianstockage. Je vérifie aussi les ressources créées lors des tentatives de déploiement pour ne pas laisser un environnement dédié inutilisé.

## Vérifier les suppressions

Avant de supprimer, je garde un inventaire, les preuves du déploiement et du retour arrière, ainsi que le relevé de coûts disponible. Après chaque retrait, je vérifie la disparition de la ressource dans Azure et je conserve une capture datée. Arrêter l'application ne suffit pas à prouver sa suppression.

Au 28 octobre, les échanges disponibles ne confirment pas la suppression de l'application, du registre ni de l'environnement. Les captures de suppression restent à joindre à ce document.

| Vérification finale | Résultat et date |
|---|---|
| film-app supprimée | À compléter |
| acrfilmsivella supprimé | À compléter |
| Environnement dédié supprimé ou conservation justifiée | À compléter |
| Journaux dédiés traités | À compléter |
| Secrets retirés et publication arrêtée | À compléter |
| Ressources des autres exercices conservées | À compléter |

## Coût final

Le 28 octobre, Cost Management ne montre pas encore de montant attribuable au registre et à l'application dans les vues consultées. Le montant des comptes de stockage et le total mensuel du groupe ne représentent pas le coût de ce projet.

Je consulterai à nouveau les dépenses après leur actualisation, sur toute la période de création à suppression, en les détaillant par ressource. Je conserverai l'export et la date du relevé, même si les ressources ont déjà été supprimées.

Coût total du TP : à compléter. Période : à compléter. Date du relevé final : à compléter. Preuve : à joindre.
