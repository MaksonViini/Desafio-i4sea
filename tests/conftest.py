from fastapi.testclient import TestClient
import pytest
from typing import Generator

from src.database import DATABASE_URL

from src.main import app
from pymongo import MongoClient

@pytest.fixture(scope="function")
def client() -> Generator:
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="function")
def db():
    with MongoClient(DATABASE_URL) as c:
        yield c