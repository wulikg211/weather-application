from typing import Text, List, Optional

from pydantic import BaseModel, PositiveInt, Field


class WeatherResult(BaseModel):
    fxDate: Text
    tempMax: Text
    tempMin: Text
    textDay: Text
    textNight: Text


class QweatherCityWeatherResult(BaseModel):
    code: PositiveInt
    updateTime: Optional[Text] = Field(default=None)
    fxLink: Optional[Text] = Field(default=None)
    daily: Optional[List[WeatherResult]] = Field(default=None)


class Weather(BaseModel):
    fxDate: Text
    temperature: Text
    sunlight: Text
