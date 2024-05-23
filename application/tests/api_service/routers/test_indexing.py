from fastapi.testclient import TestClient
from application.main import app

client = TestClient(app)


def test_load():
    response = client.get("/indexing/load")
    assert response.status_code == 200
    assert response.json() == {"message": "Indexing document..."}
    