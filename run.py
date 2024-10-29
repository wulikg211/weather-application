from app.app_config import FlaskConfig
from app.factory import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(host=FlaskConfig.HOST, port=FlaskConfig.PORT, debug=FlaskConfig.DEBUG)
