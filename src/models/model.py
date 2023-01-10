from pydantic import BaseModel, ConstrainedFloat, root_validator


class Latitude(ConstrainedFloat):
    ge = -90
    le = 90


class Longitude(ConstrainedFloat):
    ge = -180
    le = 180


class ForecastEnvironmental(BaseModel):

    station_id: int
    station_name: str
    station_depth: str
    station_depth_unit: str
    station_lat: Latitude
    station_lon: Longitude
    macro_region: str
    region: str
    region_timezone: str
    data_type: str
    environmental_type: str
    environmental_data: list

    class Config:
        orm_mode = True


class ForecastData(BaseModel):
    station_id: int
    region: str
    environmental_type: str

    @root_validator(pre=True)
    def check_data(cls, values) -> dict:

        if not any(map(str.isdigit, values["region"])) and any(
            map(str.isdigit, values["region"])
        ):
            raise TypeError("Object not valid")
        return values

    class Config:
        orm_mode = True


class ForecastStation(BaseModel):
    region: str
    environmental_type: str

    class Config:
        orm_mode = True