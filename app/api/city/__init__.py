from flask import Blueprint

city_bp = Blueprint(name="city", import_name=__name__, url_prefix="/api/city")

from app.api.city import api

