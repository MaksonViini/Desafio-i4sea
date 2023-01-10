from pymongo import MongoClient

import os
from dotenv import load_dotenv

load_dotenv()


# DATABASE_URL = f"""mongodb://root:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:
#                                                         {os.getenv('DB_PORT')}/"""
DATABASE_URL = 'mongodb://root:example@localhost:27017/'

client = MongoClient(DATABASE_URL)

database = client['forecast_i4sea']
collection = database['forecast_environmental']


def insert(**args):
    try:
        collection.insert_one(args)
    except Exception:
        return False


def read(**args):
    try:
        return collection.find(args)
    except Exception:
        return False


def update(args):
    try:
        collection.update_one(args[0], args[1])
    except Exception:
        return False


def delete(args):
    try:
        collection.delete_one(args)
    except Exception:
        return False


def delete_(args):
    try:
        collection.delete_many(args)
    except Exception:
        return False
