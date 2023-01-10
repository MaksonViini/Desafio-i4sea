import requests
from requests.structures import CaseInsensitiveDict

import os
from dotenv import load_dotenv

load_dotenv()


def get_auth_token():

    credentials = {
        "user": os.getenv('USERACCESS'),
        "password": os.getenv('PASSWORD'),
        "keep_connected": True
    }
    
    url_token = os.getenv('ENDPOINT_AUTH')

    return requests.post(url_token, json=credentials, timeout=100).json()


def get_headers():
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {get_auth_token()['access_token']}"

    return headers


def get_stations(data):

    headers = get_headers()

    url_stations = os.getenv('ENDPOINT_STATIONS')

    return requests.post(url_stations, json={"region": data["region"]}, timeout=100, headers=headers).json()


def get_forecast_environment_data(data):

    headers = get_headers()

    url_region = os.getenv('ENDPOINT_REGION')

    data_ = {
        "station_id":  data["station_id"],
        "region": data["region"],
        "data_type": "forecast",
        "environmental_type": data["environmental_type"]
    }
    

    return requests.post(url_region, json=data_, timeout=100, headers=headers).json()
