import pytest
from app.factory import create_app
flask_app = create_app()


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


# city相关
def test_city_found(client):
    response = client.get('/api/v1/city/北京市')
    assert response.status_code == 200
    assert "data" in response.json
    assert "cityItems" in response.json["data"]
    assert len(response.json["data"]["cityItems"]) > 0


def test_pass_city_name_not_valid(client):
    response = client.get('/api/v1/city/北京市1')
    assert response.status_code == 500
    assert "message" in response.json
    assert response.json["message"] == "城市名称必须是全中文并且以市字结尾"


def test_city_name_not_found(client):
    response = client.get('/api/v1/city/北平市')
    assert response.status_code == 200
    assert "cityItems" in response.json["data"]
    assert len(response.json["data"]["cityItems"]) == 0


# weather相关
def test_weather_found(client):
    response = client.get('/api/v1/weather/101010100')
    assert response.status_code == 200
    assert "data" in response.json
    assert "weatherItems" in response.json["data"]
    assert len(response.json["data"]["weatherItems"]) > 0


def test_weather_not_found(client):
    response = client.get('/api/v1/weather/999999999')
    assert response.status_code == 200
    assert "data" in response.json
    assert "weatherItems" in response.json["data"]
    assert len(response.json["data"]["weatherItems"]) == 0


def test_pass_city_location_not_valid(client):
    response = client.get('/api/v1/weather/10101010a')
    assert "weatherItems" in response.json["data"]
    assert len(response.json["data"]["weatherItems"]) == 0


# 其他
def test_not_found_error(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert response.json == {'error': 'Resource not found'}


def test_raise_exception(client):
    response = client.get('/errors/raise_exception')
    assert response.status_code == 500
    assert "error" in response.json
    assert response.json["error"] == "An unexpected error occurred"
