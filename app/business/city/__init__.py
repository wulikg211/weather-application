import pypinyin
import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout, TooManyRedirects
from flask import abort

from app.app_config import FlaskConfig
from app.models.dto import QweatherListCityResult
from app.models.vo import City, ListCityResponseData
from common.utils import is_validate_chinese_city


def list_city(city_name: str) -> ListCityResponseData:
    if not is_validate_chinese_city(city_name):
        raise ValueError("城市名称必须是全中文并且以市字结尾")

    location = "".join(pypinyin.lazy_pinyin(city_name))
    url = f"{FlaskConfig.QWEATHER_CITY_API}/?location={location}&key={FlaskConfig.QWEATHER_API_KEY}"

    city_items = []

    response = requests.get(url)
    response.raise_for_status()

    result = QweatherListCityResult(**response.json())
    if result.code == 200:
        for cityItem in result.location:
            if cityItem.adm2 == cityItem.name:
                full_name = f"{cityItem.adm1}-{cityItem.name}"
            else:
                full_name = f"{cityItem.adm1}-{cityItem.adm2}-{cityItem.name}"
            city = City(city_name=full_name, city_id=cityItem.id)
            city_items.append(city)

    res = ListCityResponseData(cityItems=city_items)

    return res



