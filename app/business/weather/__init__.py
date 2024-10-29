import requests
from flask import abort

from app.app_config import FlaskConfig

from app.models.dto import QweatherCityWeatherResult
from app.models.vo import Weather, ListWeatherResponseData


def list_weather(location: str) -> ListWeatherResponseData:
    url = f"{FlaskConfig.QWEATHER_WEATHER_API}/?location={location}&key={FlaskConfig.QWEATHER_API_KEY}"

    weather_items = []

    response = requests.get(url)
    response.raise_for_status()

    result = QweatherCityWeatherResult(**response.json())
    if result.code == 200:
        for weatherItem in result.daily:
            temperature = f"最高{weatherItem.tempMax}°C,最低{weatherItem.tempMin}°C"
            sunlight = f"{weatherItem.textDay} ~ {weatherItem.textNight}"
            weather = Weather(fxDate=weatherItem.fxDate, temperature=temperature, sunlight=sunlight)
            weather_items.append(weather)

    res = ListWeatherResponseData(weatherItems=weather_items)

    return res


