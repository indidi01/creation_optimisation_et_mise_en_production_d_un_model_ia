import json, pytest
from fastapi.testclient import TestClient
from app import app, DOSSIER_MODELE

@pytest.fixture
def client():
    with TestClient(app) as client_test:
        yield client_test

def test_health(client):
    reponse = client.get("/health")

    assert reponse.status_code ==200 
    contenu =reponse.json()

    assert contenu["status"] == "ok"
    assert contenu["version"] == client.app.state.version_modele

def test_prediction_valide(client):
    reponse = client.post(
        "/predict",
        json={
            "texte": (
                "A masked killer follows a group of friends "
                "inside an abandoned house."
            )
        }
    )

    assert reponse.status_code == 200
    contenu = reponse.json()

    assert contenu["classe"] in [0, 1]
    assert 0 <= contenu["probabilite"] <= 1
    assert contenu["version"] == client.app.state.version_modele

@pytest.mark.parametrize("texte", ["", "A film.", " " * 30])
def test_texte_invalide(client, texte):
    reponse = client.post("/predict", json={"texte": texte})

    assert reponse.status_code == 422
    assert "detail" in reponse.json()

def test_score_minimum():
    with open(DOSSIER_MODELE / "metrics.json", encoding="utf-8") as fichier:
        metriques = json.load(fichier)

    assert metriques["f1_test"] >= 0.82