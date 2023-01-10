from fastapi.testclient import TestClient


def test_get_status_client(client: TestClient) -> None:

    response = client.get("/status")
    body = response.json()

    assert response.status_code == 200
    assert body["Status"] == "Ok!"


def test_get_root(client: TestClient) -> None:

    response = client.get("/")
    assert response.status_code == 200
