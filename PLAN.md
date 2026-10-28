# Plan du projet

Le projet consiste à entraîner un modèle qui classe les résumés de films, puis à le rendre accessible avec une API sur Azure. Je réalise le travail seul.

Ce document est mis à jour le 28 octobre 2026. Les dates de réalisation viennent de l'historique de travail. Les durées prévues viennent du premier brouillon du 22 octobre. Elles n'ont pas été chronométrées et leur validation avant le travail n'est pas établie. Les trois premières estimations ont été faites après réalisation.

## Organisation du travail

| Tâche | Dépend de | Charge estimée | Charge réelle | Ressources humaines | Ressources matérielles | Ressources techniques | Ressources financières | Date prévue | Réalisation |
|---|---|---|---|---|---|---|---|---|---|
| 1. Auditer et nettoyer les données | Aucune | 1 h, après réalisation | Non mesurée | Moi | Ordinateur personnel | Python, pandas, notebook | Coût local non chiffré | Non définie | 22 octobre |
| 2. Découper les données | 1 | 1 h, après réalisation | Non mesurée | Moi | Ordinateur personnel | scikit-learn | Coût local non chiffré | Non définie | 22 octobre |
| 3. Transformer les résumés avec TF-IDF | 2 | 1 h, après réalisation | Non mesurée | Moi | Ordinateur personnel | TfidfVectorizer | Coût local non chiffré | Non définie | 22 octobre |
| 4. Comparer et régler les modèles | 3 | 2 h | Non mesurée | Moi | Ordinateur personnel | scikit-learn, Keras, KerasTuner, Optuna | Coût local non chiffré | 22 octobre | 22 et 23 octobre |
| 5. Évaluer le modèle | 4 | 2 h | Non mesurée | Moi | Ordinateur personnel | F1, test réservé, cinq graines | Coût local non chiffré | 23 octobre | 23 octobre |
| 6. Sauvegarder et recharger le modèle | 5 | 2 h | Non mesurée | Moi | Disque local | Keras, joblib, JSON, CSV | Coût local non chiffré | 23 octobre | Sauvegarde le 23, rechargement abordé le 26 |
| 7. Développer l'API | 6 | 3 h | Non mesurée | Moi | Ordinateur personnel | FastAPI, Uvicorn, Pydantic | Coût local non chiffré | 24 octobre | 26 octobre |
| 8. Écrire les tests et la barrière qualité | 7 | 2 h | Non mesurée | Moi | Ordinateur personnel | pytest, HTTPX, PyYAML | Coût local non chiffré | 24 octobre | 26 et 27 octobre |
| 9. Construire et tester le conteneur | 8 | 2 h | Non mesurée | Moi | Ordinateur et disque local | Docker | Coût local non chiffré | 25 octobre | 27 octobre |
| 10. Automatiser les contrôles | 9 | 2 h | Non mesurée | Moi | Machine GitHub Actions | Git, GitHub Actions | Consommation GitHub non relevée | 25 octobre | 27 octobre |
| 11. Créer le registre et publier l'image | 10 | 2 h | Non mesurée | Moi | Ressources Azure | ACR Basic, secrets GitHub | Coût Azure à compléter | 26 octobre | 27 et 28 octobre |
| 12. Déployer l'application à la main | 11 | 2 h | Non mesurée | Moi | Azure, 1 vCPU et 2 Gio | Container Apps, port 8000 | Coût Azure à compléter | 27 octobre | Travail effectué le 28, preuve finale à joindre |
| 13. Ajouter une route et revenir à l'ancienne version | 12 | 2 h | Non mesurée | Moi | Ressources Azure | Route /hello, images identifiées par commit | Coût Azure à compléter | 28 octobre | Travail abordé le 28, résultats à justifier |
| 14. Relever les coûts, supprimer les ressources et finir la documentation | 13 | 3 h | Non mesurée | Moi | Ordinateur et portail Azure | Cost Management, documents Markdown | Coût final à compléter | 29 octobre | Relevé provisoire et documentation le 28, suppression à confirmer |

Le premier brouillon représentait 27 heures. Je ne peux pas donner de total réel fiable car je n'ai pas relevé mes heures. L'historique montre une activité les 22, 23, 26, 27 et 28 octobre, pas cinq journées complètes.

## Ressources et budget

J'utilise mon ordinateur, mon environnement Python, VS Code et Docker. GitHub Actions exécute les contrôles et publie l'image. Sur Azure, le projet utilise le registre acrfilmsivella, l'application film-app et l'environnement ivella.

Le groupe ivellaRG contient aussi d'autres exercices. Il ne doit pas être supprimé avec ce projet.

Une enveloppe de 30 € figurait dans le brouillon initial. Elle n'a pas été validée et ne correspond pas à une facture. Au 28 octobre, les vues de coûts consultées ne montrent pas encore de montant pour le registre et l'application. Les montants des comptes de stockage ne sont pas comptés comme des dépenses de ce TP.

## Bilan prévu et réalisé

L'API et Docker ont été abordés deux jours après les dates du brouillon. Ce décalage ne permet pas de calculer un dépassement en heures. J'ai notamment dû corriger l'environnement Python utilisé par VS Code, plusieurs erreurs de code, la configuration GitHub Actions et les paramètres Azure.

Sur Azure, l'identité managée nécessitait des droits que je n'avais pas. J'ai utilisé les identifiants administrateur du registre prévus par le TP. J'ai aussi corrigé la région, le port et l'étiquette de l'image.

Pour un prochain projet, je noterais les heures dès le début, les commits déployés et les preuves après chaque étape. Je définirais aussi les réglages de recherche dans un seul endroit pour éviter les différences entre KerasTuner et Optuna.

Il reste à joindre les preuves de mise en ligne, de retour arrière et de suppression, puis à compléter le coût final. Les charges réelles restent non mesurées.
