
def stations_id_list():

    return [6, 27, 16, 73, 74, 126, 125, 210, 211, 224, 259, 258, 257]


def api_forecast_content():

    return {
        "station_id": 27,
        "station_name": "POB",
        "station_depth": "null",
        "station_depth_unit": "m",
        "station_lat": -24.009433,
        "station_lon": -46.332399,
        "macro_region": "san",
        "region": "1711",
        "region_timezone": "America/Bahia",
        "data_type": "forecast",
        "environmental_type": "weather",
        "environmental_data": [
            {
                        "date": "2023-01-08T21:00:00-03:00",
                        "environmental_variable": "wind_vel",
                        "value": 10.76887321472168,
                        "units": "knots"
            }
        ]}


def api_forecast_new_content():

    return (

        {
            "station_id": 27,
            "station_name": "POB",
            "station_depth": "null",
            "station_depth_unit": "m",
            "station_lat": -24.009433,
            "station_lon": -46.332399,
            "macro_region": "san",
            "region": "1711",
            "region_timezone": "America/Bahia",
            "data_type": "forecast",
            "environmental_type": "weather",
            "environmental_data": [
                {
                    "date": "2023-01-08T21:00:00-03:00",
                    "environmental_variable": "wind_vel",
                    "value": 10.76887321472168,
                    "units": "knots"
                }
            ]},
        {"$set":
         {
             "station_id": 10000,
             "station_name": "teste",
             "station_depth": "teste",
             "station_depth_unit": "m",
             "station_lat": -24.009433,
             "station_lon": -46.332399,
             "macro_region": "teste",
             "region": "teste",
             "region_timezone": "America/Bahia",
             "data_type": "forecast",
             "environmental_type": "weather",
             "environmental_data": [
                 {
                     "date": "2023-01-08T21:00:00-03:00",
                     "environmental_variable": "wind_vel",
                     "value": 10.76887321472168,
                     "units": "knots"
                 }
             ]}})


def get_my_localhost_connection():

    return {
        "localcon": "Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'test'), 'my_collection')"
    }


def get_enter_api_data():
    
    return {
    "station_id": 27,
	"region": "1711",
	"environmental_type": "weather"
}
