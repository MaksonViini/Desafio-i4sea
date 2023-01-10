import json
import os


def write_json(lista, data):

    if not os.path.isdir(f"{os.path.dirname(os.path.realpath(__file__))}/output/"):
        os.mkdir(f"{os.path.dirname(os.path.realpath(__file__))}/output/")

    path = f"""{os.path.dirname(os.path.realpath(__file__))}/output/{lista['station_id']}-{data['region']}-{data['environmental_type']}.json"""

    with open(path, "w") as f:
        json.dump(lista, f)
