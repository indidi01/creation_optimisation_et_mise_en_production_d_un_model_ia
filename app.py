import json
import re
from contextlib import asynccontextmanager
from pathlib import Path

import joblib
import keras
from fastapi import FastAPI, Request
from pydantic import BaseModel, field_validator

DOSSIER_MODELE = Path(__file__).resolve().parent / "modele"

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.reseau = keras.models.load_model(
        DOSSIER_MODELE / "reseau.keras",
        compile=False
    )
    app.state.tfidf = joblib.load(DOSSIER_MODELE / "tfidf.joblib")

    with open(DOSSIER_MODELE / "metrics.json", encoding="utf-8") as fichier:
        metriques = json.load(fichier)

    app.state.version_modele = metriques["version_modele"]

    yield

app = FastAPI(title="Classification de films", lifespan=lifespan)

class TexteEntree(BaseModel):
    texte: str

    @field_validator("texte")
    @classmethod
    def verifier_texte(cls, valeur):
        valeur = re.sub(r"\s+", " ", valeur).strip()

        if len(valeur) < 20:
            raise ValueError(
                "Le résumé doit contenir au moins 20 caractères après nettoyage."
            )

        return valeur

@app.get("/health")
def health(request: Request):
    return {
        "status": "ok",
        "version": request.app.state.version_modele
    }

@app.post("/predict")
def predict(entree: TexteEntree, request: Request):
    ressources = request.app.state

    x = ressources.tfidf.transform([entree.texte])
    x_dense = x.toarray().astype("float32")

    probabilite_classe_1 = float(
        ressources.reseau.predict(x_dense, verbose=0).ravel()[0]
    )

    classe = int(probabilite_classe_1 >= 0.5)

    probabilite = (
        probabilite_classe_1
        if classe == 1
        else 1 - probabilite_classe_1
    )

    return {
        "classe": classe,
        "probabilite": probabilite,
        "version": ressources.version_modele
    }