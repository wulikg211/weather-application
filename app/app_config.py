class FlaskConfig:
    SECRET_KEY = 'owjmmdu0mjetywq1oc00zji3ltllodqtzti4ztawnwfhmzk1'

    HOST = "0.0.0.0"
    PORT = 5050
    DEBUG = True

    # 和风天气api 配置
    QWEATHER_API_KEY = 'ff264663db424b3eb93d255c71ab31c9'
    QWEATHER_CITY_API = 'https://geoapi.qweather.com/v2/city/lookup'
    QWEATHER_WEATHER_API = 'https://devapi.qweather.com/v7/weather/7d'
