import json

import httpx
import pytest
from jsonschema import validate
from core.contracts import REGISTERED_USER_SCHEME

BASE_URL = "https://reqres.in/"
REGISTER_USERS = "api/register"

json_file = open('C:/Users/User/PycharmProjects/ApiTests/core/new_users_data.json') #обращаемся к json-файлу
users_data = json.load(json_file) #загружаем json-файл

@pytest.mark.parametrize('users_data', users_data) #параметризация по "users_data"
def test_successful_register(users_data):
    headers = {'Content-Type': 'aplication/json'}
    response = httpx.post(BASE_URL + REGISTER_USERS, json=users_data, headers=headers)
    assert response.status_code == 200

    validate(response.json(), REGISTERED_USER_SCHEME)


