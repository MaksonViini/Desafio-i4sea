from pydantic import BaseModel, ConstrainedFloat


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
    region: str
    environmental_type: str

    class Config:
        orm_mode = True
