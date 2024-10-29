from . import city_bp
from app.business.city import list_city
from common.response import CommonResponse


@city_bp.route('/<city_name>', methods=['GET'])
def get_city_list(city_name):
    """
    This is the city relation location info API
    Call this api passing a chinese city name and get back it's relation location info
    ---
    tags:
        - City Relation Location API
    parameters:
        - name: city_name
          in: path
          type: string
          required: true
          description: The chinese city name
    responses:
        500:
            description: Error
        200:
            description: city relation location info
            schema:
                id: location
                properties:
                    cityItems:
                        type: array
                        description: the location list
                        items:
                            type: object

    """
    return CommonResponse(data=list_city(city_name))
