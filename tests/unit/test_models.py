import pytest
from tests.utils.content import get_enter_api_data, api_forecast_content
from src.models.model import ForecastData, ForecastEnvironmental


def test_model_forecast_data():

    values = get_enter_api_data()
    fd = ForecastData(
        region="1711", environmental_type=values["environmental_type"])

    assert fd.region == values["region"]
    assert fd.environmental_type == values["environmental_type"]


def test_model_forecast_environmental():

    values = api_forecast_content()
    fe = ForecastEnvironmental(
        **values
    )

    assert fe.station_id == values["station_id"]
    assert fe.station_name == values["station_name"]
    assert fe.station_depth == values["station_depth"]
    assert fe.station_depth_unit == values["station_depth_unit"]
    assert fe.station_lat == values["station_lat"]
    assert fe.station_lon == values["station_lon"]
    assert fe.macro_region == values["macro_region"]
    assert fe.region == values["region"]
    assert fe.region_timezone == values["region_timezone"]
    assert fe.region_timezone == values["region_timezone"]
    assert fe.data_type == values["data_type"]
    assert fe.environmental_type == values["environmental_type"]
    assert fe.environmental_data == values["environmental_data"]
