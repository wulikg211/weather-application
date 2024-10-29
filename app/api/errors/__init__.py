from flask import Blueprint

errors_bp = Blueprint(name="errors", import_name=__name__, url_prefix="/errors")

from app.api.errors import api
