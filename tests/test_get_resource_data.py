import re
import httpx
from jsonschema import validate
from core.contracts1 import USER_DATA_SCHEME1

BASE_URL = "https://reqres.in/"
LIST_RESOURCE = "api/unknown"
SINGLE_RESOURCE = "api/unknown/2"
SINGLE_RESOURCE_NOT_FOUND = "api/unknown/23"
COLOR_START = "#"
PANTONE_VALUE_MASK = r"^\d{2}-\d{4}$" # Регулярное выражение для формата "NN-NNNN"
YEAR_MASK = r"^\d{4}$" # Регулярное выражение для формата "YYYY"

def test_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, USER_DATA_SCHEME1)
        assert item['color'].startswith(COLOR_START)
        assert re.match(PANTONE_VALUE_MASK, item['pantone_value'])
        assert re.match(YEAR_MASK, str(item['year']))

def test_single_resource():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']
    assert data['color'].startswith(COLOR_START)
    assert re.match(YEAR_MASK, str(data['year']))

def test_resource_not_found():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE_NOT_FOUND)
    assert response.status_code == 404