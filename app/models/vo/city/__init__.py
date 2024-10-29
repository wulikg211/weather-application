from typing import List

from pydantic import BaseModel, Field

from app.models.dto import City


class ListCityResponseData(BaseModel):
    cityItems: List[City] = Field(default=[])