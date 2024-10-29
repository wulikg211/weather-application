from flask import Blueprint

home_bp = Blueprint(name="home", import_name=__name__, url_prefix="/")

from app.api.home import api

