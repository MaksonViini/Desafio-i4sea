from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse

from ..schemas.schema import forecast_environmental_serializer, data_serializer
from ..models.model import ForecastEnvironmental, ForecastData


from ..database import collection

from ..services.i4sea_api import get_stations, get_auth_token, get_forecast_environment_data


router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)


class Basic:

    @router.get("/")
    async def main():
        return RedirectResponse(url="/docs/")

    @router.get("/hello")
    async def hello_world():
        return {"hello": "ok"}, 200


class Records:

    @router.get("/records")
    async def get_forecast_all():
        return data_serializer(collection.find())

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
        return data_serializer(collection.find({"_id": _id.inserted_id}))
