from flask import Flask
from flasgger import Swagger

from app.app_config import FlaskConfig
from .errors import errorHandler
from .https import httpHandler


def create_app(config_class=FlaskConfig):
    """ 创建Flask应用工厂函数 """

    app = Flask(__name__)
    Swagger(app)
    app.config.from_object(config_class)
    register_blueprints(app)
    errorHandler(app)   # handle exceptions globally

    # httpHandler(app)  #http自动跳转https

    return app


def register_blueprints(app: Flask):
    from app.api.home import home_bp
    from app.api.city import city_bp
    from app.api.errors import errors_bp
    from app.api.weather import weather_bp

    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(errors_bp, url_prefix="/errors")
    app.register_blueprint(city_bp, url_prefix="/api/v1/city")
    app.register_blueprint(weather_bp, url_prefix="/api/v1/weather")

