import httpx
import pytest
from fastapi.testclient import TestClient
from tests.utils.content import stations_id_list


def test_forecast_stations_id_27() -> None:

    data = {
        "region": "1711",
        "environmental_type": "weather"
    }

    response = httpx.post(
        "http://localhost:8080/api/forecast_records", json=data, timeout=10000)

    body = response.json()[0]

    assert response.status_code == 200
    assert body.get("station_id") == 27


def test_get_records(client: TestClient) -> None:

    response = client.get("api/records")
    assert response.status_code == 200


def test_get_stations_id() -> None:
    data = {
        "region": "1711",
        "environmental_type": "weather"
    }

    response = httpx.post(
        "http://localhost:8080/api/stations", json=data, timeout=10000)

    body = response.json()

    assert response.status_code == 200
    assert body.get("id") == stations_id_list()
