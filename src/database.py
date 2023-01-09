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
