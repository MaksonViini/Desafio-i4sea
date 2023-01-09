
def forecast_environmental_serializer(data) -> dict:

    return {
        "station_id": int(data["station_id"]),
        "station_name": data["station_name"],
        "station_depth": data["station_depth"],
        "station_depth_unit": data["station_depth_unit"],
        "station_lat": data["station_lat"],
        "station_lon": data["station_lon"],
        "macro_region": data["macro_region"],
        "region": data["region"],
        "region_timezone": data["region_timezone"],
        "data_type": data["data_type"],
        "environmental_type": data["environmental_type"],
        "environmental_data": list(data["environmental_data"])
    }


def data_serializer(data_all) -> list:

    return [forecast_environmental_serializer(data) for data in data_all]
