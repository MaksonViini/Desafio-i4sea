from fastapi import APIRouter
from starlette.responses import RedirectResponse

from ..schemas.schema import forecast_environmental_serializer, data_serializer
from ..models.model import ForecastEnvironmental, ForecastData, ForecastStation


from ..database import collection

from ..services.i4sea_api import get_stations, get_forecast_environment_data
from ..services.utils import write_json


router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)


class Basic:

    @router.get("/")
    async def main():
        return RedirectResponse(url="/docs/")

    @router.get("/status")
    async def get_status():
        return {"Status": "Ok!"}


class Records:

    @router.get("/records")
    async def get_forecast_all():
        return data_serializer(collection.find())

    # @router.get("/records_count/{id}")
    # async def get_forecast_all(_id: int):
    #     return data_serializer(collection.find({"station_id": _id}))

    @router.post("/records")
    async def create_forecast(data: ForecastEnvironmental):
        _id = collection.insert_one(dict(data))
        return data_serializer(collection.find({"_id": _id.inserted_id}))


class ForecastRecords:

    @router.post("/forecast_records")
    async def create_forecast(data: ForecastData):

        predict_environment = get_forecast_environment_data(dict(data))
        _data: ForecastEnvironmental = predict_environment
        _id = collection.insert_one(dict(_data))

        write_json(dict(_data), dict(data))

        return data_serializer(collection.find({"_id": _id.inserted_id}))

    @router.post("/stations")
    async def get_stations_id(data: ForecastStation):

        response = get_stations(dict(data))

        print(response)

        station_id_list = [station["station_id"] for station in response]

        return {"id": station_id_list}
