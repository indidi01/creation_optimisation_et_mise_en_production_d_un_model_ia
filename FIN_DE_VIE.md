# Fin de vie des composants

Mise à jour : 28/10/2026. Décision et exécution : moi. Plan adapté aux ressources vues dans l'échange ; sa réalisation reste à confirmer. Aucune suppression n'est affirmée ici.

## Partielle et totale

La fin de vie partielle retire une version obsolète tout en maintenant le service et une possibilité de retour arrière jusqu'à validation. La fin de vie totale ferme le service et retire les ressources et accès dédiés. Le code et les pièces d'évaluation peuvent rester archivés : la fermeture du service n'impose pas de détruire son historique pédagogique.

Déclencheur de fermeture totale : démonstration terminée, captures du déploiement/rollback conservées et inventaire des ressources vérifié. Pas de date de suppression réalisée connue. La date du 29/10 du brouillon était une proposition, non un constat.

## Inventaire et ordre de retrait

| Composant | Fin de vie partielle : quand et comment | Fin de vie totale : ordre et méthode | Ce qui est conservé | Coût du maintien |
|---|---|---|---|---|
| Application film-app et révisions | Après validation de la nouvelle version, désactiver les anciennes révisions qui ne servent plus au trafic ni au rollback | 2. Supprimer l'application dédiée dans Azure ; contrôler sa disparition | URL historique, commits, révisions et réponses de contrôle | Calcul/requêtes selon activité et offre ; montant non relevé |
| Modèle reseau.keras, TF-IDF et métriques | Remplacer comme un ensemble cohérent, garder la version précédente jusqu'au test du rollback | 3. Retirer les copies de production avec l'application et les images ; nettoyer les copies temporaires | Artefacts locaux/dans le dépôt nécessaires à l'évaluation et à la reproductibilité | Disque ou stockage selon support ; non chiffré |
| Images films-api:<commit> | Nettoyer les versions inutilisées seulement après validation et fin du besoin de rollback | 3. Retirer les conteneurs/copies locaux inutiles ; suppression des images cloud avec le registre à l'étape 4 | Dockerfile, références/digests et preuves ; pas d'archive binaire CI permanente requise | Stockage registre/local et éventuels transferts ; non chiffré |
| Registre acrfilmsivella | Le conserver tant que le service et le retour arrière en dépendent | 4. Supprimer le registre dédié après l'application | Nom, tags/digests et relevé des coûts | Offre Basic facturée tant que le registre existe ; montant exact à relever |
| Environnement Container Apps ivella | Ne pas le retirer s'il héberge une application utile | 5. Inventorier les applications et travaux associés ; supprimer uniquement si dédié et devenu inutilisé | Inventaire avant/après | Selon profil de charge et ressources associées ; non chiffré |
| Journaux / Log Analytics | Exporter les preuves et retirer ce qui n'est plus nécessaire selon les règles de formation | 6. Vérifier l'espace associé, notamment workspaceivellarg882c visible dans le portail ; supprimer seulement si dédié et sans autre consommateur | Logs utiles nettoyés et captures ; association exacte à confirmer | Ingestion/rétention éventuelles ; montant à identifier |
| Secrets Azure et GitHub | Retirer/renouveler les identifiants devenus obsolètes | 7. Retirer ACR_LOGIN_SERVER, ACR_USERNAME, ACR_PASSWORD des secrets du dépôt après fermeture ; les secrets de l'application disparaissent avec elle ; retirer les accès locaux ACR inutiles | Noms des secrets, jamais leurs valeurs | Pas de coût direct mesuré ; accès résiduel si oubli |
| Dépôt Git et workflow | Garder les commits nécessaires au rollback ; laisser expirer les artefacts CI à un jour selon le workflow | 8. Désactiver la publication devenue inutile ; conserver le dépôt pour le rendu, l'archiver après correction/évaluation selon consignes | Sources, historique, modèles, documents et preuves autorisés | Quotas GitHub de stockage/exécution, non relevés |
| Données CSV et échantillon de référence | Retirer les copies intermédiaires inutiles | 8. Nettoyer copies temporaires ; conserver les données autorisées nécessaires au rendu, documenter leur provenance | reference.csv et données autorisées pour reproduction | Stockage local ou cloud éventuel, non chiffré |
| Groupe ivellaRG et autres projets | Aucun retrait lié à ce TP | À conserver : ne pas supprimer ivellaRG, streamvault, indianstockage ou une ressource partagée | Ressources des autres exercices | Hors périmètre de ce TP |

## Exécution

1. Sauvegarder preuves, journal des versions, inventaire et relevé des coûts disponible. Confirmer les dépendances et le caractère dédié de chaque ressource.
2. Appliquer les étapes 2 à 8 du tableau. Ne jamais supprimer le groupe partagé ivellaRG. Les ressources éventuellement créées lors des essais échoués doivent aussi être inventoriées ; leur seule présence ne prouve pas qu'elles sont dédiées et supprimables.
3. Vérifier que les ressources dédiées ont disparu ; conserver des captures datées de la liste des ressources et du journal d'activité. Une application simplement arrêtée n'est pas une application supprimée.
4. Compléter PREUVE_FIN_DE_VIE_TOTALE.md avec les résultats réels. Reconsulter Cost Management après remontée des données : la clôture ne se prouve pas par un total immédiatement nul.

## Coût observé et statut

Au 28/10, les vues de coûts partagées affichent uniquement les comptes de stockage d'autres usages sur les journées consultées. Aucun montant spécifique à ACR/Container Apps n'est identifié. Coût du TP : en attente de données, pas 0 €. Fin de vie totale : non attestée dans les éléments disponibles.
