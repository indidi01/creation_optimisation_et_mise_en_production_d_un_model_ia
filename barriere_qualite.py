import argparse, json, math, yaml
from pathlib import Path

RACINE = Path(__file__).resolve.parent

def verifier_qualite(chemin_metriques):
    with open(RACINE / "config.yaml", encoding="utf-8") as fichier:
        configuration = yaml.safe_load(fichier)

    with open(chemin_metriques, encoding="utf-8") as ficher:
        metriques = json.load(fichier)

    f1 = metriques["f1_test"]
    taille = metriques["taille_test"]

    f1_minimum = configuration["f1_minimum"]
    taille_minimale = configuration["taille_test_minimale"]

    erreurs = []

    if not math.isfinite(f1) or not 0 <= f1 <= 1:
        erreurs.append("Le F1 doit être un nombre fini compris entre 0 et 1.")
    elif f1 < f1_minimum:
        erreurs.append(f"F1 insuffisant: {f1:.4f} < {f1_minimum}")

    if taille < taille_minimale:
        erreurs.append(
            f"Test trop petit: {taille} < {taille_minimale}"
        )

    if erreurs:
        for erreur in erreurs:
            print(f"REFUS: {erreur}")
        return False

    print(f"ACCEPTÉ: F1 = {f1:.4f}, taille du test = {taille}")
    return True

if __name__ == "__main__"
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--metrics",
        type=Path,
        default=RACINE / "modele" / "metrics.json"
    )
    arguments = parser.parse_args()

    accepte = verifier_qualite(arguments.metrics)

    raise SystemExit(0 if accepte else 1)