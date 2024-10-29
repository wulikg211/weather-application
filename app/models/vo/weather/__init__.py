from typing import List

from pydantic import BaseModel, Field

from app.models.dto import Weather


class ListWeatherResponseData(BaseModel):
    weatherItems: List[Weather] = Field(default=[])

