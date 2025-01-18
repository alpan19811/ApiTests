import json

import httpx
import pytest
from jsonschema import validate
from core.contracts import LOGIN_SUCCESSFUL_SCHEME

BASE_URL = "https://reqres.in/"
LOGIN_USERS = "api/login"

json_file = open('/core/login_successful_data.json') #обращаемся к json-файлу
users_data = json.load(json_file) #загружаем json-файл

@pytest.mark.parametrize('users_data', users_data) #параметризация по "users_data"
def test_successful_login(users_data):
    response = httpx.post(BASE_URL + LOGIN_USERS, json=users_data)
    assert response.status_code == 200

    validate(response.json(), LOGIN_SUCCESSFUL_SCHEME)