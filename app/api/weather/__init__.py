from flask import Blueprint

weather_bp = Blueprint(name="weather", import_name=__name__, url_prefix="/api/weather")

from app.api.weather import api

