import requests
from requests.structures import CaseInsensitiveDict

import os
from dotenv import load_dotenv

load_dotenv()


def get_auth_token():

    # credentials = {
    #     "user": os.getenv('USER'),
    #     "password": os.getenv('PASSWORD'),
    #     "keep_connected": True
    # }

    credentials = {
        "user": "demo_backend_api",
        "password": "Tmp1234",
        "keep_connected": True
    }

    url_token = "https://i4cast-backend.i4sea.com/v1/auth/login"

    return requests.post(url_token, json=credentials, timeout=10000000).json()


def get_headers():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {get_auth_token()['access_token']}"

    return headers


def get_stations(data):

    headers = get_headers()

    url_stations = "https://i4cast-backend.i4sea.com/v1/atmocean/getStations"

    return requests.post(url_stations, json={"region": data["region"]}, timeout=10000000, headers=headers).json()


def get_forecast_environment_data(data):

    headers = get_headers()

    url_region = "https://i4cast-backend.i4sea.com/v1/atmocean/getEnvironmentalData"

    data = {
        "station_id":  27,
        "region": data["region"],
        "data_type": "forecast",
        "environmental_type": data["environmental_type"]
    }

    return requests.post(url_region, json=data, timeout=10000000, headers=headers).json()
