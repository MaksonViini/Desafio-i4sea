import httpx
import pytest

def test_forecast_records():
    url = "http://localhost:8080/api/forecast_records"


def test_forecast_stations_id_27():
    response = httpx.post("/stations")
    body = response.json()

    assert body["id"] == []


def test_create_propose():
    url = 'http://localhost:8080/api/propose'
    data = {
        "cnpj": "03215360000107",
        "email": "maksonvinicio7@unifei.edu.br"
    }
    response = httpx.post(url, json=data, timeout=10000000)
    assert response.status_code == 200
