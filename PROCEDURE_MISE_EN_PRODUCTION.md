# Procédure de mise en production et journal des versions

Projet : API de classification de films. Mise à jour : 28/10/2026. Décideur et exécutant : moi. Ressources connues : ivellaRG (partagé), acrfilmsivella.azurecr.io, dépôt d'images films-api, application film-app. Procédure synthétique destinée à tenir sur une page à la mise en forme.

1. **Déclencheur.** Correction, nouvelle route ou nouveau modèle. Noter le changement ; conserver le commit complet et la référence de l'image actuellement déployée avant toute modification.
2. **Vérifications.** Exécuter `python barriere_qualite.py` et `python -m pytest -v`. Vérifier config.yaml (F1 minimum 0,82 ; taille minimale 400), la cohérence du modèle et de metrics.json et l'absence de secrets dans le code. Refuser la version si un contrôle échoue.
3. **Publication.** Commit puis push. Le workflow exécute test → image → publier : barrière et tests ; construction et contrôle de /health ; transfert de l'image vérifiée et publication dans ACR sous le tag du commit. Les secrets ACR_LOGIN_SERVER, ACR_USERNAME et ACR_PASSWORD permettent la connexion du robot. Attendre trois jobs verts et vérifier la présence du tag dans le registre. Une publication n'est pas une mise en ligne.
4. **Déploiement manuel.** Dans film-app, ouvrir Containers / Conteneurs et modifier/déployer une révision avec `acrfilmsivella.azurecr.io/films-api:<commit>`. Sélectionner explicitement le tag, conserver 1 vCPU, 2 Gio et l'entrée publique HTTP vers le port 8000. Utiliser les identifiants administrateur du registre stockés comme secret, selon le brief ; ne pas demander une attribution de rôle via identité managée. Conserver l'ancien tag pour le rollback.
5. **Contrôle public.** Attendre une révision saine et vérifier la répartition du trafic vers la version voulue. Sur l'URL HTTPS : /health répond 200 avec version et commit si instrumenté ; /predict renvoie classe/probabilité/version pour un texte valide, 422 pour un texte vide ou très court ; /hello apparaît uniquement dans la nouvelle version prévue. Conserver les captures et noter le résultat.
6. **Retour arrière.** Je décide le retour si l'application ne démarre pas, si les contrôles échouent ou dans le cadre de la démonstration du TP. Je redéploie l'image portant l'ancien commit ; je contrôle la révision servant le trafic, /health, /predict et la disparition de /hello (404 et absence dans /docs). Si l'ancienne image n'expose pas le commit, conserver une preuve de sa référence dans Azure et signaler cette limite. Consigner date, commit, résultat et preuve. Ne pas supprimer l'ancienne image avant le test de retour arrière.

## Journal factuel à compléter avec les preuves

| Date | Commit complet | Changement / opération | Résultat connu et preuve restante |
|---|---|---|---|
| 27–28/10, date exacte à confirmer | 4472cdf15d5028ec0f11de0b8ef4cb363046d183 | Image publiée puis utilisée pour un essai Docker local | Authentification ACR corrigée ; référence visible dans l'échange. Ce tag ne prouve pas une mise en ligne Azure. |
| 28/10, heure à relever | À relever dans Azure | Déploiement initial de film-app | Échecs droits, région puis tag manquant documentés ; révision saine et contrôles publics à joindre. |
| 28/10, heure à relever | À relever dans GitHub et Azure | Ajout /hello, suivi du commit dans /health si intégré | Publication discutée ; résultat public à confirmer par capture. |
| À confirmer | Ancien commit à relever | Retour à l'image précédente | Ne pas déclarer réussi sans preuve /hello absent et ancienne image déployée. |

Les dates de discussion ne remplacent pas les dates de déploiement. Compléter le journal depuis les commits, les révisions et les captures, sans inventer les identifiants manquants.
