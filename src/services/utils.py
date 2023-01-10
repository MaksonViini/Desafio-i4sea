import json
import os
from google.cloud import storage


def write_json(lista, data):

    if not os.path.isdir(f"{os.path.dirname(os.path.realpath(__file__))}/output/"):
        os.mkdir(f"{os.path.dirname(os.path.realpath(__file__))}/output/")

    path = f"""{os.path.dirname(os.path.realpath(__file__))}/output/{data['station_id']}-{data['region']}-{data['environmental_type']}.json"""

    with open(path, "w") as f:
        json.dump(lista, f)


def upload_bucket():
    bucket_name = "i4sea-bucket"

    utils_path = f'{os.path.dirname(os.path.realpath(__file__))}/output/zip/'

    secrets_key = (
        f'{os.getcwd().replace("src/services", "")}terraform/secrets_key.json'
    )

    path = os.path.abspath(secrets_key)

    storage_client = storage.Client.from_service_account_json(path)

    bucket = storage_client.get_bucket(bucket_name)

    arquivos = list(os.walk(utils_path))

    for file_name in arquivos[0][2]:
        path_archive = os.path.abspath(f"{utils_path}{file_name}")
        blob = bucket.blob(file_name)
        blob.upload_from_filename(path_archive)


if __name__ == '__main__':
    upload_bucket()
