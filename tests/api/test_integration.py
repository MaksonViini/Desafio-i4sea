import pytest
from src.database import insert, read, update, delete, delete_
from tests.utils.content import api_forecast_content, get_my_localhost_connection, api_forecast_new_content
from pymongo import MongoClient


def test_db_connection(db: MongoClient):

    client = db.test
    assert client.name == "test"
    assert str(client.my_collection) == get_my_localhost_connection()[
        "localcon"]


def test_get_all_content():

    assert list(read()) is not None


def test_insert_content_partial():

    json = api_forecast_content()
    assert insert(**json) is None


def test_update_content():

    values_to_update = api_forecast_new_content()
    assert update(values_to_update) is None


def test_delete_content():

    assert delete({"station_id":"27"}) is None

def test_delete_many_content():
    assert delete_({"station_id":"27"}) is None
