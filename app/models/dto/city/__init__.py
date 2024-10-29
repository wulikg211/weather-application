from typing import Text, List, Optional

from pydantic import BaseModel, PositiveInt, Field


class QweatherCityInfo(BaseModel):
    name: Text
    id: Text
    adm1: Text
    adm2: Text
    tz: Text
    fxLink: Text


class QweatherListCityResult(BaseModel):
    code: PositiveInt
    location: Optional[List[QweatherCityInfo]] = Field(default=None)


class City(BaseModel):
    city_name: Text
    city_id: Text

