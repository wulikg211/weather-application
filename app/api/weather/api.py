from . import weather_bp
from app.business.weather import list_weather

from common.response import CommonResponse


@weather_bp.route('/<city_location>', methods=['GET'])
def get_city_weather(city_location):
    """
    This is the city weather info API
    Call this api passing a city location and get back it's last 7 days weather info
    ---
    tags:
        - City Weather Info API
    parameters:
        - name: city_location
          in: path
          type: string
          required: true
          description: The city location
    responses:
        500:
            description: Error
        200:
            description: city weather info list
            schema:
                id: weather
                properties:
                    cityItems:
                        type: array
                        description: the weather info list
                        items:
                            type: object

    """
    return CommonResponse(data=list_weather(city_location))
